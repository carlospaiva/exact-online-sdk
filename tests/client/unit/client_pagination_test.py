from __future__ import annotations

from typing import Any, List
from unittest.mock import MagicMock

import httpx
import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.client import AsyncExactOnlineClient, ExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import APIError, RateLimitError, ExactOnlineSDKError


class DummyAuth:
    def get_access_token(self) -> str:
        return "token"

    async def aget_access_token(self) -> str:
        return "token"


def test_iter_pages_odata_v4_nextlink(httpx_mock: HTTPXMock) -> None:
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={
            "value": [{"ID": "1"}],
            "@odata.nextLink": "https://api.example/api/v1/crm/Accounts?$skiptoken=ABC",
        },
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?$skiptoken=ABC",
        json={"value": [{"ID": "2"}]},
    )

    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = list(client.iter_pages("crm/Accounts"))

    assert len(pages) == 2
    assert pages[0][0]["ID"] == "1"
    assert pages[1][0]["ID"] == "2"


def test_iter_pages_odata_v2_next(httpx_mock: HTTPXMock) -> None:
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={
            "d": {
                "results": [{"ID": "1"}],
                "__next": "https://api.example/api/v1/crm/Accounts?$skiptoken=DEF",
            }
        },
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?$skiptoken=DEF",
        json={"d": {"results": [{"ID": "2"}]}},
    )

    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = list(client.iter_pages("crm/Accounts"))

    assert len(pages) == 2
    assert pages[0][0]["ID"] == "1"
    assert pages[1][0]["ID"] == "2"


async def test_aiter_pages_v4_nextlink(httpx_mock: HTTPXMock) -> None:
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={
            "value": [{"ID": "1"}],
            "@odata.nextLink": "https://api.example/api/v1/crm/Accounts?$skiptoken=XYZ",
        },
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?$skiptoken=XYZ",
        json={"value": [{"ID": "3"}]},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = []
    async for page in client.aiter_pages("crm/Accounts"):
        pages.append(page)

    assert len(pages) == 2
    assert pages[0][0]["ID"] == "1"
    assert pages[1][0]["ID"] == "3"


def test_iter_pages_list_payload(httpx_mock: HTTPXMock) -> None:
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json=[{"ID": "1"}, {"ID": "2"}],
    )

    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = list(client.iter_pages("crm/Accounts"))

    assert len(pages) == 1
    assert [item["ID"] for item in pages[0]] == ["1", "2"]

    client.close()


def test_iter_pages_http_error_raises_apierror() -> None:
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    client._client = MagicMock()
    client._client.request.side_effect = httpx.ConnectTimeout(
        "timeout",
        request=httpx.Request("GET", "https://api.example/api/v1/crm/Accounts"),
    )

    iterator = client.iter_pages("crm/Accounts")

    with pytest.raises(APIError) as exc:
        next(iterator)
    assert exc.value.status_code == 0

    client.close()


def test_iter_pages_rate_limit_sleeps_and_raises(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    request = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    response = httpx.Response(429, headers={"Retry-After": "0.25"}, request=request)

    client._client = MagicMock()
    client._client.request.return_value = response

    slept: List[float] = []

    def fake_sleep(seconds: float) -> None:
        slept.append(seconds)

    monkeypatch.setattr("exact_online_sdk.client.time.sleep", fake_sleep)

    iterator = client.iter_pages("crm/Accounts")

    with pytest.raises(RateLimitError):
        next(iterator)

    assert slept[0] == 0.25

    client.close()


def test_iter_pages_xml_response_raises_sdk_error(httpx_mock: HTTPXMock) -> None:
    """Test that paginated XML success response produces descriptive SDK failure."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    xml_content = b'<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom"><entry><id>1</id></entry></feed>'
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        content=xml_content,
        headers={"Content-Type": "application/atom+xml"},
        status_code=200,
    )

    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    iterator = client.iter_pages("crm/Accounts")

    with pytest.raises(ExactOnlineSDKError) as exc:
        next(iterator)

    assert "JSON" in str(exc.value) or "parse" in str(exc.value).lower()
    client.close()


def test_iter_pages_malformed_json_raises_sdk_error(httpx_mock: HTTPXMock) -> None:
    """Test that malformed JSON during page extraction is wrapped in SDK error."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        content=b'{"invalid json: missing closing brace',
        headers={"Content-Type": "application/json"},
        status_code=200,
    )

    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    iterator = client.iter_pages("crm/Accounts")

    with pytest.raises(ExactOnlineSDKError) as exc:
        next(iterator)

    assert "JSON" in str(exc.value) or "parse" in str(exc.value).lower()
    client.close()


def test_iter_pages_preserves_format_override(httpx_mock: HTTPXMock) -> None:
    """Test that explicit $format override survives next-page traversal."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?%24format=json",
        json={
            "value": [{"ID": "1"}],
            "@odata.nextLink": "https://api.example/api/v1/crm/Accounts?$skiptoken=ABC&$format=json",
        },
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?$skiptoken=ABC&$format=json",
        json={"value": [{"ID": "2"}]},
    )

    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = list(
        client.iter_pages("crm/Accounts", params={"$format": "json"})
    )

    assert len(pages) == 2
    assert pages[0][0]["ID"] == "1"
    assert pages[1][0]["ID"] == "2"
    client.close()
