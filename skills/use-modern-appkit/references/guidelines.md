# AppKit version rules

Resolve the Swift language mode, Xcode, SDK, and macOS deployment target before
using version-sensitive AppKit APIs. AppKit availability is a platform and
deployment decision, not just a compiler decision.

## Windows, documents, and commands

- Give each window a clear owner, usually a window controller or document
  controller, and make close, restoration, and teardown follow that ownership.
- Use `NSDocumentController` and the document architecture for document-based
  apps instead of duplicating file, undo, autosave, and restoration behavior in
  view controllers.
- Route menu and keyboard commands through the responder chain. Implement menu
  validation from current state and keep command state out of unrelated views.
- Keep state restoration and deep-link state in explicit values when a window or
  document must be reconstructed reliably.

## UI and concurrency

- Keep AppKit mutations on the main actor/main thread required by the API. Move
  blocking or asynchronous work out of the UI path and return results through an
  explicit isolation boundary.
- Prefer Auto Layout, system control metrics, system text sizing where supported,
  localization, and accessibility descriptions/actions over fixed display sizes.
- Use Observation or the target's supported model-data mechanism when it reduces
  manual view invalidation; keep model ownership and availability explicit.

## SwiftUI interop and availability

- Use representables only at a real platform boundary. Forward SwiftUI updates
  into the AppKit object, avoid retaining coordinators or views unnecessarily,
  and release subscriptions and delegates with the wrapped object's lifecycle.
- Use `NSHostingView` or `NSHostingController` when SwiftUI owns part of an
  AppKit interface, and keep the boundary small enough that window ownership and
  navigation remain obvious.
- Guard newer APIs with the declared macOS deployment target and prefer standard
  AppKit components so supported system appearance changes flow through
  automatically.

## Authority

- https://developer.apple.com/documentation/appkit
- https://developer.apple.com/documentation/updates/appkit
- https://developer.apple.com/documentation/swiftui/appkit-integration
- https://developer.apple.com/design/human-interface-guidelines
