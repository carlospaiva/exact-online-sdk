from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DocumentTypeFolder(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    division: Optional[int] = Field(default=None, alias="Division")
    document_folder: Optional[UUID] = Field(default=None, alias="DocumentFolder")
    document_type: Optional[int] = Field(default=None, alias="DocumentType")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
