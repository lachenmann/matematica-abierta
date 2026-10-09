#!/usr/bin/env python3
"""MA-FIG-PIPE: fail-closed scope and manifest preflight. Never builds images."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import posixpath
from collections import Counter
from urllib.parse import unquote, urlsplit
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SCOPE = "data/ma-fig-scope-v1.json"
MANIFESTS = "data/ma-fig-manifests"
FIGURE_MARKUP = re.compile(
    r"!\[[^\]\n]*\]\([^)]+\)|"
    r"<\s*(?:img|picture|svg|object|canvas|iframe)\b|"
    r"\{\s*#fig-[^}]+\}|"
    r"\{\{<\s*(?:figure|video|embed)\b", re.I)
HEX = re.compile(r"[0-9a-f]{64}\Z")
ID = re.compile(r"[A-Za-z][A-Za-z0-9_-]{3,119}\Z")
CLASSES = {"FORMAL_TREATISE", "PEDAGOGICAL_BOOK", "SITE_EDUCATIONAL", "AUDIOVISUAL_INTERACTIVE"}
STATES = {"DRAFT", "REFERENCE_ONLY", "READY_FOR_PUBLICATION", "PUBLISHED"}
QA_FIELDS = ("math", "visual", "technical", "accessibility", "rights", "integration")
OUTPUT_EXTENSIONS = {"web_svg": ".svg", "print_pdf": ".pdf", "preview_png": ".png"}
SVG_FORBIDDEN = {"script", "foreignObject", "iframe", "animate", "animateMotion", "animateTransform", "set", "audio", "video"}
URL_RE = re.compile(r"url\(\s*(?!#|['\"]#)", re.I)
IMPORT_RE = re.compile(r"@import\b", re.I)


def load_scope(root: Path) -> dict:
    registry = json.loads((root / SCOPE).read_text(encoding="utf-8"))
    if registry.get("schema_version") != 1:
        raise ValueError("scope schema_version must be 1")
    for field in ("formal_treatise_prefixes", "formal_treatise_exact", "non_treatise_landing_exceptions"):
        if not isinstance(registry.get(field), list) or not all(isinstance(x, str) for x in registry[field]):
            raise ValueError(f"invalid scope field {field}")
    return registry


def is_formal_treatise(path: str, scope: dict) -> bool:
    p = path.replace("\\", "/").removeprefix("./")
    if p in scope["non_treatise_landing_exceptions"]:
        return False
    if p in scope["formal_treatise_exact"]:
        return True
    if any(p.startswith(prefix) for prefix in scope["formal_treatise_prefixes"]):
        return True
    return (p.startswith("libros/otros/tratado-")
            and PurePosixPath(p).suffix in {".md", ".qmd"})


def checked_path(root: Path, value: str, label: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"{label}: missing or invalid relative path")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in {".", ".."} for part in pure.parts):
        raise ValueError(f"{label}: unsafe path")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"{label}: path escapes repository")
    return path


def validate_svg(raw: bytes, label: str) -> list[str]:
    problems = []
    try:
        data = raw.decode("utf-8")
    except UnicodeDecodeError:
        return [f"{label}: SVG is not UTF-8"]
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)\b", data, re.I):
        problems.append(f"{label}: DTD/entities forbidden")
    try:
        tree = ET.fromstring(raw)
    except ET.ParseError:
        return problems + [f"{label}: invalid SVG XML"]
    if tree.tag.rsplit("}", 1)[-1] != "svg":
        problems.append(f"{label}: not an SVG document")
    if not any(key in tree.attrib for key in ("viewBox", "width")):
        problems.append(f"{label}: missing dimensions/viewBox")
    for node in tree.iter():
        name = node.tag.rsplit("}", 1)[-1]
        if name in SVG_FORBIDDEN:
            problems.append(f"{label}: forbidden SVG element {name}")
        if name == "style" and (IMPORT_RE.search(node.text or "") or URL_RE.search(node.text or "")):
            problems.append(f"{label}: external CSS forbidden")
        for key, value in node.attrib.items():
            local = key.rsplit("}", 1)[-1]
            if local.lower().startswith("on"):
                problems.append(f"{label}: event handler forbidden")
            if local.lower() in {"href", "src"} and value and not value.startswith("#"):
                problems.append(f"{label}: external/embedded resource forbidden")
            if local == "style" and (URL_RE.search(value) or IMPORT_RE.search(value)):
                problems.append(f"{label}: external CSS forbidden")
    return sorted(set(problems))


def validate_manifest(doc: dict, root: Path, scope: dict, label: str) -> list[str]:
    errors = []
    def reject(message: str) -> None:
        errors.append(f"{label}: {message}")

    if not isinstance(doc, dict):
        return [f"{label}: must be JSON object"]
    if doc.get("schema_version") != 1:
        reject("schema_version must be 1")
    fid = doc.get("figure_id")
    if not isinstance(fid, str) or not ID.fullmatch(fid):
        reject("invalid figure_id")
    status = doc.get("status")
    if status not in STATES:
        reject("invalid status")
    kind = doc.get("document_class")
    if kind not in CLASSES:
        reject("invalid document_class")
    if kind in {"FORMAL_TREATISE", "AUDIOVISUAL_INTERACTIVE"}:
        reject("document_class cannot use the static illustration pipeline")
    consumer = doc.get("consumer_source")
    try:
        consumer_path = checked_path(root, consumer, "consumer_source")
        if consumer_path.suffix not in {".md", ".qmd"}:
            reject("consumer_source must be Markdown/Quarto")
        if is_formal_treatise(consumer, scope):
            reject("C0-SCOPE: formal treatise illustrations forbidden")
        if kind == "PEDAGOGICAL_BOOK" and not consumer.startswith("libros/"):
            reject("PEDAGOGICAL_BOOK consumer must be under libros/")
        if kind == "SITE_EDUCATIONAL" and consumer.startswith("libros/"):
            reject("site class cannot conceal a book consumer")
        if not consumer_path.is_file():
            reject("consumer_source does not exist")
    except (ValueError, TypeError) as exc:
        reject(str(exc))

    # Cataloguing a prior reference is not publication approval or a build instruction.
    if status not in {"READY_FOR_PUBLICATION", "PUBLISHED"}:
        return errors
    if doc.get("author_generation_authorization") != "GRANTED_WITH_EVIDENCE":
        reject("C2-AUTH: explicit generation authorization absent")
    if not isinstance(doc.get("authorization_evidence"), str) or not doc.get("authorization_evidence", "").strip():
        reject("C2-AUTH: authorization evidence absent")
    if doc.get("rights") != "CLEARED":
        reject("QA-RIGHTS: rights not cleared")
    if not isinstance(doc.get("caption"), str) or len(doc["caption"].strip()) < 20:
        reject("QA-A11Y: substantial caption required")
    if not isinstance(doc.get("alt"), str) or len(doc["alt"].strip()) < 30:
        reject("QA-A11Y: descriptive alt required")
    qa = doc.get("qa")
    if not isinstance(qa, dict) or any(qa.get(field) != "PASS" for field in QA_FIELDS):
        reject("QA: all six gates must be PASS")
    if not isinstance(doc.get("source_canonical"), str) or not doc.get("source_canonical"):
        reject("C3-SOURCE: canonical Obsidian source reference required")
    if not isinstance(doc.get("build_toolchain_digest"), str) or not doc.get("build_toolchain_digest"):
        reject("C3-SOURCE: pinned toolchain digest required")
    if not isinstance(doc.get("build_command"), str) or not doc.get("build_command"):
        reject("C3-SOURCE: documented build command required")
    source, sha = doc.get("source_repository"), doc.get("source_sha256")
    if not isinstance(sha, str) or not HEX.fullmatch(sha):
        reject("C3-SOURCE: invalid source SHA-256")
    try:
        src = checked_path(root, source, "source_repository")
        if not src.is_file():
            reject("C3-SOURCE: source missing")
        elif isinstance(sha, str) and HEX.fullmatch(sha):
            if hashlib.sha256(src.read_bytes()).hexdigest() != sha:
                reject("C3-SOURCE: source SHA-256 mismatch")
    except (ValueError, TypeError) as exc:
        reject(str(exc))
    outputs, hashes = doc.get("outputs"), doc.get("output_sha256")
    if not isinstance(outputs, dict) or not outputs:
        reject("QA-TECH: at least one output required")
        outputs = {}
    if not isinstance(hashes, dict):
        reject("QA-TECH: output_sha256 object required")
        hashes = {}
    for key, name in outputs.items():
        if key not in OUTPUT_EXTENSIONS:
            reject(f"QA-TECH: unknown output kind {key}")
            continue
        try:
            target = checked_path(root, name, key)
            if target.suffix != OUTPUT_EXTENSIONS[key]:
                reject(f"QA-TECH: {key} wrong extension")
            if not target.is_file():
                reject(f"QA-TECH: missing {key}")
                continue
            data = target.read_bytes()
            digest = hashes.get(key)
            if not isinstance(digest, str) or not HEX.fullmatch(digest):
                reject(f"QA-TECH: {key} SHA-256 missing/invalid")
            elif hashlib.sha256(data).hexdigest() != digest:
                reject(f"QA-TECH: {key} SHA-256 mismatch")
            if key == "web_svg":
                errors.extend(validate_svg(data, f"{label}: {key}"))
            if key == "print_pdf" and not data.startswith(b"%PDF-"):
                reject("QA-TECH: invalid PDF header")
            if key == "preview_png" and not data.startswith(b"\x89PNG\r\n\x1a\n"):
                reject("QA-TECH: invalid PNG signature")
        except (ValueError, TypeError) as exc:
            reject(str(exc))
    return errors


def diff_formal_additions(root: Path, base: str, scope: dict) -> list[str]:
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        return ["C0-SCOPE: --base requires a 40-character commit SHA"]
    names = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", base, "HEAD", "--"],
        cwd=root, capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    errors = []
    for filename in names:
        if not is_formal_treatise(filename, scope) or PurePosixPath(filename).suffix not in {".md", ".qmd"}:
            continue
        delta = subprocess.run(
            ["git", "diff", "--unified=0", "--no-ext-diff", base, "HEAD", "--", filename],
            cwd=root, capture_output=True, text=True, check=True,
        ).stdout
        for line in delta.splitlines():
            if line.startswith("+") and not line.startswith("+++"):
                if FIGURE_MARKUP.search(line[1:]):
                    errors.append(f"C0-SCOPE: new figure markup in formal treatise {filename}")
                    break
    return errors



# C8: require an approved manifest for every NEW local static image reference.
# Preserve legacy references in educational Markdown/Quarto.
MD_IMAGE_RE = re.compile(r'!\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))', re.I)
MD_REFERENCE_IMAGE_RE = re.compile(r'!\[[^\]\n]*\]\[[^\]\n]*\]', re.I)
HTML_IMAGE_RE = re.compile(
    r'<img\b[^>]*?\bsrc\s*=\s*(?:"([^"]+)"|\'([^\']+)\'|([^\s>]+))',
    re.I | re.S,
)
EDUCATIONAL_PREFIXES = (
    "libros/", "conceptos/", "teoria/", "cursos/", "problemas/",
    "blog/", "explorar/",
)


def educational_source(path: str, scope: dict) -> bool:
    return (path.endswith((".qmd", ".md"))
            and path.startswith(EDUCATIONAL_PREFIXES)
            and not is_formal_treatise(path, scope))


def strip_nonrendered(text: str) -> str:
    """Exclude Markdown code fences and HTML comments from static image checks."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    result = []
    active = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s*(\x60{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if active is None:
                active = marker
            elif marker[0] == active[0] and len(marker) >= len(active):
                active = None
            result.append("\n")
        elif active is None:
            result.append(line)
        else:
            result.append("\n")
    return "".join(result)


def image_references(text: str) -> list[str]:
    """Extract local/remote static image targets without opening any images."""
    body = strip_nonrendered(text)
    refs = [next(part for part in m.groups() if part is not None)
            for m in MD_IMAGE_RE.finditer(body)]
    refs.extend(next(part for part in m.groups() if part is not None)
                for m in HTML_IMAGE_RE.finditer(body))
    refs.extend("__UNRESOLVED_REFERENCE_STYLE_IMAGE__"
                for _ in MD_REFERENCE_IMAGE_RE.finditer(body))
    return refs


def normalize_illustration_ref(ref: str, consumer: str) -> str:
    """Canonical repository target; refuse external/ambiguous image URLs."""
    if ref == "__UNRESOLVED_REFERENCE_STYLE_IMAGE__":
        raise ValueError("reference-style image requires explicit parser support")
    raw = ref.strip()
    if not raw or raw.startswith("//") or "\\" in raw:
        raise ValueError("unsupported or external image URL")
    url = urlsplit(raw)
    if url.scheme or url.netloc or not url.path:
        raise ValueError("external or empty image URL")
    path = unquote(url.path)
    if "\x00" in path or "\\" in path:
        raise ValueError("invalid image path")
    if path.startswith("/"):
        output = posixpath.normpath(path.lstrip("/"))
    else:
        output = posixpath.normpath(posixpath.join(posixpath.dirname(consumer), path))
    if output in {"", ".", ".."} or output.startswith("../"):
        raise ValueError("image reference escapes repository")
    return output


def new_educational_image_references(root: Path, base: str, scope: dict,
                                     manifests: list[dict]) -> list[str]:
    """Require manifests for added teaching figures, grandfathering old references."""
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        return ["C8-MANIFEST: --base requires a 40-character commit SHA"]
    changed = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", "--no-renames",
         base, "HEAD", "--"],
        cwd=root, capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    issues: list[str] = []
    for consumer in changed:
        if not educational_source(consumer, scope):
            continue
        current_file = root / consumer
        if not current_file.is_file():
            continue
        previous = subprocess.run(
            ["git", "show", f"{base}:{consumer}"],
            cwd=root, capture_output=True, text=True,
        )
        old_text = previous.stdout if previous.returncode == 0 else ""
        after_text = current_file.read_text(encoding="utf-8-sig")

        def refs(content: str) -> Counter:
            result = Counter()
            for raw in image_references(content):
                try:
                    result[normalize_illustration_ref(raw, consumer)] += 1
                except ValueError as exc:
                    result[f"INVALID:{raw}:{exc}"] += 1
            return result

        extra = refs(after_text) - refs(old_text)
        for asset, count in extra.items():
            if asset.startswith("INVALID:"):
                issues.append(f"C8-MANIFEST: {consumer}: {asset[8:]}")
                continue
            matches = [
                m for m in manifests
                if m.get("consumer_source") == consumer
                and asset in (m.get("outputs") or {}).values()
                and m.get("document_class") ==
                ("PEDAGOGICAL_BOOK" if consumer.startswith("libros/")
                 else "SITE_EDUCATIONAL")
                and m.get("status") in {"READY_FOR_PUBLICATION", "PUBLISHED"}
            ]
            if len(matches) != 1:
                issues.append(
                    f"C8-MANIFEST: {consumer}: new illustration {asset}"
                    f" ({count} new reference(s)) requires exactly one"
                    " publication-ready manifest with matching output and consumer"
                )
    return issues


def check(root: Path, base: str | None = None) -> list[str]:
    scope = load_scope(root)
    errors = []
    manifests = root / MANIFESTS
    entries = sorted(manifests.glob("*.json")) if manifests.exists() else []
    used = set()
    for entry in entries:
        try:
            doc = json.loads(entry.read_text(encoding="utf-8"))
            fid = doc.get("figure_id") if isinstance(doc, dict) else None
            if fid in used:
                errors.append(f"{entry.name}: duplicate figure_id {fid}")
            elif fid is not None:
                used.add(fid)
            errors.extend(validate_manifest(doc, root, scope, entry.name))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"{entry.name}: invalid JSON: {exc}")
    if base:
        errors.extend(diff_formal_additions(root, base, scope))
        manifests_for_refs = []
        for entry in entries:
            try:
                data = json.loads(entry.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    manifests_for_refs.append(data)
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass
        errors.extend(new_educational_image_references(root, base, scope,
                                                       manifests_for_refs))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="PR base commit; inspect newly added formal-treatise markup")
    args = parser.parse_args()
    try:
        errors = check(ROOT, args.base)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"MA-FIG-PIPE: FAIL — {exc}", file=sys.stderr)
        return 1
    if errors:
        for issue in errors:
            print(issue, file=sys.stderr)
        print(f"MA-FIG-PIPE: FAIL — {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print("MA-FIG-PIPE: PASS — no image generation performed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
