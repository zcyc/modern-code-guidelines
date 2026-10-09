---
name: use-modern-rails
description: "Use for Rails code and reviews: requests, Active Record, jobs, migrations, and frontend integration."
---

# Rails

Resolve the changed file's target from Gemfile/lock, Ruby/Rails, database adapter, job adapter and full-stack/API/Hotwire/other frontend architecture.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-ruby for language; add the matching frontend skill for client code.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
