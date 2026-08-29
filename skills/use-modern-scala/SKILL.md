---
name: use-modern-scala
description: Use version-aware Scala language, standard-library, build, functional, and concurrency idioms when writing, modifying, fixing, or reviewing Scala code.
---

# Modern Scala

Apply stable Scala features supported by the module's declared Scala version,
platform target, and JDK. Read `references/guidelines.md` before using
version-gated syntax or APIs.

## Target resolution

Read the effective target for the module:

1. `scalaVersion`/`crossScalaVersions` in `build.sbt`, Gradle, or Mill
   configuration, plus `project/build.properties` for sbt.
2. Scala CLI directives such as `//> using scala` and the selected
   `scala-cli`/Coursier toolchain.
3. JVM/Scala.js/Scala Native/Wasm targets, JDK target, and explicit settings in
   CI or build scripts.

Scala 2.13 and Scala 3 are separate language and binary-version targets. The
Scala version, platform library, and JDK/JavaScript/native runtime are separate
constraints. If a target is unknown, report it and avoid version-gated syntax or
APIs. Do not infer it from the local compiler or IDE.

## Checks

- Use the repository's declared build tool: `sbt compile`/`test`, `mill`,
  `scala-cli compile`/`test`, or the configured Gradle task.
- Use `scalafmt` with the checked-in `.scalafmt.conf`; do not invent formatter
  settings for a local change.
- Run configured Scalafix rules with `scalafix --check` only when the project
  already declares Scalafix and its SemanticDB/compiler setup.
- Treat compiler warnings, exhaustiveness diagnostics, and unused/import
  diagnostics as correctness feedback; do not add broad suppressions.

## Working rules

- Prefer immutable `val`, immutable collections, total pattern matches, and
  explicit ownership of effects and resources.
- Use `Option`/`Either` or the project's established effect type for absence and
  recoverable failure; do not use `null` or exceptions as routine control flow.
- Keep public result types explicit. Use `enum`, opaque types, extension methods,
  and type classes when they make the domain contract clearer.
- Use `given`/`using` for contextual dependencies in Scala 3 and explicit
  `implicit` parameters in Scala 2 only where the dependency is genuinely
  contextual. Avoid surprising implicit conversions and global mutable state.
- Give every `Future`, fiber, stream, or actor an owner, execution context, and
  cancellation/error policy. Do not run blocking work on a general-purpose
  compute pool.
- Keep Java/platform interop at explicit boundaries and preserve the module's
  binary/API contract while changing the smallest relevant surface.
