---
name: use-modern-flutter
description: "Use for Flutter code and reviews: widgets, state, lifecycle, and platform integration."
---

# Flutter

Resolve the changed file's target from pubspec.yaml/lockfile, Dart constraint, pinned Flutter SDK/channel, target platforms and existing state-management packages.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-dart for language and analyzer rules.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
