---
name: use-modern-go
description: Use version-aware Go language, standard-library, tooling, error-handling, and concurrency idioms when writing, modifying, fixing, or reviewing Go code.
---

# Modern Go

Apply stable, idiomatic Go features supported by the package's declared Go
version. Read `references/guidelines.md` before using version-gated syntax or APIs.

## Target resolution

Read the effective target for the package being changed:

1. The nearest `go.mod` `go` directive and `toolchain` directive.
2. The selected workspace/module from `go.work` when the repository has multiple
   modules.
3. Explicit Go toolchain, build tags, and target settings in CI/build scripts.

Treat the module's declared Go version as the language and standard-library
compatibility target; the installed toolchain is a separate constraint. If the
target is unknown, report it and avoid version-gated syntax or APIs. Do not infer
the target from the local Go installation.

## Checks

- Use `gofmt`/`go fmt` for mechanical formatting, `go test` for behavior, and
  `go vet` for correctness diagnostics. Run the repository's configured commands
  and scope them to the changed packages when a full-repository run is excessive.
- Use `go test -race` for changes that exercise concurrent shared state when the
  target/platform supports the race detector.
- Use `go fix -diff` only for an intentional modernization pass on Go 1.26+ and
  only after resolving the module's Go version; do not use it as a formatter.
- Run `staticcheck` or `golangci-lint` only when the repository already declares
  them or the user requests them. Do not add a linter dependency for a local fix.

## Source precedence

- Treat the official Go specification, release notes, standard-library
  documentation, and project configuration as authoritative. Use
  `go-modern-guidelines` as supplementary idiomatic guidance; when they differ,
  follow the official Go source.

## Working rules

- Keep the happy path left-aligned with early returns; make zero values useful and
  names short but precise.
- Prefer the standard library and existing package APIs. Define small interfaces at
  the consuming boundary and avoid abstractions with one implementation.
- Check errors immediately, add operation context with `%w`, and use
  `errors.Is`/`errors.As` (or `errors.AsType` when supported) instead of comparing
  wrapped errors or asserting concrete types directly.
- Accept `context.Context` as the first parameter for cancellable operations; do
  not store contexts in structs or discard cancellation.
- Give every goroutine an owner, exit condition, and error path. Choose channels,
  mutexes, or atomics from the actual ownership model rather than habit.
- Reuse `slices`, `maps`, `cmp`, `sync`, `context`, `log/slog`, and other standard
  packages introduced by the resolved Go version instead of hand-written helpers.
- Document exported declarations with Go doc comments, keep comments factual, and
  preserve the package's public API and module boundaries.
