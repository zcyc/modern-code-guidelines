---
name: use-modern-java
description: "Use for Java code and reviews: language versions, JDK APIs, resource ownership, and concurrency."
---

# Java

Resolve the changed file's target from effective Maven/Gradle module: --release (maven.compiler.release/compiler-plugin release) first, then maven.compiler.source/target or Gradle languageVersion/sourceCompatibility/targetCompatibility; inherited build and CI settings. Without --release/equivalent, source/target alone does not constrain JDK APIs.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
