---
name: use-modern-expo
description: "Use version-aware Expo configuration, routing, native-module, development-build, and OTA-update idioms when writing, modifying, fixing, or reviewing Expo code."
---

# Modern Expo

Use for Expo applications and Expo modules. For a bare React Native app without
Expo's SDK/configuration boundary, use use-modern-react-native instead. Pair with
use-modern-react for React rules and use-modern-typescript for TypeScript rules.

## Target resolution

Read package.json, the lockfile, Expo SDK, React Native, React, Node.js, app
config, eas.json, Expo Router presence, and whether android/ios directories are
managed or committed. Resolve the native and JavaScript targets separately.

## Working rules

- Distinguish JavaScript-only changes from native changes. Native modules,
  permissions, config plugins, and native project edits require a development
  build or a new native binary.
- Treat app.json/app.config.* as build and public-runtime configuration. Never
  put secrets in values that are embedded in the app or OTA manifest.
- Use Expo Router only when it is part of the project; preserve the existing
  navigation model and deep-link contract.
- Keep runtimeVersion and update channels compatible with the native binary.
  OTA updates must not require native code or native dependency changes.
- Prefer Expo's supported install/configuration flow for SDK modules and inspect
  the resolved native configuration after prebuild or plugin changes.
- Keep Expo SDK packages on the project's selected SDK line; prefer `expo
  install` and its compatibility checks over generic package installation for
  Expo modules.
- Handle platform permissions, lifecycle, and unavailable APIs explicitly on
  Android, iOS, and web targets.

Read references/guidelines.md before using SDK-specific, EAS, Router, or
development-build behavior.
