from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ShopOrderSubOrder(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    entry_date: Optional[datetime] = Field(None, alias="EntryDate")
    id: Optional[UUID] = Field(None, alias="ID")
    is_completed: Optional[int] = Field(None, alias="IsCompleted")
    is_released: Optional[int] = Field(None, alias="IsReleased")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    planned_date: Optional[datetime] = Field(None, alias="PlannedDate")
    planned_quantity: Optional[float] = Field(None, alias="PlannedQuantity")
    planned_start_date: Optional[datetime] = Field(None, alias="PlannedStartDate")
    produced_quantity: Optional[float] = Field(None, alias="ProducedQuantity")
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    shop_order_parent: Optional[UUID] = Field(None, alias="ShopOrderParent")
    shop_order_parent_number: Optional[int] = Field(None, alias="ShopOrderParentNumber")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
