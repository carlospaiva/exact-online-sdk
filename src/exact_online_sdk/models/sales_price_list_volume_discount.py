from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SalesPriceListVolumeDiscount(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    id: Optional[UUID] = Field(None, alias="ID")
    base_price_amount: Optional[float] = Field(None, alias="BasePriceAmount")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    discount: Optional[float] = Field(None, alias="Discount")
    division: Optional[int] = Field(None, alias="Division")
    entry_method: Optional[int] = Field(None, alias="EntryMethod")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_group: Optional[UUID] = Field(None, alias="ItemGroup")
    item_group_code: Optional[str] = Field(None, alias="ItemGroupCode")
    item_group_description: Optional[str] = Field(None, alias="ItemGroupDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    new_price: Optional[float] = Field(None, alias="NewPrice")
    number_of_items_per_unit: Optional[float] = Field(
        None, alias="NumberOfItemsPerUnit"
    )
    price_list_code: Optional[str] = Field(None, alias="PriceListCode")
    price_list_id: Optional[UUID] = Field(None, alias="PriceListId")
    price_list_period: Optional[UUID] = Field(None, alias="PriceListPeriod")
    quantity: Optional[float] = Field(None, alias="Quantity")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
