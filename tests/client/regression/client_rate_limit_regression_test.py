from __future__ import annotations

from typing import Any, Dict

import pytest

from exact_online_sdk.client import ExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.exceptions import RateLimitError

pytestmark = pytest.mark.regression


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )


def test_retry_on_rate_limit_regression(monkeypatch: pytest.MonkeyPatch) -> None:
    settings = _settings()
    client = ExactOnlineClient(settings=settings)

    calls: Dict[str, int] = {"count": 0}

    def fake_impl(
        method: str, path: str, *, params: Any = None, json: Any = None
    ) -> str:
        calls["count"] += 1
        if calls["count"] == 1:
            raise RateLimitError("limit")
        return "ok"

    monkeypatch.setattr(client, "_request_impl", fake_impl)

    result = client.get("crm/Accounts")

    assert result == "ok"
    assert calls["count"] == 2

    client.close()
