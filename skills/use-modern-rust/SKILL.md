---
name: use-modern-rust
description: Use version-aware Rust language, standard-library, ownership, and concurrency idioms when writing, modifying, fixing, or reviewing Rust code.
---

# Modern Rust

Apply stable Rust patterns supported by the crate's declared toolchain and
edition. Read `references/guidelines.md` before using edition-gated syntax or
APIs.

## Target resolution

Read the effective target for the crate:

1. `Cargo.toml` `rust-version` (MSRV) and `edition`.
2. A checked-in `rust-toolchain.toml`, `rust-toolchain`, or explicit compiler
   target in CI/build scripts.
3. The selected workspace package when the repository contains multiple crates.

`rust-version` and the installed compiler are separate constraints. If either
target is unknown, report it and avoid version-gated syntax or APIs. Do not infer
the target from the local compiler.

## Working rules

- Run the project's `cargo fmt` and `cargo clippy` configuration; do not invent a
  stricter lint policy for an unrelated change.
- Prefer ownership and borrowing that make lifetimes obvious; use slices and
  `&str` for borrowed inputs instead of owning `Vec`/`String` parameters.
- Model recoverable absence and failure with `Option` and `Result`; do not use
  `unwrap`, `expect`, or `panic!` on recoverable input or I/O paths.
- Prefer standard-library types, iterators, and combinators when they stay clearer
  than a manual loop; avoid collecting only to iterate again.
- Use enums for finite states and derive standard traits when their semantics fit.
- Keep `unsafe` blocks small and document the invariant that makes each block safe.
- Use async/concurrency patterns from the project's runtime and preserve structured
  cancellation and error propagation.
