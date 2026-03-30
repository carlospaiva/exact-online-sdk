from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class RequestAttachment(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    division: Optional[int] = Field(None, alias="Division")
    download_url: Optional[str] = Field(None, alias="DownloadUrl")
    file_name: str = Field(..., alias="FileName")
    file_size: Optional[float] = Field(None, alias="FileSize")
    request: Optional[UUID] = Field(None, alias="Request")
