from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AccountClass(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    code: Optional[str] = Field(default=None, alias="Code")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    credit_management_scenario: Optional[UUID] = Field(
        default=None, alias="CreditManagementScenario"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
