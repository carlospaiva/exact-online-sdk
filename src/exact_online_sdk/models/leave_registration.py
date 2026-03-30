from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class LeaveRegistration(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    end_time: Optional[datetime] = Field(None, alias="EndTime")
    hours: Optional[float] = Field(None, alias="Hours")
    hours_first_day: Optional[float] = Field(None, alias="HoursFirstDay")
    hours_last_day: Optional[float] = Field(None, alias="HoursLastDay")
    leave_type: Optional[UUID] = Field(None, alias="LeaveType")
    leave_type_code: Optional[str] = Field(None, alias="LeaveTypeCode")
    leave_type_description: Optional[str] = Field(None, alias="LeaveTypeDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    start_time: Optional[datetime] = Field(None, alias="StartTime")
    status: Optional[int] = Field(None, alias="Status")
