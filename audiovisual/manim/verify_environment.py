from __future__ import annotations

import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXPECTED_MANIM = "0.21.0"
EXPECTED_PYTHON = (3, 13)


def fail(message: str) -> None:
    raise SystemExit(f"[FAIL] {message}")


if sys.version_info[:2] != EXPECTED_PYTHON:
    fail(
        f"Python {EXPECTED_PYTHON[0]}.{EXPECTED_PYTHON[1]} esperado; "
        f"se está usando {platform.python_version()}."
    )

try:
    import manim
except Exception as exc:
    fail(f"No se pudo importar Manim: {exc}")

if manim.__version__ != EXPECTED_MANIM:
    fail(f"Manim {EXPECTED_MANIM} esperado; se encontró {manim.__version__}.")

for exe in ("xelatex", "dvisvgm"):
    path = shutil.which(exe)
    if not path:
        fail(f"No se encontró {exe} en PATH.")
    print(f"[OK] {exe}: {path}")

scene = r"""
from manim import *

TEX = TexTemplate(tex_compiler="xelatex", output_format=".xdv")

class VerifyMA(Scene):
    def construct(self):
        formula = MathTex(
            r"\int_0^1 x^2\,dx=\frac{1}{3}",
            tex_template=TEX,
        )
        self.add(formula)
"""

with tempfile.TemporaryDirectory(prefix="ma-manim-verify-") as tmp:
    tmp_path = Path(tmp)
    scene_path = tmp_path / "verify_scene.py"
    scene_path.write_text(scene, encoding="utf-8")

    cmd = [
        sys.executable,
        "-m",
        "manim",
        "-ql",
        "--disable_caching",
        str(scene_path),
        "VerifyMA",
    ]
    result = subprocess.run(
        cmd,
        cwd=tmp,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        fail("Falló el render mínimo MathTex → vídeo.")

print(f"[OK] Python {platform.python_version()}")
print(f"[OK] Manim Community {manim.__version__}")
print("[OK] MathTex con XeLaTeX/XDV")
print("[OK] Render mínimo de vídeo")
print("[PASS] Entorno MA-Manim operativo.")
