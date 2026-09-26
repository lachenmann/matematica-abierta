import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from generate_app_catalog import build_catalog, parse_front_matter, source_to_public_path


class FrontMatterTests(unittest.TestCase):
    def test_parses_catalog_fields(self):
        data = parse_front_matter(
            """---
title: "Ejemplo"
description: "Descripción"
content-id: MA-CON-9999
content-type: concept
status: published
date-modified: 2026-09-24
areas:
  - algebra
  - fundamentos
topics: []
difficulty: 2
draft: false
---

Texto.
"""
        )
        self.assertEqual(data["content-id"], "MA-CON-9999")
        self.assertEqual(data["areas"], ["algebra", "fundamentos"])
        self.assertEqual(data["topics"], [])
        self.assertEqual(data["difficulty"], 2)
        self.assertFalse(data["draft"])

    def test_public_path(self):
        self.assertEqual(
            source_to_public_path(Path("conceptos/ejemplo.md")),
            "/conceptos/ejemplo.html",
        )


class CatalogTests(unittest.TestCase):
    def test_exports_only_explicitly_published_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "conceptos").mkdir()
            (root / "conceptos" / "publicado.md").write_text(
                """---
title: "Publicado"
content-id: MA-CON-0001
content-type: concept
status: published
date-modified: 2026-09-24
areas:
  - fundamentos
license: GFDL-1.3-or-later
---
""",
                encoding="utf-8",
            )
            (root / "conceptos" / "borrador.md").write_text(
                """---
title: "Borrador"
content-id: MA-CON-0002
content-type: concept
status: draft
---
""",
                encoding="utf-8",
            )
            (root / "sin-id.qmd").write_text(
                """---
title: "Índice"
---
""",
                encoding="utf-8",
            )

            catalog = build_catalog(
                root,
                generated_at="2026-09-24T12:00:00Z",
            )

            self.assertEqual(catalog["schemaVersion"], 1)
            self.assertEqual(catalog["generatedAt"], "2026-09-24T12:00:00Z")
            self.assertEqual(len(catalog["items"]), 1)
            self.assertEqual(catalog["items"][0]["id"], "MA-CON-0001")
            self.assertEqual(
                catalog["items"][0]["path"],
                "/conceptos/publicado.html",
            )

    def test_book_id_maps_to_parent_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "capitulo.md").write_text(
                """---
title: "Capítulo"
content-id: MA-BCH-9999
content-type: book-chapter
book-id: MA-BOK-9999
status: published
---
""",
                encoding="utf-8",
            )

            catalog = build_catalog(
                root,
                generated_at="2026-09-24T12:00:00Z",
            )
            self.assertEqual(catalog["items"][0]["parentId"], "MA-BOK-9999")

    def test_duplicate_ids_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("a.md", "b.md"):
                (root / name).write_text(
                    f"""---
title: "{name}"
content-id: MA-CON-0001
content-type: concept
status: published
---
""",
                    encoding="utf-8",
                )

            with self.assertRaisesRegex(ValueError, "duplicate content-id"):
                build_catalog(root)

    def test_noncanonical_type_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "x.md").write_text(
                """---
title: "X"
content-id: MA-APP-0001
content-type: interactive-application
status: published
---
""",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "non-canonical content-type"):
                build_catalog(root)

    def test_id_prefix_must_match_type(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "x.md").write_text(
                """---
title: "X"
content-id: MA-PRB-0001
content-type: concept
status: published
---
""",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "expected prefix MA-CON-"):
                build_catalog(root)


if __name__ == "__main__":
    unittest.main()
