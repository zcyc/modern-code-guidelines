# Kotlin

## Language/library gates

- Null-safe types, smart casts, named/default arguments and extensions predate 1.4; keep receiver and public result contracts explicit.
- 1.5: value classes, stable unsigned types and sealed interfaces; verify platform representation/interop.
- ..<: experimental in 1.7.20, syntax stable in 1.8, related standard-library APIs stable in 1.9. Use until on earlier stable targets.
- 1.9: data objects.
- 2.0: default K2, enumEntries<T>() and common AutoCloseable; check target platform.
- 2.2: stable when guards, non-local break/continue, multi-dollar strings, Base64 and HexFormat. Context parameters/resolution require the selected release's stability status.
- 2.3: stable nested aliases, data-flow exhaustiveness and kotlin.time.Clock/Instant; UUID generation remains opt-in until documented stable.
- 2.4: stable context parameters, explicit backing fields, common Uuid and sortedness helpers; UUID v4/v7 generation remains experimental. Java 26 bytecode requires a matching JVM/toolchain. Collection literals, explicit context arguments and Swift export follow their documented stability level.

## Concurrency and APIs

- Kotlin read-only collections are not necessarily immutable; protect shared mutation. Prefer val and finite sealed domains with exhaustive when.
- Coroutines are a separate library: own scopes/dispatchers, propagate cancellation and avoid GlobalScope. Flow/channels need streaming/coordination semantics.
- Keep chains of scope/collection functions readable; follow existing formatter/compiler diagnostics rather than broad suppressions.

## Sources

- [Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html)
- [What's new in Kotlin 2.0](https://kotlinlang.org/docs/whatsnew20.html)
- [What's new in Kotlin 2.4](https://kotlinlang.org/docs/whatsnew24.html)
- [Kotlin null safety](https://kotlinlang.org/docs/null-safety.html)
- [Kotlin sealed classes and interfaces](https://kotlinlang.org/docs/sealed-classes.html)
- [Kotlin coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html)
- [Range stabilization](https://kotlinlang.org/docs/whatsnew19.html#stable-operator-for-open-ended-ranges)
