---
name: use-modern-java
description: "Use when writing or reviewing code involving Java language versions, JDK APIs, resources, and concurrency."
---

# Java

Resolve the changed file's target from effective Maven/Gradle module: --release (maven.compiler.release/compiler-plugin release) first, then maven.compiler.source/target or Gradle languageVersion/sourceCompatibility/targetCompatibility; inherited build and CI settings. Without --release/equivalent, source/target alone does not constrain JDK APIs.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
