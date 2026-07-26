# Enterprise Platform

**Enterprise-grade platform architecture and implementation portfolio demonstrating specification-driven development, security, testing, DevOps, observability and software governance.**

---

| | |
|---|---|
| **Architecture Baseline** | v1.0.0 |
| **Status** | Approved |
| **Date** | 2026-07-25 |
| **Reference** | Architecture Baseline v1.0 |
| **Repository Visibility** | Public |
| **Source Model** | Proprietary Source-Available |
| **Open-Source Status** | No |
| **Primary Purpose** | Professional Portfolio and Technical Evaluation |

---

## License and Permitted Use

This repository is publicly accessible for professional portfolio review,
technical evaluation, recruitment assessment and demonstration of
engineering capabilities.

Public access does not make this project open source.

Unless expressly authorized in writing by the copyright owner, no
permission is granted to use, copy, reproduce, modify, distribute,
sublicense, sell, commercialize or create derivative works from this
repository or any of its contents.

See the [LICENSE](LICENSE) file for the complete terms.

---

## About

This repository presents a complete enterprise software architecture built
on Django, PostgreSQL, Redis, and Docker. It demonstrates a governance-first
approach to software engineering where specifications are authored and
approved before any implementation begins.

The platform is designed as the foundation for business-critical systems
including ERP, CRM, SGCI (grant management), Finance, and HR platforms.

---

## Architecture Baseline

Architecture Baseline v1.0.0 establishes the non-negotiable architectural
constraints for the platform. All implementation must conform to these
specifications.

| | |
|---|---|
| **Baseline Version** | v1.0.0 |
| **Specification Count** | 23 documents |
| **Approval Date** | 2026-07-25 |
| **Location** | `docs/` directory |

---

## Governance Model

```
Business Vision
       │
       ▼
Human
(Product Owner)
       │
       ▼
Product Architect
(System Architecture)
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
Local Version Control
(OpenCode + Git)
       │
       ▼
Human Technical Review
       │
       ▼
Human Release Approval
       │
       ▼
GitHub Repository
       │
       ▼
CI/CD
       │
       ▼
Production
```

### Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Human (Product Owner)** | Product vision, requirements, final release approval |
| **Product Architect** | System architecture, technical design authority |
| **Architecture & Engineering Review (ChatGPT)** | Architecture review, engineering standards, technical decisions |
| **Implementation (OpenCode)** | Source code implementation, project file modifications, local version control |
| **Human Technical Review** | Code review, quality assurance, architectural compliance |
| **Human Release Approval** | Final validation before publishing to GitHub |
| **GitHub** | Remote repository, collaboration, CI/CD pipelines |
| **CI/CD** | Automated testing, building, deployment |

### Human Approval Gates

| Gate | Required Before | Approver |
|------|----------------|----------|
| Specification approval | Implementation begins | Product Owner |
| Architecture review | Code merge to develop | Product Architect |
| Code review | Merge to main | Human Developer |
| Release approval | Production deploy | Product Owner |
| Security review | External release | Security Lead |

### Policies

- **Specification-First** — All implementation begins with an approved specification
- **Architecture-Before-Code** — Architecture decisions precede implementation

---

## Technology Stack

| Category | Choice | Rationale |
|----------|--------|-----------|
| **Runtime** | Python 3.12+ | Modern, typed, async-ready |
| **Framework** | Django 6 | Mature, batteries-included, strong ORM |
| **Database** | PostgreSQL 16 | ACID compliance, JSONB, robust extensions |
| **Cache** | Redis 7 | Sub-millisecond latency, Celery broker |
| **Reverse Proxy** | Nginx | High-performance static serving, TLS |
| **Containerisation** | Docker + Compose | Reproducible environments, production parity |
| **CI/CD** | GitHub Actions | Tight integration, matrix builds, caching |
| **AI Assistant** | OpenCode | Team-consistent agent conventions |
| **Config** | django-environ | 12-factor app compliance |

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

---

## Repository Structure

```
enterprise-platform/
├── architecture/
│   ├── decisions/          # Architecture Decision Records (ADRs)
│   ├── diagrams/           # System and component diagrams
│   ├── models/             # Domain models and data schemas
│   └── reviews/            # Architecture review artifacts
├── implementation/
│   ├── backend/            # Django application (Python 3.12+)
│   │   ├── apps/           #   Domain-specific Django apps
│   │   ├── common/         #   Shared enterprise primitives
│   │   ├── core/           #   Django project root (settings, URLs, WSGI/ASGI)
│   │   ├── requirements/   #   Split dependency files
│   │   └── tests/          #   Project-wide integration tests
│   └── frontend/           # Frontend application (framework TBD)
├── tests/
│   ├── architecture/       # Architecture compliance tests
│   ├── contract/           # API contract tests
│   ├── end_to_end/         # E2E user-journey tests
│   ├── performance/        # Load and stress tests
│   └── security/           # Security scanning tests
├── docker/                 # Docker service configurations
├── docs/                   # Documentation (23 baseline specs, workstation guides)
├── scripts/                # Automation and utility scripts
├── tools/                  # Developer tooling and helpers
├── AGENTS.md               # AI agent engineering manual
├── CONTRIBUTING.md         # Contribution policy
├── SECURITY.md             # Security policy
├── docker-compose.yml      # Multi-container orchestration
├── LICENSE                 # Proprietary licence
├── Makefile                # Standardised developer commands
└── README.md               # This file
```

