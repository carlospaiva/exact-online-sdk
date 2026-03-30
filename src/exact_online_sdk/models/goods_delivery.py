from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .goods_delivery_line import GoodsDeliveryLine


class GoodsDelivery(StrictModel):
    entry_id: Optional[UUID] = Field(default=None, alias="EntryID")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    delivery_account: Optional[UUID] = Field(default=None, alias="DeliveryAccount")
    delivery_account_code: Optional[str] = Field(
        default=None, alias="DeliveryAccountCode"
    )
    delivery_account_name: Optional[str] = Field(
        default=None, alias="DeliveryAccountName"
    )
    delivery_address: Optional[UUID] = Field(default=None, alias="DeliveryAddress")
    delivery_contact: Optional[UUID] = Field(default=None, alias="DeliveryContact")
    delivery_contact_person_full_name: Optional[str] = Field(
        default=None, alias="DeliveryContactPersonFullName"
    )
    delivery_date: datetime = Field(alias="DeliveryDate")
    delivery_number: Optional[int] = Field(default=None, alias="DeliveryNumber")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    document: Optional[UUID] = Field(default=None, alias="Document")
    document_subject: Optional[str] = Field(default=None, alias="DocumentSubject")
    entry_number: Optional[int] = Field(default=None, alias="EntryNumber")
    goods_delivery_lines: list[GoodsDeliveryLine] = Field(
        default_factory=list, alias="GoodsDeliveryLines"
    )
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    shipping_method: Optional[UUID] = Field(default=None, alias="ShippingMethod")
    shipping_method_code: Optional[str] = Field(
        default=None, alias="ShippingMethodCode"
    )
    shipping_method_description: Optional[str] = Field(
        default=None, alias="ShippingMethodDescription"
    )
    tracking_number: Optional[str] = Field(default=None, alias="TrackingNumber")
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
