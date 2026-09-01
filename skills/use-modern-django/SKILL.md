---
name: use-modern-django
description: "Use version-aware Django request, ORM, async, security, migration, and settings idioms when writing, modifying, fixing, or reviewing Django code."
---

# Modern Django

Use for Django applications and reusable Django packages. Pair with
use-modern-python for Python rules.

## Target resolution

Read pyproject.toml or the project's packaging metadata, lockfile, Django
version, settings module, URL configuration, database backend, and WSGI/ASGI
entry point. Do not infer support from the local interpreter.

## Working rules

- Keep validation and authorization at the request boundary; rely on Django's
  CSRF and escaping protections instead of bypassing them with safe-marking APIs.
- Prevent ORM N+1 queries with deliberate select_related or prefetch_related
  choices, and keep query construction lazy until evaluation is intended.
- Use transaction.atomic for multi-step invariants and keep external network
  calls outside database transactions unless the coupling is deliberate.
- Treat migrations as versioned schema history. Create, review, and commit new
  migrations; do not rewrite applied migrations to repair application behavior.
- Use async views and async ORM APIs only when the deployment is ASGI and every
  relevant dependency supports the async path. Bridge synchronous code explicitly.
- Use Django's Tasks API for queueing deferred work when the target supports it,
  but configure a production backend and worker; the framework contract alone
  does not make work durable or executable.
- Keep settings and secrets environment-specific; never commit credentials or
  weaken production security settings to make a test pass.

Read references/guidelines.md before using version-gated async ORM or framework APIs.
