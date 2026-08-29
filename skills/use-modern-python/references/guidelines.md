# Python version rules

Use these rules after resolving the package's explicit `requires-python` target. The
interpreter version controls both syntax and standard-library availability.

## Python 3.9+

- Use built-in collection generics (`list[str]`, `dict[str, int]`) in annotations.
- Use `pathlib.Path` for filesystem paths and `zoneinfo.ZoneInfo` for IANA time zones.
- Use `str.removeprefix`/`removesuffix` when the operation is a prefix/suffix operation, not arbitrary replacement.
- Prefer `collections.abc` for public iterable/mapping protocols.

## Python 3.10+

- Use structural pattern matching for finite data shapes when it is clearer than nested conditionals.
- Use `X | Y` for union types and `TypeGuard` for user-defined narrowing.
- Use `zip(..., strict=True)` when equal-length inputs are an invariant.

## Python 3.11+

- Use `ExceptionGroup` and `except*` for genuinely concurrent operations that can fail independently.
- Use `asyncio.TaskGroup` for structured sibling-task lifetimes; prefer it to manually managed task lists.
- Use `tomllib` for reading TOML instead of adding a TOML parser for read-only configuration.
- Use `typing.Self`, `LiteralString`, and `StrEnum` where they express a real contract.

## Python 3.12+

- Use the `type` statement and type-parameter syntax for generic aliases/functions/classes when it improves the public type model.
- Use `typing.override` when overriding a base method in a typed class hierarchy.
- Use the relaxed f-string expression grammar, but keep expressions simple enough to read.

```python
type UserId = int

def first[T](items: list[T]) -> T:
    return items[0]
```

## Python 3.13+

- Treat free-threaded CPython as an explicit deployment/runtime choice; do not assume the GIL is present or absent without project configuration.
- Use the improved standard-library APIs only when the declared interpreter target includes them.
- Do not enable the experimental JIT or free-threaded build as an incidental style change.

## Python 3.14+

- Use `concurrent.interpreters` for explicit subinterpreter coordination and `concurrent.futures.InterpreterPoolExecutor` for workloads that benefit from isolated interpreters; verify extension-module compatibility first.
- When introspecting annotations at runtime, use the documented `annotationlib` APIs rather than reading `__annotations__` dictionaries directly.
- Treat annotations as lazily evaluated in Python 3.14+; request an explicit
  annotation format when runtime introspection needs values, strings, or ASTs.
- Use template string literals (`t"..."`) for custom string-processing APIs, not
  ordinary interpolation; use f-strings when the result should be a string.
- Use `compression.zstd` instead of a third-party Zstandard binding when the
  project target and deployment environment provide it.
- Do not use `return`, `break`, or `continue` to leave a `finally` block;
  Python 3.14 rejects that control flow.
- Do not add `from __future__ import annotations` merely as a cross-version habit when the project targets 3.14+.
- On Unix, account for the `forkserver` multiprocessing default when code relies on fork inheritance or pickling behavior.

## Cross-version style

- Keep imports at module scope unless a real import cycle or optional dependency requires otherwise.
- Use context managers for resources and make ownership visible at the call site.
- Use `dataclass` for data with behavior/validation; use plain dictionaries for genuinely unstructured payloads.
- Avoid mutable default arguments, broad `except Exception`, and hidden global state.

## Authority

- [Python What’s New](https://docs.python.org/3/whatsnew/)
- [Python Language Reference](https://docs.python.org/3/reference/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [What’s New in Python 3.14](https://docs.python.org/3.14/whatsnew/3.14.html)
