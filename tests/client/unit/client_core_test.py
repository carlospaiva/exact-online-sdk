from __future__ import annotations

from typing import Any, List, Optional
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.client import (
    AsyncExactOnlineClient,
    ExactOnlineClient,
    _is_retryable,
)
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import APIError, RateLimitError


class DummyAuth:
    def __init__(self) -> None:
        self.called = 0

    def get_access_token(self) -> str:
        self.called += 1
        return "token"

    async def aget_access_token(self) -> str:
        self.called += 1
        return "token"


def _settings(*, division: Optional[int] = None) -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
        division=division,
    )


def test_get_success(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={"value": [{"ID": "1"}]},
    )
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    result = client.get("crm/Accounts")

    assert isinstance(result, list)
    assert result[0]["ID"] == "1"
    client.close()


def test_rate_limit_then_retry(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        status_code=429,
        headers={"Retry-After": "0"},
    )
    httpx_mock.add_response(
        method="GET", url="https://api.example/api/v1/crm/Accounts", json={"value": []}
    )
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    result = client.get("crm/Accounts")
    assert result == []
    client.close()


async def test_async_get_success(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/crm/Accounts",
        json={"value": [{"ID": "1"}]},
    )
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    result = await client.get("crm/Accounts")

    assert isinstance(result, list)
    assert result[0]["ID"] == "1"
    await client.aclose()


def test_handle_response_errors() -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    req = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")

    rate_resp = httpx.Response(429, headers={"Retry-After": "2"}, request=req)
    with pytest.raises(RateLimitError) as rate:
        client._handle_response(rate_resp)
    assert rate.value.retry_after == 2.0

    error_resp = httpx.Response(500, text="boom", request=req)
    with pytest.raises(APIError) as api_err:
        client._handle_response(error_resp)
    assert api_err.value.status_code == 500

    client.close()


def test_request_impl_handles_http_errors() -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())

    def fail(*args: object, **kwargs: object) -> None:
        raise httpx.ConnectTimeout(
            "boom",
            request=httpx.Request("GET", "https://api.example/api/v1/crm/Accounts"),
        )

    client._client = MagicMock()
    client._client.request.side_effect = fail

    with pytest.raises(APIError) as exc:
        client._request_impl("GET", "crm/Accounts")
    assert exc.value.status_code == 0

    client.close()


def test_request_impl_rate_limit_sleeps(monkeypatch: pytest.MonkeyPatch) -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    req = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    resp = httpx.Response(429, headers={"Retry-After": "0.1"}, request=req)

    client._client = MagicMock()
    client._client.request.return_value = resp

    slept: List[float] = []

    def fake_sleep(seconds: float) -> None:
        slept.append(seconds)

    monkeypatch.setattr("exact_online_sdk.client.time.sleep", fake_sleep)

    with pytest.raises(RateLimitError):
        client._request_impl("GET", "crm/Accounts")
    assert slept == [0.1]

    client.close()


def test_request_retries_after_retryable(monkeypatch: pytest.MonkeyPatch) -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    attempts = {"count": 0}

    def fake_impl(
        method: str, path: str, *, params: Any = None, json: Any = None
    ) -> str:
        attempts["count"] += 1
        if attempts["count"] == 1:
            raise RateLimitError("limit")
        return "ok"

    monkeypatch.setattr(client, "_request_impl", fake_impl)

    assert client._request("GET", "crm/Accounts") == "ok"
    assert attempts["count"] == 2

    client.close()


def test_is_retryable_utility() -> None:
    assert _is_retryable(RateLimitError("limit"))
    assert _is_retryable(APIError(500, "boom"))
    timeout_exc = httpx.ConnectTimeout(
        "timeout", request=httpx.Request("GET", "https://api.example")
    )
    assert _is_retryable(timeout_exc)
    assert not _is_retryable(APIError(400, "bad"))


def _response(
    status: int, data: Any, url: str, headers: dict[str, str] | None = None
) -> httpx.Response:
    request = httpx.Request("GET", url)
    return httpx.Response(status, json=data, headers=headers or {}, request=request)


def test_iter_pages_handles_odata_v4(monkeypatch: pytest.MonkeyPatch) -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    first = _response(
        200,
        {"value": [{"ID": "1"}], "@odata.nextLink": "crm/Accounts?$skip=1"},
        "https://api.example/api/v1/crm/Accounts",
    )
    second = _response(
        200,
        {"value": [{"ID": "2"}]},
        "https://api.example/api/v1/crm/Accounts?$skip=1",
    )

    client._client = MagicMock()
    client._client.request.side_effect = [first, second]

    pages = list(client.iter_pages("crm/Accounts"))
    assert pages == [[{"ID": "1"}], [{"ID": "2"}]]

    client.close()


def test_iter_pages_non_success_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    error_resp = httpx.Response(
        404,
        text="missing",
        request=httpx.Request("GET", "https://api.example/api/v1/crm/Accounts"),
    )

    client._client = MagicMock()
    client._client.request.return_value = error_resp

    iterator = client.iter_pages("crm/Accounts")
    with pytest.raises(APIError):
        next(iterator)

    client.close()


def test_client_context_manager_closes(monkeypatch: pytest.MonkeyPatch) -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    original_close = client.close
    close_called = False

    def wrapped_close() -> None:
        nonlocal close_called
        close_called = True
        original_close()

    monkeypatch.setattr(client, "close", wrapped_close)

    with client as ctx:
        assert ctx is client
    assert close_called is True


