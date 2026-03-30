from __future__ import annotations

from datetime import datetime, timezone

from exact_online_sdk.models import DocumentTypeCategory


def test_document_type_category_parses_aliases() -> None:
    created = datetime.now(timezone.utc)

    category = DocumentTypeCategory.model_validate(
        {
            "ID": 1,
            "Description": "Sales",
            "Created": created.isoformat(),
        }
    )

    assert category.id == 1
    assert category.description == "Sales"
    assert category.created == created
