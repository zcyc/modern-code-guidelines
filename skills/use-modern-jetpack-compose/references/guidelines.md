# Jetpack Compose version rules

Resolve Kotlin, Android Gradle Plugin, Compose BOM/compiler, lifecycle, and
min/target SDK versions from Gradle before using an API. The BOM and compiler
must be compatible with the project.

## Compiler gate

- Kotlin 2.0 and later use the Compose Compiler Gradle plugin, whose version
  follows Kotlin. Older Kotlin targets use the legacy compiler-extension
  configuration; do not mix the two configuration models in one module.
- Keep Kotlin, AGP, Compose compiler, and Compose BOM compatibility aligned;
  the compiler plugin and BOM solve different compatibility constraints.

## State and recomposition

- Composables should be side-effect free. Use LaunchedEffect, DisposableEffect,
  SideEffect, or other supported effect APIs with keys that match the work's
  lifecycle.
- Hoist state to the lowest common owner that reads or changes it. Expose
  immutable state and event callbacks rather than mutable state objects.
- Use remember for composition lifetime and rememberSaveable for small UI values
  that must survive recreation. Keep business state in the project's supported
  state holder or ViewModel.
- Prefer immutable collections or observable state holders; mutating an
  ArrayList in place does not reliably trigger recomposition.

## Android integration

- Collect flows with the lifecycle-aware API supported by the project's
  dependencies. Preserve cancellation when the screen leaves composition.
- Use stable keys for lazy lists and navigation entities. Measure recomposition
  and frame performance before adding stability annotations or custom caching.

## Authority

- https://developer.android.com/develop/ui/compose/architecture
- https://developer.android.com/develop/ui/compose/state
- https://developer.android.com/develop/ui/compose/state-hoisting
- https://developer.android.com/develop/ui/compose/side-effects
- https://developer.android.com/topic/architecture
