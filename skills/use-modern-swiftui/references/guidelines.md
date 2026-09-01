# SwiftUI version rules

Resolve the Swift, Xcode, SDK, and deployment targets before using a SwiftUI
feature. Availability is determined by the deployment target as well as the
compiler.

## State and identity

- Use the narrowest state owner that can express the data flow. Keep child views
  editing parent state through bindings rather than creating a second copy.
- Use the Observation APIs supported by the target; do not mix old and new
  observation models without an explicit interop boundary.
- Stable identity is part of UI correctness. Use domain identifiers for
  collections and navigation, not indices or regenerated UUIDs.

## Async and platform behavior

- Prefer task-based work that participates in Swift concurrency cancellation.
  Make repeated or parameterized work use a stable task identity.
- Keep UI state updates on the main actor when required by the target, and make
  availability checks explicit for newer OS APIs.
- Treat UIKit/AppKit representables as lifecycle boundaries: forward updates,
  release resources, and avoid retaining views or coordinators accidentally.

## Authority

- https://developer.apple.com/documentation/SwiftUI
- https://developer.apple.com/documentation/swiftui/model-data
- https://developer.apple.com/documentation/swiftui/task
- https://developer.apple.com/documentation/swiftui/foreach
- https://developer.apple.com/design/human-interface-guidelines
