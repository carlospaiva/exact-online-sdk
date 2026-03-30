from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ScheduleEntry(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    id: Optional[UUID] = Field(None, alias="ID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    day: Optional[int] = Field(None, alias="Day")
    division: Optional[int] = Field(None, alias="Division")
    end_time: Optional[datetime] = Field(None, alias="EndTime")
    hours: Optional[float] = Field(None, alias="Hours")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    schedule: Optional[UUID] = Field(None, alias="Schedule")
    schedule_code: Optional[str] = Field(None, alias="ScheduleCode")
    schedule_description: Optional[str] = Field(None, alias="ScheduleDescription")
    start_time: Optional[datetime] = Field(None, alias="StartTime")
