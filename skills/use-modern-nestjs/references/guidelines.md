# NestJS version rules

Resolve Nest core, platform adapter, Node.js, TypeScript, and package versions
from the repository before using an API. Express and Fastify adapters are not
interchangeable in every integration.

## Nest generation gate

- Nest 12 and later require an explicit Node/module-format decision: its core
  packages are ESM-oriented, and that generation adds Standard Schema and
  native observability paths. Do not copy those APIs into an older Nest target
  without checking its migration guide and package support.
- Upgrade `@nestjs/*` packages as a coordinated set. A mixed-major framework
  install can make otherwise valid decorators and adapters fail at runtime.

## Module and request boundaries

- Modules own explicit imports, providers, controllers, and exports. Avoid
  circular dependencies and broad global modules unless the boundary is truly
  application-wide.
- Controllers handle transport concerns. Providers own reusable application
  behavior and should not depend on HTTP objects unless that coupling is explicit.
- Pipes validate or transform inputs, guards authorize, interceptors wrap
  cross-cutting behavior, and exception filters map errors to the transport.

## Runtime behavior

- Use request scope only when per-request state is required; it changes provider
  lifetime and can increase allocation and dependency-graph cost.
- Keep Observable and Promise boundaries deliberate. Preserve the project's
  chosen contract instead of converting every handler for stylistic reasons.
- Validate generated OpenAPI, serialization, and security metadata when those
  artifacts are part of the public API.

## Schema and module boundaries

- When the target supports Standard Schema, use the schema-first validation and
  serialization pipes for new boundaries when the project already uses a
  compatible schema library. Keep class-based DTOs where that is the established
  contract; do not mix both styles invisibly.
- Review module format and Node support when upgrading Nest packages:
  core packages may be ESM while an application can still remain CommonJS if
  its runtime and tooling support that interop.

## Authority

- https://docs.nestjs.com/
- https://docs.nestjs.com/modules
- https://docs.nestjs.com/providers
- https://docs.nestjs.com/pipes
- https://docs.nestjs.com/guards
- https://docs.nestjs.com/interceptors
- https://docs.nestjs.com/security
- https://docs.nestjs.com/migration-guide
