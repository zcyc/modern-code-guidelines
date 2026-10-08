---
name: use-modern-kotlin
description: "Use when writing or reviewing code involving Kotlin language versions, platform APIs, and structured coroutines."
---

# Kotlin

Resolve the changed file's target from Gradle/Maven compiler languageVersion/apiVersion and toolchain/CI; JVM/Android/Native/JS/Wasm targets and coroutine-library version.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
