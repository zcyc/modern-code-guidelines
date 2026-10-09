---
name: use-modern-sveltekit
description: "Use for Svelte/SvelteKit code and reviews: components, runes, load, form actions, SSR, and adapters."
---

# Svelte and SvelteKit

Resolve the changed file's target from package.json/lockfile, Svelte and (if present) SvelteKit/Vite, component legacy vs runes mode; Kit adapter/runtime and prerender/SSR/CSR settings.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime; add use-modern-typescript for TS. Apply Kit rules only when Kit is installed; standalone Svelte is covered.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
