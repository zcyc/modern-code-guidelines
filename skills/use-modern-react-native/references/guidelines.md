# React Native

## Gates

- New Architecture defaults on in 0.76; inspect opt-out/library support on older targets. 0.82+ requires it.
- 0.84+ defaults to Hermes V1; check worklets/animation/native libraries when changing engine or upgrading.
- 0.87+ defaults to Strict TypeScript API and requires Node 22, AGP 9 and Kotlin 2.0+. SwiftPM support remains experimental until the native build explicitly supports it.

## Native and UI boundaries

- Use supported Fabric/TurboModule/Codegen contracts for new native work; expose narrow typed APIs and explicit platform failure/absence.
- Native dependencies, Podfile/Gradle, permissions, codegen or lifecycle changes require native rebuilds and affected-platform tests. JS reload does not verify a binary.
- Core platform components and established navigation/data libraries preserve native behavior; virtualize large lists with stable domain keys and measure frames/memory/startup before memoization/native optimization.
- Test accessibility, safe areas, keyboard, permission denial, backgrounding and deep links on each target. React render/effect rules still apply in Expo.

## Sources

- https://reactnative.dev/releases/overview
- https://reactnative.dev/blog/2026/08/11/react-native-0.87
- https://reactnative.dev/blog/2026/02/11/react-native-0.84
- https://reactnative.dev/architecture/landing-page
- https://reactnative.dev/docs/the-new-architecture/landing-page
- https://reactnative.dev/docs/turbo-native-modules-introduction
- https://reactnative.dev/docs/optimizing-flatlist-configuration
