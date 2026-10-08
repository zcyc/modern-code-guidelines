# NestJS

## Gates

- Nest 12 core is ESM-oriented and adds Standard Schema/native observability paths; resolve module format before adopting APIs.
- Runtime ESM interop needs Node 20.19+ or 22.12+; CLI/schematics have a higher floor. Check generation tools separately.
- Upgrade @nestjs/* packages together; Express/Fastify adapters differ in integration semantics.

## Modules and transport

- Modules own imports/providers/controllers/exports; avoid circular dependencies and unneeded global scope. Providers own application behavior, controllers transport.
- Pipes validate/transform, guards authorize, interceptors wrap cross-cutting work, filters map transport errors. Keep domain decisions outside middleware.
- Request scope is for real per-request state and increases graph/allocation cost. Preserve deliberate Promise/Observable contracts.
- Standard Schema pipes fit existing compatible schema libraries; keep class DTOs when established. Check OpenAPI/serialization/security metadata against runtime behavior.
- Keep configuration/secrets aligned with deployment; CommonJS apps need verified interop with ESM core/tooling.

## Sources

- https://docs.nestjs.com/
- https://docs.nestjs.com/modules
- https://docs.nestjs.com/providers
- https://docs.nestjs.com/pipes
- https://docs.nestjs.com/guards
- https://docs.nestjs.com/interceptors
- https://docs.nestjs.com/security
- https://docs.nestjs.com/migration-guide
