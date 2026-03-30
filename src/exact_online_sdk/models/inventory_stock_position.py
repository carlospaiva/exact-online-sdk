from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class InventoryStockPosition(StrictModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    current_stock: Optional[float] = Field(default=None, alias="CurrentStock")
    division: Optional[int] = Field(default=None, alias="Division")
    free_stock: Optional[float] = Field(default=None, alias="FreeStock")
    id: Optional[UUID] = Field(default=None, alias="ID")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_id: Optional[UUID] = Field(default=None, alias="ItemId")
    planning_in: Optional[float] = Field(default=None, alias="PlanningIn")
    planning_out: Optional[float] = Field(default=None, alias="PlanningOut")
    projected_stock: Optional[float] = Field(default=None, alias="ProjectedStock")
    reorder_point: Optional[float] = Field(default=None, alias="ReorderPoint")
    reserved_stock: Optional[float] = Field(default=None, alias="ReservedStock")
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None,
        alias="WarehouseDescription",
    )
