from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemWarehouse(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    counting_cycle: Optional[int] = Field(default=None, alias="CountingCycle")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    current_stock: Optional[float] = Field(default=None, alias="CurrentStock")
    default_storage_location: Optional[UUID] = Field(
        default=None, alias="DefaultStorageLocation"
    )
    default_storage_location_code: Optional[str] = Field(
        default=None, alias="DefaultStorageLocationCode"
    )
    default_storage_location_description: Optional[str] = Field(
        default=None, alias="DefaultStorageLocationDescription"
    )
    division: Optional[int] = Field(default=None, alias="Division")
    item: UUID = Field(alias="Item")
    item_barcode: Optional[str] = Field(default=None, alias="ItemBarcode")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_end_date: Optional[datetime] = Field(default=None, alias="ItemEndDate")
    item_is_fraction_allowed_item: Optional[bool] = Field(
        default=None, alias="ItemIsFractionAllowedItem"
    )
    item_is_stock_item: Optional[bool] = Field(default=None, alias="ItemIsStockItem")
    item_start_date: Optional[datetime] = Field(default=None, alias="ItemStartDate")
    item_unit: Optional[str] = Field(default=None, alias="ItemUnit")
    item_unit_description: Optional[str] = Field(
        default=None, alias="ItemUnitDescription"
    )
    maximum_stock: Optional[float] = Field(default=None, alias="MaximumStock")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    next_counting_cycle: Optional[datetime] = Field(
        default=None, alias="NextCountingCycle"
    )
    order_policy: Optional[int] = Field(default=None, alias="OrderPolicy")
    period: Optional[int] = Field(default=None, alias="Period")
    planned_stock_in: Optional[float] = Field(default=None, alias="PlannedStockIn")
    planned_stock_out: Optional[float] = Field(default=None, alias="PlannedStockOut")
    planning_details_url: Optional[str] = Field(
        default=None, alias="PlanningDetailsUrl"
    )
    projected_stock: Optional[float] = Field(default=None, alias="ProjectedStock")
    reorder_point: Optional[float] = Field(default=None, alias="ReorderPoint")
    reorder_quantity: Optional[float] = Field(default=None, alias="ReorderQuantity")
    replenishment_type: Optional[int] = Field(default=None, alias="ReplenishmentType")
    reserved_stock: Optional[float] = Field(default=None, alias="ReservedStock")
    safety_stock: Optional[float] = Field(default=None, alias="SafetyStock")
    storage_location_sequence_number: Optional[int] = Field(
        default=None, alias="StorageLocationSequenceNumber"
    )
    storage_location_url: Optional[str] = Field(
        default=None, alias="StorageLocationUrl"
    )
    warehouse: UUID = Field(alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
