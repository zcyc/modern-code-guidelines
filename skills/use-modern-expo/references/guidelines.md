# Expo

## Build boundary

- Expo SDK pins a tested React Native/module/toolchain combination; use expo install and compatibility checks instead of arbitrary package versions.
- JS-only changes can reuse a compatible development client. Native modules, permissions, config plugins and native edits need a new binary; inspect native diffs and test affected platforms.
- With Continuous Native Generation, prebuild output is generated; durable edits belong in app config/plugins. Preserve directly maintained native projects when CNG is not used.

## Configuration and updates

- app.json/app.config.* values shipped in builds/updates are public; use server-side secret storage for secrets. Native build-only secret inputs must not enter embedded config.
- runtimeVersion expresses binary compatibility; channels/branches select updates. Publish only to binaries providing all required native APIs.
- Router applies only when configured; preserve navigation/deep-link contracts. Handle permission denial, lifecycle and missing APIs per Android/iOS/web target.

## Sources

- https://docs.expo.dev/workflow/overview/
- https://docs.expo.dev/workflow/configuration/
- https://docs.expo.dev/develop/development-builds/introduction/
- https://docs.expo.dev/develop/development-builds/development-workflows/
- https://docs.expo.dev/router/introduction/
- https://docs.expo.dev/eas-update/runtime-versions/
- https://docs.expo.dev/workflow/using-libraries/
