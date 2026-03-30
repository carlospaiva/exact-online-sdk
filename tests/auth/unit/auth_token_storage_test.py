from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import pytest
from cryptography.fernet import Fernet
from pytest_httpx import HTTPXMock

from exact_online_sdk.auth import (
    EncryptedFileTokenStorage,
    ExactOnlineAuth,
    InMemoryTokenStorage,
    Token,
    TokenStorage,
)
from exact_online_sdk.config import Settings


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
    )


def test_refresh_token(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    storage = InMemoryTokenStorage()
    expired = Token(
        access_token="old",
        token_type="Bearer",
        refresh_token="refresh",
        expires_at=datetime.now(timezone.utc) - timedelta(seconds=10),
    )
    storage.set_token(expired)

    token_json = {
        "access_token": "new_access",
        "token_type": "Bearer",
        "refresh_token": "new_refresh",
        "expires_in": 3600,
    }
    auth = ExactOnlineAuth(settings, storage=storage)
    httpx_mock.add_response(method="POST", url=settings.token_url, json=token_json)

    token = auth.refresh_token()

    assert token.access_token == "new_access"
    assert token.refresh_token == "new_refresh"


def test_get_access_token_triggers_refresh(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    storage = InMemoryTokenStorage()
    expired = Token(
        access_token="old",
        token_type="Bearer",
        refresh_token="refresh",
        expires_at=datetime.now(timezone.utc) - timedelta(seconds=10),
    )
    storage.set_token(expired)
    token_json = {
        "access_token": "fresh",
        "token_type": "Bearer",
        "refresh_token": "refresh2",
        "expires_in": 3600,
    }
    auth = ExactOnlineAuth(settings, storage=storage)
    httpx_mock.add_response(method="POST", url=settings.token_url, json=token_json)

    access = auth.get_access_token()

    assert access == "fresh"


def test_in_memory_token_storage_roundtrip() -> None:
    storage = InMemoryTokenStorage()
    expires = datetime.now(timezone.utc) + timedelta(hours=1)
    token = Token(access_token="tok", token_type="Bearer", expires_at=expires)

    storage.set_token(token)
    assert storage.get_token() is token

    storage.clear()
    assert storage.get_token() is None


def test_encrypted_file_token_storage_roundtrip(tmp_path: Path) -> None:
    key = Fernet.generate_key().decode("utf-8")
    path = tmp_path / "token.enc"
    storage = EncryptedFileTokenStorage(path, key)

    expires = datetime.now(timezone.utc) + timedelta(hours=1)
    token = Token(
        access_token="tok",
        token_type="Bearer",
        refresh_token="refresh",
        expires_at=expires,
    )

    storage.set_token(token)
    loaded = storage.get_token()

    assert loaded is not None
    assert loaded.access_token == "tok"
    assert loaded.refresh_token == "refresh"

    storage.clear()
    assert storage.get_token() is None


def test_exact_online_auth_uses_encrypted_storage(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    key = Fernet.generate_key().decode("utf-8")
    expected_path = tmp_path / "secure-token.enc"
    captured: dict[str, object] = {}

    class DummyStorage(TokenStorage):
        def __init__(self, path: Path, key_b64url: str) -> None:
            captured["path"] = path
            captured["key"] = key_b64url

        def get_token(self) -> Optional[Token]:
            return None

        def set_token(self, token: Token) -> None:  # pragma: no cover - not used
            pass

        def clear(self) -> None:  # pragma: no cover - not used
            pass

    monkeypatch.setattr("exact_online_sdk.auth.EncryptedFileTokenStorage", DummyStorage)

    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        token_path=str(expected_path),
        encryption_key=key,
    )

    ExactOnlineAuth(settings)

    assert captured["path"] == expected_path
    assert captured["key"] == key
