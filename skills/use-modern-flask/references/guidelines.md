# Flask

## Structure and contexts

- Factories support multiple configs/test instances and late extension init; use init_app instead of import-order-dependent binding.
- Blueprints group route/error boundaries; business rules remain usable outside requests.
- request/session/current_app/g require their documented contexts. Store owned request resources on g and close in teardown.
- Validate headers/path/query/body/forms; preserve Jinja HTML autoescaping. CORS is neither authentication nor CSRF protection; apply explicit browser mutation policies.

## Versions and deployment

- Async views require Flask 2.0+ and the async extra; extension decorators must also support async. WSGI still occupies one worker per request and stops the per-request event loop after the view.
- Use a durable queue for background jobs; an explicit ASGI adapter can support an ongoing loop, but does not make jobs durable.
- Map expected failures to deliberate statuses, log unexpected causes server-side and hide tracebacks/secrets. flask run is development-only; use a production WSGI server or explicit ASGI adapter and trusted-proxy header config.
- Test via fresh configured factory instances/client and explicit contexts; reset database/filesystem/environment state.

## Sources

- https://flask.palletsprojects.com/en/stable/
- https://flask.palletsprojects.com/en/stable/patterns/appfactories/
- https://flask.palletsprojects.com/en/stable/appcontext/
- https://flask.palletsprojects.com/en/stable/reqcontext/
- https://flask.palletsprojects.com/en/stable/async-await/
- https://flask.palletsprojects.com/en/stable/testing/
