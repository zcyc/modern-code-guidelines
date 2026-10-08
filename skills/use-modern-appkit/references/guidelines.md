# AppKit

## Availability

- Read the selected SDK declaration's availability and actor annotations; compare macOS deployment and SDK/compiler independently before adopting an API.
- SwiftUI hosting requires macOS 10.15+; Observation integration requires macOS 14+. Verify individual APIs beyond these framework baselines.

## Windows and UI

- Own windows through NSWindowController or document controllers. NSDocument architecture owns file lifecycle, undo, autosave and restoration for document apps.
- Route commands through responder chain/menu validation; reconstruct windows/documents from explicit restoration/deep-link values.
- UI mutations belong on the required main actor/thread; blocking work and shared model state need separate isolation.
- Use Auto Layout, system metrics/text sizing, localization and accessibility actions/descriptions rather than fixed display assumptions.

## SwiftUI interop

- NSViewRepresentable/NSViewControllerRepresentable must forward updates, coordinate ownership and release subscriptions/delegates. Avoid retain cycles around views/coordinators.
- NSHostingView/Controller embeds SwiftUI; keep window/navigation ownership explicit. Preserve native appearance behavior through standard controls.

## Sources

- https://developer.apple.com/documentation/appkit
- https://developer.apple.com/documentation/updates/appkit
- https://developer.apple.com/documentation/swiftui/appkit-integration
- https://developer.apple.com/design/human-interface-guidelines
