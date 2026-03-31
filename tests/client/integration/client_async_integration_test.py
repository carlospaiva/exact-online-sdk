from __future__ import annotations

from typing import Any, List

import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.client import AsyncExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import APIError, ExactOnlineSDKError

pytestmark = pytest.mark.integration


class DummyAuth:
    """Dummy auth for testing."""

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
async def test_async_integration_list_accounts(httpx_mock: HTTPXMock) -> None:
    """Integration test: async GET request negotiates JSON and parses response."""
    settings = _settings()

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={"value": [{"ID": "1", "Name": "Test Account"}]},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    data = await client.get("crm/Accounts")

    assert data == [{"ID": "1", "Name": "Test Account"}]

    # Verify Accept header was sent
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_pagination_odata_v2(httpx_mock: HTTPXMock) -> None:
    """Integration test: async pagination with OData v2 next-link."""
    settings = _settings()

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={
            "d": {
                "results": [{"ID": "1"}, {"ID": "2"}],
                "__next": "https://api.example/api/v1/crm/Accounts?$skiptoken=ABC",
            }
        },
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts?$skiptoken=ABC",
        json={"d": {"results": [{"ID": "3"}, {"ID": "4"}]}},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    pages: List[list[Any]] = []
    async for page in client.aiter_pages("crm/Accounts"):
        pages.append(page)

    assert len(pages) == 2
    assert len(pages[0]) == 2
    assert len(pages[1]) == 2
    assert pages[0][0]["ID"] == "1"
    assert pages[1][0]["ID"] == "3"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_pagination_list_payload(httpx_mock: HTTPXMock) -> None:
    """Integration test: async pagination with plain list response."""
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
    assert len(pages[0]) == 2
    assert pages[0][0]["ID"] == "1"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_post_sends_accept_json(httpx_mock: HTTPXMock) -> None:
    """Integration test: async POST sends Accept: application/json."""
    settings = _settings()

    httpx_mock.add_response(
        method="POST",
        url="https://api.example/api/v1/crm/Accounts",
        json={"d": {"results": [{"ID": "new-id", "Name": "New Account"}]}},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    result = await client.post("crm/Accounts", json={"Name": "New Account"})

    # Response is normalized by _handle_response
    assert result == [{"ID": "new-id", "Name": "New Account"}]

    # Verify Accept header was sent
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_patch_sends_accept_json(httpx_mock: HTTPXMock) -> None:
    """Integration test: async PATCH sends Accept: application/json."""
    settings = _settings()

    httpx_mock.add_response(
        method="PATCH",
        url="https://api.example/api/v1/crm/Accounts(guid'123')",
        json={"d": {"results": [{"ID": "123", "Name": "Updated"}]}},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    result = await client.patch("crm/Accounts(guid'123')", json={"Name": "Updated"})

    # Response is normalized by _handle_response
    assert result == [{"ID": "123", "Name": "Updated"}]

    # Verify Accept header was sent
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_delete_sends_accept_json(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async DELETE sends Accept: application/json."""
    settings = _settings()

    httpx_mock.add_response(
        method="DELETE",
        url="https://api.example/api/v1/crm/Accounts(guid'123')",
        status_code=204,
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    await client.delete("crm/Accounts(guid'123')")

    # Verify Accept header was sent even for DELETE
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_xml_response_raises_sdk_error(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async XML success raises SDK error, not JSONDecodeError."""
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

    with pytest.raises(ExactOnlineSDKError) as exc_info:
        await client.get("crm/Accounts")

    # Should be SDK error, not raw JSONDecodeError
    error_msg = str(exc_info.value).lower()
    assert "json" in error_msg or "parse" in error_msg or "content" in error_msg

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_html_response_raises_sdk_error(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async HTML success response raises SDK error."""
    settings = _settings()

    html_content = b"<html><body>Error Page</body></html>"
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=200,
        content=html_content,
        headers={"Content-Type": "text/html"},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    with pytest.raises(ExactOnlineSDKError) as exc_info:
        await client.get("crm/Accounts")

    error_msg = str(exc_info.value).lower()
    assert "json" in error_msg or "html" in error_msg or "content" in error_msg

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_malformed_json_raises_sdk_error(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async malformed JSON success response raises SDK error."""
    settings = _settings()

    malformed_content = b'{"d": {"results": [{"ID": "1"}, {"ID": "2"'
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=200,
        content=malformed_content,
        headers={"Content-Type": "application/json"},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    with pytest.raises(ExactOnlineSDKError) as exc_info:
        await client.get("crm/Accounts")

    error_msg = str(exc_info.value).lower()
    assert "json" in error_msg or "parse" in error_msg or "malformed" in error_msg

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_pagination_xml_raises_sdk_error(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async pagination XML response raises SDK error."""
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

    with pytest.raises(ExactOnlineSDKError) as exc_info:
        await agen.__anext__()

    error_msg = str(exc_info.value).lower()
    assert "json" in error_msg or "parse" in error_msg or "content" in error_msg

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_pagination_malformed_json_raises_sdk_error(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async pagination malformed JSON raises SDK error."""
    settings = _settings()

    malformed_content = b'{"d": {"results": [{"ID": "1"}'
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=200,
        content=malformed_content,
        headers={"Content-Type": "application/json"},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(ExactOnlineSDKError) as exc_info:
        await agen.__anext__()

    error_msg = str(exc_info.value).lower()
    assert "json" in error_msg or "parse" in error_msg or "malformed" in error_msg

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_preserves_explicit_format_override(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async client preserves explicit $format override."""
    settings = _settings()

    # Match URL with encoded $format parameter (%24 is URL-encoded $)
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

    # Verify $format=xml was preserved in both requests (URL-encoded as %24format)
    requests = httpx_mock.get_requests()
    assert len(requests) == 2
    for req in requests:
        url_str = str(req.url)
        assert "$format=xml" in url_str or "%24format=xml" in url_str

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_accounts_style_path(httpx_mock: HTTPXMock) -> None:
    """Integration test: async Accounts-style path works with JSON negotiation."""
    settings = _settings()

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={
            "d": {
                "results": [
                    {"ID": "acc-1", "Name": "Account 1", "Email": "a1@example.com"},
                    {"ID": "acc-2", "Name": "Account 2", "Email": "a2@example.com"},
                ]
            }
        },
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    data = await client.get("crm/Accounts")

    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["ID"] == "acc-1"
    assert data[0]["Name"] == "Account 1"

    # Verify Accept header was sent
    request = httpx_mock.get_request()
    assert request.headers["Accept"] == "application/json"

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_error_response_with_xml_body(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async error response with XML body is handled correctly."""
    settings = _settings()

    xml_error = b'<?xml version="1.0"?><error><message>Not Found</message></error>'
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=404,
        content=xml_error,
        headers={"Content-Type": "application/xml"},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    with pytest.raises(APIError) as exc_info:
        await client.get("crm/Accounts")

    assert exc_info.value.status_code == 404

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_odata_v4_value_format(httpx_mock: HTTPXMock) -> None:
    """Integration test: async OData v4 'value' format works correctly."""
    settings = _settings()

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Contacts",
        json={"value": [{"ID": "c1", "FullName": "John Doe"}]},
    )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    data = await client.get("crm/Contacts")

    assert data == [{"ID": "c1", "FullName": "John Doe"}]

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_pagination_with_error_status(
    httpx_mock: HTTPXMock,
) -> None:
    """Integration test: async pagination handles error status codes."""
    settings = _settings()

    # Add multiple responses for retry attempts
    for _ in range(5):
        httpx_mock.add_response(
            method="GET",
            url="https://api.example/api/v1/crm/Accounts",
            status_code=500,
            json={"error": {"message": "Internal Server Error"}},
        )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(APIError) as exc_info:
        await agen.__anext__()

    assert exc_info.value.status_code == 500

    await client.aclose()


@pytest.mark.asyncio
async def test_async_integration_rate_limit_handling(httpx_mock: HTTPXMock) -> None:
    """Integration test: async rate limit is handled correctly."""
    settings = _settings()

    from exact_online_sdk.exceptions import RateLimitError

    # Add multiple responses for retry attempts
    for _ in range(5):
        httpx_mock.add_response(
            method="GET",
            url="https://api.example/api/v1/crm/Accounts",
            status_code=429,
            headers={"Retry-After": "0.1"},
            json={"error": "Rate limit exceeded"},
        )

    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    agen = client.aiter_pages("crm/Accounts")

    with pytest.raises(RateLimitError) as exc_info:
        await agen.__anext__()

    assert exc_info.value.retry_after == 0.1

    await client.aclose()
