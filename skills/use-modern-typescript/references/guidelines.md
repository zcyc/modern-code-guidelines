# TypeScript

## Compiler gates

- 4.9: satisfies checks assignability while retaining useful inference; it does not universally freeze literals. Prefer unknown and runtime narrowing at trust boundaries; reserve any for documented interop.
- 5.0: const type parameters and verbatimModuleSyntax; decorators require explicit standard vs legacy runtime/configuration semantics.
- 5.2: using/await using and dispose symbols require runtime/helper support plus explicit resource lifetimes.
- 5.4: NoInfer controls which arguments drive inference; retain precise constraints.
- 5.5: inferred predicates and regex syntax checks; verify actual narrowing.
- 5.6: always-truthy/nullish diagnostics reveal likely bugs; iterator helper types still need runtime APIs.
- 5.9: newer module syntax requires matching module/bundler/runtime; check declaration output against actual consumer targets.
- 6: review breaking/deprecated options before upgrades; es2025 lib/target does not polyfill runtime APIs. RegExp.escape is a runtime gate. Replace deprecated es5/node resolution/baseUrl/outFile options through an explicit migration, not new shims/suppressions.
- 7: remove constructs/options dropped after 6. Defaults include strict, module esnext, noUncheckedSideEffectImports and stable type ordering; keep compiler/editor diagnostics aligned. Compiler integrations must use the release's supported API; do not assume the former compiler API is available.
- 7: types defaults to [] and rootDir to ./; explicitly select required ambient packages (e.g. node/jest) and verify emitted directory paths against package exports, entry points and deployment scripts during upgrades.

## Contracts

- Model finite states with discriminated unions/exhaustive checks. Avoid unchecked casts/non-null assertions; validate missing invariants.
- New apps use strict and explicit runtime-appropriate target/module/moduleResolution. noUncheckedIndexedAccess exposes indexed absence; exactOptionalPropertyTypes distinguishes missing from undefined.
- Respect effective inherited tsconfig and module/export/declaration contracts; type-only imports follow verbatimModuleSyntax. TypeScript types do not validate input or supply JavaScript APIs.

## Sources

- [TypeScript release notes](https://www.typescriptlang.org/docs/handbook/release-notes/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)
- [TSConfig reference](https://www.typescriptlang.org/tsconfig/)
- [TypeScript 5.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html)
- [TypeScript 6.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)
- [Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
