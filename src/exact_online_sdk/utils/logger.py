from __future__ import annotations

import json
import logging
import os
import sys
import threading
from datetime import datetime, timezone
from typing import Any, Optional

_SENSITIVE_KEYS = {"authorization", "access_token", "refresh_token", "client_secret"}
_LOGGER_SETUP_LOCK = threading.Lock()


class _RedactFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:  # noqa: D401
        """Redact sensitive fields in record if present in `record.__dict__`."""
        for k in list(record.__dict__.keys()):
            if k.lower() in _SENSITIVE_KEYS and isinstance(record.__dict__[k], str):
                record.__dict__[k] = "<redacted>"
        return True


class _JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:  # noqa: D401
        """Format log record as JSON."""
        payload: dict[str, Any] = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "lineno": record.lineno,
        }
        # Merge any extra fields
        for k, v in record.__dict__.items():
            if k.startswith("_") or k in {
                "args",
                "msg",
                "created",
                "msecs",
                "relativeCreated",
                "levelno",
            }:
                continue
            if k not in payload:
                try:
                    json.dumps(v)  # ensure serializable
                    payload[k] = v
                except Exception:
                    payload[k] = str(v)
        return json.dumps(payload, ensure_ascii=False)


def get_logger(
    name: str = "exact_online_sdk", *, json_output: Optional[bool] = None
) -> logging.Logger:
    """Return configured logger.

    Environment:
    - EXACT_LOG_LEVEL (default INFO)
    - EXACT_LOG_JSON (true/false)
    - EXACT_LOG_FILE (path) optional
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    with _LOGGER_SETUP_LOCK:
        # Double-check after acquiring the lock to avoid duplicate handlers.
        if logger.handlers:
            return logger

        level = os.getenv("EXACT_LOG_LEVEL", "INFO").upper()
        use_json = (
            (os.getenv("EXACT_LOG_JSON", "false").lower() == "true")
            if json_output is None
            else json_output
        )
        log_file = os.getenv("EXACT_LOG_FILE")

        logger.setLevel(level)

        handler: logging.Handler
        if log_file:
            handler = logging.FileHandler(log_file)
        else:
            handler = logging.StreamHandler(sys.stdout)

        formatter: logging.Formatter
        if use_json:
            formatter = _JSONFormatter()
        else:
            formatter = logging.Formatter(
                "%(asctime)s %(levelname)s [%(name)s] %(message)s"
            )

        handler.setFormatter(formatter)
        handler.addFilter(_RedactFilter())
        logger.addHandler(handler)
        logger.propagate = False

    return logger
