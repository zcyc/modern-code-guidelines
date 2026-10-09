---
name: use-modern-scala
description: "Use for Scala code and reviews: versions, givens/implicits, effects, tools, and platform compatibility."
---

# Scala

Resolve the changed file's target from scalaVersion/crossScalaVersions in build.sbt/Gradle/Mill, project/build.properties or Scala CLI //> using scala/toolchain; JVM/JS/Native/Wasm and JDK targets.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
