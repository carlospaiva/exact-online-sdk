from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .planned_sales_return_line import PlannedSalesReturnLine


class PlannedSalesReturn(StrictModel):
    planned_sales_return_id: Optional[UUID] = Field(
        default=None, alias="PlannedSalesReturnID"
    )
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    delivered_to: UUID = Field(alias="DeliveredTo")
    delivered_to_contact_person: Optional[UUID] = Field(
        default=None, alias="DeliveredToContactPerson"
    )
    delivered_to_contact_person_full_name: Optional[str] = Field(
        default=None, alias="DeliveredToContactPersonFullName"
    )
    delivered_to_name: Optional[str] = Field(default=None, alias="DeliveredToName")
    delivery_address: Optional[UUID] = Field(default=None, alias="DeliveryAddress")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    document: Optional[UUID] = Field(default=None, alias="Document")
    document_subject: Optional[str] = Field(default=None, alias="DocumentSubject")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    planned_sales_return_lines: list[PlannedSalesReturnLine] = Field(
        default_factory=list, alias="PlannedSalesReturnLines"
    )
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    return_date: Optional[datetime] = Field(default=None, alias="ReturnDate")
    return_number: Optional[int] = Field(default=None, alias="ReturnNumber")
    source: Optional[int] = Field(default=None, alias="Source")
    status: Optional[int] = Field(default=None, alias="Status")
    warehouse: UUID = Field(alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
