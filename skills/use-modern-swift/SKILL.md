---
name: use-modern-swift
description: "Use when writing or reviewing code involving Swift language mode, API availability, isolation, and testing."
---

# Swift

Resolve the changed file's target from Package.swift swift-tools-version/target language settings, Xcode SWIFT_VERSION, SDK/deployment/concurrency settings, .xcconfig and CI swiftc -swift-version/platform flags. Resolve test targets separately.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Tools version, language mode, SDK and deployment availability are separate; add only the framework skills used by the changed code.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
