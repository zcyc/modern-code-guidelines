---
name: use-modern-react
description: "Use for React code and reviews: components, Hooks, state, Actions, and React Compiler."
---

# React

Resolve the changed file's target from workspace package.json/lockfile, selected React and renderer versions, build config, compiler enablement and client-only vs RSC architecture.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime and use-modern-typescript for TS; use-modern-nextjs owns Next.js routing, server and cache rules.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
