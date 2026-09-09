# Django version rules

Resolve Django, Python, database, and deployment targets from the repository.
The WSGI/ASGI choice changes the concurrency model.

## Version gates

- Django's built-in Tasks API and CSP middleware/settings are available from
  Django 6.0. On older targets, use only the project's selected task and CSP
  integration; do not import these APIs conditionally as a compatibility layer.
- Django 6.0 requires Python 3.12 or later. Resolve the Python and Django
  targets together before copying a 6.0 example or upgrading dependencies.
- Async ORM coverage continues to grow across Django releases. Check the
  declared Django version and database backend for each async query method
  instead of assuming the synchronous ORM has an async equivalent.

## ORM and requests

- Use select_related for single-valued joins and prefetch_related for
  collections when profiling or query inspection shows a fan-out problem.
- Keep transaction.atomic scopes small and database-focused. Do not hold a
  transaction open while waiting on an unrelated service.
- Let templates autoescape untrusted data. Treat mark_safe and raw SQL as
  reviewed boundary operations.

## Async

- Async views provide a useful async stack under ASGI; synchronous middleware or
  database/library calls can force thread adaptation or block the event loop.
- Use the async ORM APIs available in the installed Django version. Wrap
  synchronous-only code with the supported bridge rather than calling it directly
  from an async context.

## Tasks and security defaults

- Django's Tasks API defines task metadata, queueing, and result handling; it
  does not provide the worker or a durable production queue. Choose and verify
  the external backend before treating a task as reliable background work.
- On targets that provide Django's CSP middleware, use `SECURE_CSP` and
  `SECURE_CSP_REPORT_ONLY` deliberately. Start in report-only mode when tuning a
  policy, then enforce a reviewed policy without weakening other security headers.

## Authority

- https://docs.djangoproject.com/en/6.0/releases/6.0/
- https://docs.djangoproject.com/en/stable/
- https://docs.djangoproject.com/en/stable/topics/async/
- https://docs.djangoproject.com/en/stable/topics/db/optimization/
- https://docs.djangoproject.com/en/stable/topics/db/transactions/
- https://docs.djangoproject.com/en/stable/topics/security/
- https://docs.djangoproject.com/en/stable/topics/tasks/
- https://docs.djangoproject.com/en/stable/ref/settings/
- https://docs.djangoproject.com/en/stable/topics/migrations/
