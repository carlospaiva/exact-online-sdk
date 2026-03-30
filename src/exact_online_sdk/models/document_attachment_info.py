from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DocumentAttachmentInfo(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    attachment_file_name: Optional[str] = Field(
        default=None, alias="AttachmentFileName"
    )
    attachment_file_size: Optional[float] = Field(
        default=None, alias="AttachmentFileSize"
    )
    attachment_url: Optional[str] = Field(default=None, alias="AttachmentUrl")
    can_show_in_web_view: Optional[bool] = Field(default=None, alias="CanShowInWebView")
