from __future__ import annotations

from typing import Any, Dict, Optional
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from exact_online_sdk.client import AsyncExactOnlineClient, ExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import APIError, RateLimitError


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


def _response(status: int, data: Any) -> httpx.Response:
    request = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    return httpx.Response(status, json=data, request=request)


def _response_with_content_type(
    status: int, content: bytes, content_type: str
) -> httpx.Response:
    request = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    headers = {"Content-Type": content_type}
    return httpx.Response(status, content=content, headers=headers, request=request)


def test_handle_response_odata_v2_results() -> None:
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    resp = _response(200, {"d": {"results": [{"ID": "1"}]}})

    result = client._handle_response(resp)
    assert result == [{"ID": "1"}]

    client.close()


def test_handle_response_list_payload() -> None:
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    resp = _response(200, [{"ID": "1"}, {"ID": "2"}])

    result = client._handle_response(resp)
    assert isinstance(result, list)
    assert len(result) == 2

    client.close()


def test_handle_response_odata_v4_value() -> None:
    """Test OData v4 format with 'value' key."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    resp = _response(200, {"value": [{"ID": "1"}, {"ID": "2"}]})

    result = client._handle_response(resp)
    assert result == [{"ID": "1"}, {"ID": "2"}]

    client.close()


def test_sync_get_sends_accept_json_header(httpx_mock: Any) -> None:
    """Test that GET requests send Accept: application/json header."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    # Mock the response
    httpx_mock.add_response(
        url="https://api.example/api/v1/crm/Accounts",
        json={"d": {"results": [{"ID": "1"}]}},
        status_code=200,
    )

    client.get("crm/Accounts")

    # Verify the request had the Accept header
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    client.close()


def test_sync_post_sends_accept_json_header(httpx_mock: Any) -> None:
    """Test that POST requests send Accept: application/json header."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    # Mock the response
    httpx_mock.add_response(
        url="https://api.example/api/v1/crm/Accounts",
        json={"d": {"results": [{"ID": "1"}]}},
        status_code=200,
    )

    client.post("crm/Accounts", json={"Name": "Test"})

    # Verify the request had the Accept header
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    client.close()


def test_sync_handle_response_xml_raises_sdk_error() -> None:
    """Test that XML success responses raise SDK exception, not JSONDecodeError."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    xml_content = (
        b"<?xml version='1.0'?><feed xmlns='http://www.w3.org/2005/Atom'>"
        b"<entry></entry></feed>"
    )
    resp = _response_with_content_type(200, xml_content, "application/atom+xml")

    with pytest.raises(APIError) as exc_info:
        client._handle_response(resp)

    assert (
        "JSON" in str(exc_info.value)
        or "xml" in str(exc_info.value).lower()
        or "atom" in str(exc_info.value).lower()
    )
    assert exc_info.value.context.get("content_type") == "application/atom+xml"

    client.close()


def test_sync_handle_response_html_raises_sdk_error() -> None:
    """Test that HTML success responses raise SDK exception, not JSONDecodeError."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    html_content = b"<html><body>Error Page</body></html>"
    resp = _response_with_content_type(200, html_content, "text/html")

    with pytest.raises(APIError) as exc_info:
        client._handle_response(resp)

    assert "JSON" in str(exc_info.value) or "html" in str(exc_info.value).lower()
    assert exc_info.value.context.get("content_type") == "text/html"

    client.close()


def test_sync_handle_response_malformed_json_raises_sdk_error() -> None:
    """Test that malformed JSON success responses raise SDK exception."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    malformed_content = b'{"invalid json: missing closing brace'
    resp = _response_with_content_type(200, malformed_content, "application/json")

    with pytest.raises(APIError) as exc_info:
        client._handle_response(resp)

    assert (
        "JSON" in str(exc_info.value)
        or "parse" in str(exc_info.value).lower()
        or "malformed" in str(exc_info.value).lower()
    )
    assert exc_info.value.context.get("content_type") == "application/json"

    client.close()


def test_sync_handle_response_missing_content_type_raises_sdk_error() -> None:
    """Test responses without Content-Type header raise SDK exception for bad JSON."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    # Create response without Content-Type header and with invalid JSON
    content = b"not valid json"
    request = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    resp = httpx.Response(200, content=content, headers={}, request=request)

    with pytest.raises(APIError) as exc_info:
        client._handle_response(resp)

    assert (
        "JSON" in str(exc_info.value) or "content-type" in str(exc_info.value).lower()
    )
    # Content-Type should be None or missing in context
    assert exc_info.value.context.get("content_type") is None

    client.close()


def test_sync_handle_response_empty_body_returns_none() -> None:
    """Test that empty response body returns None."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    resp = _response_with_content_type(200, b"", "application/json")

    result = client._handle_response(resp)
    assert result is None

    client.close()


@pytest.mark.asyncio
async def test_async_handle_response_odata_v2_results() -> None:
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    resp = _response(200, {"d": {"results": [{"ID": "1"}]}})

    result = client._handle_response(resp)
    assert result == [{"ID": "1"}]

    await client.aclose()


@pytest.mark.asyncio
async def test_async_handle_response_list_payload() -> None:
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    resp = _response(200, [{"ID": "1"}])

    result = client._handle_response(resp)
    assert result == [{"ID": "1"}]

    await client.aclose()


