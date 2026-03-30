from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Warehouse(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    code: Optional[str] = Field(default=None, alias="Code")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    default_storage_location: Optional[UUID] = Field(
        default=None, alias="DefaultStorageLocation"
    )
    default_storage_location_code: Optional[str] = Field(
        default=None, alias="DefaultStorageLocationCode"
    )
    default_storage_location_description: Optional[str] = Field(
        default=None, alias="DefaultStorageLocationDescription"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    e_mail: Optional[str] = Field(default=None, alias="EMail")
    main: Optional[int] = Field(default=None, alias="Main")
    manager_user: Optional[UUID] = Field(default=None, alias="ManagerUser")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    use_storage_locations: Optional[int] = Field(
        default=None, alias="UseStorageLocations"
    )
