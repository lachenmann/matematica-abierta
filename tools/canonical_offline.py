"""Derive a reader package from the already-rendered canonical website.

No Markdown rendering or formula-specific layout changes occur here. Remote
downloads happen only at build time, from the explicit font/CDN allowlist.
"""
import base64
import hashlib
import gzip
import io
import json
import re
import tarfile
from html import escape, unescape
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

import tinycss2

from offline_resources import Resources, package_path

LOCK = Path(__file__).with_name("offline-runtime-lock.json")
MEDIA = {".css": "text/css", ".js": "application/javascript", ".woff2": "font/woff2",
         ".woff": "font/woff", ".ttf": "font/ttf", ".svg": "image/svg+xml",
         ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
         ".webp": "image/webp", ".txt": "text/plain"}


def download(url):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname not in {
        "fonts.googleapis.com", "fonts.gstatic.com", "registry.npmjs.org", "cdn.jsdelivr.net"
    }:
        raise ValueError(f"build resource origin not allowed: {url}")
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36"})
    with urlopen(request, timeout=60) as response:
        if urlsplit(response.url).hostname != parsed.hostname:
            raise ValueError("resource redirected outside its origin")
        return response.read()


class CanonicalAssets:
    def __init__(self, site):
        self.site = site.resolve()
        self.assets = {}
        self.resolved = {}
        self.active = set()

    def mathjax(self):
        lock = json.loads(LOCK.read_text())
        speech_maps = {}
        speech_worker = None
        for name, info in lock.items():
            raw = download(info["url"])
            if hashlib.sha512(raw).digest() != base64.b64decode(info["integrity"].removeprefix("sha512-")):
                raise ValueError(f"MathJax distribution integrity failed: {name}")
            with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as archive:
                for member in archive.getmembers():
                    relative = member.name.removeprefix("package/")
                    if not member.isfile():
                        continue
                    if name == "mathjax" and relative.startswith("sre/mathmaps/") and relative.endswith(".json"):
                        speech_maps[Path(relative).name] = json.loads(archive.extractfile(member).read())
                    if name == "mathjax" and relative == "sre/speech-worker.js":
                        speech_worker = archive.extractfile(member).read().decode("utf-8")
                    if name == "mathjax":
                        keep = relative == "tex-chtml.js" or relative.startswith("input/tex/extensions/") or relative == "LICENSE"
                        dest = "assets/mathjax/" + relative
                    else:
                        keep = relative.startswith("chtml/") or relative == "LICENSE"
                        dest = "assets/mathjax-newcm/" + relative
                    if keep:
                        if relative == "LICENSE":
                            dest += ".txt"
                        package_path(dest)
                        self.assets[dest] = archive.extractfile(member).read()
        if not speech_worker or not {"base.json", "en.json", "es.json", "nemeth.json"}.issubset(speech_maps):
            raise ValueError("MathJax speech resources missing")
        # file:// workers cannot fetch JSON or importScripts from sibling files
        # with the app's restrictive WebView permissions. Supply the unchanged
        # upstream worker and every locale map in one deterministic compressed
        # asset; its fetch adapter only serves this in-memory declared map.
        worker_source = ('self.maps="offline-mathmaps:";const offlineMaps='
                         + json.dumps(speech_maps, separators=(",", ":"))
                         + ';self.fetch=async function(url){const key=String(url).split("/").pop();'
                         'if(!Object.hasOwn(offlineMaps,key))throw Error("Undeclared speech map: "+key);'
                         'return {json:async()=>offlineMaps[key]};};\n' + speech_worker)
        packed = bytearray(gzip.compress(worker_source.encode(), mtime=0))
        packed[9] = 255  # Normalize the gzip OS byte across Python/zlib platforms.
        compressed = base64.b64encode(packed).decode()
        adapter = '''window.__maCreateSpeechWorker=async function(onmessage){
          const packed=Uint8Array.from(atob(PAYLOAD),c=>c.charCodeAt(0));
          const source=await new Response(new Blob([packed]).stream().pipeThrough(new DecompressionStream("gzip"))).text();
          const url=URL.createObjectURL(new Blob([source],{type:"text/javascript"}));
          const worker=new Worker(url); worker.onmessage=onmessage;
          URL.revokeObjectURL(url); return worker;
        };'''.replace("PAYLOAD", json.dumps(compressed))
        self.assets['assets/mathjax-offline-speech.js'] = adapter.encode()
        # Fail if the canonical moving-major URL no longer matches this lock.
        canonical = download("https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js")
        if canonical != self.assets["assets/mathjax/tex-chtml.js"]:
            raise ValueError("canonical MathJax changed: update and verify offline-runtime-lock.json")

    def resource(self, url, base, preferred=None):
        if url.startswith("data:") or url.startswith("#"):
            return url
        absolute = urljoin(base, url)
        if absolute in self.resolved:
            return self.resolved[absolute]
        if absolute in self.active:
            raise ValueError(f"cyclic resource import: {absolute}")
        self.active.add(absolute)
        parsed = urlsplit(absolute)
        if parsed.scheme == "https":
            raw = download(absolute)
            suffix = ".css" if parsed.hostname == "fonts.googleapis.com" else Path(parsed.path).suffix
        elif parsed.scheme == "file":
            if parsed.netloc or "%" in parsed.path:
                raise ValueError(f"unsupported canonical file URL: {url}")
            path = Path(parsed.path).resolve()
            if not path.is_relative_to(self.site):
                raise ValueError(f"canonical resource outside site: {url}")
            raw = path.read_bytes()
            suffix = path.suffix
        else:
            raise ValueError(f"unsupported canonical resource: {url}")
        if suffix not in MEDIA:
            raise ValueError(f"unsupported canonical media: {absolute}")
        if suffix == ".css":
            raw = self.css(raw.decode("utf-8"), absolute).encode("utf-8")
        dest = preferred or f"assets/{hashlib.sha256(raw).hexdigest()[:24]}{suffix}"
        package_path(dest)
        if dest in self.assets and self.assets[dest] != raw:
            raise ValueError(f"divergent canonical asset: {dest}")
        self.assets[dest] = raw
        result = "../" + dest
        self.resolved[absolute] = result
        self.active.remove(absolute)
        return result

    def css(self, text, base):
        def replace(token):
            value = self.resource(token.value, base)
            token.value = value
            quoted = json.dumps(value, ensure_ascii=False)
            token.representation = f"url({quoted})" if token.type == "url" else quoted

        def walk(tokens):
            significant = [t for t in tokens if t.type not in {"whitespace", "comment"}]
            for index, token in enumerate(significant):
                if token.type == "error":
                    raise ValueError("invalid canonical CSS")
                if token.type == "url":
                    replace(token)
                elif token.type == "function":
                    if token.lower_name == "url":
                        for arg in token.arguments:
                            if arg.type == "string":
                                replace(arg)
                    else:
                        walk(token.arguments)
                elif token.type == "at-keyword" and token.lower_value == "import":
                    following = significant[index + 1]
                    if following.type == "string":
                        replace(following)
                elif hasattr(token, "content"):
                    walk(token.content)
        tokens = tinycss2.parse_component_value_list(text)
        walk(tokens)
        return tinycss2.serialize(tokens)

    def chapter(self, canonical_path, chapter_id):
        # Shared structural parser; imported lazily to avoid initialization cycles.
        from generate_offline_manifests import _isolate_offline_structure, _SCRIPT_RE, _html_attr_value, _OfflineStructureParser
        path = (self.site / canonical_path.lstrip("/")).resolve()
        if not path.is_relative_to(self.site):
            raise ValueError("canonical chapter escapes site")
        text = path.read_text()
        head, body, main, lang = _isolate_offline_structure(text, label=chapter_id)
        base = path.as_uri()
        if not any(_html_attr_value(m.group(0), "id") == "ma-math-font-ready"
                   for m in _SCRIPT_RE.finditer(head)):
            raise ValueError(f"{chapter_id}: canonical MathJax font readiness hook missing; render the current source")

        def script(match):
            src = _html_attr_value(match.group(0), "src")
            if src == "../../site_libs/quarto-html/anchor.min.js":
                return match.group(0).replace(src, self.resource(src, base))
            if src == "https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js":
                return ('<script src="../assets/mathjax-offline-speech.js"></script>'
                        '<script>(function(){const fontRoot=new URL("../assets/mathjax-newcm",location.href).href;'
                        'window.MathJax=Object.assign(window.MathJax||{}, {loader:{paths:{"mathjax-newcm":fontRoot}},'
                        'startup:{ready:function(){MathJax.startup.defaultReady();'
                        'MathJax.startup.adaptor.createWorker=window.__maCreateSpeechWorker;},'
                        'pageReady:window.MathJax.startup.pageReady},'
                        'output:{fontPath:fontRoot},'
                        'chtml:{fontURL:fontRoot+"/chtml/woff2",'
                        'dynamicPrefix:fontRoot+"/chtml/dynamic"}});})();</script>'
                        '<script defer src="../assets/mathjax/tex-chtml.js"></script>')
            if src == "https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=es6":
                return ""  # Expo 57 WebViews and supported browsers implement ES6.
            if src:
                if src in {"../../site_libs/" + item for item in (
                    "quarto-nav/quarto-nav.js", "quarto-nav/headroom.min.js",
                    "clipboard/clipboard.min.js", "quarto-search/autocomplete.umd.js",
                    "quarto-search/fuse.min.js", "quarto-search/quarto-search.js",
                    "quarto-html/quarto.js", "quarto-html/tabsets/tabsets.js",
                    "quarto-html/popper.min.js", "quarto-html/tippy.umd.min.js",
                    "quarto-html/anchor.min.js", "bootstrap/bootstrap.min.js",
                )}:
                    return ""
                raise ValueError(f"unreviewed canonical script: {src}")
            if _html_attr_value(match.group(0), "id") == "quarto-search-options":
                return ""
            return match.group(0)

        head = _SCRIPT_RE.sub(script, head)
        head = ('<meta http-equiv="Content-Security-Policy" content="'
                "default-src 'none'; script-src 'self' file: 'unsafe-inline'; "
                "style-src 'self' file: data: 'unsafe-inline'; font-src 'self' file: data:; "
                "img-src 'self' file: data:; connect-src 'none'; base-uri 'none'; form-action 'none'"
                "; worker-src blob:"
                '">' + head)
        head += '<style id="ma-reader-mode-v1-style">' + Path(__file__).with_name("offline-reader.css").read_text() + "</style>"
        # quarto-nav computes this from the hidden header in the online reader.
        # Offline has no navigation runtime/header, so its reserved space is 0.
        head += '<style>body.nav-fixed{padding-top:0!important}</style>'
        def link(match):
            tag = match.group(0)
            href = _html_attr_value(tag, "href")
            if not href:
                return tag
            if href.endswith("/bootstrap-icons.css") and not re.search(r'class=["\'][^"\']*\bbi(?:\s|[-"\'])', main):
                return ""
            if _html_attr_value(tag, "rel") == "canonical":
                return ""
            preferred = None
            if _html_attr_value(tag, "id") == "quarto-bootstrap":
                mode = _html_attr_value(tag, "data-mode")
                if mode not in {"light", "dark"}:
                    raise ValueError("invalid canonical theme")
                preferred = f"assets/quarto-bootstrap-{mode}.css"
            return tag.replace(href, escape(self.resource(unescape(href), base, preferred), quote=True))
        head = re.sub(r"<link\b[^>]*>", link, head, flags=re.I)
        # Keep Quarto's exact theme initialization, body and content shell.
        theme = next((m.group(0) for m in _SCRIPT_RE.finditer(text)
                      if _html_attr_value(m.group(0), "id") == "quarto-html-before-body"), "")
        reader_controls = "".join(m.group(0) for m in _SCRIPT_RE.finditer(text)
                                  if "main.querySelector(':scope > .ma-reader-tools')" in m.group(2))
        anchor_setup = re.search(r'const icon = [^;]+;\s*const anchorJS = new window\.AnchorJS\(\);[\s\S]*?anchorJS\.add\(\x27\.anchored\x27\);', text)
        if 'class="anchored"' in main or re.search(r'class="[^"]*\banchored\b', main):
            if not anchor_setup:
                raise ValueError("canonical heading anchor initialization missing")
            reader_controls += ('<script>document.addEventListener("DOMContentLoaded",function(){'
                                + anchor_setup.group() + '});</script>')
        structure = _OfflineStructureParser(text)
        structure.feed(text)
        shell = structure.content_open
        if not shell or not theme:
            raise ValueError("canonical reader shell/theme missing")
        # Navigation hrefs remain canonical: the native bridge maps these to
        # downloaded chapters. Fragment links stay byte-for-byte unchanged.
        result = f'<!DOCTYPE html><html lang="{escape(lang)}"><head>{head}</head>{body}{theme}{shell}{main}</div>{reader_controls}</body></html>'
        Resources(f"content/{chapter_id}.html", self.assets, chapter_id).html(result)
        return result.encode("utf-8")
