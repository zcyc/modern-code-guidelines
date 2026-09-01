# React Native version rules

Resolve React Native, React, Node.js, Hermes, Metro, Android, iOS, and native
library versions from the repository. React Native compatibility is a matrix,
not a single package version.

## Architecture gates

- The New Architecture is enabled by default from React Native 0.76. Resolve
  the target's opt-in or opt-out state before assuming Fabric, TurboModules, or
  Codegen are available.
- React Native 0.82 and later run only on the New Architecture. For older
  targets, verify native library compatibility before adding a new-architecture
  dependency or module.

## Architecture and native boundary

- Treat the New Architecture as the baseline for new code. Custom native
  modules and components should use the supported TurboModule/Fabric and Codegen
  paths instead of inventing a new bridge protocol.
- A JavaScript-only change and a native change have different verification
  paths. Rebuild after native dependencies, permissions, generated code, Podfile,
  Gradle, or app lifecycle changes.
- Keep native APIs narrow and typed, and surface platform failure or absence as
  an explicit result rather than assuming both platforms behave identically.

## UI and performance

- Keep components pure and use React's state/effect rules. Prefer core platform
  components and the project's established navigation/data libraries.
- Virtualize large collections, use stable keys, and measure before changing
  rendering strategy or adding memoization.
- Test accessibility, safe areas, keyboard behavior, permissions, backgrounding,
  and deep links on each supported platform.

## Authority

- https://reactnative.dev/releases/overview
- https://reactnative.dev/architecture/landing-page
- https://reactnative.dev/docs/the-new-architecture/landing-page
- https://reactnative.dev/docs/turbo-native-modules-introduction
- https://reactnative.dev/docs/optimizing-flatlist-configuration
