---
name: use-modern-uikit
description: "Use version-aware UIKit view, controller, lifecycle, concurrency, accessibility, and SwiftUI interop idioms when writing, modifying, fixing, or reviewing UIKit code."
---

# Modern UIKit

Use for UIKit applications and UIKit code embedded in SwiftUI. Pair with
`use-modern-swift` for language, concurrency, and API-availability rules.

## Target resolution

Read the Xcode and Swift toolchain, SDK, deployment target, and target settings.
Establish whether the code uses the scene-based lifecycle, Mac Catalyst,
Objective-C interop, or SwiftUI representables before using newer APIs.


## Working rules

- Keep UI work on the main actor/main thread required by the API, and isolate
  shared model state separately from view-controller lifecycle state.
- Use the scene-based lifecycle for targets that support or require it; keep
  app-wide responsibilities in the app delegate and scene responsibilities in
  scene delegates or scene configuration.
- Keep view controllers focused on lifecycle and view coordination. Use stable
  domain identity with diffable data sources when collection contents change.
- Prefer Auto Layout, safe areas, trait environments, Dynamic Type, localization,
  and accessibility APIs over fixed device assumptions.
- Treat `UIViewRepresentable` and `UIViewControllerRepresentable` as lifecycle
  boundaries: forward updates, coordinate ownership, and release resources.
- Make deployment checks explicit for newer UIKit APIs and keep platform-specific
  code at the UIKit boundary.

Read `references/guidelines.md` for lifecycle, concurrency, SwiftUI interop, and
availability rules.
