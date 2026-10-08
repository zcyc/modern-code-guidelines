# Flutter

## API availability

- Check the selected SDK's API docs/source and release migration notes before adopting a widget/API; latest online examples may target a newer SDK. Verify plugin constraints and platform implementations independently.
- After awaiting, verify the owning State/BuildContext is mounted before UI access; use the API available in the selected SDK. disposed ownership cannot be revived by a mounted check.

## State and resources

- build describes immutable UI; start requests/timers/subscriptions in an owned lifecycle/state boundary. Keys preserve identity for dynamic/reordered children.
- Keep existing state management; durable data belongs behind the established repository/service boundary. Extra domain layers need actual complexity.
- Dispose controllers, focus nodes, listeners, animations and subscriptions at their owner; cancel work when possible rather than relying only on mounted checks.
- Measure frame/memory costs before isolates/caches/render objects. Typed platform channels must report unsupported APIs/failure.
- Verify accessibility, localization and responsive layout on supported platforms.

## Sources

- https://docs.flutter.dev/resources/architectural-overview
- https://docs.flutter.dev/app-architecture/guide
- https://docs.flutter.dev/data-and-backend/state-mgmt/intro
- https://docs.flutter.dev/perf
- https://docs.flutter.dev/ui/accessibility-and-internationalization
- [SDK migration notes](https://docs.flutter.dev/release/breaking-changes)
- [Mounted contexts](https://api.flutter.dev/flutter/widgets/BuildContext/mounted.html)
