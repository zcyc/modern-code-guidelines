---
name: use-modern-jetpack-compose
description: "Use when writing or reviewing code involving Jetpack Compose state, effects, recomposition, and Android lifecycle."
---

# Jetpack Compose

Resolve the changed file's target from Gradle/version catalogs, Kotlin, AGP, Compose BOM/compiler/plugin, lifecycle/navigation dependencies, min/target SDK and architecture.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-kotlin for language and coroutines.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
