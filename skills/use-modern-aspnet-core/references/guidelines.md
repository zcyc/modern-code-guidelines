# ASP.NET Core

## Gates

- TargetFramework constrains APIs; global.json selects SDK; deployment selects runtime. Resolve each.
- .NET 8+: keyed DI and supported Native AOT paths; AOT requires trim-safe serialization/endpoints and compatible libraries.
- .NET 10+: Minimal API validation needs the matching APIs/packages; WithOpenApi is deprecated in favor of built-in OpenAPI/metadata. Known API endpoints using cookies return 401/403 instead of login redirects; verify clients.

## HTTP and lifetimes

- Preserve chosen endpoint model (Minimal APIs/MVC/Razor/Blazor/gRPC/SignalR). Exception middleware wraps work; authentication precedes authorization; CORS/antiforgery follow endpoint policy/order.
- Validate/authorize at the boundary; use ProblemDetails or the established error contract. Keep OpenAPI/endpoint metadata accurate.
- Singletons cannot capture scoped services; background work creates scopes. Await I/O end to end and propagate CancellationToken through database/HTTP/streams.

## Sources

- https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-10.0?view=aspnetcore-10.0
- https://learn.microsoft.com/en-us/aspnet/core/
- https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis
- https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware
- https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection
- https://learn.microsoft.com/en-us/aspnet/core/web-api/handle-errors
