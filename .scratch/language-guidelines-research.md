# 语言 skill 一手文档审计

审计范围：

- `use-modern-java`
- `use-modern-javascript`
- `use-modern-typescript`
- `use-modern-python`
- `use-modern-csharp`

方法：

- 只对照官方/一手来源：语言规范、官方语言更新、官方 release notes、官方 API 文档。
- 重点看三件事：版本检测、规则源、以及是否存在过时或无证据的断言。
- 只写这一份研究记录，不修改其他文件。

## 总览

| Skill | 版本检测 | 规则源 | 结论 |
| --- | --- | --- | --- |
| Java | 项目构建目标 + `--release` / `toolchain` / CI | Oracle language updates, JLS, Java SE 25 API docs, Oracle migration guide | 有 2 处明确不一致 |
| JavaScript | `package.json` / `.nvmrc` / `.node-version` / CI + 浏览器 `browserslist` | ECMAScript 2025 spec, Node ESM docs, Node release schedule | 未发现实质问题 |
| TypeScript | `typescript` 版本 + `tsconfig` + 选中的项目配置 | TS release notes / Handbook / TSConfig reference | 未发现实质问题 |
| Python | `requires-python` / packaging metadata / tox-nox-CI | Python What’s New, language reference, stdlib docs | 有 1 处命名边界问题 |
| C# | `.csproj` / `Directory.Build.props` / `global.json` / CI | C# version history, language versioning, language reference, .NET API docs | 有 1 处覆盖滞后 |

## Findings

### Java

Version detection is fine: the skill reads Maven/Gradle/`--release` targets and refuses to infer from the installed JDK. That matches the intended project-local resolution model.

Rule sources are mostly strong and first-party. The main Java rule table is anchored in Oracle docs and the JLS, and the official Java 25 language update page confirms the current 25-level permanent features.

Findings:

- [Medium] `use-modern-java/references/guidelines.md:54-57` says string templates were withdrawn in Java 22. Oracle’s own release table says the opposite ordering: Java 22 still had String Templates as a second preview, and the withdrawal happened in Java 23. The rule should be retargeted to 23+ or softened to “not stable yet”.
  Evidence: [Java Language Changes Summary](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-summary.html), [Java Language Changes by Release](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-release.html).

- [Medium] `use-modern-java/references/guidelines.md:59-61` limits module import declarations to modular code. JEP 511 explicitly says `import module` can be used in any source file, whether or not that file is part of an explicit module. The current wording is narrower than the official spec and reads like an unsupported restriction.
  Evidence: [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511).

Net: the Java skill is close, but these two lines need a wording fix to stay aligned with the official docs.

### JavaScript

Version detection is a sensible host-runtime heuristic: `engines.node`, explicit runtime files, and checked-in CI/runtime declarations are the right project-local places to read the target from.

Rule sources are clean and first-party: ECMA-262 for language features, Node’s ESM docs for module boundary behavior, and Node’s release schedule for runtime support windows.

Findings:

- None. I did not find a rule that clearly conflicts with the official ECMAScript or Node documentation.

Useful source anchors:

- [ECMAScript 2025 specification](https://262.ecma-international.org/16.0/)
- [Node.js ECMAScript modules](https://nodejs.org/dist/latest/docs/api/esm.html)
- [Node.js release schedule](https://nodejs.org/en/about/previous-releases)

### TypeScript

Version detection is aligned with the language’s real control knobs: compiler version plus the concrete `tsconfig` that actually includes the file.

Rule sources are current: the release notes page covers the referenced 5.x and 6.0 behaviors, and the Handbook/TSConfig reference are official first-party docs.

Findings:

- None. The 4.9+ through 6.0+ rules are consistent with current official TypeScript docs.

Useful source anchors:

- [TypeScript release notes](https://www.typescriptlang.org/docs/handbook/release-notes/)
- [TypeScript 5.6 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-6.html)
- [TypeScript 5.9 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-9.html)
- [TypeScript 6.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)

### Python

Version detection is fine: `requires-python`, packaging metadata, and CI matrices are the right project-local target sources.

Rule sources are current. Python 3.14 docs now cover deferred annotation evaluation, `annotationlib`, the new `concurrent.interpreters` module, and `InterpreterPoolExecutor`.

Findings:

- [Low] `use-modern-python/references/guidelines.md:45-49` conflates `concurrent.interpreters` and `InterpreterPoolExecutor` as if they were one combined API. The official docs split them: `concurrent.interpreters` is a module, while `InterpreterPoolExecutor` is a class in `concurrent.futures`, and the 3.14 docs explicitly call out that separation. The current slash notation can send readers to the wrong namespace.
  Evidence: [What’s new in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html), [concurrent.interpreters](https://docs.python.org/3/library/concurrent.interpreters.html), [concurrent.futures](https://docs.python.org/3.14/library/concurrent.futures.html).

Net: the Python skill is current overall, but this one line should be split or renamed to match the actual stdlib layout.

### C#

Version detection is aligned with how Microsoft says C# should be targeted: read `LangVersion`, target framework, `global.json`, and checked-in build/CI settings, and keep language version separate from runtime/API availability.

Rule sources are current for C# 14. The C# 14 page documents extension members, `field`-backed properties, partial events/constructors, and the other feature bullets used in the skill.

Finding:

- [Medium] `use-modern-csharp/references/guidelines.md:44-48` stops at C# 14+, but Microsoft’s current documentation now includes C# 15 as the latest preview release and says C# 15 is supported on .NET 11 and newer. That means the skill is already one version behind the official versioning docs and cannot express current C# 15 guidance.
  Evidence: [What’s new in C# 15](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15), [C# language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning), [C# version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history).

Net: the C# guidance is accurate through 14, but it lags current official docs once 15 preview support is in scope.

## Source set used

- Java: [Oracle Java language updates](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-summary.html), [Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/index.html), [Java SE 25 API documentation](https://docs.oracle.com/en/java/javase/25/docs/api/), [Oracle JDK migration guide](https://docs.oracle.com/en/java/javase/25/migrate/migrating-jdk-8-later-jdk-releases.html)
- JavaScript: [ECMAScript 2025 specification](https://262.ecma-international.org/16.0/), [Node.js ECMAScript modules](https://nodejs.org/dist/latest/docs/api/esm.html), [Node.js release schedule](https://nodejs.org/en/about/previous-releases)
- TypeScript: [TypeScript release notes](https://www.typescriptlang.org/docs/handbook/release-notes/), [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/), [TSConfig reference](https://www.typescriptlang.org/tsconfig/), [TypeScript 5.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html), [TypeScript 6.0 release notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)
- Python: [Python What’s New](https://docs.python.org/3/whatsnew/), [Python Language Reference](https://docs.python.org/3/reference/), [Python Standard Library](https://docs.python.org/3/library/), [What’s New in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html)
- C#: [Microsoft C# version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history), [Microsoft C# language versioning](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning), [Microsoft C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/), [.NET API browser](https://learn.microsoft.com/en-us/dotnet/api/)
