from __future__ import annotations

import asyncio
import threading
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from exact_online_sdk.client import AsyncExactOnlineClient, ExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import RateLimitError


class DummyAuth:
    def __init__(self) -> None:
        self.called = 0

    def get_access_token(self) -> str:
        self.called += 1
        return "token"

    async def aget_access_token(self) -> str:
        self.called += 1
        return "token"


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )


# ---------------------------------------------------------------------------
# ExactOnlineClient — sync thread-safety
# ---------------------------------------------------------------------------


def test_concurrent_get_requests_are_safe(httpx_mock: "Any") -> None:
    """Multiple threads calling .get() must not corrupt the httpx.Client."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    errors: list[Exception] = []
    results: list[Any] = []

    # Use a mock client that is thread-safe (returns canned responses)
    call_count = {"n": 0}
    lock = threading.Lock()

    def safe_request(*args: Any, **kwargs: Any) -> httpx.Response:
        with lock:
            call_count["n"] += 1
        return httpx.Response(
            200,
            json={"value": [{"ID": str(call_count["n"])}]},
            request=httpx.Request("GET", str(args[1]) if len(args) > 1 else ""),
        )

    client._client = MagicMock()
    client._client.request.side_effect = safe_request

    def worker() -> None:
        try:
            result = client.get("crm/Accounts")
            results.append(result)
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []
    assert len(results) == 20
    for r in results:
        assert isinstance(r, list)

    client.close()


def test_concurrent_post_requests_are_safe() -> None:
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    errors: list[Exception] = []

    def safe_request(*args: Any, **kwargs: Any) -> httpx.Response:
        return httpx.Response(
            200,
            json={"d": {"results": []}},
            request=httpx.Request("POST", str(args[1]) if len(args) > 1 else ""),
        )

    client._client = MagicMock()
    client._client.request.side_effect = safe_request

    def worker() -> None:
        try:
            client.post("crm/Accounts", json={"Name": "Test"})
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []
    client.close()


def test_http_lock_attribute_exists() -> None:
    """ExactOnlineClient must have an _http_lock for thread-safe HTTP access."""
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())
    assert hasattr(client, "_http_lock")
    assert isinstance(client._http_lock, type(threading.Lock()))
    client.close()


# ---------------------------------------------------------------------------
# AsyncExactOnlineClient — 429 no longer recreates client
# ---------------------------------------------------------------------------


async def test_arequest_impl_429_does_not_recreate_client() -> None:
    """On 429, the async client should sleep but NOT close/recreate self._client."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())
    original_client = client._client

    req = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")
    resp = httpx.Response(429, headers={"Retry-After": "0"}, request=req)

    async def fake_request(*args: Any, **kwargs: Any) -> httpx.Response:
        return resp

    client._client = MagicMock()
    client._client.request = fake_request

    client_before = client._client
    with pytest.raises(RateLimitError):
        await client._arequest_impl("GET", "crm/Accounts")

    # The client reference should NOT have changed (no recreation)
    assert client._client is client_before

    await original_client.aclose()


async def test_concurrent_async_get_requests() -> None:
    """Multiple async tasks calling .get() concurrently should be safe."""
    settings = _settings()
    client = AsyncExactOnlineClient(settings=settings, auth=DummyAuth())

    call_count = {"n": 0}

    async def fake_request(*args: Any, **kwargs: Any) -> httpx.Response:
        call_count["n"] += 1
        await asyncio.sleep(0)
        return httpx.Response(
            200,
            json={"value": [{"ID": str(call_count["n"])}]},
            request=httpx.Request("GET", str(args[1]) if len(args) > 1 else ""),
        )

    client._client = MagicMock()
    client._client.request = fake_request
    client._client.aclose = AsyncMock()

    results = await asyncio.gather(*[client.get("crm/Accounts") for _ in range(10)])

    assert len(results) == 10
    for r in results:
        assert isinstance(r, list)
