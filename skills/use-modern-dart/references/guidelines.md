# Dart

## Language gates

- Null safety: Dart 2.12+ with an enabled language target; required in Dart 3. Prefer nullable types/promotion over unchecked ! or late initialization.
- Dart 3: records, patterns, exhaustive switch expressions and sealed/base/final/interface modifiers for explicit library contracts.
- 3.10: dot shorthands when contextual types make the member unambiguous.
- 3.12: private named parameters for library-private contracts.
- 3.13: primary constructors for clear initialization; ordinary constructors for complex validation. Check changed promotion diagnostics and language-versioned formatting. Wasm deferred loading and native-library tree-shaking are platform/build decisions.

## Libraries and async

- Use final/const and typed literals; public APIs follow Effective Dart and /// documentation. Avoid other packages' src/ imports.
- Validate/narrow dynamic boundary data; types do not validate input.
- Own Future/Stream errors, subscriptions and cancellation; long-lived callbacks need an owner.
- Run configured dart format/analyze; preserve analysis_options rather than adding another lint package.

## Sources

- [Effective Dart](https://dart.dev/effective-dart)
- [Dart 3.13 announcement](https://dart.dev/blog/announcing-dart-3-13)
- [Dart language specification](https://spec.dart.dev/)
- [Dart null safety](https://dart.dev/null-safety/understanding-null-safety)
- [Dart analyzer lints](https://dart.dev/tools/linter-rules)
