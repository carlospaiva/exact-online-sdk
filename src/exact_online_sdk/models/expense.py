from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Expense(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    approver_comment: Optional[str] = Field(None, alias="ApproverComment")
    category: Optional[UUID] = Field(None, alias="Category")
    category_description: Optional[str] = Field(None, alias="CategoryDescription")
    claimant: Optional[UUID] = Field(None, alias="Claimant")
    claimant_full_name: Optional[str] = Field(None, alias="ClaimantFullName")
    country: Optional[str] = Field(None, alias="Country")
    currency: Optional[str] = Field(None, alias="Currency")
    description: Optional[str] = Field(None, alias="Description")
    distance: Optional[float] = Field(None, alias="Distance")
    division: Optional[int] = Field(None, alias="Division")
    expense_date: Optional[datetime] = Field(None, alias="ExpenseDate")
    expense_number: Optional[int] = Field(None, alias="ExpenseNumber")
    expense_type: Optional[int] = Field(None, alias="ExpenseType")
    expense_type_description: Optional[str] = Field(
        None, alias="ExpenseTypeDescription"
    )
    from_location: Optional[str] = Field(None, alias="FromLocation")
    payment_method: Optional[int] = Field(None, alias="PaymentMethod")
    per_diem_rate_amount: Optional[float] = Field(None, alias="PerDiemRateAmount")
    project: Optional[UUID] = Field(None, alias="Project")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    quantity: Optional[float] = Field(None, alias="Quantity")
    rate_fc: Optional[float] = Field(None, alias="RateFC")
    report: Optional[UUID] = Field(None, alias="Report")
    report_description: Optional[str] = Field(None, alias="ReportDescription")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    sys_created: Optional[datetime] = Field(None, alias="SysCreated")
    sys_creator: Optional[UUID] = Field(None, alias="SysCreator")
    sys_creator_full_name: Optional[str] = Field(None, alias="SysCreatorFullName")
    sys_modified: Optional[datetime] = Field(None, alias="SysModified")
    sys_modifier: Optional[UUID] = Field(None, alias="SysModifier")
    sys_modifier_full_name: Optional[str] = Field(None, alias="SysModifierFullName")
    to_location: Optional[str] = Field(None, alias="ToLocation")
    total_amount_dc: Optional[float] = Field(None, alias="TotalAmountDC")
    total_amount_fc: Optional[float] = Field(None, alias="TotalAmountFC")
    vendor: Optional[UUID] = Field(None, alias="Vendor")
