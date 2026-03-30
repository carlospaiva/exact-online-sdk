from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class BatchNumber(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    available_quantity: Optional[float] = Field(default=None, alias="AvailableQuantity")
    batch_number: Optional[str] = Field(default=None, alias="BatchNumber")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    division: Optional[int] = Field(default=None, alias="Division")
    expiry_date: Optional[datetime] = Field(default=None, alias="ExpiryDate")
    is_blocked: Optional[int] = Field(default=None, alias="IsBlocked")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    storage_locations: Optional[Any] = Field(default=None, alias="StorageLocations")
    warehouses: Optional[Any] = Field(default=None, alias="Warehouses")
