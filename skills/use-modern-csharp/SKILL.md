---
name: use-modern-csharp
description: "Use when writing or reviewing code involving C# language features, nullable types, async, and .NET APIs."
---

# C#

Resolve the changed file's target from .csproj and inherited Directory.Build.props/targets: LangVersion, TargetFramework(s), Nullable, ImplicitUsings; global.json SDK and deployment runtime.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Compiler syntax and framework APIs have separate gates.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
