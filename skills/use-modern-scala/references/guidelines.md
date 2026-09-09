# Scala version rules

Use these rules after resolving the module's Scala version, binary target,
platform, and JDK. Pin a patched release in the chosen support line.

## Support lines

- Resolve the selected Scala 2.13 or Scala 3 support line and platform
  toolchain from the build. Compiler, standard library, plugins, and published
  artifacts must remain aligned.
- Treat release candidates, nightly builds, and other development snapshots as
  non-production toolchain versions unless the project explicitly targets them.
- Scala 3.9 and 3.3 are LTS lines; choose 3.3 for JDK 8-compatible bytecode.
  Scala 3.8+ requires JDK 17. Choose the line from deployment policy, not the
  local JDK.

## Scala 2.13+

- Prefer immutable collections, `Option`, `Either`, and explicit result types;
  keep `scala.collection.mutable` and `var` at deliberate state boundaries.
- Pass `ExecutionContext` explicitly for `Future`-returning APIs and do not run
  blocking work on `ExecutionContext.global`.
- Prefer ordinary methods, case classes, and explicit type classes over implicit
  conversions or macro-heavy abstractions.
- Keep Scala 2.13 and Scala 3 source/binary compatibility explicit when
  cross-building; do not assume a Scala 2.13 artifact is a drop-in Scala 3 API.

## Scala 3+

- Prefer `enum`, opaque types, extension methods, `given`/`using`, union and
  intersection types, and `derives` when they make the model or type-class
  contract clearer.
- Use exhaustive `match` expressions for closed domains and keep pattern
  alternatives readable; do not silence exhaustiveness warnings broadly.
- Prefer contextual parameters over implicit conversions. Keep the provider
  visible at the boundary when implicit resolution would obscure ownership.
- Use `inline` and compile-time operations only when they remove a measured
  runtime cost or enforce a useful compile-time invariant.

## Scala 3.7+

- Review given resolution after upgrading to Scala 3.7 because the default
  prioritization changed; make competing givens unambiguous.
- Keep `-preview` and migration rewrites as explicit, reviewed choices; never
  enable them as a normal published-library build default.

## Scala 3.8+

- Use the stabilized Better Fors desugaring when its aliases and reduced
  intermediate `map` calls make the comprehension clearer; review behavior when
  migrating code that depends on collection result types.
- Use `runtimeChecked` when a deliberate runtime check is preferable to the old
  `: @unchecked` type ascription; do not use it to hide exhaustiveness or
  unsafe-access diagnostics accidentally.
- Keep flexible varargs and strict-equality pattern matching experimental; do
  not introduce them into ordinary production code without explicit opt-in.

## Scala 3.9+

- Use `into` only where an implicit conversion is an intentional API contract;
  its stabilization is not a reason to enable unrestricted conversions.
- Compile with `-deprecation` after upgrading to surface companion-given
  lookups that will stop resolving in Scala 3.10; fix the library boundary
  rather than adding a consumer-side workaround.

## Scala 2.13 and Scala 3 compatibility

- Scala 3 can consume Scala 2.13 artifacts, but Scala 2.13's `-Ytasty-reader`
  only reads Scala 3 artifacts through Scala 3.7; it does not read Scala 3.8+
  artifacts.
- Treat `-Ytasty-reader` as a one-way migration tool. If both ecosystems are
  published, cross-build native Scala 2.13 and Scala 3 artifacts.

## Cross-platform and concurrency rules

- Resolve JVM, Scala.js, Scala Native, and Wasm library availability separately
  from the language version; a compiler feature does not guarantee a platform
  API.
- Keep `Future` execution contexts bounded and owned for blocking work. If the
  project uses an effect runtime, preserve its structured lifetime and
  cancellation model instead of creating detached fibers or global scopes.

## Tooling

- Use `scalafmt` with the repository's pinned version and dialect.
- Use Scalafix only when the repository has a checked-in `.scalafix.conf` and
  compatible compiler/SemanticDB setup; prefer `--check` in CI and review
  rewrites before applying them.
- Set sbt `scalaVersion` explicitly; use `crossScalaVersions` and explicit
  JVM/JS/Native rows only when the project publishes those targets.
- Pin an exact Scala CLI version and an exact `using scala`/platform version in
  reproducible builds; do not rely on a moving default or short version prefix.

## Authority

- [Scala downloads and support lines](https://www.scala-lang.org/download/)
- [Scala 3.9 release](https://www.scala-lang.org/news/3.9/)
- [Scala 3 release notes](https://www.scala-lang.org/news/3.8/)
- [Scala 3.7 release](https://www.scala-lang.org/news/3.7.0/)
- [Scala 3 Reference](https://docs.scala-lang.org/scala3/reference/)
- [TASTy compatibility](https://www.scala-lang.org/blog/state-of-tasty-reader.html)
- [Scala/JDK compatibility](https://docs.scala-lang.org/overviews/jdk-compatibility/overview.html)
- [sbt](https://www.scala-sbt.org/)
- [Scala CLI version selection](https://scala-cli.virtuslab.org/docs/cookbooks/introduction/scala-versions/)
- [Scala.js releases](https://github.com/scala-js/scala-js/releases)
- [Scala Native releases](https://github.com/scala-native/scala-native/releases)
- [Scalafmt configuration](https://scalameta.org/scalafmt/docs/configuration.html)
- [Scalafix installation and checks](https://scalacenter.github.io/scalafix/docs/users/installation.html)
