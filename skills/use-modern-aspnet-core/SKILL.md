---
name: use-modern-aspnet-core
description: "Use for ASP.NET Core code and reviews: endpoints, middleware, hosting, and dependency lifetimes."
---

# ASP.NET Core

Resolve the changed file's target from .csproj/solution, Directory.Build.*, global.json, packages, TargetFramework and deployed runtime; Minimal APIs, MVC, Razor, Blazor, gRPC or SignalR.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-csharp for language and .NET APIs.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
