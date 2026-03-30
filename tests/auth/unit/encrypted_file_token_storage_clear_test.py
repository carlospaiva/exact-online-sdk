from __future__ import annotations

from pathlib import Path

from cryptography.fernet import Fernet

from exact_online_sdk.auth import EncryptedFileTokenStorage


def test_clear_handles_missing_file(tmp_path: Path) -> None:
    key = Fernet.generate_key().decode("utf-8")
    path = tmp_path / "missing-token.enc"

    storage = EncryptedFileTokenStorage(path, key)

    storage.clear()

    assert not path.exists()
