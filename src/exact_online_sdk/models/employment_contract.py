from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class EmploymentContract(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    contract_flex_phase: Optional[int] = Field(None, alias="ContractFlexPhase")
    contract_flex_phase_description: Optional[str] = Field(
        None, alias="ContractFlexPhaseDescription"
    )
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    employee: Optional[UUID] = Field(None, alias="Employee")
    employee_full_name: Optional[str] = Field(None, alias="EmployeeFullName")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    employee_type: Optional[int] = Field(None, alias="EmployeeType")
    employee_type_description: Optional[str] = Field(
        None, alias="EmployeeTypeDescription"
    )
    employment: Optional[UUID] = Field(None, alias="Employment")
    employment_hid: Optional[int] = Field(None, alias="EmploymentHID")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    probation_end_date: Optional[datetime] = Field(None, alias="ProbationEndDate")
    probation_period: Optional[int] = Field(None, alias="ProbationPeriod")
    reason_contract: Optional[int] = Field(None, alias="ReasonContract")
    reason_contract_description: Optional[str] = Field(
        None, alias="ReasonContractDescription"
    )
    sequence: Optional[int] = Field(None, alias="Sequence")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
