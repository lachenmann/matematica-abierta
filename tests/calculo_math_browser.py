"""Reject MathJax failures in every published Cálculo para matemáticos page.

Run after Quarto render: python3 tests/calculo_math_browser.py --site _site
Requires Playwright and Chromium (already installed by Quarto Check).
"""
import argparse
import functools
import http.server
import json
import re
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright


def book_pages(root):
    pages = []
    for source in sorted((root / "libros/capitulos").glob("*.md")):
        text = source.read_text(encoding="utf-8")
        if re.search(r"^book-id: MA-BOK-0001\s*$", text, re.M) and not re.search(
            r"^draft: true\s*$", text, re.M
        ):
            pages.append(source.relative_to(root).with_suffix(".html").as_posix())
    if len(pages) < 20:
        raise RuntimeError(f"Incomplete calculation book corpus: {len(pages)} pages")
    return pages


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--output", type=Path, default=Path(".ma-build/calculo-math"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    pages = book_pages(root)
    site = args.site.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    handler = functools.partial(QuietHandler, directory=str(site))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    results = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": 1365, "height": 900})
            page.set_default_timeout(60000)
            for path in pages:
                result = {"path": path}
                try:
                    if not (site / path).is_file():
                        raise RuntimeError("Rendered page missing")
                    response = page.goto(f"http://127.0.0.1:{server.server_port}/{path}")
                    if not response or response.status != 200:
                        raise RuntimeError("Rendered page unavailable")
                    page.wait_for_function("window.MathJax && MathJax.startup && MathJax.startup.promise")
                    page.evaluate("async () => { await MathJax.startup.promise; }")
                    result.update(page.evaluate(r"""() => {
                        const root = document.querySelector('main');
                        if (!root) throw new Error('Missing main content');
                        const math = [...root.querySelectorAll('mjx-container')];
                        const errors = math.filter(e =>
                            e.querySelector('mjx-merror, merror, [mathcolor="red"]') ||
                            [...e.querySelectorAll('mjx-mtext')].some(n =>
                                n.style.color === 'red') ||
                            /\\[A-Za-z]+/.test(e.textContent)
                        ).map(e => e.textContent.slice(0, 500));
                        const unprocessed = [...root.querySelectorAll('.math')]
                            .filter(e => !e.querySelector('mjx-container'))
                            .map(e => e.textContent.slice(0, 500));
                        return {formulas: math.length, errors, unprocessed};
                    }"""))
                    if not result["formulas"]:
                        raise RuntimeError("No rendered formulas; MathJax check would be vacuous")
                    result["pass"] = not result["errors"] and not result["unprocessed"]
                except Exception as error:
                    result.update({"pass": False, "exception": str(error)})
                results.append(result)
                print(json.dumps(result, ensure_ascii=False), flush=True)
                if not result["pass"]:
                    page.screenshot(path=str(args.output / (Path(path).stem + ".png")))
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    report = {"pages": len(results), "formulas": sum(r.get("formulas", 0) for r in results),
              "pass": all(r["pass"] for r in results), "results": results}
    (args.output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if not report["pass"]:
        raise SystemExit("Cálculo MathJax QA FAILED; inspect report.json")
    print(f"Cálculo MathJax QA PASS: {report['pages']} pages, {report['formulas']} formulas")


if __name__ == "__main__":
    main()
