from __future__ import annotations

import logging
import threading
from typing import Iterable
from uuid import uuid4

import pytest

from exact_online_sdk.utils.logger import _LOGGER_SETUP_LOCK, get_logger


@pytest.fixture
def cleanup_loggers() -> Iterable[list[logging.Logger]]:
    created: list[logging.Logger] = []
    yield created
    for logger in created:
        for handler in list(logger.handlers):
            logger.removeHandler(handler)
            handler.close()
        logger.setLevel(logging.NOTSET)


def test_get_logger_concurrent_no_duplicate_handlers(
    cleanup_loggers: list[logging.Logger],
) -> None:
    """Calling get_logger from many threads must add exactly one handler."""
    name = f"exact_online_sdk.tests.threadsafe.{uuid4()}"
    loggers: list[logging.Logger] = []
    errors: list[Exception] = []

    def worker() -> None:
        try:
            lg = get_logger(name)
            loggers.append(lg)
        except Exception as exc:
            errors.append(exc)

    threads = [threading.Thread(target=worker) for _ in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []
    assert len(loggers) == 20

    # All should be the same instance
    assert all(lg is loggers[0] for lg in loggers)

    # Exactly one handler should have been added
    cleanup_loggers.append(loggers[0])
    assert len(loggers[0].handlers) == 1


def test_get_logger_double_check_lock_returns_early(
    cleanup_loggers: list[logging.Logger],
) -> None:
    """Force the double-check branch inside _LOGGER_SETUP_LOCK.

    Simulate a race where another thread adds a handler between the outer
    ``if logger.handlers`` check and the lock acquisition.
    """
    name = f"exact_online_sdk.tests.doublecheck.{uuid4()}"
    logger = logging.getLogger(name)

    # Pre-add a handler so the inner check (line 72) triggers the early return.
    sentinel_handler = logging.StreamHandler()
    logger.addHandler(sentinel_handler)
    cleanup_loggers.append(logger)

    # get_logger sees no handlers on the *fast path* (we bypass it by
    # temporarily removing the handler, calling get_logger, then verifying).
    # Actually, the simplest way: just call get_logger while handler exists.
    # The outer fast-path returns immediately — but if we clear handlers
    # right before and then re-add inside the lock window, we can't control
    # that reliably. Instead, we test by acquiring the lock ourselves first,
    # starting get_logger in another thread (it will block), adding a handler,
    # then releasing the lock.

    logger.removeHandler(sentinel_handler)
    assert len(logger.handlers) == 0

    result_holder: list[logging.Logger] = []

    with _LOGGER_SETUP_LOCK:
        # Start get_logger in another thread — it will pass the outer check
        # (no handlers) but block on the lock.
        t = threading.Thread(target=lambda: result_holder.append(get_logger(name)))
        t.start()

        # Give the thread time to reach the lock
        import time

        time.sleep(0.05)

        # Sneak a handler in while we hold the lock
        logger.addHandler(sentinel_handler)

    # Lock released — thread proceeds, hits inner check, returns early
    t.join(timeout=2)
    assert len(result_holder) == 1
    assert result_holder[0] is logger
    # Should still have exactly the one sentinel handler (no duplicate added)
    assert len(logger.handlers) == 1
