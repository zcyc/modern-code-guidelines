# Jetpack Compose

## Compiler and platform gates

- Kotlin 2.0+ uses the Compose Compiler Gradle plugin versioned with Kotlin; earlier targets use the compiler-extension configuration. BOM versions libraries, not the compiler.
- Check AGP/Kotlin/BOM plus lifecycle/navigation/Material library versions and Android min SDK; matching Kotlin alone does not establish API availability.

## State and effects

- Render without side effects; LaunchedEffect/DisposableEffect/SideEffect own external work with lifecycle keys. Hoist immutable state to the lowest common owner and pass events upward.
- remember is composition-local; rememberSaveable stores small recreatable UI values; ViewModel/state holders own business state.
- Mutating an ordinary ArrayList is not observable state. Use immutable replacements or observable state holders.
- Collect flows through supported lifecycle-aware APIs; cancel composition-owned work on exit. Stable list/navigation keys preserve identity.
- Measure frames/recomposition before stability annotations/caching; test UI semantics and state restoration where changed.

## Sources

- https://developer.android.com/develop/ui/compose/architecture
- https://developer.android.com/develop/ui/compose/state
- https://developer.android.com/develop/ui/compose/state-hoisting
- https://developer.android.com/develop/ui/compose/side-effects
- https://developer.android.com/topic/architecture
