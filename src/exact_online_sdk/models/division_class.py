from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class DivisionClass(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    class_name_customer: Optional[UUID] = Field(None, alias="ClassNameCustomer")
    class_name_description: Optional[str] = Field(None, alias="ClassNameDescription")
    class_name_id: Optional[UUID] = Field(None, alias="ClassNameID")
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    description_term_id: Optional[int] = Field(None, alias="DescriptionTermID")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    sequence_nr: Optional[int] = Field(None, alias="SequenceNr")
