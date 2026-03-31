from __future__ import annotations

import asyncio
import base64
import json
import os
import threading
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional, Protocol, runtime_checkable

import httpx
from cryptography.fernet import Fernet

from .config import Settings
from .exceptions import AuthenticationError
from .utils.logger import get_logger


@dataclass
class Token:
    access_token: str
    token_type: str
    expires_at: datetime
    refresh_token: Optional[str] = None

    @property
    def expired(self) -> bool:
        # Refresh slightly before expiry
        return datetime.now(timezone.utc) >= (self.expires_at - timedelta(seconds=60))

    @staticmethod
    def from_token_response(data: dict[str, Any]) -> "Token":
        try:
            access_token = str(data["access_token"])
            token_type = str(data.get("token_type", "Bearer"))
            refresh_token = data.get("refresh_token")
            expires_in = int(data.get("expires_in", 3600))
            expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
        except Exception as exc:  # pragma: no cover
            raise AuthenticationError("Invalid token response") from exc
        return Token(
            access_token=access_token,
            token_type=token_type,
            refresh_token=str(refresh_token) if refresh_token else None,
            expires_at=expires_at,
        )


@runtime_checkable
class SyncAuthProtocol(Protocol):
    def get_access_token(self) -> str: ...


@runtime_checkable
class AsyncAuthProtocol(Protocol):
    async def aget_access_token(self) -> str: ...


class TokenStorage:
    def get_token(self) -> Optional[Token]:  # pragma: no cover - interface
        raise NotImplementedError

    def set_token(self, token: Token) -> None:  # pragma: no cover - interface
        raise NotImplementedError

    def clear(self) -> None:  # pragma: no cover - interface
        raise NotImplementedError


class InMemoryTokenStorage(TokenStorage):
    def __init__(self) -> None:
        self._token: Optional[Token] = None
        self._lock = threading.Lock()

    def get_token(self) -> Optional[Token]:
        with self._lock:
            return self._token

    def set_token(self, token: Token) -> None:
        with self._lock:
            self._token = token

    def clear(self) -> None:
        with self._lock:
            self._token = None


class EncryptedFileTokenStorage(TokenStorage):
    def __init__(self, path: Path, key_b64url: str) -> None:
        self._path = path
        self._fernet = Fernet(key_b64url.encode("utf-8"))
        self._lock = threading.Lock()

    def get_token(self) -> Optional[Token]:
        with self._lock:
            if not self._path.exists():
                return None
            try:
                raw = self._path.read_bytes()
                data = json.loads(self._fernet.decrypt(raw).decode("utf-8"))
                return Token(
                    access_token=data["access_token"],
                    token_type=data.get("token_type", "Bearer"),
                    refresh_token=data.get("refresh_token"),
                    expires_at=datetime.fromisoformat(data["expires_at"]),
                )
            except Exception:  # pragma: no cover - safest fallback
                return None

    def set_token(self, token: Token) -> None:
        with self._lock:
            payload = {
                "access_token": token.access_token,
                "token_type": token.token_type,
                "refresh_token": token.refresh_token,
                "expires_at": token.expires_at.isoformat(),
            }
            enc = self._fernet.encrypt(json.dumps(payload).encode("utf-8"))
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._path.write_bytes(enc)

    def clear(self) -> None:
        with self._lock:
            try:
                self._path.unlink()
            except FileNotFoundError:
                pass


