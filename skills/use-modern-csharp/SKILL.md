---
name: use-modern-csharp
description: "Use for C# code and reviews: language features, nullable references, async, and .NET APIs."
---

# C#

Resolve the changed file's target from .csproj and inherited Directory.Build.props/targets: LangVersion, TargetFramework(s), Nullable, ImplicitUsings; global.json SDK and deployment runtime.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Compiler syntax and framework APIs have separate gates.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
