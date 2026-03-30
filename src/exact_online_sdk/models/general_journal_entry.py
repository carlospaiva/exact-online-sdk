from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class GeneralJournalEntry(StrictModel):
    entry_id: Optional[UUID] = Field(None, alias="EntryID")
    created: Optional[datetime] = Field(None, alias="Created")
    currency: Optional[str] = Field(None, alias="Currency")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    division: Optional[int] = Field(None, alias="Division")
    entry_number: Optional[int] = Field(None, alias="EntryNumber")
    exchange_rate: Optional[float] = Field(None, alias="ExchangeRate")
    financial_period: Optional[int] = Field(None, alias="FinancialPeriod")
    financial_year: Optional[int] = Field(None, alias="FinancialYear")
    journal_code: Optional[str] = Field(None, alias="JournalCode")
    journal_description: Optional[str] = Field(None, alias="JournalDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    reversal: Optional[bool] = Field(None, alias="Reversal")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
