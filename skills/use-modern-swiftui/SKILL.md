---
name: use-modern-swiftui
description: "Use for SwiftUI code and reviews: state, identity, navigation, tasks, and platform integration."
---

# SwiftUI

Resolve the changed file's target from Xcode/Swift, SDKs, deployment targets, Package.swift/Xcode settings; Observation, widgets, multiplatform and UIKit/AppKit interop.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-swift; add use-modern-uikit or use-modern-appkit for representable/hosting work.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
