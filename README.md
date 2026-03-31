# exact-online-sdk

A robust, production-ready Python SDK for integrating with Exact Online APIs. It emphasizes reliability, type safety, and ergonomics for finance, CRM, logistics, and inventory workflows.

## Features

- **OAuth2 built-in** – automatic token acquisition/refresh with pluggable encrypted storage.
- **Strict Pydantic v2 models** – 210+ model files with request/response validation mirroring Exact payload schemas.
- **Sync + Async clients** – powered by `httpx`, sharing the same retry, timeout, and pagination semantics.
- **Retries, rate limiting, and request IDs** – exponential backoff, `Retry-After` honoring, and rich exception hierarchy with Exact request identifiers for support tickets.
- **270 endpoint classes** – CRUD helpers, typed pagination, and `$filter/$select` builders covering all 270 tracked Exact Online API entities across accountancy, activities, assets, budget, bulk, cashflow, CRM, documents, financial, general, HRM, inventory, logistics, mailbox, manufacturing, payroll, project, purchase, quotation, sales, subscription, system, users, VAT, webhooks, and sync endpoints.
- **Structured logging** – optional JSON output with automatic redaction of sensitive fields.
- **AWS Secrets Manager integration** – optional, thread-safe token storage via `boto3` (`pip install exact-online-sdk[aws]`).
- **100 % test coverage** – 738 tests enforced by CI (`--cov-fail-under=100`).

## Installation

```bash
# Development install (with tooling extras)
uv pip install -e .[dev]

# Production / consumer install
uv pip install exact-online-sdk

# With AWS Secrets Manager support
uv pip install exact-online-sdk[aws]
```

## Configuration

Set environment variables or a `.env` file in project root:

```env
EXACT_CLIENT_ID=your-client-id
EXACT_CLIENT_SECRET=your-client-secret
EXACT_REDIRECT_URI=https://your-app.example/callback
EXACT_BASE_URL=https://start.exactonline.nl
# Optional
EXACT_ENCRYPTION_KEY=base64url_fernet_key
EXACT_TOKEN_PATH=~/.exact_online_token.json.enc
EXACT_LOG_LEVEL=INFO
EXACT_LOG_JSON=false
EXACT_LOG_FILE=
EXACT_TIMEOUT=30
EXACT_USER_AGENT=exact-online-sdk/1.0.3 (+https://github.com/carlospaiva/exact-online-sdk)
```

The SDK derives default auth/token URLs from `EXACT_BASE_URL` (`/api/oauth2/auth` and `/api/oauth2/token`).

## Bootstrap Authentication

For first-time setup or local development, use `scripts/bootstrap_auth.py` to acquire and persist an OAuth token. This script supports two modes: manual callback URL paste, or a temporary localhost listener.

### Required environment variables

Add these to your `.env` file:

```env
EXACT_CLIENT_ID=your-client-id
EXACT_CLIENT_SECRET=your-client-secret
EXACT_REDIRECT_URI=https://localhost:8000/callback
EXACT_ENCRYPTION_KEY=your-fernet-key
EXACT_TOKEN_PATH=~/.exact_online_token.json.enc
```

**Security note**: Never commit `.env` files or hardcode secrets in source code. Add `.env` to your `.gitignore`.

### Generate a Fernet encryption key

Token persistence uses Fernet symmetric encryption. Generate a key:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Copy the output and set it as `EXACT_ENCRYPTION_KEY` in your `.env`.

### Manual mode

Prints the authorization URL and waits for you to paste the callback URL:

```bash
uv run python scripts/bootstrap_auth.py --mode manual
```

1. Open the printed URL in your browser
2. Authenticate with Exact Online
3. Copy the full callback URL from your browser
4. Paste it into the terminal prompt

### Listener mode

Starts a temporary HTTPS localhost server to capture the callback automatically.
When using listener mode, set both TLS file paths in your environment:

```env
EXACT_LISTENER_CERT_PATH=/absolute/path/to/listener-cert.pem
EXACT_LISTENER_KEY_PATH=/absolute/path/to/listener-key.pem
```

The `EXACT_REDIRECT_URI` value must use the `https` scheme for listener mode.

```bash
uv run python scripts/bootstrap_auth.py --mode listener
```

1. Open the printed URL in your browser
2. Authenticate with Exact Online
3. The browser redirects to localhost, the script captures the code, and the token is persisted

### Token persistence requirements

Tokens are only persisted when **both** `EXACT_ENCRYPTION_KEY` and `EXACT_TOKEN_PATH` are set. If either is missing, the bootstrap will **fail fast** with an error message indicating the missing configuration.

### Next steps after bootstrap

Once authenticated, you can use `scripts/fetch_accounts.py` to verify the connection. Note that this script still requires `EXACT_DIVISION` (set via environment variable or `--division` flag):

```bash
# Set division via environment
export EXACT_DIVISION=123456
uv run python scripts/fetch_accounts.py

# Or pass as argument
uv run python scripts/fetch_accounts.py --division 123456
```

