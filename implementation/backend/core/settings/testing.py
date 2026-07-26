"""Testing settings — inherit base and optimise for fast test runs."""

from .base import *

# ---------------------------------------------------------------------------
# Debug / hosts
# ---------------------------------------------------------------------------

DEBUG = False

ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]

# ---------------------------------------------------------------------------
# Database – use in-memory SQLite for speed
# ---------------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

# ---------------------------------------------------------------------------
# Password hashing – use the fastest possible hasher
# ---------------------------------------------------------------------------

PASSWORD_HASHERS = [
    "django.contrib.auth.hashes.MD5PasswordHasher",
]

# ---------------------------------------------------------------------------
# Email – disable sending during tests
# ---------------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# ---------------------------------------------------------------------------
# Storage – use local file-based storage (no S3 during tests)
# ---------------------------------------------------------------------------

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
