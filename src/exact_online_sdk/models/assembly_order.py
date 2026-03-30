from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AssemblyOrder(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    assembly_date: Optional[datetime] = Field(default=None, alias="AssemblyDate")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    finished_assembly_date: Optional[datetime] = Field(
        default=None, alias="FinishedAssemblyDate"
    )
    finished_quantity: Optional[float] = Field(default=None, alias="FinishedQuantity")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    notes: Optional[str] = Field(default=None, alias="Notes")
    order_date: Optional[datetime] = Field(default=None, alias="OrderDate")
    order_number: Optional[int] = Field(default=None, alias="OrderNumber")
    order_status: Optional[int] = Field(default=None, alias="OrderStatus")
    part_items: Optional[Any] = Field(default=None, alias="PartItems")
    planned_quantity: Optional[float] = Field(default=None, alias="PlannedQuantity")
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
    type: Optional[int] = Field(default=None, alias="Type")
    unit: Optional[UUID] = Field(default=None, alias="Unit")
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
