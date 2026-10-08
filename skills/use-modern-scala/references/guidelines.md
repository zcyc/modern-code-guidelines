# Scala

## Versions and binary boundaries

- Align compiler, stdlib, plugins and artifacts within Scala 2.13 or Scala 3. Production uses a patched stable support line.
- Scala 3.9 and 3.3 are LTS; 3.3 supports JDK 8-compatible bytecode, 3.8+ requires JDK 17. Resolve deployment JVM separately from source version.
- 2.13: immutable collections, Option/Either, explicit public result types and ExecutionContext; keep implicit conversions deliberate.
- 3: enum, opaque types, extensions, given/using, unions/intersections and derives when they clarify a reusable contract; inline needs a compile-time invariant or measured runtime reason.
- 3.7 changes given prioritization; disambiguate competing givens. Preview/migration rewrites require explicit intent.
- 3.8: Better Fors and runtimeChecked; check collection result types after desugaring changes. Flexible varargs and strict-equality matching remain experimental.
- 3.9: into for intentional conversions; -deprecation exposes companion-given lookup changes ahead of 3.10.
- Scala 3 consumes 2.13 artifacts; 2.13 -Ytasty-reader reads Scala 3 through 3.7, not 3.8+. Cross-build native artifacts when publishing to both ecosystems.

## Effects and tooling

- Own Future/fiber/stream/actor execution and failure/cancellation; blocking work needs a bounded executor rather than the general compute/global pool. Preserve an existing effect runtime.
- Resolve JVM/Scala.js/Native/Wasm libraries separately. Keep platform interop and binary/API contracts explicit.
- Run the selected sbt/Mill/Scala CLI/Gradle build; scalafmt uses .scalafmt.conf and its pinned version/dialect. Existing Scalafix needs compatible SemanticDB/config; review rewrites and use scalafix --check in CI.
- Pin scalaVersion and reproducible Scala CLI/platform versions; crossScalaVersions/platform rows belong only to published targets.

## Sources

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
