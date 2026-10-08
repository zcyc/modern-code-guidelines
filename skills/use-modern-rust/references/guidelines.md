# Rust

## Ownership and checks

- Borrow inputs with &[T]/&str when ownership is unnecessary; return owned values when creating/transferring ownership. Use Option/Result and preserve causal context with ?.
- Recoverable input/I/O errors are not unwrap/expect/panic paths. Keep async work within the selected runtime's cancellation/resource model.
- Keep unsafe operations small with documented safety invariants. Run cargo fmt/clippy and behavior tests using project configuration.

## Editions and releases

- 2018: explicit module/path boundaries; ? and Option/Result handling predate this edition.
- 2021: account for array IntoIterator edition semantics; avoid collecting just to iterate again.
- 2024 requires compatible MSRV (1.85+); retain configured rustfmt style edition. Use explicit unsafe blocks inside unsafe fn; gen is reserved.
- Rust 2024 requires unsafe extern blocks. The author guarantees declaration signatures; foreign items default to unsafe to call. Mark an item safe only when every allowed call is safe; marking the block unsafe does not make its items safe.
- 1.98: fix runtime-symbol/FFI diagnostics (invalid_runtime_symbol_definitions, suspicious_runtime_symbol_definitions, c_void_returns). Algebraic float operations require acceptance of relaxed guarantees; buffered integer formatting needs measured allocation benefit.

## Sources

- [Rust Edition Guide](https://doc.rust-lang.org/edition-guide/)
- [Rust release notes](https://doc.rust-lang.org/stable/releases.html)
- [Rust Style Guide](https://doc.rust-lang.org/style-guide/)
- [The Cargo Book: rust-version](https://doc.rust-lang.org/cargo/reference/rust-version.html)
- [The Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [The Clippy Book](https://doc.rust-lang.org/clippy/)
- [Unsafe extern blocks](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-extern.html)
