from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class InventoryItemStorageLocation(StrictModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    id: Optional[UUID] = Field(default=None, alias="ID")
    item: UUID = Field(alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    maximum_stock: Optional[float] = Field(default=None, alias="MaximumStock")
    minimum_stock: Optional[float] = Field(default=None, alias="MinimumStock")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    storage_location: Optional[UUID] = Field(default=None, alias="StorageLocation")
    storage_location_code: Optional[str] = Field(
        default=None,
        alias="StorageLocationCode",
    )
    storage_location_description: Optional[str] = Field(
        default=None,
        alias="StorageLocationDescription",
    )
    type: Optional[int] = Field(default=None, alias="Type")
    warehouse: UUID = Field(alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None,
        alias="WarehouseDescription",
    )
