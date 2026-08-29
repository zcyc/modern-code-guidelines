# SQL dialect rules

Use these rules after resolving the database engine/version and the project's
formatter configuration. Portable SQL and vendor extensions must stay visibly
separate.

## SQL:2023+

- Treat SQL:2023 as the portable reference point, not as a promise that a
  database implements every feature. Resolve the actual engine/version before
  using JSON, temporal, graph, routine, or other optional feature areas.
- Keep standard SQL separate from vendor extensions in migrations and queries;
  document the required dialect when portability is not the goal.

## Portable SQL

- Use bound parameters for values and allow-list/quote identifiers through the
  driver's identifier API when dynamic identifiers are unavoidable.
- Prefer explicit select lists, qualified columns, explicit `JOIN ... ON`, and
  deterministic `ORDER BY` clauses.
- Preserve null semantics: use `IS NULL`, `IS NOT NULL`, `COALESCE`, and `NULLIF`
  only when their exact missing-value behavior is intended.
- Use constraints for invariants that the database can enforce; validate complex
  business rules in the owning application/service as well.
- Keep migrations transactional where the engine supports it and document locking,
  table-rewrite, and backfill costs for production-sized tables.

## Query structure

- Use CTEs to name meaningful stages, not to wrap a single expression for style.
- Use window functions for per-row aggregates/ranking instead of correlated loops
  in application code when the database can express the relation directly.
- Avoid `SELECT *` in stable application/report contracts; it couples consumers to
  schema drift. Exploratory queries are a separate case.
- Add `ORDER BY` before limiting or paginating; row order without it is undefined.

## Tooling

- Use SQLFluff or the repository's equivalent with the configured dialect.
- Use `EXPLAIN`/execution plans and representative data before making a performance
  claim or adding an index.

## Authority

- [SQLFluff rules reference](https://docs.sqlfluff.com/en/stable/reference/rules.html)
- [ISO/IEC 9075:2023 SQL standard](https://www.iso.org/standard/76583.html)
- [PostgreSQL sorting rows](https://www.postgresql.org/docs/current/queries-order.html)
- [PostgreSQL release notes](https://www.postgresql.org/docs/release/)
