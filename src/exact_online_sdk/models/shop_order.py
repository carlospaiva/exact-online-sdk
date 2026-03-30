from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ShopOrder(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    cad_drawing_url: Optional[str] = Field(None, alias="CADDrawingURL")
    costcenter: Optional[str] = Field(None, alias="Costcenter")
    costcenter_description: Optional[str] = Field(None, alias="CostcenterDescription")
    costunit: Optional[str] = Field(None, alias="Costunit")
    costunit_description: Optional[str] = Field(None, alias="CostunitDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    entry_date: Optional[datetime] = Field(None, alias="EntryDate")
    is_completed: Optional[int] = Field(None, alias="IsCompleted")
    is_released: Optional[int] = Field(None, alias="IsReleased")
    is_sub_order_of: Optional[UUID] = Field(None, alias="ISubOrderOf")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_picture_url: Optional[str] = Field(None, alias="ItemPictureUrl")
    item_version: Optional[UUID] = Field(None, alias="ItemVersion")
    item_version_description: Optional[str] = Field(
        None, alias="ItemVersionDescription"
    )
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    planned_date: Optional[datetime] = Field(None, alias="PlannedDate")
    planned_quantity: Optional[float] = Field(None, alias="PlannedQuantity")
    planned_start_date: Optional[datetime] = Field(None, alias="PlannedStartDate")
    produced_quantity: Optional[float] = Field(None, alias="ProducedQuantity")
    production_area: Optional[UUID] = Field(None, alias="ProductionArea")
    project: Optional[UUID] = Field(None, alias="Project")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    purchase_order: Optional[UUID] = Field(None, alias="PurchaseOrder")
    quantity_on_sub_order: Optional[float] = Field(None, alias="QuantityOnSubOrder")
    sales_order_line: Optional[UUID] = Field(None, alias="SalesOrderLine")
    sales_order_line_number: Optional[int] = Field(None, alias="SalesOrderLineNumber")
    sales_order_number: Optional[int] = Field(None, alias="SalesOrderNumber")
    shop_order_main: Optional[UUID] = Field(None, alias="ShopOrderMain")
    shop_order_main_number: Optional[int] = Field(None, alias="ShopOrderMainNumber")
    shop_order_number: Optional[int] = Field(None, alias="ShopOrderNumber")
    shop_order_number_string: Optional[str] = Field(None, alias="ShopOrderNumberString")
    shop_order_parent: Optional[UUID] = Field(None, alias="ShopOrderParent")
    shop_order_parent_number: Optional[int] = Field(None, alias="ShopOrderParentNumber")
    shop_order_routing_step_plans: Optional[list] = Field(  # type: ignore[type-arg]
        None, alias="ShopOrderRoutingStepPlans"
    )
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    sub_shop_order_count: Optional[int] = Field(None, alias="SubShopOrderCount")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    unit: Optional[str] = Field(None, alias="Unit")
    unit_description: Optional[str] = Field(None, alias="UnitDescription")
    warehouse: Optional[UUID] = Field(None, alias="Warehouse")
    your_ref: Optional[str] = Field(None, alias="YourRef")
