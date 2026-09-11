# Shell version rules

Resolve the shell from the shebang and the execution environment. POSIX `sh`,
Bash, and other shells are different languages; a script must not silently rely
on the interactive shell or on a newer local installation.

## Portability and syntax

- Use POSIX shell syntax for `#!/bin/sh` scripts. Use Bash arrays, `[[ ... ]]`,
  `mapfile`, and other Bash features only under an explicit Bash shebang and
  declared Bash target.
- Keep shell logic small. Move substantial parsing or data transformation to a
  language with structured types instead of growing a string-processing DSL.
- Prefer shell built-ins and standard utilities already required by the target
  environment; document a non-portable command when it is a real dependency.
- Do not use GNU-only flags in a POSIX script unless the runtime declares GNU
  utilities. Choose a portable form or make the dependency explicit.

## Expansion and input

- Quote expansions unless word splitting and pathname expansion are intentional.
  Use arrays to preserve argument boundaries in Bash.
- Read lines with `IFS= read -r` when line content is data. Do not parse `ls`
  output or use command substitution when it can lose trailing newlines or split
  filenames.
- Keep untrusted text out of `eval`, `sh -c`, and generated source. Pass values as
  arguments or environment variables with an explicit validation contract.

## Failure and cleanup

- Check the status of commands whose failure matters, including commands inside
  pipelines. If strict mode is used, handle its documented exceptions explicitly
  instead of treating `errexit` as a complete error model.
- Use `mktemp` for temporary paths and a `trap` for cleanup owned by the script.
  Narrow destructive operations to validated paths; never use a broad recursive
  target assembled from unchecked input.
- Emit actionable errors to stderr and preserve the failing command's status.
  Keep retries bounded and make backoff or timeout behavior explicit.

## Authority

- https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
- https://www.gnu.org/software/bash/manual/bash.html
- https://www.shellcheck.net/wiki/
