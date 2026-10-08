---
name: use-modern-nextjs
description: "Use when writing or reviewing code involving Next.js routing, server boundaries, actions, caching, and deployment."
---

# Next.js

Resolve the changed file's target from package.json/lockfile, next.config.*, Next/React/Node, deployment runtime and file router (App or Pages).

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-react for components; add use-modern-typescript for TS and use-modern-javascript for runtime.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
