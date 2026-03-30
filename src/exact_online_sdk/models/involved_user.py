from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class InvolvedUser(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_city: Optional[str] = Field(None, alias="AccountCity")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_is_supplier: Optional[bool] = Field(None, alias="AccountIsSupplier")
    account_logo_thumbnail_url: Optional[str] = Field(
        None, alias="AccountLogoThumbnailUrl"
    )
    account_name: Optional[str] = Field(None, alias="AccountName")
    account_status: Optional[str] = Field(None, alias="AccountStatus")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    division: Optional[int] = Field(None, alias="Division")
    involved_user_role: Optional[UUID] = Field(None, alias="InvolvedUserRole")
    involved_user_role_description: Optional[str] = Field(
        None, alias="InvolvedUserRoleDescription"
    )
    is_main_contact: Optional[bool] = Field(None, alias="IsMainContact")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    person_email: Optional[str] = Field(None, alias="PersonEmail")
    person_phone: Optional[str] = Field(None, alias="PersonPhone")
    person_phone_extension: Optional[str] = Field(None, alias="PersonPhoneExtension")
    person_picture_thumbnail_url: Optional[str] = Field(
        None, alias="PersonPictureThumbnailUrl"
    )
    user: Optional[UUID] = Field(None, alias="User")
    user_full_name: Optional[str] = Field(None, alias="UserFullName")
