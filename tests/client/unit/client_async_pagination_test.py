from __future__ import annotations

from typing import Any, List
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.client import AsyncExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import APIError, ExactOnlineSDKError, RateLimitError


class DummyAuth:
    def get_access_token(self) -> str:
        return "token"

    async def aget_access_token(self) -> str:
        return "token"


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )


@pytest.mark.asyncio
async def test_aiter_pages_odata_v2_nextlink(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
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

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = []
    async for page in client.aiter_pages("crm/Accounts"):
        pages.append(page)

    assert len(pages) == 2
    assert pages[0][0]["ID"] == "1"
    assert pages[1][0]["ID"] == "2"

    await client.aclose()


@pytest.mark.asyncio
async def test_aiter_pages_list_payload(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json=[{"ID": "1"}, {"ID": "2"}],
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = []
    async for page in client.aiter_pages("crm/Accounts"):
        pages.append(page)

    assert len(pages) == 1
    assert [item["ID"] for item in pages[0]] == ["1", "2"]

    await client.aclose()


@pytest.mark.asyncio
async def test_aiter_pages_http_error_raises_apierror() -> None:
    client = AsyncExactOnlineClient(settings=_settings(), auth=DummyAuth())

    stub = MagicMock()
    stub.request = AsyncMock(
        side_effect=httpx.ConnectTimeout(
            "timeout",
            request=httpx.Request("GET", "https://api.example/api/v1/crm/Accounts"),
        )
    )
    stub.aclose = AsyncMock()
    client._client = stub

    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(APIError) as exc:
        await agen.__anext__()

    assert exc.value.status_code == 0

    await client.aclose()


@pytest.mark.asyncio
async def test_aiter_pages_rate_limit_sleeps(monkeypatch: pytest.MonkeyPatch) -> None:
    client = AsyncExactOnlineClient(settings=_settings(), auth=DummyAuth())

    request = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    response = httpx.Response(429, headers={"Retry-After": "0.1"}, request=request)

    stub = MagicMock()
    stub.request = AsyncMock(return_value=response)
    stub.aclose = AsyncMock()
    client._client = stub

    sleep_calls: List[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("exact_online_sdk.client.asyncio.sleep", fake_sleep)

    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(RateLimitError):
        await agen.__anext__()

    assert sleep_calls[0] == 0.1

    await client.aclose()


@pytest.mark.asyncio
async def test_aiter_pages_non_success_status_raises_apierror(
    httpx_mock: HTTPXMock,
) -> None:
    settings = _settings()
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=404,
        json={"error": "not found"},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(APIError) as exc:
        await agen.__anext__()

    assert exc.value.status_code == 404

    await client.aclose()


@pytest.mark.asyncio
async def test_aiter_pages_xml_response_raises_sdk_error(
    httpx_mock: HTTPXMock,
) -> None:
    settings = _settings()
    xml_content = (
        b'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">'
        b"<entry><id>1</id></entry></feed>"
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=200,
        content=xml_content,
        headers={"Content-Type": "application/atom+xml"},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(ExactOnlineSDKError) as exc:
        await agen.__anext__()

    assert exc.value is not None
    error_msg = str(exc.value).lower()
    assert "json" in error_msg or "parse" in error_msg or "content" in error_msg

    await client.aclose()


@pytest.mark.asyncio
async def test_aiter_pages_malformed_json_raises_sdk_error(
    httpx_mock: HTTPXMock,
) -> None:
    settings = _settings()
    malformed_json = b'{"d": {"results": [{"ID": "1"}, {"ID": "2"'
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=200,
        content=malformed_json,
        headers={"Content-Type": "application/json"},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(ExactOnlineSDKError) as exc:
        await agen.__anext__()

    assert exc.value is not None
    error_msg = str(exc.value).lower()
    assert "json" in error_msg or "parse" in error_msg or "malformed" in error_msg

    await client.aclose()


@pytest.mark.asyncio
async def test_aiter_pages_preserves_explicit_format_override(
    httpx_mock: HTTPXMock,
) -> None:
    settings = _settings()
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?%24format=xml",
        json={
            "d": {
                "results": [{"ID": "1"}],
                "__next": (
                    "https://api.example/api/v1/crm/Accounts?$skiptoken=DEF&$format=xml"
                ),
            }
        },
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?%24skiptoken=DEF&%24format=xml",
        json={"d": {"results": [{"ID": "2"}]}},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = []
    async for page in client.aiter_pages("crm/Accounts", params={"$format": "xml"}):
        pages.append(page)

    assert len(pages) == 2
    assert pages[0][0]["ID"] == "1"
    assert pages[1][0]["ID"] == "2"

    requests = httpx_mock.get_requests()
    assert len(requests) == 2
    for req in requests:
        assert "$format=xml" in str(req.url) or "%24format=xml" in str(req.url)

    await client.aclose()
