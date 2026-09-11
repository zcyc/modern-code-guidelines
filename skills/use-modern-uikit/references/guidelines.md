# UIKit version rules

Resolve the Swift language mode, Xcode, SDK, deployment target, and Mac Catalyst
target before using version-sensitive UIKit APIs. UIKit availability is a
platform and deployment decision, not just a compiler decision.

## App lifecycle

- Prefer the scene-based lifecycle on targets that support it, and keep
  application-wide services separate from scene-specific UI state.
- Treat view-controller callbacks as lifecycle events, not as a general-purpose
  data-loading scheduler. Start parameterized work with task identity or an
  explicit lifecycle owner and cancel it when the owner goes away.
- Keep restoration and deep-link state in explicit value types rather than hidden
  controller state when the app must restore multiple scenes.

## UI and concurrency

- Keep UIKit mutations on the main actor/main thread required by the API. Move
  blocking or asynchronous work out of the UI path and return results through an
  explicit isolation boundary.
- Prefer diffable data sources and stable item identifiers when collection order
  or membership can change; do not use array positions as identity.
- Use Auto Layout, safe areas, trait collections, Dynamic Type, localization,
  and accessibility labels/traits as part of the feature, not as a later pass.

## SwiftUI interop and availability

- Use representables only at a real platform boundary. Forward SwiftUI updates
  into the UIKit object, avoid retaining coordinators or views unnecessarily,
  and release subscriptions and delegates with the wrapped object's lifecycle.
- Use `UIHostingController` when SwiftUI owns a screen inside UIKit, and keep the
  boundary small enough that ownership and navigation remain obvious.
- Guard newer APIs with the declared deployment target and prefer standard UIKit
  components so supported system appearance changes flow through automatically.

## Authority

- https://developer.apple.com/documentation/uikit
- https://developer.apple.com/documentation/updates/uikit
- https://developer.apple.com/documentation/swiftui/uikit-integration
- https://developer.apple.com/design/human-interface-guidelines
