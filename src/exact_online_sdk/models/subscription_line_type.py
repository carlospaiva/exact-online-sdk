from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import StrictModel


class SubscriptionLineType(StrictModel):
    id: Optional[int] = Field(None, alias="ID")
    description: Optional[str] = Field(None, alias="Description")
