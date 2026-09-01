---
name: use-modern-flutter
description: "Use version-aware Flutter widget, state, architecture, platform-integration, and performance idioms when writing, modifying, fixing, or reviewing Flutter code."
---

# Modern Flutter

Use for Flutter applications and packages. Pair with use-modern-dart for Dart
language rules.

## Target resolution

Read pubspec.yaml, pubspec.lock, the Dart SDK constraint, Flutter SDK channel or
version, target platforms, and the state-management packages already used.
Do not introduce a second state-management approach just because it is popular.

## Working rules

- Keep build methods fast, deterministic, and free of I/O or unrelated side
  effects. Move asynchronous work to an explicit state owner.
- Give state a clear owner: local widget state for local interaction, shared
  state through the project's established mechanism, and durable data behind a
  repository or service boundary.
- Dispose controllers, focus nodes, streams, and subscriptions at the owner
  that created them. Guard async UI updates after the widget is unmounted.
- Use keys when widget identity must survive reordering or preserve state; do
  not add keys mechanically.
- Keep CPU-heavy work off the UI isolate when measurement shows it can block
  frames; use platform APIs explicitly for platform-specific behavior.
- Follow the project's accessibility, localization, and responsive-layout
  conventions rather than hard-coding one device's assumptions.

Read references/guidelines.md before using version-gated Flutter APIs or
architecture recommendations.
