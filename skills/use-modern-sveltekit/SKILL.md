---
name: use-modern-sveltekit
description: "Use when writing or reviewing code involving Svelte components and runes, plus SvelteKit load, actions, SSR, and adapters."
---

# Svelte and SvelteKit

Resolve the changed file's target from package.json/lockfile, Svelte and (if present) SvelteKit/Vite, component legacy vs runes mode; Kit adapter/runtime and prerender/SSR/CSR settings.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime; add use-modern-typescript for TS. Apply Kit rules only when Kit is installed; standalone Svelte is covered.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
