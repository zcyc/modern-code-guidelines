# Rust version rules

Use these rules after resolving the crate's `edition`, `rust-version`, and
toolchain. `rustfmt` and Clippy are the executable checks; this file supplies
the decisions that a formatter cannot make.

## All supported editions

- Use `cargo fmt --check` and the repository's configured `cargo clippy` lints.
- Prefer values, borrowing, and standard-library resource types over manual
  lifetime or cleanup protocols.
- Use `Option` for a value that may be absent and `Result` for an operation that
  may fail. Preserve the error context across abstraction boundaries.
- Prefer `&[T]`, `&str`, and generic iterator inputs for borrowed data; return an
  owned value when the function creates or transfers ownership.
- Make unsafe code the smallest possible boundary and state its safety invariant.

## Rust 2018+

- Use the 2018 module and path rules; keep modules and re-exports explicit.
- Prefer `?` for error propagation and exhaustive `match`/`if let` handling of
  `Option` and `Result`.

## Rust 2021+

- Use `IntoIterator` and iterator APIs where they express the operation without
  needless intermediate allocations.
- Prefer `std::array::IntoIter` behavior supplied by the declared edition rather
  than compatibility workarounds.

## Rust 2024+

- Use Rust 2024 semantics only when `edition = "2024"` is declared and the MSRV
  supports them; do not silently change a crate's edition during a local fix.
- Keep the style edition used by `rustfmt` aligned with the repository's config.
- Keep `unsafe` operations inside explicit `unsafe {}` blocks, even within an
  `unsafe fn`, so the unsafe operation and its safety invariant are visible.
- Mark `unsafe extern` declarations and each unsafe foreign item explicitly;
  do not make an entire FFI block unsafe by default.
- Treat `gen` as a reserved keyword in new identifiers; migrate affected names
  or use raw identifiers only at a deliberate boundary.

## Rust 1.98+

- Treat new FFI/runtime-symbol diagnostics as correctness feedback; fix invalid
  declarations and document any deliberate low-level exception instead of
  suppressing `invalid_runtime_symbol_definitions`, `suspicious_runtime_symbol_definitions`,
  or `c_void_returns` diagnostics.
- Use algebraic floating-point operations only when their relaxed numerical
  guarantees are acceptable; retain stricter operations when reproducibility or
  IEEE behavior is part of the contract.
- Use buffered integer formatting APIs when allocation is a measured concern;
  keep ordinary formatting readable rather than optimizing speculatively.

## Authority

- [Rust Edition Guide](https://doc.rust-lang.org/edition-guide/)
- [Rust release notes](https://doc.rust-lang.org/stable/releases.html)
- [Rust Style Guide](https://doc.rust-lang.org/style-guide/)
- [The Cargo Book: rust-version](https://doc.rust-lang.org/cargo/reference/rust-version.html)
- [The Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Clippy Book](https://doc.rust-lang.org/clippy/)
