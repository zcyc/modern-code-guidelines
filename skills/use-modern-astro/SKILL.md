---
name: use-modern-astro
description: "Use when writing or reviewing code involving Astro islands, content, actions, rendering, and adapters."
---

# Astro

Resolve the changed file's target from package.json/lockfile, Astro/Vite, integrations, content sources, output, adapter and runtime; static vs on-demand routes.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-typescript for TS, use-modern-javascript for runtime, and the matching framework skill for islands.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
