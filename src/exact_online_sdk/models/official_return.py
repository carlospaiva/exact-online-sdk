from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class OfficialReturn(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    amount: Optional[float] = Field(None, alias="Amount")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    document_subject: Optional[str] = Field(None, alias="DocumentSubject")
    frequency: Optional[int] = Field(None, alias="Frequency")
    is_correction: Optional[int] = Field(None, alias="IsCorrection")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    period: Optional[int] = Field(None, alias="Period")
    presentation_data: Optional[str] = Field(None, alias="PresentationData")
    presentation_date: Optional[datetime] = Field(None, alias="PresentationDate")
    presentation_file_name: Optional[str] = Field(None, alias="PresentationFileName")
    reference: Optional[str] = Field(None, alias="Reference")
    source: Optional[int] = Field(None, alias="Source")
    status: Optional[int] = Field(None, alias="Status")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    year: Optional[int] = Field(None, alias="Year")
