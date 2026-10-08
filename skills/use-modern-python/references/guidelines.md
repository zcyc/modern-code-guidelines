# Python

## Interpreter gates

- 3.9: built-in collection generics, zoneinfo, removeprefix/removesuffix; pathlib and collections.abc are available earlier.
- 3.10: match, X | Y, TypeGuard and zip(strict=True) for equal-length invariants.
- 3.11: TaskGroup for owned sibling tasks, ExceptionGroup/except* for independent concurrent failures, tomllib for TOML reads, Self/LiteralString/StrEnum.
- 3.12: type aliases/type-parameter syntax, typing.override and relaxed f-string grammar; keep expressions readable.
- 3.13: free-threaded CPython and JIT are explicit deployment choices; check extension compatibility rather than assuming GIL behavior.
- 3.14: concurrent.interpreters/InterpreterPoolExecutor need compatible extensions; compression.zstd needs deployment support. t-strings feed custom processors; f-strings produce strings.
- 3.14 annotations are deferred unless future annotations changes their semantics; inspect with annotationlib VALUE/FORWARDREF/STRING formats. Do not add future annotations automatically.
- 3.14 CPython emits SyntaxWarning for return/break/continue that exits finally; avoid this because it can discard exceptions, not because it is universally rejected.
- 3.14 multiprocessing defaults to forkserver on supported POSIX platforms; macOS remains spawn. Review pickling and inherited state.

## Resources and boundaries

- Validate input at runtime; annotations are not validation. Use aware datetimes for instants and dates for date-only values.
- Use context managers, owned async tasks and observable cancellation; never swallow CancelledError as ordinary failure.
- Keep imports at module scope except real cycles/optional dependencies. Avoid mutable defaults, hidden global state and indiscriminate except Exception.
- Prefer stdlib dataclasses/contextlib/pathlib; dataclasses fit structured data, dictionaries fit unstructured payloads.

## Sources

- [Python What’s New](https://docs.python.org/3/whatsnew/)
- [Python Language Reference](https://docs.python.org/3/reference/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [What’s New in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html)
