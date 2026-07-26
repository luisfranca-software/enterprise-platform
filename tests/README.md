# tests/

## Purpose

Project-wide test suites organized by test category. Application-specific unit and integration tests live alongside their source code in `implementation/backend/apps/*/tests/`.

## Directory Structure

```
tests/
├── architecture/     # Architecture compliance and constraint tests
├── contract/         # API contract and schema validation tests
├── end_to_end/       # Full user-journey E2E tests (Playwright/Selenium)
├── performance/      # Load testing, stress testing, benchmarks
└── security/         # Security scanning, penetration test helpers
```

## Allowed Artifact Types

- Python test files (`test_*.py`, `conftest.py`)
- Test configuration (`pytest.ini`, `conftest.py`)
- Test fixtures and factories (`factories.py`, `fixtures/`)
- E2E test scripts (`.spec.ts`, `.spec.js`)

## Prohibited Content

- Application source code (use `implementation/`)
- Architecture decision records (use `architecture/decisions/`)
- Sensitive credentials or secrets
- Test data containing real PII

## Applicable Baseline References

- Architecture Baseline v1.0.0
- AGENTS.md — Testing Strategy, PR Checklist
