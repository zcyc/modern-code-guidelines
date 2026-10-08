---
name: use-modern-flask
description: "Use when writing or reviewing code involving Flask factories, contexts, async views, and WSGI deployment."
---

# Flask

Resolve the changed file's target from Python/Flask and extension versions, packaging/lockfile, configuration, WSGI server or ASGI adapter and async extra.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-python for language and concurrency.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
