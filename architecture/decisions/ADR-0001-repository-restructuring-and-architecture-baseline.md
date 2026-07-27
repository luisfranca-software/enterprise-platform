# ADR-0001: Repository Restructuring and Architecture Baseline

## Status

Accepted

## Date

2026-07-25

## Context

The `template-web-enterprise` repository was created as a Django starter template with a flat directory structure. As the project matures into a multi-product enterprise platform (SGCI, CRM, ERP, Finance, HR), the repository structure must evolve to support:

- Formal architecture governance with baseline specifications
- Clear separation between implementation code, architecture documentation, and test suites
- A scalable directory layout that accommodates multiple bounded contexts
- Compliance with Specification-First and Architecture-Before-Code policies
- Traceable architecture decisions via Architecture Decision Records

The existing structure placed `backend/` and `frontend/` at the repository root alongside infrastructure files, with no dedicated directories for architecture documentation, cross-cutting test suites, or developer tooling.

## Decision

Restructure the repository from a flat Django template layout into the `enterprise-platform` structure and establish Architecture Baseline v1.0.0 with 23 approved specification documents.

## Target Structure

```
enterprise-platform/
├── architecture/
│   ├── decisions/          # Architecture Decision Records (ADRs)
│   ├── diagrams/           # System and component diagrams
│   ├── models/             # Domain models and data schemas
│   └── reviews/            # Architecture review artifacts
├── implementation/
│   ├── backend/            # Django application (Python 3.12+)
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
├── docker-compose.yml      # Multi-container orchestration
├── LICENSE                 # Proprietary licence
├── Makefile                # Standardised developer commands
└── README.md               # Project overview with governance workflow
```

## Migration Strategy

1. **Branch** — Create `chore/architecture-baseline-v1` from `main`
2. **Directories** — Create all target directories with scoped README files
3. **Application migration** — `git mv backend implementation/backend`, `git mv frontend implementation/frontend`
4. **Reference updates** — Update `.gitignore`, `AGENTS.md`, `base.py` comments, and workstation docs
5. **Documentation** — Replace `README.md` with governance-complete version; replace `LICENSE` with proprietary licence
6. **ADR** — Create this decision record
7. **Cleanup** — Remove tracked backup files (`.backup/`, `base.py.save`)
8. **Baseline documents** — Copy 23 approved specification documents to `docs/01-EPRD.md` through `docs/23-DGEH.md`
9. **Manifest** — Generate SHA-256 checksum manifest for baseline documents
10. **Validation** — Verify all references, run Django checks, validate Docker config
11. **Commit** — Single commit with all changes
12. **Tag** — Annotated tag `architecture-baseline-v1.0.0`

Git history is preserved using `git mv` for all file moves. No functional code is modified during this restructuring.

## Consequences

- All source code now lives under `implementation/`, clearly separating implementation from architecture and testing
- Architecture documentation has a dedicated home with a clear decision record process
- Cross-cutting tests are separated from application-specific tests
- The repository structure supports future multi-product development without further restructuring
- All existing development workflows remain functional after path reference updates
- The 23 baseline documents establish the non-negotiable architectural constraints for all future development

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Broken path references in CI/CD | Low | Medium | Comprehensive grep search for old paths; manual review of all config files |
| External documentation links break | Medium | Low | Document the restructuring in ADR; update all internal references |
| Developer muscle memory disruption | Medium | Low | Clear communication; updated README with new paths |
| Missing baseline documents delay implementation | Low | High | Documents are approved and will be provided by Product Owner before implementation begins |

## Rollback Strategy

If the restructuring causes critical issues:

1. Abort the migration branch: `git switch main`
2. Delete the migration branch: `git branch -D chore/architecture-baseline-v1`
3. The `main` branch remains untouched throughout the operation
4. No push is performed until explicit approval, so remote is unaffected

## References

- Architecture Baseline v1.0.0 — 23 specification documents in `docs/`
- AGENTS.md — Engineering manual for AI agents and human developers
- README.md — Project overview with governance workflow and repository structure
