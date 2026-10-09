---
name: use-modern-django
description: "Use for Django code and reviews: requests, ORM queries, transactions, tasks, and deployment."
---

# Django

Resolve the changed file's target from pyproject.toml/packaging, lockfile, Python/Django, settings, URLs, database and WSGI/ASGI entry point.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-python for language and concurrency.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
