from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

from .utils.logger import get_logger

DEFAULT_BASE_URL = "https://start.exactonline.nl"
AUTH_PATH = "/api/oauth2/auth"
TOKEN_PATH = "/api/oauth2/token"
DEFAULT_TIMEOUT = 30
USER_AGENT = "exact-online-sdk/1.0.3 (+https://github.com/carlospaiva/exact-online-sdk)"


@dataclass(frozen=True)
class Settings:
    """SDK settings loaded from environment.

    Use `Settings.from_env()` to build an instance. All fields are immutable.
    """

    client_id: str
    client_secret: str
    redirect_uri: str

    base_url: str = DEFAULT_BASE_URL
    auth_url: str = f"{DEFAULT_BASE_URL}{AUTH_PATH}"
    token_url: str = f"{DEFAULT_BASE_URL}{TOKEN_PATH}"

    timeout: int = DEFAULT_TIMEOUT
    user_agent: str = USER_AGENT

    encryption_key: Optional[str] = None
    token_path: Optional[str] = None

    division: Optional[int] = None

    @staticmethod
    def _env(key: str, default: Optional[str] = None) -> str:
        val = os.getenv(key, default)
        if val is None:
            raise ValueError(f"Missing required environment variable: {key}")
        return val

    @classmethod
    def from_env(cls) -> "Settings":
        """Create settings from environment variables and `.env` file."""
        load_dotenv()
        logger = get_logger(__name__)

        base_url = os.getenv("EXACT_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
        auth_url = os.getenv("EXACT_AUTH_URL", f"{base_url}{AUTH_PATH}")
        token_url = os.getenv("EXACT_TOKEN_URL", f"{base_url}{TOKEN_PATH}")

        try:
            settings = cls(
                client_id=cls._env("EXACT_CLIENT_ID"),
                client_secret=cls._env("EXACT_CLIENT_SECRET"),
                redirect_uri=cls._env("EXACT_REDIRECT_URI"),
                base_url=base_url,
                auth_url=auth_url,
                token_url=token_url,
                timeout=int(os.getenv("EXACT_TIMEOUT", str(DEFAULT_TIMEOUT))),
                user_agent=os.getenv("EXACT_USER_AGENT", USER_AGENT),
                encryption_key=os.getenv("EXACT_ENCRYPTION_KEY"),
                token_path=os.getenv("EXACT_TOKEN_PATH"),
                division=(
                    int(division_env)
                    if (division_env := os.getenv("EXACT_DIVISION"))
                    else None
                ),
            )
        except Exception:  # pragma: no cover
            logger.error("Failed to load settings", exc_info=True)
            raise
        return settings
