---
name: use-modern-unity
description: "Use for Unity code and reviews: component lifecycle, serialization, assets, Editor tooling, profiling, and player builds."
---

# Unity

Resolve the Editor version from ProjectSettings/ProjectVersion.txt; package versions from Packages/manifest.json and packages-lock.json; target platforms, scripting backend, API compatibility and stripping from ProjectSettings and build scripts/profiles. Inspect relevant .asmdef/.asmref files and compiler response files. Unity-generated .csproj files and an installed .NET SDK do not establish Unity's supported language or runtime APIs.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify engine APIs in the matching Editor documentation and package APIs in the installed package's versioned docs. For upgrades, consult the version-sensitive rules and every intervening official upgrade guide plus exact patch/package release notes. Keep unrelated engine/package upgrades out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-csharp for language and general .NET guidance, constrained by Unity's compiler and API compatibility support. This skill adds engine-specific rules only.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run existing Edit Mode/Play Mode checks relevant to the change and a target player build when platform/backend behavior changes; report checks unavailable without Unity.
