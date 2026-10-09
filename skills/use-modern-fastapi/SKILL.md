---
name: use-modern-fastapi
description: "Use for FastAPI code and reviews: validation, dependencies, lifespan, and async endpoints."
---

# FastAPI

Resolve the changed file's target from pyproject.toml/packaging, lockfile, Python/FastAPI/Starlette/Pydantic, ASGI server and dependency/lifespan conventions.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-python for language and typing.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
