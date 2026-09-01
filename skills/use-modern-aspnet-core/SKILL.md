---
name: use-modern-aspnet-core
description: "Use version-aware ASP.NET Core API, middleware, dependency-injection, security, validation, and hosting idioms when writing, modifying, fixing, or reviewing .NET web code."
---

# Modern ASP.NET Core

Use for ASP.NET Core applications and libraries. Pair with use-modern-csharp
for C# rules.

## Target resolution

Read the nearest csproj, solution, Directory.Build.* files, package versions,
SDK selection, and TargetFramework. Establish whether the changed area uses
Minimal APIs, MVC/controllers, Razor, Blazor, gRPC, or SignalR before changing
its hosting model.

## Working rules

- Use the project's established endpoint style; do not migrate controllers to
  Minimal APIs or vice versa without an explicit migration request.
- Treat middleware order as behavior. Keep exception handling, HTTPS, routing,
  CORS, authentication, authorization, antiforgery, and endpoints in a valid order.
- Use async APIs end to end and propagate CancellationToken through I/O and
  application boundaries.
- Respect dependency-injection lifetimes. Do not capture scoped services in
  singletons; create a scope inside background work when needed.
- Return consistent ProblemDetails or the project's established error contract;
  validate input at the HTTP boundary and authorize before privileged work.
- Keep OpenAPI output and endpoint metadata accurate when the project publishes it.

Read references/guidelines.md before using version-gated Minimal API, validation,
OpenAPI, or hosting behavior.
