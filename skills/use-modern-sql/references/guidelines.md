# SQL

## Dialect and trust boundaries

- SQL:2023 is a reference, not an engine capability guarantee. Check vendor/version support for JSON, temporal, graph and routine features; document intentional dialect dependence.
- Bind values; allow-list/quote dynamic identifiers with driver APIs. Types/ORM-generated SQL do not remove injection boundaries.
- Use explicit columns/joins/aliases and qualified ambiguous names. NULL uses three-valued logic: use IS NULL/IS NOT NULL and deliberate COALESCE/NULLIF semantics.
- Order contractual results explicitly; pagination needs a deterministic tie-breaker, not ORDER BY on a non-unique field alone.

## Data and plans

- Enforce invariants with constraints/foreign keys and transactions; application checks alone cannot protect concurrent writes.
- Transactions alone do not prevent lost updates or write skew. For read-modify-write invariants, choose atomic conditional updates, appropriate locks or isolation for the selected engine; check affected rows and retry the whole transaction on documented retryable conflicts with bounded attempts. Keep external side effects outside retried transactions or make them idempotent.
- Keep deployed migrations as history. Review destructive changes, locks, rewrites and backfills at production scale; use transactions/reversibility where the engine/deployment permits.
- CTEs name meaningful stages; window/set operations can replace application loops. Avoid SELECT * in stable consumer contracts.
- Use representative EXPLAIN plans before performance claims/index additions; follow the configured SQLFluff/equivalent dialect and style.

## Sources

- [SQLFluff rules reference](https://docs.sqlfluff.com/en/stable/reference/rules.html)
- [ISO/IEC 9075:2023 SQL standard](https://www.iso.org/standard/76583.html)
- [PostgreSQL sorting rows](https://www.postgresql.org/docs/current/queries-order.html)
- [PostgreSQL release notes](https://www.postgresql.org/docs/release/)
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
