#!/usr/bin/env python3
"""FND temporary release QA: official Quarto HTML, cross-links, MathJax and responsive browser."""
import functools
import http.server
import json
import re
import threading
from pathlib import Path
from urllib.parse import unquote, urlsplit

from playwright.sync_api import sync_playwright

SITE = Path("_site").resolve()
OUT = Path("qa-fnd-release")
WIDTHS = (320, 390, 1440)

def pages():
    index = SITE / "libros/para-matematicos/fundamentos-para-matematicos.html"
    chapters = sorted((SITE / "libros/capitulos").glob("fundamentos-para-matematicos-capitulo-*.html"))
    appendices = sorted((SITE / "libros/capitulos").glob("fundamentos-para-matematicos-apendice-*.html"))
    assert len(chapters) == 11, f"expected 11 chapters; found {len(chapters)}"
    assert len(appendices) == 4, f"expected 4 appendices; found {len(appendices)}"
    assert index.is_file(), "book index missing"
    return [index, *chapters, *appendices]

def verify_local_links(paths):
    errors = []
    count = 0
    for file in paths:
        contents = file.read_text(encoding="utf-8")
        assert "<html" in contents.lower(), file
        for href in re.findall(r'<a\b[^>]*\bhref="([^"]+)"', contents):
            u = urlsplit(href)
            if u.scheme or u.netloc or not u.path:
                continue
            if "fundamentos-para-matematicos" not in u.path:
                continue
            target = (SITE / unquote(u.path).lstrip("/") if u.path.startswith("/")
                      else file.parent / unquote(u.path)).resolve()
            count += 1
            if not target.is_relative_to(SITE) or not target.is_file():
                errors.append(f"{file.name}: missing target {href}")
                continue
            if u.fragment and u.fragment.startswith("fnd-section-"):
                anchor = unquote(u.fragment)
                if f'id="{anchor}"' not in target.read_text(encoding="utf-8"):
                    errors.append(f"{file.name}: missing anchor {href}")
    print("FND_LINK_QA", json.dumps({"checked": count, "errors": errors[:15]}))
    assert not errors, "FND internal links broken"
    return count

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return

def main():
    paths = pages()
    OUT.mkdir(exist_ok=True)
    link_count = verify_local_links(paths)
    handler = functools.partial(QuietHandler, directory=str(SITE))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 8765), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    results = []
    issues = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        context = browser.new_context(viewport={"width": WIDTHS[0], "height": 900}, device_scale_factor=1)
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda exception: errors.append(str(exception)))
        for file in paths:
            slug = str(file.relative_to(SITE))
            chapter = "capitulo-" in file.name
            errors = []
            try:
                page.set_viewport_size({"width": WIDTHS[0], "height": 900})
                page.goto("http://127.0.0.1:8765/" + slug, wait_until="load", timeout=60000)
                if chapter:
                    page.wait_for_function("() => Boolean(window.MathJax && MathJax.startup && MathJax.startup.promise)", timeout=60000)
                    page.evaluate("async () => { await MathJax.startup.promise; }")
                page.evaluate("() => document.fonts.ready")
                for width in WIDTHS:
                    page.set_viewport_size({"width": width, "height": 900})
                    page.wait_for_timeout(150)
                    stats = page.evaluate("""() => {
                       const W = document.documentElement.clientWidth;
                       const H = Math.max(document.documentElement.scrollWidth, document.body.scrollWidth);
                       const isScrollable = (e) => {
                         for (let p=e.parentElement;p;p=p.parentElement) {
                           const css=getComputedStyle(p);
                           if (/(auto|scroll|hidden|clip)/.test(css.overflowX) && p.clientWidth < p.scrollWidth+2) return true;
                         }
                         return false;
                       };
                       const nodes = [...document.querySelectorAll("main table, main mjx-container, main pre, main svg, main img")];
                       const unprotected = nodes.filter(e => {
                         const rect = e.getBoundingClientRect();
                         const css = getComputedStyle(e);
                         return css.display !== "none" && css.visibility !== "hidden" && rect.width > 0 &&
                                rect.right > W + 3 && !isScrollable(e);
                       }).slice(0, 12).map(e => ({tag:e.tagName, width:Math.round(e.getBoundingClientRect().width)}));
                       return {
                         clientWidth: W, scrollWidth:H,
                         math: document.querySelectorAll("mjx-container").length,
                         merror: document.querySelectorAll("mjx-merror,.mjx-merror,[data-mjx-error]").length,
                         remainingMath: document.querySelectorAll(".MathJax_Preview, script[type^='math/tex']").length,
                         wrappers:document.querySelectorAll(".table-responsive").length,
                         unprotected
                       };
                    }""")
                    item = {"page": slug, "width": width, **stats, "pageErrors": errors[:3]}
                    results.append(item)
                    if chapter and stats["math"] == 0:
                        issues.append(f"{slug}/{width}: MathJax rendered no expressions")
                    if stats["merror"] or stats["remainingMath"]:
                        issues.append(f"{slug}/{width}: unprocessed/error MathJax {stats}")
                    if stats["scrollWidth"] > stats["clientWidth"] + 2:
                        issues.append(f"{slug}/{width}: page horizontal overflow {stats['scrollWidth']}>{stats['clientWidth']}")
                    if stats["unprotected"]:
                        issues.append(f"{slug}/{width}: unprotected overflowing content: {stats['unprotected']}")
                    if width in (320, 390, 1440) and any(k in file.name for k in (
                        "capitulo-2-", "capitulo-3-", "capitulo-4-", "capitulo-6-", "capitulo-11-",
                        "fundamentos-para-matematicos.html"
                    )):
                        page.screenshot(path=str(OUT / f"{file.stem}-{width}.png"), full_page=False)
                    print("FND_VIEWPORT_DONE", slug, width, stats["math"], flush=True)
                print("FND_PAGE_DONE", slug, flush=True)
            except Exception as err:
                issues.append(f"{slug}: browser failure {err}")
                print("FND_PAGE_ERROR", slug, str(err), flush=True)
        context.close()
        browser.close()
    server.shutdown()
    report = {"pages":len(paths), "viewports":list(WIDTHS), "loads":len(results),
              "internalLinks":link_count, "results":results, "issues":issues}
    (OUT / "fnd-release-qa.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print("FND_RELEASE_QA_SUMMARY", json.dumps({
        "pages":len(paths), "loads":len(results), "math_total":sum(v["math"] for v in results),
        "merror_total":sum(v["merror"] for v in results),
        "page_overflows":sum(v["scrollWidth"]>v["clientWidth"]+2 for v in results),
        "unprotected":sum(len(v["unprotected"]) for v in results),
        "internal_links":link_count,"issues":issues[:25]
    },ensure_ascii=False))
    assert len(results) == len(paths) * len(WIDTHS), "missing browser viewports"
    assert not issues, "release browser QA failed"

if __name__ == "__main__":
    main()
