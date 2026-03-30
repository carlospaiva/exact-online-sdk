from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class LeadSource(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    code: Optional[str] = None
    description: Optional[str] = None
