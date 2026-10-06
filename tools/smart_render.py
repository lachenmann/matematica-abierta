#!/usr/bin/env python3
"""Conservative Quarto incremental builds from verified, published state."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET

SCHEMA = 1
STATE = ".ma-build"
MAX_TARGETS = 30
FRONT = re.compile(r"\A---\s*\n.*?\n---(?:\s*\n|\Z)", re.S)
INCLUDE = re.compile(r'\{\{<\s*include\s+(?:"([^"]+)"|\x27([^\x27]+)\x27|([^\s>]+))\s*>\}\}')
# Preserve structure, cross-reference labels/citations, resource/link destinations
# and executable code. Prose and math expressions may change.
TOKENS = re.compile(r"(?m)^\s*#{1,6}\s+.*$|^\s*:::.*$|\{#[^}]+\}|(?<![\w])@[\w:.-]+|!?\[[^\]\n]*\]\([^\n)]*\)|^\s*\[[^\]]+\]:.*$|<[^>]+>|\{\{.*?\}\}")
CODE = re.compile(r"(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1\s*$")


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    return {p.relative_to(root).as_posix(): sha(p)
            for p in sorted(root.rglob("*")) if p.is_file()}


def version(root):
    return subprocess.check_output(["quarto", "--version"], cwd=root, text=True).strip()


def json_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def safe_edit(before, after):
    """Only body edits with unchanged structural tokens qualify."""
    old_front = FRONT.match(before)
    new_front = FRONT.match(after)
    if (old_front.group() if old_front else "") != (new_front.group() if new_front else ""):
        return False
    old_body = before[old_front.end():] if old_front else before
    new_body = after[new_front.end():] if new_front else after
    return (TOKENS.findall(old_body) == TOKENS.findall(new_body)
            and CODE.findall(old_body) == CODE.findall(new_body)
            and [m.group() for m in CODE.finditer(old_body)] == [m.group() for m in CODE.finditer(new_body)])


def documents(root):
    names = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).split(b"\0")
    return [n.decode() for n in names if n and Path(n.decode()).suffix in {".md", ".qmd"}]


def dependencies(root):
    consumers = {}
    listings = set()
    for name in documents(root):
        text = (root / name).read_text(encoding="utf-8-sig")
        front = FRONT.match(text)
        if front and re.search(r"(?m)^\s*listing\s*:", front.group()):
            listings.add(name)
        matches = list(INCLUDE.finditer(text))
        if len(re.findall(r"\{\{<\s*include\b", text)) != len(matches):
            raise ValueError("unrecognized include directive")
        for match in matches:
            value = next(v for v in match.groups() if v is not None)
            if value.startswith("/"):
                target = posixpath.normpath(value.lstrip("/"))
            else:
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name), value))
            if target.startswith("../") or target == "..":
                raise ValueError("include outside repository")
            consumers.setdefault(target, set()).add(name)
    return consumers, listings


def verify_base(root, quarto, books):
    base = json.loads((root / STATE / "base.json").read_text())
    if base.get("schema") != SCHEMA or base.get("quarto") != quarto:
        raise ValueError("base format or Quarto version changed")
    if base.get("offline_books") != books:
        raise ValueError("offline policy changed")
    if not re.fullmatch(r"[a-f0-9]{40}", base.get("commit", "")):
        raise ValueError("invalid base commit")
    if subprocess.run(["git", "merge-base", "--is-ancestor", base["commit"], "HEAD"], cwd=root).returncode:
        raise ValueError("base is not an ancestor")
    if not base.get("site") or not base.get("quarto_state"):
        raise ValueError("incomplete base")
    if inventory(root / "_site") != base["site"]:
        raise ValueError("site base integrity failed")
    if inventory(root / ".quarto") != base["quarto_state"]:
        raise ValueError("Quarto state integrity failed")
    return base


def plan(root, base):
    # Compare the cached source commit, never merely HEAD's parent.
    raw = subprocess.check_output(["git", "diff", "--name-status", "--no-renames", "-z", base["commit"], "HEAD"], cwd=root).split(b"\0")
    changes = []
    for i in range(0, len(raw) - 1, 2):
        changes.append((raw[i].decode(), raw[i + 1].decode()))
    changed = [name for _, name in changes]
    for status, name in changes:
        if status != "M" or Path(name).suffix not in {".md", ".qmd"}:
            return {"mode": "full", "reason": "structural, resource or unknown change", "changed": changed, "targets": []}
        before = git(root, "show", f"{base['commit']}:{name}")
        after = (root / name).read_text(encoding="utf-8-sig").strip()
        if not safe_edit(before, after):
            return {"mode": "full", "reason": "metadata, structure, reference or code changed", "changed": changed, "targets": []}
    consumers, listings = dependencies(root)
    affected = set(changed)
    pending = list(changed)
    while pending:
        for parent in consumers.get(pending.pop(), set()):
            if parent not in affected:
                affected.add(parent)
                pending.append(parent)
    targets = {name for name in affected if Path(name).with_suffix(".html").as_posix() in base["site"]}
    if changes and not targets:
        return {"mode": "full", "reason": "changed source has no known public output", "changed": changed, "targets": []}
    # Include shared listing consumers conservatively, even if only excerpts changed.
    if changes:
        targets.update(name for name in listings if Path(name).with_suffix(".html").as_posix() in base["site"])
    for name in changed:
        reachable = {name}
        queue = [name]
        while queue:
            for parent in consumers.get(queue.pop(), set()):
                if parent not in reachable:
                    reachable.add(parent)
                    queue.append(parent)
        if not reachable.intersection(targets):
            return {"mode": "full", "reason": "unmapped changed fragment", "changed": changed, "targets": []}
    if len(targets) > MAX_TARGETS:
        return {"mode": "full", "reason": "too many affected pages", "changed": changed, "targets": []}
    return {"mode": "incremental" if changes else "reuse", "reason": "verified body-only edit" if changes else "source unchanged", "changed": changed, "targets": sorted(targets)}


def render(root, targets=None):
    commands = [["quarto", "render", target, "--no-clean"] for target in targets] if targets is not None else [["quarto", "render"]]
    for command in commands:
        print("Running:", " ".join(command), flush=True)
        subprocess.run(command, cwd=root, check=True)


def validate_site(root, targets):
    site = root / "_site"
    for name in ["index.html", "search.json", "sitemap.xml", *[str(Path(t).with_suffix(".html")) for t in targets]]:
        path = site / name
        if not path.is_file() or not path.stat().st_size:
            raise ValueError(f"missing rendered output: {name}")
    search = json.loads((site / "search.json").read_text())
    if not isinstance(search, list) or not search:
        raise ValueError("invalid or empty search index")
    ET.parse(site / "sitemap.xml")
    catalog = site / "app/catalog-v1.json"
    if catalog.exists():
        data = json.loads(catalog.read_text())
        if data.get("schemaVersion") != 1 or not data.get("items"):
            raise ValueError("invalid app catalog")


def check_preservation(root, base, targets):
    after = inventory(root / "_site")
    allowed = {"search.json", "sitemap.xml", "app/catalog-v1.json"}
    allowed.update(Path(t).with_suffix(".html").as_posix() for t in targets)
    if set(after) != set(base["site"]):
        raise ValueError("incremental file inventory changed unexpectedly")
    unexpected = [name for name in after if name not in allowed and after[name] != base["site"][name]]
    if unexpected:
        raise ValueError("unexpected changes outside affected pages: " + ", ".join(unexpected[:5]))


def verify_package(root, book):
    package = root / "_site/app/offline" / book
    data = json.loads((package / "manifest-v1.json").read_text())
    if data.get("schemaVersion") != 1 or data.get("bookId") != book or not data.get("contents"):
        raise ValueError("invalid offline package")
    total = 0
    for item in data["contents"]:
        path = (package / item["localPath"]).resolve()
        if not path.is_relative_to(package.resolve()):
            raise ValueError("unsafe offline resource path")
        if sha(path) != item["sha256"] or path.stat().st_size != item["size"]:
            raise ValueError("offline package integrity failed")
        total += item["size"]
    if total != data["totalSize"]:
        raise ValueError("offline size mismatch")
    return data


def offline(root, books, decision):
    results = {}
    for book in books:
        regenerate = decision["mode"] == "full"
        if not regenerate:
            try:
                manifest = verify_package(root, book)
                sources = {str(Path(item["canonicalPath"].lstrip("/")).with_suffix(suffix)) for item in manifest["contents"] for suffix in [".md", ".qmd"]}
                regenerate = bool(sources.intersection(decision["targets"]))
            except (OSError, ValueError, KeyError):
                regenerate = True
        if regenerate:
            subprocess.run(["python3", "tools/generate_offline_manifests.py", "--site-dir", "_site", "--book-id", book], cwd=root, check=True)
            verify_package(root, book)
        results[book] = "regenerated" if regenerate else "reused"
    return results


def build(root, force_full=False, books=None):
    books = books or []
    start = time.monotonic()
    quarto = version(root)
    base = None
    decision = {"mode": "full", "reason": "forced complete render", "changed": [], "targets": []}
    if not force_full:
        try:
            base = verify_base(root, quarto, books)
            decision = plan(root, base)
        except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
            decision["reason"] = "unusable base or dependency map: " + str(error)
    print(json.dumps(decision, ensure_ascii=False), flush=True)
    if decision["mode"] in {"incremental", "reuse"}:
        try:
            render(root, decision["targets"])
            catalog = root / "app/catalog-v1.json"
            if catalog.exists():
                (root / "_site/app").mkdir(exist_ok=True)
                shutil.copy2(catalog, root / "_site/app/catalog-v1.json")
            validate_site(root, decision["targets"])
            check_preservation(root, base, decision["targets"])
        except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
            decision.update(mode="full", reason="incremental fallback: " + str(error))
            print(decision["reason"], flush=True)
    if decision["mode"] == "full":
        # Remove restored output/state only, never sources. Partial failures cannot
        # leak stale/deleted resources into the complete fallback.
        shutil.rmtree(root / "_site", ignore_errors=True)
        shutil.rmtree(root / ".quarto", ignore_errors=True)
        render(root)
        validate_site(root, decision["targets"])
    packages = offline(root, books, decision)
    report = {**decision, "schema": SCHEMA, "commit": git(root, "rev-parse", "HEAD"), "base_commit": base["commit"] if base else None,
              "quarto": quarto, "seconds": round(time.monotonic() - start, 3), "offline_books": books, "offline": packages,
              "files": len(inventory(root / "_site"))}
    json_write(root / STATE / "report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as stream:
            stream.write(f"### Render: {report['mode']}\n\n{report['reason']}\n\n{report['seconds']} s; {len(report['targets'])} selected pages.\n")
    return report


def seal(root):
    report = json.loads((root / STATE / "report.json").read_text())
    validate_site(root, report["targets"])
    for book in report["offline_books"]:
        verify_package(root, book)
    data = {"schema": SCHEMA, "commit": git(root, "rev-parse", "HEAD"), "quarto": version(root),
            "offline_books": report["offline_books"], "site": inventory(root / "_site"), "quarto_state": inventory(root / ".quarto")}
    if not data["quarto_state"]:
        raise ValueError("missing Quarto project state")
    json_write(root / STATE / "base.json", data)
    print(f"Sealed {len(data['site'])} files for {data['commit']}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "seal"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--force-full", action="store_true")
    parser.add_argument("--offline-book", action="append", default=[])
    args = parser.parse_args()
    root = args.root.resolve()
    if args.action == "seal":
        seal(root)
    else:
        build(root, args.force_full or os.environ.get("MA_FORCE_FULL", "false").lower() == "true", args.offline_book)


if __name__ == "__main__":
    main()
