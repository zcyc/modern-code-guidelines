# Modern Code Guidelines

[简体中文](README.zh-CN.md)

A shared skill package for Codex, Cursor, and Claude Code, containing five
independently triggered language skills:

- Codex: `.codex-plugin/plugin.json`
- Cursor: `.cursor-plugin/plugin.json`
- Claude Code: `.claude-plugin/plugin.json`

All three hosts use the same `skills/` directory, so language guidance is not
duplicated or allowed to drift between integrations.

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

## Skills

- `use-modern-java`
- `use-modern-javascript`
- `use-modern-typescript`
- `use-modern-python`
- `use-modern-csharp`

Each skill reads the project's explicit language/compiler/runtime target and applies
only stable rules supported by that target. Version-specific references stay beside
their skill so updating one language does not change the others.

The JavaScript skill covers core ECMAScript and Node.js. TypeScript has its own skill
for compiler/type-system behavior. Browser APIs, CSS, accessibility, and web
performance remain the responsibility of `modern-web-guidance`.

## Rule sources

Each skill resolves the project's declared target first, then reads the versioned
reference beside that skill. The references prioritize official language
specifications, release notes, compiler documentation, and runtime/standard-library
API documentation:

| Language | Version and language source | Runtime/API source |
| --- | --- | --- |
| Java | [Oracle Java Language Updates](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-summary.html), [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/index.html) | [Java SE API](https://docs.oracle.com/en/java/javase/25/docs/api/) |
| JavaScript | [ECMAScript 2025](https://262.ecma-international.org/16.0/) | [Node.js APIs](https://nodejs.org/dist/latest/docs/api/), [Node.js releases](https://nodejs.org/en/about/previous-releases) |
| TypeScript | [TypeScript release notes](https://www.typescriptlang.org/docs/handbook/release-notes/), [TypeScript 6.0](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html), [TSConfig reference](https://www.typescriptlang.org/tsconfig/) | The selected JavaScript host and its runtime/API documentation |
| Python | [Python What’s New](https://docs.python.org/3/whatsnew/), [What’s New in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html), [Language Reference](https://docs.python.org/3/reference/) | [Python Standard Library](https://docs.python.org/3/library/) |
| C# | [C# version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history), [C# 15 preview](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15), [language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning) | [C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/), [.NET API browser](https://learn.microsoft.com/en-us/dotnet/api/) |

The detailed rules and their source links live in each skill's
`references/guidelines.md`. Secondary guidance can inform examples, but it does not
override the project's declared target or the primary sources above.

## Relationship to related projects

This project was inspired by [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines)
and [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance). It
complements both projects rather than replacing them:

- [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) focuses on
  modern Go language and standard-library guidance.
- [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) focuses on
  browser and web-platform practices such as Web APIs,
  CSS, accessibility, and web performance.
- `modern-code-guidelines` focuses on Java, JavaScript, TypeScript, Python, and C# language,
  compiler, runtime, and standard-library guidance.

The JavaScript and TypeScript skills intentionally stop at core language, compiler,
Node.js, and runtime concerns. Browser UI, CSS, accessibility, and web performance
remain in `modern-web-guidance`, so the projects can be used together with clear
boundaries.

## Compatibility boundary

Support means that Codex, Cursor, and Claude Code can discover the shared skill
package through their host-specific plugin manifest. This project does not add
host-specific commands, agents, or duplicated rule files.
