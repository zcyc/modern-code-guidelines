---
name: use-modern-nuxt
description: "Use for Nuxt code and reviews: routing, SSR data, Nitro, caching, and deployment."
---

# Nuxt

Resolve the changed file's target from package.json/lockfile, nuxt.config.*, Nuxt/Vue/Nitro/Node, directory/compatibility settings and deployment preset.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-vue for components; add use-modern-typescript for TS and use-modern-javascript for runtime.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
