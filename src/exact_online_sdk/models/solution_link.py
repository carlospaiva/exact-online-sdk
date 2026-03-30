from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SolutionLink(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: UUID = Field(..., alias="Account")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    division: Optional[int] = Field(None, alias="Division")
    external_solution_code: Optional[int] = Field(None, alias="ExternalSolutionCode")
    external_solution_name: Optional[str] = Field(None, alias="ExternalSolutionName")
    external_solution_url: Optional[str] = Field(None, alias="ExternalSolutionUrl")
    internal_solution_division: Optional[int] = Field(
        None, alias="InternalSolutionDivision"
    )
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    name: Optional[str] = Field(None, alias="Name")
    other_external_solution_name: Optional[str] = Field(
        None, alias="OtherExternalSolutionName"
    )
    solution_type: int = Field(..., alias="SolutionType")
    status: Optional[int] = Field(None, alias="Status")
