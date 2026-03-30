from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ProjectWBS(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    additional_invoicing: Optional[int] = Field(None, alias="AdditionalInvoicing")
    baseline_date: Optional[datetime] = Field(None, alias="BaselineDate")
    block_entry: Optional[bool] = Field(None, alias="BlockEntry")
    block_rebilling: Optional[bool] = Field(None, alias="BlockRebilling")
    budget_overrun_hours: Optional[int] = Field(None, alias="BudgetOverrunHours")
    completed: Optional[int] = Field(None, alias="Completed")
    cost: Optional[float] = Field(None, alias="Cost")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    default_item: Optional[UUID] = Field(None, alias="DefaultItem")
    default_item_is_mandatory: Optional[int] = Field(
        None, alias="DefaultItemIsMandatory"
    )
    description: str = Field(..., alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    hours: Optional[float] = Field(None, alias="Hours")
    invoice_method: Optional[int] = Field(None, alias="InvoiceMethod")
    is_baseline: Optional[int] = Field(None, alias="IsBaseline")
    milestone: Optional[int] = Field(None, alias="Milestone")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    notes: Optional[str] = Field(None, alias="Notes")
    parent: Optional[UUID] = Field(None, alias="Parent")
    project: Optional[UUID] = Field(None, alias="Project")
    project_term: Optional[UUID] = Field(None, alias="ProjectTerm")
    purchase_markup_percentage: Optional[float] = Field(
        None, alias="PurchaseMarkupPercentage"
    )
    purchase_price: Optional[float] = Field(None, alias="PurchasePrice")
    quantity: Optional[float] = Field(None, alias="Quantity")
    revenue: Optional[float] = Field(None, alias="Revenue")
    sequence_number: Optional[int] = Field(None, alias="SequenceNumber")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    supplier: Optional[UUID] = Field(None, alias="Supplier")
    time_quantity_to_alert: Optional[float] = Field(None, alias="TimeQuantityToAlert")
    type: Optional[int] = Field(None, alias="Type")
