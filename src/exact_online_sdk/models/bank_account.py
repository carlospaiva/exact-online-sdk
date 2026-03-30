from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class BankAccount(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    account: UUID = Field(alias="Account")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    bank: Optional[UUID] = Field(default=None, alias="Bank")
    bank_account: str = Field(alias="BankAccount")
    bank_account_holder_name: Optional[str] = Field(
        default=None, alias="BankAccountHolderName"
    )
    bank_description: Optional[str] = Field(default=None, alias="BankDescription")
    bank_name: Optional[str] = Field(default=None, alias="BankName")
    bic_code: Optional[str] = Field(default=None, alias="BICCode")
    blocked: Optional[bool] = Field(default=None, alias="Blocked")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    format: Optional[str] = Field(default=None, alias="Format")
    iban: Optional[str] = Field(default=None, alias="IBAN")
    main: Optional[bool] = Field(default=None, alias="Main")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    payment_service_account: Optional[UUID] = Field(
        default=None, alias="PaymentServiceAccount"
    )
    type: Optional[str] = Field(default=None, alias="Type")
    type_description: Optional[str] = Field(default=None, alias="TypeDescription")
