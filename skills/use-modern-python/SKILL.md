---
name: use-modern-python
description: "Use when writing or reviewing code involving Python version ranges, typing, standard APIs, and concurrency."
---

# Python

Resolve the changed file's target from package pyproject.toml project.requires-python/Poetry/PDM, setup.cfg/setup.py, then tox.ini/noxfile.py/CI matrix; use the full supported interpreter range.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
