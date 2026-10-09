---
name: use-modern-flask
description: "Use for Flask code and reviews: factories, request contexts, async views, and WSGI deployment."
---

# Flask

Resolve the changed file's target from Python/Flask and extension versions, packaging/lockfile, configuration, WSGI server or ASGI adapter and async extra.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-python for language and concurrency.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
