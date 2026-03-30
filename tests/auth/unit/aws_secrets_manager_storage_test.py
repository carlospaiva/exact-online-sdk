from __future__ import annotations

import json
import threading
from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from unittest.mock import MagicMock, patch

import pytest

from exact_online_sdk.auth import Token
from exact_online_sdk.contrib.aws import (
    ReadOnlyTokenStorage,
    SecretsManagerTokenStorage,
)
from exact_online_sdk.exceptions import AuthenticationError

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_client_error(code: str, message: str = "err") -> Any:
    """Build a botocore ClientError with the given error code."""
    from botocore.exceptions import ClientError

    return ClientError(
        {"Error": {"Code": code, "Message": message}},
        "TestOperation",
    )


def _token(*, expired: bool = False) -> Token:
    offset = timedelta(minutes=-5) if expired else timedelta(hours=1)
    return Token(
        access_token="access-123",
        token_type="Bearer",
        refresh_token="refresh-456",
        expires_at=datetime.now(timezone.utc) + offset,
    )


def _mock_session(
    mock_client: Optional[MagicMock] = None,
) -> MagicMock:
    """Return a mock boto3.Session whose .client() returns *mock_client*."""
    session = MagicMock()
    session.client.return_value = mock_client or MagicMock()
    return session


# ---------------------------------------------------------------------------
# Roundtrip
# ---------------------------------------------------------------------------


def test_roundtrip() -> None:
    """set_token → get_token returns the same data."""
    sm_client = MagicMock()
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("my/secret", session=session)

    tok = _token()

    # set_token succeeds (no exception from put_secret_value)
    storage.set_token(tok)
    sm_client.put_secret_value.assert_called_once()

    # Capture what was stored to return it from get_secret_value
    stored = sm_client.put_secret_value.call_args[1]["SecretString"]
    sm_client.get_secret_value.return_value = {"SecretString": stored}

    loaded = storage.get_token()
    assert loaded is not None
    assert loaded.access_token == tok.access_token
    assert loaded.token_type == tok.token_type
    assert loaded.refresh_token == tok.refresh_token
    assert loaded.expires_at.isoformat() == tok.expires_at.isoformat()


# ---------------------------------------------------------------------------
# get_token — missing secret
# ---------------------------------------------------------------------------


def test_get_token_missing_secret_returns_none() -> None:
    sm_client = MagicMock()
    sm_client.get_secret_value.side_effect = _make_client_error(
        "ResourceNotFoundException"
    )
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("missing/secret", session=session)

    assert storage.get_token() is None


def test_get_token_unexpected_error_raises() -> None:
    sm_client = MagicMock()
    sm_client.get_secret_value.side_effect = _make_client_error(
        "AccessDeniedException", "not allowed"
    )
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("denied/secret", session=session)

    with pytest.raises(AuthenticationError, match="AWS Secrets Manager error"):
        storage.get_token()


# ---------------------------------------------------------------------------
# set_token — auto-create on first use
# ---------------------------------------------------------------------------


def test_set_token_creates_secret_on_first_use() -> None:
    sm_client = MagicMock()
    sm_client.put_secret_value.side_effect = _make_client_error(
        "ResourceNotFoundException"
    )
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("new/secret", session=session)

    storage.set_token(_token())

    sm_client.create_secret.assert_called_once()
    call_kwargs = sm_client.create_secret.call_args[1]
    assert call_kwargs["Name"] == "new/secret"
    data = json.loads(call_kwargs["SecretString"])
    assert data["access_token"] == "access-123"


def test_set_token_create_secret_failure_raises() -> None:
    sm_client = MagicMock()
    sm_client.put_secret_value.side_effect = _make_client_error(
        "ResourceNotFoundException"
    )
    sm_client.create_secret.side_effect = _make_client_error(
        "AccessDeniedException", "cannot create"
    )
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("new/secret", session=session)

    with pytest.raises(AuthenticationError, match="AWS Secrets Manager error"):
        storage.set_token(_token())


def test_set_token_unexpected_put_error_raises() -> None:
    sm_client = MagicMock()
    sm_client.put_secret_value.side_effect = _make_client_error(
        "InternalServiceError", "boom"
    )
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("bad/secret", session=session)

    with pytest.raises(AuthenticationError, match="AWS Secrets Manager error"):
        storage.set_token(_token())


# ---------------------------------------------------------------------------
# clear
# ---------------------------------------------------------------------------


def test_clear_deletes_secret() -> None:
    sm_client = MagicMock()
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("my/secret", session=session)

    storage.clear()

    sm_client.delete_secret.assert_called_once_with(
        SecretId="my/secret",
        ForceDeleteWithoutRecovery=True,
    )


def test_clear_handles_missing_secret() -> None:
    sm_client = MagicMock()
    sm_client.delete_secret.side_effect = _make_client_error(
        "ResourceNotFoundException"
    )
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("gone/secret", session=session)

    storage.clear()  # should not raise


def test_clear_unexpected_error_raises() -> None:
    sm_client = MagicMock()
    sm_client.delete_secret.side_effect = _make_client_error(
        "AccessDeniedException", "denied"
    )
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("denied/secret", session=session)

    with pytest.raises(AuthenticationError, match="AWS Secrets Manager error"):
        storage.clear()


# ---------------------------------------------------------------------------
# Thread-safety
# ---------------------------------------------------------------------------


