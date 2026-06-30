# AGENTS.md — Engineering Manual

**Project:** template-web-enterprise  
**Purpose:** Foundation for enterprise web systems (SGCI, CRM, ERP, Finance, HR, and AI-powered business applications)  
**Stack:** Python 3.12 · Django 6 · PostgreSQL 16 · Redis 7 · Docker · Nginx  
**Audience:** Human developers and AI coding agents (OpenCode, GPT, Claude, Gemini, and future models)

---

## 1. Project Vision

Build the definitive open-source Django starter for business-critical web systems. The template is the shared substrate for a family of products: SGCI (grant management), CRM, ERP, Finance, and HR. It must remain generic enough to power any of them, yet opinionated enough to enforce consistency across all of them.

## 2. Engineering Principles

1. **Convention over configuration.** Opinions are baked into the scaffold. Developers override only what differs.
2. **Production parity.** The Docker Compose topology mirrors production. If it works in `make up`, it works in production.
3. **12-Factor App.** Config is extracted from code via environment variables. Every deploy is repeatable and immutable.
4. **Defence in depth.** Clean layers (service layer → middleware → permissions → exceptions) enforce separation of concerns.
5. **Fail closed.** Security defaults deny. Permissions are explicit. Sensible defaults are never permissive.
6. **Small, focused apps.** Each Django app owns one bounded context. Cross-app communication goes through services, not direct imports.

## 3. Clean Architecture

```
Presentation Layer    │  views, serializers, URL patterns
Service Layer         │  backend/common/services/ – orchestration logic
Domain Layer          │  backend/apps/*/ – models, domain logic
Infrastructure Layer  │  backend/common/ – middleware, permissions, utils
```

**Dependency rule:** Inner layers never import from outer layers. `apps/*` may import from `common/`, but `common/` never imports from `apps/*`.

## 4. Folder Responsibilities

| Path | Responsibility |
|------|---------------|
| `backend/apps/*/` | One Django app per bounded business domain |
| `backend/common/` | Shared primitives: constants, exceptions, helpers, middleware, mixins, permissions, services, utils |
| `backend/core/` | Django project root — settings, root URL conf, WSGI/ASGI entrypoints |
| `backend/core/settings/` | Split settings: `base.py` (shared) → `development.py` / `testing.py` / `production.py` |
| `backend/requirements/` | Split dependencies: `base.txt` (shared) → `dev.txt` / `prod.txt` |
| `backend/tests/` | Project-wide integration and end-to-end tests |
| `docker/` | Per-service Docker assets (Dockerfiles, configs, entrypoint scripts) |
| `env/` | `.env.dev`, `.env.prod`, `.env.test` — one per environment |
| `frontend/` | Frontend application (framework TBD by the team adopting the template) |
| `scripts/` | Automation and utility scripts |
| `docs/` | ADRs, runbooks, architecture decision records |

## 5. Django Architecture

### Settings resolution

```
core/settings/__init__.py  →  imports development.py (default)
                      ↕
base.py  ←  environment variables via django-environ
   ↑
development.py  │  testing.py  │  production.py
```

- `DJANGO_SETTINGS_MODULE` determines the active settings file.
- `base.py` is always the foundation. Environment files inherit and override only what differs.
- `django-environ` reads from the `.env` file at the project root.
- Never hardcode secrets, hostnames, or environment-specific values in settings.

### URL resolution

- Root URLconf at `core/urls.py` includes app URLs via `path("api/", include("apps.<app>.urls"))`.
- Each app owns its own `urls.py` with namespaced routes.
- API versioning uses a URL prefix (`/api/v1/`).

### ASGI / WSGI

- `wsgi.py` for Gunicorn (HTTP API).
- `asgi.py` for Daphne / Uvicorn (WebSockets, async consumers).

## 6. App Organization

Every Django app under `backend/apps/` follows this layout:

```
apps/<app_name>/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
├── serializers.py        (if REST API is present)
├── services.py           (or a services/ package)
├── tasks.py              (Celery/Huey tasks)
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_views.py
└── migrations/
    └── __init__.py
```

**Rules:**
- Keep models thin (validation + relationships). Business logic goes in `services.py`.
- Keep views thin (request parsing + response rendering). Orchestration goes in services.
- Each app declares its own URL namespace.
- Tests mirror the module structure (`test_models.py` for models, etc.).

## 7. Coding Standards

- All code is written in Python 3.12+ using modern type annotations.
- Every function and method has typed signatures. Use `|` syntax for unions (`str | None`), `list[X]`, `dict[str, X]`.
- Use `@dataclass` or Pydantic models for complex data containers.
- Avoid `*args` and `**kwargs` unless wrapping a foreign API.
- Prefer explicit over implicit. No dynamic attribute access, no `setattr` tricks.
- Use `pathlib.Path` for all filesystem paths.
- No print statements in production code — use the logging framework.

