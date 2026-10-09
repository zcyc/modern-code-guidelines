---
name: use-modern-nestjs
description: "Use for NestJS code and reviews: modules, providers, validation, transports, and adapters."
---

# NestJS

Resolve the changed file's target from package.json/lockfile, Nest core/packages, platform adapter, Node/TypeScript, module format and Express/Fastify/GraphQL/WebSocket/microservice transport.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-typescript for types and use-modern-javascript for Node/runtime.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
