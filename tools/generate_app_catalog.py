#!/usr/bin/env python3
"""Generate the public Matemática Abierta mobile catalog.

The generator uses only the Python standard library and reads the controlled
subset of YAML front matter defined by Matemática Abierta's editorial schema.

Export policy is fail-closed:
- only documents with content-id, content-type and status: published are exported;
- draft: true is always excluded;
- non-canonical content types are rejected;
- duplicate IDs and duplicate rendered paths are rejected;
- ID prefixes must agree with content-type.

No private repository or private route is consulted by this script.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SITE_BASE_URL = "https://matematicaabierta.cl"
SCHEMA_VERSION = 1

CANONICAL_TYPES = {
    "concept",
    "problem",
    "article",
    "lesson",
    "book-chapter",
    "course",
    "book",
}

TYPE_ID_PREFIX = {
    "concept": "MA-CON-",
    "problem": "MA-PRB-",
    "article": "MA-ART-",
    "lesson": "MA-LES-",
    "book-chapter": "MA-BCH-",
    "course": "MA-CRS-",
    "book": "MA-BOK-",
}

SCALAR_FIELDS = {
    "content-id": "id",
    "content-type": "type",
    "title": "title",
    "description": "description",
    "author": "author",
    "collection": "collection",
    "status": "status",
    "date-modified": "dateModified",
    "level": "level",
    "difficulty": "difficulty",
    "license": "license",
    "parent-id": "parentId",
    "book-id": "parentId",
}

LIST_FIELDS = {
    "areas": "areas",
    "topics": "topics",
    "prerequisites": "prerequisites",
    "related": "related",
}

IGNORED_DIRS = {
    ".git",
    ".quarto",
    "_freeze",
    "_site",
    "node_modules",
}

FRONT_MATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.S)


def _parse_scalar(raw: str) -> Any:
    raw = raw.strip()
    if raw == "":
        return ""
    if raw == "[]":
        return []
    if raw.lower() == "true":
        return True
    if raw.lower() == "false":
        return False
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    if (raw.startswith('"') and raw.endswith('"')) or (
        raw.startswith("'") and raw.endswith("'")
    ):
        return raw[1:-1]
    return raw


def parse_front_matter(text: str) -> dict[str, Any]:
    """Parse only the catalog-relevant subset of front matter."""
    match = FRONT_MATTER_RE.search(text)
    if not match:
        return {}

    lines = match.group(1).splitlines()
    data: dict[str, Any] = {}
    i = 0

    while i < len(lines):
        line = lines[i]
        if not line or line.lstrip().startswith("#") or line[:1].isspace():
            i += 1
            continue

        if ":" not in line:
            i += 1
            continue

        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()

        if key in LIST_FIELDS:
            if raw_value:
                value = _parse_scalar(raw_value)
                if isinstance(value, list):
                    data[key] = value
                elif isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                    inner = value[1:-1].strip()
                    data[key] = [] if not inner else [
                        _parse_scalar(part.strip()) for part in inner.split(",")
                    ]
                else:
                    data[key] = [value]
                i += 1
                continue

            values: list[Any] = []
            i += 1
            while i < len(lines):
                candidate = lines[i]
                stripped = candidate.strip()
                if not candidate[:1].isspace():
                    break
                if stripped.startswith("- "):
                    values.append(_parse_scalar(stripped[2:].strip()))
                i += 1
            data[key] = values
            continue

        if key in SCALAR_FIELDS or key == "draft":
            data[key] = _parse_scalar(raw_value)

        i += 1

    return data


def source_to_public_path(relative_path: Path) -> str:
    """Convert a source Markdown/Quarto path to its rendered public HTML path."""
    return "/" + relative_path.with_suffix(".html").as_posix()


def iter_source_documents(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".qmd"}:
            continue
        relative = path.relative_to(root)
        if any(part in IGNORED_DIRS for part in relative.parts):
            continue
        yield path, relative


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_catalog(root: Path, *, generated_at: str | None = None) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    seen_ids: dict[str, str] = {}
    seen_paths: dict[str, str] = {}
    errors: list[str] = []

    for path, relative in iter_source_documents(root):
        metadata = parse_front_matter(path.read_text(encoding="utf-8-sig"))

        content_id = metadata.get("content-id")
        content_type = metadata.get("content-type")
        status = metadata.get("status")

        if not content_id or not content_type or status != "published":
            continue
        if metadata.get("draft") is True:
            continue

        relative_str = relative.as_posix()

        if not metadata.get("title"):
            errors.append(f"{relative_str}: published content has no title")
            continue

        if content_type not in CANONICAL_TYPES:
            errors.append(
                f"{relative_str}: non-canonical content-type {content_type!r}"
            )
            continue

        expected_prefix = TYPE_ID_PREFIX[str(content_type)]
        if not str(content_id).startswith(expected_prefix):
            errors.append(
                f"{relative_str}: content-id {content_id!r} does not match "
                f"content-type {content_type!r} (expected prefix {expected_prefix})"
            )

        public_path = source_to_public_path(relative)

        if content_id in seen_ids:
            errors.append(
                f"duplicate content-id {content_id}: "
                f"{seen_ids[str(content_id)]} and {relative_str}"
            )
        else:
            seen_ids[str(content_id)] = relative_str

        if public_path in seen_paths:
            errors.append(
                f"duplicate public path {public_path}: "
                f"{seen_paths[public_path]} and {relative_str}"
            )
        else:
            seen_paths[public_path] = relative_str

        item: dict[str, Any] = {
            "id": str(content_id),
            "type": str(content_type),
            "title": str(metadata["title"]),
            "path": public_path,
            "status": "published",
        }

        for source_key, output_key in SCALAR_FIELDS.items():
            if source_key in {"content-id", "content-type", "title", "status"}:
                continue
            value = metadata.get(source_key)
            if value not in (None, "", []):
                item[output_key] = value

        for source_key, output_key in LIST_FIELDS.items():
            value = metadata.get(source_key)
            if value:
                item[output_key] = value

        items.append(item)

    if errors:
        formatted = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"catalog validation failed:\n{formatted}")

    items.sort(key=lambda item: item["id"])

    return {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": generated_at or _utc_now_iso(),
        "siteBaseUrl": SITE_BASE_URL,
        "items": items,
    }


def write_catalog(root: Path, output: Path) -> dict[str, Any]:
    catalog = build_catalog(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return catalog


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="output path (defaults to <root>/app/catalog-v1.json)",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    output = (args.output or (root / "app" / "catalog-v1.json")).resolve()
    catalog = write_catalog(root, output)
    print(f"catalog-v1: {len(catalog['items'])} published items -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
