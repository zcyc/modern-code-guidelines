# C standard rules

Use these rules after resolving the compiler standard, libc, ABI, and warning
configuration. Secure coding rules are correctness requirements at boundaries,
not permission to rewrite a whole legacy codebase.

## C99+

- Use designated initializers, `static inline`, `restrict` only with a documented
  aliasing contract, and `snprintf` where they improve correctness.
- Keep array lengths paired with buffers; prefer an explicit span-like `(pointer,
  count)` contract when no project type exists.

## C11+

- Use `_Static_assert`, `<stdint.h>`, `<inttypes.h>`, `<stdatomic.h>`, and
  `<threads.h>` only when the target libc/toolchain provides them.
- Treat atomics and memory ordering as a synchronization design, not a compiler
  warning workaround.

## C17+

- Prefer the C17 standard library and diagnostics where supported, but do not
  claim portability to a libc merely because the compiler accepts the syntax.

## C23+

- Use `nullptr`, `auto` type inference, `constexpr` objects, attributes,
  `static_assert`, `typeof`/`typeof_unqual`, and other C23 features only
  with an explicit C23 target and a verified toolchain/libc.
- Prefer `<stdckdint.h>` for checked integer arithmetic and `<stdbit.h>` for
  standard bit operations when they express the overflow/bit contract directly.
- Use `memset_explicit` when clearing sensitive data must not be optimized away;
  verify that the target libc actually provides it.
- Use `#embed` only for deliberate compile-time binary embedding with a clear
  size and build-input contract.
- Do not make C23 the default for a project whose build target is unspecified.

## Authority

- [cppreference C language](https://en.cppreference.com/w/c/language)
- [cppreference C23](https://en.cppreference.com/w/c/23)
- [ISO/IEC 9899:2024 (C23)](https://www.iso.org/standard/82075.html)
- [SEI CERT C Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c)
