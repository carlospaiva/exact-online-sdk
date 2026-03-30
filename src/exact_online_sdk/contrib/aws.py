from __future__ import annotations

import json
import threading
from datetime import datetime
from typing import Any, Optional

from ..auth import Token, TokenStorage
from ..exceptions import AuthenticationError

try:
    import boto3
    import boto3.session
    from botocore.exceptions import ClientError
except ImportError as _imp_err:
    raise ImportError(
        "boto3 is required for SecretsManagerTokenStorage. "
        "Install it with:  pip install exact-online-sdk[aws]"
    ) from _imp_err


class SecretsManagerTokenStorage(TokenStorage):
    """Thread-safe token storage backed by AWS Secrets Manager.

    Creates a fresh ``boto3`` Secrets Manager client per call to avoid
    sharing non-thread-safe clients across threads.  All public methods
    are serialised with a ``threading.Lock``.

    Args:
        secret_id: The name or ARN of the secret in AWS Secrets Manager.
        region_name: AWS region (default ``"eu-west-1"``).
        session: Optional pre-configured ``boto3.Session``.  When
            provided the *region_name* argument is ignored and the
            session's region is used instead.
    """

    def __init__(
        self,
        secret_id: str,
        *,
        region_name: str = "eu-west-1",
        session: Optional[boto3.session.Session] = None,
    ) -> None:
        self._secret_id = secret_id
        self._session = session or boto3.session.Session(region_name=region_name)
        self._lock = threading.Lock()

    # -- helpers -------------------------------------------------------------

    def _client(self) -> Any:
        """Return a fresh Secrets Manager client from the session."""
        return self._session.client("secretsmanager")

    @staticmethod
    def _serialize_token(token: Token) -> str:
        payload = {
            "access_token": token.access_token,
            "token_type": token.token_type,
            "refresh_token": token.refresh_token,
            "expires_at": token.expires_at.isoformat(),
        }
        return json.dumps(payload)

    @staticmethod
    def _deserialize_token(raw: str) -> Token:
        data = json.loads(raw)
        return Token(
            access_token=data["access_token"],
            token_type=data.get("token_type", "Bearer"),
            refresh_token=data.get("refresh_token"),
            expires_at=datetime.fromisoformat(data["expires_at"]),
        )

    # -- TokenStorage interface ----------------------------------------------

    def get_token(self) -> Optional[Token]:
        """Retrieve the token from AWS Secrets Manager.

        Returns ``None`` when the secret does not exist.

        Raises:
            AuthenticationError: On unexpected AWS errors.
        """
        with self._lock:
            try:
                resp = self._client().get_secret_value(SecretId=self._secret_id)
                return self._deserialize_token(resp["SecretString"])
            except ClientError as exc:
                code = exc.response["Error"]["Code"]
                if code == "ResourceNotFoundException":
                    return None
                raise AuthenticationError(f"AWS Secrets Manager error: {exc}") from exc

    def set_token(self, token: Token) -> None:
        """Store the token in AWS Secrets Manager.

        Creates the secret automatically on first use.

        Raises:
            AuthenticationError: On unexpected AWS errors.
        """
        with self._lock:
            secret_string = self._serialize_token(token)
            client = self._client()
            try:
                client.put_secret_value(
                    SecretId=self._secret_id,
                    SecretString=secret_string,
                )
            except ClientError as exc:
                code = exc.response["Error"]["Code"]
                if code == "ResourceNotFoundException":
                    try:
                        client.create_secret(
                            Name=self._secret_id,
                            SecretString=secret_string,
                        )
                    except ClientError as create_exc:
                        raise AuthenticationError(
                            f"AWS Secrets Manager error: {create_exc}"
                        ) from create_exc
                else:
                    raise AuthenticationError(
                        f"AWS Secrets Manager error: {exc}"
                    ) from exc

    def clear(self) -> None:
        """Delete the secret from AWS Secrets Manager.

        Silently succeeds when the secret does not exist.

        Raises:
            AuthenticationError: On unexpected AWS errors.
        """
        with self._lock:
            try:
                self._client().delete_secret(
                    SecretId=self._secret_id,
                    ForceDeleteWithoutRecovery=True,
                )
            except ClientError as exc:
                code = exc.response["Error"]["Code"]
                if code == "ResourceNotFoundException":
                    return
                raise AuthenticationError(f"AWS Secrets Manager error: {exc}") from exc


class ReadOnlyTokenStorage(TokenStorage):
    """Read-only wrapper around any ``TokenStorage`` backend.

    Delegates ``get_token()`` to the wrapped storage but raises
    ``AuthenticationError`` on ``set_token()`` and ``clear()``.

    This enforces the **single-writer pattern** for multi-container
    deployments: only a dedicated refresh process (e.g. an AWS Lambda)
    should write tokens, while worker containers use this wrapper to
    guarantee they never accidentally trigger a token refresh.

    Example::

        inner = SecretsManagerTokenStorage("my-app/exact-online/oauth-token")
        storage = ReadOnlyTokenStorage(inner)
        auth = ExactOnlineAuth(settings, storage=storage)
        # auth.get_access_token() reads from Secrets Manager
        # auth.refresh_token() raises AuthenticationError
    """

    def __init__(self, inner: TokenStorage) -> None:
        self._inner = inner

    def get_token(self) -> Optional[Token]:
        """Retrieve the token from the wrapped storage."""
        return self._inner.get_token()

    def set_token(self, token: Token) -> None:
        """Always raises — writes are not permitted in read-only mode.

        Raises:
            AuthenticationError: Always.
        """
        raise AuthenticationError(
            "Token storage is read-only. "
            "Writes must go through the dedicated refresh process. "
            "Check that your token-refresh Lambda or flow is running."
        )

    def clear(self) -> None:
        """Always raises — clearing is not permitted in read-only mode.

        Raises:
            AuthenticationError: Always.
        """
        raise AuthenticationError(
            "Token storage is read-only. "
            "Writes must go through the dedicated refresh process. "
            "Check that your token-refresh Lambda or flow is running."
        )
