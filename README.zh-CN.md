# Modern Code Guidelines

[English](README.md)

这是一个同时面向 Codex、Cursor、Claude Code、Kiro、Google Antigravity、Gemini CLI、GitHub Copilot、Cline、OpenCode、Devin、JetBrains Junie 和 OpenHands 的共享 skill 包，包含三十五个可独立触发的语言与框架 skill：

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

语言 skill 都会读取项目明确声明的语言、编译器或运行时版本，只应用该版本可用且稳定的现代实践。各语言的版本规则与 skill 放在一起。

## 支持的框架

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

框架 skill 还会解析框架、构建工具、部署目标和项目架构，再应用版本敏感的规则。浏览器 API、CSS、无障碍和 Web 性能仍由 `modern-web-guidance` 负责。

JavaScript skill 覆盖 ECMAScript 和 Node.js；TypeScript 单独处理编译器与类型系统行为。浏览器 API、CSS、无障碍和 Web 性能仍由 `modern-web-guidance` 负责。

## 规则来源

每个 skill 会先解析项目声明的目标版本，再读取本地规则文件。规则优先参考官方语言与框架规范、版本发布说明、编译器文档，以及运行时/标准库/平台 API 文档：

| 语言 | 版本与语言规则来源 | 运行时/API 来源 |
| --- | --- | --- |
| Java | [Oracle Java Language Updates](https://docs.oracle.com/en/java/javase/26/language/java-language-changes-summary.html)、[Java Language Specification](https://docs.oracle.com/javase/specs/jls/se26/html/index.html) | [Java SE API](https://docs.oracle.com/en/java/javase/26/docs/api/) |
| JavaScript | [ECMAScript 2026](https://tc39.es/ecma262/2026/multipage/) | [Node.js API](https://nodejs.org/dist/latest/docs/api/)、[Node.js 版本发布信息](https://nodejs.org/en/about/previous-releases) |
| TypeScript | [TypeScript Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/)、[TypeScript 7](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)、[TSConfig Reference](https://www.typescriptlang.org/tsconfig/) | 项目实际使用的 JavaScript 宿主及其运行时/API 文档 |
| Python | [Python What’s New](https://docs.python.org/3/whatsnew/)、[Python 3.14 更新](https://docs.python.org/3.14/whatsnew/3.14.html)、[语言参考](https://docs.python.org/3/reference/) | [Python 标准库](https://docs.python.org/3/library/) |
| C# | [C# 版本历史](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history)、[C# 15 preview](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15)、[语言版本控制](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-versioning) | [C# 语言参考](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)、[.NET API 浏览器](https://learn.microsoft.com/en-us/dotnet/api/) |
| Go | [Go 语言规范](https://go.dev/ref/spec)、[Effective Go](https://go.dev/doc/effective_go)、[Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)、[Go 1.27 发布说明](https://go.dev/doc/go1.27)；补充参考 [Modern Go Guidelines](https://github.com/JetBrains/go-modern-guidelines) | [Go 标准库](https://pkg.go.dev/std)、[Go 版本历史](https://go.dev/doc/devel/release) |
| Rust | [Rust Edition Guide](https://doc.rust-lang.org/edition-guide/)、[Rust Style Guide](https://doc.rust-lang.org/style-guide/) | [Rust 发布说明](https://doc.rust-lang.org/stable/releases.html)、[Rust 标准库](https://doc.rust-lang.org/std/)、[Cargo Book](https://doc.rust-lang.org/cargo/) |
| Scala | [Scala 发布线](https://www.scala-lang.org/download/)、[Scala 3 Reference](https://docs.scala-lang.org/scala3/reference/) | [Scala/JDK 兼容性](https://docs.scala-lang.org/overviews/jdk-compatibility/overview.html)、[sbt](https://www.scala-sbt.org/)、[Scalafmt](https://scalameta.org/scalafmt/)、[Scalafix](https://scalacenter.github.io/scalafix/) |
| C++ | [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html)、[ISO/IEC 14882:2024](https://www.iso.org/standard/83626.html)、[C++26 工作论文](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/) | [cppreference C++ 语言](https://en.cppreference.com/w/cpp/language)、[标准库](https://en.cppreference.com/w/cpp/standard_library) |
| Swift | [Swift 6.3 发布说明](https://www.swift.org/blog/swift-6.3-released/)、[Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/)、[Swift Evolution](https://www.swift.org/swift-evolution/) | [Swift Book](https://docs.swift.org/swift-book/)、[Swift 并发](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) |
| Kotlin | [Kotlin 2.0 更新](https://kotlinlang.org/docs/whatsnew20.html)、[Kotlin 2.4 更新](https://kotlinlang.org/docs/whatsnew24.html)、[Kotlin 编码约定](https://kotlinlang.org/docs/coding-conventions.html) | [Kotlin 语言文档](https://kotlinlang.org/docs/kotlin-reference.html)、[Kotlin 协程指南](https://kotlinlang.org/docs/coroutines-guide.html) |
| Dart | [Dart 3.13 发布说明](https://dart.dev/blog/announcing-dart-3-13)、[Effective Dart](https://dart.dev/effective-dart) | [Dart 语言规范](https://spec.dart.dev/)、[Dart lint 规则](https://dart.dev/tools/linter-rules) |
| PHP | [PHP 8.5 发布说明](https://www.php.net/releases/8.5/en.php)、[PHP 语言手册](https://www.php.net/manual/en/langref.php) | [PHP 标准库](https://www.php.net/manual/en/book.standard.php)、[PHP-FIG PSR](https://www.php-fig.org/psr/) |
| Ruby | [Ruby 4.0 发布说明](https://www.ruby-lang.org/en/news/2025/12/25/ruby-4-0-0-released/)、[Ruby 文档](https://www.ruby-lang.org/en/documentation/)、[RuboCop 风格规则](https://docs.rubocop.org/rubocop/latest/cops_style.html) | [Ruby Core API](https://docs.ruby-lang.org/en/) |
| C | [ISO/IEC 9899:2024（C23）](https://www.iso.org/standard/82075.html)、[C 语言参考](https://en.cppreference.com/w/c/language)、[SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c) | [C 标准库参考](https://en.cppreference.com/w/c/header) |
| SQL | [ISO/IEC 9075:2023](https://www.iso.org/standard/76583.html)、[SQLFluff 规则](https://docs.sqlfluff.com/en/stable/reference/rules.html) | [PostgreSQL 发布说明](https://www.postgresql.org/docs/release/)，或项目所选数据库厂商的 SQL 与事务文档 |

### 框架规则来源

| 框架 | 发布、版本与兼容性来源 | 架构与 API 来源 |
| --- | --- | --- |
| React | [React versions](https://react.dev/versions)、[React 19.2](https://react.dev/blog/2025/10/01/react-19-2) | [Rules of React](https://react.dev/reference/rules)、[React Compiler](https://react.dev/learn/react-compiler/introduction)、[React Actions](https://react.dev/reference/react/useActionState) |
| Next.js | [Next.js 16](https://nextjs.org/blog/next-16)、[Next.js release blog](https://nextjs.org/blog) | [App Router](https://nextjs.org/docs/app)、[Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)、[`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache)、[Cache Components](https://nextjs.org/docs/app/getting-started/partial-prerendering)、[Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) |
| Vue | [Vue releases](https://github.com/vuejs/core/releases) | [Vue introduction](https://vuejs.org/guide/introduction)、[Composition API FAQ](https://vuejs.org/guide/extras/composition-api-faq)、[Vue with TypeScript](https://vuejs.org/guide/typescript/overview)、[Composables](https://vuejs.org/guide/reusability/composables) |
| Angular | [Angular releases](https://angular.dev/reference/releases)、[Version compatibility](https://angular.dev/reference/versions) | [Angular overview](https://angular.dev/overview)、[Component anatomy](https://angular.dev/guide/components)、[Signals](https://angular.dev/guide/signals)、[Zoneless](https://angular.dev/guide/zoneless)、[Standalone migration](https://angular.dev/reference/migrations/standalone)、[`resource`](https://angular.dev/guide/signals/resource) |
| Spring Boot | [Spring Boot project](https://spring.io/projects/spring-boot) | [Spring Boot reference](https://docs.spring.io/spring-boot/reference/)、[Spring Security reference](https://docs.spring.io/spring-security/reference/)、[Spring application features](https://docs.spring.io/spring-boot/reference/features/spring-application.html)、[Observability](https://docs.spring.io/spring-boot/reference/actuator/observability.html)、[Reactive web](https://docs.spring.io/spring-boot/reference/web/reactive.html) |
| ASP.NET Core | [ASP.NET Core release notes](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-10.0?view=aspnetcore-10.0) | [ASP.NET Core docs](https://learn.microsoft.com/en-us/aspnet/core/)、[Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)、[Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware)、[Dependency injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)、[Error handling](https://learn.microsoft.com/en-us/aspnet/core/web-api/handle-errors) |
| Django | [Django 6.1 release](https://docs.djangoproject.com/en/6.1/releases/6.1/)、[Django 6.0 release](https://docs.djangoproject.com/en/6.0/releases/6.0/) | [Django documentation](https://docs.djangoproject.com/en/stable/)、[Async support](https://docs.djangoproject.com/en/stable/topics/async/)、[Tasks](https://docs.djangoproject.com/en/stable/topics/tasks/)、[Database optimization](https://docs.djangoproject.com/en/stable/topics/db/optimization/)、[Transactions](https://docs.djangoproject.com/en/stable/topics/db/transactions/)、[Security](https://docs.djangoproject.com/en/stable/topics/security/) |
| FastAPI | [FastAPI release notes](https://fastapi.tiangolo.com/release-notes/) | [FastAPI documentation](https://fastapi.tiangolo.com/)、[Async](https://fastapi.tiangolo.com/async/)、[Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)、[Events](https://fastapi.tiangolo.com/advanced/events/)、[Response models](https://fastapi.tiangolo.com/tutorial/response-model/) |
| Flutter | [Flutter what's new](https://docs.flutter.dev/release/whats-new) | [Architectural overview](https://docs.flutter.dev/resources/architectural-overview)、[App architecture](https://docs.flutter.dev/app-architecture/guide)、[State management](https://docs.flutter.dev/data-and-backend/state-mgmt/intro)、[Performance](https://docs.flutter.dev/perf)、[Accessibility](https://docs.flutter.dev/ui/accessibility-and-internationalization) |
| SwiftUI | [iOS and iPadOS release notes](https://developer.apple.com/documentation/ios-ipados-release-notes) | [SwiftUI documentation](https://developer.apple.com/documentation/SwiftUI)、[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)、[Model data](https://developer.apple.com/documentation/swiftui/model-data)、[NavigationStack](https://developer.apple.com/documentation/swiftui/navigationstack)、[`task`](https://developer.apple.com/documentation/swiftui/task) |
| NestJS | [Migration guide](https://docs.nestjs.com/migration-guide) | [NestJS documentation](https://docs.nestjs.com/)、[Modules](https://docs.nestjs.com/modules)、[Providers](https://docs.nestjs.com/providers)、[Pipes](https://docs.nestjs.com/pipes)、[Guards](https://docs.nestjs.com/guards)、[Interceptors](https://docs.nestjs.com/interceptors)、[Security](https://docs.nestjs.com/security) |
| Nuxt | [Nuxt releases](https://github.com/nuxt/nuxt/releases) | [Nuxt 4 data fetching](https://nuxt.com/docs/4.x/getting-started/data-fetching)、[Nuxt 4 rendering](https://nuxt.com/docs/4.x/guide/concepts/rendering)、[Nuxt 3 data fetching](https://nuxt.com/docs/3.x/getting-started/data-fetching)、[Server directory](https://nuxt.com/docs/4.x/directory-structure/server)、[Server components](https://nuxt.com/docs/4.x/guide/concepts/server-components)、[Configuration](https://nuxt.com/docs/4.x/getting-started/configuration) |
| Expo | [Expo SDK versions](https://docs.expo.dev/versions/latest/)、[Upgrade the Expo SDK](https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough/) | [Workflow overview](https://docs.expo.dev/workflow/overview/)、[Configuration](https://docs.expo.dev/workflow/configuration/)、[Development builds](https://docs.expo.dev/develop/development-builds/introduction/)、[Expo Router](https://docs.expo.dev/router/introduction/)、[EAS Update runtime versions](https://docs.expo.dev/eas-update/runtime-versions/)、[Using libraries](https://docs.expo.dev/workflow/using-libraries/) |
| React Native | [Release overview](https://reactnative.dev/releases/overview)、[React Native 0.87](https://reactnative.dev/blog/2026/08/11/react-native-0.87) | [Architecture](https://reactnative.dev/architecture/landing-page)、[New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page)、[Turbo Native Modules](https://reactnative.dev/docs/turbo-native-modules-introduction)、[FlatList optimization](https://reactnative.dev/docs/optimizing-flatlist-configuration) |
| SvelteKit | [SvelteKit releases](https://github.com/sveltejs/kit/releases) | [Svelte runes](https://svelte.dev/docs/svelte/what-are-runes)、[Load](https://svelte.dev/docs/kit/load)、[Form actions](https://svelte.dev/docs/kit/form-actions)、[Hooks](https://svelte.dev/docs/kit/hooks)、[`$app/state`](https://svelte.dev/docs/kit/$app-state)、[adapter-auto](https://svelte.dev/docs/kit/adapter-auto) |
| Astro | [Astro 7](https://astro.build/blog/astro-7/) | [Islands](https://docs.astro.build/en/concepts/islands/)、[Content collections](https://docs.astro.build/en/guides/content-collections/)、[On-demand rendering](https://docs.astro.build/en/guides/on-demand-rendering/)、[Server islands](https://docs.astro.build/en/guides/server-islands/)、[Actions](https://docs.astro.build/en/guides/actions/)、[Middleware](https://docs.astro.build/en/guides/middleware/) |
| Jetpack Compose | [Compose releases](https://developer.android.com/jetpack/androidx/releases/compose) | [Compose architecture](https://developer.android.com/develop/ui/compose/architecture)、[Android architecture](https://developer.android.com/topic/architecture)、[State](https://developer.android.com/develop/ui/compose/state)、[State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)、[Side-effects](https://developer.android.com/develop/ui/compose/side-effects) |
| Laravel | [Laravel releases](https://laravel.com/framework/docs/releases) | [Laravel documentation](https://laravel.com/docs)、[Routing](https://laravel.com/docs/routing)、[Validation](https://laravel.com/docs/validation)、[Authorization](https://laravel.com/docs/authorization)、[Eloquent relationships](https://laravel.com/docs/eloquent-relationships)、[Queues](https://laravel.com/docs/queues)、[Migrations](https://laravel.com/docs/migrations) |
| Rails | [Rails releases](https://rubyonrails.org/category/releases)、[Upgrading Rails](https://guides.rubyonrails.org/upgrading_ruby_on_rails.html) | [Rails guides](https://guides.rubyonrails.org/)、[Getting started](https://guides.rubyonrails.org/getting_started.html)、[Active Record basics](https://guides.rubyonrails.org/active_record_basics.html)、[Active Record querying](https://guides.rubyonrails.org/active_record_querying.html)、[Active Job](https://guides.rubyonrails.org/active_job_basics.html) |

详细规则和来源链接位于各 skill 自带的 `references/guidelines.md`。框架 references 以对应框架的官方文档为主要来源。第三方最佳实践可以用于补充示例，但不能覆盖项目声明的目标版本或上述一手来源。

## 与相关项目的关系

本项目受到 [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 和
[`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 启发，
同时是两个项目的补充，而不是替代品：

- [`modern-go-guidelines`](https://github.com/JetBrains/go-modern-guidelines) 专注于现代 Go 语言和标准库实践。
- [`modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) 专注于 Web API、CSS、无障碍和 Web 性能等浏览器与 Web 平台实践。
- `modern-code-guidelines` 专注于上述语言的版本感知语言、编译器、运行时、标准库、数据库及安全编码实践。Go 规则以官方 Go 文档为准，JetBrains 的 `go-modern-guidelines` 仅作补充参考；格式化、测试和正确性检查则按项目需要选择最合适的工具，不绑定某个 CLI 入口。

JavaScript 和 TypeScript skill 有意只覆盖核心语言、编译器、Node.js 和运行时问题；浏览器 UI、CSS、无障碍和 Web 性能仍由 `modern-web-guidance` 负责，因此两个项目可以一起使用，同时保持清晰的职责边界。

## 兼容边界

Codex、Cursor 和 Claude Code 通过各自的插件 manifest 发现并加载本包。直接打开本仓库时，Kiro、GitHub Copilot、Cline、OpenCode、Devin、JetBrains Junie 和 OpenHands 通过 `AGENTS.md` 加载，Gemini CLI 通过 `GEMINI.md` 加载。`npx skills` 命令只将唯一的 `skills/` 源目录安装到指定宿主的原生路径，不会复制根目录指令文件。所有入口都指向同一套 skill 规则。
