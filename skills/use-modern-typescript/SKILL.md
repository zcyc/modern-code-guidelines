---
name: use-modern-typescript
description: "Use version-aware TypeScript type-system and compiler idioms when writing, modifying, fixing, or reviewing TypeScript code."
---

# Modern TypeScript

Apply TypeScript rules supported by the project's explicit compiler and `tsconfig`.
Use `use-modern-javascript` for runtime JavaScript decisions and
`modern-web-guidance` for browser-platform decisions.

## Target resolution

Read the configuration for the file being changed:

1. The TypeScript compiler package actually selected by the nearest workspace/package
   manager configuration and lockfile. Do not choose an arbitrary version from a
   lockfile containing multiple workspace versions.
2. The nearest `tsconfig.json` or explicitly selected project config.
3. `target`, `lib`, `module`, `moduleResolution`, `strict`, and
   `verbatimModuleSyntax` from that config.

If a monorepo has multiple configs, use the config that actually includes the file.
If the compiler version or config cannot be established, report it as unknown and do
not introduce version-gated syntax. Never use a globally installed `tsc` as the source
of truth.

After resolving the target, read `references/guidelines.md` for the applicable
TypeScript compiler and runtime feature gates.

## Working rules

- Treat types as compile-time contracts: validate untrusted values at runtime.
- Prefer `unknown` at trust boundaries, narrow with type guards, and reserve `any` for a documented interop boundary.
- Use discriminated unions and exhaustive checks for finite state instead of boolean flag combinations.
- Prefer `satisfies` when a value must be checked against a type without losing its inferred literal shape.
- Use type-only imports/exports when `verbatimModuleSyntax` or the module boundary requires them.
- Avoid non-null assertions and unchecked casts; fix the missing invariant or validate it.
- Preserve the project's module/runtime contract. TypeScript syntax does not make a JavaScript API available at runtime.
