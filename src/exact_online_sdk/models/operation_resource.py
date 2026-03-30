from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class OperationResource(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    attendance_percentage: Optional[float] = Field(None, alias="AttendancePercentage")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    division: Optional[int] = Field(None, alias="Division")
    effective_work_percentage: Optional[float] = Field(
        None, alias="EffectiveWorkPercentage"
    )
    is_primary: Optional[int] = Field(None, alias="IsPrimary")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    operation: Optional[UUID] = Field(None, alias="Operation")
    operation_description: Optional[str] = Field(None, alias="OperationDescription")
    purchase_lead_days: Optional[int] = Field(None, alias="PurchaseLeadDays")
    purchase_unit: Optional[str] = Field(None, alias="PurchaseUnit")
    purchase_vat_code: Optional[str] = Field(None, alias="PurchaseVATCode")
    rate: Optional[float] = Field(None, alias="Rate")
    resource_type: Optional[int] = Field(None, alias="ResourceType")
    run: Optional[float] = Field(None, alias="Run")
    run_method: Optional[int] = Field(None, alias="RunMethod")
    setup: Optional[float] = Field(None, alias="Setup")
    setup_unit: Optional[str] = Field(None, alias="SetupUnit")
    workcenter: Optional[UUID] = Field(None, alias="Workcenter")
    workcenter_description: Optional[str] = Field(None, alias="WorkcenterDescription")
