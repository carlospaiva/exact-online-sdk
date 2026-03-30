from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ReasonCodesLinkType(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    reason: Optional[UUID] = Field(default=None, alias="Reason")
    type: Optional[int] = Field(default=None, alias="Type")
    type_description: Optional[str] = Field(default=None, alias="TypeDescription")
