---
name: use-modern-ktor
description: "Use version-aware Ktor server routing, plugins, serialization, coroutine, configuration, testing, and deployment idioms when writing, modifying, fixing, or reviewing Ktor code."
---

# Modern Ktor

Use for Ktor server applications. Pair with `use-modern-kotlin` for
Kotlin language and coroutine rules; resolve Gradle and Ktor versions together.

## Target resolution

Read the Gradle version catalog/build files, Kotlin compiler, Ktor version, JVM or
Android target, serialization plugin, engine, and deployment environment. Do not
mix Ktor plugin and artifact versions or infer the engine from a sample.


## Working rules

- Keep application modules and installed plugins explicit. Use routing for HTTP
  boundaries and keep domain work outside the Ktor pipeline.
- Use structured coroutines in Ktor's request/application scopes. Do not
  launch request work in `GlobalScope` or detach work whose lifetime belongs to a
  request or application.
- Install serialization, status handling, authentication, and content policies
  deliberately; plugin order and route scope are part of the request contract.
- Decode and validate request data at the boundary, return typed responses with
  deliberate status codes, and keep error payloads safe for clients.
- Load configuration from the declared environment/config file, validate required
  values at startup, and keep secrets out of source and logs.
- Test routes and plugins with `testApplication` or the project's established Ktor
  test host; avoid real network sockets for unit-level behavior.

Read `references/guidelines.md` for plugin pipelines, coroutines, configuration,
deployment, and testing rules.
