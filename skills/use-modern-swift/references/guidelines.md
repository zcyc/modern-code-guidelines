# Swift

## Isolation and ownership

- Prefer value types; classes/actors represent identity/shared state. Optionals/enums model absence/finite domains; !/try! require proven invariants.
- Follow call-site API clarity and narrow access control. async/await does not itself establish isolation: own tasks, cancellation and actor boundaries.
- Sendable is a cross-isolation contract; unchecked conformance needs an audited invariant. MainActor expresses UI ownership, not a blanket diagnostics workaround.

## Gates

- Swift 5.9: macros and parameter packs require supporting toolchain/target and a real contract benefit.
- Swift 6 language mode: repair strict-concurrency isolation/sendability errors at their boundary.
- 6.2: @concurrent explicitly leaves caller isolation; ordinary async executor behavior also depends on concurrency settings. Span/InlineArray need clear lifetimes and measured memory reasons.
- 6.3: @c for reviewed C exports; module selectors resolve actual import-name collisions.
- 6.4: Swift Build is SwiftPM's default; verify plugins/caches/CI. Async defer and withTaskCancellationShield support awaited cleanup that must finish despite cancellation.

## Tests and tools

- Swift Testing requires Swift 6/Xcode 16 tooling; prefer it for new unit/integration tests. XCTest remains for UI/performance and existing suites; both coexist in one bundle.
- Swift 6.4 permits XCTAssert in Testing tests and #expect in XCTest tests. Check test-target toolchain/deployment separately; keep async tests deterministic and cancellation-aware.
- Use configured swift-format/lint rather than introducing another formatting policy.

## Sources

- [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/)
- [Swift 6.4 release](https://www.swift.org/blog/swift-6.4-released/)
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html)
- [Swift Testing](https://developer.apple.com/documentation/testing)
- [XCTest](https://developer.apple.com/documentation/xctest)
- [Swift 6 migration: data-race safety](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/dataracesafety/)
- [Swift Evolution](https://www.swift.org/swift-evolution/)
