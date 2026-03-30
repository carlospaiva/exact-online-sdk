from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import StrictModel


class DocumentType(StrictModel):
    id: Optional[int] = Field(default=None, alias="ID")
    created: Optional[datetime] = Field(default=None, alias="Created")
    description: Optional[str] = Field(default=None, alias="Description")
    document_is_creatable: Optional[bool] = Field(
        default=None, alias="DocumentIsCreatable"
    )
    document_is_deletable: Optional[bool] = Field(
        default=None, alias="DocumentIsDeletable"
    )
    document_is_updatable: Optional[bool] = Field(
        default=None, alias="DocumentIsUpdatable"
    )
    document_is_viewable: Optional[bool] = Field(
        default=None, alias="DocumentIsViewable"
    )
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    type_category: Optional[int] = Field(default=None, alias="TypeCategory")