## 8. Python Style Guide

| Concern | Tool | Command |
|---------|------|---------|
| Linting | ruff | `ruff check .` |
| Formatting | ruff format | `ruff format .` |
| Type checking | mypy | `mypy backend/` |

Configuration lives in `pyproject.toml`. Rules enforced: line length 120, double quotes for strings, isort-compatible import sorting, trailing commas in multi-line collections, two blank lines before classes/functions, one before methods. No bare `except:`, no `# noqa` without a rule code.

## 9. Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Django apps | `snake_case`, singular | `accounts`, `billing`, `inventory` |
| Models | `PascalCase`, singular | `class PurchaseOrder` |
| Model fields | `snake_case` | `created_at`, `is_active` |
| Views (FBV) | `snake_case` | `def list_invoices(request)` |
| Views (CBV) | `PascalCase` | `class InvoiceDetailView` |
| Services | `snake_case` prefix `service` | `def create_invoice_service(...)` |
| Serializers | `PascalCase` suffix `Serializer` | `class InvoiceSerializer` |
| URL patterns | `snake_case` | `path("invoices/", ...)` |
| Management commands | `snake_case` | `class ImportOrdersCommand` |
| Tests | `snake_case` prefix `test_` | `def test_invoice_total()` |
| Private helpers | `_leading_underscore` | `def _calculate_tax(amount)` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_LOGIN_ATTEMPTS = 5` |
| Exceptions | `PascalCase` suffix `Error` | `class PaymentGatewayError(Exception)` |

## 10. Environment Variables

All configuration is driven by environment variables loaded via `django-environ`. Never hardcode configuration in settings files.

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | Yes | Django secret key (rotate per environment) |
| `DEBUG` | Yes | Boolean — must be `False` in production |
| `ALLOWED_HOSTS` | Yes | Comma-separated domain whitelist |
| `DATABASE_URL` | No | PostgreSQL DSN; falls back to SQLite for local dev |
| `REDIS_URL` | No | Redis DSN; optional for dev |
| `LANGUAGE_CODE` | No | Default `en-us` |
| `TIME_ZONE` | No | Default `UTC` |
| `USE_TZ` | No | Default `True` |
| `STATIC_URL` | No | Default `/static/` |
| `MEDIA_URL` | No | Default `/media/` |

**Rules:**
- Every variable has a documented default or is clearly marked required.
- `.env.example` documents every variable with a placeholder value. Keep it in sync.
- `env/.env.dev` is committed with safe defaults for local development.
- `env/.env.prod` and `env/.env.test` contain only placeholders — real values are injected at deploy time.
- Never commit real secrets. Use your secret manager (GitHub Secrets, Vault, 1Password, etc.).

## 11. Dependency Management

Dependencies are split into three files under `backend/requirements/`:

```
base.txt  →  shared across all environments (Django, django-environ, psycopg, redis)
dev.txt   →  base.txt + dev-only (pytest, ruff, mypy, factory_boy, ipython)
prod.txt  →  base.txt + prod-only (gunicorn, sentry-sdk, uvicorn)
```

**Rules:**
- Pin major/minor versions (`django>=6.0,<6.1`), never pin patch unless required.
- `dev.txt` and `prod.txt` start with `-r base.txt`.
- Add a new dependency to `base.txt` only if it is used in every environment.
- Keep the dependency tree lean. No dependency is added without a clear justification in the commit message.

## 12. Database Guidelines

- **PostgreSQL 16** is the production and staging database. SQLite is acceptable only for local development.
- Every model gets `id` (UUIDField or BigAutoField), `created_at`, `updated_at`, and `is_active` unless there is a specific reason not to.
- Use Django's built-in `db_index` for foreign keys and frequently-queried fields.
- Prefer `JSONField` over join tables for loosely-structured metadata.
- All migrations are reviewed before merging. Never squash migrations on a shared branch.
- Raw SQL is forbidden unless approved by the lead architect. When used, it must be wrapped in a named `RunSQL` migration with a comment explaining why Django ORM is insufficient.

## 13. API Standards

- **Versioning:** URL prefix `/api/v1/`, `/api/v2/`.
- **Format:** All requests and responses use JSON. No XML.
- **Errors:** Consistent error envelope: `{"error": {"code": "...", "detail": "...", "field": "..."}}`
- **Pagination:** Cursor-based pagination for list endpoints. Page size defaults to 100.
- **Authentication:** JWT (via `djangorestframework-simplejwt` or similar).
- **Documentation:** OpenAPI/Swagger auto-generated. Every endpoint has `description`, `summary`, `tags`, and `request/response examples`.
- **Idempotency:** Mutating endpoints support an `Idempotency-Key` header for safe retries.

## 14. Security Rules

- `DEBUG` is never `True` in production.
- `SECRET_KEY` is rotated per environment and never committed.
- `ALLOWED_HOSTS` is restricted to known domains.
- All passwords hashed via Django's `PBKDF2PasswordHasher` (or an upgrade listed in `PASSWORD_HASHERS`).
- Session cookies: `HTTPOnly`, `Secure`, `SameSite=Lax`.
- CSRF protection is enabled globally.
- API rate limiting is applied at the Nginx or middleware layer.
- File uploads are validated by type and size. `Content-Type` is verified server-side, not trusted from the client.
- SQL injection is prevented via Django ORM parameterised queries. Raw SQL (when approved) uses `cursor.execute(sql, params)` with positional or named placeholders.
- All tenant-scoped queries include the tenant filter. Never trust client-supplied IDs without ownership verification.

## 15. Performance Rules

- **N+1 queries:** Use `select_related()` and `prefetch_related()` for every FK and M2M traversal in views and serializers.
- **Connection pooling:** PgBouncer or Django's `CONN_MAX_AGE`.
- **Redis** for: session storage, cache framework, Celery broker, rate limiting.
- **Static files:** Served by Nginx/CDN in production, never by Django.
- **Media files:** S3-compatible storage (django-storages) in production.
- **Background tasks:** Offloaded to Celery / Huey. Never run long operations in the request-response cycle.
- **Query count middleware** warns on views exceeding 50 queries per request (configurable).

## 16. Logging Policy

- **Structure:** All logs are structured JSON in production, plain text in development.
- **Levels:**
  - `DEBUG` — development only, verbose diagnostic info
  - `INFO` — startup, shutdown, successful operations
  - `WARNING` — unexpected but handled situations (e.g., rate limit approaching)
  - `ERROR` — recoverable errors (e.g., external API failure)
  - `CRITICAL` — unrecoverable errors (e.g., database connection failure)
- **Context:** Every log record includes `request_id`, `user_id`, `app_name`, and `environment`.
- **Sensitive data:** Never log passwords, tokens, PII, or session keys. Use a sanitisation filter.
- **Third-party:** Sentry for error tracking in production. Console + file in development.

## 17. Testing Strategy

| Layer | Tool | What to test |
|-------|------|-------------|
| Unit | `pytest` + `pytest-django` | Models (validations, properties, custom managers), services (business rules, edge cases), helpers, permissions |
| Integration | `pytest` + `factory_boy` | API endpoints (status codes, response shape, auth enforcement), middleware behaviour, database transactions |
| E2E | Playwright / Selenium (optional) | Critical user journeys (sign-up, create order, checkout) |

**Rules:**
- Every new feature includes tests. Test coverage minimum: 90%.
- Use `factory_boy` factories, not `Model.objects.create()` in test setup.
- Mark slow tests with `@pytest.mark.slow`. Run them separately from the fast suite.
- Tests are idempotent and isolated. Never depend on test execution order.
- Use Django's `override_settings` for environment-specific test scenarios.

Run suite: `make test` (or `pytest`).

## 18. Git Workflow

```
main          ─── production-ready, protected
  ├── develop ─── integration branch
  │     ├── feature/*  ─── new features
  │     ├── fix/*      ─── bug fixes
  │     └── chore/*    ─── maintenance
  └── release/* ─── release candidates
```

- `main` is protected. Only release managers merge into it.
- `develop` is the default branch for pull requests.
- Feature branches are short-lived (< 3 days). Large features are broken into smaller, mergeable increments.
- After merge, delete the source branch.

## 19. Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]
```

| Type | Usage |
|------|-------|
| `feat` | New feature |
| `fix` | Bug fix |
| `chore` | Maintenance (deps, config, tooling) |
| `docs` | Documentation only |
| `refactor` | Code change with no functional change |
| `test` | Adding or fixing tests |
| `style` | Formatting, linting (no logic change) |
| `perf` | Performance improvement |

Examples:
```
feat(accounts): add multi-factor authentication
fix(billing): handle null tax rate on invoice line items
chore(deps): upgrade django to 6.0.1
```

## 20. Pull Request Checklist

Before requesting review, verify:

- [ ] Code compiles and `make lint` passes with zero warnings
- [ ] `make test` passes (all tests green)
- [ ] New code includes tests covering happy path, error cases, and edge cases
- [ ] Type annotations are complete — `mypy` reports no errors
- [ ] Database migrations are included if models changed
- [ ] Environment variables (new ones) are documented in `.env.example`
- [ ] No secrets, TODOs, debug prints, or commented-out code remain
- [ ] PR title follows Conventional Commits format
- [ ] PR description explains the _what_ and the _why_ (not the _how_)

## 21. Documentation Standards

- **README.md** — Project overview, quick start, feature index, badge row. Updated every release.
- **AGENTS.md** — This file. Engineering manual. Updated when architecture or conventions change.
- **docs/** — ADRs (architecture decision records named `adr-XXX-title.md`), runbooks, infrastructure notes.
- **Docstrings** — Every public module, class, and function has a docstring. Google-style format. Private helpers are encouraged to have one when non-trivial.
- **Inline comments** — Explain _why_ something is done, not _what_ the code does. The code is the what.

## 22. AI Agent Rules

Instructions for AI coding assistants (OpenCode, GPT, Claude, Gemini, and future models):

1. **Read AGENTS.md first** before making changes. This file defines the non-negotiable constraints.
2. **Preserve the folder structure.** Do not move files between `apps/`, `common/`, and `core/` without a compelling architectural reason.
3. **Follow the dependency rule.** `common/` never imports from `apps/`. Services in `common/` operate on primitives and interfaces.
4. **Do not introduce new patterns** that contradict existing code style (single-quote vs double-quote, type annotation style, model layout).
5. **Prefer existing abstractions** over new ones. Put business logic in `common/services/`, not in views or model methods.
6. **Ask for clarification** when requirements are ambiguous. Do not guess URLs, library versions, or team conventions.
7. **Never commit secrets** or generate code that logs, exposes, or hardcodes credentials.
8. **When in doubt, be explicit.** Explicit imports, explicit types, explicit error handling — no magic.
9. **Update documentation** alongside code changes. If a settings key is added, update `.env.example`. If an env var is added, document it.
10. **Respect the testing strategy.** Code changes include corresponding tests. Do not skip testing because the change "looks simple."

## 23. Forbidden Practices

| Practice | Why |
|----------|-----|
| `from django.db.models import *` | Pollutes namespace, hides dependencies |
| `except:` without an exception type | Catches `SystemExit` / `KeyboardInterrupt` |
| Using `print()` in production code | Breaks log aggregation, no structured output |
| Hardcoding secrets, API keys, or passwords | Security violation |
| `null=False, default=""` on CharField | Prefer `blank=True` or nullable |
| Raw SQL without lead architect approval | Breaks database abstraction, hard to migrate |
| Committing `__pycache__/`, `.pyc`, `.DS_Store` | Never. These are in `.gitignore`. |
| Chaining multiple `filter()` calls without understanding QuerySet caching | Accelerates N+1, confusing behaviour |
| Creating a new Django app for fewer than 2 models | Consolidate into an existing app or a `utils` module |
| Bypassing the service layer in views | Business logic must be testable independently of HTTP |
| Using `Faker` in tests without `factory_boy` | Factories compose better, are more maintainable |
| Adding a dependency without updating requirements files | Breaks builds for other developers |

## 24. Definition of Done

A feature, fix, or chore is "done" when:

1. Code is implemented and follows all standards in this document.
2. `make lint` passes with zero warnings.
3. `make test` passes with >90% coverage on new code.
4. Database migrations (if any) are reversible (`migrate <app> <previous_migration>` works).
5. Environment variables (if new) are documented in `.env.example` and the settings module.
6. PR is submitted with a Conventional Commit title and descriptive body.
7. At least one human reviewer has approved the PR.
8. All CI checks pass.
9. Documentation is updated (README, ADRs, or inline docs as relevant).

## 25. Future Roadmap

| Theme | Items |
|-------|-------|
| **Multi-tenancy** | Row-level tenant isolation for SaaS deployments |
| **RBAC / ACL** | Fine-grained role-based and attribute-based access control |
| **Audit logging** | Immutable change tracking for compliance (SOX, LGPD, GDPR) |
| **Async tasks** | Celery integration with Flower monitoring |
| **REST API** | DRF or Django Ninja with OpenAPI/Swagger |
| **GraphQL** | Strawberry or Graphene endpoint |
| **Notifications** | Email, SMS, WebSocket, in-app notification hub |
| **Observability** | Health checks, Sentry, OpenTelemetry tracing |
| **Kubernetes** | Helm chart with readiness/liveness probes |
| **Module apps** | `apps/sgci/`, `apps/crm/`, `apps/erp/`, `apps/finance/`, `apps/hr/` |
| **AI features** | LLM-powered assistants, document intelligence, predictive analytics |

Each item is an app under `backend/apps/` consuming `common/` primitives. The template stays generic; product-specific code lives in the adopting repository.

---

*Maintain this document as the project evolves. Every architecture decision, convention change, or new pattern must be reflected here before code is merged.*

---

## AI Development Workflow

This project follows a structured human-AI engineering pipeline:


This workflow ensures:

- architectural consistency across all modules
- controlled AI-driven development
- reduced technical debt
- predictable system evolution
- clear separation between design, implementation, and approval

