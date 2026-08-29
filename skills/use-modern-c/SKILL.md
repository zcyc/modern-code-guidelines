---
name: use-modern-c
description: Use version-aware C language, standard-library, memory-safety, and secure-coding idioms when writing, modifying, fixing, or reviewing C code.
---

# Modern C

Apply stable C features supported by the translation unit's actual language
standard, compiler, and libc. Read `references/guidelines.md` before using
standard-version-gated syntax or APIs.

## Target resolution

Read the effective target for the file:

1. `C_STANDARD` and compiler/toolchain settings in CMake, Meson, Make, Bazel, or
   the project's build files.
2. The actual compile command or checked-in `compile_commands.json`.
3. Explicit `-std=` flags, libc targets, and warning/sanitizer settings in CI.

If the target is unknown, report it and avoid C23-only features. Do not infer the
target from the local compiler. Preserve the project's ABI and C linkage contract.

## Working rules

- Make ownership, allocation, lifetime, and cleanup visible in API contracts;
  pair every acquired resource with one cleanup path.
- Use `const`, `size_t`, fixed-width integer types where representation matters,
  designated initializers, `static inline`, and `_Static_assert` when supported.
- Check allocation, conversion, bounds, format strings, and return values at trust
  boundaries. Use `snprintf` and bounded operations with verified sizes.
- Prefer enums and functions over magic-number or function-like macro machinery;
  keep macros for conditional compilation and genuinely compile-time operations.
- Compile with the repository's highest warning set and use sanitizers/static
  analysis where configured. Do not hide warnings with broad casts or suppressions.
