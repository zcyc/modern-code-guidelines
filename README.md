# Modern Code Guidelines

[简体中文](README.zh-CN.md)

A shared skill package for Codex, Cursor, Claude Code, Kiro, Google Antigravity,
Gemini CLI, GitHub Copilot, Cline, OpenCode, Devin, JetBrains Junie, and OpenHands,
containing thirty-five independently triggered language and framework skills:

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

Framework skills:

- `use-modern-react`
- `use-modern-nextjs`
- `use-modern-vue`
- `use-modern-angular`
- `use-modern-spring-boot`
- `use-modern-aspnet-core`
- `use-modern-django`
- `use-modern-fastapi`
- `use-modern-flutter`
- `use-modern-swiftui`
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
Version-specific references stay beside each skill.

The JavaScript skill covers core ECMAScript and Node.js. TypeScript has its own skill
for compiler/type-system behavior. Browser APIs, CSS, accessibility, and web
performance remain the responsibility of `modern-web-guidance`.

## Rule sources

Each skill resolves the project's declared target first, then reads its local rules.
The references prioritize official language
specifications, release notes, compiler documentation, and runtime/standard-library
API documentation:

| Language | Version and language source | Runtime/API source |
| --- | --- | --- |
| Java | [Oracle Java Language Updates](https://docs.oracle.com/en/java/javase/26/language/java-language-changes-summary.html), [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se26/html/index.html) | [Java SE API](https://docs.oracle.com/en/java/javase/26/docs/api/) |
| JavaScript | [ECMAScript 2026](https://tc39.es/ecma262/2026/multipage/) | [Node.js APIs](https://nodejs.org/dist/latest/docs/api/), [Node.js releases](https://nodejs.org/en/about/previous-releases) |
| TypeScript | [TypeScript release notes](https://www.typescriptlang.org/docs/handbook/release-notes/), [TypeScript 7](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/), [TSConfig reference](https://www.typescriptlang.org/tsconfig/) | The selected JavaScript host and its runtime/API documentation |
| Python | [Python What’s New](https://docs.python.org/3/whatsnew/), [What’s New in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html), [Language Reference](https://docs.python.org/3/reference/) | [Python Standard Library](https://docs.python.org/3/library/) |
| C# | [C# version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history), [C# 15 preview](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15), [language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning) | [C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/), [.NET API browser](https://learn.microsoft.com/en-us/dotnet/api/) |
| Go | [Go specification](https://go.dev/ref/spec), [Effective Go](https://go.dev/doc/effective_go), [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments), [Go 1.27 release notes](https://go.dev/doc/go1.27); supplementary [Modern Go Guidelines](https://github.com/JetBrains/go-modern-guidelines) | [Go standard library](https://pkg.go.dev/std), [Go release history](https://go.dev/doc/devel/release) |
| Rust | [Rust Edition Guide](https://doc.rust-lang.org/edition-guide/), [Rust Style Guide](https://doc.rust-lang.org/style-guide/) | [Rust release notes](https://doc.rust-lang.org/stable/releases.html), [Rust standard library](https://doc.rust-lang.org/std/), [Cargo Book](https://doc.rust-lang.org/cargo/) |
| Scala | [Scala release lines](https://www.scala-lang.org/download/), [Scala 3 Reference](https://docs.scala-lang.org/scala3/reference/) | [Scala/JDK compatibility](https://docs.scala-lang.org/overviews/jdk-compatibility/overview.html), [sbt](https://www.scala-sbt.org/), [Scalafmt](https://scalameta.org/scalafmt/), [Scalafix](https://scalacenter.github.io/scalafix/) |
| C++ | [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html), [ISO/IEC 14882:2024](https://www.iso.org/standard/83626.html), [C++26 working papers](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/) | [cppreference C++ language](https://en.cppreference.com/w/cpp/language), [standard library](https://en.cppreference.com/w/cpp/standard_library) |
| Swift | [Swift 6.3 release](https://www.swift.org/blog/swift-6.3-released/), [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/), [Swift Evolution](https://www.swift.org/swift-evolution/) | [Swift Book](https://docs.swift.org/swift-book/), [Swift concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) |
| Kotlin | [What's new in Kotlin 2.0](https://kotlinlang.org/docs/whatsnew20.html), [What's new in Kotlin 2.4](https://kotlinlang.org/docs/whatsnew24.html), [Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html) | [Kotlin language documentation](https://kotlinlang.org/docs/kotlin-reference.html), [Kotlin coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html) |
| Dart | [Dart 3.13 announcement](https://dart.dev/blog/announcing-dart-3-13), [Effective Dart](https://dart.dev/effective-dart) | [Dart language specification](https://spec.dart.dev/), [Dart linter rules](https://dart.dev/tools/linter-rules) |
| PHP | [PHP 8.5 release](https://www.php.net/releases/8.5/en.php), [PHP language manual](https://www.php.net/manual/en/langref.php) | [PHP standard library](https://www.php.net/manual/en/book.standard.php), [PHP-FIG PSR](https://www.php-fig.org/psr/) |
| Ruby | [Ruby 4.0 release](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/), [Ruby documentation](https://www.ruby-lang.org/en/documentation/), [RuboCop style cops](https://docs.rubocop.org/rubocop/latest/cops_style.html) | [Ruby core API](https://docs.ruby-lang.org/en/) |
| C | [ISO/IEC 9899:2024 (C23)](https://www.iso.org/standard/82075.html), [C language reference](https://en.cppreference.com/w/c/language), [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c) | [C standard library reference](https://en.cppreference.com/w/c/header) |
| SQL | [ISO/IEC 9075:2023](https://www.iso.org/standard/76583.html), [SQLFluff rules](https://docs.sqlfluff.com/en/stable/reference/rules.html) | [PostgreSQL release notes](https://www.postgresql.org/docs/release/), or the selected database vendor's SQL and transaction documentation |

The detailed rules and their source links live in each skill's local
`references/guidelines.md`. Framework references use the framework's official
documentation as the primary source. Secondary guidance can inform examples, but
it does not override the project's declared target or the primary sources above.

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
remain in `modern-web-guidance`, so the projects can be used together with clear
boundaries.

## Compatibility boundary

Codex, Cursor, and Claude Code discover the package through host-specific plugin
manifests. When this repository is opened directly, Kiro, GitHub Copilot, Cline,
OpenCode, Devin, JetBrains Junie, and OpenHands use `AGENTS.md`; Gemini CLI uses
`GEMINI.md`. The `npx skills` commands install only the canonical `skills/`
directory into the selected host paths; they do not copy these root instruction
files. Every entry point routes to the same skill rules.
