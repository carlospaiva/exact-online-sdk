from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Costcenter(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    active: Optional[bool] = Field(None, alias="Active")
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
