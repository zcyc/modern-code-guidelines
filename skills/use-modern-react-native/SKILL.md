---
name: use-modern-react-native
description: "Use version-aware React Native component, New Architecture, platform, performance, and native-module idioms when writing, modifying, fixing, or reviewing React Native code."
---

# Modern React Native

Use for bare React Native applications and libraries. If Expo SDK, app config,
or Continuous Native Generation is the build boundary, use use-modern-expo for
that work. Pair with use-modern-react for React rules and use-modern-typescript
for TypeScript rules.

## Target resolution

Read package.json, the lockfile, React Native and React versions, Hermes and
Metro configuration, Android Gradle/SDK targets, iOS deployment and CocoaPods
settings, and whether the New Architecture is enabled. Resolve native and
JavaScript targets separately.

## Working rules

- Treat the New Architecture as the default design target. Use Fabric,
  TurboModules, and Codegen for new native components or modules when the target
  supports them; do not create new bridge-only APIs by habit.
- Keep native code behind a narrow, typed boundary. Native dependency, Podfile,
  Gradle, permission, or codegen changes require a native rebuild and platform
  testing; hot reload is not evidence that the binary is correct.
- Use platform selectors and native APIs deliberately. Keep Android and iOS
  lifecycle, permission, accessibility, and unavailable-feature behavior explicit.
- Give virtualized lists stable domain keys and measure frame, memory, or startup
  problems before adding memoization, custom renderers, or native optimizations.
- Keep render logic pure and preserve React state ownership; do not hide native
  side effects in component render or duplicate server/cache state locally.

Read references/guidelines.md before using version-sensitive architecture,
native-module, Hermes, or platform behavior.
