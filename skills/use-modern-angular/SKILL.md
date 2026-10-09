---
name: use-modern-angular
description: "Use for Angular code and reviews: components, signals, templates, forms, and change detection."
---

# Angular

Resolve the changed file's target from package.json/lockfile, angular.json, tsconfig, Angular/TypeScript versions; standalone vs NgModule, SSR, ZoneJS vs zoneless.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-typescript for types and use-modern-javascript for runtime behavior.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
