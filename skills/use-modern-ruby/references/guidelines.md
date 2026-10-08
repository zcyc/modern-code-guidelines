# Ruby

## Gates

- 2.3: # frozen_string_literal: true follows project policy; explicitly duplicate strings that must mutate. Keyword arguments and Enumerable predate this release.
- 2.7: pattern matching (experimental here); follow selected release status and keyword-argument transition behavior.
- 3: positional/keyword separation is required; preserve it across forwarding boundaries. Ractors require explicit shareability/isolation design.
- 3.2: Data for immutable value containers; referenced members may still be mutable.
- 3.4: implicit it for short unambiguous blocks; Prism is the tooling parser baseline.
- 4.0: core Set and Array#rfind/#find; preserve traversal/allocation semantics. Ruby::Box is experimental. *nil no longer delegates to nil.to_a.

Use specific StandardError subclasses for operational failures, not rescue Exception or silent nil. Keep monkey patches/metaprogramming at explicit boundaries; follow configured RuboCop.

## Sources

- [Ruby documentation](https://www.ruby-lang.org/en/documentation/)
- [Ruby 3.4 release](https://www.ruby-lang.org/en/news/2024/12/25/ruby-3-4-0-released/)
- [Ruby 4.0 release](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/)
- [Ruby syntax and core API docs](https://docs.ruby-lang.org/en/)
- [RuboCop style cops](https://docs.rubocop.org/rubocop/latest/cops_style.html)
