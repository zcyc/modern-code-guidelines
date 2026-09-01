---
name: use-modern-nestjs
description: "Use version-aware NestJS module, dependency-injection, validation, security, and transport idioms when writing, modifying, fixing, or reviewing NestJS code."
---

# Modern NestJS

Use for NestJS applications and packages. Pair with use-modern-typescript for
TypeScript rules and use-modern-javascript for Node.js runtime rules.

## Target resolution

Read package.json, the lockfile, Nest core and platform adapter versions, the
Node.js target, and whether the application uses Express, Fastify, GraphQL,
WebSockets, or microservices. Preserve the transport already used by the area.

## Working rules

- Keep module imports and exports explicit. Use providers for application logic
  and keep controllers focused on transport concerns.
- Use dependency injection scopes deliberately; avoid request-scoped providers
  unless the request lifetime is required and its cost is understood.
- Validate and transform untrusted input at the pipe/DTO boundary, then keep
  domain logic independent of transport decorators.
- Use guards for authorization, interceptors for cross-cutting behavior, and
  exception filters for transport error mapping; do not hide business decisions
  in middleware.
- Prefer one clear async contract per boundary. Do not mix Observable and
  Promise flows merely for style.
- Keep configuration, secrets, and generated OpenAPI metadata aligned with the
  deployed module graph.

Read references/guidelines.md before using version-sensitive Nest APIs or
adapter-specific behavior.
