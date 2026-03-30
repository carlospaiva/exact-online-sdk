from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AddressState(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    country: Optional[str] = Field(default=None, alias="Country")
    display_value: Optional[str] = Field(default=None, alias="DisplayValue")
    latitude: Optional[float] = Field(default=None, alias="Latitude")
    longitude: Optional[float] = Field(default=None, alias="Longitude")
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[str] = Field(default=None, alias="State")
