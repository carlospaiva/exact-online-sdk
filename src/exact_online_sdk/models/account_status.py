from __future__ import annotations

from enum import Enum


class AccountStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
