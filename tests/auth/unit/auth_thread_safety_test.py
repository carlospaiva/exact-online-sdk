from __future__ import annotations

import asyncio
import threading
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

import httpx

from exact_online_sdk.auth import (
    EncryptedFileTokenStorage,
    ExactOnlineAuth,
    InMemoryTokenStorage,
    Token,
)
from exact_online_sdk.config import Settings


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
    )


def _valid_token(*, expired: bool = False) -> Token:
    offset = timedelta(minutes=-5) if expired else timedelta(minutes=30)
    return Token(
        access_token="access",
        token_type="Bearer",
        refresh_token="refresh",
        expires_at=datetime.now(timezone.utc) + offset,
    )


# ---------------------------------------------------------------------------
# InMemoryTokenStorage thread-safety
# ---------------------------------------------------------------------------


def test_in_memory_storage_concurrent_set_and_get() -> None:
    """Multiple threads setting and getting tokens should not corrupt state."""
    storage = InMemoryTokenStorage()
    errors: list[Exception] = []

    def worker(i: int) -> None:
        try:
            tok = Token(
                access_token=f"tok-{i}",
                token_type="Bearer",
                expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
            )
            storage.set_token(tok)
            result = storage.get_token()
            assert result is not None
            assert result.access_token.startswith("tok-")
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []


def test_in_memory_storage_concurrent_clear() -> None:
    storage = InMemoryTokenStorage()
    storage.set_token(_valid_token())
    errors: list[Exception] = []

    def worker() -> None:
        try:
            storage.clear()
            storage.get_token()  # Should be None or a Token, never crash
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []


# ---------------------------------------------------------------------------
# EncryptedFileTokenStorage thread-safety
# ---------------------------------------------------------------------------


def test_encrypted_storage_concurrent_set_and_get(tmp_path: "object") -> None:
    from pathlib import Path

    from cryptography.fernet import Fernet

    key = Fernet.generate_key().decode()
    path = Path(str(tmp_path)) / "token.enc"
    storage = EncryptedFileTokenStorage(path, key)
    errors: list[Exception] = []

    def worker(i: int) -> None:
        try:
            tok = Token(
                access_token=f"enc-tok-{i}",
                token_type="Bearer",
                refresh_token=f"ref-{i}",
                expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
            )
            storage.set_token(tok)
            result = storage.get_token()
            assert result is not None
            assert result.access_token.startswith("enc-tok-")
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []


# ---------------------------------------------------------------------------
# ExactOnlineAuth sync thread-safety
# ---------------------------------------------------------------------------


def test_get_access_token_concurrent_no_race() -> None:
    """Concurrent get_access_token calls must not raise or corrupt state."""
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(_valid_token())
    auth = ExactOnlineAuth(settings, storage=storage)
    errors: list[Exception] = []
    results: list[str] = []

    def worker() -> None:
        try:
            token = auth.get_access_token()
            results.append(token)
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []
    assert all(r == "access" for r in results)


def test_refresh_token_concurrent_serialized() -> None:
    """Concurrent refresh_token calls should be serialized by the lock."""
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(_valid_token())
    auth = ExactOnlineAuth(settings, storage=storage)

    call_count = {"n": 0}

    def fake_post(*args: object, **kwargs: object) -> httpx.Response:
        call_count["n"] += 1
        return httpx.Response(
            200,
            json={
                "access_token": f"new-{call_count['n']}",
                "token_type": "Bearer",
                "refresh_token": "new-refresh",
                "expires_in": 3600,
            },
            request=httpx.Request("POST", str(args[0]) if args else ""),
        )

    errors: list[Exception] = []

    def worker() -> None:
        try:
            with patch("exact_online_sdk.auth.httpx.post", side_effect=fake_post):
                auth.refresh_token()
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []
    result = storage.get_token()
    assert result is not None
    assert result.access_token.startswith("new-")


# ---------------------------------------------------------------------------
# ExactOnlineAuth async task-safety
# ---------------------------------------------------------------------------


async def test_aget_access_token_concurrent_tasks() -> None:
    """Concurrent async get_access_token calls should be serialized."""
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(_valid_token())
    auth = ExactOnlineAuth(settings, storage=storage)

    results = await asyncio.gather(*[auth.aget_access_token() for _ in range(10)])
    assert all(r == "access" for r in results)


async def test_arefresh_token_concurrent_tasks() -> None:
    """Concurrent async refresh calls should be serialized by the async lock."""
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(_valid_token())
    auth = ExactOnlineAuth(settings, storage=storage)

    call_count = {"n": 0}

    async def fake_post(self: object, url: object, **kwargs: object) -> httpx.Response:
        call_count["n"] += 1
        await asyncio.sleep(0)  # yield to event loop
        return httpx.Response(
            200,
            json={
                "access_token": f"async-new-{call_count['n']}",
                "token_type": "Bearer",
                "refresh_token": "async-refresh",
                "expires_in": 3600,
            },
            request=httpx.Request("POST", str(url)),
        )

    with patch.object(httpx.AsyncClient, "post", new=fake_post):
        results = await asyncio.gather(*[auth.arefresh_token() for _ in range(5)])

    assert len(results) == 5
    for tok in results:
        assert tok.access_token.startswith("async-new-")


async def test_aget_access_token_refreshes_expired_without_deadlock() -> None:
    """aget_access_token -> _arefresh_token_unlocked must not deadlock."""
    settings = _settings()
    storage = InMemoryTokenStorage()
    storage.set_token(_valid_token(expired=True))
    auth = ExactOnlineAuth(settings, storage=storage)

    async def fake_post(self: object, url: object, **kwargs: object) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "access_token": "refreshed",
                "token_type": "Bearer",
                "refresh_token": "new-refresh",
                "expires_in": 3600,
            },
            request=httpx.Request("POST", str(url)),
        )

    with patch.object(httpx.AsyncClient, "post", new=fake_post):
        token = await auth.aget_access_token()

    assert token == "refreshed"
