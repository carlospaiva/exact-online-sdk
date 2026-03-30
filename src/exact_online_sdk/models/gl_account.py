from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class GLAccount(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    code: Optional[str] = Field(default=None, alias="Code")
    description: Optional[str] = Field(default=None, alias="Description")
    allow_costs_in_sales: Optional[bool] = Field(
        default=None, alias="AllowCostsInSales"
    )
    division: Optional[int] = Field(default=None, alias="Division")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    costcenter: Optional[str] = Field(default=None, alias="Costcenter")
    costunit: Optional[str] = Field(default=None, alias="Costunit")
    private_gl_account: Optional[UUID] = Field(default=None, alias="PrivateGLAccount")
    vat_code: Optional[str] = Field(default=None, alias="VATCode")
    vat_non_deductible_gl_account: Optional[UUID] = Field(
        default=None, alias="VATNonDeductibleGLAccount"
    )
    year_end_cost_gl_account: Optional[UUID] = Field(
        default=None, alias="YearEndCostGLAccount"
    )
    year_end_reflection_gl_account: Optional[UUID] = Field(
        default=None, alias="YearEndReflectionGLAccount"
    )
