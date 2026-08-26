# Modern Code Guidelines

[English](README.md)

这是一个同时面向 Codex、Cursor 和 Claude Code 的共享 skill 包，包含五个可独立触发的语言 skill：

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

每个 skill 都会读取项目明确声明的语言、编译器或运行时版本，只应用该版本可用且稳定的现代实践。

JavaScript skill 覆盖 ECMAScript 和 Node.js；TypeScript 单独处理编译器与类型系统行为。浏览器 API、CSS、无障碍和 Web 性能仍由 `modern-web-guidance` 负责。

## 规则来源

每个 skill 会先解析项目声明的目标版本，再读取该 skill 旁边的版本规则文件。规则优先参考官方语言规范、版本发布说明、编译器文档，以及运行时/标准库 API 文档：

| 语言 | 版本与语言规则来源 | 运行时/API 来源 |
| --- | --- | --- |
| Java | [Oracle Java Language Updates](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-summary.html)、[Java Language Specification](https://docs.oracle.com/javase/specs/jls/se25/html/index.html) | [Java SE API](https://docs.oracle.com/en/java/javase/25/docs/api/) |
| JavaScript | [ECMAScript 2025](https://262.ecma-international.org/16.0/) | [Node.js API](https://nodejs.org/dist/latest/docs/api/)、[Node.js 版本发布信息](https://nodejs.org/en/about/previous-releases) |
| TypeScript | [TypeScript Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/)、[TypeScript 6.0](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)、[TSConfig Reference](https://www.typescriptlang.org/tsconfig/) | 项目实际使用的 JavaScript 宿主及其运行时/API 文档 |
| Python | [Python What’s New](https://docs.python.org/3/whatsnew/)、[Python 3.14 更新](https://docs.python.org/3.14/whatsnew/3.14.html)、[语言参考](https://docs.python.org/3/reference/) | [Python 标准库](https://docs.python.org/3/library/) |
| C# | [C# 版本历史](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history)、[C# 15 preview](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15)、[语言版本控制](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning) | [C# 语言参考](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)、[.NET API 浏览器](https://learn.microsoft.com/en-us/dotnet/api/) |

详细规则和来源链接位于各 skill 的 `references/guidelines.md`。第三方最佳实践可以用于补充示例，但不能覆盖项目声明的目标版本或上述一手来源。

## 与相关项目的关系

本项目受到 [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 和
[`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 启发，
同时是两个项目的补充，而不是替代品：

- [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 专注于现代 Go 语言和标准库实践。
- [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 专注于 Web API、CSS、无障碍和 Web 性能等浏览器与 Web 平台实践。
- `modern-code-guidelines` 专注于 Java、JavaScript、TypeScript、Python 和 C# 的语言、编译器、运行时及标准库实践。

JavaScript 和 TypeScript skill 有意只覆盖核心语言、编译器、Node.js 和运行时问题；浏览器 UI、CSS、无障碍和 Web 性能仍由 `modern-web-guidance` 负责，因此两个项目可以一起使用，同时保持清晰的职责边界。

## 兼容边界

这里的“支持”是指 Codex、Cursor 和 Claude Code 可以通过各自的插件 manifest 发现并加载同一套 skill。项目不额外维护宿主专属的命令、agent 或重复规则文件。
