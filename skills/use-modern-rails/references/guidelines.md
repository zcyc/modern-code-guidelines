# Rails version rules

Resolve Ruby, Rails, database adapter, and frontend/job stack versions from
Gemfile.lock and the project configuration. Rails 7 and 8 defaults differ in
jobs, assets, and frontend conventions.

## Rails 8.1 feature gate

- Rails 8.1 and later provide Active Job continuations and the structured
  `Rails.event` reporter. Use them only when the target supports them; they do
  not replace the job adapter's durability or the application's logging and
  authorization boundaries.

## Active Record and schema

- Use database constraints and indexes for invariants; model validations alone
  cannot protect concurrent writes.
- Inspect query shape for N+1 access and use eager loading deliberately. Batch
  large reads and writes instead of loading an entire table.
- Append migrations as schema history. Do not rewrite a migration that may have
  run in another environment.

## Requests and jobs

- Use strong parameters and the project's authorization boundary before changing
  records. Callbacks are not access control.
- Active Job provides the application job contract; the actual adapter controls
  durability, retry, scheduling, and concurrency. Make jobs idempotent and pass
  stable identifiers.
- If using Solid Queue or another database-backed adapter, validate queue
  database configuration and transaction timing in the deployment environment.

## Frontend and operations

- Preserve the selected Hotwire/Turbo/Stimulus, Inertia, or API architecture.
  Do not introduce a separate client framework without a concrete requirement.
- Keep credentials, production configuration, and deployment defaults aligned
  with the Rails version and generated application structure.

## Authority

- https://guides.rubyonrails.org/
- https://guides.rubyonrails.org/getting_started.html
- https://guides.rubyonrails.org/active_record_basics.html
- https://guides.rubyonrails.org/active_record_querying.html
- https://guides.rubyonrails.org/active_job_basics.html
- https://guides.rubyonrails.org/upgrading_ruby_on_rails.html
