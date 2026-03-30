from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import StrictModel


class Currency(StrictModel):
    code: Optional[str] = Field(None, alias="Code")
    amount_precision: Optional[float] = Field(None, alias="AmountPrecision")
    created: Optional[datetime] = Field(None, alias="Created")
    description: Optional[str] = Field(None, alias="Description")
    modified: Optional[datetime] = Field(None, alias="Modified")
    price_precision: Optional[float] = Field(None, alias="PricePrecision")
