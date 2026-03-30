from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .warehouse_transfer_line import WarehouseTransferLine


class WarehouseTransfer(StrictModel):
    transfer_id: Optional[UUID] = Field(default=None, alias="TransferID")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    entry_date: datetime = Field(alias="EntryDate")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    picked_by: Optional[UUID] = Field(default=None, alias="PickedBy")
    planned_delivery_date: Optional[datetime] = Field(
        default=None, alias="PlannedDeliveryDate"
    )
    planned_receipt_date: Optional[datetime] = Field(
        default=None, alias="PlannedReceiptDate"
    )
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    source: Optional[int] = Field(default=None, alias="Source")
    status: Optional[int] = Field(default=None, alias="Status")
    transfer_date: Optional[datetime] = Field(default=None, alias="TransferDate")
    transfer_number: Optional[int] = Field(default=None, alias="TransferNumber")
    transferred_by: Optional[UUID] = Field(default=None, alias="TransferredBy")
    warehouse_from: UUID = Field(alias="WarehouseFrom")
    warehouse_from_code: Optional[str] = Field(default=None, alias="WarehouseFromCode")
    warehouse_from_description: Optional[str] = Field(
        default=None, alias="WarehouseFromDescription"
    )
    warehouse_to: UUID = Field(alias="WarehouseTo")
    warehouse_to_code: Optional[str] = Field(default=None, alias="WarehouseToCode")
    warehouse_to_description: Optional[str] = Field(
        default=None, alias="WarehouseToDescription"
    )
    warehouse_transfer_lines: list[WarehouseTransferLine] = Field(
        default_factory=list, alias="WarehouseTransferLines"
    )
