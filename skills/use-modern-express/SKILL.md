---
name: use-modern-express
description: "Use for Express code and reviews: routes, middleware, async errors, and server lifecycle."
---

# Express

Resolve the changed file's target from package.json/lockfile: Express, Node engines, module type and build target; proxy topology, serverless vs long-lived process.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-javascript for Node/runtime; add use-modern-typescript for TS.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
