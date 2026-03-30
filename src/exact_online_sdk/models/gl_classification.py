from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class GLClassification(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    abstract: Optional[bool] = Field(None, alias="Abstract")
    balance: Optional[str] = Field(None, alias="Balance")
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    is_tuple_sub_element: Optional[bool] = Field(None, alias="IsTupleSubElement")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    name: Optional[str] = Field(None, alias="Name")
    nillable: Optional[bool] = Field(None, alias="Nillable")
    parent: Optional[UUID] = Field(None, alias="Parent")
    period_type: Optional[str] = Field(None, alias="PeriodType")
    substitution_group: Optional[str] = Field(None, alias="SubstitutionGroup")
    taxonomy_namespace: Optional[UUID] = Field(None, alias="TaxonomyNamespace")
    taxonomy_namespace_description: Optional[str] = Field(
        None, alias="TaxonomyNamespaceDescription"
    )
    type: Optional[UUID] = Field(None, alias="Type")
