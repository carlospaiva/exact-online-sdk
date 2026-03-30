from __future__ import annotations

import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.client import ExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import APIError

pytestmark = pytest.mark.integration


def test_integration_list_accounts(httpx_mock: HTTPXMock) -> None:
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )

    httpx_mock.add_response(
        method="GET", url="https://api.example/api/v1/crm/Accounts", json={"value": []}
    )

    class _Auth:
        def get_access_token(self) -> str:
            return "token"

    client = ExactOnlineClient(settings=settings, auth=_Auth())
    data = client.get("crm/Accounts")
    assert data == []


def test_integration_sync_json_negotiation_success(httpx_mock: HTTPXMock) -> None:
    """Prove direct client GET path behaves correctly when JSON is negotiated."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={"value": [{"ID": "abc-123", "Name": "Test Account"}]},
        headers={"Content-Type": "application/json"},
    )

    class _Auth:
        def get_access_token(self) -> str:
            return "token"

    client = ExactOnlineClient(settings=settings, auth=_Auth())
    data = client.get("crm/Accounts")

    # Verify JSON data is correctly parsed
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["ID"] == "abc-123"
    assert data[0]["Name"] == "Test Account"

    # Verify Accept header was sent
    request = httpx_mock.get_request()
    assert request is not None
    assert request.headers.get("Accept") == "application/json"


def test_integration_sync_non_json_success_response(httpx_mock: HTTPXMock) -> None:
    """Prove non-JSON success responses produce descriptive SDK failure, not raw decode error."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )

    # Simulate XML/Atom response (non-JSON success)
    xml_body = """<?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
        <entry><content type="application/xml"><m:properties></m:properties></content></entry>
    </feed>"""

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        content=xml_body.encode(),
        headers={"Content-Type": "application/atom+xml"},
        status_code=200,
    )

    class _Auth:
        def get_access_token(self) -> str:
            return "token"

    client = ExactOnlineClient(settings=settings, auth=_Auth())

    # Should raise APIError with descriptive message, not raw JSONDecodeError
    with pytest.raises(APIError) as exc_info:
        client.get("crm/Accounts")

    # Verify the error is descriptive and contains context
    assert "Expected JSON response" in str(
        exc_info.value
    ) or "Failed to parse JSON" in str(exc_info.value)
    assert exc_info.value.context is not None
    assert "content_type" in exc_info.value.context
    assert "atom" in exc_info.value.context["content_type"].lower()


def test_integration_sync_accounts_path_no_raw_decode_error(
    httpx_mock: HTTPXMock,
) -> None:
    """Prove the Exact-style Accounts path no longer fails with raw JSON decode errors."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )

    # Simulate successful JSON response from Exact-style endpoint
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={
            "d": {
                "results": [
                    {"ID": "guid-1", "Name": "Account One", "Email": "one@example.com"},
                    {"ID": "guid-2", "Name": "Account Two", "Email": "two@example.com"},
                ],
                "__next": None,
            }
        },
        headers={"Content-Type": "application/json"},
    )

    class _Auth:
        def get_access_token(self) -> str:
            return "token"

    client = ExactOnlineClient(settings=settings, auth=_Auth())

    # This should work without raising any JSON decode errors
    data = client.get("crm/Accounts")

    # Verify OData v2 envelope is normalized correctly
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["ID"] == "guid-1"
    assert data[0]["Name"] == "Account One"


def test_integration_sync_html_error_response(httpx_mock: HTTPXMock) -> None:
    """Prove HTML success responses (like error pages) produce descriptive SDK failure."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )

    # Simulate HTML response (e.g., WAF block or proxy error page)
    html_body = """<html><body><h1>Service Unavailable</h1></body></html>"""

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        content=html_body.encode(),
        headers={"Content-Type": "text/html"},
        status_code=200,
    )

    class _Auth:
        def get_access_token(self) -> str:
            return "token"

    client = ExactOnlineClient(settings=settings, auth=_Auth())

    # Should raise APIError with descriptive message
    with pytest.raises(APIError) as exc_info:
        client.get("crm/Accounts")

    # Verify the error mentions content-type mismatch
    error_message = str(exc_info.value)
    assert (
        "Expected JSON response" in error_message
        or "Failed to parse JSON" in error_message
    )
    assert exc_info.value.context is not None
    assert "content_type" in exc_info.value.context


def test_integration_sync_malformed_json_response(httpx_mock: HTTPXMock) -> None:
    """Prove malformed JSON success responses produce descriptive SDK failure."""
    settings = Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )

    # Simulate malformed JSON response
    malformed_json = b'{"value": ["unclosed string}'

    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        content=malformed_json,
        headers={"Content-Type": "application/json"},
        status_code=200,
    )

    class _Auth:
        def get_access_token(self) -> str:
            return "token"

    client = ExactOnlineClient(settings=settings, auth=_Auth())

    # Should raise APIError with descriptive message, not raw JSONDecodeError
    with pytest.raises(APIError) as exc_info:
        client.get("crm/Accounts")

    # Verify the error is descriptive
    assert "Failed to parse JSON" in str(exc_info.value)
    assert exc_info.value.context is not None
    assert "content_type" in exc_info.value.context
