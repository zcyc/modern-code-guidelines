# Modern Code Guidelines

[简体中文](README.zh-CN.md)

A shared skill package for Codex, Cursor, Claude Code, Kiro, Google Antigravity,
Gemini CLI, GitHub Copilot, Cline, OpenCode, Devin, JetBrains Junie, and OpenHands,
containing forty-two independently triggered language and framework skills:

- Codex: `.codex-plugin/plugin.json`
- Cursor: `.cursor-plugin/plugin.json`
- Claude Code: `.claude-plugin/plugin.json`

Canonical sources and distribution entry points:

- `skills/`: the canonical Agent Skills source directory.
- `AGENTS.md`: always-on project guidance when this repository is opened directly.
- `GEMINI.md`: Gemini CLI context for a direct checkout; it imports `AGENTS.md`.
- `npx skills`: installs only the canonical `skills/` directory into selected host paths.
- Plugin manifests: Codex, Cursor, and Claude Code.

Marketplace catalogs are provided for direct repository or local installation:

- Codex: `.agents/plugins/marketplace.json`
- Cursor: `.cursor-plugin/marketplace.json`
- Claude Code: `.claude-plugin/marketplace.json`

This project is distributed directly from its repository and is not submitted to
the official plugin stores.

## Installation

The repository is hosted at
[`zcyc/modern-code-guidelines`](https://github.com/zcyc/modern-code-guidelines).
The marketplace name is `modern-code-guidelines` for all three hosts.

### Codex

Run these commands in a terminal. The first command adds the repository marketplace;
the second installs the plugin:

```bash
codex plugin marketplace add zcyc/modern-code-guidelines
codex plugin add modern-code-guidelines@modern-code-guidelines
```

For a local checkout, replace `zcyc/modern-code-guidelines` with its absolute path.

### Cursor

Add the repository marketplace from a terminal, then install the plugin from Cursor's
`/plugins` interface:

```bash
cursor-agent plugin marketplace add https://github.com/zcyc/modern-code-guidelines
```

Open `/plugins`, select the `modern-code-guidelines` marketplace, and install
`modern-code-guidelines`.

### Claude Code

Run these commands inside a Claude Code session:

```text
/plugin marketplace add zcyc/modern-code-guidelines
/plugin install modern-code-guidelines@modern-code-guidelines
```

For a local checkout, use its absolute path with `/plugin marketplace add`.

### Updating

Refresh the marketplace before reinstalling or updating the plugin:

```bash
# Codex
codex plugin marketplace upgrade modern-code-guidelines
codex plugin remove modern-code-guidelines@modern-code-guidelines
codex plugin add modern-code-guidelines@modern-code-guidelines

# Claude Code
claude plugin marketplace update modern-code-guidelines
claude plugin update modern-code-guidelines@modern-code-guidelines
```

For Cursor, run `cursor-agent plugin marketplace update modern-code-guidelines`,
then reopen Cursor and reinstall from `/plugins` if the cached version does not
change.

### Native Agent Skills (`npx skills`)

```bash
# Run from the target project's root.
# Interactive installation:
npx skills add zcyc/modern-code-guidelines

# Install all skills into one host.
npx skills add zcyc/modern-code-guidelines \
  --skill '*' \
  --agent gemini-cli \
  --yes

# Supported values for --agent:
# codex cursor claude-code gemini-cli antigravity kiro-cli
# github-copilot cline opencode devin junie openhands

# Install all skills into this project's supported hosts.
npx skills add zcyc/modern-code-guidelines \
  --skill '*' \
  --agent codex cursor claude-code gemini-cli antigravity kiro-cli \
  --agent github-copilot cline opencode devin junie openhands \
  --yes

# Verify and update.
npx skills ls -a gemini-cli
npx skills update

# Use --copy when symlinks are unavailable.
npx skills add zcyc/modern-code-guidelines --skill '*' --agent gemini-cli --copy
```

## Skills

Language skills (17):

- `use-modern-java`
- `use-modern-javascript`
- `use-modern-typescript`
- `use-modern-python`
- `use-modern-csharp`
- `use-modern-go`
- `use-modern-rust`
- `use-modern-scala`
- `use-modern-cpp`
- `use-modern-swift`
- `use-modern-kotlin`
- `use-modern-dart`
- `use-modern-php`
- `use-modern-ruby`
- `use-modern-c`
- `use-modern-sql`
- `use-modern-shell`

Framework skills (25):

- `use-modern-react`
- `use-modern-nextjs`
- `use-modern-vue`
- `use-modern-angular`
- `use-modern-spring-boot`
- `use-modern-aspnet-core`
- `use-modern-django`
- `use-modern-fastapi`
- `use-modern-express`
- `use-modern-flask`
- `use-modern-flutter`
- `use-modern-uikit`
- `use-modern-appkit`
- `use-modern-swiftui`
- `use-modern-swiftdata`
- `use-modern-ktor`
- `use-modern-nestjs`
- `use-modern-nuxt`
- `use-modern-expo`
- `use-modern-react-native`
- `use-modern-sveltekit`
- `use-modern-astro`
- `use-modern-jetpack-compose`
- `use-modern-laravel`
- `use-modern-rails`

Language skills read the project's explicit language/compiler/runtime target.
Framework skills additionally resolve the framework, build tool, deployment
target, and project architecture before applying version-sensitive guidance.
Version-specific references stay beside each skill. Entry points resolve targets
and route to those references; rules are maintained only in the references.
Each installed skill carries its own target/unknown-version policy and does not
depend on this repository's root `AGENTS.md` being copied into the project.

Install the companion skills named by your selected skill when using selective
installation. TypeScript adds compiler/type rules to JavaScript runtime guidance;
Expo adds SDK/build/update rules to React Native. `use-modern-sveltekit` covers
standalone Svelte too, with Kit rules applied only to Kit projects.

Apple skills are layered: use `use-modern-swift` for the language, then add
only the frameworks present in the target. Keep SwiftUI, UIKit, and AppKit
separate because their lifecycle and platform rules differ; keep SwiftData
separate because persistence and migration have different boundaries.

The JavaScript skill covers core ECMAScript and Node.js. TypeScript has its own skill
for compiler/type-system behavior. For browser APIs, CSS, accessibility, and web
performance, consult official browser documentation or the separately installed
[`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance).
That skill is optional and is not bundled or installed by this package.

## Rule sources

Each skill resolves the project's declared target before applying its local rules.
Version and API sources live beside those rules in each skill's
`references/guidelines.md` under [skills/](skills/).

Use official language/framework specifications, release notes, compiler docs and
runtime/platform API docs as primary sources. Secondary guidance can supplement
examples but does not override the project's target or primary sources.

Maintain rules that guide a coding decision: when to adopt an API, its version
and runtime requirements, and behavior or safety boundaries. Release highlights
alone do not justify a rule; keep exact source links with the rule they support.

## Relationship to related projects

This project was inspired by [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines)
and [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance). It
complements both projects rather than replacing them:

- [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) focuses on
  modern Go language and standard-library guidance.
- [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) focuses on
  browser and web-platform practices such as Web APIs,
  CSS, accessibility, and web performance.
- `modern-code-guidelines` focuses on version-aware language, compiler, runtime,
  standard-library, database, and secure-coding guidance across the listed languages.
  Its Go rules use official Go documentation as the authority, with JetBrains
  `go-modern-guidelines` as supplementary reference; the official Go toolchain
  is used only for the most suitable formatting, testing, and correctness checks.

The JavaScript and TypeScript skills intentionally stop at core language, compiler,
Node.js, and runtime concerns. Browser UI, CSS, accessibility, and web performance
can use `modern-web-guidance`, so the projects can be used together with clear
boundaries.

## Maintenance

Run the dependency-free checks with Python 3.11+:

```bash
python scripts/check_skills.py
python -m unittest discover -s scripts -p 'test_*.py'
```

CI checks frontmatter, local references, companion skill names, plugin manifests,
and README inventories. It does not verify API facts or remote link availability.
For each version-sensitive rule, verify the exact API name, first supported
version, stable/preview status, and separate runtime/platform requirements against
the linked official release/API documentation. Keep rules in references and
discovery/target routing in `SKILL.md`; check that compression preserves safety,
lifecycle, migration and verification requirements.

## Compatibility boundary

Codex, Cursor, and Claude Code discover the package through host-specific plugin
manifests. When this repository is opened directly, Kiro, GitHub Copilot, Cline,
OpenCode, Devin, JetBrains Junie, and OpenHands use `AGENTS.md`; Gemini CLI uses
`GEMINI.md`. The `npx skills` commands install only the canonical `skills/`
directory into the selected host paths; they do not copy these root instruction
files. Every entry point routes to the same skill rules.
