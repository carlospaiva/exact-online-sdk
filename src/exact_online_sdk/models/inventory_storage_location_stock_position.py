from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class InventoryStorageLocationStockPosition(StrictModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    division: Optional[int] = Field(default=None, alias="Division")
    id: Optional[UUID] = Field(default=None, alias="ID")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    quantity_to_picked: Optional[float] = Field(default=None, alias="QuantityToPicked")
    reserved_pick: Optional[float] = Field(default=None, alias="ReservedPick")
    serial_batch_reserved_stock: Optional[float] = Field(
        default=None,
        alias="SerialBatchReservedStock",
    )
    stock: Optional[float] = Field(default=None, alias="Stock")
    storage_location: Optional[UUID] = Field(default=None, alias="StorageLocation")
    storage_location_code: Optional[str] = Field(
        default=None,
        alias="StorageLocationCode",
    )
    storage_location_description: Optional[str] = Field(
        default=None,
        alias="StorageLocationDescription",
    )
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None,
        alias="WarehouseDescription",
    )
