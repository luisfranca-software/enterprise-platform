<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Django-6-092E20?style=for-the-badge&logo=django">
  <img alt="Django 6" src="https://img.shields.io/badge/Django-6-092E20?style=for-the-badge&logo=django">
</picture>

# template-web-enterprise

**Enterprise-grade Django template for building scalable web systems — ERP, CRM, SGCI, Finance, and HR platforms.**

A production-ready foundation that enforces clean architecture, environment-based configuration, containerised development, and CI/CD automation so your team can ship business-critical applications from day one.

---

## Badges

[![CI](https://img.shields.io/badge/CI-passing-3FB950?style=flat-square&logo=github-actions&logoColor=white)](https://github.com/your-org/template-web-enterprise/actions)
[![Coverage](https://img.shields.io/badge/Coverage-90%25-3FB950?style=flat-square&logo=codecov&logoColor=white)](https://codecov.io)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6-092E20?style=flat-square&logo=django)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=flat-square&logo=redis&logoColor=white)](https://redis.io)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-26.04-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://ubuntu.com)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![code style: ruff](https://img.shields.io/badge/code_style-ruff-261230?style=flat-square)](https://docs.astral.sh/ruff)

---

## Table of Contents

- [Why this template?](#why-this-template)
- [Project Philosophy](#project-philosophy)
- [Development Environment](#development-environment)
- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Technology Stack](#technology-stack)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Quick Start with Docker](#quick-start-with-docker)
  - [Local Development (without Docker)](#local-development-without-docker)
  - [Environment Variables](#environment-variables)
- [Development Workflow](#development-workflow)
  - [Makefile Commands](#makefile-commands)
  - [Code Quality](#code-quality)
  - [Testing Strategy](#testing-strategy)
  - [Branch Strategy](#branch-strategy)
- [Docker](#docker)
- [Deployment](#deployment)
- [Future Modules](#future-modules)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
  - [Commit Conventions](#commit-conventions)
- [Support](#support)
- [License](#license)

---

## Why this template?

Building enterprise web applications from scratch means solving the same hard problems every time: multi-environment configuration, container orchestration, background job processing, async communication, clean separation of concerns, and CI/CD pipelines.

**template-web-enterprise** distills years of Django production experience into a single, opinionated starter that gives you:

- A **battle-tested folder layout** that scales from a single module to dozens of domain apps.
- **Environment isolation** that prevents "works on my machine" — every environment gets its own settings, requirements, and env file.
- **Containerised everything** — Django, PostgreSQL, Redis, Nginx, and workers all defined in a single `docker-compose.yml`.
- **CI/CD out of the box** — GitHub Actions workflows for linting, testing, building, and deploying.
- **Team-wide consistency** — Makefile targets, pre-commit hooks, and OpenCode AI conventions (`AGENTS.md`) keep every developer on the same page.

Use this template when you need to build a **business-critical web system** and want to skip the boilerplate without sacrificing quality.

---

## Project Philosophy

1. **Convention over configuration.** Opinions are baked in — modular apps, env-based settings, split requirements — so you spend time on business logic, not infrastructure decisions.
2. **Production parity.** If it runs in Docker locally, it runs the same way in staging and production. No surprises.
3. **12-Factor App compliance.** Configuration is extracted from code via environment variables. Every deploy is a repeatable, immutable operation.
4. **Defence in depth.** Clean architecture layers (service layer, middleware, permissions, exceptions) enforce separation of concerns and make the codebase auditable.
5. **Developer experience first.** One command (`make up`) starts the entire stack. Linting, formatting, and type-checking run automatically. The feedback loop is measured in seconds, not minutes.

---

## Development Environment

| Component | Version / Tool |
|-----------|---------------|
| **Operating System** | Ubuntu 26.04 LTS |
| **Runtime** | Python 3.14 |
| **Virtual Environment** | `venv` (built-in) |
| **Containerisation** | Docker |
| **Version Control** | Git + GitHub CLI (`gh`) |
| **AI Assistant** | OpenCode |
| **Editor** | VS Code |

---

## Features

- **Python 3.14 + Django 6** — modern, typed, and async-ready
- **Modular app structure** — `apps/` for domain modules, `common/` for shared primitives
- **Multi-environment settings** — `base.py` → `development.py` / `testing.py` / `production.py`
- **Split requirements** — `base.txt`, `dev.txt`, `prod.txt` with zero noise in production
- **Docker Compose orchestration** — Django, PostgreSQL, Redis, Nginx, and background workers
- **Environment-first configuration** — `.env.dev`, `.env.prod`, `.env.test` with `.env.example`
- **Automated CI/CD** — GitHub Actions workflows (lint, test, build, deploy)
- **WSL2 + Ubuntu 26.04** — optimised for Windows development with Linux parity
- **OpenCode AI integration** — team-wide agent conventions via `AGENTS.md`
- **Makefile automation** — common commands standardised for the whole team

---

## Architecture Overview

```
┌────────────────────────────────────────────────────┐
│                     Client                          │
└────────────┬───────────────────────────────────────┘
             │ HTTPS
┌────────────▼──────────────────────────────────────┐
│                   Nginx (reverse proxy)            │
└──┬────────────────────┬───────────────────────────┘
   │  /api              │  /ws
┌──▼────────────────┐ ┌─▼────────────────────────────┐
│  Django (Gunicorn) │ │  Django ASGI (Channels/Daphne)│
│  WSGI App Server   │ │  WebSocket / Async workers   │
└──┬─────────────────┘ └──┬──────────────────────────┘
   │                       │
┌──▼───────────────────────▼────────────────────────┐
│                  Redis (cache + broker)            │
└──┬───────────────────────┬────────────────────────┘
   │                       │
┌──▼───────────────────────▼────────────────────────┐
│                  PostgreSQL (primary DB)            │
└────────────────────────────────────────────────────┘
```

| Layer | Technology | Role |
|-------|-----------|------|
| **Reverse proxy** | Nginx | TLS termination, static files, load balancing |
| **Application** | Django 6 + Gunicorn | HTTP API, business logic, ORM |
| **Async** | Django ASGI / Channels | WebSockets, real-time events |
| **Cache & broker** | Redis | Session store, Celery broker, rate limiting |
| **Database** | PostgreSQL 16 | Relational persistence, JSONB, full-text search |
| **Workers** | Celery / Huey | Background jobs, scheduled tasks, email |

---

## Technology Stack

| Category | Choice | Rationale |
|----------|--------|-----------|
| **Runtime** | Python 3.14 | Pattern matching, improved types, faster CPython |
| **Framework** | Django 6 | Mature, batteries-included, strong ORM |
| **Database** | PostgreSQL 16 | ACID compliance, JSONB, robust extension ecosystem |
| **Cache** | Redis | Sub-millisecond latency, pub/sub, Celery broker |
| **Reverse proxy** | Nginx | High-performance static serving, TLS, load balancing |
| **Containerisation** | Docker + Compose | Reproducible environments, local ↔ production parity |
| **OS** | Ubuntu 26.04 LTS | Long-term support, Docker-native, WSL2 compatible |
| **Workflow** | WSL2 | Seamless Windows ↔ Linux development |
| **CI/CD** | GitHub Actions | Tight GitHub integration, matrix builds, caching |
| **AI assistant** | OpenCode | Team-consistent agent conventions via `AGENTS.md` |
| **Config** | django-environ | 12-factor app compliance, env var separation |

---

## Folder Structure

```
template-web-enterprise/
├── backend/
│   ├── apps/                  # Domain applications (one per bounded context)
│   │   └── accounts/          #   Authentication & user management
│   ├── common/                # Shared enterprise primitives
│   │   ├── constants/         #   Application-wide constants
│   │   ├── exceptions/        #   Custom exception hierarchy
│   │   ├── helpers/           #   Utility functions
│   │   ├── middleware/        #   Request/response middleware
│   │   ├── mixins/            #   Reusable class-based view mixins
│   │   ├── permissions/       #   Authorization & access control
│   │   ├── services/          #   Business logic service layer
│   │   └── utils/             #   General utilities
│   ├── config/                # App configuration modules
│   ├── core/                  # Django project root
│   │   ├── settings/          #   Environment-specific settings
│   │   │   ├── base.py        #     Shared settings (inherited by all)
│   │   │   ├── development.py
│   │   │   ├── production.py
│   │   │   └── testing.py
│   │   ├── urls.py            #   Root URL configuration
│   │   ├── wsgi.py            #   WSGI entrypoint (Gunicorn)
│   │   └── asgi.py            #   ASGI entrypoint (Channels/Daphne)
│   ├── requirements/          # Split dependency files
│   │   ├── base.txt           #   Shared dependencies
│   │   ├── dev.txt            #   Development-only (includes base)
│   │   └── prod.txt           #   Production-only (includes base)
│   ├── static/                # Static assets (CSS, JS, images)
│   ├── media/                 # User-uploaded files
│   ├── logs/                  # Application logs (gitignored)
│   ├── tests/                 # Project-wide test suite
│   └── manage.py              # Django management script
├── docker/                    # Docker service configurations
│   ├── django/                #   Django app image (Dockerfile + entrypoint)
│   ├── nginx/                 #   Nginx config (site conf, SSL templates)
│   ├── postgres/              #   PostgreSQL init scripts & custom config
│   ├── redis/                 #   Redis configuration
│   └── workers/               #   Background worker image (Celery/Huey)
├── docs/                      # Architecture & developer documentation
├── env/                       # Environment variable files
│   ├── .env.dev               #   Development environment
│   ├── .env.prod              #   Production environment
│   └── .env.test              #   Testing environment
├── frontend/                  # Frontend application scaffold
├── scripts/                   # Automation & utility scripts
├── .github/
│   └── workflows/             # GitHub Actions CI/CD pipelines
├── .env.example               # Reference environment file (documented)
├── .gitignore
├── AGENTS.md                  # OpenCode AI agent instructions
├── docker-compose.yml         # Multi-container orchestration
├── Makefile                   # Standardised developer commands
└── README.md
```

### Key directories explained

| Directory | Purpose |
|-----------|---------|
| `backend/apps/` | Domain applications — add one sub-package per business domain (e.g., `inventory`, `billing`, `notifications`). |
| `backend/common/` | Shared primitives reused across all apps — never import from `apps/*` here. |
| `backend/core/settings/` | Split settings module — `base.py` is the foundation; each environment file overrides only what differs. |
| `docker/` | Per-service Docker assets — keeps Dockerfiles and configs out of the project root. |
| `env/` | Environment variable files, one per environment — never committed with real secrets. |

---

## Installation

### Prerequisites

| Tool | Version | Notes |
|------|---------|-------|
| Python | 3.14+ | Required for local (non-Docker) development |
| Docker | 24+ | Required for containerised development |
| Docker Compose | v2 | Bundled with Docker Desktop / Docker Engine |
| PostgreSQL | 16 | Only needed when running Django without Docker |
| Redis | 7+ | Only needed when running Django without Docker |
| Make | 4+ | Optional — simplifies command execution |

> **Recommendation:** Use Docker for day-to-day development. It guarantees environment parity and eliminates the need to install PostgreSQL, Redis, or system-level dependencies on your host.

### Quick Start with Docker

```bash
# 1. Clone the repository
git clone https://github.com/your-org/template-web-enterprise.git
cd template-web-enterprise

# 2. Copy environment file (development)
cp env/.env.dev .env

# 3. Build and start all services
make up
# or: docker compose up --build

# 4. Apply database migrations
make migrate
# or: docker compose exec django python manage.py migrate

# 5. Create a superuser
make superuser
# or: docker compose exec django python manage.py createsuperuser

# 6. Open the application
open http://localhost:8000
```

### Local Development (without Docker)

```bash
# 1. Create and activate a virtual environment
python3.14 -m venv .venv
source .venv/bin/activate

# 2. Install development dependencies
pip install -r backend/requirements/dev.txt

# 3. Configure environment
cp env/.env.dev .env
# Edit .env to match your local PostgreSQL / Redis credentials

# 4. Run migrations
python backend/manage.py migrate

# 5. Start the development server
python backend/manage.py runserver
```

### Environment Variables

This project follows the [12-Factor App](https://12factor.net/config) methodology. All configuration is driven by environment variables loaded from a `.env` file.

| File | Purpose |
|------|---------|
| `.env.example` | Documented reference with placeholder values — safe to commit |
| `env/.env.dev` | Development overrides (debug on, SQLite or local PG, etc.) |
| `env/.env.prod` | Production overrides (debug off, PG, Redis, secret key, etc.) |
| `env/.env.test` | Testing overrides (in-memory DB, disabled migrations, etc.) |

**Important:** Copy the relevant file to `.env` at the project root. Never commit `.env` or the `env/` files with real secrets. Use your secret manager (e.g., GitHub Secrets, Vault) to inject values at deploy time.

Key variables you will typically find in these files:

| Variable | Description |
|----------|-------------|
| `DJANGO_SETTINGS_MODULE` | Which settings file to use (`core.settings.development`, etc.) |
| `DATABASE_URL` | PostgreSQL connection string |
| `REDIS_URL` | Redis connection string |
| `SECRET_KEY` | Django secret key (rotate per environment) |
| `DEBUG` | Boolean — must be `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed domain names |

---

## Development Workflow

### Makefile Commands

| Command | Description |
|---------|-------------|
| `make up` | Start all Docker services |
| `make down` | Stop all Docker services |
| `make build` | Rebuild Docker images |
| `make shell` | Open Django shell in the container |
| `make dbshell` | Open PostgreSQL shell |
| `make migrate` | Run database migrations |
| `make migrations` | Create new migrations |
| `make superuser` | Create a Django admin superuser |
| `make test` | Run the test suite |
| `make lint` | Run ruff / flake8 / mypy |
| `make format` | Format code with ruff |
| `make requirements` | Compile `requirements/*.txt` |
| `make logs` | Tail container logs |

### Code Quality

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **ruff** (linter) | Fast Python linting with 800+ rules | `pyproject.toml` |
| **ruff** (formatter) | Zero-config opinionated code formatter | `pyproject.toml` |
| **mypy** | Gradual static type checking | `pyproject.toml` |
| **pre-commit** | Git hook automation — runs lint + format before every commit | `.pre-commit-config.yaml` |

Run all checks at once:

```bash
make lint        # ruff check + mypy
make format      # auto-format with ruff
```

Pre-commit hooks are installed automatically on first `git commit` if `pre-commit` is configured. To install manually:

```bash
pre-commit install
```

### Testing Strategy

| Layer | Tool / Approach | Scope |
|-------|-----------------|-------|
| **Unit tests** | `pytest` + `pytest-django` | Models, services, helpers, permissions |
| **Integration tests** | `pytest` + `factory_boy` | API endpoints, middleware, database queries |
| **End-to-end tests** | Selenium / Playwright (optional) | Critical user journeys |
| **Coverage** | `pytest-cov` | Minimum threshold: 90% |

Run the full suite:

```bash
make test
# or: docker compose exec django pytest
```

Generate a coverage report:

```bash
pytest --cov=backend --cov-report=html
open htmlcov/index.html
```

### Branch Strategy

```
main          ─── production-ready, protected
  ├── develop ─── integration branch
  │     ├── feature/*  ─── new features
  │     ├── fix/*      ─── bug fixes
  │     └── chore/*    ─── maintenance
  └── release/* ─── release candidates
```

1. Create a feature/fix/chore branch from `develop`.
2. Open a Pull Request against `develop`.
3. After review and CI passes, squash-merge into `develop`.
4. When ready for release, open a PR from `develop` into `main` or create a `release/*` branch.

---

## AI-Assisted Software Engineering Workflow

Human defines the product vision and approves every release. ChatGPT is responsible for architecture, engineering review and technical guidance. OpenCode implements the approved architecture and performs local versioning (Git add and local commit). Human decides when changes are released, and GitHub serves as the official shared repository.

```
Human
   │
   ▼
Architecture & Engineering Review
(ChatGPT)
   │
   ▼
Implementation
(OpenCode)
   │
   ▼
Local Versioning
(OpenCode)
   │
   ▼
Human Release Approval
   │
   ▼
GitHub
```

| Stage | Responsibility |
|-------|---------------|
| Human | Product vision, requirements, final release approval |
| Architecture & Engineering Review (ChatGPT) | Architecture, engineering review, technical decisions |
| Implementation (OpenCode) | Source code implementation and project file modifications |
| Local Versioning (OpenCode) | Local Git staging and commit creation |
| Human Release Approval | Final validation before publishing |
| GitHub | Remote repository, collaboration and CI/CD |

---

## Docker

The project uses a multi-service Docker Compose setup that mirrors a production topology.

```bash
# Start all services (detached)
make up

# View logs
make logs

# Rebuild images after dependency changes
make build

# Stop everything
make down
```

### Services

| Service | Image Base | Exposed Port | Purpose |
|---------|-----------|--------------|---------|
| `django` | `python:3.14-slim` | `8000` | Gunicorn WSGI server + ASGI |
| `nginx` | `nginx:alpine` | `80`, `443` | Reverse proxy, static/media serving |
| `postgres` | `postgres:16-alpine` | `5432` | Primary relational database |
| `redis` | `redis:7-alpine` | `6379` | Cache, session store, Celery broker |
| `workers` | `python:3.14-slim` | — | Celery / Huey background task workers |

Volumes are used for:
- **PostgreSQL data** — survives container restarts
- **Static / media files** — shared between Django and Nginx
- **Application code** — mounted as a bind volume for hot-reload in development

> **Production note:** Replace bind mounts with explicit COPY in the Dockerfile. Use a container registry (Docker Hub, ECR, GCR) for immutable image deploys.

---

## Deployment

### CI/CD Pipeline (GitHub Actions)

The repository includes pre-configured workflows under `.github/workflows/`:

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Lint** | PR + push to `develop`, `main` | ruff check, mypy |
| **Test** | PR + push to `develop`, `main` | pytest, coverage report |
| **Build** | Push to `main` | Docker image build & push to registry |
| **Deploy** | Release published | Deploy to staging / production |

### Production Checklist

Before going live, ensure:

- [ ] `DEBUG=False` in production settings
- [ ] `SECRET_KEY` rotated and injected via environment / secret manager
- [ ] `ALLOWED_HOSTS` restricted to known domains
- [ ] Database migrations tested against a staging database
- [ ] Static files collected and served via Nginx or CDN
- [ ] HTTPS configured (Nginx + Let's Encrypt / cloud LB)
- [ ] Health-check endpoints configured (readiness + liveness)
- [ ] Sentry or similar error tracking integrated
- [ ] Database backups automated
- [ ] Resource limits set in `docker-compose.yml` or orchestrator

---

## Future Modules

This template is designed to be the foundation for a suite of enterprise business systems. The modular app structure and shared primitives in `backend/common/` make it straightforward to add new domains without rewiring the entire application.

| Module | Domain | Description |
|--------|--------|-------------|
| **SGCI** | Science & Research | Grant lifecycle management, compliance tracking, peer review workflows |
| **CRM** | Customer Relations | Contact management, pipeline tracking, sales analytics, communication logs |
| **ERP** | Enterprise Resources | Inventory, procurement, order management, supply chain, MRP |
| **Finance** | Accounting & Treasury | General ledger, accounts payable/receivable, invoicing, reconciliation |
| **HR** | Human Resources | Employee records, payroll, time tracking, leave management, onboarding |

Each module lives as a self-contained Django app under `backend/apps/`, following the same conventions established by the `accounts` app. Shared concerns (auth, permissions, audit logging, notifications) are provided by the `common/` layer and are ready to be consumed out of the box.

---

## Roadmap

- [ ] **Multi-tenancy** — row-level tenant isolation for SaaS deployments
- [ ] **RBAC / ACL** — fine-grained role-based and attribute-based access control
- [ ] **Audit logging** — immutable change tracking for compliance (SOX, LGPD, GDPR)
- [ ] **Celery integration** — async task queue with Flower monitoring
- [ ] **REST API** — DRF or Django Ninja with OpenAPI/Swagger documentation
- [ ] **GraphQL endpoint** — Strawberry or Graphene for flexible data queries
- [ ] **Notification system** — email, SMS, WebSocket, and in-app notifications
- [ ] **Health checks** — readiness/liveness probes for Kubernetes deployment
- [ ] **Sentry integration** — error tracking and performance monitoring
- [ ] **Helm chart** — Kubernetes deployment manifests

---

## Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'feat: add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. Open a **Pull Request**

### Commit Conventions

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

```
feat:     new feature
fix:      bug fix
chore:    maintenance (deps, config, tooling)
docs:     documentation changes
refactor: code restructuring without feature changes
test:     adding or fixing tests
```

---

## Support

- **Documentation** — See the `docs/` directory for architecture decisions, ADRs, and runbooks.
- **Issues** — Report bugs and request features via [GitHub Issues](https://github.com/Lu-Fran/template-web-enterprise/issues).
- **Discussions** — Use GitHub Discussions for questions, ideas, and community support.
- **Security** — For security vulnerabilities, email the maintainers directly (do not open a public issue).

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Project Status

🚧 **Active Development**

This project is currently under active development. Core architecture is being stabilized and foundational modules are being implemented.