def test_sync_public_methods_delegate_to_request(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    calls: list[tuple[str, str, Optional[Dict[str, Any]], Optional[Dict[str, Any]]]] = (
        []
    )

    def fake_request(
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> str:
        calls.append((method, path, params, json))
        return "ok"

    monkeypatch.setattr(client, "_request", fake_request)

    payload = {"Name": "Test"}
    assert client.post("crm/Accounts", json=payload) == "ok"
    assert client.patch("crm/Accounts(guid'1')", json=payload) == "ok"
    assert client.delete("crm/Accounts(guid'1')") == "ok"

    assert calls == [
        ("POST", "crm/Accounts", None, payload),
        ("PATCH", "crm/Accounts(guid'1')", None, payload),
        ("DELETE", "crm/Accounts(guid'1')", None, None),
    ]

    client.close()


@pytest.mark.asyncio
async def test_async_public_methods_delegate_to_arequest(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    calls: list[tuple[str, str, Optional[Dict[str, Any]], Optional[Dict[str, Any]]]] = (
        []
    )

    async def fake_arequest(
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> str:
        calls.append((method, path, params, json))
        return "ok"

    monkeypatch.setattr(client, "_arequest", fake_arequest)

    payload = {"Name": "Test"}
    assert await client.post("crm/Accounts", json=payload) == "ok"
    assert await client.patch("crm/Accounts(guid'1')", json=payload) == "ok"
    assert await client.delete("crm/Accounts(guid'1')") == "ok"

    assert calls == [
        ("POST", "crm/Accounts", None, payload),
        ("PATCH", "crm/Accounts(guid'1')", None, payload),
        ("DELETE", "crm/Accounts(guid'1')", None, None),
    ]

    await client.aclose()


@pytest.mark.asyncio
async def test_async_get_sends_accept_json_header(httpx_mock: Any) -> None:
    """Test that async GET requests send Accept: application/json header."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    # Mock the response
    httpx_mock.add_response(
        url="https://api.example/api/v1/crm/Accounts",
        json={"d": {"results": [{"ID": "1"}]}},
        status_code=200,
    )

    await client.get("crm/Accounts")

    # Verify the request had the Accept header
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_post_sends_accept_json_header(httpx_mock: Any) -> None:
    """Test that async POST requests send Accept: application/json header."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    # Mock the response
    httpx_mock.add_response(
        url="https://api.example/api/v1/crm/Accounts",
        json={"d": {"results": [{"ID": "1"}]}},
        status_code=200,
    )

    await client.post("crm/Accounts", json={"Name": "Test"})

    # Verify the request had the Accept header
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_handle_response_xml_raises_sdk_error() -> None:
    """Test async XML success responses raise SDK exception, not JSONDecodeError."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    xml_content = (
        b"<?xml version='1.0'?><feed xmlns='http://www.w3.org/2005/Atom'>"
        b"<entry></entry></feed>"
    )
    resp = _response_with_content_type(200, xml_content, "application/atom+xml")

    with pytest.raises(APIError) as exc_info:
        client._handle_response(resp)

    assert (
        "JSON" in str(exc_info.value)
        or "xml" in str(exc_info.value).lower()
        or "atom" in str(exc_info.value).lower()
    )
    assert exc_info.value.context.get("content_type") == "application/atom+xml"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_handle_response_html_raises_sdk_error() -> None:
    """Test async HTML success responses raise SDK exception, not JSONDecodeError."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    html_content = b"<html><body>Error Page</body></html>"
    resp = _response_with_content_type(200, html_content, "text/html")

    with pytest.raises(APIError) as exc_info:
        client._handle_response(resp)

    assert "JSON" in str(exc_info.value) or "html" in str(exc_info.value).lower()
    assert exc_info.value.context.get("content_type") == "text/html"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_handle_response_malformed_json_raises_sdk_error() -> None:
    """Test that async malformed JSON success responses raise SDK exception."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    malformed_content = b'{"invalid json: missing closing brace'
    resp = _response_with_content_type(200, malformed_content, "application/json")

    with pytest.raises(APIError) as exc_info:
        client._handle_response(resp)

    assert (
        "JSON" in str(exc_info.value)
        or "parse" in str(exc_info.value).lower()
        or "malformed" in str(exc_info.value).lower()
    )
    assert exc_info.value.context.get("content_type") == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_handle_response_empty_body_returns_none() -> None:
    """Test that async empty response body returns None."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    resp = _response_with_content_type(200, b"", "application/json")

    result = client._handle_response(resp)
    assert result is None

    await client.aclose()


@pytest.mark.asyncio
async def test_async_handle_response_odata_v4_value() -> None:
    """Test async OData v4 format with 'value' key remains unchanged."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    resp = _response(200, {"value": [{"ID": "1"}, {"ID": "2"}]})

    result = client._handle_response(resp)
    assert result == [{"ID": "1"}, {"ID": "2"}]

    await client.aclose()


@pytest.mark.asyncio
async def test_arequest_impl_rate_limit_sleeps_without_recreating_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    request = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    resp = httpx.Response(200, json={"value": []}, request=request)

    async def fake_request(*args: object, **kwargs: object) -> httpx.Response:
        return resp

    stub = MagicMock()
    stub.request = AsyncMock(side_effect=fake_request)
    stub.aclose = AsyncMock()
    client._client = stub

    def fake_handle_response(response: httpx.Response) -> None:
        raise RateLimitError("limit", retry_after=0.01)

    monkeypatch.setattr(client, "_handle_response", fake_handle_response)

    sleep_calls: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleep_calls.append(seconds)

    monkeypatch.setattr("exact_online_sdk.client.asyncio.sleep", fake_sleep)

    with pytest.raises(RateLimitError):
        await client._arequest_impl("GET", "crm/Accounts")

    assert sleep_calls == [0.01]
    # Client should NOT have been closed or recreated
    assert stub.aclose.await_count == 0
    assert client._client is stub

    await client.aclose()
