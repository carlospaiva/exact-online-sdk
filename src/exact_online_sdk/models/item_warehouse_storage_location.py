from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemWarehouseStorageLocation(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    is_fraction_allowed_item: Optional[int] = Field(
        default=None, alias="IsFractionAllowedItem"
    )
    is_stock_item: Optional[int] = Field(default=None, alias="IsStockItem")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_barcode: Optional[str] = Field(default=None, alias="ItemBarcode")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_end_date: Optional[datetime] = Field(default=None, alias="ItemEndDate")
    item_start_date: Optional[datetime] = Field(default=None, alias="ItemStartDate")
    item_unit: Optional[str] = Field(default=None, alias="ItemUnit")
    item_unit_description: Optional[str] = Field(
        default=None, alias="ItemUnitDescription"
    )
    stock: Optional[float] = Field(default=None, alias="Stock")
    storage_location: Optional[UUID] = Field(default=None, alias="StorageLocation")
    storage_location_code: Optional[str] = Field(
        default=None, alias="StorageLocationCode"
    )
    storage_location_description: Optional[str] = Field(
        default=None, alias="StorageLocationDescription"
    )
    storage_location_sequence_number: Optional[int] = Field(
        default=None, alias="StorageLocationSequenceNumber"
    )
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
