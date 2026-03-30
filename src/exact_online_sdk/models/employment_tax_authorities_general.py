from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class EmploymentTaxAuthoritiesGeneral(StrictModel):
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
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    type_of_income: Optional[int] = Field(None, alias="TypeOfIncome")
    type_of_income_description: Optional[str] = Field(
        None, alias="TypeOfIncomeDescription"
    )
