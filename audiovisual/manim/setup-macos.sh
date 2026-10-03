#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [ -d /Library/TeX/texbin ]; then
  export PATH="/Library/TeX/texbin:$PATH"
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "Instalando uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

if ! command -v brew >/dev/null 2>&1; then
  echo "Falta Homebrew. Instálalo desde https://brew.sh y vuelve a ejecutar este script."
  exit 2
fi

for pkg in cairo pkg-config; do
  if ! brew list --versions "$pkg" >/dev/null 2>&1; then
    brew install "$pkg"
  fi
done

if ! command -v xelatex >/dev/null 2>&1 || ! command -v dvisvgm >/dev/null 2>&1; then
  echo "Falta la cadena TeX. Instala MacTeX y asegúrate de que /Library/TeX/texbin esté disponible."
  exit 3
fi

uv python install 3.13.15
uv sync
uv run python verify_environment.py

echo
echo "Entorno MA-Manim listo en macOS."
echo "Render de prueba:"
echo "  uv run manim -pql ma_cls_c13_p01/scene.py MAVizC13RiemannRefinement"
