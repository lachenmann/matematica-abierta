#!/bin/sh
set -eu
# Run in a separate clone of lachenmann/matematica-abierta; keep logs for review.
task_commit=3e542ee39a9a3103c33d4a1d5a2a74e9359a4a7c
task_root=$(git rev-parse --show-toplevel)
task_out=$(mktemp -d "${TMPDIR:-/tmp}/fdc-m16-reproduction.XXXXXX")
git fetch origin "$task_commit"
git worktree add --detach "$task_out/code" "$task_commit"
cd "$task_out/code/lean"
test "$(cat lean-toolchain)" = "leanprover/lean4:v4.34.0"
lake exe cache get
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = 5ed2965256430c3649e86755f9576b54eca72435
lake build --wfail > "$task_out/build.log" 2>&1
cd ..
python3 formalizacion/FDC-FOR-v1-REPARACION-M16/verify_m16.py > "$task_out/negative-history.log" 2>&1
cat "$task_out/negative-history.log"
printf '%s\n' "M16_REPRODUCTION_PASS: $task_out"
# The worktree and evidence are intentionally retained; no original checkout is changed.
