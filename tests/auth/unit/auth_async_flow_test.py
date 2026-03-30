from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from exact_online_sdk.auth import (
    ExactOnlineAuth,
    InMemoryTokenStorage,
    Token,
)
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import AuthenticationError


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
    )


@pytest.mark.asyncio
async def test_arefresh_token_missing_refresh_raises() -> None:
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(
        Token(
            access_token="tok",
            token_type="Bearer",
            refresh_token=None,
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=5),
        )
    )
    auth = ExactOnlineAuth(settings, storage=storage)

    with pytest.raises(AuthenticationError):
        await auth.arefresh_token()


@pytest.mark.asyncio
async def test_aget_access_token_requires_token() -> None:
    settings = _settings()
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())

    with pytest.raises(AuthenticationError):
        await auth.aget_access_token()