@pytest.mark.asyncio
async def test_async_handle_response_raises() -> None:
    client = AsyncExactOnlineClient(settings=_settings(), auth=DummyAuth())
    req = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")

    resp = httpx.Response(429, headers={"Retry-After": "1"}, request=req)
    with pytest.raises(RateLimitError):
        client._handle_response(resp)

    api_resp = httpx.Response(400, text="bad", request=req)
    with pytest.raises(APIError):
        client._handle_response(api_resp)

    await client.aclose()


@pytest.mark.asyncio
async def test_arequest_impl_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    client = AsyncExactOnlineClient(settings=_settings(), auth=DummyAuth())
    await client._client.aclose()

    async def fail(*args: object, **kwargs: object) -> None:
        raise httpx.ConnectTimeout(
            "boom",
            request=httpx.Request("GET", "https://api.example/api/v1/crm/Accounts"),
        )

    stub = MagicMock()
    stub.request = AsyncMock(side_effect=fail)
    stub.aclose = AsyncMock()
    client._client = stub

    with pytest.raises(APIError):
        await client._arequest_impl("GET", "crm/Accounts")

    await client.aclose()


@pytest.mark.asyncio
async def test_arequest_retries_after_retryable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = AsyncExactOnlineClient(settings=_settings(), auth=DummyAuth())

    calls = {"count": 0}

    async def fake_impl(
        method: str, path: str, *, params: Any = None, json: Any = None
    ) -> str:
        calls["count"] += 1
        if calls["count"] == 1:
            raise RateLimitError("limit")
        return "ok"

    monkeypatch.setattr(client, "_arequest_impl", fake_impl)

    result = await client._arequest("GET", "crm/Accounts")
    assert result == "ok"
    assert calls["count"] == 2

    await client.aclose()


@pytest.mark.asyncio
async def test_async_context_manager_calls_aclose(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = AsyncExactOnlineClient(settings=_settings(), auth=DummyAuth())
    original_aclose = client.aclose
    aclose_called = False

    async def wrapped_aclose() -> None:
        nonlocal aclose_called
        aclose_called = True
        await original_aclose()

    monkeypatch.setattr(client, "aclose", wrapped_aclose)

    async with client as ctx:
        assert ctx is client

    assert aclose_called is True


def test_resolve_path_no_division() -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    assert client._resolve_path("crm/Accounts") == "crm/Accounts"
    client.close()


def test_resolve_path_prepends_division() -> None:
    client = ExactOnlineClient(settings=_settings(division=12345), auth=DummyAuth())
    assert client._resolve_path("crm/Accounts") == "12345/crm/Accounts"
    client.close()


def test_resolve_path_replaces_placeholder() -> None:
    client = ExactOnlineClient(settings=_settings(division=99), auth=DummyAuth())
    path = "beta/{division}/budget/BudgetScenarios"
    assert client._resolve_path(path) == "beta/99/budget/BudgetScenarios"
    client.close()


def test_resolve_path_skip_division_with_bang_prefix() -> None:
    client = ExactOnlineClient(settings=_settings(division=12345), auth=DummyAuth())
    assert client._resolve_path("!current/Me") == "current/Me"
    client.close()


def test_resolve_path_skip_division_no_division_set() -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    assert client._resolve_path("!current/Me") == "current/Me"
    client.close()


def test_get_with_division(httpx_mock: HTTPXMock) -> None:
    settings = _settings(division=12345)
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/12345/crm/Accounts",
        json={"value": [{"ID": "1"}]},
    )
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    result = client.get("crm/Accounts")
    assert isinstance(result, list)
    assert result[0]["ID"] == "1"
    client.close()


@pytest.mark.asyncio
async def test_async_resolve_path_prepends_division() -> None:
    client = AsyncExactOnlineClient(
        settings=_settings(division=12345), auth=DummyAuth()
    )
    assert client._resolve_path("crm/Accounts") == "12345/crm/Accounts"
    await client.aclose()


@pytest.mark.asyncio
async def test_async_resolve_path_replaces_placeholder() -> None:
    client = AsyncExactOnlineClient(settings=_settings(division=99), auth=DummyAuth())
    path = "beta/{division}/budget/BudgetScenarios"
    assert client._resolve_path(path) == "beta/99/budget/BudgetScenarios"
    await client.aclose()


@pytest.mark.asyncio
async def test_async_resolve_path_skip_division_with_bang_prefix() -> None:
    client = AsyncExactOnlineClient(
        settings=_settings(division=12345), auth=DummyAuth()
    )
    assert client._resolve_path("!current/Me") == "current/Me"
    await client.aclose()


@pytest.mark.asyncio
async def test_async_resolve_path_skip_division_no_division_set() -> None:
    client = AsyncExactOnlineClient(settings=_settings(), auth=DummyAuth())
    assert client._resolve_path("!current/Me") == "current/Me"
    await client.aclose()


@pytest.mark.asyncio
async def test_async_get_with_division(httpx_mock: HTTPXMock) -> None:
    settings = _settings(division=12345)
    httpx_mock.add_response(
        method="GET",
        url="https://api.example/api/v1/12345/crm/Accounts",
        json={"value": [{"ID": "1"}]},
    )
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    result = await client.get("crm/Accounts")
    assert isinstance(result, list)
    assert result[0]["ID"] == "1"
    await client.aclose()
