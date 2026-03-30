from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SubscriptionLine(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    amount_dc: Optional[float] = Field(None, alias="AmountDC")
    amount_fc: Optional[float] = Field(None, alias="AmountFC")
    costcenter: Optional[str] = Field(None, alias="Costcenter")
    costcenter_description: Optional[str] = Field(None, alias="CostcenterDescription")
    costunit: Optional[str] = Field(None, alias="Costunit")
    costunit_description: Optional[str] = Field(None, alias="CostunitDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    description: Optional[str] = Field(None, alias="Description")
    discount: Optional[float] = Field(None, alias="Discount")
    division: Optional[int] = Field(None, alias="Division")
    entry_id: Optional[UUID] = Field(None, alias="EntryID")
    from_date: Optional[datetime] = Field(None, alias="FromDate")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    line_type: Optional[int] = Field(None, alias="LineType")
    line_type_description: Optional[str] = Field(None, alias="LineTypeDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    net_price: Optional[float] = Field(None, alias="NetPrice")
    notes: Optional[str] = Field(None, alias="Notes")
    quantity: Optional[float] = Field(None, alias="Quantity")
    to_date: Optional[datetime] = Field(None, alias="ToDate")
    unit_code: Optional[str] = Field(None, alias="UnitCode")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
    unit_price: Optional[float] = Field(None, alias="UnitPrice")
    vat_amount_fc: Optional[float] = Field(None, alias="VATAmountFC")
    vat_code: Optional[str] = Field(None, alias="VATCode")
    vat_code_description: Optional[str] = Field(None, alias="VATCodeDescription")
