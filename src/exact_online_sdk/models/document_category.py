from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DocumentCategory(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    created: Optional[datetime] = Field(default=None, alias="Created")
    description: Optional[str] = Field(default=None, alias="Description")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
