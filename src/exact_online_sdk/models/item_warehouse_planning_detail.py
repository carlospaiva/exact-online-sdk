from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemWarehousePlanningDetail(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    planned_date: Optional[datetime] = Field(default=None, alias="PlannedDate")
    planned_quantity: Optional[float] = Field(default=None, alias="PlannedQuantity")
    planning_source_description: Optional[str] = Field(
        default=None, alias="PlanningSourceDescription"
    )
    planning_source_id: Optional[UUID] = Field(default=None, alias="PlanningSourceID")
    planning_source_line_number: Optional[int] = Field(
        default=None, alias="PlanningSourceLineNumber"
    )
    planning_source_number: Optional[int] = Field(
        default=None, alias="PlanningSourceNumber"
    )
    planning_source_url: Optional[str] = Field(default=None, alias="PlanningSourceUrl")
    planning_type: Optional[int] = Field(default=None, alias="PlanningType")
    planning_type_description: Optional[str] = Field(
        default=None, alias="PlanningTypeDescription"
    )
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
