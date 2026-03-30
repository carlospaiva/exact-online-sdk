from __future__ import annotations

from enum import IntEnum


class QuotationStatus(IntEnum):
    REJECTED = 5
    REVIEWED_AND_CLOSED = 6
    RECOVERY = 10
    DRAFT = 20
    OPEN = 25
    PROCESSING = 35
    PRINTED = 40
    ACCEPTED = 50
    AWAITING_ONLINE_ACCEPTANCE = 60
    ACCEPTED_WITH_PROCESSING_ERROR = 70
