from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ExpenseReport(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    approved_date: Optional[datetime] = Field(None, alias="ApprovedDate")
    approver: Optional[UUID] = Field(None, alias="Approver")
    approver_comment: Optional[str] = Field(None, alias="ApproverComment")
    approver_comments: Optional[str] = Field(None, alias="ApproverComments")
    approver_full_name: Optional[str] = Field(None, alias="ApproverFullName")
    claimant: Optional[UUID] = Field(None, alias="Claimant")
    claimant_full_name: Optional[str] = Field(None, alias="ClaimantFullName")
    controlled_date: Optional[datetime] = Field(None, alias="ControlledDate")
    controller: Optional[UUID] = Field(None, alias="Controller")
    controller_full_name: Optional[str] = Field(None, alias="ControllerFullName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    expense_count: Optional[int] = Field(None, alias="ExpenseCount")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    rejected_date: Optional[datetime] = Field(None, alias="RejectedDate")
    rejecter: Optional[UUID] = Field(None, alias="Rejecter")
    rejecter_full_name: Optional[str] = Field(None, alias="RejecterFullName")
    report_number: Optional[int] = Field(None, alias="ReportNumber")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    submitted_date: Optional[datetime] = Field(None, alias="SubmittedDate")
    submitter: Optional[UUID] = Field(None, alias="Submitter")
    submitter_full_name: Optional[str] = Field(None, alias="SubmitterFullName")
    total_amount_dc: Optional[float] = Field(None, alias="TotalAmountDC")
