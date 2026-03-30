from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.auth import ExactOnlineAuth, InMemoryTokenStorage, Token
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import AuthenticationError


def _make_settings(**overrides: object) -> Settings:
    defaults: dict[str, object] = {
        "client_id": "client",
        "client_secret": "secret",
        "redirect_uri": "https://app.example/callback",
        "base_url": "https://api.example",
        "auth_url": "https://api.example/auth",
        "token_url": "https://api.example/token",
        "timeout": 5,
    }
    defaults.update(overrides)
    return Settings(**defaults)  # type: ignore[arg-type]


def test_get_authorization_url_handles_optional_scope() -> None:
    settings = _make_settings()
    auth = ExactOnlineAuth(settings)

    scoped_url = auth.get_authorization_url(state="xyz", scope="crm")
    assert "scope=crm" in scoped_url

    url = auth.get_authorization_url(state="xyz")
    assert "scope=" not in url


def test_exchange_code_for_token_persists(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
    storage = InMemoryTokenStorage()
    auth = ExactOnlineAuth(settings, storage=storage)

    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        json={
            "access_token": "access",
            "token_type": "Bearer",
            "refresh_token": "refresh",
            "expires_in": 3600,
        },
    )

    token = auth.exchange_code_for_token("code123")

    assert token.access_token == "access"
    assert storage.get_token() is token


def test_refresh_token_requires_stored_refresh_token() -> None:
    settings = _make_settings()
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())

    with pytest.raises(AuthenticationError, match="No refresh token available"):
        auth.refresh_token()


def test_refresh_token_updates_storage(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
    storage = InMemoryTokenStorage()
    storage.set_token(
        Token(
            access_token="old",
            token_type="Bearer",
            refresh_token="refresh",
            expires_at=datetime.now(timezone.utc) - timedelta(hours=1),
        )
    )
    auth = ExactOnlineAuth(settings, storage=storage)

    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        json={
            "access_token": "new",
            "token_type": "Bearer",
            "refresh_token": "new-refresh",
            "expires_in": 3600,
        },
    )

    token = auth.refresh_token()
    assert token.access_token == "new"
    assert storage.get_token() is token


def test_get_access_token_refreshes_when_expired(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
    storage = InMemoryTokenStorage()
    storage.set_token(
        Token(
            access_token="old",
            token_type="Bearer",
            refresh_token="refresh",
            expires_at=datetime.now(timezone.utc) - timedelta(seconds=1),
        )
    )
    auth = ExactOnlineAuth(settings, storage=storage)

    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        json={
            "access_token": "fresh",
            "token_type": "Bearer",
            "refresh_token": "refresh",
            "expires_in": 3600,
        },
    )

    token = auth.get_access_token()
    assert token == "fresh"


def test_get_access_token_requires_token() -> None:
    settings = _make_settings()
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())

    with pytest.raises(AuthenticationError, match="No access token"):
        auth.get_access_token()


@pytest.mark.asyncio
async def test_async_exchange_code_for_token(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
    storage = InMemoryTokenStorage()
    auth = ExactOnlineAuth(settings, storage=storage)

    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        json={
            "access_token": "async",
            "token_type": "Bearer",
            "refresh_token": "refresh",
            "expires_in": 3600,
        },
    )

    token = await auth.aexchange_code_for_token("code123")

    assert token.access_token == "async"
    assert storage.get_token() is token


@pytest.mark.asyncio
async def test_async_get_access_token_refreshes(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
    storage = InMemoryTokenStorage()
    storage.set_token(
        Token(
            access_token="old",
            token_type="Bearer",
            refresh_token="refresh",
            expires_at=datetime.now(timezone.utc) - timedelta(seconds=1),
        )
    )
    auth = ExactOnlineAuth(settings, storage=storage)

    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        json={
            "access_token": "async-fresh",
            "token_type": "Bearer",
            "refresh_token": "refresh",
            "expires_in": 3600,
        },
    )

    token = await auth.aget_access_token()
    assert token == "async-fresh"


@pytest.mark.asyncio
async def test_async_exchange_code_for_token_non_json(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
    storage = InMemoryTokenStorage()
    auth = ExactOnlineAuth(settings, storage=storage)
    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        content=b"<html><body>OAuth Error</body></html>",
        headers={"Content-Type": "text/html"},
        status_code=200,
    )

    with pytest.raises(AuthenticationError) as exc_info:
        await auth.aexchange_code_for_token("code123")

    assert (
        "token" in str(exc_info.value).lower() or "json" in str(exc_info.value).lower()
    )


@pytest.mark.asyncio
async def test_async_exchange_code_for_token_malformed_json(
    httpx_mock: HTTPXMock,
) -> None:
    settings = _make_settings()
    storage = InMemoryTokenStorage()
    auth = ExactOnlineAuth(settings, storage=storage)
    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        content=b'{"access_token": "test", "expires_in": }',
        headers={"Content-Type": "application/json"},
        status_code=200,
    )

    with pytest.raises(AuthenticationError) as exc_info:
        await auth.aexchange_code_for_token("code123")

    assert (
        "json" in str(exc_info.value).lower() or "parse" in str(exc_info.value).lower()
    )


@pytest.mark.asyncio
async def test_async_refresh_token_non_json(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
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
        await auth.arefresh_token()

    assert (
        "token" in str(exc_info.value).lower() or "json" in str(exc_info.value).lower()
    )


@pytest.mark.asyncio
async def test_async_refresh_token_malformed_json(httpx_mock: HTTPXMock) -> None:
    settings = _make_settings()
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
        content=b'{"access_token": "test", "token_type": }',
        headers={"Content-Type": "application/json"},
        status_code=200,
    )

    with pytest.raises(AuthenticationError) as exc_info:
        await auth.arefresh_token()

    assert (
        "json" in str(exc_info.value).lower() or "parse" in str(exc_info.value).lower()
    )
