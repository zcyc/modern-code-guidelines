---
name: use-modern-angular
description: "Use when writing or reviewing code involving Angular components, signals, templates, forms, and change detection."
---

# Angular

Resolve the changed file's target from package.json/lockfile, angular.json, tsconfig, Angular/TypeScript versions; standalone vs NgModule, SSR, ZoneJS vs zoneless.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-typescript for types and use-modern-javascript for runtime behavior.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
