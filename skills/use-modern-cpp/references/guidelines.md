# C++

## Ownership and checks

- Use RAII, values and std::unique_ptr; std::shared_ptr requires shared ownership. Raw pointers/references are non-owning unless documented otherwise.
- Non-owning std::string_view/std::span/ranges require valid lifetimes. Preserve ABI and compiler settings; check narrowing and indexing with configured warnings/sanitizers/static analysis.
- Prefer scoped enums, const/constexpr and standard algorithms; concepts should clarify reusable template contracts.

## Standards

- C++11: move semantics, nullptr, enum class, override and standard resource/container types.
- C++14: generic lambdas and expanded constexpr.
- C++17: structured bindings, if constexpr, optional, variant, string_view and filesystem.
- C++20: concepts, ranges, span and format. Coroutines need a runtime that owns scheduling/cancellation.
- C++23: expected for value-or-error boundaries, print, ranges::to and mdspan.
- C++26: reflection, inplace_vector, function_ref and copyable_function require explicit toolchain/library support. Treat draft/experimental modes as opt-in until the selected implementation provides the needed feature.
- Language flags do not prove library availability; check feature-test macros and the exact standard-library implementation.

## Sources

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html)
- [ISO/IEC 14882:2024 (C++23)](https://www.iso.org/standard/83626.html)
- [cppreference C++ language](https://en.cppreference.com/w/cpp/language)
- [cppreference C++ standard library](https://en.cppreference.com/w/cpp/standard_library)
- [WG21 C++26 working papers](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/)
- [C++20 formatting](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2909r4.html)
