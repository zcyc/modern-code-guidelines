# Language guidelines release audit

Audit date: 2026-08-29. Scope: the 15 language skills in this repository. “Current” means the latest stable language/toolchain release visible in an official source on the audit date; preview, nightly, and development snapshots are called out separately. SQL is treated as a family of standards and database dialects, not as one runtime version.

Sources are limited to language-owner release pages, standards bodies, official specifications, and first-party tool documentation. The “likely missing” items are audit findings only; this note does not change any skill or manifest.

The repository-coverage column records the state at the start of the audit; the
findings below have since been applied to the corresponding skill references and
README files.

## Executive findings

- The largest version gaps are Kotlin (skill stops at 1.9; stable language release is 2.4.0), TypeScript (skill has a 6.x section; the official TypeScript team has released 7.0), Java (skill stops at 25; Java SE 26 is current), Rust (skill has no post-2024-edition section despite Rust 1.98), Swift (skill stops at Swift 6 language-mode guidance while the stable toolchain line is 6.3), PHP (skill stops at 8.2 while 8.5 is current), and Ruby (skill stops at 3.2 while 4.0 is current). [Kotlin releases](https://kotlinlang.org/docs/releases.html), [TypeScript 7 announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/), [Java SE](https://www.oracle.com/java/technologies/java-se-glance.html), [Rust releases](https://blog.rust-lang.org/releases/), [Swift 6.3](https://www.swift.org/blog/swift-6.3-released/), [PHP 8.5](https://www.php.net/releases/8.5/en.php), [Ruby downloads](https://www.ruby-lang.org/en/downloads/)
- Go is already at Go 1.27 in the repository and its 1.27 section covers the most important language/tooling additions; the residual high-value omission is the generally available `runtime/pprof` `goroutineleak` profile and its testing/debugging use case. [Go release history](https://go.dev/doc/devel/release), [Go 1.27 release notes](https://go.dev/doc/go1.27)
- C++ and C are standards rather than annual compiler releases: the current published standards are C++23 / ISO/IEC 14882:2024 and C23 / ISO/IEC 9899:2024; C++26 and C2y are still work in progress in the cited standards-body material. [C++ standard status](https://isocpp.org/std/the-standard), [ISO C++ standard](https://www.iso.org/standard/83626.html), [WG14 project status](https://open-std.org/jtc1/sc22/wg14/www/projects.html)
- ECMAScript 2026 is published, while Node.js 26 is Current and Node.js 24 is LTS. The JavaScript skill still names only ECMAScript 2025 and should add an explicit 2026/host-runtime boundary; the official ECMAScript page does not provide a concise feature delta suitable for safely inventing a new rule list. [ECMAScript 2026](https://ecma-international.org/publications-and-standards/standards/ecma-262/), [Node.js releases](https://nodejs.org/en/about/previous-releases)

## Version and gap matrix

| Language | Stable status on 2026-08-29 | Current repository coverage | Highest-confidence likely gap |
|---|---|---|---|
| Go | 1.27.0, released 2026-08-19 | Go 1.27 section present | Add `goroutineleak` guidance; otherwise 1.27 coverage is strong. [Release history](https://go.dev/doc/devel/release) |
| Rust | 1.98.0, released 2026-08-20; edition 2024 is stable | Editions 2018/2021/2024 only | Add Rust 2024 migration/safety rules and post-1.85 MSRV/tooling examples. [Release](https://blog.rust-lang.org/releases/latest/), [Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/index.html) |
| C++ | C++23, formally ISO/IEC 14882:2024; C++26 is in DIS/work-in-progress status | Through C++23 | Do not treat C++26 draft features as stable; add concrete C++23 library guidance only if needed. [C++ status](https://isocpp.org/std/the-standard), [WG21 2026 papers](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/) |
| Swift | 6.3.3 patch line; 6.4 is a development snapshot line | Swift 5.9 and Swift 6 mode | Add Swift 6.2/6.3 features and explicitly exclude 6.4 snapshots from stable guidance. [Swift 6.3](https://www.swift.org/blog/swift-6.3-released/), [6.3.3 announcement](https://forums.swift.org/t/announcing-swift-6-3-3/87888), [Install snapshots](https://www.swift.org/install/linux/) |
| Kotlin | 2.4.10 latest tooling patch; 2.4.0 latest language release | Through Kotlin 1.9 | Add Kotlin 2.0 K2, 2.3/2.4 stable language features, and platform-target rules. [Kotlin releases](https://kotlinlang.org/docs/releases.html), [Kotlin 2.4](https://kotlinlang.org/docs/whatsnew24.html) |
| Dart | 3.13 stable, released 2026-08-12 | Through Dart 3 | Add Dart 3.10 dot shorthands, 3.12 private named parameters, and 3.13 primary constructors/type-promotion changes. [Language evolution](https://dart.dev/resources/language/evolution), [Dart 3.13](https://dart.dev/blog/announcing-dart-3-13) |
| PHP | 8.5.10 latest stable patch; 8.6 is beta | Through PHP 8.2 | Add 8.3 typed constants/`#[\Override]`, 8.4 property hooks/asymmetric visibility, and 8.5 URI/pipe/clone-with/`#[\NoDiscard]`. [PHP releases](https://www.php.net/), [8.5 announcement](https://www.php.net/releases/8.5/en.php) |
| Ruby | 4.0.6 current stable | Through Ruby 3.2 | Add Ruby 3.4 `it`/Prism and Ruby 4.0 `Set`/Ractor/ZJIT boundaries. [Ruby downloads](https://www.ruby-lang.org/en/downloads/), [Ruby 4.0](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/) |
| C | C23, ISO/IEC 9899:2024 | C23 basics present | Add C23 `constexpr` object, `typeof`, and feature-test/implementation-availability guidance; replace non-primary authority links where practical. [ISO C](https://www.iso.org/standard/82075.html), [WG14](https://open-std.org/jtc1/sc22/wg14/) |
| SQL | ISO/IEC 9075-1:2023 framework; dialects vary | Portable SQL only | Keep dialect resolution, but add explicit PostgreSQL 18/MySQL LTS-vs-Innovation notes if dialect-specific modernization is intended. [ISO SQL](https://www.iso.org/standard/76583.html), [PostgreSQL 18](https://www.postgresql.org/about/news/postgresql-18-released-3142/), [MySQL release model](https://dev.mysql.com/doc/refman/8.4/en/mysql-releases.html) |
| Python | 3.14.7 latest stable patch | Through Python 3.14 | Add 3.14 deferred annotations, t-strings, `compression.zstd`, and `finally` control-flow restriction. [Python 3.14.7](https://www.python.org/downloads/release/python-3147/), [What’s New](https://docs.python.org/3.14/whatsnew/3.14.html) |
| C# | C# 14 on .NET 10; C# 15 remains preview | Through C# 14 plus preview marker | C# 14 list omits implicit span conversions, unbound-generic `nameof`, lambda modifiers, and user-defined compound assignment. [C# 14](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14), [.NET 10](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) |
| Java | Java SE 26.0.2.1; Java 26 language feature is preview-only primitive patterns | Through Java 25 | Add Java 26 preview gating, final-field mutation warnings, Applet removal, and HTTP/3 API notes. [Java SE](https://www.oracle.com/java/technologies/java-se-glance.html), [Java 26 language changes](https://docs.oracle.com/en/java/javase/26/language/java-language-changes-summary.html), [JDK 26 migration](https://docs.oracle.com/en/java/javase/26/migrate/jdk-migration-guide.pdf) |
| JavaScript | ECMAScript 2026; Node.js 26.8.1 Current / 24.20.0 LTS | Through ECMAScript 2025 | Add an ECMAScript 2026 heading and retain explicit Node/browser host targeting; do not infer unlisted 2026 features. [ECMAScript 2026](https://tc39.es/ecma262/2026/multipage/), [Node.js 26.8.1](https://nodejs.org/en/blog/release/v26.8.1) |
| TypeScript | 7.0.2 package line; TypeScript 7 announced 2026-07-08 | Through TypeScript 6 | Add TypeScript 7’s hard-error/deprecation behavior, new defaults, no compiler API, and embedded-language compatibility caveat. [TypeScript 7](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/), [official package](https://www.npmjs.com/package/typescript) |

## Detailed audit

### Go

Go 1.27.0 was released on 2026-08-19. The current Go skill already covers generic methods, generalized generic inference, promoted struct-literal selectors, `stdversion`, the new `go fix` modernizers, `go mod tidy` grouping, and several new packages/APIs. [Go release history](https://go.dev/doc/devel/release), [Go 1.27 release notes](https://go.dev/doc/go1.27)

Likely remaining additions:

- Mention the generally available `goroutineleak` profile for diagnosing permanently blocked goroutines. [Go 1.27 blog](https://go.dev/blog/go1.27)
- Mention `go doc package@version` and response-file parsing only as toolchain capabilities, not style rules. [Go 1.27 release notes](https://go.dev/doc/go1.27)

`testing/synctest` is not missing: it is a Go 1.25 addition already represented in the current Go reference. [Go 1.25 release notes](https://go.dev/doc/go1.25)

### Rust

Rust 1.98.0 is the latest stable release visible in the official release list on the audit date. Rust 2024 is the latest stable edition and was released with Rust 1.85.0. [Rust releases](https://blog.rust-lang.org/releases/), [Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/index.html)

The skill’s Rust 2024 section is too thin. High-confidence missing rules are explicit `unsafe` blocks inside `unsafe fn`, `unsafe extern` blocks and per-item safety marking, and the reserved `gen` keyword/raw-identifier migration. [`unsafe_op_in_unsafe_fn`](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-op-in-unsafe-fn.html), [unsafe extern blocks](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-extern.html), [`gen` keyword](https://doc.rust-lang.org/edition-guide/rust-2024/gen-keyword.html)

Rust 1.98 also stabilizes algebraic floating-point methods whose optimizer freedom can change numerical results, plus buffered integer formatting APIs. These should be treated as explicit performance/precision trade-offs rather than blanket modernization rules. [Rust 1.98 release](https://blog.rust-lang.org/releases/latest/)

### C++

The current published ISO standard is C++23, formally ISO/IEC 14882:2024. C++26 material is still a draft/DIS work stream in the standards-body sources, so a C++26 section must be marked non-stable and compiler/library support must remain independently checked. [The Standard](https://isocpp.org/std/the-standard), [ISO/IEC 14882:2024](https://www.iso.org/standard/83626.html), [WG21 2026 papers](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/)

The current C++ skill has the correct C++23 boundary but mostly gives pre-C++23 design rules. The likely gap is a short, concrete C++23 library checklist only if the project wants API modernization; do not add draft C++26 features based on compiler extensions. [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html), [C++ standard status](https://isocpp.org/std/status)

### Swift

Swift 6.3 was released on 2026-03-24 and the official Swift forums announced Swift 6.3.3 on 2026-06-30. Swift.org labels the 6.4 line as development snapshots, not official releases, so 6.4 must not be treated as stable as of the audit date. [Swift 6.3](https://www.swift.org/blog/swift-6.3-released/), [Swift 6.3.3](https://forums.swift.org/t/announcing-swift-6-3-3/87888), [Swift snapshot policy](https://www.swift.org/install/linux/)

Likely missing rules are Swift 6.2 opt-in strict memory safety, `InlineArray`/`Span` when the target provides them, and Swift 6.3’s `@c` C interoperability, module selectors, and optimization-control attributes. These should remain target/toolchain gated. [Swift 6.2](https://www.swift.org/blog/swift-6.2-released/), [Swift 6.3](https://www.swift.org/blog/swift-6.3-released/)

### Kotlin

Kotlin 2.4.0 is the latest language release and 2.4.10 is its latest tooling patch in the official release table. Kotlin 2.0 made the K2 compiler stable and default; Kotlin 2.4 stabilized context parameters except context arguments/callable references, explicit backing fields, annotation-target improvements, common UUID support, and sorted-order checks. [Kotlin release process](https://kotlinlang.org/docs/releases.html), [Kotlin 2.0](https://kotlinlang.org/docs/whatsnew20.html), [Kotlin 2.4](https://kotlinlang.org/docs/whatsnew24.html)

The current skill is missing a 2.x section. Add rules for K2 as the compiler baseline, `enumEntries()`/stable `AutoCloseable`, Kotlin 2.3 nested type aliases and data-flow `when` exhaustiveness, Kotlin 2.4 stable context parameters/backing fields/UUID, and Java/JVM target alignment. Keep collection literals, explicit context arguments, and name-based destructuring marked experimental where the official notes do so. [Kotlin 2.0](https://kotlinlang.org/docs/whatsnew20.html), [Kotlin 2.3](https://kotlinlang.org/docs/whatsnew23.html), [Kotlin 2.3.20](https://kotlinlang.org/docs/whatsnew2320.html), [Kotlin 2.4](https://kotlinlang.org/docs/whatsnew24.html)

### Dart

Dart 3.13 is the current stable language release and was released on 2026-08-12. Dart language-version constraints gate features, and Dart 3.13 makes primary constructors stable; Dart 3.12 added private named parameters; Dart 3.10 added dot shorthands. [Dart language evolution](https://dart.dev/resources/language/evolution), [Dart 3.13 announcement](https://dart.dev/blog/announcing-dart-3-13), [Dart changelog](https://dart.dev/changelog)

The current Dart skill covers Dart 3 records, patterns, and class modifiers but omits those newer language-versioned rules. It should also call out the Dart 3.13 type-promotion behavior change and the analyzer’s related diagnostics as migration-sensitive. [Dart changelog](https://dart.dev/changelog), [Dart type system](https://dart.dev/language/type-system)

### PHP

PHP 8.5.10 is the latest stable patch shown by php.net on the audit date; PHP 8.6 is explicitly a beta and is not production guidance. [PHP homepage](https://www.php.net/)

The current PHP skill stops at 8.2. Likely missing version rules are PHP 8.3 typed class constants, dynamic class-constant fetch, `#[\Override]`, and `json_validate`; PHP 8.4 property hooks, asymmetric visibility, `#[\Deprecated]`, lazy objects, and new array/PDO APIs; and PHP 8.5 URI APIs, the pipe operator, `clone()` with property updates, `#[\NoDiscard]`, `array_first()`/`array_last()`, and the relevant deprecations. [PHP 8.3](https://www.php.net/releases/8.3/en.php), [PHP 8.4](https://www.php.net/releases/8.4/en.php), [PHP 8.5](https://www.php.net/releases/8.5/en.php), [PHP 8.5 migration guide](https://www.php.net/migration85)

### Ruby

Ruby 4.0.6 is the current stable version listed by ruby-lang.org. Ruby 4.0 introduced Ruby Box and ZJIT as experimental features, Ractor improvements, `Set` as a core class, and a changed `*nil` behavior; Ruby 3.4 introduced `it` and made Prism the default parser. [Ruby downloads](https://www.ruby-lang.org/en/downloads/), [Ruby 4.0 release](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/), [Ruby 3.4 release](https://www.ruby-lang.org/en/news/2024/12/25/ruby-3-4-0-released/)

The current Ruby skill stops at 3.2. Add 3.4/4.0 rules, but keep Ruby Box and ZJIT explicitly experimental and avoid recommending them as ordinary style changes. [Ruby 4.0 release](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/)

### C

C23 is the current C standard, published as ISO/IEC 9899:2024. WG14 lists C2y as unavailable rather than published, so C2y material must not be treated as a stable language target. [ISO/IEC 9899:2024](https://www.iso.org/standard/82075.html), [WG14 project status](https://open-std.org/jtc1/sc22/wg14/www/projects.html)

The current C23 section already has `nullptr`, attributes, `static_assert`, and `typeof_unqual`, but likely omits C23 `constexpr` objects and the broader `typeof`/type-inference family. It also relies on cppreference and SEI CERT links in its authority list, which are useful references but not the primary standards sources requested for this audit. [WG14 `constexpr` paper](https://open-std.org/jtc1/sc22/wg14/www/docs/n3315.htm), [WG14 `nullptr` paper](https://open-std.org/jtc1/sc22/wg14/www/docs/n2978.htm), [WG14 home](https://open-std.org/jtc1/sc22/wg14/)

### SQL

ISO/IEC 9075-1:2023 is the published framework part of the SQL standard, but SQL code is still governed by the selected engine and dialect. PostgreSQL 18 is the current major version and PostgreSQL 18.6 was released on 2026-08-13; MySQL documents separate LTS and Innovation tracks, with MySQL 8.4.12 listed in its official 8.4 release notes. [ISO SQL](https://www.iso.org/standard/76583.html), [PostgreSQL FAQ](https://www.postgresql.org/about/press/faq/), [PostgreSQL 18 release](https://www.postgresql.org/about/news/postgresql-18-released-3142/), [MySQL 8.4 release notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/), [MySQL release model](https://dev.mysql.com/doc/refman/8.4/en/mysql-releases.html)

The current SQL skill’s portable-first/dialect-resolution model is correct. The likely gap is explicit dialect sections: PostgreSQL 18 virtual generated columns and `uuidv7()`, plus MySQL’s LTS-versus-Innovation compatibility and upgrade rules, should be added only if this repository intends to guide those dialects rather than remain portable SQL guidance. [PostgreSQL 18 release notes](https://www.postgresql.org/docs/release/18.0/), [MySQL release model](https://dev.mysql.com/doc/refman/8.4/en/mysql-releases.html)

### Python

Python 3.14.7 is the latest stable patch release on the audit date. Python 3.15 is still a preview line in the cited official release material. [Python 3.14.7](https://www.python.org/downloads/release/python-3147/), [Python 3.15 beta](https://www.python.org/downloads/release/python-3150b1/)

The current Python skill already covers subinterpreters, `InterpreterPoolExecutor`, annotation introspection, free-threading, and the Unix `forkserver` change. Likely omissions are deferred annotation evaluation, template string literals, `compression.zstd`, omitted parentheses in `except`/`except*`, and the prohibition on `return`/`break`/`continue` exiting `finally`. [Python 3.14 release](https://www.python.org/downloads/release/python-3147/), [What’s New in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html)

### C#

C# 14 is the latest C# release and is supported on .NET 10. C# 15 is still a preview in the current Microsoft versioning material. [C# 14](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14), [C# language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning)

The current C# skill has the major C# 14 features but omits implicit `Span<T>`/`ReadOnlySpan<T>` conversions, unbound generic types in `nameof`, simple lambda parameters with modifiers, and user-defined compound assignment. These are worth adding as version-gated examples, while keeping the .NET API/runtime split. [C# 14](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14)

### Java

Java SE 26.0.2.1 is the latest Java SE platform release shown by Oracle. Java 26 has no new permanent language feature in Oracle’s language summary; primitive types in patterns/`instanceof`/`switch` remain preview. [Java SE](https://www.oracle.com/java/technologies/javase/java-se-glance.html), [Java 26 language summary](https://docs.oracle.com/en/java/javase/26/language/java-language-changes-summary.html)

The current Java skill stops at 25. Add Java 26 as a release/API target with a preview-only primitive-pattern rule, warnings around deep reflection mutating final fields, Applet API removal, and the HTTP/3-capable HTTP Client API. [Java 26 release notes](https://www.oracle.com/java/technologies/javase/26-relnote-issues.html), [JDK 26 migration guide](https://docs.oracle.com/en/java/javase/26/migrate/jdk-migration-guide.pdf)

### JavaScript

ECMAScript 2026 is the 17th edition and defines the current ECMAScript language specification. Node.js 26.8.1 is Current, while Node.js 24.20.0 is the latest LTS line listed by Node’s release page on the audit date. [ECMAScript 2026](https://ecma-international.org/publications-and-standards/standards/ecma-262/), [Node.js releases](https://nodejs.org/en/about/previous-releases), [Node.js 26.8.1](https://nodejs.org/en/blog/release/v26.8.1)

The current JavaScript skill should at least add an ECMAScript 2026 section and update its Node host boundary. I did not promote Stage 3 proposals or infer a feature list from incomplete official summaries; the current official ECMAScript page documents the standard but does not give a concise 2026 delta suitable for a high-confidence style rule. [ECMAScript 2026 specification](https://tc39.es/ecma262/2026/multipage/), [TC39 proposal stages](https://github.com/tc39/proposals)

### TypeScript

The official TypeScript team announced TypeScript 7.0 on 2026-07-08, and the official `typescript` package registry shows 7.0.2 as the current package version. The TypeScript 6.0 release notes remain important as the migration bridge, but TypeScript 7 is the current stable line. [TypeScript 7 announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/), [TypeScript package](https://www.npmjs.com/package/typescript), [TypeScript 6.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)

The current skill’s TypeScript 6 section is stale. The likely missing TypeScript 7 rules are that deprecated 6.0 options become hard errors, `strict`/`module`/`types`/`rootDir` and related defaults change, `stableTypeOrdering` is enabled by default, and TypeScript 7 does not ship the TypeScript 6 compiler API. The official blog also warns that tools embedding TypeScript through the programmatic API may need to remain on 6.0 temporarily. [TypeScript 7 announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

## Earlier useful findings retained

The previous version of this note identified two Java wording corrections. String Templates were withdrawn in Java 23, not Java 22; and `import module` is permitted in any source file, not only in an explicit module. [Java language changes](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-summary.html), [Java language changes by release](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-release.html), [JEP 511](https://openjdk.org/jeps/511)

The previous Python audit also correctly separated the `concurrent.interpreters` module from `InterpreterPoolExecutor`, which is a class in `concurrent.futures`; that namespace distinction remains useful in the version-gated guidance. [Python 3.14 What’s New](https://docs.python.org/3.14/whatsnew/3.14.html), [concurrent.interpreters](https://docs.python.org/3/library/concurrent.interpreters.html), [concurrent.futures](https://docs.python.org/3.14/library/concurrent.futures.html)

The previous C# audit noted that C# 15 is preview-only in the current Microsoft versioning material and is associated with .NET 11 or later. This remains a preview/toolchain-boundary concern, not stable C# guidance. [C# 15](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15), [C# language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning), [C# version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history)

## Scala audit

Audit date: 2026-08-29. This section records the research used by the Scala
skill; implementation lives in `skills/use-modern-scala/`. Sources are limited
to Scala’s official sites, official Scala/sbt/Scala CLI documentation, the Scala
3 reference, and official GitHub repositories and release notes.

### Version status

- **Scala 3.8.4** is the latest stable Scala release visible on the official download page. **Scala 3.3.8** is the current LTS line and is the recommended line for publishing libraries that need a longer support window. **Scala 2.13.18** is the current Scala 2.13 maintenance release; Scala 2.13.18 is binary-compatible with the 2.13 series and supports JDK 8–26. [Scala downloads](https://www.scala-lang.org/download/), [Scala 3.8.4](https://www.scala-lang.org/news/3.8.4/), [Scala 3.3.8 LTS](https://www.scala-lang.org/news/3.3.8/), [Scala 2.13.18](https://github.com/scala/scala/releases/tag/v2.13.18)
- **Scala 3.9.0 is not stable as of the audit date.** The official compiler repository lists `3.9.0-RC6` as a pre-release; do not treat the generated 3.9 reference or RC behavior as stable production guidance. The 3.9 line is intended to become the next LTS line, but it remains preview/development until a non-RC release is published. [Scala 3 releases](https://github.com/scala/scala3/releases), [Scala 3 reference](https://docs.scala-lang.org/scala3/reference/)
- Do not conflate Scala language releases with platform releases: Scala.js **1.22.0**, Scala Native **0.5.12**, sbt **2.0.8**, and Scala CLI **1.16.0** are independently versioned toolchains. [Scala.js 1.22.0](https://github.com/scala-js/scala-js/releases/tag/v1.22.0), [Scala Native 0.5.12](https://github.com/scala-native/scala-native/releases/tag/v0.5.12), [sbt releases](https://github.com/sbt/sbt/releases), [Scala CLI 1.16.0](https://github.com/VirtusLab/scala-cli/releases/tag/v1.16.0)

### Scala 3.7 rules

- Named tuples and `@publicInBinary` are stable in 3.7. Use named tuples where the names materially improve a tuple-shaped API, and use `@publicInBinary` only when maintaining an intentional binary API; it is not a general annotation for ordinary application code. [Scala 3.7 release](https://www.scala-lang.org/news/3.7.0/)
- Scala 3.7 introduced the `-preview` gate for SIP-approved features that may still change incompatibly. Preview features are acceptable for applications or internal tools that accept that risk, but are discouraged in published libraries. `-preview` must not be treated as an ordinary modernization flag. [Scala 3.7 release](https://www.scala-lang.org/news/3.7.0/), [Preview definitions](https://docs.scala-lang.org/scala3/reference/other-new-features/preview-defs.html)
- Better Fors were previewed in 3.7 and became stable in 3.8. Before upgrading a 3.7 codebase, compile with the latest 3.7 patch and use the documented migration source/rewrite mode when the project accepts compiler rewrites; specifically check `for` comprehensions with consecutive aliases and overloaded `map` implementations because their runtime result type can change. [Scala 3.8 release](https://www.scala-lang.org/news/3.8/), [Scala 3.7.4](https://www.scala-lang.org/news/3.7.4/)
- The new given-prioritization behavior is the default in 3.7. Do not rely on the old “most specific subtype always wins” behavior; make competing givens unambiguous and use the migration source mode to expose changed resolutions. [Scala 3.7 release](https://www.scala-lang.org/news/3.7.0/)

### Scala 3.8 rules

- Scala 3.8 requires **JDK 17 or later** for compilation and execution. Scala 3.3 LTS remains the line for producing JDK 8-compatible bytecode; use the official JDK/Scala compatibility matrix instead of inferring compatibility from the language version alone. [Scala 3.8 release](https://www.scala-lang.org/news/3.8/), [JDK compatibility](https://docs.scala-lang.org/overviews/jdk-compatibility/overview.html)
- Better Fors and `runtimeChecked` are stable in 3.8. Use `runtimeChecked` when a deliberately partial operation is part of the contract; do not use it to hide a match-exhaustivity or unsafe-access warning accidentally. [Better Fors](https://docs.scala-lang.org/scala3/reference/other-new-features/better-fors.html), [runtimeChecked](https://docs.scala-lang.org/scala3/reference/other-new-features/runtimeChecked.html)
- The Scala 3 standard library is compiled with Scala 3 starting in 3.8. Explicitly supplying a context-bound argument may therefore require `using`; prefer the inferred/contextual form where possible, and run the 3.7.4 migration rewrite before upgrading. Do not manually mix compiler, library, and reflect artifacts from different Scala lines. [Scala 3.8 release](https://www.scala-lang.org/news/3.8/), [Scala 3.8/TASTy compatibility](https://www.scala-lang.org/blog/state-of-tasty-reader.html)
- The REPL became a separate artifact in 3.8, and deprecated legacy runner/REPL entry points from 3.7 were removed. Build and tooling rules must select the 3.8 REPL artifact explicitly when embedding the REPL; do not assume it is included in the compiler distribution. [Scala 3.8 release](https://www.scala-lang.org/news/3.8/), [Scala 3.7.4](https://www.scala-lang.org/news/3.7.4/)
- `into` is preview in 3.8 and requires the preview gate/language opt-in. Flexible varargs and strict-equality pattern matching are experimental. Keep all three out of ordinary library guidance until the relevant stable release is actually published; the 3.9 RC’s planned stabilization does not retroactively make them 3.8-stable. [Scala 3.8 release](https://www.scala-lang.org/news/3.8/), [Scala 3 preview/experimental reference](https://docs.scala-lang.org/scala3/reference/experimental/)
- Avoid Scala 3.8.0 specifically; the official release notes document regressions in 3.8.0/3.8.1 and recommend waiting for a later hotfix. The current stable 3.8 line is 3.8.4. [Scala 3.8 release](https://www.scala-lang.org/news/3.8/), [Scala 3.8.4](https://www.scala-lang.org/news/3.8.4/)

### Scala 2.13 and Scala 3 compatibility boundary

- The supported direction remains **Scala 3 consuming Scala 2.13 artifacts**. The reverse direction is limited: Scala 2.13’s `-Ytasty-reader` can consume Scala 3 artifacts through Scala 3.7, but it will not consume Scala 3.8 or later artifacts. Scala 3.7 is the last Scala 3 minor version in that migration path. [TASTy compatibility status](https://www.scala-lang.org/blog/state-of-tasty-reader.html)
- Treat `-Ytasty-reader` as a migration bridge, not a permanent compatibility layer. If a library must serve both ecosystems, cross-publish native Scala 2.13 and Scala 3 artifacts; when a one-way Scala 3 artifact is unavoidable, Scala 3.3 LTS is the safest published baseline for Scala 2.13 consumers. [TASTy compatibility status](https://www.scala-lang.org/blog/state-of-tasty-reader.html)
- Scala 2.13.18 is a maintenance line, not a Scala 3 language-feature line. Keep compiler/library/reflect versions aligned within the selected Scala 2.13 line, and do not let dependency eviction substitute a Scala 3 `scala-library` for the Scala 2.13 compiler’s matching artifacts. [Scala 2.13.18](https://github.com/scala/scala/releases/tag/v2.13.18), [TASTy compatibility status](https://www.scala-lang.org/blog/state-of-tasty-reader.html)

### Tool and target resolution

#### sbt

- `project/build.properties` selects the sbt version; `scalaVersion` selects the project’s Scala compiler and standard library. If `scalaVersion` is omitted, sbt falls back to the Scala version sbt itself was built against, so production builds should set it explicitly. [sbt configure Scala](https://www.scala-sbt.org/1.x/docs/Howto-Scala.html), [sbt 2 changes](https://www.scala-sbt.org/2.x/docs/en/changes/sbt-2.0-change-summary.html)
- sbt 2.x uses Scala 3.8.4 for build definitions/plugins and requires JDK 17+, but it can build projects using Scala 2.x or Scala 3.x. Do not confuse the Scala version of the build definition with the Scala version of the application/library being built. [sbt 2 announcement](https://github.com/scala/scala-lang/blob/main/blog/_posts/2026-06-29-sbt2.md)
- `crossScalaVersions` is the explicit set of project language versions used by `+` cross-build actions. `projectMatrix` in sbt 2.x turns Scala-version/platform rows into separate subprojects; declare JVM, JS, and Native rows explicitly instead of assuming one row’s target applies to all platforms. [sbt cross-building](https://www.scala-sbt.org/1.x/docs/Cross-Build.html), [sbt 2 project matrix](https://www.scala-sbt.org/2.x/docs/en/changes/sbt-2.0-change-summary.html)
- `%%` resolves a dependency using sbt’s `scalaBinaryVersion` convention (`_2.13` for Scala 2.13 and `_3` for Scala 3). This artifact suffix is not a promise that Scala 2.13 can read every Scala 3 TASTy version; keep the TASTy boundary above separate from artifact naming. [sbt cross-building](https://www.scala-sbt.org/1.x/docs/Cross-Build.html), [sbt CrossVersion API](https://www.scala-sbt.org/1.x/api/sbt/librarymanagement/CrossVersion%24.html)

#### Scala CLI

- Scala CLI uses the latest stable Scala version tested by that Scala CLI release when no version is specified. `--scala`/`-S` and `using scala` accept exact or short versions; a short version resolves to the highest corresponding stable version. Command-line options override `using` directives, so CI should pin an exact version rather than relying on the default or a prefix. [Scala CLI supported versions](https://scala-cli.virtuslab.org/docs/reference/scala-versions/), [Scala version selection](https://scala-cli.virtuslab.org/docs/cookbooks/introduction/scala-versions/)
- The current Scala CLI line is 1.16.0; the official supported-version table resolves the current line to Scala 3.8.4, Scala 2.13.18, and Scala 2.12.21. Scala CLI 1.15 explicitly paired its default Scala 3.8.4 with Scala.js 1.22.0 and Scala Native 0.5.12; verify the installed CLI’s `version` output rather than assuming those defaults for an older CLI. [Scala CLI 1.16.0](https://github.com/VirtusLab/scala-cli/releases/tag/v1.16.0), [supported Scala versions](https://scala-cli.virtuslab.org/docs/reference/scala-versions/), [Scala CLI 1.15 defaults](https://github.com/VirtusLab/scala-cli/releases/tag/v1.15.0)
- `using target.platform`, `using target.scala`, and version-bound target directives are file-level requirements and are documented as experimental. Use them to constrain source applicability, not as a replacement for the project’s pinned compiler/platform configuration. `using jsVersion` and `using nativeVersion` resolve platform versions independently from `using scala`. [Scala CLI directives](https://scala-cli.virtuslab.org/docs/reference/directives/)
- Scala CLI’s current Wasm switch remains experimental at the CLI layer even though Scala.js 1.22.0 made its Wasm backend stable. This distinction matters: the Scala.js backend requires an ES2022+ JavaScript host, Wasm 3.0, and ES modules; JSPI remains an explicit opt-in. [Scala CLI 1.15 release](https://github.com/VirtusLab/scala-cli/releases/tag/v1.15.0), [Scala.js 1.22.0](https://github.com/scala-js/scala-js/releases/tag/v1.22.0)

#### Scala Native

- Scala Native 0.5.12 is the latest stable release. Its release matrix explicitly lists Scala 2.12.17–2.12.21, Scala 2.13.9–2.13.18, and Scala 3 through 3.8.3. The project states that version-dependent artifacts for newly released Scala versions may be published without a new Native release; therefore do not infer 3.8.4 or 3.9 RC support from the Native release number—resolve the exact artifact and test it. [Scala Native 0.5.12](https://github.com/scala-native/scala-native/releases/tag/v0.5.12)
- Scala Native’s JDK 17+ and LLVM/Clang 16+ versions are the tested toolchain baseline in 0.5.12; older versions remain accepted but deprecated. Virtual threads are explicitly experimental and not production-ready. [Scala Native 0.5.12](https://github.com/scala-native/scala-native/releases/tag/v0.5.12)
- Native target selection is separate from Scala language selection: the Scala version selects the compiler/library artifacts, while the Native plugin/version and native linker options select the native backend/target. Keep those versions explicit in sbt/Scala CLI and do not silently use a nightly snapshot for a production target. [Scala Native releases](https://github.com/scala-native/scala-native/releases), [Scala CLI directives](https://scala-cli.virtuslab.org/docs/reference/directives/)

#### Scala.js

- Scala.js 1.22.0 is the latest stable backend release. It supports sbt 2.x and makes the WebAssembly backend stable, but 1.22.0 is not forward binary-compatible with artifacts produced by 1.21.x or earlier; upgrade and relink the complete backend/toolchain together. [Scala.js 1.22.0](https://github.com/scala-js/scala-js/releases/tag/v1.22.0)
- The language version and Scala.js backend version are independent selectors: `scalaVersion`/`using scala` chooses Scala, while the sbt Scala.js plugin or Scala CLI `jsVersion` chooses Scala.js. For multi-platform projects, use explicit JVM/JS rows and platform-specific dependencies rather than assuming JVM APIs exist on JS. [sbt 2 project matrix](https://github.com/scala/scala-lang/blob/main/blog/_posts/2026-06-29-sbt2.md), [Scala CLI directives](https://scala-cli.virtuslab.org/docs/reference/directives/)
- Scala.js Wasm output requires a JavaScript host, ES2022+, Wasm 3.0, and ES modules. `js.async`/`js.await` with Wasm additionally requires JSPI support and an explicit opt-in; these runtime constraints belong in the target matrix, not only in source-level rules. [Scala.js 1.22.0](https://github.com/scala-js/scala-js/releases/tag/v1.22.0)

### Implementation checklist

- Establish a modern Scala 3 baseline: `given`/`using`, extension methods, enums/ADTs, opaque types, top-level definitions, export clauses, union/intersection types, match types, and Scala 3 Quotes macros; require an intentional language version when using preview/experimental features. [Scala 3 reference](https://docs.scala-lang.org/scala3/reference/), [Scala 3 syntax summary](https://docs.scala-lang.org/scala3/reference/syntax.html)
- Make compiler target, JDK target, Scala library/compiler/reflect versions, sbt version, Scala CLI version, and JS/Native backend versions explicit. Do not rely on “latest” resolution in reproducible CI, and do not infer source/TASTy compatibility from `_2.13`/`_3` artifact suffixes. [sbt configure Scala](https://www.scala-sbt.org/1.x/docs/Howto-Scala.html), [Scala CLI version selection](https://scala-cli.virtuslab.org/docs/cookbooks/introduction/scala-versions/), [TASTy compatibility status](https://www.scala-lang.org/blog/state-of-tasty-reader.html)
- Separate stable, preview, experimental, RC, nightly, and deprecated rules. In particular: Scala 3.8 stable features are safe to document; `into`/flexible varargs/strict-equality pattern matching need opt-in; Scala 3.9 RC6 is not stable; Scala Native virtual threads and Scala CLI Wasm are experimental. [Scala 3.8 release](https://www.scala-lang.org/news/3.8/), [Scala 3 releases](https://github.com/scala/scala3/releases), [Scala Native 0.5.12](https://github.com/scala-native/scala-native/releases/tag/v0.5.12), [Scala CLI 1.15](https://github.com/VirtusLab/scala-cli/releases/tag/v1.15.0)

### Source caveat

The official Scala 3 reference currently renders a 3.9.0 label even though the official Scala download page still identifies 3.8.4 as the latest stable release and the compiler repository marks 3.9.0-RC6 as a pre-release. Version-status rules should therefore use the release/download pages and GitHub release classification, not the reference site’s generated version label alone. [Scala downloads](https://www.scala-lang.org/download/), [Scala 3 releases](https://github.com/scala/scala3/releases), [Scala 3 reference](https://docs.scala-lang.org/scala3/reference/)

## Uncertainty and source caveats

- Swift has a clear stable 6.3 patch announcement, but Swift.org’s documentation is already describing 6.4 snapshots; this audit treats 6.4 as preview because the install page explicitly says snapshots are not official releases. [Swift 6.3.3](https://forums.swift.org/t/announcing-swift-6-3-3/87888), [Swift install page](https://www.swift.org/install/linux/)
- TypeScript’s official documentation page still foregrounds TypeScript 6.0 while the official team blog and official package registry show TypeScript 7.0.2. The release status is therefore high confidence, but the repository should use the TypeScript 7 release blog as the behavioral authority until the handbook is updated. [TypeScript 6.0 handbook](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html), [TypeScript 7 announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/), [TypeScript package](https://www.npmjs.com/package/typescript)
- C++26 and C2y are deliberately not converted into stable guidance here: the cited C++ sources describe C++26 as in progress/DIS material and WG14 lists C2y as not available. [C++ standard status](https://isocpp.org/std/the-standard), [WG14 project status](https://open-std.org/jtc1/sc22/wg14/www/projects.html)
- SQL cannot have one “latest language version” without naming an engine and dialect; the audit records the published ISO framework and representative PostgreSQL/MySQL statuses instead. [ISO SQL](https://www.iso.org/standard/76583.html), [PostgreSQL FAQ](https://www.postgresql.org/about/press/faq/), [MySQL release model](https://dev.mysql.com/doc/refman/8.4/en/mysql-releases.html)
