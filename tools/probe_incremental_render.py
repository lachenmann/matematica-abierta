#!/usr/bin/env python3
"""Isolated incremental/full Quarto equivalence probe; never publishes."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "incremental-probe-report"
TARGET = "licencia.qmd"
MARKER = "MA_INCREMENTAL_PROBE_20261006"
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(directory):
    return {p.relative_to(directory).as_posix(): digest(p)
            for p in directory.rglob("*") if p.is_file()}
def render(root, args, label):
    start = time.monotonic()
    with (REPORT / (label + ".log")).open("w") as log:
        process = subprocess.run(["quarto", "render", *args], cwd=root,
                                 stdout=log, stderr=subprocess.STDOUT)
    elapsed = time.monotonic() - start
    if process.returncode:
        raise RuntimeError(f"{label} failed; inspect log")
    return elapsed
def main():
    REPORT.mkdir(exist_ok=True)
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    version = subprocess.check_output(["quarto", "--version"], text=True).strip()
    with tempfile.TemporaryDirectory(prefix="ma-incremental-probe-") as tmp:
        work = Path(tmp)
        baseline = work / "baseline"
        shutil.copytree(ROOT, baseline, ignore=shutil.ignore_patterns(".git", "_site", ".quarto", "incremental-probe-report"))
        subprocess.run(["python3", "tools/generate_app_catalog.py"], cwd=baseline, check=True)
        times = {"baseline_full": render(baseline, [], "baseline")}
        before = inventory(baseline / "_site")
        incremental = work / "incremental"
        full = work / "full"
        # Both start with exactly the same full output, catalog and Quarto state.
        shutil.copytree(baseline, incremental)
        shutil.copytree(baseline, full)
        for root in [incremental, full]:
            p = root / TARGET
            text = p.read_text()
            assert "## Código" in text
            p.write_text(text.replace("## Código", f"Prueba editorial aislada: {MARKER}.\n\n## Código", 1))
        times["incremental"] = render(incremental, [TARGET], "incremental")
        times["full"] = render(full, [], "full")
        inc = inventory(incremental / "_site")
        ref = inventory(full / "_site")
        missing = sorted(set(ref) - set(inc))
        extra = sorted(set(inc) - set(ref))
        different = sorted(p for p in set(ref) & set(inc) if ref[p] != inc[p])
        changed = sorted(p for p in set(before) & set(inc) if before[p] != inc[p])
        marker_html = MARKER in (incremental / "_site/licencia.html").read_text()
        marker_search = MARKER in (incremental / "_site/search.json").read_text()
        base_search = json.loads((baseline / "_site/search.json").read_text())
        inc_search = json.loads((incremental / "_site/search.json").read_text())
        ref_search = json.loads((full / "_site/search.json").read_text())
        identical = not missing and not extra and not different
        summary = {
            "revision": revision, "quarto": version, "target": TARGET,
            "method": "copy full _site and .quarto; identical editorial patch; shared catalog timestamp; no publish",
            "seconds": times, "speedup_render": times["full"] / times["incremental"],
            "files_baseline": len(before), "files_incremental": len(inc), "files_full": len(ref),
            "missing": missing, "extra": extra, "different": different,
            "changed_from_baseline": changed,
            "marker_in_html": marker_html, "marker_in_search": marker_search,
            "search_records": {"baseline":len(base_search), "incremental":len(inc_search), "full":len(ref_search)},
            "search_json_semantically_equal": inc_search == ref_search,
            "verdict": "PASS_EXACT" if identical and marker_html and marker_search else "DIFFERENCES_REQUIRE_REVIEW"
        }
        (REPORT / "report.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
        for name, root in [("baseline", baseline), ("incremental", incremental), ("full", full)]:
            (REPORT / (name + "-inventory.json")).write_text(json.dumps(inventory(root / "_site"), indent=2))
        for path in sorted(set(different + extra + missing + ["licencia.html", "search.json", "sitemap.xml"])):
            for name, root in [("incremental", incremental), ("full", full)]:
                p = root / "_site" / path
                if p.is_file():
                    out = REPORT / "differences" / name / path
                    out.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(p, out)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        with open(os.environ.get("GITHUB_STEP_SUMMARY", os.devnull), "a") as stream:
            stream.write(f"### Quarto incremental probe\n\nVerdict: **{summary['verdict']}**\n\n")
            stream.write(f"Full render: {times['full']:.1f}s; incremental: {times['incremental']:.1f}s.\n")
        return 0
if __name__ == "__main__":
    raise SystemExit(main())
