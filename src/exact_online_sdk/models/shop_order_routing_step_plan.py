from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ShopOrderRoutingStepPlan(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_name: Optional[str] = Field(None, alias="AccountName")
    account_number: Optional[int] = Field(None, alias="AccountNumber")
    attendance_percentage: Optional[float] = Field(None, alias="AttendancePercentage")
    backflush_labor: Optional[int] = Field(None, alias="BackflushLabor")
    cost_per_item: Optional[float] = Field(None, alias="CostPerItem")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    effective_work_percentage: Optional[float] = Field(
        None, alias="EffectiveWorkPercentage"
    )
    line_number: Optional[int] = Field(None, alias="LineNumber")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    operation: Optional[UUID] = Field(None, alias="Operation")
    operation_code: Optional[str] = Field(None, alias="OperationCode")
    operation_description: Optional[str] = Field(None, alias="OperationDescription")
    operation_resource: Optional[UUID] = Field(None, alias="OperationResource")
    planned_run_hours: Optional[float] = Field(None, alias="PlannedRunHours")
    planned_setup_hours: Optional[float] = Field(None, alias="PlannedSetupHours")
    planned_start_date: Optional[datetime] = Field(None, alias="PlannedStartDate")
    planned_total_hours: Optional[float] = Field(None, alias="PlannedTotalHours")
    purchase_unit: Optional[str] = Field(None, alias="PurchaseUnit")
    purchase_unit_factor: Optional[float] = Field(None, alias="PurchaseUnitFactor")
    purchase_unit_price_fc: Optional[float] = Field(None, alias="PurchaseUnitPriceFC")
    purchase_unit_quantity: Optional[float] = Field(None, alias="PurchaseUnitQuantity")
    routing_step_type: Optional[int] = Field(None, alias="RoutingStepType")
    run: Optional[float] = Field(None, alias="Run")
    run_method: Optional[int] = Field(None, alias="RunMethod")
    setup: Optional[float] = Field(None, alias="Setup")
    setup_unit: Optional[str] = Field(None, alias="SetupUnit")
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    sub_order_count: Optional[int] = Field(None, alias="SubOrderCount")
    total_cost_dc: Optional[float] = Field(None, alias="TotalCostDC")
    workcenter: Optional[UUID] = Field(None, alias="Workcenter")
    workcenter_code: Optional[str] = Field(None, alias="WorkcenterCode")
    workcenter_description: Optional[str] = Field(None, alias="WorkcenterDescription")
