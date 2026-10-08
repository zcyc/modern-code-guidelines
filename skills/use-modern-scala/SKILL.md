---
name: use-modern-scala
description: "Use when writing or reviewing code involving Scala versions, contextual APIs, effects, tooling, and platform compatibility."
---

# Scala

Resolve the changed file's target from scalaVersion/crossScalaVersions in build.sbt/Gradle/Mill, project/build.properties or Scala CLI //> using scala/toolchain; JVM/JS/Native/Wasm and JDK targets.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
