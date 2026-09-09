# Go version rules

Use these rules after resolving the module's `go` directive and toolchain.
Official Go specifications, release notes, standard-library documentation, and
project configuration are authoritative. [`go-modern-guidelines`](https://github.com/JetBrains/go-modern-guidelines)
is supplementary guidance for modern idioms; when sources differ, follow the
official Go source.

## All supported versions

- Run `gofmt`/`go fmt` for formatting, `go test` for behavior, and `go vet` for
  correctness. `go vet` is not a style checker.
- Prefer early returns, useful zero values, standard-library types, and small
  consumer-owned interfaces.
- Check every error at the point it is produced. Wrap with `%w` when callers need
  to inspect the cause; use `errors.Is` and `errors.As` for wrapped errors.
- Pass `context.Context` explicitly as the first parameter for cancellable work;
  propagate cancellation and never store a context in a long-lived struct.
- Keep goroutine lifetimes explicit. Every goroutine needs an owner, a completion
  path, and a policy for reporting errors.
- Use `crypto/rand` for secrets, `html/template` for HTML, and parameterized
  database APIs for values. Do not use `math/rand` or string-built SQL at a trust
  boundary.
- Write doc comments for exported declarations and keep package names short,
  lower-case, and free of redundant terms.

## Go 1.18+

- Use generics when one implementation genuinely serves multiple types; do not
  replace a clear interface or concrete function with a generic abstraction.

## Go 1.20+

- Use `errors.Join` when one operation must return multiple independent errors;
  preserve a single causal error when that is the actual model.

## Go 1.21+

- Use `min`/`max` instead of hand-written comparisons and `clear` for clearing
  slices or maps when their semantics are exact.
- Prefer `slices.Contains`, `Index`, `Sort`, `Max`, `Min`, `Reverse`, `Compact`,
  `Clip`, and `Clone` over equivalent manual loops.
- Prefer `maps.Clone`, `Copy`, and `DeleteFunc` over equivalent map loops.
- Use `cmp.Or` for ordered fallback values and `sync.OnceFunc`/`OnceValue` for
  one-time initialization when they express the ownership clearly.
- Use `context.AfterFunc` and cause-aware context constructors when cancellation
  needs cleanup or a meaningful cause.
- Use `log/slog` for structured application logging when the project has no
  established logging contract.

## Go 1.22+

- Use `for i := range n` for integer ranges and rely on per-iteration loop
  variables when the module's `go` directive enables the Go 1.22 semantics.
- Prefer the enhanced `net/http.ServeMux` patterns when the project targets Go
  1.22+ and does not already depend on a router with required features.

## Go 1.23+

- Use the `iter` package and range-over-function iterators for reusable lazy
  sequences; use `slices.Collect`, `Sorted`, and related helpers when they make
  allocation and ownership obvious.
- Do not introduce an iterator abstraction for a one-off loop.

## Go 1.24+

- Use `os.OpenInRoot`/`os.Root` for untrusted paths that must stay within a
  directory; do not reconstruct traversal checks manually.
- Use `testing.B.Loop` for benchmarks when the target provides it, and use the
  `omitzero` JSON tag when zero-value omission—not empty-value omission—is the
  intended contract.

## Go 1.25+

- Use `sync.WaitGroup.Go` for the standard add/start/done pattern when its
  lifecycle semantics fit the code.
- Use `testing/synctest` for deterministic tests of concurrent code and virtual
  time when the project target includes it.

## Go 1.26+

- Use `new(value)` for pointers to values and `errors.AsType[T]` for type-safe
  error matching when the module target supports them.

## Go 1.27+

- Use generic methods, promoted/nested field selectors, and generalized generic
  inference only when they make the API or construction clearer; keep explicit
  structure when it communicates ownership or keeps a contract readable.
- Treat the `stdversion` vet check run by `go test` as a compatibility signal:
  fix the module/file Go target or the code instead of suppressing the warning.
- Use `encoding/json/v2`/`jsontext`, `crypto/mldsa`, native `uuid`, or
  `httptest.NewTestServer` when the target and API contract require them; do not
  replace an established API merely because a newer one exists.

## Authority

- [Go language specification](https://go.dev/ref/spec)
- [Effective Go](https://go.dev/doc/effective_go)
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
- [Go release history](https://go.dev/doc/devel/release)
- [Go 1.27 release blog](https://go.dev/blog/go1.27)
- [Go vet](https://go.dev/cmd/vet/)
- [Go test command](https://go.dev/cmd/go/#hdr-Test_packages)
- [JetBrains Modern Go Guidelines (supplementary)](https://github.com/JetBrains/go-modern-guidelines)
