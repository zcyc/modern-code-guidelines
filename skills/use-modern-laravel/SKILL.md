---
name: use-modern-laravel
description: "Use version-aware Laravel routing, validation, authorization, Eloquent, queues, and config idioms when writing, modifying, fixing, or reviewing Laravel code."
---

# Modern Laravel

Use for Laravel applications and packages. Pair with use-modern-php for PHP
rules and modern-web-guidance for browser-platform decisions.

## Target resolution

Read composer.json, composer.lock, PHP version, Laravel version, the selected
frontend stack, database, queue driver, and application bootstrap/configuration.
Preserve the project's Blade, Livewire, Inertia, or API architecture.

## Working rules

- Keep routes and controllers focused on request orchestration; use the
  project's existing action/service pattern only when the behavior has real
  complexity or reuse.
- Validate with Form Requests or the project's established boundary mechanism,
  and authorize with policies/gates before privileged model changes.
- Treat Eloquent relationships as query boundaries: define needed relationships,
  prevent N+1 queries, and use database constraints for invariants.
- Keep migrations append-only for deployed schemas. Use transactions where the
  database can preserve a multi-step invariant.
- Send slow, retryable work to queues; make jobs idempotent and account for
  transaction commit timing before dispatching dependent jobs.
- Read environment variables through configuration, not throughout application
  code. Keep secrets out of config that is exposed to frontend builds.

Read references/guidelines.md before using version-sensitive Laravel bootstrap,
queue, starter-kit, or frontend integration behavior.
