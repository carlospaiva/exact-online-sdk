from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AccountantInfo(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    address_line1: Optional[str] = Field(None, alias="AddressLine1")
    address_line2: Optional[str] = Field(None, alias="AddressLine2")
    address_line3: Optional[str] = Field(None, alias="AddressLine3")
    city: Optional[str] = Field(None, alias="City")
    email: Optional[str] = Field(None, alias="Email")
    is_accountant: Optional[bool] = Field(None, alias="IsAccountant")
    logo: Optional[str] = Field(None, alias="Logo")
    menu_logo_url: Optional[str] = Field(None, alias="MenuLogoUrl")
    name: Optional[str] = Field(None, alias="Name")
    phone: Optional[str] = Field(None, alias="Phone")
    postcode: Optional[str] = Field(None, alias="Postcode")
    website: Optional[str] = Field(None, alias="Website")
