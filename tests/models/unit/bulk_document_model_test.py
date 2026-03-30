from __future__ import annotations

from exact_online_sdk.models import BulkDocument


def test_bulk_document_parses_aliases() -> None:
    document = BulkDocument.model_validate({"Subject": "Bulk", "Type": 7})

    assert isinstance(document, BulkDocument)
    assert document.subject == "Bulk"
    assert document.type == 7
