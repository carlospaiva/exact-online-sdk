from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class CommercialBuildingValue(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    asset: Optional[UUID] = Field(None, alias="Asset")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    minimum_value: Optional[float] = Field(None, alias="MinimumValue")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    property_value: Optional[float] = Field(None, alias="PropertyValue")
    property_value_option: Optional[int] = Field(None, alias="PropertyValueOption")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
