from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ReportingBalance(StrictModel):
    id: Optional[int] = Field(None, alias="ID")
    amount: Optional[float] = Field(None, alias="Amount")
    amount_credit: Optional[float] = Field(None, alias="AmountCredit")
    amount_debit: Optional[float] = Field(None, alias="AmountDebit")
    balance_type: Optional[str] = Field(None, alias="BalanceType")
    cost_center_code: Optional[str] = Field(None, alias="CostCenterCode")
    cost_center_description: Optional[str] = Field(None, alias="CostCenterDescription")
    cost_unit_code: Optional[str] = Field(None, alias="CostUnitCode")
    cost_unit_description: Optional[str] = Field(None, alias="CostUnitDescription")
    count: Optional[int] = Field(None, alias="Count")
    division: Optional[int] = Field(None, alias="Division")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(None, alias="GLAccountDescription")
    reporting_period: Optional[int] = Field(None, alias="ReportingPeriod")
    reporting_year: Optional[int] = Field(None, alias="ReportingYear")
    status: Optional[int] = Field(None, alias="Status")
    type: Optional[int] = Field(None, alias="Type")
