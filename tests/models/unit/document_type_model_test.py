from __future__ import annotations

from datetime import datetime, timezone

from exact_online_sdk.models import DocumentType


def test_document_type_parses_aliases() -> None:
    created = datetime.now(timezone.utc)

    doc_type = DocumentType.model_validate(
        {
            "ID": 5,
            "Description": "Invoice",
            "DocumentIsCreatable": True,
            "Created": created.isoformat(),
        }
    )

    assert doc_type.id == 5
    assert doc_type.description == "Invoice"
    assert doc_type.document_is_creatable is True
    assert doc_type.created == created
