from __future__ import annotations

from enum import Enum


class SalesInvoiceStatus(str, Enum):
    DRAFT = "Draft"
    FINAL = "Final"

    def __str__(self) -> str:
        return str(self.value)
