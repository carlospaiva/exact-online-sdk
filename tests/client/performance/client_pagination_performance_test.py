from __future__ import annotations

import time
from typing import Any, List

import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.client import ExactOnlineClient
from exact_online_sdk.config import Settings

pytestmark = pytest.mark.performance


class DummyAuth:
    def get_access_token(self) -> str:
        return "token"


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )


def test_iter_pages_is_fast(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    first_url = "https://api.example/api/v1/crm/Accounts"
    second_url = "https://api.example/api/v1/crm/Accounts?$skiptoken=XYZ"

    httpx_mock.add_response(
        method="GET",
        url=first_url,
        json={
            "value": [{"ID": "1"}],
            "@odata.nextLink": second_url,
        },
    )
    httpx_mock.add_response(
        method="GET",
        url=second_url,
        json={"value": [{"ID": "2"}]},
    )

    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    start = time.perf_counter()
    pages: List[List[Any]] = list(client.iter_pages("crm/Accounts"))
    elapsed = time.perf_counter() - start

    assert len(pages) == 2
    assert elapsed < 2.0

    client.close()
