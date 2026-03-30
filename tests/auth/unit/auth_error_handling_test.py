from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Optional

import httpx
import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.auth import (
    ExactOnlineAuth,
    InMemoryTokenStorage,
    Token,
    TokenStorage,
)
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import AuthenticationError


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        token_url="https://api.example/token",
    )


def _http_status_error(status: int) -> httpx.HTTPStatusError:
    request = httpx.Request("POST", "https://api.example/token")
    response = httpx.Response(status, request=request)
    return httpx.HTTPStatusError("error", request=request, response=response)


def test_exchange_code_for_token_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    settings = _settings()
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())

    def fake_post(*args: object, **kwargs: object) -> None:
        raise _http_status_error(400)

    monkeypatch.setattr(httpx, "post", fake_post)

    with pytest.raises(AuthenticationError):
        auth.exchange_code_for_token("bad")


def test_refresh_token_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(
        Token(
            access_token="old",
            token_type="Bearer",
            refresh_token="refresh",
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=30),
        )
    )
    auth = ExactOnlineAuth(settings, storage=storage)

    def fake_post(*args: object, **kwargs: object) -> None:
        raise _http_status_error(500)

    monkeypatch.setattr(httpx, "post", fake_post)

    with pytest.raises(AuthenticationError):
        auth.refresh_token()


def test_get_access_token_without_token_raises() -> None:
    settings = _settings()
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())

    with pytest.raises(AuthenticationError):
        auth.get_access_token()


def test_exchange_code_for_token_non_json_response(httpx_mock: HTTPXMock) -> None:
    """Test that non-JSON success responses raise AuthenticationError."""
    settings = _settings()
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())
    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        content=b"<html><body>OAuth Error</body></html>",
        headers={"Content-Type": "text/html"},
        status_code=200,
    )

    with pytest.raises(AuthenticationError) as exc_info:
        auth.exchange_code_for_token("code123")

    assert (
        "token" in str(exc_info.value).lower() or "json" in str(exc_info.value).lower()
    )


def test_exchange_code_for_token_malformed_json(httpx_mock: HTTPXMock) -> None:
    """Test that malformed JSON success responses raise AuthenticationError."""
    settings = _settings()
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())
    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        content=b'{"access_token": "test", "expires_in": }',  # Invalid JSON
        headers={"Content-Type": "application/json"},
        status_code=200,
    )

    with pytest.raises(AuthenticationError) as exc_info:
        auth.exchange_code_for_token("code123")

    assert (
        "json" in str(exc_info.value).lower() or "parse" in str(exc_info.value).lower()
    )


def test_refresh_token_non_json_response(httpx_mock: HTTPXMock) -> None:
    """Test that non-JSON success responses during refresh raise AuthenticationError."""
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(
        Token(
            access_token="old",
            token_type="Bearer",
            refresh_token="refresh",
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=30),
        )
    )
    auth = ExactOnlineAuth(settings, storage=storage)
    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        content=b"<html><body>OAuth Error</body></html>",
        headers={"Content-Type": "text/html"},
        status_code=200,
    )

    with pytest.raises(AuthenticationError) as exc_info:
        auth.refresh_token()

    assert (
        "token" in str(exc_info.value).lower() or "json" in str(exc_info.value).lower()
    )


def test_refresh_token_malformed_json(httpx_mock: HTTPXMock) -> None:
    """Test that malformed JSON success responses during refresh raise AuthenticationError."""
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(
        Token(
            access_token="old",
            token_type="Bearer",
            refresh_token="refresh",
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=30),
        )
    )
    auth = ExactOnlineAuth(settings, storage=storage)
    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        content=b'{"access_token": "test", "token_type": }',  # Invalid JSON
        headers={"Content-Type": "application/json"},
        status_code=200,
    )

    with pytest.raises(AuthenticationError) as exc_info:
        auth.refresh_token()

    assert (
        "json" in str(exc_info.value).lower() or "parse" in str(exc_info.value).lower()
    )


class _EmptyStorage(TokenStorage):
    def get_token(self) -> Optional[Token]:
        return None

    def set_token(self, token: Token) -> None:  # pragma: no cover
        pass

    def clear(self) -> None:  # pragma: no cover
        pass
