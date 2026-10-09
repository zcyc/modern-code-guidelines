---
name: use-modern-uikit
description: "Use for UIKit code and reviews: scenes, view controllers, collection views, and SwiftUI integration."
---

# UIKit

Resolve the changed file's target from Xcode/Swift, SDK, deployment/target settings, scenes, Mac Catalyst, restoration, Objective-C and SwiftUI interop.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-swift for language/concurrency; use-modern-swiftui for embedded SwiftUI.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
