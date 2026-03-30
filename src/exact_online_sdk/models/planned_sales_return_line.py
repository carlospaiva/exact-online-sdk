from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class PlannedSalesReturnLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    batch_numbers: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="BatchNumbers"
    )
    create_credit: int = Field(alias="CreateCredit")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    good_delivery_line_id: UUID = Field(alias="GoodDeliveryLineID")
    item: UUID = Field(alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    notes: Optional[str] = Field(default=None, alias="Notes")
    planned_return_quantity: float = Field(alias="PlannedReturnQuantity")
    planned_sales_return_id: Optional[UUID] = Field(
        default=None, alias="PlannedSalesReturnID"
    )
    received_quantity: float = Field(alias="ReceivedQuantity")
    return_reason_code_code: Optional[str] = Field(
        default=None, alias="ReturnReasonCodeCode"
    )
    return_reason_code_description: Optional[str] = Field(
        default=None, alias="ReturnReasonCodeDescription"
    )
    return_reason_code_id: Optional[UUID] = Field(
        default=None, alias="ReturnReasonCodeID"
    )
    sales_order_line_id: Optional[UUID] = Field(default=None, alias="SalesOrderLineID")
    sales_order_number: Optional[int] = Field(default=None, alias="SalesOrderNumber")
    serial_numbers: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="SerialNumbers"
    )
    stock_transaction_entry_id: Optional[UUID] = Field(
        default=None, alias="StockTransactionEntryID"
    )
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
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
