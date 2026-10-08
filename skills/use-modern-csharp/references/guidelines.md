# C# and .NET

## Language gates

- C# 8: nullable references, switch expressions, property patterns, ranges/indices, using declarations and async streams; propagate stream cancellation.
- C# 9: records/init, relational/logical patterns and small top-level entry points.
- C# 10: file-scoped namespaces, global usings, constant interpolation and improved lambda inference. Keep project-wide style migrations separate.
- C# 11: raw strings, list patterns, required members, u8 literals for UTF-8 consumers and static abstract interfaces/generic math for genuine numeric abstractions.
- C# 12: primary constructors and collection expressions with clear initialization/allocation semantics; interceptors require explicit preview support.
- C# 13: params collections, System.Threading.Lock (also framework-gated) and ref-struct improvements for explicit lifetime contracts.
- C# 14: extension members, null-conditional assignment, field-backed properties, partial events/constructors, span conversions, compound-assignment operators, unbound generics in nameof and modifiers on simple lambda parameters. Keep mutation/lifetime semantics visible.
- C# 15: preview compiler/SDK only.

## Runtime boundaries

- Nullable diagnostics express invariants; repair the invariant instead of adding !. Records fit value-like immutable data; IAsyncEnumerable fits streamed results.
- Pass CancellationToken through cancellable I/O; await end to end. async void is for event callbacks only.
- Use DateTimeOffset for instants; TimeProvider needs .NET 8+. Reuse HttpClient or the project's client factory/lifetime.
- Span/Memory optimizations need an allocation/copying reason. ConfigureAwait(false) depends on synchronization-context requirements, not blanket style.

## Sources

- [Microsoft C# version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history)
- [Microsoft C# 15 preview](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15)
- [Microsoft C# language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning)
- [Microsoft C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)
- [.NET API browser](https://learn.microsoft.com/en-us/dotnet/api/)