---

## Engineering Standards

### Code Quality

| Tool | Purpose |
|------|---------|
| **ruff** | Linting and formatting |
| **mypy** | Static type checking |
| **pytest** | Unit and integration testing |
| **pre-commit** | Git hook automation |

### Testing Strategy

| Layer | Tool | Scope |
|-------|------|-------|
| Unit | pytest + factory_boy | Models, services, helpers, permissions |
| Integration | pytest + factory_boy | API endpoints, middleware, database queries |
| E2E | Playwright / Selenium | Critical user journeys |
| Architecture | Custom | Compliance with baseline constraints |

### Security Approach

- `DEBUG` is never `True` in production
- `SECRET_KEY` is rotated per environment and never committed
- `ALLOWED_HOSTS` is restricted to known domains
- All passwords hashed via Django's PBKDF2 hasher
- Session cookies: HTTPOnly, Secure, SameSite=Lax
- CSRF protection enabled globally
- API rate limiting at Nginx or middleware layer
- File uploads validated by type and size
- SQL injection prevented via Django ORM parameterised queries
- Full security policy in [SECURITY.md](SECURITY.md)

### CI/CD Approach

GitHub Actions workflows for linting, testing, building, and deployment.
Every merge to `develop` or `main` triggers automated validation.

### Observability Approach

Structured JSON logging in production, Sentry for error tracking,
health-check endpoints for readiness and liveness probes.

---

## Document Hierarchy

The 23 Architecture Baseline documents define the complete platform specification:

| # | Document | Purpose |
|---|----------|---------|
| 01 | EPRD | Enterprise Product Requirements Document |
| 02 | TIP | Technology Implementation Plan |
| 03 | SDD | System Design Document |
| 04 | BIS | Business Intelligence Specification |
| 05 | FIS | Financial Information Specification |
| 06 | DDS | Data Design Specification |
| 07 | AIPS | API Integration Specification |
| 08 | AIAS | AI Architecture Specification |
| 09 | KMS | Knowledge Management Specification |
| 10 | RKS | Reporting and KPI Specification |
| 11 | TCS | Technical Compliance Specification |
| 12 | WOS | Workflow Orchestration Specification |
| 13 | EAS | Enterprise Architecture Specification |
| 14 | EDC | Enterprise Data Classification |
| 15 | ESAS | Enterprise Security and Access Specification |
| 16 | IAS | Infrastructure Architecture Specification |
| 17 | DCS | Deployment and Configuration Specification |
| 18 | MOS | Monitoring and Observability Specification |
| 19 | ETSS | Enterprise Testing Strategy Specification |
| 20 | DES | Documentation and Education Specification |
| 21 | ORS | Operations and Reliability Specification |
| 22 | BCDRS | Business Continuity and Disaster Recovery Specification |
| 23 | DGEH | Development Governance and Ethics Handbook |

---

## Implementation Status

**Active Development** — Architecture Baseline v1.0.0 established.
Core architecture is stabilised and foundational modules are being implemented.

| Component | Status |
|-----------|--------|
| Repository structure | Complete |
| Architecture baseline | Approved (v1.0.0) |
| Django scaffold | Implemented |
| Accounts app | Scaffolded |
| Settings module | Configured (base, development, testing, production) |
| Docker Compose | Configured |
| CI/CD | Planned |
| Frontend | Planned |

---

## Roadmap

- Multi-tenancy — row-level tenant isolation for SaaS deployments
- RBAC / ACL — fine-grained role-based and attribute-based access control
- Audit logging — immutable change tracking for compliance
- Celery integration — async task queue with Flower monitoring
- REST API — DRF or Django Ninja with OpenAPI documentation
- GraphQL endpoint — Strawberry or Graphene
- Notification system — email, SMS, WebSocket, in-app
- Health checks — readiness/liveness probes for Kubernetes
- Sentry integration — error tracking and performance monitoring
- Helm chart — Kubernetes deployment manifests

---

## Contact

[PROFESSIONAL PROFILE OR CONTACT PLACEHOLDER TO BE DEFINED]

---

## References

- **AGENTS.md** — Engineering manual for AI agents and human developers
- **CONTRIBUTING.md** — Contribution policy
- **SECURITY.md** — Security policy and vulnerability reporting
- **LICENSE** — Proprietary software licence
- **Architecture Baseline v1.0.0** — 23 specification documents in `docs/`
- **ADR-0001** — Repository restructuring and architecture baseline decision record
