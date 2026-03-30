from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ProductionArea(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    code: Optional[str] = Field(None, alias="Code")
    cost_center: Optional[str] = Field(None, alias="Costcenter")
    cost_center_description: Optional[str] = Field(None, alias="CostcenterDescription")
    cost_unit: Optional[str] = Field(None, alias="Costunit")
    cost_unit_description: Optional[str] = Field(None, alias="CostunitDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    is_default: Optional[int] = Field(None, alias="IsDefault")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
