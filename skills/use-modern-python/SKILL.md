---
name: use-modern-python
description: "Use for Python code and reviews: interpreter versions, typing, standard-library APIs, and concurrency."
---

# Python

Resolve the changed file's target from package pyproject.toml project.requires-python/Poetry/PDM, setup.cfg/setup.py, then tox.ini/noxfile.py/CI matrix; use the full supported interpreter range.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
