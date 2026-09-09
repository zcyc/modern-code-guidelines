# Expo version rules

Resolve Expo SDK, React Native, React, Node.js, app config, and EAS targets from
the repository. SDK modules, native projects, and OTA updates have different
compatibility contracts.

## Native boundary

- JavaScript-only changes can use the existing development client. A native
  module, permission, config-plugin, or native-project change needs a new
  development or production build.
- Treat prebuild output as generated when the project uses Continuous Native
  Generation; make durable native changes through app config or config plugins.
- Inspect the native diff after prebuild or plugin changes and test each target
  platform affected.
- Treat the SDK's React Native version and native build tooling as one tested
  compatibility line. A package can be JavaScript-compatible yet still require
  a native rebuild or a newer development client.

## Configuration and updates

- app.json/app.config.* contributes to builds and public runtime configuration;
  never place secrets in it.
- Keep runtimeVersion and update channels aligned with the native binary. Do not
  publish an OTA update that requires a native API absent from that binary.
- Use Expo Router only when installed and configured by the project; preserve
  its deep-link and file-based route contract.

## Authority

- https://docs.expo.dev/workflow/overview/
- https://docs.expo.dev/workflow/configuration/
- https://docs.expo.dev/develop/development-builds/introduction/
- https://docs.expo.dev/develop/development-builds/development-workflows/
- https://docs.expo.dev/router/introduction/
- https://docs.expo.dev/eas-update/runtime-versions/
- https://docs.expo.dev/workflow/using-libraries/
