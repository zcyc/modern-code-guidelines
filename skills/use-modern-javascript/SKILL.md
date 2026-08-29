---
name: use-modern-javascript
description: "Use version-aware ECMAScript and Node.js idioms when writing, modifying, fixing, or reviewing JavaScript code."
---

# Modern JavaScript

Apply the newest stable ECMAScript and Node.js patterns guaranteed by the project's
declared runtime.

## Scope

This skill covers core JavaScript, Node.js, modules, async control flow, and built-in
runtime APIs. For browser UI, DOM, CSS, accessibility, browser compatibility, or web
performance, use `modern-web-guidance` as well.

Keep JavaScript and TypeScript decisions separate. If the file is TypeScript, use the
`use-modern-typescript` skill instead.

## Target resolution

Read the target from checked-in project metadata:

1. `package.json` `engines.node` and `type`.
2. `.nvmrc`, `.node-version`, or an equivalent explicit runtime file.
3. A checked-in CI/container runtime declaration.

For browser code, read an explicit `browserslist` or build target. If no target is
declared, report the runtime as unknown and avoid runtime-gated APIs. Never infer the
target from the locally installed Node.js or browser.

## Working rules

- Use ESM for new packages when the package declares `"type": "module"`; preserve CommonJS only when the package contract requires it.
- Prefer `const`, then `let` when reassignment is required; never introduce `var` in new code.
- Prefer `async`/`await`, explicit error handling, and cancellation with `AbortSignal` over nested promise callbacks.
- Prefer standard built-ins over small utility dependencies when the target supports them.
- Keep values and types distinct: JavaScript code must not rely on compile-time-only assumptions.
- Modernize the smallest relevant diff and preserve the package's module/export contract.
- For production Node.js code, target an Active or Maintenance LTS release; use
  Current releases only when the project explicitly accepts their shorter support
  window.
