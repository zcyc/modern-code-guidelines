# Ruby version rules

Use these rules after resolving the project's Ruby target and RuboCop config.
Ruby syntax and framework/gem APIs are separate constraints.

## Ruby 2.3+

- Use `# frozen_string_literal: true` when the project enables it and duplicate a
  string explicitly before mutation.
- Prefer keyword arguments and `Enumerable` operations when they make the call
  contract and traversal clear.

## Ruby 2.7+

- Use pattern matching only for data shapes where `case`/`when` would otherwise
  obscure the structure; keep keyword-argument behavior aligned with the target.

## Ruby 3+

- Preserve the separation between positional and keyword arguments at public
  boundaries; do not rely on implicit hash-to-keyword conversion.
- Use Ractors only when the application has an explicit isolation and shareability
  design; ordinary threads/fibers do not become safer automatically.

## Ruby 3.2+

- Use `Data` for small immutable value objects when the target provides it and a
  `Struct` or class would add no needed behavior.

## Ruby 3.4+

- Use the implicit `it` block parameter only for a short, unambiguous
  single-argument block; keep an explicit parameter for nested or multi-argument
  logic.
- Treat Prism as the Ruby 3.4 parser baseline for tooling, but do not make
  parser-specific behavior part of application semantics.

## Ruby 4.0+

- Use `Set` as a core collection and `Array#rfind`/`Array#find` when they express
  the traversal directly; keep the older form when its allocation or order
  behavior is part of the contract.
- Treat `Ruby::Box` as experimental isolation infrastructure; do not introduce it
  for ordinary object organization or as a substitute for package boundaries.
- Remember that `*nil` no longer converts through `nil.to_a`; make splat inputs
  explicit when nil is a possible value.

## Authority

- [Ruby documentation](https://www.ruby-lang.org/en/documentation/)
- [Ruby 3.4 release](https://www.ruby-lang.org/en/news/2024/12/25/ruby-3-4-0-released/)
- [Ruby 4.0 release](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/)
- [Ruby syntax and core API docs](https://docs.ruby-lang.org/en/)
- [RuboCop style cops](https://docs.rubocop.org/rubocop/latest/cops_style.html)
