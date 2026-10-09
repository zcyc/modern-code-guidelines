---
name: use-modern-expo
description: "Use for Expo code and reviews: SDK configuration, native builds, Expo Router, and over-the-air updates."
---

# Expo

Resolve the changed file's target from package.json/lockfile, Expo SDK/React Native/React/Node, app config, eas.json, Router, committed vs generated android/ios projects.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Add use-modern-react-native for native/UI work; Expo supplies SDK, build and update rules.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
