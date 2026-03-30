from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class HourTypeBudget(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    budget_hours: Optional[float] = Field(None, alias="BudgetHours")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    project: Optional[UUID] = Field(None, alias="Project")
    project_code: Optional[str] = Field(None, alias="ProjectCode")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
