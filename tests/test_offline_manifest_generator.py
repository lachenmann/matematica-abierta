import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from generate_offline_manifests import (
    build_manifest,
    load_catalog,
    resolve_source_path,
    select_book,
    validate_self_contained_html,
)


def sample_catalog():
    return {
        "schemaVersion": 1,
        "generatedAt": "2026-10-05T17:00:00Z",
        "siteBaseUrl": "https://matematicaabierta.cl",
        "items": [
            {
                "id": "MA-BOK-0005",
                "type": "book",
                "title": "Física para matemáticos",
                "path": "/libros/para-matematicos/fisica-para-matematicos.html",
                "status": "published",
            },
            {
                "id": "MA-BCH-0009",
                "type": "book-chapter",
                "title": "Capítulo 1",
                "path": "/libros/capitulos/capitulo-1.html",
                "parentId": "MA-BOK-0005",
                "dateModified": "2026-09-10",
                "status": "published",
            },
            {
                "id": "MA-BCH-0031",
                "type": "book-chapter",
                "title": "Capítulo 2",
                "path": "/libros/capitulos/capitulo-2.html",
                "parentId": "MA-BOK-0005",
                "dateModified": "2026-09-15",
                "status": "published",
            },
        ],
    }


class OfflineManifestGeneratorTests(unittest.TestCase):
    def test_catalog_and_book_selection_are_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "catalog.json"
            path.write_text(json.dumps(sample_catalog()), encoding="utf-8")
            catalog = load_catalog(path)

        book, chapters = select_book(catalog, "MA-BOK-0005")
        self.assertEqual(book["id"], "MA-BOK-0005")
        self.assertEqual([item["id"] for item in chapters], ["MA-BCH-0009", "MA-BCH-0031"])

        with self.assertRaisesRegex(ValueError, "bookId inválido"):
            select_book(catalog, "../bad")

    def test_source_resolution_uses_canonical_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "libros" / "capitulos" / "capitulo-1.md"
            source.parent.mkdir(parents=True)
            source.write_text("---\ntitle: X\n---\n", encoding="utf-8")

            self.assertEqual(
                resolve_source_path(root, "/libros/capitulos/capitulo-1.html"),
                source,
            )

    def test_self_contained_validation_allows_external_links_but_not_subresources(self):
        validate_self_contained_html(
            b'<html><body><a href="https://example.com">x</a>'
            b'<img src="data:image/png;base64,AA=="></body></html>',
            label="ok",
        )

        with self.assertRaisesRegex(ValueError, "subrecurso externo"):
            validate_self_contained_html(
                b'<html><body><script src="https://cdn.example/x.js"></script></body></html>',
                label="bad",
            )

    def test_manifest_hashes_real_bytes_and_version_is_deterministic(self):
        catalog = sample_catalog()
        book, chapters = select_book(catalog, "MA-BOK-0005")
        artifacts = {
            "MA-BCH-0009": b"<html><body>uno</body></html>",
            "MA-BCH-0031": b"<html><body>dos</body></html>",
        }

        first = build_manifest(
            book,
            chapters,
            artifacts,
            generated_at="2026-10-05T17:00:00Z",
        )
        second = build_manifest(
            book,
            chapters,
            artifacts,
            generated_at="2026-10-05T18:00:00Z",
        )

        self.assertEqual(first["schemaVersion"], 1)
        self.assertEqual(first["bookId"], "MA-BOK-0005")
        self.assertEqual(first["entryContentId"], "MA-BCH-0009")
        self.assertEqual(first["assets"], [])
        self.assertEqual(first["version"], second["version"])
        self.assertEqual(
            first["totalSize"],
            sum(item["size"] for item in first["contents"]),
        )
        self.assertEqual(len(first["contents"][0]["sha256"]), 64)

        changed = dict(artifacts)
        changed["MA-BCH-0031"] = b"<html><body>dos revisado</body></html>"
        third = build_manifest(
            book,
            chapters,
            changed,
            generated_at="2026-10-05T18:00:00Z",
        )
        self.assertNotEqual(first["version"], third["version"])


if __name__ == "__main__":
    unittest.main()
