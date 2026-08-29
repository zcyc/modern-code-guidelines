# Modern Code Guidelines

[English](README.md)

这是一个同时面向 Codex、Cursor 和 Claude Code 的共享 skill 包，包含十六个可独立触发的语言 skill：

- Codex：`.codex-plugin/plugin.json`
- Cursor：`.cursor-plugin/plugin.json`
- Claude Code：`.claude-plugin/plugin.json`

三个宿主共用同一个 `skills/` 目录，不复制规则，避免不同集成之间逐渐产生差异。

项目也提供用于仓库或本地安装的三个宿主 marketplace catalog：

- Codex：`.agents/plugins/marketplace.json`
- Cursor：`.cursor-plugin/marketplace.json`
- Claude Code：`.claude-plugin/marketplace.json`

项目通过代码仓库直接分发，不提交官方插件商店。

## 安装

本仓库地址为
[`zcyc/modern-code-guidelines`](https://github.com/zcyc/modern-code-guidelines)。三个宿主使用的
marketplace 名称都是 `modern-code-guidelines`。

### Codex

在终端执行。第一条命令添加仓库 marketplace，第二条命令安装插件：

```bash
codex plugin marketplace add zcyc/modern-code-guidelines
codex plugin add modern-code-guidelines@modern-code-guidelines
```

如果使用本地 checkout，将 `zcyc/modern-code-guidelines` 替换为本地绝对路径。

### Cursor

先在终端添加仓库 marketplace，再在 Cursor 的 `/plugins` 界面安装插件：

```bash
cursor-agent plugin marketplace add https://github.com/zcyc/modern-code-guidelines
```

打开 `/plugins`，选择 `modern-code-guidelines` marketplace，然后安装
`modern-code-guidelines`。

### Claude Code

在 Claude Code 会话中执行：

```text
/plugin marketplace add zcyc/modern-code-guidelines
/plugin install modern-code-guidelines@modern-code-guidelines
```

如果使用本地 checkout，将本地绝对路径传给 `/plugin marketplace add`。

### 更新

先刷新 marketplace，再重新安装或更新插件：

```bash
# Codex
codex plugin marketplace upgrade modern-code-guidelines
codex plugin remove modern-code-guidelines@modern-code-guidelines
codex plugin add modern-code-guidelines@modern-code-guidelines

# Claude Code
claude plugin marketplace update modern-code-guidelines
claude plugin update modern-code-guidelines@modern-code-guidelines
```

Cursor 使用 `cursor-agent plugin marketplace update modern-code-guidelines` 刷新；
如果缓存版本没有变化，重新打开 Cursor 并在 `/plugins` 中重新安装。

## 支持的语言

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

每个 skill 都会读取项目明确声明的语言、编译器或运行时版本，只应用该版本可用且稳定的现代实践。各语言的版本规则与 skill 放在一起。

JavaScript skill 覆盖 ECMAScript 和 Node.js；TypeScript 单独处理编译器与类型系统行为。浏览器 API、CSS、无障碍和 Web 性能仍由 `modern-web-guidance` 负责。

## 规则来源

每个 skill 会先解析项目声明的目标版本，再读取本地规则文件。规则优先参考官方语言规范、版本发布说明、编译器文档，以及运行时/标准库 API 文档：

| 语言 | 版本与语言规则来源 | 运行时/API 来源 |
| --- | --- | --- |
| Java | [Oracle Java Language Updates](https://docs.oracle.com/en/java/javase/26/language/java-language-changes-summary.html)、[Java Language Specification](https://docs.oracle.com/javase/specs/jls/se26/html/index.html) | [Java SE API](https://docs.oracle.com/en/java/javase/26/docs/api/) |
| JavaScript | [ECMAScript 2026](https://tc39.es/ecma262/2026/multipage/) | [Node.js API](https://nodejs.org/dist/latest/docs/api/)、[Node.js 版本发布信息](https://nodejs.org/en/about/previous-releases) |
| TypeScript | [TypeScript Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/)、[TypeScript 7](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)、[TSConfig Reference](https://www.typescriptlang.org/tsconfig/) | 项目实际使用的 JavaScript 宿主及其运行时/API 文档 |
| Python | [Python What’s New](https://docs.python.org/3/whatsnew/)、[Python 3.14 更新](https://docs.python.org/3.14/whatsnew/3.14.html)、[语言参考](https://docs.python.org/3/reference/) | [Python 标准库](https://docs.python.org/3/library/) |
| C# | [C# 版本历史](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history)、[C# 15 preview](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15)、[语言版本控制](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning) | [C# 语言参考](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)、[.NET API 浏览器](https://learn.microsoft.com/en-us/dotnet/api/) |
| Go | [Go 语言规范](https://go.dev/ref/spec)、[Effective Go](https://go.dev/doc/effective_go)、[Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)、[Go 1.27 发布说明](https://go.dev/doc/go1.27)；补充参考 [Modern Go Guidelines](https://github.com/JetBrains/go-modern-guidelines) | [Go 标准库](https://pkg.go.dev/std)、[Go 版本历史](https://go.dev/doc/devel/release) |
| Rust | [Rust Edition Guide](https://doc.rust-lang.org/edition-guide/)、[Rust Style Guide](https://doc.rust-lang.org/style-guide/) | [Rust 发布说明](https://doc.rust-lang.org/stable/releases.html)、[Rust 标准库](https://doc.rust-lang.org/std/)、[Cargo Book](https://doc.rust-lang.org/cargo/) |
| Scala | [Scala 3.8.4 / 3.3.8 LTS / 2.13.18 发布版本](https://www.scala-lang.org/download/)、[Scala 3 Reference](https://docs.scala-lang.org/scala3/reference/) | [Scala/JDK 兼容性](https://docs.scala-lang.org/overviews/jdk-compatibility/overview.html)、[sbt](https://www.scala-sbt.org/)、[Scalafmt](https://scalameta.org/scalafmt/)、[Scalafix](https://scalacenter.github.io/scalafix/) |
| C++ | [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html)、[ISO/IEC 14882:2024](https://www.iso.org/standard/83626.html)、[C++26 工作论文](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/) | [cppreference C++ 语言](https://en.cppreference.com/w/cpp/language)、[标准库](https://en.cppreference.com/w/cpp/standard_library) |
| Swift | [Swift 6.3 发布说明](https://www.swift.org/blog/swift-6.3-released/)、[Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/)、[Swift Evolution](https://www.swift.org/swift-evolution/) | [Swift Book](https://docs.swift.org/swift-book/)、[Swift 并发](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) |
| Kotlin | [Kotlin 2.0 更新](https://kotlinlang.org/docs/whatsnew20.html)、[Kotlin 2.4 更新](https://kotlinlang.org/docs/whatsnew24.html)、[Kotlin 编码约定](https://kotlinlang.org/docs/coding-conventions.html) | [Kotlin 语言文档](https://kotlinlang.org/docs/kotlin-reference.html)、[Kotlin 协程指南](https://kotlinlang.org/docs/coroutines-guide.html) |
| Dart | [Dart 3.13 发布说明](https://dart.dev/blog/announcing-dart-3-13)、[Effective Dart](https://dart.dev/effective-dart) | [Dart 语言规范](https://spec.dart.dev/)、[Dart lint 规则](https://dart.dev/tools/linter-rules) |
| PHP | [PHP 8.5 发布说明](https://www.php.net/releases/8.5/en.php)、[PHP 语言手册](https://www.php.net/manual/en/langref.php) | [PHP 标准库](https://www.php.net/manual/en/book.standard.php)、[PHP-FIG PSR](https://www.php-fig.org/psr/) |
| Ruby | [Ruby 4.0 发布说明](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/)、[Ruby 文档](https://www.ruby-lang.org/en/documentation/)、[RuboCop 风格规则](https://docs.rubocop.org/rubocop/latest/cops_style.html) | [Ruby Core API](https://docs.ruby-lang.org/en/) |
| C | [ISO/IEC 9899:2024（C23）](https://www.iso.org/standard/82075.html)、[C 语言参考](https://en.cppreference.com/w/c/language)、[SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c) | [C 标准库参考](https://en.cppreference.com/w/c/header) |
| SQL | [ISO/IEC 9075:2023](https://www.iso.org/standard/76583.html)、[SQLFluff 规则](https://docs.sqlfluff.com/en/stable/reference/rules.html) | [PostgreSQL 发布说明](https://www.postgresql.org/docs/release/)，或项目所选数据库厂商的 SQL 与事务文档 |

详细规则和来源链接位于各 skill 自带的 `references/guidelines.md`。第三方最佳实践可以用于补充示例，但不能覆盖项目声明的目标版本或上述一手来源。

## 与相关项目的关系

本项目受到 [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 和
[`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 启发，
同时是两个项目的补充，而不是替代品：

- [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 专注于现代 Go 语言和标准库实践。
- [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 专注于 Web API、CSS、无障碍和 Web 性能等浏览器与 Web 平台实践。
- `modern-code-guidelines` 专注于上述语言的版本感知语言、编译器、运行时、标准库、数据库及安全编码实践。Go 规则以官方 Go 文档为准，JetBrains 的 `go-modern-guidelines` 仅作补充参考；格式化、测试和正确性检查则按项目需要选择最合适的工具，不绑定某个 CLI 入口。

JavaScript 和 TypeScript skill 有意只覆盖核心语言、编译器、Node.js 和运行时问题；浏览器 UI、CSS、无障碍和 Web 性能仍由 `modern-web-guidance` 负责，因此两个项目可以一起使用，同时保持清晰的职责边界。

## 兼容边界

这里的“支持”是指 Codex、Cursor 和 Claude Code 可以通过各自的插件 manifest 发现并加载同一套 skill。项目不额外维护宿主专属的命令、agent 或重复规则文件。
