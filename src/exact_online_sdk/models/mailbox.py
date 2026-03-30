from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Mailbox(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_name: Optional[str] = Field(None, alias="AccountName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    for_division: Optional[int] = Field(None, alias="ForDivision")
    for_division_description: Optional[str] = Field(
        None, alias="ForDivisionDescription"
    )
    mailbox: Optional[str] = Field(None, alias="Mailbox")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    publish: Optional[int] = Field(None, alias="Publish")
    type: Optional[int] = Field(None, alias="Type")
    valid_from: Optional[datetime] = Field(None, alias="ValidFrom")
    valid_to: Optional[datetime] = Field(None, alias="ValidTo")
