---
name: use-modern-javascript
description: "Use when writing or reviewing code involving JavaScript and TypeScript runtime behavior, ECMAScript APIs, and Node.js."
---

# JavaScript

Resolve the changed file's target from package.json engines.node/type, .nvmrc/.node-version, CI/container runtime; browserslist/build target for browsers. Resolve package module/export contracts.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

For TS, also use use-modern-typescript; it covers types/compiler, this skill covers runtime.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
