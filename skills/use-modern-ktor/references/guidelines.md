# Ktor version rules

Resolve Kotlin, Ktor, Gradle, serialization, engine, and deployment versions from
the build. Ktor artifact/plugin compatibility, Kotlin compiler compatibility, and
the runtime target are separate constraints.

## Application and plugin structure

- Keep `Application.module` focused on assembling configuration, plugins, and
  routes. Move domain logic into ordinary Kotlin components with explicit
  dependencies.
- Install plugins only where their scope is required. Make authentication,
  serialization, status handling, compression, and CORS policies visible rather
  than hiding them in a global setup function.
- Treat route and plugin order as behavior. Test the order when a plugin changes
  request parsing, authentication, response transformation, or error handling.

## Requests, responses, and errors

- Use `ContentNegotiation` and typed serialization for structured payloads. Validate
  path, query, headers, and body values at the HTTP boundary before calling domain
  code.
- Map expected failures to deliberate status codes and safe response bodies with
  `StatusPages`. Log unexpected causes on the server without exposing internals.
- Keep handlers short and suspend-aware. Propagate cancellation when a request is
  gone; do not convert request-scoped work into an unowned global coroutine.

## Configuration and lifecycle

- Validate configuration at startup and keep secrets in environment or the
  deployment secret store. Do not log credentials or full connection strings.
- Choose the engine and deployment model explicitly. Configure timeouts, TLS,
  proxy headers, and graceful shutdown for the actual hosting environment.
- Stop accepting work and close owned resources during application shutdown; keep
  background jobs in an application-owned scope with a visible cancellation path.

## Testing

- Use `testApplication` for routing, plugin, serialization, and status behavior.
  Keep tests in-process unless socket, TLS, proxy, or engine integration is the
  behavior under test.
- Exercise invalid input and error paths, not only successful routes. Keep test
  configuration isolated from development and production configuration.

## Authority

- https://ktor.io/docs/server-create-and-configure.html
- https://ktor.io/docs/server-plugins.html
- https://ktor.io/docs/server-serialization.html
- https://ktor.io/docs/server-status-pages.html
- https://ktor.io/docs/server-auth.html
- https://ktor.io/docs/server-testing.html
