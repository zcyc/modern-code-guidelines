---
name: use-modern-ruby
description: "Use when writing or reviewing code involving Ruby language versions, value objects, keyword arguments, and gem boundaries."
---

# Ruby

Resolve the changed file's target from .ruby-version, Gemfile ruby, gemspec required_ruby_version, lockfile, RuboCop and selected CI/deployment target; distinguish application pin from gem support range.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
