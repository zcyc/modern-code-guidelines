# C++ standard rules

Use these rules after resolving the compiler standard and standard-library
implementation. The C++ Core Guidelines are a design baseline; the project build
and ABI remain authoritative.

## C++11+

- Use RAII, scoped objects, move semantics, `nullptr`, `enum class`, `override`,
  `const`, and standard containers where they improve the contract.
- Return values instead of transferring ownership through raw pointers. Make
  ownership explicit with a value or smart pointer.

## C++14+

- Use generic lambdas and `constexpr` where they remove boilerplate without
  hiding control flow.

## C++17+

- Prefer structured bindings, `if constexpr`, `std::optional`, `std::variant`,
  `std::string_view`, and `std::filesystem` when the target provides them.
- Use `std::span` only from C++20; do not substitute a project-specific view type
  without checking the existing codebase first.

## C++20+

- Use concepts for meaningful template constraints, ranges when the pipeline is
  clearer, and `std::span` for bounded non-owning sequences.
- Use coroutines only when the project already has a coroutine runtime contract;
  the language feature alone does not provide scheduling or cancellation.

## C++23+

- Use C++23 library features only when both the compiler and standard library
  support them. Do not assume the compiler's `-std=c++23` flag proves API support.
- Prefer `std::expected` for value-or-error APIs when the project does not use
  exceptions for that boundary.
- Use `std::print`/`std::format`, `std::ranges::to`, `std::mdspan`, and
  other C++23 facilities when they remove local boilerplate and their ownership,
  formatting, or lifetime contracts are explicit.

## C++26 draft

- Treat C++26 as a draft/toolchain mode until the project explicitly adopts a
  conforming implementation; do not introduce `-std=c++2c` features in ordinary
  production code.
- Keep reflection, `std::inplace_vector`, `std::function_ref`, `std::copyable_function`,
  and other C++26 facilities behind explicit compiler/standard-library support;
  test the exact toolchain rather than relying on the language-mode flag alone.

## Authority

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html)
- [ISO/IEC 14882:2024 (C++23)](https://www.iso.org/standard/83626.html)
- [cppreference C++ language](https://en.cppreference.com/w/cpp/language)
- [cppreference C++ standard library](https://en.cppreference.com/w/cpp/standard_library)
- [WG21 C++26 working papers](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/)
