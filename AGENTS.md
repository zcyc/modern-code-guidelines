# Modern Code Guidelines

Use this repository's `skills/` directory as the source of version-aware coding
guidance.

When a task changes code:

1. Resolve the target language, framework, and runtime from checked-in project metadata.
2. Read the matching `skills/use-modern-*/SKILL.md`.
3. After resolving the target, read that skill's `references/guidelines.md`.
4. Apply only the guidance relevant to the changed code and keep the diff focused.
5. When language and framework skills both apply, use both; framework guidance is
   additional to the language guidance.
6. If the target is unknown, state that it is unknown and avoid version-gated APIs.

Keep `AGENTS.md` or `GEMINI.md` next to `skills/` when using this repository with
one of the supported agents listed in the README. The files are entry points,
not a second copy of the rules.
