---
name: use-modern-kotlin
description: "Use for Kotlin code and reviews: language versions, platform APIs, and structured coroutines."
---

# Kotlin

Resolve the changed file's target from Gradle/Maven compiler languageVersion/apiVersion and toolchain/CI; JVM/Android/Native/JS/Wasm targets and coroutine-library version.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
