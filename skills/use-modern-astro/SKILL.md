---
name: use-modern-astro
description: "Use for Astro code and reviews: islands, content, server actions, rendering, and adapters."
---

# Astro

Resolve the changed file's target from package.json/lockfile, Astro/Vite, integrations, content sources, output, adapter and runtime; static vs on-demand routes.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-typescript for TS, use-modern-javascript for runtime, and the matching framework skill for islands.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
