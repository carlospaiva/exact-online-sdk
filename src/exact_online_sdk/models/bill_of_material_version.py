from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class BillOfMaterialVersion(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    batch_quantity: Optional[float] = Field(None, alias="BatchQuantity")
    cad_drawing_url: Optional[str] = Field(None, alias="CadDrawingUrl")
    calculated_cost_price: Optional[float] = Field(None, alias="CalculatedCostPrice")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    is_default: Optional[int] = Field(None, alias="IsDefault")
    item: Optional[UUID] = Field(None, alias="Item")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    order_lead_days: Optional[int] = Field(None, alias="OrderLeadDays")
    production_lead_days: Optional[int] = Field(None, alias="ProductionLeadDays")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    version_date: Optional[datetime] = Field(None, alias="VersionDate")
    version_number: Optional[int] = Field(None, alias="VersionNumber")
