---
name: use-modern-laravel
description: "Use for Laravel code and reviews: routing, authorization, Eloquent, migrations, and queues."
---

# Laravel

Resolve the changed file's target from composer.json/lock, PHP/Laravel, bootstrap/config, database, queue backend and Blade/Livewire/Inertia/API stack.

Respect the declared target range; if unknown, report it and avoid version-gated APIs. Verify gated APIs in official versioned docs. Installed tools do not establish the target. Keep unrelated migrations/config changes out of local fixes. Preview/experimental features require explicit project opt-in.

Use use-modern-php for language; add the matching frontend skill when editing frontend code.

For browser APIs/CSS/accessibility/performance, consult official browser docs or the separately installed modern-web-guidance.

Read [references/guidelines.md](references/guidelines.md) before applying rules. Run the project's existing checks for the changed behavior.
