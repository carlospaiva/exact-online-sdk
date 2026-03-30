from __future__ import annotations

from uuid import uuid4

from exact_online_sdk.models import BulkDocumentAttachment


def test_bulk_document_attachment_parses_aliases() -> None:
    document_id = uuid4()

    attachment = BulkDocumentAttachment.model_validate(
        {"Document": str(document_id), "FileName": "bulk.pdf"}
    )

    assert isinstance(attachment, BulkDocumentAttachment)
    assert attachment.document == document_id
    assert attachment.file_name == "bulk.pdf"
