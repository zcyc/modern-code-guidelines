# Django

## Gates

- Django 6.0 requires Python 3.12+ and adds Tasks and CSP middleware/settings. Older targets use their existing integrations.
- Verify each async ORM method against the selected Django/database version; synchronous and async APIs are not interchangeable.

## Requests and ORM

- Validate/authorize requests; preserve CSRF and template escaping. mark_safe and raw SQL are reviewed trust boundaries.
- Inspect query count; select_related handles single-valued joins, prefetch_related collections. Keep QuerySets lazy until intended evaluation.
- transaction.atomic protects multi-step invariants; keep scopes small and unrelated network calls outside. Append deployed migration history.
- ASGI enables an async stack; sync middleware/libraries can force thread adaptation. Use supported bridges for sync-only work; async transactions need a documented supported boundary.

## Tasks and security

- Tasks defines queue/result contracts, not a durable queue/worker; configure and verify a production backend before relying on execution.
- SECURE_CSP/SECURE_CSP_REPORT_ONLY configure built-in CSP; tune report-only then enforce. Keep production secrets/settings separate from tests.

## Sources

- https://docs.djangoproject.com/en/6.0/releases/6.0/
- https://docs.djangoproject.com/en/stable/
- https://docs.djangoproject.com/en/stable/topics/async/
- https://docs.djangoproject.com/en/stable/topics/db/optimization/
- https://docs.djangoproject.com/en/stable/topics/db/transactions/
- https://docs.djangoproject.com/en/stable/topics/security/
- https://docs.djangoproject.com/en/stable/topics/tasks/
- https://docs.djangoproject.com/en/stable/ref/settings/
- https://docs.djangoproject.com/en/stable/topics/migrations/
