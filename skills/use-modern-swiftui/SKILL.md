---
name: use-modern-swiftui
description: "Use when writing or reviewing code involving SwiftUI state, identity, navigation, tasks, and platform integration."
---

# SwiftUI

Resolve the changed file's target from Xcode/Swift, SDKs, deployment targets, Package.swift/Xcode settings; Observation, widgets, multiplatform and UIKit/AppKit interop.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-swift; add use-modern-uikit or use-modern-appkit for representable/hosting work.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
