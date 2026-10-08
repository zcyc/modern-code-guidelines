---
name: use-modern-react
description: "Use when writing or reviewing code involving React components, hooks, state, Actions, and compiler behavior."
---

# React

Resolve the changed file's target from workspace package.json/lockfile, selected React and renderer versions, build config, compiler enablement and client-only vs RSC architecture.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for runtime and use-modern-typescript for TS; use-modern-nextjs owns Next.js routing, server and cache rules.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
