---
name: use-modern-csharp
description: "Use version-aware C# language and .NET idioms when writing, modifying, fixing, or reviewing C# code."
---

# Modern C#

Apply stable C# features supported by the project's declared compiler/SDK and target
framework. Read `references/guidelines.md` before using version-gated syntax or APIs.

## Target resolution

Read the effective project metadata for the file being changed:

1. `LangVersion`, `TargetFramework`/`TargetFrameworks`, `Nullable`, and
   `ImplicitUsings` after considering the `.csproj`, `Directory.Build.props`/
   `Directory.Build.targets`, and any project-specific overrides.
2. The selected SDK from a checked-in `global.json`.
3. An explicit SDK/compiler target in checked-in CI or build scripts.

The language version and target framework are separate constraints: the compiler may
accept syntax whose runtime/library API is unavailable. If either target is unknown,
report it and avoid version-gated syntax or APIs. Never infer the SDK from the local
machine.

Preview features require an explicit `LangVersion`/preview configuration and must be
labeled as preview. Do not add preview features to ordinary production code.

## Working rules

- Keep nullable reference types enabled when the project enables them; fix the nullability invariant instead of adding `!`.
- Prefer records for value-like immutable data, pattern matching for finite domains, and `IAsyncEnumerable<T>` for streamed async results.
- Pass `CancellationToken` through genuinely cancellable I/O and honor it; do not add token parameters to unrelated synchronous code.
- Use `DateTimeOffset` for instants and `TimeProvider` for testable time when the target framework provides it.
- Use `Span<T>`/`Memory<T>` only where allocation or copying is a measured concern; keep ordinary code readable.
- Keep project-wide `global using`/file-scoped namespace changes separate from a local behavioral fix.
