# Modern Code Guidelines

[English](README.md)

这是一个同时面向 Codex、Cursor、Claude Code、Kiro、Google Antigravity、Gemini CLI、GitHub Copilot、Cline、OpenCode、Devin、JetBrains Junie 和 OpenHands 的共享 skill 包，包含四十二个可独立触发的语言与框架 skill：

- Codex：`.codex-plugin/plugin.json`
- Cursor：`.cursor-plugin/plugin.json`
- Claude Code：`.claude-plugin/plugin.json`

项目统一维护源目录，并提供分发入口：

- `skills/`：唯一的 Agent Skills 源目录。
- `AGENTS.md`：直接打开本仓库时使用的常驻项目指令。
- `GEMINI.md`：直接 checkout 本仓库时的 Gemini CLI 上下文入口，会导入 `AGENTS.md`。
- `npx skills`：只将唯一的 `skills/` 源目录安装到指定宿主的原生路径。
- 插件 manifest：Codex、Cursor 和 Claude Code。

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

### 原生 Agent Skills（`npx skills`）

```bash
# 在目标项目根目录执行。
# 交互式安装：
npx skills add zcyc/modern-code-guidelines

# 将全部 skill 安装到一个宿主。
npx skills add zcyc/modern-code-guidelines \
  --skill '*' \
  --agent gemini-cli \
  --yes

# --agent 支持：
# codex cursor claude-code gemini-cli antigravity kiro-cli
# github-copilot cline opencode devin junie openhands

# 将全部 skill 安装到本项目支持的宿主。
npx skills add zcyc/modern-code-guidelines \
  --skill '*' \
  --agent codex cursor claude-code gemini-cli antigravity kiro-cli \
  --agent github-copilot cline opencode devin junie openhands \
  --yes

# 查看和更新。
npx skills ls -a gemini-cli
npx skills update

# 不支持 symlink 时使用 --copy。
npx skills add zcyc/modern-code-guidelines --skill '*' --agent gemini-cli --copy
```

## 支持的语言（17 个）

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

语言 skill 都会读取项目明确声明的语言、编译器或运行时版本，只应用该版本可用且稳定的现代实践。各语言的版本规则与 skill 放在一起。

## 支持的框架（25 个）

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

框架 skill 还会解析框架、构建工具、部署目标和项目架构，再应用版本敏感的规则。入口只保留目标解析和路由，具体规则统一放在 references。各 skill 自带目标未知时的处理要求，不依赖安装时复制根目录 `AGENTS.md`。

选择性安装时，需一起安装入口中列出的配套 skill：TypeScript 补充 JavaScript 的类型与编译器规则；Expo 补充 React Native 的 SDK、构建和更新规则。`use-modern-sveltekit` 也覆盖独立 Svelte 项目，仅在使用 Kit 时应用 Kit 专属规则。

Apple 相关 skill 采用分层方式：语言层使用 `use-modern-swift`，然后只添加目标中实际使用的框架。SwiftUI、UIKit、AppKit 的生命周期和平台规则不同，因此保持拆分；SwiftData 的持久化与迁移边界也不同，因此单独保留。

JavaScript skill 覆盖 ECMAScript 和 Node.js；TypeScript 单独处理编译器与类型系统行为。浏览器 API、CSS、无障碍和 Web 性能使用官方浏览器文档或另行安装的 [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance)。该 skill 为可选配套，本包不包含也不会自动安装它。

## 规则来源

每个 skill 先解析项目声明的目标版本，再应用本地规则。版本与 API 来源统一维护在
[skills/](skills/) 下各 skill 的 `references/guidelines.md`，与对应规则放在一起。

优先采用官方语言与框架规范、版本发布说明、编译器文档及运行时/平台 API 文档。
第三方指导可以补充示例，但不能覆盖项目声明的目标版本或一手来源。

规则应帮助作出编码决策：何时采用 API、需要什么版本和运行时，以及行为或安全边界。
仅介绍新版亮点不足以成为规则；具体来源链接与其支持的规则一起维护。

## 与相关项目的关系

本项目受到 [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 和
[`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 启发，
同时是两个项目的补充，而不是替代品：

- [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 专注于现代 Go 语言和标准库实践。
- [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 专注于 Web API、CSS、无障碍和 Web 性能等浏览器与 Web 平台实践。
- `modern-code-guidelines` 专注于上述语言的版本感知语言、编译器、运行时、标准库、数据库及安全编码实践。Go 规则以官方 Go 文档为准，JetBrains 的 `go-modern-guidelines` 仅作补充参考；格式化、测试和正确性检查则按项目需要选择最合适的工具，不绑定某个 CLI 入口。

JavaScript 和 TypeScript skill 有意只覆盖核心语言、编译器、Node.js 和运行时问题；浏览器 UI、CSS、无障碍和 Web 性能可以配合 `modern-web-guidance`，职责边界保持清晰。

## 维护检查

使用 Python 3.11+ 执行，无第三方依赖：

```bash
python scripts/check_skills.py
python -m unittest discover -s scripts -p 'test_*.py'
```

CI 检查 frontmatter、本地引用、配套 skill 名称、插件 manifest 和 README 清单，不验证 API 事实或远程链接可用性。修改版本规则时，逐项核对 API 准确名称、首次支持版本、稳定或预览状态、独立运行时与平台要求，并链接官方发布说明或 API 文档。具体规则只在 references 维护；压缩后仍须保留安全、生命周期、迁移和验证要求。

## 兼容边界

Codex、Cursor 和 Claude Code 通过各自的插件 manifest 发现并加载本包。直接打开本仓库时，Kiro、GitHub Copilot、Cline、OpenCode、Devin、JetBrains Junie 和 OpenHands 通过 `AGENTS.md` 加载，Gemini CLI 通过 `GEMINI.md` 加载。`npx skills` 命令只将唯一的 `skills/` 源目录安装到指定宿主的原生路径，不会复制根目录指令文件。所有入口都指向同一套 skill 规则。
