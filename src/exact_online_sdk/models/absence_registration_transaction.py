from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AbsenceRegistrationTransaction(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    absence_registration: Optional[UUID] = Field(None, alias="AbsenceRegistration")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    end_time: Optional[datetime] = Field(None, alias="EndTime")
    expected_end_date: Optional[datetime] = Field(None, alias="ExpectedEndDate")
    hours: Optional[float] = Field(None, alias="Hours")
    hours_first_day: Optional[float] = Field(None, alias="HoursFirstDay")
    hours_last_day: Optional[float] = Field(None, alias="HoursLastDay")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    notification_moment: Optional[datetime] = Field(None, alias="NotificationMoment")
    percentage_disablement: Optional[float] = Field(None, alias="PercentageDisablement")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    start_time: Optional[datetime] = Field(None, alias="StartTime")
    status: Optional[int] = Field(None, alias="Status")
