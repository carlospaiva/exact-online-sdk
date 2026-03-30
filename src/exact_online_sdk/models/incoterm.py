from __future__ import annotations

from typing import Optional

from pydantic import Field

from .base import StrictModel


class Incoterm(StrictModel):
    id: Optional[int] = Field(default=None, alias="ID")
    code: Optional[str] = Field(default=None, alias="Code")
    description: Optional[str] = Field(default=None, alias="Description")
    version: Optional[int] = Field(default=None, alias="Version")
