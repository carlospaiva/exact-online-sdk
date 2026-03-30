from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class PaymentCondition(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    code: str = Field(..., alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    credit_management_scenario: Optional[UUID] = Field(
        None, alias="CreditManagementScenario"
    )
    credit_management_scenario_code: Optional[str] = Field(
        None, alias="CreditManagementScenarioCode"
    )
    credit_management_scenario_description: Optional[str] = Field(
        None, alias="CreditManagementScenarioDescription"
    )
    description: str = Field(..., alias="Description")
    discount_calculation: Optional[str] = Field(None, alias="DiscountCalculation")
    discount_payment_days: Optional[int] = Field(None, alias="DiscountPaymentDays")
    discount_percentage: Optional[float] = Field(None, alias="DiscountPercentage")
    division: Optional[int] = Field(None, alias="Division")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    payment_days: Optional[int] = Field(None, alias="PaymentDays")
    payment_discount_type: Optional[str] = Field(None, alias="PaymentDiscountType")
    payment_end_of_months: Optional[int] = Field(None, alias="PaymentEndOfMonths")
    payment_method: Optional[str] = Field(None, alias="PaymentMethod")
    percentage: Optional[float] = Field(None, alias="Percentage")
    vat_calculation: Optional[str] = Field(None, alias="VATCalculation")
