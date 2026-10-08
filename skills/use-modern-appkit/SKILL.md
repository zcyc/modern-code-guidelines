---
name: use-modern-appkit
description: "Use when writing or reviewing code involving AppKit windows, documents, commands, and SwiftUI integration."
---

# AppKit

Resolve the changed file's target from Xcode/Swift, SDK, macOS deployment target, target settings; document architecture, restoration, Objective-C and SwiftUI interop.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-swift for language and concurrency; use-modern-swiftui for embedded SwiftUI.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
