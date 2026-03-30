from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class PlannedShopOrder(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_version: Optional[UUID] = Field(None, alias="ItemVersion")
    planned_date: Optional[datetime] = Field(None, alias="PlannedDate")
    planned_quantity: Optional[float] = Field(None, alias="PlannedQuantity")
    planned_start_date: Optional[datetime] = Field(None, alias="PlannedStartDate")
    production_area: Optional[UUID] = Field(None, alias="ProductionArea")
    project: Optional[UUID] = Field(None, alias="Project")
    sales_order_line: Optional[UUID] = Field(None, alias="SalesOrderLine")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    status: Optional[int] = Field(None, alias="Status")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
