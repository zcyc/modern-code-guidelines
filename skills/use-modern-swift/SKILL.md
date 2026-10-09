---
name: use-modern-swift
description: "Use for Swift code and reviews: language modes, API availability, isolation, and testing."
---

# Swift

Resolve the changed file's target from Package.swift swift-tools-version/target language settings, Xcode SWIFT_VERSION, SDK/deployment/concurrency settings, .xcconfig and CI swiftc -swift-version/platform flags. Resolve test targets separately.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Tools version, language mode, SDK and deployment availability are separate; add only the framework skills used by the changed code.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
