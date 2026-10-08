---
name: use-modern-rust
description: "Use when writing or reviewing code involving Rust editions, MSRV, ownership, errors, and unsafe boundaries."
---

# Rust

Resolve the changed file's target from crate/workspace Cargo.toml edition/rust-version (including inherited values), rust-toolchain(.toml), CI and platform. Edition, MSRV and selected toolchain are separate.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
