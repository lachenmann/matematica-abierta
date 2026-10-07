#!/usr/bin/env python3
"""Generate offline-manifest-v1 packages from published Matemática Abierta books.

The public catalog supplies canonical identities. Each selected book chapter is
derived from the canonical _site HTML and packaged with shared local resources,
then hashed into the B1 manifest contract.

B2 policy:
- public books only;
- explicit book IDs at generation time;
- derive chapter HTML from the same canonical _site build;
- preserve canonical shell, theme and fonts;
- share CSS, fonts and the locked canonical MathJax runtime through B1 assets;
- deterministic package version derives from content and shared asset hashes;
- fail closed on missing source, unsafe output, external subresources, or
  catalog inconsistencies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from html.parser import HTMLParser
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from offline_resources import Resources, package_path
from canonical_offline import CanonicalAssets, MEDIA

SITE_BASE_URL = "https://matematicaabierta.cl"
SCHEMA_VERSION = 1
HASH_ALGORITHM = "sha256"
BOOK_ID_RE = re.compile(r"^MA-BOK-[0-9]{4,}$")
CHAPTER_ID_RE = re.compile(r"^MA-BCH-[0-9]{4,}$")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_catalog(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if (
        not isinstance(data, dict)
        or data.get("schemaVersion") != 1
        or data.get("siteBaseUrl") != SITE_BASE_URL
        or not isinstance(data.get("items"), list)
    ):
        raise ValueError("catalog-v1 inválido o incompatible")
    return data


def select_book(catalog: dict[str, Any], book_id: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if not BOOK_ID_RE.fullmatch(book_id):
        raise ValueError(f"bookId inválido: {book_id}")

    items = catalog["items"]
    books = [
        item
        for item in items
        if item.get("type") == "book" and item.get("id") == book_id
    ]
    if len(books) != 1:
        raise ValueError(f"libro {book_id} ausente o duplicado en catalog-v1")

    book = books[0]
    chapters = [
        item
        for item in items
        if item.get("type") == "book-chapter" and item.get("parentId") == book_id
    ]
    if not chapters:
        raise ValueError(f"libro {book_id} no tiene capítulos publicados")

    by_id: dict[str, dict[str, Any]] = {}
    for chapter in chapters:
        chapter_id = chapter.get("id")
        if not isinstance(chapter_id, str) or not CHAPTER_ID_RE.fullmatch(chapter_id):
            raise ValueError(f"capítulo con ID inválido en {book_id}: {chapter_id!r}")
        if not isinstance(chapter.get("path"), str) or not chapter["path"].startswith("/"):
            raise ValueError(f"capítulo {chapter_id} no tiene path canónico")
        by_id[chapter_id] = chapter

    related = book.get("related")
    if not isinstance(related, list):
        raise ValueError(
            f"libro {book_id} no declara un orden completo de capítulos en related"
        )

    ordered_ids = [
        value
        for value in related
        if isinstance(value, str) and value in by_id
    ]
    if len(ordered_ids) != len(set(ordered_ids)):
        raise ValueError(f"libro {book_id} repite capítulos en related")

    missing = sorted(set(by_id) - set(ordered_ids))
    if missing:
        raise ValueError(
            f"libro {book_id} no declara el orden de todos sus capítulos: "
            + ", ".join(missing)
        )

    return book, [by_id[chapter_id] for chapter_id in ordered_ids]


def resolve_source_path(root: Path, public_path: str) -> Path:
    relative = Path(public_path.lstrip("/"))
    if relative.suffix.lower() != ".html":
        raise ValueError(f"path público no HTML: {public_path}")

    stem = relative.with_suffix("")
    candidates = [root / stem.with_suffix(".md"), root / stem.with_suffix(".qmd")]
    existing = [candidate for candidate in candidates if candidate.is_file()]
    if len(existing) != 1:
        raise ValueError(
            f"no se pudo resolver una única fuente para {public_path}: "
            + ", ".join(str(path.relative_to(root)) for path in candidates)
        )
    return existing[0]


def validate_self_contained_html(data: bytes, *, label: str,
                                 local_path: str = "content/chapter.html",
                                 assets: dict[str, bytes] | None = None) -> None:
    if not data or b"<html" not in data.lower() or b"<body" not in data.lower():
        raise ValueError(f"{label}: HTML offline vacío o incompleto")

    text = data.decode("utf-8", errors="strict")
    Resources(local_path, assets or {}, label).html(text)


_SCRIPT_RE = re.compile(
    r"<script\b([^>]*)>([\s\S]*?)</script>",
    re.I,
)
class _OfflineStructureParser(HTMLParser):
    """Locate real document tags without matching HTML-like strings in scripts."""

    def __init__(self, text: str) -> None:
        super().__init__(convert_charrefs=False)
        self.text = text
        self._line_starts = [0]
        self._line_starts.extend(match.end() for match in re.finditer("\n", text))
        self.lang = "es"
        self.head_inner_start: int | None = None
        self.head_inner_end: int | None = None
        self.body_open_start: int | None = None
        self.body_open_end: int | None = None
        self.main_start: int | None = None
        self.main_end: int | None = None
        self.content_open: str | None = None

    def _absolute_index(self) -> int:
        line, column = self.getpos()
        return self._line_starts[line - 1] + column

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        tag = tag.lower()
        start = self._absolute_index()
        raw = self.get_starttag_text()
        if raw is None:
            return
        end = start + len(raw)
        attr_map = dict(attrs)

        if tag == "div" and attr_map.get("id") == "quarto-content":
            self.content_open = raw
        if tag == "html" and attr_map.get("lang"):
            self.lang = str(attr_map["lang"])
        elif tag == "head" and self.head_inner_start is None:
            self.head_inner_start = end
        elif tag == "body" and self.body_open_start is None:
            self.body_open_start = start
            self.body_open_end = end
        elif (
            tag == "main"
            and attr_map.get("id") == "quarto-document-content"
            and self.main_start is None
        ):
            self.main_start = start

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        start = self._absolute_index()
        close = self.text.find(">", start)
        if close < 0:
            return
        end = close + 1

        if tag == "head" and self.head_inner_start is not None:
            if self.head_inner_end is None:
                self.head_inner_end = start
        elif tag == "main" and self.main_start is not None:
            if self.main_end is None:
                self.main_end = end


def _isolate_offline_structure(
    text: str,
    *,
    label: str,
) -> tuple[str, str, str, str]:
    parser = _OfflineStructureParser(text)
    parser.feed(text)
    parser.close()

    required = (
        parser.head_inner_start,
        parser.head_inner_end,
        parser.body_open_start,
        parser.body_open_end,
        parser.main_start,
        parser.main_end,
    )
    if any(value is None for value in required):
        raise ValueError(f"{label}: no se pudo aislar head/main/body para offline")

    assert parser.head_inner_start is not None
    assert parser.head_inner_end is not None
    assert parser.body_open_start is not None
    assert parser.body_open_end is not None
    assert parser.main_start is not None
    assert parser.main_end is not None

    return (
        text[parser.head_inner_start : parser.head_inner_end],
        text[parser.body_open_start : parser.body_open_end],
        text[parser.main_start : parser.main_end],
        parser.lang,
    )


def _html_attr_value(tag: str, name: str) -> str | None:
    class Attributes(HTMLParser):
        values = None

        def handle_starttag(self, tag, attrs):
            if self.values is None:
                self.values = dict(attrs)

    parser = Attributes()
    parser.feed(tag)
    return (parser.values or {}).get(name)


def build_manifest(
    book: dict[str, Any],
    chapters: list[dict[str, Any]],
    artifacts: dict[str, bytes],
    *,
    generated_at: str,
    assets: dict[str, bytes] | None = None,
) -> dict[str, Any]:
    contents: list[dict[str, Any]] = []
    asset_bytes = assets or {}
    for local_path, data in asset_bytes.items():
        package_path(local_path)
        if not data:
            raise ValueError(f"asset offline vacío: {local_path}")
        if local_path.endswith(".css"):
            Resources(local_path, asset_bytes, local_path).css(data.decode("utf-8"))
        elif local_path.endswith(".svg"):
            Resources(local_path, asset_bytes, local_path).html(data.decode("utf-8"))

    for chapter in chapters:
        chapter_id = chapter["id"]
        data = artifacts.get(chapter_id)
        if data is None:
            raise ValueError(f"falta artefacto offline para {chapter_id}")
        validate_self_contained_html(data, label=chapter_id,
                                     local_path=f"content/{chapter_id}.html", assets=asset_bytes)

        contents.append(
            {
                "contentId": chapter_id,
                "title": chapter["title"],
                "canonicalPath": chapter["path"],
                "localPath": f"content/{chapter_id}.html",
                "mediaType": "text/html",
                "size": len(data),
                "sha256": sha256_bytes(data),
                "contentVersion": chapter.get("dateModified"),
            }
        )

    asset_entries: list[dict[str, Any]] = []
    for local_path, data in sorted(asset_bytes.items()):
        if not local_path.startswith("assets/") or Path(local_path).suffix not in MEDIA:
            raise ValueError(f"asset offline no soportado: {local_path}")
        asset_entries.append(
            {
                "remotePath": f"/app/offline/{book['id']}/{local_path}",
                "localPath": local_path,
                "mediaType": MEDIA[Path(local_path).suffix],
                "size": len(data),
                "sha256": sha256_bytes(data),
            }
        )

    version_material = {
        "bookId": book["id"],
        "title": book["title"],
        "contents": [
            {
                "contentId": item["contentId"],
                "canonicalPath": item["canonicalPath"],
                "localPath": item["localPath"],
                "sha256": item["sha256"],
                "contentVersion": item["contentVersion"],
            }
            for item in contents
        ],
        "assets": [
            {
                "remotePath": item["remotePath"],
                "localPath": item["localPath"],
                "sha256": item["sha256"],
            }
            for item in asset_entries
        ],
    }
    version_digest = hashlib.sha256(
        json.dumps(
            version_material,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()

    return {
        "schemaVersion": SCHEMA_VERSION,
        "siteBaseUrl": SITE_BASE_URL,
        "hashAlgorithm": HASH_ALGORITHM,
        "bookId": book["id"],
        "title": book["title"],
        "version": f"sha256-{version_digest[:24]}",
        "generatedAt": generated_at,
        "entryContentId": contents[0]["contentId"],
        "totalSize": (
            sum(item["size"] for item in contents)
            + sum(item["size"] for item in asset_entries)
        ),
        "contents": contents,
        "assets": asset_entries,
    }


def write_book_package(
    root: Path,
    site_dir: Path,
    catalog: dict[str, Any],
    book_id: str,
    *,
    quarto: str = "quarto",
) -> Path:
    book, chapters = select_book(catalog, book_id)
    package_dir = site_dir / "app" / "offline" / book_id
    content_dir = package_dir / "content"

    shutil.rmtree(package_dir, ignore_errors=True)
    content_dir.mkdir(parents=True, exist_ok=True)

    artifacts: dict[str, bytes] = {}
    canonical = CanonicalAssets(site_dir)
    canonical.mathjax()
    for chapter in chapters:
        data = canonical.chapter(chapter["path"], chapter["id"])
        artifacts[chapter["id"]] = data
        (content_dir / f"{chapter['id']}.html").write_bytes(data)
        print(f"offline-canonical: {chapter['id']}: {len(data)} bytes")
    shared_assets = canonical.assets

    for local_path, asset_data in shared_assets.items():
        asset_path = package_dir / local_path
        asset_path.parent.mkdir(parents=True, exist_ok=True)
        asset_path.write_bytes(asset_data)

    generated_at = catalog.get("generatedAt")
    if not isinstance(generated_at, str) or not generated_at:
        generated_at = utc_now_iso()

    manifest = build_manifest(
        book,
        chapters,
        artifacts,
        generated_at=generated_at,
        assets=shared_assets,
    )
    manifest_path = package_dir / "manifest-v1.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root",
    )
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=Path("_site"),
        help="rendered Quarto site directory",
    )
    parser.add_argument(
        "--book-id",
        action="append",
        required=True,
        help="public MA-BOK ID to package; repeat for more books",
    )
    parser.add_argument(
        "--quarto",
        default="quarto",
        help="Quarto executable",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    site_dir = args.site_dir
    if not site_dir.is_absolute():
        site_dir = (root / site_dir).resolve()

    catalog_path = site_dir / "app" / "catalog-v1.json"
    if not catalog_path.is_file():
        raise SystemExit(f"catalog-v1 no existe en {catalog_path}")

    catalog = load_catalog(catalog_path)

    for book_id in args.book_id:
        manifest_path = write_book_package(
            root,
            site_dir,
            catalog,
            book_id,
            quarto=args.quarto,
        )
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        print(
            f"offline-manifest-v1: {book_id} -> "
            f"{len(manifest['contents'])} capítulos, "
            f"{manifest['totalSize']} bytes, {manifest_path}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
