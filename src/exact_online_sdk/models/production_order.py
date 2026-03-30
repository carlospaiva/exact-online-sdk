from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ProductionOrder(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    costcenter: Optional[str] = Field(None, alias="Costcenter")
    costcenter_description: Optional[str] = Field(None, alias="CostcenterDescription")
    costunit: Optional[str] = Field(None, alias="Costunit")
    costunit_description: Optional[str] = Field(None, alias="CostunitDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    entry_date: Optional[datetime] = Field(None, alias="EntryDate")
    is_completed: Optional[int] = Field(None, alias="IsCompleted")
    is_released: Optional[int] = Field(None, alias="IsReleased")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_version: Optional[UUID] = Field(None, alias="ItemVersion")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    planned_date: Optional[datetime] = Field(None, alias="PlannedDate")
    planned_quantity: Optional[float] = Field(None, alias="PlannedQuantity")
    planned_start_date: Optional[datetime] = Field(None, alias="PlannedStartDate")
    produced_quantity: Optional[float] = Field(None, alias="ProducedQuantity")
    project: Optional[UUID] = Field(None, alias="Project")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    quantity_on_sub_order: Optional[float] = Field(None, alias="QuantityOnSubOrder")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
