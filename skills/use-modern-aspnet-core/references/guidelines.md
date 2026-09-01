# ASP.NET Core version rules

Resolve the .NET SDK, TargetFramework, ASP.NET Core packages, and hosting model
from the repository. New APIs and defaults must match that target.

## .NET generation gates

- `TargetFramework` selects the compile-time API surface; the SDK selected by
  `global.json` and the runtime used in deployment are separate constraints.
  Resolve all three before copying an example.
- .NET 8 and later provide keyed dependency injection and supported Native AOT
  paths. Use them only when the target and deployment actually require them;
  AOT code must remain trim-safe and use compatible serialization and endpoint
  APIs.
- .NET 10 and later provide the newer Minimal API validation surface. Do not
  introduce it into a project whose target does not expose the corresponding
  validation APIs and package references.

## HTTP pipeline

- Middleware order is semantic. Exception handling must wrap the work it should
  catch; authentication precedes authorization; antiforgery and CORS must follow
  the project's documented endpoint and security model.
- Keep endpoint metadata, authorization policies, and OpenAPI descriptions
  aligned with the actual behavior.
- Use Minimal APIs when the project has chosen them and they reduce ceremony;
  controllers remain valid for applications that need their conventions.

## Lifetime and async behavior

- A singleton must not hold a scoped dependency. Background services should
  create a scope for scoped application services.
- Do not block on Tasks or use sync-over-async. Pass cancellation to database,
  HTTP, and streaming operations.

## Authority

- https://learn.microsoft.com/en-us/aspnet/core/
- https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis
- https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware
- https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection
- https://learn.microsoft.com/en-us/aspnet/core/web-api/handle-errors
