# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Architecture Baseline v1.0.x | Yes |
| Older versions | No |

Only the latest release and the current Architecture Baseline version
receive security updates. If you are using an older version, upgrade
to the latest supported version.

---

## Reporting a Vulnerability

If you discover a security vulnerability in this repository or its
documented architecture, please report it responsibly.

### How to Report

- **Do not** open a public issue for security vulnerabilities.
- **Do not** disclose vulnerability details in public forums, pull
  requests, or discussions.
- Contact the maintainer directly using the channel below.

### Contact

[SECURITY CONTACT TO BE DEFINED]

If no contact is listed, do not submit vulnerability reports until
one is established.

### What to Include

- Description of the vulnerability
- Affected component or document
- Steps to reproduce (if applicable)
- Potential impact assessment
- Suggested remediation (if known)

### What to Expect

- Acknowledgement of your report within a reasonable timeframe
- An assessment of the vulnerability's severity and impact
- Notification when the issue is resolved
- Credit in the release notes (unless you prefer anonymity)

---

## Scope

This security policy covers:

- The source code in `implementation/`
- Configuration files and settings
- Architecture documents that describe security controls
- Docker and deployment configurations

This policy does **not** cover:

- Third-party dependencies (report issues to their respective maintainers)
- Deployed instances of the application (report to the deployment operator)
- Infrastructure not managed by this project's maintainer

---

## Responsible Disclosure

We ask that you:

- Allow reasonable time for remediation before public disclosure
- Do not exploit the vulnerability beyond what is necessary to demonstrate it
- Do not access, modify, or delete data belonging to others
- Do not disrupt services or systems
- Act in good faith

---

## Authorisation Limitations

Authorisation to inspect public source code does not authorise:

- Testing against deployed systems or services
- Accessing data or systems without explicit permission
- Performing penetration testing or security scanning against infrastructure
  not owned by the reporter
- Circumventing security controls for purposes beyond vulnerability reporting

Any such activity requires separate, explicit written authorisation from
the system owner.

---

## Security Practices

This project follows these security practices:

- `DEBUG` is never enabled in production
- `SECRET_KEY` is rotated per environment and never committed to version control
- `ALLOWED_HOSTS` is restricted to known domains
- Passwords are hashed using Django's PBKDF2 hasher
- Session cookies are HTTPOnly, Secure, and SameSite=Lax
- CSRF protection is enabled globally
- API rate limiting is applied at the Nginx or middleware layer
- File uploads are validated by type and size
- SQL injection is prevented via Django ORM parameterised queries
- No secrets, credentials, or private keys are committed to the repository

---

## Git History

This repository's Git history is publicly visible. Sensitive information
must never have been committed. If a secret or credential is discovered
in the Git history:

1. The repository maintainer must be notified immediately
2. The affected credentials must be revoked and rotated
3. A history-rewrite plan must be prepared (requiring Human Approval)

---

## Contact

[SECURITY CONTACT TO BE DEFINED]
