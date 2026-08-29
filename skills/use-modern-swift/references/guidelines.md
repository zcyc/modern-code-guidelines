# Swift version rules

Use these rules after resolving the Swift language mode, SDK, and deployment
target. A compiler feature can be available while the corresponding platform API
is unavailable.

## Swift 5+

- Prefer value types for data, protocol requirements that express real behavior,
  and standard collection algorithms over hand-written indexing.
- Use `guard`, optional binding, and typed errors instead of force-unwrapping
  values that came from input, I/O, or a platform API.
- Follow Swift API Design Guidelines: optimize for clarity at the point of use,
  not merely short declarations.

## Swift concurrency

- Use structured tasks and `async`/`await`; make cancellation observable in long
  operations.
- Use actors for isolated shared mutable state and mark cross-isolation values
  `Sendable` only when their semantics satisfy the protocol.
- Keep `@MainActor` for UI/main-thread ownership, not as a blanket workaround for
  concurrency diagnostics.

## Swift 5.9+

- Use macros, parameter packs, and other newer features only when the target and
  project toolchain explicitly support them; do not introduce them for small
  boilerplate reductions.

## Swift 6 language mode

- Treat strict concurrency diagnostics as design feedback. Fix isolation and
  sendability at the boundary instead of suppressing the diagnostic.

## Swift 6.2+

- Use `@concurrent` only for work that must leave the actor or caller executor;
  keep ordinary asynchronous code on the caller's isolation when that is the
  intended ownership model.
- Use `Span` and `InlineArray` for measured contiguous-memory or fixed-size data
  paths; do not replace ordinary collections without a lifetime and allocation
  reason.

## Swift 6.3+

- Use `@c` for deliberate Swift/C boundaries and keep the generated C contract
  reviewed like a public API.
- Use module selectors only to resolve a real import-name collision; do not use
  them to hide ambiguous module ownership.
- Treat Swift Build integration and other 6.3 preview tooling as opt-in; keep
  production builds on the repository's declared build system.

## Authority

- [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/)
- [Swift 6.3 release](https://www.swift.org/blog/swift-6.3-released/)
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html)
- [Swift 6 migration: data-race safety](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/dataracesafety/)
- [Swift Evolution](https://www.swift.org/swift-evolution/)
