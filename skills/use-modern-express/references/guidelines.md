# Express version rules

Resolve the Express major version, Node.js runtime, module system, and deployment
topology before using framework APIs. Express 4 and Express 5 have overlapping
APIs but different async error behavior, so do not infer one from imports alone.

## Middleware and routing

- Keep `app.use` and router order visible. Middleware that parses, authenticates,
  authorizes, or transforms a request must run before the handlers that depend on
  it.
- Keep routers organized around a resource or boundary. Share middleware only
  when its scope and ordering remain obvious; avoid a global middleware registry.
- Keep request or user state request-scoped; use `res.locals` or an explicit
  service context rather than mutable module globals. Shared module state should
  be immutable configuration or deliberately synchronized infrastructure.
- Validate path parameters, query values, headers, and bodies before passing them
  to domain code. Treat request data as untrusted even after a TypeScript type
  assertion.

## Async errors and responses

- Express 5 forwards rejected promises from route handlers to error middleware;
  use that behavior when the project targets Express 5 instead of adding a
  wrapper to every handler.
- Do not assume that Express 4 has Express 5's rejected-promise forwarding; use
  the target version's established error contract when reviewing older code.
- Keep one four-argument error middleware near the end of the pipeline. Map
  expected domain errors to safe responses and log unexpected errors with their
  causes without exposing stack traces or secrets to clients.
- Set response status and body once. Return after sending a response or calling
  `next` so fallthrough cannot produce headers-sent failures.

## Security and lifecycle

- Set JSON and URL-encoded body limits, configure `trust proxy` from the real
  ingress topology, and use secure cookie/header settings for production.
- Keep secrets and environment configuration outside source. Validate required
  configuration at startup rather than failing on the first request.
- For long-lived servers, handle termination signals by stopping new work,
  closing the HTTP server, and cancelling owned resources. Do not leave timers,
  queues, or database connections running after shutdown begins.

## Authority

- https://expressjs.com/en/guide/migrating-5.html
- https://expressjs.com/en/guide/error-handling.html
- https://expressjs.com/en/advanced/best-practice-security.html
- https://expressjs.com/en/guide/using-middleware.html
