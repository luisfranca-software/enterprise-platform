# Third-Party Notices

This document records third-party dependencies, their licences, and
compatibility status with the proprietary repository licence.

**Review Date:** 2026-07-25
**Reviewer:** OpenCode (automated audit)

---

## Runtime Dependencies (base.txt)

| Dependency | Version Constraint | Installed Version | Licence | Source | Compatibility | Attribution Required | Review Status |
|------------|-------------------|-------------------|---------|--------|---------------|---------------------|---------------|
| Django | `>=6.0` | 6.0.6 | BSD-3-Clause | https://www.djangoproject.com/ | Compatible | Yes (BSD notice) | Verified |
| psycopg | `*` | 3.3.4 | LGPL-3.0-only | https://psycopg.org/ | Compatible (dynamic linking) | Yes (LGPL notice) | Verified |
| psycopg-binary | (transitive) | 3.3.4 | LGPL-3.0-only | https://psycopg.org/ | Compatible (dynamic linking) | Yes (LGPL notice) | Verified |
| python-dotenv | `*` | 1.2.2 | BSD-3-Clause | https://github.com/theskumar/python-dotenv | Compatible | Yes (BSD notice) | Verified |
| django-environ | `>=0.12` | 0.14.0 | MIT | https://django-environ.readthedocs.org | Compatible | Yes (MIT notice) | Verified |

## Development Dependencies (dev.txt)

| Dependency | Version Constraint | Installed Version | Licence | Source | Compatibility | Attribution Required | Review Status |
|------------|-------------------|-------------------|---------|--------|---------------|---------------------|---------------|
| pytest | `*` | 9.1.1 | MIT | https://docs.pytest.org/ | Compatible | Yes (MIT notice) | Verified |
| pytest-django | `*` | 4.12.0 | BSD-3-Clause | https://pytest-django.readthedocs.io/ | Compatible | Yes (BSD notice) | Verified |
| black | `*` | 26.5.1 | MIT | https://github.com/psf/black | Compatible | Yes (MIT notice) | Verified |
| ruff | `*` | 0.15.20 | MIT | https://docs.astral.sh/ruff | Compatible | Yes (MIT notice) | Verified |
| ipython | `*` | 9.15.0 | BSD-3-Clause | https://ipython.org | Compatible | Yes (BSD notice) | Verified |

## Production Dependencies (prod.txt)

| Dependency | Version Constraint | Installed Version | Licence | Source | Compatibility | Attribution Required | Review Status |
|------------|-------------------|-------------------|---------|--------|---------------|---------------------|---------------|
| gunicorn | `*` | Not installed locally | MIT | https://gunicorn.org | Compatible | Yes (MIT notice) | Verified (not installed in dev) |

---

## Licence Compatibility Summary

| Licence Category | Count | Compatibility |
|------------------|-------|---------------|
| MIT | 5 | Compatible — permissive, no copyleft obligations for proprietary use |
| BSD-3-Clause | 4 | Compatible — permissive, attribution required |
| LGPL-3.0-only | 2 (psycopg, psycopg-binary) | Compatible — dynamic linking; no copyleft obligation for proprietary works using the library as a dependency |

### Notes on LGPL-3.0 (psycopg)

psycopg and psycopg-binary are licensed under LGPL-3.0-only. When used
as a dynamically linked library (as is standard with pip-installed Python
packages), the LGPL does not impose copyleft obligations on the consuming
proprietary software. The binary distribution (psycopg-binary) bundles
libpq under the same LGPL terms.

**Required action:** Include LGPL-3.0 licence text and attribution in
distribution notices if the software is distributed to end users.

---

## Flagged Items

| Item | Status | Action Required |
|------|--------|-----------------|
| All dependencies | Permissive or LGPL (dynamic linking) | No blocking issues identified |
| No GPL-only dependencies | Confirmed | None |
| No AGPL dependencies | Confirmed | None |
| No unknown-licence dependencies | Confirmed | None |
| No copied code without provenance | Confirmed | None |
| No third-party images or fonts | Confirmed | None |
| No generated assets with unclear rights | Confirmed | None |

---

## Attribution Notices

The following licences require attribution in distributed works:

### BSD-3-Clause (Django, python-dotenv, pytest-django, ipython)

```
Copyright (c) [ respective copyright holders ]
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

### MIT (django-environ, pytest, black, ruff, gunicorn)

```
Copyright (c) [ respective copyright holders ]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### LGPL-3.0-only (psycopg, psycopg-binary)

Full LGPL-3.0 licence text available at:
https://www.gnu.org/licenses/lgpl-3.0.html
