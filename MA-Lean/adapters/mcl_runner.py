#!/usr/bin/env python3
"""Runner local/CI para ejercicios MCL.

El runner distingue aceptación del kernel de aceptación pedagógica.
No es todavía un servicio web seguro: código de estudiantes no confiable debe
ejecutarse en un sandbox aislado con límites de CPU, memoria, tiempo y red.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def find_exercise(spec: dict, exercise_id: str) -> dict:
    matches = [x for x in spec.get("exercises", []) if x.get("id") == exercise_id]
    if len(matches) != 1:
        raise ValueError(f"Exercise id must resolve uniquely: {exercise_id}")
    return matches[0]


def tactic_heads(solution: str) -> list[str]:
    heads: list[str] = []
    for raw in solution.splitlines():
        line = raw.split("--", 1)[0].strip()
        if not line:
            continue
        match = re.match(r"([A-Za-z_][A-Za-z0-9_']*)", line)
        if match:
            heads.append(match.group(1))
    return heads


def policy_check(solution: str, exercise: dict, security: dict) -> dict:
    reasons: list[str] = []
    if not solution.strip():
        reasons.append("empty_submission")
    max_chars = int(security.get("max_submission_chars", 2000))
    if len(solution) > max_chars:
        reasons.append("submission_too_long")

    lower = solution.lower()
    for item in security.get("forbidden_constructs", []):
        token = str(item)
        if token == "#":
            if "#" in solution:
                reasons.append("forbidden_construct:#")
        elif re.search(rf"(?<![A-Za-z0-9_]){re.escape(token.lower())}(?![A-Za-z0-9_])", lower):
            reasons.append(f"forbidden_construct:{token}")

    forbidden = exercise.get("forbidden_tactics", [])
    for tactic in forbidden:
        if re.search(rf"(?<![A-Za-z0-9_]){re.escape(tactic)}(?![A-Za-z0-9_])", solution):
            reasons.append(f"forbidden_tactic:{tactic}")

    allowed = set(exercise.get("allowed_tactics", []))
    heads = tactic_heads(solution)
    if allowed:
        unexpected = sorted({x for x in heads if x not in allowed})
        reasons.extend(f"tactic_not_introduced:{x}" for x in unexpected)

    return {
        "accepts": not reasons,
        "reasons": sorted(set(reasons)),
        "tactic_heads": heads,
    }


def render_submission(module: str, exercise: dict, solution: str) -> str:
    indented = "\n".join("  " + line for line in solution.splitlines())
    return f"import {module}\n\n{exercise['theorem_prefix']}\n{indented}\n"


def run_lean(lean_root: Path, source: str, timeout_seconds: int) -> dict:
    lake = shutil.which("lake")
    if lake is None:
        return {"status":"infrastructure_error","returncode":-1,"diagnostic":"lake_not_found"}
    with tempfile.TemporaryDirectory() as tmp:
        path=Path(tmp)/"MCLStudentSubmission.lean"
        path.write_text(source,encoding="utf-8")
        try:
            proc=subprocess.run(
                [lake,"env","lean",str(path)],
                cwd=lean_root,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                check=False
            )
            output=((proc.stdout or "")+"\n"+(proc.stderr or ""))[-8000:]
            return {
                "status":"accepted" if proc.returncode==0 else "rejected",
                "returncode":proc.returncode,
                "diagnostic":output
            }
        except subprocess.TimeoutExpired:
            return {"status":"timeout","returncode":-1,"diagnostic":"timeout"}
        except OSError as exc:
            return {"status":"infrastructure_error","returncode":-1,"diagnostic":str(exc)}


def evaluate(spec: dict, exercise_id: str, solution: str, lean_root: Path, timeout_seconds: int=15) -> dict:
    exercise=find_exercise(spec,exercise_id)
    security=dict(spec.get("security",{}))
    security["max_submission_chars"]=spec.get("max_submission_chars",2000)
    policy=policy_check(solution,exercise,security)
    source=render_submission(spec["module"],exercise,solution)
    kernel=run_lean(lean_root,source,timeout_seconds)
    kernel_accepts=kernel["status"]=="accepted"
    pedagogical_policy_accepts=policy["accepts"]
    if kernel["status"] in {"timeout","infrastructure_error"}:
        outcome="infrastructure_error"
    elif kernel_accepts and pedagogical_policy_accepts:
        outcome="accepted"
    elif kernel_accepts and not pedagogical_policy_accepts:
        outcome="kernel_correct_policy_rejected"
    else:
        outcome="kernel_rejected"
    return {
        "schema_version":"1",
        "exercise_id":exercise_id,
        "kernel_accepts":kernel_accepts,
        "pedagogical_policy_accepts":pedagogical_policy_accepts,
        "outcome":outcome,
        "policy":policy,
        "kernel_status":kernel["status"],
        "diagnostic":kernel["diagnostic"]
    }


def main(argv: list[str] | None=None) -> int:
    p=argparse.ArgumentParser(description="MCL student exercise runner")
    p.add_argument("--spec",required=True,type=Path)
    p.add_argument("--exercise",required=True)
    p.add_argument("--solution-file",required=True,type=Path)
    p.add_argument("--lean-root",required=True,type=Path)
    p.add_argument("--timeout",type=int,default=15)
    args=p.parse_args(argv)
    spec=read_json(args.spec)
    solution=args.solution_file.read_text(encoding="utf-8")
    result=evaluate(spec,args.exercise,solution,args.lean_root,args.timeout)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result["outcome"]=="accepted" else 2


if __name__=="__main__":
    raise SystemExit(main())
