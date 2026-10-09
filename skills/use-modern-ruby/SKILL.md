---
name: use-modern-ruby
description: "Use for Ruby code and reviews: language versions, value objects, keyword arguments, and gem boundaries."
---

# Ruby

Resolve the changed file's target from .ruby-version, Gemfile ruby, gemspec required_ruby_version, lockfile, RuboCop and selected CI/deployment target; distinguish application pin from gem support range.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
