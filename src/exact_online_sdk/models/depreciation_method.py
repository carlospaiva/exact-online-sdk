from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DepreciationMethod(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    amount: Optional[float] = Field(None, alias="Amount")
    code: str = Field(..., alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    depreciation_interval: Optional[str] = Field(None, alias="DepreciationInterval")
    description: str = Field(..., alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    max_percentage: Optional[float] = Field(None, alias="MaxPercentage")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    percentage: Optional[float] = Field(None, alias="Percentage")
    percentage2: Optional[float] = Field(None, alias="Percentage2")
    periods: Optional[int] = Field(None, alias="Periods")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    years: Optional[int] = Field(None, alias="Years")
