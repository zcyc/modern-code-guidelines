# Scala version rules

Use these rules after resolving the module's Scala version, binary target,
platform, and JDK. Pin the latest patch release in the chosen support line.

## Current support lines

- Scala 3.8.4 is the current Scala 3 Next line; Scala 3.3.8 is the current
  Scala 3 LTS line, and Scala 2.13.18 is the current Scala 2.13 line.
- Treat Scala 3.9.0-RC6, nightly builds, and other development snapshots as
  non-production toolchain versions.
- Scala 3.8+ requires JDK 17 or later. Scala 3.3 LTS remains the line for
  libraries that must publish JDK 8-compatible bytecode; Scala 2.13 has its own
  JDK compatibility boundary.
- At this audit date, sbt 2.0.8, Scala CLI 1.16.0, Scala.js 1.22.0, and Scala
  Native 0.5.12 are independently versioned toolchains; do not infer one
  version from another.

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
- Use strict equality only when the domain benefits from rejecting unrelated
  comparisons; do not add `CanEqual` noise to ordinary value code.
- Use top-level definitions and `export` clauses when they make the public
  module boundary clearer; keep re-exports deliberate.

## Scala 3.3 LTS+

- Choose Scala 3.3 LTS when the library must retain JDK 8-compatible bytecode or
  the deployment support policy requires the LTS line.
- Do not assume a feature available in Scala 3.8 is available in 3.3 LTS; use
  the module's declared compiler target rather than the local compiler.

## Scala 3.7+

- Use named tuples when names materially improve a tuple-shaped API; keep
  `@publicInBinary` for intentional binary API commitments, not ordinary code.
- Treat `-preview` as an explicit risk choice for applications or internal
  tools, not as a default modernization flag or a published-library baseline.
- Review given resolution after upgrading to Scala 3.7 because the default
  prioritization changed; make competing givens unambiguous.
- Better Fors are preview in 3.7 and stable in 3.8. Before migrating, check
  comprehensions with consecutive aliases or overloaded `map` methods because
  their runtime result type can change.
- Use `-source:3.7-migration -rewrite` only in an explicit, reviewed migration
  pass; do not enable compiler rewrites as a normal build default.

## Scala 3.8+

- Use the stabilized Better Fors desugaring when its aliases and reduced
  intermediate `map` calls make the comprehension clearer; review behavior when
  migrating code that depends on collection result types.
- Use `runtimeChecked` when a deliberate runtime check is preferable to the old
  `: @unchecked` type ascription; do not use it to hide exhaustiveness or
  unsafe-access diagnostics accidentally.
- Supply context-bound arguments with `using` when the Scala 3.8 standard
  library exposes them as contextual parameters; prefer inferred calls such as
  `Array.empty[Int]` when they are clearer.
- Add an explicit `scala3-repl` dependency when embedding the REPL; the REPL is
  no longer bundled in the core distribution.
- Do not target Scala 3.8.0 or 3.8.1 for new builds; use the latest 3.8.x patch
  release because early 3.8 releases had documented runtime/compiler regressions.
- Keep `into` preview, and flexible varargs and strict-equality pattern matching
  experimental; do not introduce them into ordinary production code without an
  explicit opt-in.

## Scala 2.13 and Scala 3 compatibility

- Scala 3 can consume Scala 2.13 artifacts, but Scala 2.13's `-Ytasty-reader`
  only reads Scala 3 artifacts through Scala 3.7; it does not read Scala 3.8+
  artifacts.
- Treat `-Ytasty-reader` as a one-way migration tool, not a permanent
  compatibility facade. If both ecosystems are published, cross-build native
  Scala 2.13 and Scala 3 artifacts.
- Keep `scala-library`, compiler, reflect, and platform artifacts aligned
  within the selected binary line; `_2.13` and `_3` dependency suffixes do
  not prove source or TASTy compatibility.

## Cross-platform and concurrency rules

- Resolve JVM, Scala.js, Scala Native, and Wasm library availability separately
  from the Scala language version; a compiler feature does not guarantee a
  platform API.
- Keep `Future` execution contexts bounded and owned for blocking work. If the
  project uses an effect runtime, preserve its structured lifetime and
  cancellation model instead of creating detached fibers or global scopes.
- Cross-build only when the project explicitly publishes multiple Scala binary
  versions; otherwise migrate directly to the selected line rather than adding
  compatibility facades or duplicate APIs.
- Scala.js 1.22.0 makes its WebAssembly backend stable, but backend artifacts
  are not forward-binary-compatible across the 1.21/1.22 boundary; upgrade and
  relink the complete backend/toolchain together.
- Scala Native 0.5.12 has a separate compiler/backend support matrix; resolve
  the exact Scala artifact instead of inferring support from the Native version.
  Keep Native virtual threads experimental.
- Scala.js Wasm output still requires an ES2022+ host, Wasm 3.0, ES modules, and
  explicit JSPI support for `js.async`/`js.await`; Scala CLI Wasm directives
  remain experimental.

## Tooling

- Use `scalafmt` with the repository's pinned version and dialect.
- Use Scalafix only when the repository has a checked-in `.scalafix.conf` and
  compatible compiler/SemanticDB setup; prefer `--check` in CI and review
  rewrites before applying them.
- Set sbt `scalaVersion` explicitly; use `crossScalaVersions` and explicit
  JVM/JS/Native rows only when the project publishes those targets.
- Pin an exact Scala CLI version and an exact `using scala`/platform version in
  reproducible builds; do not rely on a moving default or short version prefix.
- Keep the compiler, build tool, formatter, Scalafix runner, and IDE language
  service aligned with the declared Scala binary version.

## Authority

- [Scala downloads and current release lines](https://www.scala-lang.org/download/)
- [Scala 3.8 release](https://www.scala-lang.org/news/3.8/)
- [Scala 3.8.4 release](https://www.scala-lang.org/news/3.8.4/)
- [Scala 2.13.18 release](https://www.scala-lang.org/news/2.13.18/)
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
