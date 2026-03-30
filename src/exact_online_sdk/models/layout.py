from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Layout(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    category: Optional[int] = Field(None, alias="Category")
    category_name: Optional[str] = Field(None, alias="CategoryName")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    dd_view: Optional[UUID] = Field(None, alias="DDView")
    division: Optional[int] = Field(None, alias="Division")
    language: Optional[str] = Field(None, alias="Language")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    status: Optional[int] = Field(None, alias="Status")
    subject: Optional[str] = Field(None, alias="Subject")
    type: Optional[int] = Field(None, alias="Type")
