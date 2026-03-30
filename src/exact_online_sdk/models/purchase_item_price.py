from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class PurchaseItemPrice(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_name: Optional[str] = Field(None, alias="AccountName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    default_item_unit: Optional[str] = Field(None, alias="DefaultItemUnit")
    default_item_unit_description: Optional[str] = Field(
        None, alias="DefaultItemUnitDescription"
    )
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    minimum_quantity: Optional[float] = Field(None, alias="MinimumQuantity")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    number_of_items_per_unit: Optional[float] = Field(
        None, alias="NumberOfItemsPerUnit"
    )
    price: Optional[float] = Field(None, alias="Price")
    quantity: Optional[float] = Field(None, alias="Quantity")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
