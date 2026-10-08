# Go

## Ownership and checks

- Check errors immediately; wrap causal errors with %w and inspect with errors.Is/As/AsType. errors.Join fits independent failures.
- Pass context.Context first for cancellable work; propagate cancellation instead of storing contexts in long-lived structs. Each goroutine needs an owner, exit and error path.
- Prefer useful zero values, early returns and consumer-owned small interfaces. Generics need real reuse across types.
- Use crypto/rand for secrets, html/template for HTML and SQL parameters for values; document exported APIs.
- Run gofmt, go test and go vet; go vet checks correctness, not style. Use go test -race for shared-state changes on supported platforms. Existing staticcheck/golangci-lint only; go fix -diff is an intentional modernization tool on Go 1.26+.

## API gates

- 1.18: generics.
- 1.20: errors.Join and cancellation causes.
- 1.21: min/max/clear, slices helpers, maps.Clone/Copy/DeleteFunc, sync.OnceFunc/OnceValue, context.AfterFunc and log/slog.
- 1.22: cmp.Or (first non-zero value), integer range, enhanced http.ServeMux; module/file go target controls per-iteration loop-variable semantics.
- 1.23: iter/range-over-function, slices.Collect/Sorted; avoid an iterator abstraction for a one-off loop.
- 1.24: os.Root/OpenInRoot for directory-confined untrusted paths, testing.B.Loop and JSON omitzero (different from omitempty).
- 1.25: WaitGroup.Go for owned add/start/done lifetimes; testing/synctest for deterministic concurrent/time tests.
- 1.26: new(value), errors.AsType[T].
- 1.27: generic methods, promoted/nested struct-literal keys and generalized inference; encoding/json/v2, encoding/json/jsontext, crypto/mldsa, uuid and httptest.NewTestServer. Choose APIs by contract, especially JSON semantic changes.
- 1.27 go test runs stdversion vet checks; fix target/API mismatches instead of suppressing them.

Official Go docs override supplementary JetBrains guidance.

## Sources

- [Go language specification](https://go.dev/ref/spec)
- [Effective Go](https://go.dev/doc/effective_go)
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
- [Go release history](https://go.dev/doc/devel/release)
- [Go 1.27 release blog](https://go.dev/blog/go1.27)
- [Go vet](https://go.dev/cmd/vet/)
- [Go test command](https://go.dev/cmd/go/#hdr-Test_packages)
- [JetBrains Modern Go Guidelines (supplementary)](https://github.com/JetBrains/go-modern-guidelines)
- [Go 1.22: cmp.Or](https://go.dev/doc/go1.22#cmp)
