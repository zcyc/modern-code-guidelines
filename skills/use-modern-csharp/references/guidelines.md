# C# version rules

Use these rules after resolving the explicit `LangVersion` and target framework. A
language feature can compile while its supporting .NET API is unavailable, so check
both constraints.

## C# 8+

- Enable nullable reference types for new projects and treat warnings as design feedback.
- Use switch expressions, property/relational patterns, ranges, indices, using declarations, and `IAsyncEnumerable<T>` where they make control flow clearer.
- Use `await foreach` for asynchronous streams and propagate cancellation when the source supports it.

## C# 9+

- Use records and init-only setters for value-like immutable data.
- Use top-level statements only for small executable entry points; keep library structure explicit.
- Prefer pattern matching and relational patterns over type tests followed by casts.

## C# 10+

- Use file-scoped namespaces for files with one namespace.
- Use global usings for stable project-wide dependencies, not for one-off local convenience.
- Use constant interpolated strings and improved lambda/type inference when they make the contract clearer.

## C# 11+

- Use raw string literals for multi-line JSON, SQL, regular expressions, and other embedded text when escaping would obscure content.
- Use list patterns for finite sequence shapes and required members when construction must establish an invariant.
- Use UTF-8 string literals (`u8`) only at APIs that explicitly consume UTF-8 data.
- Use static abstract interface members/generic math only when the abstraction is genuinely numeric and the target supports it.

## C# 12+

- Use primary constructors when constructor parameters naturally define the type's initialization contract.
- Use collection expressions (`[...]`) when the target type and allocation behavior are clear.
- Do not use preview interceptors in production code.

## C# 13+

- Use `params` collections when the API should accept a collection shape rather than force an array allocation.
- Use the new `System.Threading.Lock` pattern only when the target framework provides it; do not replace every existing lock without a reason.
- Prefer the language's improved `ref struct` support only in low-level APIs that already have a clear lifetime contract.

## C# 14+

- Use extension members when a group of extension properties/methods belongs to one coherent extension surface.
- Use null-conditional assignment only when the skipped assignment semantics are intended.
- Use `field`-backed properties and partial events/constructors only when they remove real boilerplate without hiding lifecycle behavior.
- Use implicit `Span<T>`/`ReadOnlySpan<T>` conversions only when the API is
  already span-oriented and the lifetime/allocation behavior remains obvious.
- Use user-defined compound assignment operators only when the type's mutation
  semantics are unsurprising and consistent with its ordinary operator.
- Use unbound generic types in `nameof` when the type name—not a constructed
  generic shape—is the intended diagnostic or API text.
- Use modifiers on simple lambda parameters only when they make the delegate's
  by-reference contract clearer than an explicit parameter type.

## C# 15 (preview)

- Treat C# 15 features as preview: use them only with an explicit preview
  compiler/SDK configuration and label them as preview; do not introduce them into
  ordinary production code.

## .NET API rules

- Prefer `HttpClientFactory`/the project's established client lifetime over creating a new `HttpClient` per request.
- Prefer `TimeProvider` over reading wall-clock time directly in code that needs deterministic tests.
- Do not use `ConfigureAwait(false)` as a blanket style rule; apply it only when the synchronization-context contract requires it.
- Avoid `async void` except for event handlers whose caller cannot observe a task.

## Authority

- [Microsoft C# version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history)
- [Microsoft C# 15 preview](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15)
- [Microsoft C# language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning)
- [Microsoft C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)
- [.NET API browser](https://learn.microsoft.com/en-us/dotnet/api/)
