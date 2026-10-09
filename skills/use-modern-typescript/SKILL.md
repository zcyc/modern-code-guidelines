---
name: use-modern-typescript
description: "Use for TypeScript code and reviews: compiler configuration, types, narrowing, and emitted module contracts."
---

# TypeScript

Resolve the workspace compiler from package.json/lockfile and the changed file's effective tsconfig, including extends/project references and target/lib/module/moduleResolution/strict/verbatimModuleSyntax.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime APIs and Node/module behavior.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
