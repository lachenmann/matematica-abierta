#!/usr/bin/env python3
"""Generate offline-manifest-v1 packages from published Matemática Abierta books.

The public catalog supplies canonical identities. Each selected book chapter is
rendered again as standalone HTML with Quarto's embedded resources and embedded
math runtime, then hashed into the B1 manifest contract.

B2 policy:
- public books only;
- explicit book IDs at generation time;
- chapter-level self-contained HTML;
- offline render uses Quarto minimal HTML but restores the canonical reader shell;
- embedded theme fonts are preserved for online/offline visual parity;
- math remains self-contained;
- heavy embedded theme styles/fonts are shared once per book through B1 assets;
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
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SITE_BASE_URL = "https://matematicaabierta.cl"
SCHEMA_VERSION = 1
HASH_ALGORITHM = "sha256"
BOOK_ID_RE = re.compile(r"^MA-BOK-[0-9]{4,}$")
CHAPTER_ID_RE = re.compile(r"^MA-BCH-[0-9]{4,}$")

EXTERNAL_SUBRESOURCE_PATTERNS = [
    re.compile(
        r"<(?:script|img|iframe|source|video|audio)\b[^>]*\b(?:src|poster)\s*=\s*[\"']\s*(?:https?:)?//",
        re.I,
    ),
    re.compile(
        r"<link\b[^>]*\b(?:rel\s*=\s*[\"'][^\"']*(?:stylesheet|preload|icon)[^\"']*[\"'][^>]*\bhref|href\s*=\s*[\"']\s*(?:https?:)?//)",
        re.I,
    ),
    re.compile(r"\bsrcset\s*=\s*[\"'][^\"']*(?:https?:)?//", re.I),
    re.compile(r"@import\s+(?:url\()?\s*[\"']?(?:https?:)?//", re.I),
    re.compile(r"url\(\s*[\"']?(?:https?:)?//", re.I),
]


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


def validate_self_contained_html(data: bytes, *, label: str) -> None:
    if not data or b"<html" not in data.lower() or b"<body" not in data.lower():
        raise ValueError(f"{label}: HTML offline vacío o incompleto")

    text = data.decode("utf-8", errors="strict")
    for pattern in EXTERNAL_SUBRESOURCE_PATTERNS:
        if pattern.search(text):
            raise ValueError(f"{label}: conserva un subrecurso externo")


_OFFLINE_STRIP_SCRIPT_SIGNATURES = (
    'headroomChanged = new CustomEvent("quarto-hrChanged"',
    "headroom.js v0.12.0",
    "clipboard.js v2.0.11",
    "@algolia/autocomplete-js",
    "Fuse.js v6.6.2",
    'const kQueryArg = "q";',
    "@popperjs/core v2.11.7",
    ").tippy=t(",
    "AnchorJS - v5.0.0",
    "Bootstrap v5.3.1",
)

_OFFLINE_STRIP_SCRIPT_IDS = {
    "quarto-search-options",
}

_OFFLINE_READER_LAYOUT_CSS = r"""
#quarto-content.page-columns {
  display: block !important;
  grid-template-columns: minmax(0, 1fr) !important;
}

#quarto-content {
  box-sizing: border-box !important;
  max-width: 100% !important;
  padding-left: max(1rem, env(safe-area-inset-left)) !important;
  padding-right: max(1rem, env(safe-area-inset-right)) !important;
}

#quarto-content > main.content,
#quarto-content .content {
  box-sizing: border-box !important;
  grid-column: 1 / -1 !important;
  max-width: 100% !important;
  min-width: 0 !important;
  width: 100% !important;
}

#quarto-content img,
#quarto-content figure img {
  height: auto !important;
  max-width: 100% !important;
}

#quarto-content table,
#quarto-content pre {
  max-width: 100% !important;
  overflow-x: auto !important;
  overflow-y: hidden;
}

#quarto-content .math.display {
  max-width: 100% !important;
  overflow: visible !important;
}

#quarto-content .math.display > mjx-container[display="true"] {
  box-sizing: border-box !important;
  max-width: 100% !important;
  overflow-x: auto !important;
  overflow-y: hidden !important;
  padding-top: 0.55em !important;
  padding-bottom: 0.65em !important;
}

