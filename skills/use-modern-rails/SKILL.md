---
name: use-modern-rails
description: "Use when writing or reviewing code involving Rails requests, Active Record, jobs, migrations, and frontend conventions."
---

# Rails

Resolve the changed file's target from Gemfile/lock, Ruby/Rails, database adapter, job adapter and full-stack/API/Hotwire/other frontend architecture.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-ruby for language; add the matching frontend skill for client code.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
