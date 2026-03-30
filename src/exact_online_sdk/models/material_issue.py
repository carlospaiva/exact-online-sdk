from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class MaterialIssue(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    created_by: Optional[UUID] = Field(None, alias="CreatedBy")
    created_by_full_name: Optional[str] = Field(None, alias="CreatedByFullName")
    created_date: Optional[datetime] = Field(None, alias="CreatedDate")
    draft_stock_transaction_id: Optional[UUID] = Field(
        None, alias="DraftStockTransactionID"
    )
    has_reversible_quantity: Optional[bool] = Field(None, alias="HasReversibleQuantity")
    is_backflush: Optional[int] = Field(None, alias="IsBackflush")
    is_batch: Optional[int] = Field(None, alias="IsBatch")
    is_fraction_allowed_item: Optional[int] = Field(None, alias="IsFractionAllowedItem")
    is_serial: Optional[int] = Field(None, alias="IsSerial")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_picture_url: Optional[str] = Field(None, alias="ItemPictureUrl")
    note: Optional[str] = Field(None, alias="Note")
    quantity: Optional[float] = Field(None, alias="Quantity")
    relative_cost_per_quantity: Optional[float] = Field(
        None, alias="RelativeCostPerQuantity"
    )
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    shop_order_material_plan: Optional[UUID] = Field(
        None, alias="ShopOrderMaterialPlan"
    )
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    stock_transaction_id: Optional[UUID] = Field(None, alias="StockTransactionId")
    storage_location: Optional[UUID] = Field(None, alias="StorageLocation")
    storage_location_code: Optional[str] = Field(None, alias="StorageLocationCode")
    storage_location_description: Optional[str] = Field(
        None, alias="StorageLocationDescription"
    )
    transaction_date: Optional[datetime] = Field(None, alias="TransactionDate")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(None, alias="WarehouseDescription")
