from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class BillOfMaterialMaterial(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    average_cost: Optional[float] = Field(None, alias="AverageCost")
    backflush: Optional[int] = Field(None, alias="Backflush")
    calculator_type: Optional[int] = Field(None, alias="CalculatorType")
    cost_batch: Optional[float] = Field(None, alias="CostBatch")
    cost_center: Optional[str] = Field(None, alias="CostCenter")
    cost_center_description: Optional[str] = Field(None, alias="CostCenterDescription")
    cost_unit: Optional[str] = Field(None, alias="CostUnit")
    cost_unit_description: Optional[str] = Field(None, alias="CostUnitDescription")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    detail_drawing: Optional[str] = Field(None, alias="DetailDrawing")
    division: Optional[int] = Field(None, alias="Division")
    item_version: Optional[UUID] = Field(None, alias="ItemVersion")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    net_weight: Optional[float] = Field(None, alias="NetWeight")
    net_weight_unit: Optional[str] = Field(None, alias="NetWeightUnit")
    notes: Optional[str] = Field(None, alias="Notes")
    part_item: Optional[UUID] = Field(None, alias="PartItem")
    part_item_average_cost: Optional[float] = Field(None, alias="PartItemAverageCost")
    part_item_code: Optional[str] = Field(None, alias="PartItemCode")
    part_item_cost_price_standard: Optional[float] = Field(
        None, alias="PartItemCostPriceStandard"
    )
    part_item_description: Optional[str] = Field(None, alias="PartItemDescription")
    quantity: Optional[float] = Field(None, alias="Quantity")
    quantity_batch: Optional[float] = Field(None, alias="QuantityBatch")
    routing_step_id: Optional[UUID] = Field(None, alias="RoutingStepID")
    syscreated: Optional[datetime] = Field(None, alias="syscreated")
    syscreator: Optional[UUID] = Field(None, alias="syscreator")
    sysmodified: Optional[datetime] = Field(None, alias="sysmodified")
    sysmodifier: Optional[UUID] = Field(None, alias="sysmodifier")
    type: Optional[int] = Field(None, alias="Type")
    waste_percentage: Optional[float] = Field(None, alias="WastePercentage")
