from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DropShipmentLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    batch_numbers: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="BatchNumbers"
    )
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    customer_item_code: Optional[str] = Field(default=None, alias="CustomerItemCode")
    delivery_date: Optional[datetime] = Field(default=None, alias="DeliveryDate")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    entry_id: Optional[UUID] = Field(default=None, alias="EntryID")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    notes: Optional[str] = Field(default=None, alias="Notes")
    purchase_order_line_id: UUID = Field(alias="PurchaseOrderLineID")
    quantity_delivered: float = Field(alias="QuantityDelivered")
    quantity_ordered: Optional[float] = Field(default=None, alias="QuantityOrdered")
    sales_order_line_id: UUID = Field(alias="SalesOrderLineID")
    sales_order_line_number: Optional[int] = Field(
        default=None, alias="SalesOrderLineNumber"
    )
    sales_order_number: Optional[int] = Field(default=None, alias="SalesOrderNumber")
    serial_numbers: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="SerialNumbers"
    )
    tracking_number: Optional[str] = Field(default=None, alias="TrackingNumber")
    unit_code: Optional[str] = Field(default=None, alias="Unitcode")
