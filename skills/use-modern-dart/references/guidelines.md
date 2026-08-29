# Dart version rules

Use these rules after resolving the package's SDK constraint and analyzer config.
The Dart SDK target and Flutter/plugin API targets remain separate.

## Dart 2+

- Use sound null safety when the package target enables it. Prefer promotion and
  explicit validation to force-unwrapping nullable values.
- Use `final` for bindings that do not change and `const` when the value can be a
  compile-time constant.

## Dart 3+

- Use records and patterns for small structural values, and sealed/base/final/
  interface class modifiers when they express the intended library boundary.
- Use exhaustive `switch` expressions for finite domains; keep pattern matching
  readable rather than replacing a simple conditional with a puzzle.

## Dart 3.10+

- Use dot shorthands only when the surrounding type context makes the referenced
  enum value, static member, or constructor unambiguous.

## Dart 3.12+

- Use private named parameters only for deliberate library-private contracts; do
  not expose implementation-only names as public API.

## Dart 3.13+

- Use primary constructors when they keep fields, initialization, and invariants
  clear; use an ordinary constructor when initialization or validation is complex.
- Keep `dart format` and its language-versioned style changes aligned with the
  package SDK constraint.
- Treat WebAssembly deferred loading and native-library tree-shaking as explicit
  platform/build features, not general language style rules.
- Recheck analyzer diagnostics involving type promotion after a Dart 3.13
  upgrade; keep promoted values local and immutable when aliasing or mutation can
  invalidate the promotion.

## All supported versions

- Prefer collection literals, interpolation, `Iterable` operations, and explicit
  `Future`/`Stream` lifetimes over manual boilerplate.
- Keep public API documentation in `///` comments and do not import another
  package's `src/` libraries.
- Treat the project's `analysis_options.yaml` as the lint source of truth; do not
  add a new lint package for a local style preference.

## Authority

- [Effective Dart](https://dart.dev/effective-dart)
- [Dart 3.13 announcement](https://dart.dev/blog/announcing-dart-3-13)
- [Dart language specification](https://spec.dart.dev/)
- [Dart null safety](https://dart.dev/null-safety/understanding-null-safety)
- [Dart analyzer lints](https://dart.dev/tools/linter-rules)
