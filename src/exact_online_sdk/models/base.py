from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


def _snake_to_pascal(s: str) -> str:
    parts = s.split("_")
    pascal = "".join(p.capitalize() for p in parts)
    if s == "id":
        return "ID"
    return pascal


class StrictModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        populate_by_name=True,
        frozen=False,
        alias_generator=_snake_to_pascal,
        loc_by_alias=False,
        validate_by_name=True,
    )

    def model_dump(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        """Ensure default dumps use JSON mode so aliases serialize to API payloads."""
        if "mode" not in kwargs:
            kwargs["mode"] = "json"
        return super().model_dump(*args, **kwargs)
