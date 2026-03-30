from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AssetGroup(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    depreciation_method: Optional[UUID] = Field(None, alias="DepreciationMethod")
    depreciation_method_code: Optional[str] = Field(
        None, alias="DepreciationMethodCode"
    )
    depreciation_method_description: Optional[str] = Field(
        None, alias="DepreciationMethodDescription"
    )
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    gl_account_assets: Optional[UUID] = Field(None, alias="GLAccountAssets")
    gl_account_assets_code: Optional[str] = Field(None, alias="GLAccountAssetsCode")
    gl_account_assets_description: Optional[str] = Field(
        None, alias="GLAccountAssetsDescription"
    )
    gl_account_depreciation_bs: Optional[UUID] = Field(
        None, alias="GLAccountDepreciationBS"
    )
    gl_account_depreciation_bs_code: Optional[str] = Field(
        None, alias="GLAccountDepreciationBSCode"
    )
    gl_account_depreciation_bs_description: Optional[str] = Field(
        None, alias="GLAccountDepreciationBSDescription"
    )
    gl_account_depreciation_pl: Optional[UUID] = Field(
        None, alias="GLAccountDepreciationPL"
    )
    gl_account_depreciation_pl_code: Optional[str] = Field(
        None, alias="GLAccountDepreciationPLCode"
    )
    gl_account_depreciation_pl_description: Optional[str] = Field(
        None, alias="GLAccountDepreciationPLDescription"
    )
    gl_account_revaluation_bs: Optional[UUID] = Field(
        None, alias="GLAccountRevaluationBS"
    )
    gl_account_revaluation_bs_code: Optional[str] = Field(
        None, alias="GLAccountRevaluationBSCode"
    )
    gl_account_revaluation_bs_description: Optional[str] = Field(
        None, alias="GLAccountRevaluationBSDescription"
    )
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
