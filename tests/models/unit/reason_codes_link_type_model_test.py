from __future__ import annotations

from uuid import uuid4

from exact_online_sdk.models import ReasonCodesLinkType


def test_reason_codes_link_type_parses_aliases() -> None:
    link_type = ReasonCodesLinkType.model_validate(
        {
            "ID": str(uuid4()),
            "Reason": str(uuid4()),
            "Type": 4,
            "TypeDescription": "Cancellation",
        }
    )

    assert link_type.type == 4
    assert link_type.type_description == "Cancellation"
