from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class HoursByDate(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_id: Optional[UUID] = Field(None, alias="AccountId")
    account_name: Optional[str] = Field(None, alias="AccountName")
    activity: Optional[UUID] = Field(None, alias="Activity")
    activity_description: Optional[str] = Field(None, alias="ActivityDescription")
    date: Optional[datetime] = Field(None, alias="Date")
    entry_id: Optional[UUID] = Field(None, alias="EntryId")
    hours_approved: Optional[float] = Field(None, alias="HoursApproved")
    hours_draft: Optional[float] = Field(None, alias="HoursDraft")
    hours_rejected: Optional[float] = Field(None, alias="HoursRejected")
    hours_submitted: Optional[float] = Field(None, alias="HoursSubmitted")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    notes: Optional[str] = Field(None, alias="Notes")
    project_code: Optional[str] = Field(None, alias="ProjectCode")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    project_id: Optional[UUID] = Field(None, alias="ProjectId")
    week_number: Optional[int] = Field(None, alias="WeekNumber")
