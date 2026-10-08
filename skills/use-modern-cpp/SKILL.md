---
name: use-modern-cpp
description: "Use when writing or reviewing code involving C++ standards, ownership, templates, and library availability."
---

# C++

Resolve the changed file's target from translation-unit build settings (CMake CXX_STANDARD/CXX_EXTENSIONS, Meson/Bazel), compile_commands.json/actual command, compiler, standard library, ABI and CI flags.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
