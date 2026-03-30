from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemAssortmentProperty(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    code: Optional[str] = Field(default=None, alias="Code")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    item_assortment_code: Optional[int] = Field(
        default=None, alias="ItemAssortmentCode"
    )
