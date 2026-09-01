---
name: use-modern-jetpack-compose
description: "Use version-aware Jetpack Compose state, recomposition, side-effect, architecture, accessibility, and UI testing idioms when writing, modifying, fixing, or reviewing Compose code."
---

# Modern Jetpack Compose

Use for Jetpack Compose UI and state-holder code. Pair with use-modern-kotlin
for Kotlin rules and the project's Android architecture conventions.

## Target resolution

Read Gradle version catalogs, Android Gradle Plugin, Kotlin, Compose BOM/compiler
or plugin, min/target SDK, and the Android architecture already used. Do not
mix Compose APIs from incompatible BOM or compiler lines.

## Working rules

- Keep composables side-effect free and cheap to recompose. Use effect APIs
  with lifecycle-aware keys for external work.
- Prefer unidirectional data flow: immutable state flows down and events flow
  up. Hoist state to the lowest common owner that must read or change it.
- Use remember for composition-scoped state and rememberSaveable for small UI
  state that must survive recreation; keep business state in the project's
  supported state holder or ViewModel.
- Do not store mutable, non-observable collections as Compose state. Expose
  immutable values and explicit event callbacks.
- Give lazy lists and navigation destinations stable keys and identity; avoid
  using positions for entities that can be inserted or reordered.
- Collect flows with the lifecycle-aware API supported by the project's
  dependencies, and measure recomposition or frame problems before optimizing.

Read references/guidelines.md before using version-sensitive Compose runtime,
Material, navigation, or lifecycle APIs.
