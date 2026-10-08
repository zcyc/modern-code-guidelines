---
name: use-modern-react-native
description: "Use when writing or reviewing code involving React Native UI, native modules, architecture, and performance, including Expo."
---

# React Native

Resolve the changed file's target from package.json/lockfile, React Native/React/Node, Hermes/Metro, Gradle/Android SDK, iOS deployment/CocoaPods and New Architecture state.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-react and use-modern-javascript; add use-modern-typescript for TS. Add use-modern-expo for Expo config/builds/updates; native edits use use-modern-kotlin or use-modern-swift plus the relevant platform skill.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
