from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AccountInvolvedAccount(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_name: Optional[str] = Field(None, alias="AccountName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    involved_account: Optional[UUID] = Field(None, alias="InvolvedAccount")
    involved_account_relation_type_description: Optional[str] = Field(
        None, alias="InvolvedAccountRelationTypeDescription"
    )
    involved_account_relation_type_description_term_id: Optional[int] = Field(
        None, alias="InvolvedAccountRelationTypeDescriptionTermId"
    )
    involved_account_relation_type_id: Optional[int] = Field(
        None, alias="InvolvedAccountRelationTypeId"
    )
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
