from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SalesItemPrice(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    account: Optional[UUID] = Field(default=None, alias="Account")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    barcode: Optional[str] = Field(default=None, alias="Barcode")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    default_item_unit: Optional[str] = Field(default=None, alias="DefaultItemUnit")
    default_item_unit_description: Optional[str] = Field(
        default=None, alias="DefaultItemUnitDescription"
    )
    division: Optional[int] = Field(default=None, alias="Division")
    employee: Optional[UUID] = Field(default=None, alias="Employee")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    number_of_items_per_unit: Optional[float] = Field(
        default=None, alias="NumberOfItemsPerUnit"
    )
    price: Optional[float] = Field(default=None, alias="Price")
    project: Optional[UUID] = Field(default=None, alias="Project")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    quantity: Optional[float] = Field(default=None, alias="Quantity")
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    unit: Optional[str] = Field(default=None, alias="Unit")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
