---
name: use-modern-shell
description: "Use version-aware POSIX shell and Bash quoting, process, portability, and error-handling idioms when writing, modifying, fixing, or reviewing shell scripts."
---

# Modern Shell

Use for POSIX shell and Bash scripts, including build, CI, and local automation.
Resolve whether the script promises POSIX `sh` portability or requires Bash before
using shell-specific features.

## Target resolution

Read the script shebang, checked-in CI/container images, and documented shell
version. The shell selected by the interactive terminal is not the script's
runtime. If the shell or version is unknown, use POSIX syntax and avoid gated
Bash features.

## Working rules

- Use an explicit shebang and keep the script's portability promise visible.
- Quote parameter expansions by default. Use Bash arrays for argument lists when
  Bash is the target; do not serialize arguments into one string and reparse
  them with `eval`.
- Use `printf`, `read -r`, and explicit exit-status checks. Treat expected
  non-zero commands as data instead of relying on `set -e` to define control flow.
- Create temporary files with `mktemp`, restrict their scope, and clean them with
  a `trap` when the script owns the files.
- Keep external commands at clear trust boundaries. Validate inputs, use safe
  path handling, and never build destructive commands from unchecked text.
- Prefer the repository's ShellCheck and formatter configuration when present;
  do not add a new shell toolchain for a small script change.

Read `references/guidelines.md` for portability, quoting, process lifetime, and
failure-handling rules.
