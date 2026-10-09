---
name: use-modern-jetpack-compose
description: "Use for Jetpack Compose code and reviews: state, effects, recomposition, and Android lifecycle."
---

# Jetpack Compose

Resolve the changed file's target from Gradle/version catalogs, Kotlin, AGP, Compose BOM/compiler/plugin, lifecycle/navigation dependencies, min/target SDK and architecture.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-kotlin for language and coroutines.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
