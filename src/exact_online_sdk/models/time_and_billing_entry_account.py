from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class TimeAndBillingEntryAccount(StrictModel):
    account_id: Optional[UUID] = Field(None, alias="AccountId")
    account_name: Optional[str] = Field(None, alias="AccountName")
