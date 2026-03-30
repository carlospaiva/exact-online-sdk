from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DocumentAttachment(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    attachment: Optional[bytes] = Field(default=None, alias="Attachment")
    document: UUID = Field(alias="Document")
    file_name: str = Field(alias="FileName")
    file_size: Optional[float] = Field(default=None, alias="FileSize")
    url: Optional[str] = Field(default=None, alias="Url")
