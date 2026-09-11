---
name: use-modern-flask
description: "Use version-aware Flask application-factory, request-context, validation, error-handling, testing, and deployment idioms when writing, modifying, fixing, or reviewing Flask code."
---

# Modern Flask

Use for Flask applications and APIs. Pair with `use-modern-python` for Python
language, typing, standard-library, and concurrency rules.

## Target resolution

Read the project's Python target, Flask version, WSGI/ASGI deployment, extension
set, and configuration source. Establish whether async views are actually
required by the deployment before adding them to a synchronous Flask app.


## Working rules

- Use an application factory for applications that have multiple environments,
  test instances, or extensions. Initialize extensions with `init_app` rather
  than binding them to one global application at import time.
- Use blueprints for real application boundaries and keep route handlers thin;
  move domain and persistence work out of the request wiring.
- Respect application and request context ownership. Use `current_app`, `g`, and
  request data only inside their valid context and release request-scoped
  resources through teardown hooks.
- Validate request data at the boundary, rely on Jinja autoescaping for HTML, and
  return deliberate status codes and error payloads.
- Keep async views opt-in and deployment-aware. Flask's async support requires the
  target's async extra, and its WSGI model does not become a scalable async
  service by adding `async`.
- Use Flask's test client and application contexts for focused tests; run behind a
  production WSGI server, or an explicit ASGI adapter, rather than the development
  server in production.

Read `references/guidelines.md` for factories, contexts, async behavior,
security, testing, and deployment rules.
