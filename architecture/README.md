# architecture/

## Purpose

Root directory for architecture documentation, decision records, diagrams, models, and review artifacts.

## Allowed Artifact Types

- Markdown documents (`.md`) — ADRs, design notes, review summaries
- Diagram sources (`.drawio`, `.mermaid`, `.puml`) — architecture diagrams
- Model files (`.json`, `.yaml`) — data models, API schemas, domain models
- Image files (`.png`, `.svg`, `.jpg`) — exported diagrams and screenshots

## Prohibited Content

- Source code (`.py`, `.js`, `.ts`) — use `implementation/`
- Compiled or generated artifacts — keep source only
- Sensitive credentials or secrets — use environment variables
- Temporary or draft-only files — use a local branch instead

## Applicable Baseline References

- Architecture Baseline v1.0.0
- AGENTS.md — Architecture & Engineering Principles
- `architecture/decisions/` — Architecture Decision Records
