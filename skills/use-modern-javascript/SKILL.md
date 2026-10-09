---
name: use-modern-javascript
description: "Use for JavaScript/TypeScript runtime code and reviews: ECMAScript APIs, Node.js, and module behavior."
---

# JavaScript

Resolve the changed file's target from package.json engines.node/type, .nvmrc/.node-version, CI/container runtime; browserslist/build target for browsers. Resolve package module/export contracts.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

For TS, also use use-modern-typescript; it covers types/compiler, this skill covers runtime.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
