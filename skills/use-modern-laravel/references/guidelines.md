# Laravel version rules

Resolve PHP, Laravel, Composer dependencies, database, queue backend, and
frontend stack from composer.lock and the project configuration. Laravel's
bootstrap and starter-kit conventions change across major versions.

## Application-structure gate

- Laravel 11 and later configure high-level routing, middleware, exceptions,
  and providers through `bootstrap/app.php` and `bootstrap/providers.php` in a
  new application. Do not copy older `app/Http/Kernel.php`, exception-handler,
  or provider-registration instructions into that structure.
- Existing applications may retain the older layout. Follow the files present
  in the repository rather than migrating structure as part of an unrelated
  feature.

## Application boundaries

- Use named routes, middleware, Form Requests, policies, and gates where they
  match the application's established boundary model.
- Eloquent model validation does not replace database constraints. Use indexes,
  foreign keys, and unique constraints for invariants the database must protect.
- Keep env reads in configuration and use the resolved config at runtime. Do not
  expose private config through Inertia, Livewire, or frontend build variables.

## Persistence and jobs

- Inspect relationship loading and query count; eager-load only the relationships
  needed for the response and avoid serializing an accidental graph.
- Migrations are deployed schema history. Add new migrations instead of
  rewriting migrations that may already have run.
- Queue jobs that are safe to retry, pass stable identifiers, and dispatch after
  commit when they depend on newly committed database state.

## Frontend choices

- Preserve the project's Blade, Livewire, Inertia, or API architecture. Do not
  add a second frontend stack for a single screen.
- Use official starter-kit patterns only when the project has chosen that stack;
  generated authentication code still needs project-specific authorization review.

## Authority

- https://laravel.com/docs
- https://laravel.com/docs/routing
- https://laravel.com/docs/validation
- https://laravel.com/docs/authorization
- https://laravel.com/docs/eloquent-relationships
- https://laravel.com/docs/queues
- https://laravel.com/docs/migrations
