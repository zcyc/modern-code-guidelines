# C

## Ownership and checks

- Make allocation sizes, buffer lengths, ownership and cleanup paths explicit; use const and size_t where appropriate. Check bounds, overflow, conversions, allocation and return values. snprintf still requires truncation checks.
- Prefer enums/functions to function-like macros; retain macros for conditional compilation or compile-time operations. Preserve ABI/C linkage.
- Use configured warnings, sanitizers and static analysis; fix causes rather than hiding them with casts.

## Standards

- C99+: designated initializers, static inline, fixed-width types/inttypes and snprintf; restrict requires a valid aliasing contract. Pair buffers with lengths.
- C11+: _Static_assert, atomics and optional threads APIs; verify libc/toolchain support. Memory ordering requires a synchronization design.
- C17 is primarily defect corrections, not a new library/API generation.
- C23: nullptr, auto inference, constexpr objects, attributes, static_assert, typeof/typeof_unqual and #embed require verified compiler support; keep embedded inputs and size explicit.
- C23 library: stdckdint.h for checked arithmetic, stdbit.h for bit operations, memset_explicit for sensitive-data clearing; verify libc availability separately.

## Sources

- [cppreference C language](https://en.cppreference.com/w/c/language)
- [cppreference C23](https://en.cppreference.com/w/c/23)
- [ISO/IEC 9899:2024 (C23)](https://www.iso.org/standard/82075.html)
- [SEI CERT C Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c)
