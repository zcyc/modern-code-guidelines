# JavaScript version rules

Use these rules after resolving the project's explicit ECMAScript/Node target. The
ECMAScript version describes language and built-ins; the host runtime still determines
whether an API is available.

## ECMAScript 2015+

- Use `const`/`let`, modules, classes only where they improve the model, destructuring, default parameters, template literals, promises, and iterables.
- Prefer `for...of` for iterable values and avoid index loops when the index is not part of the logic.
- Use `Map`/`Set` when keys or membership are the actual data model.

## ECMAScript 2017+

- Prefer `async`/`await` for sequential asynchronous control flow.
- Use `Object.entries`/`Object.values` when iterating object data rather than maintaining parallel key/value logic.

## ECMAScript 2019+

- Use `Array.prototype.flat`/`flatMap` and optional catch bindings where they make intent direct.
- Keep JSON serialization boundaries explicit; do not assume arbitrary values round-trip through JSON.

## ECMAScript 2020+

- Use optional chaining and nullish coalescing when absence and falsiness have distinct meanings.
- Use `globalThis` for cross-host global access and dynamic `import()` for intentional lazy module loading.
- Use `Promise.allSettled` when all outcomes matter; use `Promise.all` when one failure should fail the operation.

## ECMAScript 2021+

- Use logical assignment (`||=`, `&&=`, `??=`) only when its truthiness semantics are obvious.
- Use `replaceAll`, `Promise.any`, and numeric separators where they improve clarity.

## ECMAScript 2022+

- Use class fields/private fields, top-level `await`, `Array.prototype.at`, `Object.hasOwn`, and `Error` causes when the runtime target supports them.
- Prefer error causes (`new Error(message, { cause })`) when rethrowing across an abstraction boundary.

## ECMAScript 2023+

- Use `findLast`/`findLastIndex` and copying array methods (`toSorted`, `toReversed`, `toSpliced`, `with`) when mutation is not intended.
- Do not replace a mutating operation with a copying operation in a hot path without checking the allocation cost.

## ECMAScript 2024+

- Use `Object.groupBy`/`Map.groupBy`, `Promise.withResolvers`, and resizable buffers only when the declared runtime supports them.
- Use `RegExp` set notation and the `v` flag only when the target explicitly includes it; do not assume browser parity from Node support.

## ECMAScript 2025+

- Use the Iterator helpers and Set composition methods instead of hand-written iterator/set plumbing.
- Use `RegExp.escape` for dynamic literal text in regular expressions.
- Use JSON module import attributes only with an explicit ESM/runtime target that supports them.
- Use `Promise.try` and `Float16Array` only when the runtime target guarantees them.

## ECMAScript 2026+

- Use `Error.isError` for cross-realm checks of unknown thrown values; do not use
  `instanceof Error` when values can cross a worker, VM, or iframe boundary.
- Use `Uint8Array` base64/hex conversion methods and `Map.getOrInsert` when they
  match the data contract; keep explicit codecs when their validation policy is
  stricter than the built-in API.
- Use `Math.sumPrecise` for numerically sensitive summation of an iterable; do not
  replace a performance-critical reduction without measuring the cost.

## Node.js 24+

- Prefer Active or Maintenance LTS releases for production; pin the runtime in
  project metadata and CI rather than relying on the local Node installation.

## Node.js 26+

- Treat Node.js 26 as a Current release until it enters LTS; use its newer built-in
  APIs only when the package explicitly targets Node 26 and its support window.

## Node.js module boundary

- Make the package module system explicit with `package.json` `type`, `.mjs`, or `.cjs`.
- Do not mix `require` and `import` in a new module to hide an unresolved package-boundary problem.
- Treat Node built-ins and browser Web APIs as separate host surfaces; validate the one the project actually runs on.

## Authority

- [ECMAScript 2026 specification](https://tc39.es/ecma262/2026/multipage/)
- [Node.js ECMAScript modules](https://nodejs.org/dist/latest/docs/api/esm.html)
- [Node.js API documentation](https://nodejs.org/dist/latest/docs/api/)
- [Node.js release schedule](https://nodejs.org/en/about/previous-releases)
