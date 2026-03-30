from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AssemblyBillOfMaterialMaterial(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    assembled_item: UUID = Field(alias="AssembledItem")
    assembled_item_code: Optional[str] = Field(default=None, alias="AssembledItemCode")
    assembled_item_description: Optional[str] = Field(
        default=None, alias="AssembledItemDescription"
    )
    assembled_lead_days: Optional[int] = Field(default=None, alias="AssembledLeadDays")
    batch_quantity: Optional[float] = Field(default=None, alias="BatchQuantity")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    division: Optional[int] = Field(default=None, alias="Division")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    part_item: UUID = Field(alias="PartItem")
    part_item_code: Optional[str] = Field(default=None, alias="PartItemCode")
    part_item_description: Optional[str] = Field(
        default=None, alias="PartItemDescription"
    )
    quantity: Optional[float] = Field(default=None, alias="Quantity")
    quantity_batch: Optional[float] = Field(default=None, alias="QuantityBatch")
    update_cost_price: Optional[bool] = Field(default=None, alias="UpdateCostPrice")
    use_explosion: Optional[int] = Field(default=None, alias="UseExplosion")
