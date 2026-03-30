from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field, StrictBool

from .base import StrictModel


class Unit(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    active: Optional[StrictBool] = Field(default=None, alias="Active")
    code: Optional[str] = Field(default=None, alias="Code")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    main: Optional[int] = Field(default=None, alias="Main")
    time_unit: Optional[str] = Field(default=None, alias="TimeUnit")
    type: Optional[str] = Field(default=None, alias="Type")
