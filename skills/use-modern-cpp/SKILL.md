---
name: use-modern-cpp
description: Use version-aware modern C++ language, standard-library, ownership, and safety idioms when writing, modifying, fixing, or reviewing C++ code.
---

# Modern C++

Apply stable C++ features supported by the translation unit's actual compiler
standard and build configuration. Read `references/guidelines.md` before using
standard-version-gated syntax or library APIs.

## Target resolution

Read the effective target for the file:

1. `CXX_STANDARD`/`CXX_EXTENSIONS` and toolchain settings in CMake, Meson, Bazel,
   or the project's build files.
2. The actual compile command or checked-in `compile_commands.json`.
3. An explicit standard flag in CI or platform build configuration.

The language standard and library/compiler availability are separate constraints.
If the target is unknown, report it and avoid C++20/23/26-only features. Preserve
ABI and project-wide compiler settings while making the smallest relevant change.

## Working rules

- Use RAII and standard resource handles; avoid naked `new`/`delete` and manual
  cleanup paths.
- Prefer values and `std::unique_ptr` for ownership; use `std::shared_ptr` only
  when shared ownership is part of the model. Raw pointers and references are
  non-owning unless the API says otherwise.
- Use `std::span`, `std::string_view`, and explicit ranges for non-owning views
  when the target and lifetime make them safe.
- Prefer `const`, `constexpr`, scoped enums, standard algorithms, and range-for
  loops when they express intent clearly.
- Use concepts and constrained templates only when they make the generic
  contract clearer; avoid template machinery for one call site.
- Minimize casts, macros, implicit narrowing, global mutable state, and unchecked
  indexing. Use the project's warnings, sanitizers, and static-analysis config.
