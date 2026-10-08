---
name: use-modern-fastapi
description: "Use when writing or reviewing code involving FastAPI validation, dependencies, lifespan, and async endpoints."
---

# FastAPI

Resolve the changed file's target from pyproject.toml/packaging, lockfile, Python/FastAPI/Starlette/Pydantic, ASGI server and dependency/lifespan conventions.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-python for language and typing.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
