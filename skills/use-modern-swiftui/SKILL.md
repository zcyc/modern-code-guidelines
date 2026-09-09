---
name: use-modern-swiftui
description: "Use version-aware SwiftUI state, view, concurrency, identity, and accessibility idioms when writing, modifying, fixing, or reviewing SwiftUI code."
---

# Modern SwiftUI

Use for SwiftUI applications and packages. Pair with use-modern-swift for
Swift language, concurrency, and API-availability rules.

## Target resolution

Read the Xcode and Swift toolchain, deployment targets, package manifest or
project settings, and the OS SDKs actually used. Establish whether the code
uses Observation, UIKit/AppKit interop, widgets, or multiplatform views before
using a newer API.

## Working rules

- Treat a View as a value description. Keep body computation deterministic and
  free of network, persistence, and other externally observable side effects.
- Make state ownership explicit: local state belongs to the view, bindings belong
  to children that edit parent-owned state, and shared models use the project's
  supported Observation or environment mechanism.
- Use task-based async work with cancellation and stable task identity; do not
  start duplicate loads from repeated appearance callbacks.
- Give ForEach and navigation data stable identity. Do not use array indices as
  identity when items can change order.
- Keep UI-facing state isolated to the main actor as required by the target and
  propagate cancellation and errors instead of silently discarding them.
- Build for Dynamic Type, localization, accessibility labels/traits, and the
  supported platform size classes; use UIKit/AppKit only at a real platform boundary.

Read references/guidelines.md for SwiftUI state ownership, identity, async
lifecycle, and version-gated Observation, navigation, concurrency, or platform APIs.
