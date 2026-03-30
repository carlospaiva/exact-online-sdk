from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class MailMessageAttachment(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    attachment: Optional[str] = Field(None, alias="Attachment")
    attachment_file_extension: Optional[str] = Field(
        None, alias="AttachmentFileExtension"
    )
    attachment_file_name: Optional[str] = Field(None, alias="AttachmentFileName")
    file_size: Optional[int] = Field(None, alias="FileSize")
    mail_message_id: Optional[UUID] = Field(None, alias="MailMessageID")
    mail_message_origin: Optional[int] = Field(None, alias="MailMessageOrigin")
    recipient_account: Optional[UUID] = Field(None, alias="RecipientAccount")
    sender_account: Optional[UUID] = Field(None, alias="SenderAccount")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    url: Optional[str] = Field(None, alias="Url")
