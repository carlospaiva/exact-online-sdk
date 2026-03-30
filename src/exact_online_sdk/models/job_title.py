from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class JobTitle(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    job_code: Optional[str] = Field(None, alias="JobCode")
    job_group: Optional[UUID] = Field(None, alias="JobGroup")
    job_group_code: Optional[str] = Field(None, alias="JobGroupCode")
    job_group_description: Optional[str] = Field(None, alias="JobGroupDescription")
    job_level_from: Optional[int] = Field(None, alias="JobLevelFrom")
    job_level_to: Optional[int] = Field(None, alias="JobLevelTo")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
