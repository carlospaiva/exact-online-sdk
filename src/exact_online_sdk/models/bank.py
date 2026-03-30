from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Bank(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    bank_name: Optional[str] = Field(None, alias="BankName")
    bic_code: Optional[str] = Field(None, alias="BICCode")
    country: Optional[str] = Field(None, alias="Country")
    created: Optional[datetime] = Field(None, alias="Created")
    description: Optional[str] = Field(None, alias="Description")
    format: Optional[str] = Field(None, alias="Format")
    home_page_address: Optional[str] = Field(None, alias="HomePageAddress")
    modified: Optional[datetime] = Field(None, alias="Modified")
    status: Optional[str] = Field(None, alias="Status")
