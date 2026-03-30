from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ShopOrderMaterialPlan(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    backflush: Optional[int] = Field(None, alias="Backflush")
    calculator_type: Optional[int] = Field(None, alias="CalculatorType")
    cost_batch: Optional[float] = Field(None, alias="CostBatch")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    detail_drawing: Optional[str] = Field(None, alias="DetailDrawing")
    division: Optional[int] = Field(None, alias="Division")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_picture_url: Optional[str] = Field(None, alias="ItemPictureUrl")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    planned_amount_fc: Optional[float] = Field(None, alias="PlannedAmountFC")
    planned_date: Optional[datetime] = Field(None, alias="PlannedDate")
    planned_price_fc: Optional[float] = Field(None, alias="PlannedPriceFC")
    planned_quantity: Optional[float] = Field(None, alias="PlannedQuantity")
    planned_quantity_factor: Optional[float] = Field(
        None, alias="PlannedQuantityFactor"
    )
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    type: Optional[int] = Field(None, alias="Type")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(None, alias="WarehouseDescription")
