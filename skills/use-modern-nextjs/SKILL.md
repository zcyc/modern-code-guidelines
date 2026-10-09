---
name: use-modern-nextjs
description: "Use for Next.js code and reviews: routing, server boundaries, server actions, caching, and deployment."
---

# Next.js

Resolve the changed file's target from package.json/lockfile, next.config.*, Next/React/Node, deployment runtime and file router (App or Pages).

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-react for components; add use-modern-typescript for TS and use-modern-javascript for runtime.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