#quarto-content .callout,
#quarto-content .theorem,
#quarto-content .proof {
  max-width: 100% !important;
}
"""

_DATA_CSS_LINK_RE = re.compile(
    r'<link\b[^>]*href="(data:text/css,[^"]+)"[^>]*>',
    re.I,
)
_SCRIPT_RE = re.compile(
    r"<script\b([^>]*)>([\s\S]*?)</script>",
    re.I,
)
_STYLE_RE = re.compile(
    r"<style\b[^>]*>([\s\S]*?)</style>",
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


_FONT_FACE_RE = re.compile(
    r"@font-face\s*\{[^{}]*font-family:\s*['\"](?:Source Sans Pro|Lato)['\"][^{}]*\}",
    re.I | re.S,
)


def _script_id(attrs: str) -> str | None:
    match = re.search(r'\bid=["\']([^"\']+)["\']', attrs, re.I)
    return match.group(1) if match else None


def _strip_offline_scripts(head: str) -> str:
    def replace(match: re.Match[str]) -> str:
        attrs = match.group(1)
        body = match.group(2)
        if _script_id(attrs) in _OFFLINE_STRIP_SCRIPT_IDS:
            return ""
        if any(signature in body for signature in _OFFLINE_STRIP_SCRIPT_SIGNATURES):
            return ""
        return match.group(0)

    return _SCRIPT_RE.sub(replace, head)


def _strip_embedded_webfonts(head: str) -> str:
    from urllib.parse import quote, unquote

    def replace_link(match: re.Match[str]) -> str:
        tag = match.group(0)
        href = match.group(1)
        encoded_css = href[len("data:text/css,") :]
        try:
            css = unquote(encoded_css)
        except Exception:
            return tag

        if "Source Sans Pro" not in css and "Lato" not in css:
            return tag

        stripped = _FONT_FACE_RE.sub("", css)
        if stripped == css:
            return tag

        replacement_href = "data:text/css," + quote(
            stripped,
            safe="!$&'()*+,/:;=?@-._~",
        )
        return tag.replace(href, replacement_href, 1)

    return _DATA_CSS_LINK_RE.sub(replace_link, head)


def _html_attr_value(tag: str, name: str) -> str | None:
    match = re.search(
        rf'\\b{re.escape(name)}=["\\\']([^"\\\']+)["\\\']',
        tag,
        re.I,
    )
    return match.group(1) if match else None


def extract_shared_theme_styles(
    data: bytes,
    *,
    label: str,
) -> tuple[bytes, dict[str, bytes]]:
    """Move Quarto's embedded light/dark theme CSS to shared book assets."""

    from urllib.parse import unquote

    text = data.decode("utf-8", errors="strict")
    assets: dict[str, bytes] = {}

    def replace_link(match: re.Match[str]) -> str:
        tag = match.group(0)
        href = match.group(1)
        if _html_attr_value(tag, "id") != "quarto-bootstrap":
            return tag

        mode = _html_attr_value(tag, "data-mode")
        if mode not in {"light", "dark"}:
            raise ValueError(f"{label}: tema Bootstrap offline sin data-mode válido")

        css = unquote(href[len("data:text/css,") :])
        for pattern in EXTERNAL_SUBRESOURCE_PATTERNS[-2:]:
            if pattern.search(css):
                raise ValueError(
                    f"{label}: CSS compartido conserva un subrecurso externo"
                )

        local_path = f"assets/quarto-bootstrap-{mode}.css"
        css_bytes = css.encode("utf-8")
        previous = assets.get(local_path)
        if previous is not None and previous != css_bytes:
            raise ValueError(f"{label}: tema Bootstrap {mode} duplicado y divergente")
        assets[local_path] = css_bytes

        return tag.replace(href, f"../{local_path}", 1)

    rewritten = _DATA_CSS_LINK_RE.sub(replace_link, text)
    expected = {
        "assets/quarto-bootstrap-light.css",
        "assets/quarto-bootstrap-dark.css",
    }
    if set(assets) != expected:
        raise ValueError(
            f"{label}: no se pudieron extraer ambos temas Bootstrap compartidos"
        )

    rewritten_bytes = rewritten.encode("utf-8")
    validate_self_contained_html(rewritten_bytes, label=label)
    return rewritten_bytes, assets


def _strip_unused_bootstrap_icons(head: str, main: str) -> str:
    if re.search(r'class=["\'][^"\']*\bbi(?:\s|[-"\'])', main, re.I):
        return head

    def replace_style(match: re.Match[str]) -> str:
        return "" if "bootstrap-icons" in match.group(1) else match.group(0)

    return _STYLE_RE.sub(replace_style, head)


