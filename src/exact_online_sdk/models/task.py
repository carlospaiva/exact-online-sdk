from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Task(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_name: Optional[str] = Field(None, alias="AccountName")
    action_date: Optional[datetime] = Field(None, alias="ActionDate")
    attachments: Optional[Any] = Field(None, alias="Attachments")
    contact: Optional[UUID] = Field(None, alias="Contact")
    contact_full_name: Optional[str] = Field(None, alias="ContactFullName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    custom_task_type: Optional[UUID] = Field(None, alias="CustomTaskType")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    document_subject: Optional[str] = Field(None, alias="DocumentSubject")
    employee: Optional[UUID] = Field(None, alias="Employee")
    hid: Optional[int] = Field(None, alias="HID")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    opportunity: Optional[UUID] = Field(None, alias="Opportunity")
    opportunity_name: Optional[str] = Field(None, alias="OpportunityName")
    project: Optional[UUID] = Field(None, alias="Project")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    task_type: Optional[int] = Field(None, alias="TaskType")
    task_type_description: Optional[str] = Field(None, alias="TaskTypeDescription")
    user: Optional[UUID] = Field(None, alias="User")
    user_full_name: Optional[str] = Field(None, alias="UserFullName")
