from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AbsenceRegistration(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    cause: Optional[int] = Field(None, alias="Cause")
    cause_code: Optional[str] = Field(None, alias="CauseCode")
    cause_description: Optional[str] = Field(None, alias="CauseDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    kind: Optional[int] = Field(None, alias="Kind")
    kind_code: Optional[str] = Field(None, alias="KindCode")
    kind_description: Optional[str] = Field(None, alias="KindDescription")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
