from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class StockBatchNumber(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    batch_number: str = Field(alias="BatchNumber")
    batch_number_id: Optional[UUID] = Field(default=None, alias="BatchNumberID")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    draft_stock_transaction_id: UUID = Field(alias="DraftStockTransactionID")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    is_blocked: Optional[int] = Field(default=None, alias="IsBlocked")
    is_draft: Optional[int] = Field(default=None, alias="IsDraft")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    parent_id: Optional[UUID] = Field(default=None, alias="ParentID")
    pick_order_line: Optional[UUID] = Field(default=None, alias="PickOrderLine")
    quantity: float = Field(alias="Quantity")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    sales_order_line: Optional[UUID] = Field(default=None, alias="SalesOrderLine")
    sales_return_line: Optional[UUID] = Field(default=None, alias="SalesReturnLine")
    stock_count_line: Optional[UUID] = Field(default=None, alias="StockCountLine")
    stock_transaction_id: Optional[UUID] = Field(
        default=None, alias="StockTransactionID"
    )
    stock_transaction_type: int = Field(alias="StockTransactionType")
    storage_location: Optional[UUID] = Field(default=None, alias="StorageLocation")
    storage_location_code: Optional[str] = Field(
        default=None, alias="StorageLocationCode"
    )
    storage_location_description: Optional[str] = Field(
        default=None, alias="StorageLocationDescription"
    )
    warehouse: UUID = Field(alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
    warehouse_transfer_line: Optional[UUID] = Field(
        default=None, alias="WarehouseTransferLine"
    )
