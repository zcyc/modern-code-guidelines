#!/usr/bin/env python3
"""Check the repository's two-scalar skill format and local routing (Python 3.11+)."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check_repo(root: Path) -> list[str]:
    errors = []
    entries = sorted((root / "skills").glob("*/SKILL.md"))
    names = {entry.parent.name for entry in entries}
    if not entries:
        return ["skills/: no SKILL.md files found"]

    for entry in entries:
        folder = entry.parent
        content = entry.read_text(encoding="utf-8")
        # This package deliberately uses only a plain name and JSON-quoted description.
        header = re.match(r'\A---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: ("[^\n]*")\n---\n', content)
        if header is None:
            errors.append(f"{entry}: expected name and quoted description frontmatter")
        else:
            if header[1] != folder.name or len(header[1]) > 64:
                errors.append(f"{entry}: name must match directory and fit 64 characters")
            try:
                description = json.loads(header[2])
                if not description.strip() or len(description) > 1024 or any(c in description for c in "<>"):
                    errors.append(f"{entry}: description is empty, too long, or contains angle brackets")
            except json.JSONDecodeError:
                errors.append(f"{entry}: description must be a valid quoted scalar")

        reference = folder / "references/guidelines.md"
        if not reference.is_file():
            errors.append(f"{entry}: missing references/guidelines.md")
        elif "https://" not in reference.read_text(encoding="utf-8"):
            errors.append(f"{reference}: missing authoritative source link")
        if "[references/guidelines.md](references/guidelines.md)" not in content:
            errors.append(f"{entry}: missing reference routing link")

        for document in sorted(folder.rglob("*.md")):
            text = document.read_text(encoding="utf-8")
            for dependency in set(re.findall(r"\buse-modern-[a-z0-9]+(?:-[a-z0-9]+)*\b", text)):
                if dependency not in names:
                    errors.append(f"{document}: unknown skill {dependency}")
            for target in re.findall(r"\]\(([^\s)]+)\)", text):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                local = (document.parent / unquote(url.path)).resolve()
                if not local.is_relative_to(folder.resolve()) or not local.exists():
                    errors.append(f"{document}: missing or non-local resource {target}")

    versions = set()
    for host in ("codex", "cursor", "claude"):
        manifest = root / f".{host}-plugin/plugin.json"
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                errors.append(f"{manifest}: expected a JSON object")
                continue
            if data.get("skills") != "./skills/":
                errors.append(f"{manifest}: skills must point to ./skills/")
            version = data.get("version")
            if not isinstance(version, str) or not version:
                errors.append(f"{manifest}: missing version")
            else:
                versions.add(version)
        except (OSError, ValueError) as exc:
            errors.append(f"{manifest}: {exc}")
    if len(versions) > 1:
        errors.append("plugin manifests: versions disagree")

    for catalog in sorted(root.glob(".*-plugin/marketplace.json")) + sorted(root.glob(".agents/plugins/*.json")):
        try:
            json.loads(catalog.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{catalog}: {exc}")

    for readme in (root / "README.md", root / "README.zh-CN.md"):
        if not readme.is_file():
            errors.append(f"{readme}: missing skill inventory")
            continue
        listed = set(re.findall(r"`(use-modern-[a-z0-9-]+)`", readme.read_text(encoding="utf-8")))
        if listed != names:
            errors.append(f"{readme}: inventory mismatch; missing={sorted(names - listed)}, unknown={sorted(listed - names)}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = check_repo(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    count = len(list((root / "skills").glob("*/SKILL.md")))
    print(f"Validated {count} skills: frontmatter, references, routing, manifests and inventories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
