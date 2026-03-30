from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ByProduct(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    by_product_cost_price: Optional[float] = Field(None, alias="ByProductCostPrice")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    is_reversable: Optional[bool] = Field(None, alias="IsReversable")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_unit: Optional[str] = Field(None, alias="ItemUnit")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    quantity: Optional[float] = Field(None, alias="Quantity")
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(None, alias="WarehouseDescription")
