# UIKit

## Availability

- Scenes, diffable data sources and UIHostingController start at iOS/iPadOS 13; check Catalyst/platform variants and individual overloads separately.
- Read availability/main-actor annotations in the selected SDK declaration; compiler availability alone does not satisfy the deployment target.

## Lifecycle and UI

- App delegates own app-wide services; scene delegates/config own per-window lifecycle. Restoration/deep links reconstruct explicit scene values.
- View controllers coordinate views/lifecycle; owned tasks load data and cancel when their owner ends. Repeated callbacks are not an unbounded load scheduler.
- Main actor/thread owns UI mutation; shared model and blocking work need explicit isolation. Diffable data sources use stable domain identifiers.
- Use Auto Layout/safe areas/traits, Dynamic Type, localization and accessibility labels/traits rather than fixed devices.

## SwiftUI interop

- UIViewRepresentable/UIViewControllerRepresentable forwards updates and coordinates ownership/teardown; release delegates/subscriptions and avoid retain cycles.
- UIHostingController embeds SwiftUI with explicit navigation/ownership boundaries.

## Sources

- https://developer.apple.com/documentation/uikit
- https://developer.apple.com/documentation/updates/uikit
- https://developer.apple.com/documentation/swiftui/uikit-integration
- https://developer.apple.com/design/human-interface-guidelines
