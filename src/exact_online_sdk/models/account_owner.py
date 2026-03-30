from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AccountOwner(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_name: Optional[str] = Field(None, alias="AccountName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    owner_account: Optional[UUID] = Field(None, alias="OwnerAccount")
    owner_account_code: Optional[str] = Field(None, alias="OwnerAccountCode")
    owner_account_name: Optional[str] = Field(None, alias="OwnerAccountName")
    shares: Optional[float] = Field(None, alias="Shares")
