from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Employment(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    hid: Optional[int] = Field(None, alias="HID")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    organization_unit: Optional[UUID] = Field(None, alias="OrganizationUnit")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    start_date_organization: Optional[datetime] = Field(
        None, alias="StartDateOrganization"
    )
