#!/usr/bin/env python3
"""Real Quarto test: transfer state between jobs, includes and clean fallback."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

SPEC = importlib.util.spec_from_file_location("smart_render", Path(__file__).resolve().parents[1] / "tools/smart_render.py")
smart = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(smart)


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def commit(root):
    git(root, "add", ".")
    git(root, "commit", "-qm", "isolated integration fixture")


def main():
    with tempfile.TemporaryDirectory(prefix="ma-smart-integration-") as tmp:
        work = Path(tmp)
        root = work / "source"
        root.mkdir()
        git(root, "init", "-q")
        git(root, "config", "user.email", "probe@example.invalid")
        git(root, "config", "user.name", "Probe")
        files = {
            ".gitignore": "_site/\n.quarto/\n.ma-build/\n",
            "_quarto.yml": 'project:\n  type: website\nwebsite:\n  title: Probe\n  site-url: https://example.invalid\n  search: true\nformat:\n  html:\n    css: styles.css\n',
            "styles.css": "body { color: #123; }\n",
            "index.qmd": '---\ntitle: Inicio\n---\n\n# Inicio\n\nUna explicación original.\n',
            "chapter.qmd": '---\ntitle: Capítulo\n---\n\n{{< include _shared.md >}}\n',
            "second.qmd": '---\ntitle: Segundo\n---\n\n{{< include _shared.md >}}\n',
            "_shared.md": '## Resultado {#sec-resultado}\n\nExplicación inicial.\n\n$$x^2=2$$\n',
        }
        for name, text in files.items():
            (root / name).write_text(text)
        commit(root)
        baseline = smart.build(root)
        assert baseline["mode"] == "full"
        smart.seal(root)
        archive = work / "published-base.tar.gz"
        with tarfile.open(archive, "w:gz") as tar:
            for name in ["_site", ".quarto", ".ma-build"]:
                tar.add(root / name, arcname=name)
        # A fresh checkout plus a transferred archive, not a reused build directory.
        checkout = work / "fresh-checkout"
        subprocess.run(["git", "clone", "-q", str(root), str(checkout)], check=True)
        git(checkout, "config", "user.email", "probe@example.invalid")
        git(checkout, "config", "user.name", "Probe")
        with tarfile.open(archive) as tar:
            tar.extractall(checkout, filter="data")
        # Two commits accumulated since the published base.
        (checkout / "_shared.md").write_text(files["_shared.md"].replace("Explicación inicial", "MA_SMART_SHARED_MARKER"))
        commit(checkout)
        (checkout / "index.qmd").write_text(files["index.qmd"].replace("explicación original", "MA_SMART_BODY_MARKER"))
        commit(checkout)
        reference = work / "reference"
        shutil.copytree(checkout, reference)
        incremental = smart.build(checkout)
        assert incremental["mode"] == "incremental", incremental
        assert incremental["targets"] == ["chapter.qmd", "index.qmd", "second.qmd"]
        for name in ["chapter.html", "second.html"]:
            assert "MA_SMART_SHARED_MARKER" in (checkout / "_site" / name).read_text()
        assert "MA_SMART_BODY_MARKER" in (checkout / "_site/search.json").read_text()
        complete = smart.build(reference, force_full=True)
        inc = smart.inventory(checkout / "_site")
        full = smart.inventory(reference / "_site")
        assert inc == full, {"different": [p for p in inc if inc.get(p) != full.get(p)]}
        smart.seal(checkout)
        # Corruption must be rejected, followed by a fresh complete rebuild.
        (checkout / "_site/second.html").unlink()
        corrupt = smart.build(checkout)
        assert corrupt["mode"] == "full" and "integrity" in corrupt["reason"]
        assert (checkout / "_site/second.html").exists()
        smart.seal(checkout)
        # Deletion and a global style change cannot leave stale public files.
        (checkout / "second.qmd").unlink()
        (checkout / "styles.css").write_text("body { color: #456; }\n")
        commit(checkout)
        structural = smart.build(checkout)
        assert structural["mode"] == "full"
        assert not (checkout / "_site/second.html").exists()
        assert "#456" in (checkout / "_site/styles.css").read_text()
        result = {"verdict": "PASS", "restored_archive": True, "cumulative_commits": 2,
                  "shared_include_consumers": 2, "exact_file_equivalence": True,
                  "corrupt_base_fallback": True, "deleted_output_removed": True,
                  "seconds": {"incremental": incremental["seconds"], "full": complete["seconds"]}}
        print(json.dumps(result, indent=2))
        report = Path(__file__).resolve().parents[1] / ".ma-build/integration-report.json"
        smart.json_write(report, result)


if __name__ == "__main__":
    main()
