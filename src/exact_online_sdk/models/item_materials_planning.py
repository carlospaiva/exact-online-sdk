from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemMaterialsPlanning(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    planned_date: Optional[datetime] = Field(None, alias="PlannedDate")
    planned_quantity: Optional[float] = Field(None, alias="PlannedQuantity")
    planned_start_date: Optional[datetime] = Field(None, alias="PlannedStartDate")
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    shop_order_status: Optional[int] = Field(None, alias="ShopOrderStatus")
    source_type: Optional[int] = Field(None, alias="SourceType")
    type: Optional[int] = Field(None, alias="Type")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(None, alias="WarehouseDescription")
