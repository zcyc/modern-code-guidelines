---
name: use-modern-react-native
description: "Use for React Native code and reviews, including Expo: native UI, modules, architecture, and performance."
---

# React Native

Resolve the changed file's target from package.json/lockfile, React Native/React/Node, Hermes/Metro, Gradle/Android SDK, iOS deployment/CocoaPods and New Architecture state.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-react and use-modern-javascript; add use-modern-typescript for TS. Add use-modern-expo for Expo config/builds/updates; native edits use use-modern-kotlin or use-modern-swift plus the relevant platform skill.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
