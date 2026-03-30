from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class GLAccountClassificationMapping(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    classification: Optional[UUID] = Field(None, alias="Classification")
    classification_code: Optional[str] = Field(None, alias="ClassificationCode")
    classification_description: Optional[str] = Field(
        None, alias="ClassificationDescription"
    )
    division: Optional[int] = Field(None, alias="Division")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(None, alias="GLAccountDescription")
    gl_scheme_code: Optional[str] = Field(None, alias="GLSchemeCode")
    gl_scheme_description: Optional[str] = Field(None, alias="GLSchemeDescription")
    gl_scheme_id: Optional[UUID] = Field(None, alias="GLSchemeID")
