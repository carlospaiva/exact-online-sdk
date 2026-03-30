from __future__ import annotations

from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import ReasonCode


def test_reason_code_parses_nested_types() -> None:
    type_id = uuid4()

    reason_code = ReasonCode.model_validate(
        {
            "ID": str(uuid4()),
            "Code": "RET",
            "Types": [
                {
                    "ID": str(type_id),
                    "Type": 1,
                    "TypeDescription": "Return",
                }
            ],
        }
    )

    assert reason_code.code == "RET"
    assert reason_code.types is not None
    assert reason_code.types[0].id == type_id
    assert reason_code.types[0].type == 1
    assert reason_code.types[0].type_description == "Return"


def test_reason_code_rejects_invalid_types_item() -> None:
    with pytest.raises(ValidationError) as exc:
        ReasonCode.model_validate({"Code": "RET", "Types": ["invalid"]})

    errors = exc.value.errors()
    assert errors[0]["loc"] == ("types", 0)
