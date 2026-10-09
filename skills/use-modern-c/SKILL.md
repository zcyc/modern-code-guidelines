---
name: use-modern-c
description: "Use for C code and reviews: standards, resource ownership, libc, and memory safety."
---

# C

Resolve the changed file's target from translation-unit build settings (CMake C_STANDARD, Meson/Make/Bazel), actual compile command/compile_commands.json, -std, compiler, libc, ABI, CI warnings and sanitizers.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
