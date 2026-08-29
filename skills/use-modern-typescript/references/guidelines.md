# TypeScript version rules

Use these rules after resolving the project's compiler version and `tsconfig`. Runtime
availability still comes from the JavaScript host; TypeScript only checks and emits.

## TypeScript 4.9+

- Use `satisfies` to validate object/tuple shapes while preserving narrow inference.
- Prefer `unknown` over `any` for values whose shape has not been validated.

```ts
const routes = {
  home: "/",
  settings: "/settings",
} satisfies Record<string, `/${string}`>;
```

## TypeScript 5.0+

- Use `const` type parameters when a generic API must preserve literal inference without `as const` at every call site.
- Use standard decorators only when the project has an explicit decorator runtime/configuration; do not mix legacy and standard decorator semantics.
- Prefer `verbatimModuleSyntax` when the project can make type/value imports explicit.

## TypeScript 5.2+

- Use `using`/`await using` only when the runtime and emitted helper support are part of the project's declared target.
- Use `Symbol.dispose`/`Symbol.asyncDispose` for resource lifetimes only when the resource contract is explicit.

## TypeScript 5.4+

- Use the built-in `NoInfer<T>` when an API must prevent one argument from influencing another argument's inference.
- Keep generic constraints expressive; do not replace a precise constraint with `any` to silence inference errors.

## TypeScript 5.5+

- Let the compiler infer type predicates for straightforward filtering when it produces the correct narrowing.
- Use regular-expression syntax checking as a signal to correct patterns, not as a reason to suppress diagnostics.

## TypeScript 5.6+

- Treat disallowed always-truthy/nullish checks as real bugs unless the code intentionally documents the invariant.
- Use iterator helper types only when the runtime target also provides the iterator helpers.

## TypeScript 5.9+

- Use newer module syntax only when the selected module target, bundler, and runtime agree; compiler acceptance alone is insufficient.
- Keep declaration output stable for library packages and test it under the package's actual consumer target.

## TypeScript 6+

- Read the TypeScript 6 release notes before changing compiler options: this release contains breaking changes and deprecations preparing for TypeScript 7.
- Set `target`/`lib` to `es2025` only when the runtime provides those APIs; this
  enables the corresponding standard-library types but does not polyfill them.
- Use `RegExp.escape` when the selected runtime supports it instead of hand-written
  regular-expression escaping.
- Address deprecated `target: "es5"`, `moduleResolution: "node"`, `baseUrl`,
  `outFile`, and related options directly; do not preserve them with a new
  compatibility shim.
- Remove deprecated compiler options rather than adding compatibility shims or suppressions.

## TypeScript 7+

- Treat TypeScript 7 as the current compiler line; do not preserve options or
  constructs deprecated by TypeScript 6 with compatibility shims.
- Expect `strict`, `module: "esnext"`, `noUncheckedSideEffectImports`, and
  stable type ordering defaults; make project intent explicit when the defaults
  do not fit.
- Do not depend on the TypeScript 7 compiler API; choose the supported API or
  remove the integration rather than adding a local compatibility facade.
- Pin the compiler and editor language service together when CI and local
  diagnostics must agree.

## Configuration defaults for new projects

- Start new application projects with `strict: true`, an explicit `target`, an explicit `module`, and an explicit `moduleResolution` appropriate to the runtime.
- Add `noUncheckedIndexedAccess` when indexed access can cross a trust boundary or when the project benefits from explicit absence handling.
- Keep `exactOptionalPropertyTypes` as a deliberate project choice; enable it when optional-versus-undefined semantics matter.

## Authority

- [TypeScript release notes](https://www.typescriptlang.org/docs/handbook/release-notes/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)
- [TSConfig reference](https://www.typescriptlang.org/tsconfig/)
- [TypeScript 5.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html)
- [TypeScript 6.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)
- [Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
