---
name: use-modern-sql
description: Use dialect-aware SQL query, schema, transaction, and safety idioms when writing, modifying, fixing, or reviewing SQL code.
---

# Modern SQL

Apply portable SQL structure first, then the selected database dialect's actual
syntax and behavior. Read `references/guidelines.md` before using dialect- or
version-specific features.

## Target resolution

Read the effective database target from, in order:

1. Migration headers, schema metadata, ORM/database configuration, and SQLFluff
   `dialect` settings.
2. The database engine/version declared in container, CI, or deployment config.
3. The target of the migration/query module being changed.

SQL has no single runtime target. If the dialect or version is unknown, report it
and avoid vendor-specific syntax. Treat generated SQL and application SQL as the
same trust boundary: values must be bound parameters.

## Working rules

- Bind values through the database driver's parameter API; never concatenate
  untrusted values into SQL.
- Select explicit columns, qualify ambiguous names, use explicit join types and
  conditions, and alias expressions with stable names.
- Use `IS NULL`/`IS NOT NULL` for null tests and reason about three-valued logic;
  do not assume `NULL = NULL` is true.
- Add `ORDER BY` whenever result order is part of the contract, especially with
  `LIMIT`/`OFFSET` or pagination.
- Use constraints, foreign keys, transactions, and migration checks to protect
  data invariants; make destructive schema changes explicit and reversible where
  the deployment process requires it.
- Prefer CTEs, window functions, and set-based operations when they make the
  relational intent clearer. Measure plans before adding indexes or rewriting a
  query for presumed performance.
- Follow the repository's formatter/linter and configured dialect; do not impose a
  capitalization or comma style that conflicts with it.
