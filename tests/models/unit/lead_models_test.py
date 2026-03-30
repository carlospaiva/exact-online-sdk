from __future__ import annotations

from uuid import uuid4

from exact_online_sdk.models import LeadPurpose, LeadSource


def test_lead_source_accepts_alias_id() -> None:
    source_id = uuid4()

    lead_source = LeadSource.model_validate({"ID": str(source_id), "Code": "WEB"})

    assert lead_source.id == source_id
    assert lead_source.code == "WEB"
    assert lead_source.description is None


def test_lead_purpose_accepts_alias_id() -> None:
    purpose_id = uuid4()

    lead_purpose = LeadPurpose.model_validate(
        {"ID": str(purpose_id), "Code": "CONSULTING", "Description": "Consulting"}
    )

    assert lead_purpose.id == purpose_id
    assert lead_purpose.code == "CONSULTING"
    assert lead_purpose.description == "Consulting"
