from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemVersion(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    batch_quantity: Optional[float] = Field(default=None, alias="BatchQuantity")
    calculated_cost_price: Optional[float] = Field(
        default=None, alias="CalculatedCostPrice"
    )
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    description: str = Field(alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    is_default: Optional[int] = Field(default=None, alias="IsDefault")
    item: UUID = Field(alias="Item")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    lead_time: Optional[int] = Field(default=None, alias="LeadTime")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    notes: Optional[str] = Field(default=None, alias="Notes")
    status: Optional[int] = Field(default=None, alias="Status")
    status_description: Optional[str] = Field(default=None, alias="StatusDescription")
    type: Optional[int] = Field(default=None, alias="Type")
    type_description: Optional[str] = Field(default=None, alias="TypeDescription")
    version_date: Optional[datetime] = Field(default=None, alias="VersionDate")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
