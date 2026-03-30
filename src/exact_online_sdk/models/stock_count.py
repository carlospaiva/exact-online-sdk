from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .stock_count_line import StockCountLine


class StockCount(StrictModel):
    stock_count_id: Optional[UUID] = Field(default=None, alias="StockCountID")
    counted_by: Optional[UUID] = Field(default=None, alias="CountedBy")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    entry_number: Optional[int] = Field(default=None, alias="EntryNumber")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    offset_gl_inventory: Optional[UUID] = Field(default=None, alias="OffsetGLInventory")
    offset_gl_inventory_code: Optional[str] = Field(
        default=None, alias="OffsetGLInventoryCode"
    )
    offset_gl_inventory_description: Optional[str] = Field(
        default=None, alias="OffsetGLInventoryDescription"
    )
    source: Optional[int] = Field(default=None, alias="Source")
    status: Optional[int] = Field(default=None, alias="Status")
    stock_count_date: datetime = Field(alias="StockCountDate")
    stock_count_lines: list[StockCountLine] = Field(
        default_factory=list, alias="StockCountLines"
    )
    stock_count_number: Optional[int] = Field(default=None, alias="StockCountNumber")
    warehouse: UUID = Field(alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
