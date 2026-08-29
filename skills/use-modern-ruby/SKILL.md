---
name: use-modern-ruby
description: Use version-aware Ruby language, standard-library, object-model, and style idioms when writing, modifying, fixing, or reviewing Ruby code.
---

# Modern Ruby

Apply stable Ruby features supported by the package's declared interpreter. Read
`references/guidelines.md` before using version-gated syntax or classes.

## Target resolution

Read the effective target from:

1. `.ruby-version`, `Gemfile` `ruby`, and the gemspec's
   `required_ruby_version`.
2. The selected Ruby image/toolchain in CI or deployment configuration.
3. The target of the gem/application containing the changed file.

If the target is unknown, report it and avoid version-gated syntax. Do not infer
the target from the local Ruby interpreter.

## Working rules

- Follow the repository's RuboCop configuration and run its formatter/lints.
- Prefer `Enumerable`, blocks, keyword arguments, and small objects over manual
  indexing, flag arguments, or duplicated traversal code.
- Use `# frozen_string_literal: true` when it is the repository's established
  policy; make mutable strings explicit at the mutation site.
- Use pattern matching, endless methods, numbered parameters, or `Data` only when
  the target supports them and the result remains clearer than ordinary Ruby.
- Raise and rescue specific exceptions; do not use `rescue Exception` or silently
  turn operational failures into `nil`.
- Keep metaprogramming, monkey patches, and global mutable state at explicit
  boundaries; prefer ordinary methods when they are sufficient.
