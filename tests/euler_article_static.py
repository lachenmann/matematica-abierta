from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = ROOT / "blog/formula-de-euler-historia-derivacion-geometria.qmd"
ASSET_DIR = ROOT / "assets/articles/ma-art-0011"

EXPECTED = [
    "MA-ART-0011-F01_euler-circulo.html",
    "MA-ART-0011-F02_cotes-logaritmo.html",
    "MA-ART-0011-F03_multiplicar-girar.html",
    "MA-ART-0011-F04_euler-138.html",
    "MA-ART-0011-F05_muchos-giros.html",
    "MA-ART-0011-F06_serie-dos-ramas.html",
    "MA-ART-0011-F07_velocidad-iz.html",
    "MA-ART-0011-F08_cartesiana-polar.html",
    "MA-ART-0011-F09_media-vuelta-raices.html",
    "MA-ART-0011-F10_circulos-fourier.html",
]

def verify(condition, message):
    if not condition:
        raise AssertionError(message)

verify(ARTICLE.is_file(), "falta derivado web MA-ART-0011")
text = ARTICLE.read_text(encoding="utf-8")
verify("content-id: MA-ART-0011" in text, "content-id incorrecto")
verify(re.search(r"^draft:\s*true\s*$", text, re.M), "el derivado debe seguir como draft")
verify("style-standard: MA_STYLE_v1.7" in text, "MA-STYLE no declarado")
verify('resources:\n  - "../assets/articles/ma-art-0011/**"' in text, "recursos MA-ART-0011 no declarados")
verify("Dependencia de publicación de MA-FE-04" in text, "falta bloqueo explícito de F04")
verify("## Aparato visual" not in text, "inventario interno de producción filtrado al derivado público")

iframes = re.findall(r'<iframe[^>]+src="([^"]+)"[^>]+title="([^"]+)"[^>]*>', text)
verify(len(iframes) == 10, f"se esperaban 10 iframes, hay {len(iframes)}")
paths = []
for src, title in iframes:
    verify(title.startswith("MA-FE-"), f"iframe sin título MA-FE: {title}")
    path = (ARTICLE.parent / src).resolve()
    verify(path.is_file() and path.stat().st_size > 0, f"recurso iframe ausente: {src}")
    paths.append(path.name)
verify(paths == EXPECTED, "orden o nombres de activos MA-FE no canónicos")

allowed_remote = "https://nonagon.org/ExLibris/sites/default/files/images/Eulers-Formula-Sect-138.jpg"
for name in EXPECTED:
    path = ASSET_DIR / name
    verify(path.is_file() and path.stat().st_size > 0, f"activo vacío o ausente: {name}")
    html = path.read_text(encoding="utf-8")
    verify(re.search(r'<meta\s+name="viewport"', html, re.I), f"{name}: falta viewport")
    verify(re.search(r"<title>[^<]+</title>", html, re.I), f"{name}: falta title")
    remotes = re.findall(r'(?:src|href)="(https?://[^"]+)"', html, re.I)
    if name == EXPECTED[3]:
        verify(remotes == [allowed_remote], f"F04: dependencia remota inesperada: {remotes}")
        verify(re.search(r'<img[^>]+alt="[^"]+"', html, re.I), "F04: facsímil sin alt")
    else:
        verify(not remotes, f"{name}: dependencia remota no permitida: {remotes}")
        verify('role="img"' in html, f"{name}: SVG sin role=img")

    for script in re.findall(r"<script>(.*?)</script>", html, re.S | re.I):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as fh:
            fh.write(script)
            tmp = Path(fh.name)
        try:
            proc = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
            verify(proc.returncode == 0, f"{name}: JavaScript inválido: {proc.stderr.strip()}")
        finally:
            tmp.unlink(missing_ok=True)

print("Euler MA-ART-0011 static QA OK: qmd + 10 activos; F04 es la única dependencia remota declarada.")
