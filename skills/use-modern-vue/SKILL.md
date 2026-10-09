---
name: use-modern-vue
description: "Use for Vue code and reviews: components, reactivity, Composition API, and SFC compiler macros."
---

# Vue

Resolve the changed file's target from package.json/lockfile, Vue/compiler/build-tool versions, Vue 2 vs 3, SFC vs wrapper and Options vs Composition API.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime and use-modern-typescript for TS; use-modern-nuxt owns Nuxt server/routing/deployment rules.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
