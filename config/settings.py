"""Top-level settings defaults and constants.
This module complements `src/exact_online_sdk/config.py` which performs validation
and environment loading. Keep this file framework-agnostic.
"""

from __future__ import annotations

DEFAULT_BASE_URL = "https://start.exactonline.nl"
AUTH_PATH = "/api/oauth2/auth"
TOKEN_PATH = "/api/oauth2/token"
DEFAULT_TIMEOUT = 30
USER_AGENT = "exact-online-sdk/1.0.6 (+https://github.com/carlospaiva/exact-online-sdk)"
