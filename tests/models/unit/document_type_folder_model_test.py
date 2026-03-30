from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from exact_online_sdk.models import DocumentTypeFolder


def test_document_type_folder_parses_aliases() -> None:
    folder_id = uuid4()
    created = datetime.now(timezone.utc)

    doc_type_folder = DocumentTypeFolder.model_validate(
        {
            "ID": str(uuid4()),
            "DocumentFolder": str(folder_id),
            "DocumentType": 2,
            "Created": created.isoformat(),
        }
    )

    assert doc_type_folder.document_folder == folder_id
    assert doc_type_folder.document_type == 2
    assert doc_type_folder.created == created
