---
name: use-modern-sql
description: "Use for SQL code and reviews: dialects, queries, constraints, transactions, and migrations."
---

# SQL

Resolve the changed file's target from migration/schema metadata, ORM/database config, SQLFluff dialect, container/CI/deployment engine/version and query module. Check the actual engine, not SQL standard version alone.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
