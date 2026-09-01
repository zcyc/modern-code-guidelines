---
name: use-modern-fastapi
description: "Use version-aware FastAPI routing, Pydantic validation, dependency, async, lifecycle, security, and OpenAPI idioms when writing, modifying, fixing, or reviewing FastAPI code."
---

# Modern FastAPI

Use for FastAPI applications and packages. Pair with use-modern-python for
Python and typing rules.

## Target resolution

Read pyproject.toml or equivalent metadata, lockfile, Python target, FastAPI,
Starlette, and Pydantic versions. Establish the ASGI server and the project's
lifespan, dependency, and schema conventions before changing an endpoint.

## Working rules

- Treat type annotations and Pydantic models as the HTTP contract. Validate
  untrusted input and keep request, response, and persistence models distinct
  when their trust or shape differs.
- Use response models and accurate status codes so serialization and OpenAPI
  describe the behavior clients receive.
- Use async def for awaitable I/O; keep blocking calls out of async functions.
  A plain def path operation or dependency is appropriate when the blocking
  library should run through FastAPI's threadpool behavior.
- Use Depends for request-scoped dependencies and yield-based dependencies for
  resources that need cleanup. Avoid mutable global request state.
- Use the lifespan mechanism supported by the installed version for startup and
  shutdown resources. Do not use durable jobs as a substitute for a real queue.
- Keep authentication, authorization, CORS, and secret handling at the boundary;
  never expose internal exception details by default.

Read references/guidelines.md before using version-gated Pydantic or lifecycle APIs.
