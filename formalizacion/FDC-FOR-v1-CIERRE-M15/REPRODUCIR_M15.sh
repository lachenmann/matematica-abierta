#!/bin/sh
set -eu
# Run from an external repository clone. Creates an isolated detached worktree.
task_base=0d6b9a9885db62bec8ac07a7ca269d91597e8f56
task_code=390684ab0fce64cb710260fdde321c19cefe3547
task_root=$(git rev-parse --show-toplevel)
task_work=$(mktemp -d "${TMPDIR:-/tmp}/fdc-m15-reproduction.XXXXXX")
git fetch origin "$task_code"
git worktree add --detach "$task_work/code" "$task_code"
cd "$task_work/code"
git diff --name-status "$task_base" "$task_code" > "$task_work/source-diff.txt"
python3 - "$task_work/source-diff.txt" <<'PY'
import sys
from pathlib import Path
expected = {
    "lean/MatematicaAbierta.lean": "M",
    **{"lean/MatematicaAbierta/Continuo/"+n+".lean": "A" for n in [
        "InterpretacionParametricaRCA", "SustitucionSemanticaRCA",
        "AdecuacionLogicaOrdinariaRCA", "AuditoriaGuardaRenombradoRCA",
        "ContratosAdecuacionRCA"]}}
actual = {line.split("\t")[1]: line.split("\t")[0] for line in Path(sys.argv[1]).read_text().splitlines()}
assert actual == expected, (actual, expected)
print("Exact source preservation: only five additions and aggregate modification.")
PY
cd lean
test "$(cat lean-toolchain)" = "leanprover/lean4:v4.34.0"
if rg -n '\b(sorry|admit)\b' MatematicaAbierta.lean MatematicaAbierta; then
  exit 1
fi
lake exe cache get
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = 5ed2965256430c3649e86755f9576b54eca72435
lake build --wfail > "$task_work/lean-build.log" 2>&1
cat "$task_work/lean-build.log"
printf '%s\n' "Reproduction files: $task_work"
# Keep the worktree and logs for inspection; do not delete the original clone.
