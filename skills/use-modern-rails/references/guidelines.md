# Rails

## Gates

- Rails 8.1 adds Active Job continuations and Rails.event reporting; adapters still determine durability/retry and operational behavior.
- Resolve version defaults for jobs/assets/frontend and actual generated app structure before adopting examples.

## Requests, data and jobs

- Controllers orchestrate requests; strong parameters limit assignable fields, while policies/authorization decide permitted operations. Hidden fields/callbacks are not access control.
- Constraints/indexes protect concurrent writes; model validation alone cannot. Inspect N+1 loading, eager-load deliberately and batch large operations.
- Append deployed migration history. Active Job jobs use stable IDs/idempotency and explicit commit timing; verify Solid Queue/other adapter database, scheduling/concurrency and durability settings.
- Preserve Hotwire/Turbo/Stimulus/Inertia/API conventions; new objects/gems/frameworks need actual complexity/reuse. Keep deployment credentials/config private.

## Sources

- https://guides.rubyonrails.org/
- https://guides.rubyonrails.org/getting_started.html
- https://guides.rubyonrails.org/active_record_basics.html
- https://guides.rubyonrails.org/active_record_querying.html
- https://guides.rubyonrails.org/active_job_basics.html
- https://guides.rubyonrails.org/upgrading_ruby_on_rails.html
