from __future__ import annotations

from enum import Enum


class SalesOrderStatus(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"

    def __str__(self) -> str:
        return str(self.value)
