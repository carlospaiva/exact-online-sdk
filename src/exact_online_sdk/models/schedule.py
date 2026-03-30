from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Schedule(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    active: Optional[int] = Field(None, alias="Active")
    average_hours: Optional[float] = Field(None, alias="AverageHours")
    billability_target: Optional[float] = Field(None, alias="BillabilityTarget")
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    days: Optional[float] = Field(None, alias="Days")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employment: Optional[UUID] = Field(None, alias="Employment")
    employment_cla: Optional[UUID] = Field(None, alias="EmploymentCLA")
    employment_hid: Optional[int] = Field(None, alias="EmploymentHID")
    employment_number: Optional[int] = Field(None, alias="EmploymentNumber")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    hours: Optional[float] = Field(None, alias="Hours")
    leave_hours_compensation: Optional[float] = Field(
        None, alias="LeaveHoursCompensation"
    )
    main: Optional[int] = Field(None, alias="Main")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    payment_parttime_factor: Optional[float] = Field(
        None, alias="PaymentParttimeFactor"
    )
    schedule_type: Optional[int] = Field(None, alias="ScheduleType")
    schedule_type_description: Optional[str] = Field(
        None, alias="ScheduleTypeDescription"
    )
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    start_week: Optional[int] = Field(None, alias="StartWeek")
