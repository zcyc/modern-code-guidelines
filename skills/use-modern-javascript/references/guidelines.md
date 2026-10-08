# JavaScript runtime

## ECMAScript gates

- 2015: const/let, modules, destructuring/defaults/templates, Promise/iterables and Map/Set. Classes need an identity/behavior reason.
- 2017: async/await, Object.entries/values.
- 2019: flat/flatMap and optional catch binding; arbitrary values do not necessarily JSON-round-trip.
- 2020: optional chaining/?? (absence differs from falsiness), globalThis, dynamic import and Promise.allSettled when every outcome matters; Promise.all fails as a group.
- 2021: logical assignment with deliberate truthiness, replaceAll, Promise.any and numeric separators.
- 2022: fields/private fields, top-level await, at, Object.hasOwn and Error causes for causal rethrows.
- 2023: findLast/findLastIndex and copying toSorted/toReversed/toSpliced/with; copying changes allocation/mutation contracts.
- 2024: Object/Map.groupBy, Promise.withResolvers, resizable buffers and RegExp v sets.
- 2025: iterator helpers, Set composition, RegExp.escape, JSON import attributes, Promise.try and Float16Array.
- 2026: Error.isError for cross-realm errors, Uint8Array base64/hex codecs, Map getOrInsert and Math.sumPrecise. Keep stricter codec validation and measured numeric hot paths explicit.

## Host and module boundaries

- ECMAScript editions do not guarantee runtime support; check the declared Node/browser engine for each API. TypeScript lib declarations and transpiled syntax do not polyfill built-ins.
- Resolve ESM/CommonJS through package type, extensions and exports; preserve existing contracts instead of mixing require/import to bypass an unresolved boundary.
- Own async errors and cancellation (AbortSignal where supported). Prefer standard APIs to small utility dependencies.
- Production Node defaults to Active/Maintenance LTS; Current requires an explicit project decision. Node built-ins and browser APIs are separate host surfaces.

## Sources

- [ECMAScript 2026 specification](https://tc39.es/ecma262/2026/multipage/)
- [Node.js ECMAScript modules](https://nodejs.org/dist/latest/docs/api/esm.html)
- [Node.js API documentation](https://nodejs.org/dist/latest/docs/api/)
- [Node.js release schedule](https://nodejs.org/en/about/previous-releases)