**Important**: `bootstrap_auth.py` does not require `EXACT_DIVISION`, but `fetch_accounts.py` does.

```python
from exact_online_sdk import ExactOnlineClient, Settings

settings = Settings.from_env()
client = ExactOnlineClient(settings=settings)

# List accounts (first page)
accounts = client.get("crm/Accounts", params={"$top": 10})
print(accounts)
```

### Working with typed endpoints

```python
from exact_online_sdk.api.endpoints import ContactsAPI
from exact_online_sdk.models import Contact

contacts_api = ContactsAPI(client)

# Create using strict model validation
contact = Contact(first_name="Sam", last_name="Taylor", email="sam@example.com")
created = contacts_api.create(contact)

# Filter & paginate using OData helpers
results = contacts_api.list(
    filters={"Email": ("eq", "sam@example.com")},
    select=["ID", "FullName", "Email"],
    top=25,
)

for page in contacts_api.iter_pages(page_size=100):
    ...
```

### AWS Secrets Manager token storage

```python
from exact_online_sdk import ExactOnlineClient, Settings
from exact_online_sdk.auth import ExactOnlineAuth
from exact_online_sdk.contrib.aws import SecretsManagerTokenStorage

settings = Settings.from_env()
storage = SecretsManagerTokenStorage(
    "my-app/exact-online/oauth-token",
    region_name="eu-west-1",
)
auth = ExactOnlineAuth(settings, storage=storage)
client = ExactOnlineClient(settings=settings, auth=auth)

# Tokens are now persisted in AWS Secrets Manager.
# Safe for multi-threaded and serverless (Lambda) use.
accounts = client.get("crm/Accounts")
```

### Read-only mode for multi-container deployments

When multiple containers share a token (e.g. Prefect on ECS), use `ReadOnlyTokenStorage` in workers so only a dedicated Lambda refreshes the token:

```python
from exact_online_sdk import ExactOnlineClient, Settings
from exact_online_sdk.auth import ExactOnlineAuth
from exact_online_sdk.contrib.aws import ReadOnlyTokenStorage, SecretsManagerTokenStorage

settings = Settings.from_env()
inner = SecretsManagerTokenStorage("my-app/exact-online/oauth-token")
storage = ReadOnlyTokenStorage(inner)
auth = ExactOnlineAuth(settings, storage=storage)
client = ExactOnlineClient(settings=settings, auth=auth)

# Reads work normally; any accidental refresh attempt raises AuthenticationError.
accounts = client.get("crm/Accounts")
```

### Error handling with context

```python
from exact_online_sdk.exceptions import APIError, AuthenticationError

try:
    client.get("crm/Accounts")
except AuthenticationError as exc:
    logger.error("Auth failed: %s", exc)
except APIError as exc:
    logger.error(
        "Exact API error", status=exc.status_code, request_id=exc.context.get("request_id")
    )
```

### Response format handling

The SDK explicitly requests JSON responses from the Exact Online API by sending an `Accept: application/json` header on all API calls. This ensures consistent behavior and prevents the API from returning Atom/XML or other formats that the SDK does not parse.

If you need to override the response format for a specific request, you can pass a `$format` parameter. The SDK preserves explicit caller overrides and will not overwrite your preference:

```python
# The SDK sends Accept: application/json by default
accounts = client.get("crm/Accounts")

# Explicit format override is preserved
accounts = client.get("crm/Accounts", params={"$format": "xml"})
```

When the API returns a non-JSON success response (2xx status with unexpected content type), the SDK raises a descriptive `APIError` with context about the actual content type and URL. This replaces raw JSON parser failures with actionable error messages that help diagnose API behavior changes or misconfigurations.

Regression tests for JSON negotiation and non-JSON failure handling live in `tests/client/unit/` and `tests/auth/unit/`.

## Development & Testing

All commands are run through `uv` to ensure consistent virtual environments:

| Task                   | Command                                             |
| ---------------------- | --------------------------------------------------- |
| Install dependencies   | `uv sync`                                           |
| Format                 | `uv run black . && uv run isort .`                  |
| Lint                   | `uv run flake8 && uv run pylint src tests`          |
| Type check             | `uv run mypy src tests`                             |
| Unit/Integration tests | `uv run pytest` (or target subfolders)              |
| Coverage report        | `uv run pytest --cov=src --cov-report=term-missing` |

## Release Workflow

1. Bump the version in `pyproject.toml` (SemVer).
2. Run formatting, lint, type-check, and full test suite (see table above).
3. Build artifacts: `uv build` (wheel + sdist land in `dist/`).
4. Smoke-test the wheel: `uv pip install dist/exact_online_sdk-<version>-py3-none-any.whl` in a clean env.
5. Publish when ready: `uv publish` (requires configured PyPI token).
6. Tag the release (`git tag -a vX.Y.Z -m "Release X.Y.Z"`) and push tags.

## Contributing & Support

- See [AGENTS.md](AGENTS.md) for detailed engineering guidelines, security posture, and release expectations.
- Issues and PRs are welcome—please include tests and documentation for any behavior change.

## License

MIT License
