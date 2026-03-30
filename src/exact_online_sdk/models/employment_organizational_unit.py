from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class EmploymentOrganizationalUnit(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    department: Optional[UUID] = Field(None, alias="Department")
    department_code: Optional[str] = Field(None, alias="DepartmentCode")
    department_description: Optional[str] = Field(None, alias="DepartmentDescription")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    employment: Optional[UUID] = Field(None, alias="Employment")
    employment_hid: Optional[int] = Field(None, alias="EmploymentHID")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    job_title: Optional[UUID] = Field(None, alias="JobTitle")
    job_title_code: Optional[str] = Field(None, alias="JobTitleCode")
    job_title_description: Optional[str] = Field(None, alias="JobTitleDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
