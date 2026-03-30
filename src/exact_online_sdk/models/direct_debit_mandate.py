from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DirectDebitMandate(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: UUID = Field(..., alias="Account")
    attachment: Optional[str] = Field(None, alias="Attachment")
    attachment_file_name: Optional[str] = Field(None, alias="AttachmentFileName")
    bank_account: UUID = Field(..., alias="BankAccount")
    cancellation_date: Optional[datetime] = Field(None, alias="CancellationDate")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    first_send: Optional[int] = Field(None, alias="FirstSend")
    main: Optional[int] = Field(None, alias="Main")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    payment_type: Optional[int] = Field(None, alias="PaymentType")
    reference: Optional[str] = Field(None, alias="Reference")
    signature_date: Optional[datetime] = Field(None, alias="SignatureDate")
    type: Optional[int] = Field(None, alias="Type")
