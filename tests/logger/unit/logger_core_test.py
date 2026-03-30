from __future__ import annotations

import io
import json
import logging
import sys
from pathlib import Path
from typing import Iterable
from uuid import uuid4

import pytest

from exact_online_sdk.utils.logger import _JSONFormatter, _RedactFilter, get_logger


@pytest.fixture
def cleanup_loggers() -> Iterable[list[logging.Logger]]:
    created: list[logging.Logger] = []
    yield created
    for logger in created:
        for handler in list(logger.handlers):
            logger.removeHandler(handler)
            handler.close()
        logger.setLevel(logging.NOTSET)


def _make_record(**extra: object) -> logging.LogRecord:
    record = logging.LogRecord(
        name="tests",
        level=logging.INFO,
        pathname=__file__,
        lineno=42,
        msg="hello %s",
        args=("world",),
        exc_info=None,
    )
    for key, value in extra.items():
        setattr(record, key, value)
    return record


def test_redact_filter_masks_sensitive_fields() -> None:
    record = _make_record(
        Authorization="Bearer secret", client_secret="top", visible="ok"
    )
    redact_filter = _RedactFilter()

    assert redact_filter.filter(record) is True
    assert getattr(record, "Authorization") == "<redacted>"
    assert getattr(record, "client_secret") == "<redacted>"
    assert getattr(record, "visible") == "ok"


def test_json_formatter_serializes_extra_fields() -> None:
    formatter = _JSONFormatter()
    record = _make_record(custom={"id": 1}, non_serializable=object(), _internal="skip")

    payload = json.loads(formatter.format(record))

    assert payload["message"] == "hello world"
    assert payload["custom"] == {"id": 1}
    assert isinstance(payload["non_serializable"], str)
    assert "_internal" not in payload


def test_get_logger_stream_handler_respects_env(
    monkeypatch: pytest.MonkeyPatch, cleanup_loggers: list[logging.Logger]
) -> None:
    monkeypatch.setenv("EXACT_LOG_LEVEL", "debug")
    monkeypatch.delenv("EXACT_LOG_JSON", raising=False)
    monkeypatch.delenv("EXACT_LOG_FILE", raising=False)

    fake_stdout = io.StringIO()
    monkeypatch.setattr(sys, "stdout", fake_stdout)

    name = f"exact_online_sdk.tests.stream.{uuid4()}"
    logger = get_logger(name)
    cleanup_loggers.append(logger)

    logger.debug("plain output")

    output = fake_stdout.getvalue()
    assert "DEBUG" in output
    assert "plain output" in output


def test_get_logger_file_handler_emits_json(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    cleanup_loggers: list[logging.Logger],
) -> None:
    log_path = tmp_path / "sdk.log"
    monkeypatch.setenv("EXACT_LOG_FILE", str(log_path))
    monkeypatch.setenv("EXACT_LOG_JSON", "true")
    monkeypatch.setenv("EXACT_LOG_LEVEL", "info")

    name = f"exact_online_sdk.tests.file.{uuid4()}"
    logger = get_logger(name)
    cleanup_loggers.append(logger)

    logger.info(
        "payload",
        extra={
            "access_token": "secret",
            "details": {"foo": "bar"},
            "not_json": object(),
        },
    )
    for handler in logger.handlers:
        handler.flush()

    data = json.loads(log_path.read_text())
    assert data["message"] == "payload"
    assert data["access_token"] == "<redacted>"
    assert data["details"] == {"foo": "bar"}
    assert isinstance(data["not_json"], str)


def test_get_logger_returns_existing_instance(
    cleanup_loggers: list[logging.Logger],
) -> None:
    name = f"exact_online_sdk.tests.reuse.{uuid4()}"
    logger_first = get_logger(name, json_output=True)
    cleanup_loggers.append(logger_first)

    handler_count = len(logger_first.handlers)
    logger_second = get_logger(name, json_output=False)

    assert logger_first is logger_second
    assert len(logger_second.handlers) == handler_count
