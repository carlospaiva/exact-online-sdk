from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class MailMessagesSent(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    bank: Optional[UUID] = Field(None, alias="Bank")
    bank_account: Optional[str] = Field(None, alias="BankAccount")
    country: Optional[str] = Field(None, alias="Country")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    for_division: Optional[int] = Field(None, alias="ForDivision")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    operation: Optional[int] = Field(None, alias="Operation")
    original_message: Optional[UUID] = Field(None, alias="OriginalMessage")
    original_message_subject: Optional[str] = Field(
        None, alias="OriginalMessageSubject"
    )
    partner_key: Optional[UUID] = Field(None, alias="PartnerKey")
    quantity: Optional[float] = Field(None, alias="Quantity")
    recipient_account: Optional[UUID] = Field(None, alias="RecipientAccount")
    recipient_deleted: Optional[int] = Field(None, alias="RecipientDeleted")
    recipient_mailbox: Optional[str] = Field(None, alias="RecipientMailbox")
    recipient_mailbox_description: Optional[str] = Field(
        None, alias="RecipientMailboxDescription"
    )
    recipient_mailbox_id: Optional[UUID] = Field(None, alias="RecipientMailboxID")
    recipient_status: Optional[int] = Field(None, alias="RecipientStatus")
    recipient_status_description: Optional[str] = Field(
        None, alias="RecipientStatusDescription"
    )
    sender_account: Optional[UUID] = Field(None, alias="SenderAccount")
    sender_date_sent: Optional[datetime] = Field(None, alias="SenderDateSent")
    sender_deleted: Optional[int] = Field(None, alias="SenderDeleted")
    sender_ip_address: Optional[str] = Field(None, alias="SenderIPAddress")
    sender_mailbox: Optional[str] = Field(None, alias="SenderMailbox")
    sender_mailbox_description: Optional[str] = Field(
        None, alias="SenderMailboxDescription"
    )
    sender_mailbox_id: Optional[UUID] = Field(None, alias="SenderMailboxID")
    subject: Optional[str] = Field(None, alias="Subject")
    type: Optional[int] = Field(None, alias="Type")
