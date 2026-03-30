from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class CashEntry(StrictModel):
    entry_id: Optional[UUID] = Field(None, alias="EntryID")
    closing_balance_fc: Optional[float] = Field(None, alias="ClosingBalanceFC")
    created: Optional[datetime] = Field(None, alias="Created")
    currency: Optional[str] = Field(None, alias="Currency")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    division: Optional[int] = Field(None, alias="Division")
    entry_number: Optional[int] = Field(None, alias="EntryNumber")
    financial_period: Optional[int] = Field(None, alias="FinancialPeriod")
    financial_year: Optional[int] = Field(None, alias="FinancialYear")
    journal_code: Optional[str] = Field(None, alias="JournalCode")
    journal_description: Optional[str] = Field(None, alias="JournalDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    opening_balance_fc: Optional[float] = Field(None, alias="OpeningBalanceFC")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
