# Flutter version rules

Resolve the Flutter and Dart SDK constraints from pubspec.yaml and the lockfile
before using new widgets, APIs, or platform behavior. Check the target platform
when a feature crosses into native code.

## UI and state

- Widgets are immutable descriptions. Keep build pure and cheap; do not start
  requests, timers, or subscriptions from build.
- Prefer the project's existing state-management package. Flutter's architecture
  guidance is a useful default, not a reason to add a domain layer everywhere.
- Every controller, listener, stream subscription, and animation resource needs
  one clear owner and a matching dispose path.
- Preserve widget identity deliberately with keys, especially in reorderable or
  dynamically inserted lists.

## Performance and platform boundaries

- Measure frame or memory problems before adding isolates, caches, or custom
  render objects.
- Keep platform channels narrow and typed. Handle platform availability and
  failure explicitly instead of assuming every target implements the API.

## Authority

- https://docs.flutter.dev/resources/architectural-overview
- https://docs.flutter.dev/app-architecture/guide
- https://docs.flutter.dev/data-and-backend/state-mgmt/intro
- https://docs.flutter.dev/perf
- https://docs.flutter.dev/ui/accessibility-and-internationalization
