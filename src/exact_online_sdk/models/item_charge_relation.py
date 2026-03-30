from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemChargeRelation(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    amount: Optional[float] = Field(default=None, alias="Amount")
    charge_code: Optional[str] = Field(default=None, alias="ChargeCode")
    charge_description: Optional[str] = Field(default=None, alias="ChargeDescription")
    charge_id: Optional[UUID] = Field(default=None, alias="ChargeID")
    charge_vat_code: Optional[str] = Field(default=None, alias="ChargeVATCode")
    charge_vat_description: Optional[str] = Field(
        default=None, alias="ChargeVATDescription"
    )
    charge_vat_percentage: Optional[float] = Field(
        default=None, alias="ChargeVATPercentage"
    )
    charge_vat_type: Optional[str] = Field(default=None, alias="ChargeVATType")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    division: Optional[int] = Field(default=None, alias="Division")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_id: Optional[UUID] = Field(default=None, alias="ItemID")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    quantity: Optional[float] = Field(default=None, alias="Quantity")
    total_amount: Optional[float] = Field(default=None, alias="TotalAmount")
