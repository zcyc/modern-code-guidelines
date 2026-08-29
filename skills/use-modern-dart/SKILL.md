---
name: use-modern-dart
description: Use version-aware Dart language, sound-null-safety, standard-library, and analyzer idioms when writing, modifying, fixing, or reviewing Dart code.
---

# Modern Dart

Apply stable Dart features supported by the package's SDK constraint. Read
`references/guidelines.md` before using language-version-gated features.

## Target resolution

Read the effective target from:

1. `pubspec.yaml` `environment: sdk` for the package containing the file.
2. Workspace/package overrides and `analysis_options.yaml`.
3. The selected Dart/Flutter SDK in checked-in toolchain or CI configuration.

The SDK constraint controls language features; Flutter and platform versions also
control available APIs. If the target is unknown, report it and avoid gated
features. Do not infer it from the local SDK.

## Working rules

- Run the repository's `dart format` and `dart analyze` configuration.
- Keep sound null safety intact; model absence with nullable types and promotion,
  not unchecked `!` or `late` state.
- Prefer `final`, `const`, typed collection literals, and immutable values where
  mutation is not part of the model.
- Use `async`/`await`, `Future`, and `Stream` with explicit error and cancellation
  behavior; do not hide long-lived work in unowned callbacks.
- Avoid `dynamic` at boundaries; validate and narrow untrusted values.
- Follow Effective Dart naming, documentation, usage, and design guidance for
  public libraries; let the analyzer enforce the configured subset.
