from __future__ import annotations

from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemAssortment(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    code: Optional[int] = Field(default=None, alias="Code")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    properties: Optional[Any] = Field(default=None, alias="Properties")
