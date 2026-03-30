from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class InventorySerialBatchNumber(StrictModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    id: Optional[UUID] = Field(default=None, alias="ID")
    is_blocked: Optional[int] = Field(default=None, alias="IsBlocked")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    serial_batch_number: Optional[str] = Field(default=None, alias="SerialBatchNumber")
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    type: Optional[int] = Field(default=None, alias="Type")
