from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ProjectPlanningRecurring(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_name: Optional[str] = Field(None, alias="AccountName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    day_or_the_month: Optional[int] = Field(None, alias="DayOrTheMonth")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_code: Optional[str] = Field(None, alias="EmployeeCode")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    hours: Optional[float] = Field(None, alias="Hours")
    hours_per_day: Optional[float] = Field(None, alias="HoursPerDay")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    overtime_hours: Optional[float] = Field(None, alias="OvertimeHours")
    planning_recurring_type: Optional[int] = Field(None, alias="PlanningRecurringType")
    project: Optional[UUID] = Field(None, alias="Project")
    project_code: Optional[str] = Field(None, alias="ProjectCode")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    project_wbs: Optional[UUID] = Field(None, alias="ProjectWBS")
    project_wbs_description: Optional[str] = Field(None, alias="ProjectWBSDescription")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    status: Optional[int] = Field(None, alias="Status")
    type: Optional[int] = Field(None, alias="Type")
