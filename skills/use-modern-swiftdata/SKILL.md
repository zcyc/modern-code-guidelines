---
name: use-modern-swiftdata
description: "Use for SwiftData code and reviews: models, context isolation, migrations, CloudKit, and Core Data coexistence."
---

# SwiftData

Resolve the changed file's target from Swift language mode, Xcode/SDK, OS deployment, SwiftUI/UIKit/AppKit integration and SwiftData/Core Data/CloudKit backend.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-swift; add use-modern-swiftui, use-modern-uikit or use-modern-appkit for the actual UI integration.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
