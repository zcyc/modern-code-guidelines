---
name: use-modern-expo
description: "Use when writing or reviewing code involving Expo SDK configuration, native builds, Router, and OTA updates."
---

# Expo

Resolve the changed file's target from package.json/lockfile, Expo SDK/React Native/React/Node, app config, eas.json, Router, committed vs generated android/ios projects.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Add use-modern-react-native for native/UI work; Expo supplies SDK, build and update rules.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
