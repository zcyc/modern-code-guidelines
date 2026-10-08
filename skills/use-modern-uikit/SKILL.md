---
name: use-modern-uikit
description: "Use when writing or reviewing code involving UIKit scenes, controllers, collections, and SwiftUI integration."
---

# UIKit

Resolve the changed file's target from Xcode/Swift, SDK, deployment/target settings, scenes, Mac Catalyst, restoration, Objective-C and SwiftUI interop.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-swift for language/concurrency; use-modern-swiftui for embedded SwiftUI.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
