---
name: use-modern-python
description: "Use version-aware Python language, standard-library, typing, and concurrency idioms when writing, modifying, fixing, or reviewing Python code."
---

# Modern Python

Apply stable Python patterns supported by the project's explicit interpreter
range. Read `references/guidelines.md` before using version-gated syntax or APIs.

## Target resolution

Read the declared target from the project, in this order:

1. `pyproject.toml` `project.requires-python` or Poetry/PDM equivalent.
2. Packaging metadata in `setup.cfg`/`setup.py` when it is the source of truth.
3. An explicit matrix in `tox.ini`, `noxfile.py`, or checked-in CI configuration.

Use the target of the package/module being changed. If no target is declared, report
the Python target as unknown and avoid version-gated syntax. Do not infer it from the
local interpreter.

## Working rules

- Prefer the standard library (`pathlib`, `dataclasses`, `contextlib`, `zoneinfo`, `collections.abc`) before adding a dependency.
- Use type annotations to express contracts, not to pretend runtime validation happened.
- Use `ExceptionGroup`/`TaskGroup` only when the target supports them and the operation really has concurrent child failures.
- Keep cancellation and resource lifetime explicit in async code; do not swallow `CancelledError` as an ordinary failure.
- Prefer timezone-aware `datetime` values for instants and model date-only values as dates.
- Use small, direct functions; do not add frameworks or compatibility branches for versions outside the declared target.
