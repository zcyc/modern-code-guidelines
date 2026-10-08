# Laravel

## Structure gates

- New Laravel 11+ apps configure routing/middleware/exceptions in bootstrap/app.php and providers in bootstrap/providers.php; existing apps may retain older kernels/handlers. Follow actual structure.
- Laravel 13 requires PHP 8.3+; verify PHP/framework/packages together.

## Boundaries and persistence

- Routes/controllers orchestrate HTTP; Form Requests validate and policies/gates authorize. Actions/services need independent complexity/reuse.
- Model validation does not replace database constraints/foreign keys/unique indexes. Inspect loading/query count and eager-load only needed relationships.
- Append deployed migrations; use transactions for multi-step invariants. Queue jobs use stable IDs/idempotency and dispatch after commit when dependent on committed data.
- Read env only in configuration and use resolved config at runtime. Do not expose private settings through frontend builds/Inertia/Livewire.
- Preserve Blade/Livewire/Inertia/API architecture; starter kits do not supply application-specific authorization automatically.

## Sources

- https://laravel.com/framework/docs/releases
- https://laravel.com/docs
- https://laravel.com/docs/routing
- https://laravel.com/docs/validation
- https://laravel.com/docs/authorization
- https://laravel.com/docs/eloquent-relationships
- https://laravel.com/docs/queues
- https://laravel.com/docs/migrations
