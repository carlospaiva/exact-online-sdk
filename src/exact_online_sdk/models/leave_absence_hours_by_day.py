from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class LeaveAbsenceHoursByDay(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    created: Optional[datetime] = Field(None, alias="Created")
    date: Optional[datetime] = Field(None, alias="Date")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    employment: Optional[UUID] = Field(None, alias="Employment")
    employment_hid: Optional[int] = Field(None, alias="EmploymentHID")
    end_time: Optional[datetime] = Field(None, alias="EndTime")
    external_id_int: Optional[int] = Field(None, alias="ExternalIDInt")
    external_leave_absence_type: Optional[int] = Field(
        None, alias="ExternalLeaveAbsenceType"
    )
    hours: Optional[float] = Field(None, alias="Hours")
    modified: Optional[datetime] = Field(None, alias="Modified")
    start_time: Optional[datetime] = Field(None, alias="StartTime")
    status: Optional[int] = Field(None, alias="Status")
    type: Optional[int] = Field(None, alias="Type")
