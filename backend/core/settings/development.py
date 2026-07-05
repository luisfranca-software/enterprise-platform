"""Development settings — inherit base and enable debug / relaxed checks."""

from .base import *

# ---------------------------------------------------------------------------
# Security overrides for local development
# ---------------------------------------------------------------------------

DEBUG = True

ALLOWED_HOSTS = ["*"]

# ---------------------------------------------------------------------------
# Email – print to console instead of sending real messages
# ---------------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
