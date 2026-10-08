---
name: use-modern-laravel
description: "Use when writing or reviewing code involving Laravel routing, authorization, Eloquent, migrations, and queues."
---

# Laravel

Resolve the changed file's target from composer.json/lock, PHP/Laravel, bootstrap/config, database, queue backend and Blade/Livewire/Inertia/API stack.

Use only features supported by the declared target/range; report unknowns and verify gated APIs against official versioned docs. Local tools are not target evidence. Keep migrations and unrelated configuration changes outside a local fix. Preview/experimental features require explicit project opt-in.

Use use-modern-php for language; add the matching frontend skill when editing frontend code.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
