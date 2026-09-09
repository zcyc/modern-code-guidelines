---
name: use-modern-rails
description: "Use version-aware Ruby on Rails routing, Active Record, jobs, security, Hotwire, and deployment idioms when writing, modifying, fixing, or reviewing Rails code."
---

# Modern Rails

Use for Ruby on Rails applications and engines. Pair with use-modern-ruby for
Ruby rules.

## Target resolution

Read Gemfile, Gemfile.lock, Ruby and Rails versions, database adapter, and
whether the application is full-stack, API-only, Hotwire, or another frontend
architecture. Preserve the app's existing conventions.

## Working rules

- Use Rails conventions and built-in APIs before adding abstractions or gems.
  Keep controllers at the HTTP boundary and add a separate object only when
  the behavior has independent complexity or reuse.
- Treat Active Record validations as application checks, not a substitute for
  database constraints and indexes.
- Inspect query shape for N+1 access, use eager loading deliberately, and batch
  large data operations instead of loading entire tables.
- Treat migrations as schema history: append new migrations and do not rewrite
  migrations that may already have run in another environment.
- Use strong parameters and the project's authorization boundary; do not rely on
  hidden form fields or model callbacks as access control.
- Put slow or retryable work in Active Job. Pass stable identifiers, make jobs
  idempotent, and account for transaction commit timing.
- Prefer the project's Hotwire/Turbo/Stimulus conventions before introducing a
  separate client framework.

Read references/guidelines.md before using version-sensitive Rails, Active Job,
Solid Queue, or deployment behavior.
