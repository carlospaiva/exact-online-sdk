from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .assembly_bill_of_material_material import AssemblyBillOfMaterialMaterial
from .base import StrictModel


class AssemblyBillOfMaterialHeader(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    assembled_lead_days: Optional[int] = Field(default=None, alias="AssembledLeadDays")
    assembly_bill_of_material_materials: list[AssemblyBillOfMaterialMaterial] = Field(
        default_factory=list, alias="AssemblyBillOfMaterialMaterials"
    )
    batch_quantity: Optional[float] = Field(default=None, alias="BatchQuantity")
    code: Optional[str] = Field(default=None, alias="Code")
    cost_price: Optional[float] = Field(default=None, alias="CostPrice")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    notes: Optional[str] = Field(default=None, alias="Notes")
    update_cost_price: Optional[bool] = Field(default=None, alias="UpdateCostPrice")
    use_explosion: Optional[int] = Field(default=None, alias="UseExplosion")
