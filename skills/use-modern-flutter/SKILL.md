---
name: use-modern-flutter
description: "Use when writing or reviewing code involving Flutter widgets, state, lifecycle, and platform integration."
---

# Flutter

Resolve the changed file's target from pubspec.yaml/lockfile, Dart constraint, pinned Flutter SDK/channel, target platforms and existing state-management packages.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-dart for language and analyzer rules.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
