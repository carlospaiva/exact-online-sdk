from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class EmploymentConditionGroup(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    cla_code_tax_office: Optional[str] = Field(None, alias="CLACodeTaxOffice")
    cla_code_tax_office_description: Optional[str] = Field(
        None, alias="CLACodeTaxOfficeDescription"
    )
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    hours_per_week: Optional[float] = Field(None, alias="HoursPerWeek")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    sbi_code: Optional[str] = Field(None, alias="SBICode")
    sbi_code_description: Optional[str] = Field(None, alias="SBICodeDescription")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
