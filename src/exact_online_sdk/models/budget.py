from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Budget(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    amount_dc: float = Field(..., alias="AmountDC")
    budget_scenario: Optional[UUID] = Field(None, alias="BudgetScenario")
    budget_scenario_code: Optional[str] = Field(None, alias="BudgetScenarioCode")
    budget_scenario_description: Optional[str] = Field(
        None, alias="BudgetScenarioDescription"
    )
    costcenter: Optional[str] = Field(None, alias="Costcenter")
    costcenter_description: Optional[str] = Field(None, alias="CostcenterDescription")
    costunit: Optional[str] = Field(None, alias="Costunit")
    costunit_description: Optional[str] = Field(None, alias="CostunitDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(None, alias="GLAccountDescription")
    hid: Optional[int] = Field(None, alias="HID")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    reporting_period: Optional[int] = Field(None, alias="ReportingPeriod")
    reporting_year: Optional[int] = Field(None, alias="ReportingYear")
