from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DivisionClassValue(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    class_01_id: Optional[UUID] = Field(None, alias="Class_01_ID")
    class_02_id: Optional[UUID] = Field(None, alias="Class_02_ID")
    class_03_id: Optional[UUID] = Field(None, alias="Class_03_ID")
    class_04_id: Optional[UUID] = Field(None, alias="Class_04_ID")
    class_05_id: Optional[UUID] = Field(None, alias="Class_05_ID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    customer: Optional[UUID] = Field(None, alias="Customer")
    division: Optional[int] = Field(None, alias="Division")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
