from __future__ import annotations

from uuid import uuid4

from exact_online_sdk.models import DocumentAttachmentInfo


def test_document_attachment_info_parses_aliases() -> None:
    attachment_id = uuid4()

    info = DocumentAttachmentInfo.model_validate(
        {
            "ID": str(attachment_id),
            "AttachmentFileName": "scan.png",
            "AttachmentFileSize": 1.5,
            "AttachmentUrl": "https://example.com/scan.png",
            "CanShowInWebView": False,
        }
    )

    assert info.id == attachment_id
    assert info.attachment_file_name == "scan.png"
    assert info.attachment_file_size == 1.5
    assert info.attachment_url == "https://example.com/scan.png"
    assert info.can_show_in_web_view is False
