from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class InventoryStockSerialBatchNumber(StrictModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    draft_stock_transaction_location: Optional[UUID] = Field(
        default=None,
        alias="DraftStockTransactionLocation",
    )
    draft_transaction_id: Optional[UUID] = Field(
        default=None, alias="DraftTransactionID"
    )
    id: Optional[UUID] = Field(default=None, alias="ID")
    is_draft: Optional[int] = Field(default=None, alias="IsDraft")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    parent_id: Optional[UUID] = Field(default=None, alias="ParentID")
    picklist_line: Optional[UUID] = Field(default=None, alias="PicklistLine")
    pick_order_line: Optional[UUID] = Field(default=None, alias="PickOrderLine")
    purchase_transaction: Optional[UUID] = Field(
        default=None,
        alias="PurchaseTransaction",
    )
    quantity: Optional[float] = Field(default=None, alias="Quantity")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    sales_order_line: Optional[UUID] = Field(default=None, alias="SalesOrderLine")
    sales_return_line: Optional[UUID] = Field(default=None, alias="SalesReturnLine")
    sales_transaction: Optional[UUID] = Field(default=None, alias="SalesTransaction")
    serial_batch_number: Optional[UUID] = Field(default=None, alias="SerialBatchNumber")
    stock_count_line: Optional[UUID] = Field(default=None, alias="StockCountLine")
    stock_transaction_id: Optional[UUID] = Field(
        default=None, alias="StockTransactionID"
    )
    stock_transaction_location: Optional[UUID] = Field(
        default=None,
        alias="StockTransactionLocation",
    )
    stock_transaction_type: int = Field(alias="StockTransactionType")
    storage_location: Optional[UUID] = Field(default=None, alias="StorageLocation")
    storage_location_code: Optional[str] = Field(
        default=None,
        alias="StorageLocationCode",
    )
    storage_location_description: Optional[str] = Field(
        default=None,
        alias="StorageLocationDescription",
    )
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None,
        alias="WarehouseDescription",
    )
