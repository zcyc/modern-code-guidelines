---
name: use-modern-vue
description: "Use when writing or reviewing code involving Vue components, reactivity, Composition API, and SFC compiler macros."
---

# Vue

Resolve the changed file's target from package.json/lockfile, Vue/compiler/build-tool versions, Vue 2 vs 3, SFC vs wrapper and Options vs Composition API.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime and use-modern-typescript for TS; use-modern-nuxt owns Nuxt server/routing/deployment rules.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
