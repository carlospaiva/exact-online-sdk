from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class StockCountLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    batch_numbers: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="BatchNumbers"
    )
    cost_price: Optional[float] = Field(default=None, alias="CostPrice")
    counted_by: Optional[UUID] = Field(default=None, alias="CountedBy")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    item: UUID = Field(alias="Item")
    item_barcode: Optional[str] = Field(default=None, alias="ItemBarcode")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_cost_price: Optional[float] = Field(default=None, alias="ItemCostPrice")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_divisable: Optional[bool] = Field(default=None, alias="ItemDivisable")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    quantity_difference: Optional[float] = Field(
        default=None, alias="QuantityDifference"
    )
    quantity_in_stock: Optional[float] = Field(default=None, alias="QuantityInStock")
    quantity_new: Optional[float] = Field(default=None, alias="QuantityNew")
    reason_code: Optional[str] = Field(default=None, alias="ReasonCode")
    reason_code_description: Optional[str] = Field(
        default=None, alias="ReasonCodeDescription"
    )
    reason_code_id: Optional[UUID] = Field(default=None, alias="ReasonCodeID")
    serial_numbers: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="SerialNumbers"
    )
    source: Optional[int] = Field(default=None, alias="Source")
    status: Optional[int] = Field(default=None, alias="Status")
    stock_count_id: UUID = Field(alias="StockCountID")
    stock_keeping_unit: Optional[str] = Field(default=None, alias="StockKeepingUnit")
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
