"""Fail-closed resource graph checks for offline book packages.

HTML is parsed as HTML (never as JavaScript text); CSS URLs are tokenized so
escapes, comments and quoted @imports cannot bypass the package boundary.
"""
import base64
import posixpath
import re
from html.parser import HTMLParser
from urllib.parse import unquote_to_bytes, urlsplit

import tinycss2


def package_path(value):
    if (not isinstance(value, str) or not value or
            re.search(r"[\\%?#:\s\x00-\x1f]", value) or value.startswith("/") or
            any(part in {"", ".", ".."} for part in value.split("/"))):
        raise ValueError(f"unsafe offline resource path: {value!r}")
    return value


class Resources:
    def __init__(self, local_path, declared, label):
        self.local_path = package_path(local_path)
        self.declared = {package_path(path) for path in declared}
        self.label = label

    def fail(self, value):
        raise ValueError(f"{self.label}: subrecurso externo o no declarado: {value[:160]}")

    def url(self, value, depth=0):
        if depth > 8:
            self.fail("nested data resource")
        value = value.strip()
        if value.startswith("#"):
            return
        if value.lower().startswith("data:"):
            header, separator, payload = value.partition(",")
            media = header[5:].split(";")[0].lower()
            if not separator:
                self.fail(value)
            if media in {"text/css", "image/svg+xml"}:
                raw = unquote_to_bytes(payload)
                if ";base64" in header.lower():
                    raw = base64.b64decode(raw, validate=True)
                text = raw.decode("utf-8")
                if media == "text/css":
                    self.css(text, depth + 1)
                else:
                    self.html(text, depth + 1)
            elif not (media.startswith("image/") or media.startswith("font/") or
                      media in {"application/font-woff", "application/x-font-ttf", "application/vnd.ms-fontobject", "application/octet-stream"}):
                self.fail(value)
            return
        # Reject encoded separators/traversal instead of relying on differing
        # URL decoders in browsers, native downloaders and filesystems.
        if not value or re.search(r"[\\\x00-\x20\x7f]", value):
            self.fail(value)
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or value.startswith("/") or "%" in value or parsed.query:
            self.fail(value)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(self.local_path), parsed.path))
        if target.startswith("../") or target == ".." or target not in self.declared:
            self.fail(value)

    def css(self, text, depth=0):
        def walk(tokens):
            significant = [t for t in tokens if t.type not in {"whitespace", "comment"}]
            for index, token in enumerate(significant):
                if token.type == "error":
                    self.fail("invalid CSS")
                if token.type == "url":
                    self.url(token.value, depth)
                elif token.type == "function":
                    if token.lower_name == "url":
                        args = [t for t in token.arguments if t.type not in {"whitespace", "comment"}]
                        if len(args) != 1 or args[0].type != "string":
                            self.fail("invalid CSS URL")
                        self.url(args[0].value, depth)
                    elif token.lower_name in {"image-set", "-webkit-image-set"}:
                        for arg in token.arguments:
                            if arg.type == "string":
                                self.url(arg.value, depth)
                        walk(token.arguments)
                    else:
                        walk(token.arguments)
                elif token.type == "at-keyword" and token.lower_value == "import":
                    if index + 1 >= len(significant):
                        self.fail("invalid CSS import")
                    following = significant[index + 1]
                    if following.type == "string":
                        self.url(following.value, depth)
                elif hasattr(token, "content"):
                    walk(token.content)
        walk(tinycss2.parse_component_value_list(text))

    def html(self, text, depth=0):
        owner = self

        class Parser(HTMLParser):
            in_style = False

            def handle_starttag(self, tag, attrs):
                names = [name for name, _ in attrs]
                if len(names) != len(set(names)):
                    owner.fail("duplicate HTML attribute")
                attrs = dict(attrs)
                if tag == "base" or "srcdoc" in attrs:
                    owner.fail(tag)
                if tag == "meta" and (attrs.get("http-equiv") or "").lower() == "refresh":
                    owner.fail("meta refresh")
                self.in_style = tag == "style"
                if "style" in attrs:
                    owner.css(attrs["style"] or "", depth)
                for key in ("src", "poster", "background"):
                    if key in attrs:
                        owner.url(attrs[key] or "", depth)
                if tag == "object" and "data" in attrs:
                    owner.url(attrs["data"] or "", depth)
                if tag != "a":
                    for key in ("href", "xlink:href"):
                        if key in attrs:
                            owner.url(attrs[key] or "", depth)
                # No srcset is emitted by the supported book renderer. Reject
                # until candidate parsing is supported, including data commas.
                if "srcset" in attrs or "imagesrcset" in attrs:
                    owner.fail("srcset unsupported")

            handle_startendtag = handle_starttag

            def handle_endtag(self, tag):
                if tag == "style":
                    self.in_style = False

            def handle_data(self, data):
                if self.in_style:
                    owner.css(data, depth)

        parser = Parser(convert_charrefs=True)
        parser.feed(text)
        parser.close()
