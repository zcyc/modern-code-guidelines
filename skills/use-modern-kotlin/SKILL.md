---
name: use-modern-kotlin
description: Use version-aware Kotlin language, null-safety, standard-library, and coroutine idioms when writing, modifying, fixing, or reviewing Kotlin code.
---

# Modern Kotlin

Apply stable Kotlin features supported by the module's declared compiler and
platform targets. Read `references/guidelines.md` before using version-gated
language or library features.

## Target resolution

Read the effective target for the module:

1. Kotlin compiler `languageVersion` and `apiVersion` in Gradle/Maven build files.
2. JVM/Android/Native/JS/Wasm target settings, which are separate from the Kotlin
   language version.
3. A checked-in toolchain or explicit compiler target in CI.

If the target is unknown, report it and avoid version-gated syntax or APIs. Do not
infer the target from the local IDE or installed compiler.

## Working rules

- Prefer `val` and immutable collection interfaces; use `var` only for real state
  changes and expose the narrowest mutable type.
- Use nullable types deliberately and handle them with smart casts, `?.`, `?:`,
  and explicit validation. Keep `!!` at a proven invariant only.
- Use data classes for data, sealed hierarchies for finite domains, and exhaustive
  `when` expressions for domain branching.
- Prefer direct expressions and standard-library operations when they remain
  readable; do not build long chains of scope functions or collection operators.
- Use coroutines only through the project's declared coroutine library; preserve
  structured concurrency, cancellation, and dispatcher ownership.
- Follow the repository's Kotlin formatter and compiler warnings; keep public
  return/property types explicit when inference could change the API.
