from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class InventoryItemWarehouse(StrictModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    counting_cycle: Optional[int] = Field(default=None, alias="CountingCycle")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    default_storage_location: Optional[UUID] = Field(
        default=None,
        alias="DefaultStorageLocation",
    )
    default_storage_location_code: Optional[str] = Field(
        default=None,
        alias="DefaultStorageLocationCode",
    )
    default_storage_location_description: Optional[str] = Field(
        default=None,
        alias="DefaultStorageLocationDescription",
    )
    division: Optional[int] = Field(default=None, alias="Division")
    id: Optional[UUID] = Field(default=None, alias="ID")
    item: UUID = Field(alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    maximum_stock: Optional[float] = Field(default=None, alias="MaximumStock")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    order_policy: Optional[int] = Field(default=None, alias="OrderPolicy")
    period: Optional[int] = Field(default=None, alias="Period")
    reorder_point: Optional[float] = Field(default=None, alias="ReorderPoint")
    reorder_quantity: Optional[float] = Field(default=None, alias="ReorderQuantity")
    replenishment_type: Optional[int] = Field(default=None, alias="ReplenishmentType")
    reserved_stock: Optional[float] = Field(default=None, alias="ReservedStock")
    safety_stock: Optional[float] = Field(default=None, alias="SafetyStock")
    storage_location_sequence_number: Optional[int] = Field(
        default=None,
        alias="StorageLocationSequenceNumber",
    )
    warehouse: UUID = Field(alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None,
        alias="WarehouseDescription",
    )
