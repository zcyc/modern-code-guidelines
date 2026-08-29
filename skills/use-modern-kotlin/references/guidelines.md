# Kotlin version rules

Use these rules after resolving the Kotlin language/API version and platform
target. Coroutines are a library facility, not a Kotlin standard-library API.

## Kotlin 1.4+

- Use null-safe types, safe calls, Elvis expressions, and smart casts instead of
  Java-style null protocols.
- Prefer named arguments, default parameters, extension functions with a clear
  receiver contract, and standard collection operations where they improve use.

## Kotlin 1.5+

- Use `value`/inline classes and unsigned types only when their representation and
  platform interop are part of the design.
- Use sealed interfaces and exhaustive `when` when the domain is intentionally
  closed and the target supports them.

## Kotlin 1.7+

- Use the open-ended range operator `..<` when its language target supports it;
  do not write `0..n - 1` for half-open iteration.

## Kotlin 1.9+

- Use data objects and other stable features only when the module's compiler target
  includes them.

## Kotlin 2.0+

- Treat the K2 compiler as the stable/default compiler line when the project
  toolchain supports it; keep compiler and IDE versions aligned.
- Prefer `enumEntries<T>()` over repeatedly allocating `enumValues<T>()` when
  the enum values are read as a collection.
- Use common `AutoCloseable` APIs only when the selected platform target and
  resource lifetime make the ownership clear.

## Kotlin 2.2+

- Use stable guard conditions, non-local `break`/`continue`, and multi-dollar
  interpolation when they make the control flow or literal contract clearer.
- Treat context parameters and context-sensitive resolution as preview unless the
  selected compiler documents them as stable.
- Prefer `Base64` and `HexFormat` from the standard library when their encoding
  contract matches the project.

## Kotlin 2.3+

- Use stable nested type aliases and data-flow exhaustiveness checks for closed
  domains when they improve the model.
- Use `kotlin.time.Clock`/`Instant` only when the module's target includes them;
  keep UUID generation APIs opt-in until their stability is confirmed.

## Kotlin 2.4+

- Use stable context parameters, explicit backing fields, common `kotlin.uuid.Uuid`,
  and sortedness helpers when they make the API clearer; UUID v4/v7 generation
  remains experimental and requires opt-in.
- Use Java 26 bytecode only when the JVM deployment target and toolchain support it.
- Keep collection literals, explicit context arguments, and Swift export behind the
  feature/platform stability level declared by the project.

## Coroutines

- Launch work in an owned `CoroutineScope`; avoid unstructured global launches.
- Propagate cancellation and use `Flow`/channels only when streaming or
  coordination semantics justify them.

## Authority

- [Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html)
- [What's new in Kotlin 2.0](https://kotlinlang.org/docs/whatsnew20.html)
- [What's new in Kotlin 2.4](https://kotlinlang.org/docs/whatsnew24.html)
- [Kotlin null safety](https://kotlinlang.org/docs/null-safety.html)
- [Kotlin sealed classes and interfaces](https://kotlinlang.org/docs/sealed-classes.html)
- [Kotlin coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html)
