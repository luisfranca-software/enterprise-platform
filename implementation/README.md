# implementation/

## Purpose

Contains all application source code for the enterprise platform, organized by layer (backend and frontend).

## Directory Structure

```
implementation/
├── backend/          # Django application (Python 3.12+)
│   ├── apps/         #   Domain-specific Django apps (one per bounded context)
│   ├── common/       #   Shared enterprise primitives (services, middleware, permissions)
│   ├── core/         #   Django project root (settings, URLs, WSGI/ASGI)
│   ├── requirements/ #   Split dependency files (base, dev, prod)
│   └── tests/        #   Project-wide integration tests
└── frontend/         # Frontend application (framework TBD)
```

## Allowed Artifact Types

- Python source code (`.py`) — backend implementation
- JavaScript/TypeScript source code (`.js`, `.ts`, `.tsx`, `.jsx`) — frontend implementation
- HTML templates (`.html`)
- CSS/SCSS stylesheets (`.css`, `.scss`)
- Configuration files (`pyproject.toml`, `package.json`, etc.)
- Database migrations (`*/migrations/*.py`)

## Prohibited Content

- Architecture decision records (use `architecture/decisions/`)
- Infrastructure configuration (use `docker/`, root-level files)
- Sensitive credentials or secrets — use environment variables
- Compiled or generated artifacts (`.pyc`, `node_modules/`, `dist/`)

## Applicable Baseline References

- Architecture Baseline v1.0.0
- AGENTS.md — Folder Responsibilities, App Organization, Coding Standards
