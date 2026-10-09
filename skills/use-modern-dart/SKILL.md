---
name: use-modern-dart
description: "Use for Dart code and reviews: language features, null safety, async, and analyzer rules."
---

# Dart

Resolve the changed file's target from package pubspec.yaml environment.sdk, workspace overrides, analysis_options.yaml, checked-in Dart/Flutter SDK and platform targets.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Account for per-file // @dart language-version overrides.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
