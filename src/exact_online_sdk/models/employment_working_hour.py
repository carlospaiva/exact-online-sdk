from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class EmploymentWorkingHour(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    employment: Optional[UUID] = Field(None, alias="Employment")
    employment_hid: Optional[int] = Field(None, alias="EmploymentHID")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    hours_per_week: Optional[float] = Field(None, alias="HoursPerWeek")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    part_time_factor: Optional[float] = Field(None, alias="PartTimeFactor")
    schedule: Optional[UUID] = Field(None, alias="Schedule")
    schedule_average_hours: Optional[float] = Field(None, alias="ScheduleAverageHours")
    schedule_code: Optional[str] = Field(None, alias="ScheduleCode")
    schedule_days: Optional[float] = Field(None, alias="ScheduleDays")
    schedule_description: Optional[str] = Field(None, alias="ScheduleDescription")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
