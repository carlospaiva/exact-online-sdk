from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DeductibilityPercentage(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    expense_non_deductible_percentage: Optional[float] = Field(
        None, alias="ExpenseNonDeductiblePercentage"
    )
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    private_use_percentage: Optional[float] = Field(None, alias="PrivateUsePercentage")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    vat_non_deductible_percentage: Optional[float] = Field(
        None, alias="VATNonDeductiblePercentage"
    )
