from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AllocationRule(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_bank_account: Optional[str] = Field(None, alias="AccountBankAccount")
    costcenter: Optional[str] = Field(None, alias="Costcenter")
    costunit: Optional[str] = Field(None, alias="Costunit")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    division: Optional[int] = Field(None, alias="Division")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    vat_code: Optional[str] = Field(None, alias="VATCode")
    words: Optional[str] = Field(None, alias="Words")
