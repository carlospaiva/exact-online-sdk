from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, List
from uuid import uuid4

import pytest
from pytest_httpx import HTTPXMock

from exact_online_sdk.api.endpoints import AccountsAPI, SalesInvoicesAPI
from exact_online_sdk.client import ExactOnlineClient
from exact_online_sdk.config import Settings
from exact_online_sdk.models import Account, SalesInvoice

pytestmark = pytest.mark.e2e


class DummyAuth:
    def get_access_token(self) -> str:
        return "token"


def _settings() -> Settings:
    return Settings(
        client_id="client",
        client_secret="secret",
        redirect_uri="https://app.example/callback",
        base_url="https://api.example",
    )


def test_account_to_invoice_business_journey(httpx_mock: HTTPXMock) -> None:
    settings = _settings()
    client = ExactOnlineClient(settings=settings, auth=DummyAuth())

    accounts_api = AccountsAPI(client)
    invoices_api = SalesInvoicesAPI(client)

    # Step 1: create an Account
    account_id = uuid4()
    account_model = Account(name="Acme BV")

    httpx_mock.add_response(
        method="POST",
        url="https://api.example/api/v1/crm/Accounts",
        json={"ID": str(account_id), "Name": "Acme BV"},
    )

    created_account = accounts_api.create(account_model)
    assert isinstance(created_account, Account)
    assert created_account.name == "Acme BV"
    assert created_account.id == account_id

    # Step 2: create a SalesInvoice for that Account
    invoice_id = uuid4()
    invoice_date = datetime.now(timezone.utc)

    invoice_payload = {
        "OrderedBy": str(account_id),
        "Journal": "80",
        "InvoiceDate": invoice_date.isoformat(),
    }

    httpx_mock.add_response(
        method="POST",
        url="https://api.example/api/v1/salesinvoice/SalesInvoices",
        json={
            "InvoiceID": str(invoice_id),
            "OrderedBy": str(account_id),
            "Journal": "80",
            "InvoiceDate": invoice_date.isoformat(),
        },
    )

    created_invoice = invoices_api.create(invoice_payload)
    assert isinstance(created_invoice, SalesInvoice)
    assert created_invoice.ordered_by == account_id
    assert created_invoice.journal == "80"
    assert created_invoice.invoice_id == invoice_id

    # Step 3: list invoices for that Account using endpoint helpers
    list_response: List[dict[str, Any]] = [
        {
            "InvoiceID": str(invoice_id),
            "OrderedBy": str(account_id),
            "Journal": "80",
            "InvoiceDate": invoice_date.isoformat(),
        }
    ]

    httpx_mock.add_response(
        method="GET",
        url=re.compile(r"https://api\.example/api/v1/salesinvoice/SalesInvoices.*"),
        json={"value": list_response},
    )

    invoices = invoices_api.list(filters={"OrderedBy": str(account_id)})

    assert len(invoices) == 1
    fetched = invoices[0]
    assert isinstance(fetched, SalesInvoice)
    assert fetched.ordered_by == account_id
    assert fetched.invoice_id == invoice_id
    assert fetched.journal == "80"

    client.close()
