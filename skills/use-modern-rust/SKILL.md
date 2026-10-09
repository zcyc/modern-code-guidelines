---
name: use-modern-rust
description: "Use for Rust code and reviews: editions, minimum Rust version, ownership, errors, and unsafe code."
---

# Rust

Resolve the changed file's target from crate/workspace Cargo.toml edition/rust-version (including inherited values), rust-toolchain(.toml), CI and platform. Edition, MSRV and selected toolchain are separate.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
