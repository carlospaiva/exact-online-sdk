from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class CustomerItem(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    account: UUID = Field(alias="Account")
    account_code: Optional[str] = Field(default=None, alias="AccountCode")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    customer_item_code: Optional[str] = Field(default=None, alias="CustomerItemCode")
    division: Optional[int] = Field(default=None, alias="Division")
    item: UUID = Field(alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    type: Optional[str] = Field(default=None, alias="Type")
