from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, List

import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.auth import ExactOnlineAuth, InMemoryTokenStorage, Token
from exact_online_sdk.client import ExactOnlineClient
from exact_online_sdk.config import Settings

pytestmark = pytest.mark.e2e


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )


def test_e2e_auth_flow_and_pagination(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    storage = InMemoryTokenStorage()
    auth = ExactOnlineAuth(settings=settings, storage=storage)

    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        json={
            "access_token": "initial",
            "token_type": "Bearer",
            "refresh_token": "refresh-1",
            "expires_in": 1,
        },
    )

    token = auth.exchange_code_for_token("code123")
    assert token.access_token == "initial"
    assert storage.get_token() is not None

    expired = Token(
        access_token="initial",
        token_type="Bearer",
        refresh_token="refresh-1",
        expires_at=datetime.now(timezone.utc) - timedelta(seconds=10),
    )
    storage.set_token(expired)

    httpx_mock.add_response(
        method="POST",
        url=settings.token_url,
        json={
            "access_token": "refreshed",
            "token_type": "Bearer",
            "refresh_token": "refresh-2",
            "expires_in": 3600,
        },
    )

    first_page_url = "https://api.example/api/v1/crm/Accounts"
    second_page_url = "https://api.example/api/v1/crm/Accounts?$skiptoken=XYZ"

    httpx_mock.add_response(
        method="GET",
        url=first_page_url,
        json={
            "value": [{"ID": "1"}],
            "@odata.nextLink": second_page_url,
        },
    )
    httpx_mock.add_response(
        method="GET",
        url=second_page_url,
        json={"value": [{"ID": "2"}]},
    )

    client = ExactOnlineClient(settings=settings, auth=auth)
    pages: List[List[Any]] = list(client.iter_pages("crm/Accounts"))

    assert [item["ID"] for item in pages[0]] == ["1"]
    assert [item["ID"] for item in pages[1]] == ["2"]

    client.close()
