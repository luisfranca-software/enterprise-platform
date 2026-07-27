# GitHub Repository Governance

This document defines the required GitHub protection configuration,
repository settings, and governance policies for the Enterprise Platform
repository when published as a public proprietary repository.

**Date:** 2026-07-25
**Status:** Recommendations — to be applied by the Human Product Owner

---

## Repository Settings

### General

| Setting | Value |
|---------|-------|
| **Repository name** | `enterprise-platform` |
| **Description** | Enterprise-grade platform architecture and implementation portfolio demonstrating specification-driven development, security, testing, DevOps, observability and software governance. |
| **Website** | [TO BE DEFINED] |
| **Default branch** | `main` |
| **Visibility** | Public |
| **Features: Issues** | Enabled |
| **Features: Projects** | Enabled |
| **Features: Wiki** | Disabled (documentation lives in `docs/`) |
| **Features: Discussions** | Disabled (until community policy is defined) |
| **Features: Sponsorships** | Disabled |
| **Features: Pages** | Disabled (until needed) |

### Topics

```
python
django
enterprise-architecture
software-architecture
clean-architecture
rest-api
postgresql
redis
docker
devops
ci-cd
observability
security
pytest
software-engineering
portfolio
```

### Social Preview

- **Image:** [TO BE DESIGNED — architecture diagram or branded banner]
- **Description:** Enterprise-grade platform architecture and implementation portfolio

---

## Branch Protection — `main`

The following protection rules must be applied to the `main` branch:

| Rule | Setting |
|------|---------|
| **Require pull request before merge** | Enabled |
| **Required approving reviews** | 1 minimum |
| **Dismiss stale approvals** | Enabled |
| **Require review from code owners** | Enabled (when CODEOWNERS is defined) |
| **Require status checks** | Enabled |
| **Required status checks** | `lint`, `test`, `security-scan` (when CI is configured) |
| **Require branches to be up to date** | Enabled |
| **Require conversation resolution** | Enabled |
| **Require linear history** | Enabled (enforce squash or rebase merges) |
| **Do not allow bypassing the above settings** | Enabled |
| **Restrict force pushes** | Enabled |
| **Restrict deletions** | Enabled |
| **Allow force pushes** | Disabled |
| **Allow deletions** | Disabled |

### Restrict Direct Pushes

When CI/CD is configured, restrict direct pushes to `main`:

- **Restrict who can push to matching branches:** Enabled
- **Allowed:** No one (all changes go through pull requests)

---

## Branch Protection — `develop`

| Rule | Setting |
|------|---------|
| **Require pull request before merge** | Enabled |
| **Required approving reviews** | 1 minimum |
| **Dismiss stale approvals** | Enabled |
| **Require status checks** | Enabled |
| **Restrict force pushes** | Enabled |
| **Restrict deletions** | Enabled |

---

## Tag Protection

| Tag Pattern | Protection |
|-------------|------------|
| `architecture-baseline-*` | Protected — require review for creation and modification |
| `v*` | Protected — require review for creation |
| `*` (default) | Restrict tag creation to maintainers |

---

## CODEOWNERS

When the team is defined, create `.github/CODEOWNERS`:

```
# Architecture and governance
AGENTS.md                     @maintainer
docs/                         @maintainer
architecture/                 @maintainer
LICENSE                       @maintainer
README.md                     @maintainer
CONTRIBUTING.md               @maintainer
SECURITY.md                   @maintainer

# Implementation
implementation/backend/       @maintainer
implementation/frontend/      @maintainer

# Infrastructure
docker/                       @maintainer
docker-compose.yml            @maintainer
Makefile                      @maintainer
```

---

## Issue Templates

### Bug Report

```yaml
name: Bug Report
about: Report a defect or unexpected behaviour
labels: [bug, triage]
assignees: []
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Clear description of the issue
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected Behaviour
    validations:
      required: true
```

### Architecture Discussion

```yaml
name: Architecture Discussion
about: Discuss architecture decisions or propose changes
labels: [architecture, discussion]
body:
  - type: textarea
    id: context
    attributes:
      label: Context
      description: What architecture area does this relate to?
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposal
    validations:
      required: true
```

---

## Release Policy

| Event | Action |
|-------|--------|
| Architecture Baseline milestone | Annotated tag `architecture-baseline-v{X}` |
| Version release | Annotated tag `v{X.Y.Z}` with release notes |
| Pre-release | Tag `v{X.Y.Z}-rc.{N}` |

Release notes must include:
- Summary of changes
- Architecture baseline version (if changed)
- Breaking changes
- Migration instructions
- Security advisories (if any)

---

## Vulnerability Reporting

Configured via `SECURITY.md`. Private vulnerability reporting should be
enabled in GitHub repository settings when available.

---

## Branch Protection Enforcement

OpenCode must not apply remote GitHub settings. These settings must be
applied manually by the Human Product Owner or repository administrator.

```bash
# Example using GitHub CLI (admin only):
gh api repos/{owner}/{repo}/branches/main/protection -X PUT --input branch-protection.json
```

---

## Audit Trail

All branch protection changes, tag protection changes, and repository
setting modifications must be documented in `architecture/reviews/` with
the date, administrator, and reason for the change.