def optimize_offline_html(data: bytes, *, label: str) -> bytes:
    """Keep the static reading document while dropping website-only runtime.

    The public website render includes navigation, search and generic
    interaction libraries that are redundant inside the native offline reader.
    MathJax, theme fonts, content styles and unknown/content-specific scripts
    are preserved. The canonical reader shell is restored around <main> so the
    same mobile layout contract applies online and offline.
    """

    text = data.decode("utf-8", errors="strict")
    head, body_open, main, lang = _isolate_offline_structure(text, label=label)

    head = _strip_offline_scripts(head)
    head = _strip_unused_bootstrap_icons(head, main)
    head += (
        '<style id="ma-offline-reader-layout" data-ma-offline-reader-layout="v1">'
        + _OFFLINE_READER_LAYOUT_CSS
        + "</style>"
    )

    reader_shell = (
        '<div id="quarto-content" '
        'class="quarto-container page-columns page-rows-contents '
        'page-layout-article page-navbar">'
        + main
        + "</div>"
    )
    optimized_text = (
        "<!DOCTYPE html>\n"
        f'<html lang="{lang}"><head>{head}</head>'
        f"{body_open}{reader_shell}</body></html>\n"
    )
    _isolate_offline_structure(optimized_text, label=f"{label} optimizado")
    optimized = optimized_text.encode("utf-8")

    validate_self_contained_html(optimized, label=label)
    return optimized


def build_offline_render_command(
    root: Path,
    source: Path,
    output_dir: Path,
    quarto: str = "quarto",
) -> list[str]:
    return [
        quarto,
        "render",
        str(source.relative_to(root)),
        "--to",
        "html",
        "--output-dir",
        str(output_dir),
        "-M",
        "minimal:true",
        "-M",
        "toc:false",
        "-M",
        "anchor-sections:false",
        "-M",
        "code-copy:false",
        "-M",
        "citations-hover:false",
        "-M",
        "footnotes-hover:false",
        "-M",
        "fig-responsive:true",
        "-M",
        "embed-resources:true",
        "-M",
        "self-contained-math:true",
    ]


def render_offline_chapter(root: Path, source: Path, quarto: str = "quarto") -> bytes:
    with tempfile.TemporaryDirectory(prefix="ma-offline-") as tmp:
        output_dir = Path(tmp).resolve()
        command = build_offline_render_command(
            root,
            source,
            output_dir,
            quarto=quarto,
        )
        completed = subprocess.run(
            command,
            cwd=root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"Quarto falló para {source.relative_to(root)}:\n{completed.stdout}"
            )

        matches = list(output_dir.rglob(f"{source.stem}.html"))
        if len(matches) != 1:
            raise RuntimeError(
                f"render offline ambiguo para {source.relative_to(root)}: {len(matches)} salidas"
            )

        raw_data = matches[0].read_bytes()
        data = optimize_offline_html(
            raw_data,
            label=str(source.relative_to(root)),
        )
        reduction = 100.0 * (1.0 - (len(data) / len(raw_data)))
        print(
            "offline-optimize: "
            f"{source.relative_to(root)}: "
            f"{len(raw_data)} -> {len(data)} bytes "
            f"({reduction:.1f}% menos)"
        )
        return data


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

    for chapter in chapters:
        chapter_id = chapter["id"]
        data = artifacts.get(chapter_id)
        if data is None:
            raise ValueError(f"falta artefacto offline para {chapter_id}")
        validate_self_contained_html(data, label=chapter_id)

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
        if not local_path.startswith("assets/") or not local_path.endswith(".css"):
            raise ValueError(f"asset offline no soportado: {local_path}")
        asset_entries.append(
            {
                "remotePath": f"/app/offline/{book['id']}/{local_path}",
                "localPath": local_path,
                "mediaType": "text/css",
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
    shared_assets: dict[str, bytes] = {}
    for chapter in chapters:
        source = resolve_source_path(root, chapter["path"])
        optimized = render_offline_chapter(root, source, quarto=quarto)
        data, chapter_assets = extract_shared_theme_styles(
            optimized,
            label=str(source.relative_to(root)),
        )
        for local_path, asset_data in chapter_assets.items():
            previous = shared_assets.get(local_path)
            if previous is not None and previous != asset_data:
                raise ValueError(
                    f"asset compartido divergente entre capítulos: {local_path}"
                )
            shared_assets[local_path] = asset_data

        reduction = 100.0 * (1.0 - (len(data) / len(optimized)))
        print(
            "offline-share-theme: "
            f"{source.relative_to(root)}: "
            f"{len(optimized)} -> {len(data)} bytes "
            f"({reduction:.1f}% menos en HTML)"
        )
        artifacts[chapter["id"]] = data
        (content_dir / f"{chapter['id']}.html").write_bytes(data)

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
