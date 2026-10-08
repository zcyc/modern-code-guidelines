# Shell

## Portability and arguments

- POSIX sh and Bash are separate targets. Bash arrays, [[ ]], mapfile and version-sensitive features require a declared Bash runtime; GNU utility flags require declared GNU tools even in a POSIX script.
- Quote expansions unless splitting/globbing is intentional; Bash arrays preserve argv. Pass untrusted text as arguments/environment, never eval/generated shell source.
- Read data with IFS= read -r; printf is more predictable than echo. Do not parse ls or lose filenames/trailing newlines through command substitution.
- Move substantial structured parsing to a suitable language; retain only necessary external tool dependencies.

## Failure and lifetime

- Check meaningful exit statuses, including pipeline members. set -e has exceptions and is not a complete control-flow model.
- Use mktemp and owned cleanup traps; constrain destructive operations to validated paths. Preserve the original failure status through cleanup.
- Emit actionable errors to stderr; bound retries/backoff/timeouts. Use existing ShellCheck/formatter config.

## Sources

- https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
- https://www.gnu.org/software/bash/manual/bash.html
- https://www.shellcheck.net/wiki/
