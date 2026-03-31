from __future__ import annotations

from typing import Optional
from unittest.mock import MagicMock

import httpx
import pytest

from exact_online_sdk.client import ExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import APIError


class DummyAuth:
    def __init__(self) -> None:
        self.called = 0

    def get_access_token(self) -> str:
        self.called += 1
        return "token"


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )


def _response(
    status: int, url: str, *, headers: Optional[dict[str, str]] = None
) -> httpx.Response:
    request = httpx.Request("GET", url)
    return httpx.Response(status, text="body", headers=headers or {}, request=request)


def test_handle_response_includes_request_id_in_error_context() -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    req = httpx.Request("GET", "https://api.example/api/v1/crm/Accounts")

    resp = httpx.Response(
        500,
        text="boom",
        headers={"Exact-Request-ID": "req-123"},
        request=req,
    )

    with pytest.raises(APIError) as exc:
        client._handle_response(resp)

    assert exc.value.context.get("request_id") == "req-123"

    client.close()


def test_iter_pages_error_includes_request_id_in_context(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = ExactOnlineClient(settings=_settings(), auth=DummyAuth())
    error = _response(
        500,
        "https://api.example/api/v1/crm/Accounts",
        headers={"Exact-Request-ID": "iter-456"},
    )

    stub = MagicMock()
    stub.request.return_value = error
    client._client = stub

    iterator = client.iter_pages("crm/Accounts")
    with pytest.raises(APIError) as exc:
        next(iterator)

    assert exc.value.context.get("request_id") == "iter-456"

    client.close()
