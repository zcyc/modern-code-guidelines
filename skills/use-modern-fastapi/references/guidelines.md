# FastAPI version rules

Resolve FastAPI, Starlette, Pydantic, Python, and ASGI server versions before
using their APIs. FastAPI behavior often depends on all of these layers.

## Pydantic generation boundary

- When the project uses Pydantic 2, use `model_validate`, `model_dump`, and
  `model_config`; do not copy Pydantic 1 examples using `parse_obj`, `dict`, or
  inner `Config` into that codebase.
- If a maintained project is intentionally on Pydantic 1, follow its declared
  API consistently and treat a Pydantic upgrade as a separate migration. Do
  not mix model generations in one boundary.

## Contracts and dependencies

- Use Pydantic models for boundary validation and response serialization. Keep
  the OpenAPI schema truthful; do not hide incompatible responses with broad
  unions or unchecked dictionaries.
- Prefer `typing.Annotated` for reusable dependencies and parameter metadata
  when the project's Python and FastAPI targets support it; keep the dependency
  contract visible in the type annotation.
- Prefer Depends for reusable request-bound construction and yield dependencies
  for cleanup. Do not use a module-global mutable object as a request cache.
- Use lifespan for application-wide resource startup and shutdown when supported
  by the installed version.

## Async

- Awaitable external libraries belong in async endpoints. Blocking libraries
  belong in plain def endpoints/dependencies or an explicit executor boundary.
- Do not assume background tasks are durable, retried, or observable; use a
  queue for work that must survive process failure.

## Authority

- https://fastapi.tiangolo.com/
- https://fastapi.tiangolo.com/async/
- https://fastapi.tiangolo.com/tutorial/dependencies/
- https://fastapi.tiangolo.com/advanced/events/
- https://fastapi.tiangolo.com/tutorial/response-model/
