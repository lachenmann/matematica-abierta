#!/usr/bin/env bash
set -euo pipefail

if ! command -v elan >/dev/null 2>&1 && [[ ! -x "$HOME/.elan/bin/elan" ]]; then
  curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
    | sh -s -- -y --default-toolchain none
fi

export PATH="$HOME/.elan/bin:$PATH"
cd lean
# Lake utiliza lake-manifest.json para instalar las revisiones fijadas.
lake exe cache get
lake build
