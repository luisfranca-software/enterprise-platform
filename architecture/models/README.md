# architecture/models/

## Purpose

Contains domain model definitions, data schemas, API contracts, and entity relationship diagrams that define the system's conceptual architecture.

## Allowed Artifact Types

- Model definition files (`.json`, `.yaml`, `.graphql`)
- Schema files (`.schema`, `.proto`, `.avro`)
- Entity relationship diagrams (`.puml`, `.mermaid`, `.drawio`)
- Model documentation (`.md`)

## Prohibited Content

- Implementation code (use `implementation/backend/apps/`)
- Database migration files (use `implementation/backend/apps/*/migrations/`)
- Sensitive credentials or secrets
- Generated ORM code

## Applicable Baseline References

- Architecture Baseline v1.0.0
- AGENTS.md — Domain Layer specifications
