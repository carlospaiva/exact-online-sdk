from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from exact_online_sdk.models import DocumentCategory


def test_document_category_parses_aliases() -> None:
    category_id = uuid4()
    created = datetime.now(timezone.utc)

    category = DocumentCategory.model_validate(
        {
            "ID": str(category_id),
            "Description": "Contracts",
            "Created": created.isoformat(),
        }
    )

    assert category.id == category_id
    assert category.description == "Contracts"
    assert category.created == created
