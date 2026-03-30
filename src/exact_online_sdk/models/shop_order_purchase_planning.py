from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ShopOrderPurchasePlanning(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    id: Optional[UUID] = Field(None, alias="ID")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
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
    purchase_order: Optional[UUID] = Field(None, alias="PurchaseOrder")
    purchase_order_line: Optional[UUID] = Field(None, alias="PurchaseOrderLine")
    routing_step_plan: Optional[UUID] = Field(None, alias="RoutingStepPlan")
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
