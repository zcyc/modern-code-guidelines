# FastAPI

## Model and dependency gates

- Pydantic 2 uses model_validate/model_dump/model_config; retain Pydantic 1 APIs only in explicitly v1 projects. Upgrades are separate migrations, with no invisible model-generation mixing.
- Annotated metadata needs supporting Python/FastAPI versions. Request/response/persistence models differ when shape/trust differs; keep response models/statuses/OpenAPI truthful.
- Depends constructs reusable dependencies; yield owns cleanup. Request data stays request-scoped, while shared app resources follow lifespan ownership.
- Prefer lifespan over deprecated startup/shutdown events on supporting releases. Check yield-dependency cleanup timing against streaming responses and the installed FastAPI version.

## Async and security

- async def awaits non-blocking I/O; plain def endpoints/dependencies run blocking libraries through the threadpool. Ordinary helpers called inside async def are not automatically offloaded.
- In-process BackgroundTasks are not durable/retried across process failure; use a persistent queue for required survival/retry.
- Validate input, authenticate/authorize operations and configure CORS separately; keep internal exceptions/secrets out of responses.

## Sources

- https://fastapi.tiangolo.com/
- https://fastapi.tiangolo.com/async/
- https://fastapi.tiangolo.com/tutorial/dependencies/
- https://fastapi.tiangolo.com/advanced/events/
- https://fastapi.tiangolo.com/tutorial/response-model/
