---
name: use-modern-aspnet-core
description: "Use when writing or reviewing code involving ASP.NET Core endpoints, middleware, hosting, and dependency lifetimes."
---

# ASP.NET Core

Resolve the changed file's target from .csproj/solution, Directory.Build.*, global.json, packages, TargetFramework and deployed runtime; Minimal APIs, MVC, Razor, Blazor, gRPC or SignalR.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-csharp for language and .NET APIs.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
