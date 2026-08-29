---
name: use-modern-swift
description: Use version-aware Swift language, API-design, value-semantics, and concurrency idioms when writing, modifying, fixing, or reviewing Swift code.
---

# Modern Swift

Apply stable Swift features supported by the file's declared Swift language mode
and deployment targets. Read `references/guidelines.md` before using version- or
platform-gated syntax and APIs.

## Target resolution

Read the effective target for the package/target:

1. `swift-tools-version` and target settings in `Package.swift`.
2. `SWIFT_VERSION`, deployment targets, and concurrency settings in Xcode/
   `.xcconfig` files.
3. Explicit `swiftc -swift-version` and platform targets in CI/build scripts.

Language mode, SDK availability, and deployment target are separate constraints.
If any relevant target is unknown, report it and avoid gated features or APIs. Do
not infer the target from the installed Xcode or Swift toolchain.

## Working rules

- Prefer structs and enums with value semantics; use classes and actors when
  identity or shared mutable state is part of the model.
- Use optionals to model absence, `guard` for early exits, and exhaustive enums;
  keep `!` and `try!` at documented invariants only.
- Design public APIs for clarity at the call site and keep access control narrow.
- Use `async`/`await` for asynchronous flow. Protect shared mutable state with
  actors or the project's established isolation mechanism.
- Treat `Sendable` as a real cross-isolation contract; do not silence diagnostics
  with `@unchecked Sendable` without an audited invariant.
- Use `swift-format` or the repository's lint configuration rather than adding a
  new formatting policy to an unrelated change.
