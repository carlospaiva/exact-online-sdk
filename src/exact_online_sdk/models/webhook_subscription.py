from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class WebhookSubscription(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    callback_url: Optional[str] = Field(None, alias="CallbackURL")
    client_id: Optional[UUID] = Field(None, alias="ClientID")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    topic: Optional[str] = Field(None, alias="Topic")
    user_id: Optional[UUID] = Field(None, alias="UserID")
