---
name: use-modern-cpp
description: "Use for C++ code and reviews: standards, ownership, templates, and standard-library availability."
---

# C++

Resolve the changed file's target from translation-unit build settings (CMake CXX_STANDARD/CXX_EXTENSIONS, Meson/Bazel), compile_commands.json/actual command, compiler, standard library, ABI and CI flags.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
