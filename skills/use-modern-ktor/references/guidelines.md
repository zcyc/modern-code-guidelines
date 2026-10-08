# Ktor server

## Version boundary

- Keep Ktor artifacts/plugins on one release line and verify Kotlin/serialization/engine compatibility.
- Ktor 3 replaces low-level I/O with kotlinx-io; use that release's channel/source/sink APIs instead of copying 2.x implementations.
- Check current plugin imports/configuration against the selected release's migration guide; latest docs need not match a 2.x server.

## Pipeline and resources

- Application.module assembles plugins/routes/config; domain logic uses ordinary Kotlin dependencies. Plugin order and route scope affect auth/parsing/transformation/errors.
- ContentNegotiation serializes typed payloads; validate path/query/headers/body and authorize before domain work. StatusPages maps expected errors; log unexpected causes without leaking secrets.
- Own request/application coroutines and cancellation; never detach request work into GlobalScope. Validate config at startup; configure engine timeouts/TLS/trusted proxies and bounded graceful shutdown.
- testApplication covers routes/plugins/serialization/errors in-process; real sockets belong to socket/TLS/proxy/engine tests. Isolate test configuration.

## Sources

- https://ktor.io/docs/server-create-and-configure.html
- https://ktor.io/docs/server-plugins.html
- https://ktor.io/docs/server-serialization.html
- https://ktor.io/docs/server-status-pages.html
- https://ktor.io/docs/server-auth.html
- https://ktor.io/docs/server-testing.html
- [Ktor 3 migration](https://ktor.io/docs/migrating-3.html)
