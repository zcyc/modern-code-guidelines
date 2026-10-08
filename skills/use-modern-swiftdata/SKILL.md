---
name: use-modern-swiftdata
description: "Use when writing or reviewing code involving SwiftData models, context isolation, migrations, and Core Data coexistence."
---

# SwiftData

Resolve the changed file's target from Swift language mode, Xcode/SDK, OS deployment, SwiftUI/UIKit/AppKit integration and SwiftData/Core Data/CloudKit backend.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-swift; add use-modern-swiftui, use-modern-uikit or use-modern-appkit for the actual UI integration.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
