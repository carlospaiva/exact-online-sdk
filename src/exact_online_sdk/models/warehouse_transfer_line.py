from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class WarehouseTransferLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    batch_numbers: Optional[Any] = Field(default=None, alias="BatchNumbers")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    item: UUID = Field(alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    picked_by: Optional[UUID] = Field(default=None, alias="PickedBy")
    quantity: float = Field(alias="Quantity")
    serial_numbers: Optional[Any] = Field(default=None, alias="SerialNumbers")
    storage_location_from: Optional[UUID] = Field(
        default=None, alias="StorageLocationFrom"
    )
    storage_location_from_code: Optional[str] = Field(
        default=None, alias="StorageLocationFromCode"
    )
    storage_location_from_description: Optional[str] = Field(
        default=None, alias="StorageLocationFromDescription"
    )
    storage_location_from_location_sequence: Optional[int] = Field(
        default=None, alias="StorageLocationFromLocationSequence"
    )
    storage_location_to: Optional[UUID] = Field(default=None, alias="StorageLocationTo")
    storage_location_to_code: Optional[str] = Field(
        default=None, alias="StorageLocationToCode"
    )
    storage_location_to_description: Optional[str] = Field(
        default=None, alias="StorageLocationToDescription"
    )
    storage_location_to_location_sequence: Optional[int] = Field(
        default=None, alias="StorageLocationToLocationSequence"
    )
    transfer_id: UUID = Field(alias="TransferID")
    transferred_by: Optional[UUID] = Field(default=None, alias="TransferredBy")
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
