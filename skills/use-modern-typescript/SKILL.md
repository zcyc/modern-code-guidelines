---
name: use-modern-typescript
description: "Use when writing or reviewing code involving TypeScript compiler configuration, narrowing, types, and emitted module contracts."
---

# TypeScript

Resolve the changed file's target from workspace-selected compiler from package.json/lockfile; effective tsconfig extends/project references including target/lib/module/moduleResolution/strict/verbatimModuleSyntax and the config that includes this file.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime APIs and Node/module behavior.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
