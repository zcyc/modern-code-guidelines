---
name: use-modern-appkit
description: "Use version-aware AppKit window, view, responder, document, concurrency, accessibility, and SwiftUI interop idioms when writing, modifying, fixing, or reviewing AppKit code."
---

# Modern AppKit

Use for native macOS AppKit applications and AppKit code embedded in SwiftUI.
Pair with `use-modern-swift` for language, concurrency, and API-availability
rules.

## Target resolution

Read the Xcode and Swift toolchain, SDK, macOS deployment target, and target
settings. Establish whether the code uses document-based architecture,
Objective-C interop, state restoration, or SwiftUI representables before using
newer APIs.


## Working rules

- Keep AppKit UI work on the main actor/main thread required by the API, and
  isolate shared model state from window and view lifecycle state.
- Use `NSWindowController` and explicit ownership for windows. For document-based
  apps, use the AppKit document architecture instead of recreating document
  lifecycle and restoration in view controllers.
- Use the responder chain and menu validation for command routing; keep command
  state explicit instead of reaching through unrelated view hierarchies.
- Prefer Auto Layout, system text sizing where supported, localization, and AppKit
  accessibility APIs over fixed window or display assumptions.
- Treat `NSViewRepresentable` and `NSViewControllerRepresentable` as lifecycle
  boundaries: forward updates, coordinate ownership, and release resources.
- Make macOS availability checks explicit for newer APIs and keep platform-specific
  code at the AppKit boundary.

Read `references/guidelines.md` for window and document ownership, responder
behavior, concurrency, SwiftUI interop, and availability rules.
