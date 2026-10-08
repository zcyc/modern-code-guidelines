---
name: use-modern-django
description: "Use when writing or reviewing code involving Django requests, ORM, transactions, tasks, and deployment."
---

# Django

Resolve the changed file's target from pyproject.toml/packaging, lockfile, Python/Django, settings, URLs, database and WSGI/ASGI entry point.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-python for language and concurrency.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
