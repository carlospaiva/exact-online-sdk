from __future__ import annotations

from typing import Optional

import pytest

from exact_online_sdk.config import Settings


def test_settings_from_env_loads_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("EXACT_CLIENT_ID", "id")
    monkeypatch.setenv("EXACT_CLIENT_SECRET", "secret")
    monkeypatch.setenv("EXACT_REDIRECT_URI", "https://app.example/callback")
    monkeypatch.setenv(
        "EXACT_BASE_URL", "https://api.example/"
    )  # trailing slash trimmed
    monkeypatch.setenv("EXACT_TIMEOUT", "45")
    monkeypatch.setenv("EXACT_USER_AGENT", "custom-agent")
    monkeypatch.setenv("EXACT_ENCRYPTION_KEY", "key")
    monkeypatch.setenv("EXACT_TOKEN_PATH", "~/.tokens/exact.json")
    monkeypatch.setenv("EXACT_DIVISION", "12345")

    monkeypatch.setenv("EXACT_AUTH_URL", "https://auth.example/custom")
    monkeypatch.setenv("EXACT_TOKEN_URL", "https://auth.example/token")

    monkeypatch.setattr("exact_online_sdk.config.load_dotenv", lambda: None)

    settings = Settings.from_env()

    assert settings.base_url == "https://api.example"
    assert settings.auth_url == "https://auth.example/custom"
    assert settings.token_url == "https://auth.example/token"
    assert settings.timeout == 45
    assert settings.user_agent == "custom-agent"
    assert settings.encryption_key == "key"
    assert settings.token_path == "~/.tokens/exact.json"
    assert settings.division == 12345


@pytest.mark.parametrize(
    ("env_key", "default", "expected"),
    [
        ("EXACT_BASE_URL", None, "https://api.example"),
        ("EXACT_TIMEOUT", "30", "30"),
    ],
)
def test_env_helper_returns_value(
    monkeypatch: pytest.MonkeyPatch, env_key: str, default: Optional[str], expected: str
) -> None:
    monkeypatch.setenv(env_key, expected)
    assert Settings._env(env_key, default) == expected


def test_settings_from_env_division_defaults_to_none(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("EXACT_CLIENT_ID", "id")
    monkeypatch.setenv("EXACT_CLIENT_SECRET", "secret")
    monkeypatch.setenv("EXACT_REDIRECT_URI", "https://app.example/callback")
    monkeypatch.delenv("EXACT_DIVISION", raising=False)

    monkeypatch.setattr("exact_online_sdk.config.load_dotenv", lambda: None)

    settings = Settings.from_env()
    assert settings.division is None


def test_settings_from_env_missing_env_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("EXACT_CLIENT_ID", raising=False)
    monkeypatch.delenv("EXACT_CLIENT_SECRET", raising=False)
    monkeypatch.delenv("EXACT_REDIRECT_URI", raising=False)

    monkeypatch.setattr("exact_online_sdk.config.load_dotenv", lambda: None)
    monkeypatch.setenv("EXACT_CLIENT_SECRET", "secret")
    monkeypatch.setenv("EXACT_REDIRECT_URI", "https://app.example/callback")

    with pytest.raises(ValueError):
        Settings.from_env()