class ExactOnlineAuth:
    """OAuth2 handler for Exact Online.

    Supports authorization-code flow and refresh tokens.
    Thread-safe: sync methods use a ``threading.RLock``; async methods
    use an ``asyncio.Lock`` to serialise token operations.
    """

    def __init__(
        self, settings: Settings, *, storage: Optional[TokenStorage] = None
    ) -> None:
        self._settings = settings
        self._logger = get_logger(__name__)
        self._lock = threading.RLock()
        self._async_lock = asyncio.Lock()
        if storage is not None:
            self._storage = storage
        else:
            if settings.encryption_key and settings.token_path:
                self._storage = EncryptedFileTokenStorage(
                    path=Path(os.path.expanduser(settings.token_path)),
                    key_b64url=settings.encryption_key,
                )
            else:
                self._storage = InMemoryTokenStorage()

    # ----- Authorization URL -----
    def get_authorization_url(self, state: str, scope: Optional[str] = None) -> str:
        """Build the authorization URL for the Authorization Code flow.

        Args:
            state: CSRF token to be returned by the authorization server.
            scope: Optional OAuth2 scope string.

        Returns:
            A fully-qualified authorization URL.
        """
        import urllib.parse as _u

        query = {
            "client_id": self._settings.client_id,
            "redirect_uri": self._settings.redirect_uri,
            "response_type": "code",
            "state": state,
        }
        if scope:
            query["scope"] = scope
        return f"{self._settings.auth_url}?{_u.urlencode(query)}"

    # ----- Token Handling -----
    def _basic_auth_header(self) -> str:
        pair = f"{self._settings.client_id}:{self._settings.client_secret}".encode(
            "utf-8"
        )
        return "Basic " + base64.b64encode(pair).decode("ascii")

    def exchange_code_for_token(self, code: str) -> Token:
        """Exchange an authorization code for an access/refresh token pair.

        Raises:
            AuthenticationError: If the token endpoint returns an error.
        """
        with self._lock:
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": self._settings.redirect_uri,
            }
            headers = {
                "Authorization": self._basic_auth_header(),
                "Accept": "application/json",
            }
            try:
                resp = httpx.post(
                    self._settings.token_url,
                    data=data,
                    headers=headers,
                    timeout=self._settings.timeout,
                )
                resp.raise_for_status()
                try:
                    token_data = resp.json()
                except Exception as exc:
                    content_type = resp.headers.get("Content-Type", "unknown")
                    raise AuthenticationError(
                        "Token exchange failed: invalid JSON response "
                        f"(Content-Type: {content_type})"
                    ) from exc
                token = Token.from_token_response(token_data)
                self._storage.set_token(token)
                return token
            except httpx.HTTPStatusError as exc:
                raise AuthenticationError(f"Token exchange failed: {exc}") from exc

    def refresh_token(self) -> Token:
        """Refresh the current access token using the stored refresh token."""
        with self._lock:
            current = self._storage.get_token()
            if not current or not current.refresh_token:
                raise AuthenticationError("No refresh token available")
            data = {
                "grant_type": "refresh_token",
                "refresh_token": current.refresh_token,
            }
            headers = {
                "Authorization": self._basic_auth_header(),
                "Accept": "application/json",
            }
            try:
                resp = httpx.post(
                    self._settings.token_url,
                    data=data,
                    headers=headers,
                    timeout=self._settings.timeout,
                )
                resp.raise_for_status()
                try:
                    token_data = resp.json()
                except Exception as exc:
                    content_type = resp.headers.get("Content-Type", "unknown")
                    raise AuthenticationError(
                        "Token refresh failed: invalid JSON response "
                        f"(Content-Type: {content_type})"
                    ) from exc
                token = Token.from_token_response(token_data)
                self._storage.set_token(token)
                return token
            except httpx.HTTPStatusError as exc:
                raise AuthenticationError(f"Token refresh failed: {exc}") from exc

    def get_access_token(self) -> str:
        """Return a valid access token, refreshing if necessary."""
        with self._lock:
            token = self._storage.get_token()
            if token is None:
                raise AuthenticationError(
                    "No access token. Acquire via authorization code flow."
                )
            if token.expired:
                token = self.refresh_token()
            return token.access_token

    # Async variants
    async def aexchange_code_for_token(self, code: str) -> Token:
        """Async variant of `exchange_code_for_token`."""
        async with self._async_lock:
            async with httpx.AsyncClient(timeout=self._settings.timeout) as client:
                data = {
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": self._settings.redirect_uri,
                }
                headers = {
                    "Authorization": self._basic_auth_header(),
                    "Accept": "application/json",
                }
                try:
                    resp = await client.post(
                        self._settings.token_url, data=data, headers=headers
                    )
                    resp.raise_for_status()
                    try:
                        token_data = resp.json()
                    except Exception as exc:
                        content_type = resp.headers.get("Content-Type", "unknown")
                        raise AuthenticationError(
                            "Token exchange failed: invalid JSON response "
                            f"(Content-Type: {content_type})"
                        ) from exc
                    token = Token.from_token_response(token_data)
                    self._storage.set_token(token)
                    return token
                except httpx.HTTPStatusError as exc:  # pragma: no cover
                    raise AuthenticationError(f"Token exchange failed: {exc}") from exc

    async def _arefresh_token_unlocked(self) -> Token:
        """Refresh token without acquiring the async lock (caller must hold it)."""
        current = self._storage.get_token()
        if not current or not current.refresh_token:
            raise AuthenticationError("No refresh token available")
        async with httpx.AsyncClient(timeout=self._settings.timeout) as client:
            data = {
                "grant_type": "refresh_token",
                "refresh_token": current.refresh_token,
            }
            headers = {
                "Authorization": self._basic_auth_header(),
                "Accept": "application/json",
            }
            try:
                resp = await client.post(
                    self._settings.token_url, data=data, headers=headers
                )
                resp.raise_for_status()
                try:
                    token_data = resp.json()
                except Exception as exc:
                    content_type = resp.headers.get("Content-Type", "unknown")
                    raise AuthenticationError(
                        "Token refresh failed: invalid JSON response "
                        f"(Content-Type: {content_type})"
                    ) from exc
                token = Token.from_token_response(token_data)
                self._storage.set_token(token)
                return token
            except httpx.HTTPStatusError as exc:  # pragma: no cover
                raise AuthenticationError(f"Token refresh failed: {exc}") from exc

    async def arefresh_token(self) -> Token:
        """Async variant of `refresh_token`."""
        async with self._async_lock:
            return await self._arefresh_token_unlocked()

    async def aget_access_token(self) -> str:
        """Async variant of `get_access_token`."""
        async with self._async_lock:
            token = self._storage.get_token()
            if token is None:
                raise AuthenticationError(
                    "No access token. Acquire via authorization code flow."
                )
            if token.expired:
                token = await self._arefresh_token_unlocked()
            return token.access_token
