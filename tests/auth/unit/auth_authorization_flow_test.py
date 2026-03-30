from __future__ import annotations

from datetime import datetime, timezone

from pytest_httpx import HTTPXMock

from exact_online_sdk.auth import ExactOnlineAuth, InMemoryTokenStorage
from exact_online_sdk.config import Settings


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
    )


def test_authorization_url() -> None:
    settings = _settings()
    auth = ExactOnlineAuth(settings)

    url = auth.get_authorization_url(state="xyz", scope="crm")

    assert "response_type=code" in url
    assert "state=xyz" in url
    assert "client_id=client" in url


def test_exchange_code_for_token(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    token_json = {
        "access_token": "access",
        "token_type": "Bearer",
        "refresh_token": "refresh",
        "expires_in": 3600,
    }
    auth = ExactOnlineAuth(settings, storage=InMemoryTokenStorage())
    httpx_mock.add_response(method="POST", url=settings.token_url, json=token_json)

    token = auth.exchange_code_for_token("code123")

    assert token.access_token == "access"
    assert token.refresh_token == "refresh"
    assert token.token_type == "Bearer"
    assert token.expires_at > datetime.now(timezone.utc)
