from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Event(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_name: Optional[str] = Field(None, alias="AccountName")
    attachments: Optional[Any] = Field(None, alias="Attachments")
    campaign: Optional[UUID] = Field(None, alias="Campaign")
    campaign_description: Optional[str] = Field(None, alias="CampaignDescription")
    contact: Optional[UUID] = Field(None, alias="Contact")
    contact_full_name: Optional[str] = Field(None, alias="ContactFullName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    document_subject: Optional[str] = Field(None, alias="DocumentSubject")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    hid: Optional[int] = Field(None, alias="HID")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    opportunity: Optional[UUID] = Field(None, alias="Opportunity")
    opportunity_name: Optional[str] = Field(None, alias="OpportunityName")
    project: Optional[UUID] = Field(None, alias="Project")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    status: Optional[int] = Field(None, alias="Status")
    status_description: Optional[str] = Field(None, alias="StatusDescription")
    user: Optional[UUID] = Field(None, alias="User")
    user_full_name: Optional[str] = Field(None, alias="UserFullName")
