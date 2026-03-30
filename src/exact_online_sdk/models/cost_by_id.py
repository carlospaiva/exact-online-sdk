from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class CostById(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_id: Optional[UUID] = Field(None, alias="AccountId")
    account_name: Optional[str] = Field(None, alias="AccountName")
    amount_approved: Optional[float] = Field(None, alias="AmountApproved")
    amount_draft: Optional[float] = Field(None, alias="AmountDraft")
    amount_rejected: Optional[float] = Field(None, alias="AmountRejected")
    amount_submitted: Optional[float] = Field(None, alias="AmountSubmitted")
    currency_code: Optional[str] = Field(None, alias="CurrencyCode")
    date: Optional[datetime] = Field(None, alias="Date")
    entry_id: Optional[UUID] = Field(None, alias="EntryId")
    expense: Optional[str] = Field(None, alias="Expense")
    expense_description: Optional[str] = Field(None, alias="ExpenseDescription")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    notes: Optional[str] = Field(None, alias="Notes")
    project_code: Optional[str] = Field(None, alias="ProjectCode")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    project_id: Optional[UUID] = Field(None, alias="ProjectId")
    quantity_approved: Optional[float] = Field(None, alias="QuantityApproved")
    quantity_draft: Optional[float] = Field(None, alias="QuantityDraft")
    quantity_rejected: Optional[float] = Field(None, alias="QuantityRejected")
    quantity_submitted: Optional[float] = Field(None, alias="QuantitySubmitted")
    week_number: Optional[int] = Field(None, alias="WeekNumber")