def test_concurrent_set_and_get() -> None:
    """Multiple threads calling set_token / get_token must not corrupt state."""
    sm_client = MagicMock()
    session = _mock_session(sm_client)
    storage = SecretsManagerTokenStorage("mt/secret", session=session)

    # get_secret_value returns whatever was last stored
    latest: dict[str, str] = {}

    def fake_put(**kwargs: Any) -> None:
        latest["data"] = kwargs["SecretString"]

    def fake_get(**kwargs: Any) -> dict[str, str]:
        return {"SecretString": latest.get("data", "{}")}

    sm_client.put_secret_value.side_effect = fake_put
    sm_client.get_secret_value.side_effect = fake_get

    errors: list[Exception] = []

    def worker(i: int) -> None:
        try:
            tok = Token(
                access_token=f"tok-{i}",
                token_type="Bearer",
                refresh_token=f"ref-{i}",
                expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
            )
            storage.set_token(tok)
            result = storage.get_token()
            assert result is not None
            assert result.access_token.startswith("tok-")
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []


# ---------------------------------------------------------------------------
# Import guard
# ---------------------------------------------------------------------------


def test_import_error_without_boto3() -> None:
    """Importing the module without boto3 installed raises ImportError."""
    import importlib
    import sys

    # Temporarily remove boto3 from sys.modules
    saved_modules: dict[str, Any] = {}
    for mod_name in list(sys.modules):
        if mod_name == "boto3" or mod_name.startswith("boto3."):
            saved_modules[mod_name] = sys.modules.pop(mod_name)

    # Also remove the cached contrib.aws module so it re-imports
    contrib_aws_key = "exact_online_sdk.contrib.aws"
    saved_contrib = sys.modules.pop(contrib_aws_key, None)

    import builtins

    original_import = builtins.__import__

    def mock_import(name: str, *args: Any, **kwargs: Any) -> Any:
        if name == "boto3" or name.startswith("boto3."):
            raise ImportError("No module named 'boto3'")
        return original_import(name, *args, **kwargs)

    try:
        builtins.__import__ = mock_import
        with pytest.raises(ImportError, match="boto3 is required"):
            importlib.import_module(contrib_aws_key)
    finally:
        builtins.__import__ = original_import
        # Restore all removed modules
        sys.modules.update(saved_modules)
        if saved_contrib is not None:
            sys.modules[contrib_aws_key] = saved_contrib


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------


def test_serialize_deserialize_token() -> None:
    tok = _token()
    raw = SecretsManagerTokenStorage._serialize_token(tok)
    loaded = SecretsManagerTokenStorage._deserialize_token(raw)

    assert loaded.access_token == tok.access_token
    assert loaded.token_type == tok.token_type
    assert loaded.refresh_token == tok.refresh_token
    assert loaded.expires_at.isoformat() == tok.expires_at.isoformat()


def test_deserialize_token_minimal_fields() -> None:
    """Deserialization works with only required fields."""
    data = json.dumps(
        {
            "access_token": "min-tok",
            "expires_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    tok = SecretsManagerTokenStorage._deserialize_token(data)
    assert tok.access_token == "min-tok"
    assert tok.token_type == "Bearer"
    assert tok.refresh_token is None


# ---------------------------------------------------------------------------
# Constructor — default session creation
# ---------------------------------------------------------------------------


def test_constructor_creates_default_session() -> None:
    with patch("exact_online_sdk.contrib.aws.boto3.session.Session") as mock_cls:
        mock_cls.return_value = MagicMock()
        storage = SecretsManagerTokenStorage("my/secret", region_name="us-east-1")
        mock_cls.assert_called_once_with(region_name="us-east-1")
        assert storage._secret_id == "my/secret"


def test_constructor_uses_provided_session() -> None:
    session = MagicMock()
    storage = SecretsManagerTokenStorage("my/secret", session=session)
    assert storage._session is session


# ---------------------------------------------------------------------------
# ReadOnlyTokenStorage
# ---------------------------------------------------------------------------


def test_readonly_get_token_delegates() -> None:
    """get_token() passes through to the inner storage."""
    sm_client = MagicMock()
    session = _mock_session(sm_client)
    inner = SecretsManagerTokenStorage("my/secret", session=session)

    tok = _token()
    raw = SecretsManagerTokenStorage._serialize_token(tok)
    sm_client.get_secret_value.return_value = {"SecretString": raw}

    storage = ReadOnlyTokenStorage(inner)
    result = storage.get_token()

    assert result is not None
    assert result.access_token == tok.access_token


def test_readonly_get_token_returns_none() -> None:
    """get_token() returns None when inner storage has no token."""
    sm_client = MagicMock()
    sm_client.get_secret_value.side_effect = _make_client_error(
        "ResourceNotFoundException"
    )
    session = _mock_session(sm_client)
    inner = SecretsManagerTokenStorage("missing/secret", session=session)

    storage = ReadOnlyTokenStorage(inner)
    assert storage.get_token() is None


def test_readonly_set_token_raises() -> None:
    """set_token() always raises AuthenticationError."""
    inner = MagicMock()
    storage = ReadOnlyTokenStorage(inner)

    with pytest.raises(AuthenticationError, match="read-only"):
        storage.set_token(_token())

    inner.set_token.assert_not_called()


def test_readonly_clear_raises() -> None:
    """clear() always raises AuthenticationError."""
    inner = MagicMock()
    storage = ReadOnlyTokenStorage(inner)

    with pytest.raises(AuthenticationError, match="read-only"):
        storage.clear()

    inner.clear.assert_not_called()
