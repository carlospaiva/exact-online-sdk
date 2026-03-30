"""Optional contrib integrations (AWS, etc.)."""

from .aws import ReadOnlyTokenStorage, SecretsManagerTokenStorage

__all__ = ["ReadOnlyTokenStorage", "SecretsManagerTokenStorage"]
