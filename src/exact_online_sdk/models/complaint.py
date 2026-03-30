from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Complaint(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_name: Optional[str] = Field(None, alias="AccountName")
    assigned_to: Optional[UUID] = Field(None, alias="AssignedTo")
    assigned_to_full_name: Optional[str] = Field(None, alias="AssignedToFullName")
    attachments: Optional[Any] = Field(None, alias="Attachments")
    complaint: Optional[str] = Field(None, alias="Complaint")
    contact: Optional[UUID] = Field(None, alias="Contact")
    contact_full_name: Optional[str] = Field(None, alias="ContactFullName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    document_subject: Optional[str] = Field(None, alias="DocumentSubject")
    hid: Optional[int] = Field(None, alias="HID")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    next_action: Optional[datetime] = Field(None, alias="NextAction")
    notes: Optional[str] = Field(None, alias="Notes")
    receipt_date: Optional[datetime] = Field(None, alias="ReceiptDate")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
