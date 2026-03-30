from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class EmploymentSalary(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    average_hours_per_week: Optional[float] = Field(None, alias="AverageHoursPerWeek")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    employment: Optional[UUID] = Field(None, alias="Employment")
    employment_hid: Optional[int] = Field(None, alias="EmploymentHID")
    employment_salary_type: Optional[int] = Field(None, alias="EmploymentSalaryType")
    employment_salary_type_description: Optional[str] = Field(
        None, alias="EmploymentSalaryTypeDescription"
    )
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    external_id: Optional[str] = Field(None, alias="ExternalID")
    full_time_salary: Optional[float] = Field(None, alias="FulltimeSalary")
    hours_per_week: Optional[float] = Field(None, alias="HoursPerWeek")
    internal_rate: Optional[float] = Field(None, alias="InternalRate")
    job_level: Optional[int] = Field(None, alias="JobLevel")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    part_time_factor: Optional[float] = Field(None, alias="PartTimeFactor")
    part_time_percentage: Optional[float] = Field(None, alias="PartTimePercentage")
    salary: Optional[float] = Field(None, alias="Salary")
    schedule: Optional[UUID] = Field(None, alias="Schedule")
    schedule_code: Optional[str] = Field(None, alias="ScheduleCode")
    schedule_description: Optional[str] = Field(None, alias="ScheduleDescription")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
