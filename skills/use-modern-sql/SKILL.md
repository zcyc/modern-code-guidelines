---
name: use-modern-sql
description: "Use when writing or reviewing code involving SQL dialects, queries, constraints, transactions, and migrations."
---

# SQL

Resolve the changed file's target from migration/schema metadata, ORM/database config, SQLFluff dialect, container/CI/deployment engine/version and query module. Check the actual engine, not SQL standard version alone.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
