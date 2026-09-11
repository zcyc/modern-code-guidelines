# Flask version rules

Resolve the Python interpreter target, Flask version, WSGI/ASGI server, and
extension versions before using framework APIs. Flask application context and
request context are separate lifetimes and should remain visible in the design.

## Application structure

- Use a factory when the app has more than one configuration, a test instance,
  or extensions that need late initialization.
- Keep extensions unbound until `init_app`; do not make import order decide which
  application instance receives database, cache, or authentication state.
- Use blueprints for cohesive route and error-handler boundaries. Keep business
  rules in ordinary Python modules that can be tested without a live request.

## Context and request boundaries

- Access `request`, `session`, `current_app`, and `g` only within their documented
  context. Store request-scoped resources on `g` and close them in teardown code.
- Validate and normalize headers, query parameters, path values, JSON, and form
  data before calling domain code. Never treat a type hint as runtime validation.
- Keep Jinja autoescaping enabled for HTML templates and return explicit response
  status codes for errors, redirects, and empty results.
- Treat CORS as a browser-origin policy, not authentication or CSRF protection.
  Protect browser forms and state-changing endpoints with the project's explicit
  CSRF and authentication policy.

## Async, errors, and deployment

- Use async views only when the selected Flask version and deployment support the
  intended workload and the async extra is installed. Under WSGI, each async view
  still occupies one worker; use a task queue or an explicit ASGI adapter for
  background or long-lived async work.
- Register specific error handlers for expected failures and a safe fallback for
  unexpected failures. Log diagnostic context server-side without returning
  secrets or tracebacks to clients.
- Run production traffic behind a production WSGI server, or an explicit ASGI
  adapter. Treat `flask run` as a development tool and configure forwarded headers
  only for a trusted proxy.

## Testing

- Build a fresh app with the factory for each isolated test configuration.
- Use the test client for HTTP behavior and explicit application/request contexts
  for code that needs them. Keep database, filesystem, and environment state
  reset between tests.

## Authority

- https://flask.palletsprojects.com/en/stable/
- https://flask.palletsprojects.com/en/stable/patterns/appfactories/
- https://flask.palletsprojects.com/en/stable/appcontext/
- https://flask.palletsprojects.com/en/stable/reqcontext/
- https://flask.palletsprojects.com/en/stable/async-await/
- https://flask.palletsprojects.com/en/stable/testing/
