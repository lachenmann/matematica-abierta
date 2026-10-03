#!/usr/bin/env python3
"""Adaptador pedagógico MCL para MA-Lean.

No modifica la fuente humana ni concede revisiones semánticas/pedagógicas.
Un build exitoso sólo produce evidencia formal para el commit auditado.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROLES = {"example", "exercise", "productive-error", "generalization", "auxiliary"}
ID = re.compile(r"^MCL-U\d{2}-L\d{2}(?:-E\d{2}|-X\d{2})?$")
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_profile(profile: dict) -> list[str]:
    issues: list[str] = []
    required = {
        "schema_version", "profile_id", "project", "lean_root", "library",
        "module_root", "toolchain_file", "manifest", "workflow",
        "source_kind", "source_id_pattern"
    }
    missing = sorted(required - profile.keys())
    if missing:
        issues.append("Perfil incompleto: " + ", ".join(missing))
    if profile.get("profile_id") != "mcl":
        issues.append("El perfil no es mcl")
    return issues


def validate_mapping(mapping: dict) -> list[str]:
    issues: list[str] = []
    lesson_id = mapping.get("lesson_id", "")
    if not ID.fullmatch(lesson_id):
        issues.append(f"lesson_id inválido: {lesson_id!r}")
    if not isinstance(mapping.get("entries"), list) or not mapping.get("entries"):
        issues.append("El mapeo debe contener entries")
    seen: set[str] = set()
    for entry in mapping.get("entries", []):
        ident = entry.get("id", "")
        if ident in seen:
            issues.append(f"ID duplicado: {ident}")
        seen.add(ident)
        if not ID.fullmatch(ident):
            issues.append(f"ID de entrada inválido: {ident!r}")
        if entry.get("role") not in ROLES:
            issues.append(f"Rol inválido para {ident}: {entry.get('role')!r}")
        if not entry.get("declaration"):
            issues.append(f"Falta declaration para {ident}")
    for item in mapping.get("productive_errors", []):
        ident = item.get("id", "")
        if not ID.fullmatch(ident):
            issues.append(f"ID de error productivo inválido: {ident!r}")
        if item.get("role") != "productive-error":
            issues.append(f"{ident} debe tener rol productive-error")
        if item.get("expected_kernel_result") != "reject":
            issues.append(f"{ident} debe esperar rechazo del kernel")
        if not item.get("code"):
            issues.append(f"{ident} no contiene código")
    return issues


def forbidden_tactics(text: str, names: list[str]) -> list[str]:
    found: list[str] = []
    for name in names:
        if re.search(rf"(?<![A-Za-z0-9_]){re.escape(name)}(?![A-Za-z0-9_])", text):
            found.append(name)
    return sorted(found)


def parse_axioms(output: str, declaration: str) -> tuple[str, list[str]]:
    if "error:" in output.lower() or "sorryAx" in output or declaration not in output:
        return "rejected", []
    if re.search(r"does not depend on any axioms", output, flags=re.I):
        return "parsed", []
    matches = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", output)
    if len(matches) != 1:
        return "unparsed", []
    axioms = [a.strip() for a in matches[0].split(",") if a.strip()]
    return "parsed", axioms


def run(command: list[str], cwd: Path, timeout: int = 900) -> dict:
    try:
        proc = subprocess.run(
            command, cwd=cwd, capture_output=True, text=True,
            timeout=timeout, check=False
        )
        output = (proc.stdout or "") + "\n" + (proc.stderr or "")
        return {"returncode": proc.returncode, "output": output[-20000:]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"returncode": -1, "output": str(exc)}


def audit(
    source: Path,
    mapping_path: Path,
    profile_path: Path,
    repo_root: Path,
    output_path: Path | None = None,
) -> dict:
    profile = read_json(profile_path)
    mapping = read_json(mapping_path)
    issues = validate_profile(profile) + validate_mapping(mapping)

    if not source.is_file():
        issues.append("Fuente humana no disponible")
    expected_sha = mapping.get("source", {}).get("sha256")
    source_sha = digest(source) if source.is_file() else None
    if source_sha and expected_sha != source_sha:
        issues.append("La huella de la fuente humana no coincide con el mapeo")

    lean_rel = mapping.get("lean", {}).get("file", "")
    lean_file = repo_root / lean_rel
    lean_text = lean_file.read_text(encoding="utf-8") if lean_file.is_file() else ""
    if not lean_file.is_file():
        issues.append(f"Módulo Lean ausente: {lean_rel}")

    lesson_id = mapping.get("lesson_id", "")
    if lean_text and lesson_id not in lean_text:
        issues.append("El módulo Lean no contiene el ID de la lección")

    forbidden = mapping.get("pedagogical_policy", {}).get("forbidden_tactics", [])
    bad_tactics = forbidden_tactics(lean_text, forbidden) if lean_text else []
    if bad_tactics:
        issues.append("Tácticas prohibidas en solución canónica: " + ", ".join(bad_tactics))

    lean_root = repo_root / profile.get("lean_root", "lean")
    lake = shutil.which("lake")
    build = {"status": "not_run", "returncode": None, "log_tail": ""}
    results: list[dict] = []
    productive_errors: list[dict] = []

    if lake is None:
        issues.append("Lake no está disponible en PATH")
    elif not issues:
        built = run([lake, "build", "--wfail"], lean_root, timeout=1200)
        build = {
            "status": "pass" if built["returncode"] == 0 else "failed",
            "returncode": built["returncode"],
            "log_tail": built["output"],
        }
        if built["returncode"] != 0:
            issues.append("Falló lake build --wfail")

    module = mapping.get("lean", {}).get("module")
    if lake is not None and build["status"] == "pass":
        for entry in mapping.get("entries", []):
            declaration = entry["declaration"]
            with tempfile.TemporaryDirectory() as tmp:
                check = Path(tmp) / "MCLAudit.lean"
                check.write_text(
                    f"import {module}\n#check {declaration}\n#print axioms {declaration}\n",
                    encoding="utf-8",
                )
                tested = run([lake, "env", "lean", str(check)], lean_root, timeout=180)
            parsed, axioms = parse_axioms(tested["output"], declaration)
            formal_verified = (
                tested["returncode"] == 0
                and parsed == "parsed"
                and set(axioms) <= ALLOWED_AXIOMS
            )
            results.append({
                "id": entry["id"],
                "role": entry["role"],
                "declaration": declaration,
                "formal_verified": formal_verified,
                "axioms": axioms,
                "semantic_reviewed": entry.get("semantic_review") == "approved",
                "pedagogical_reviewed": entry.get("pedagogical_review") == "approved",
                "lean_output_tail": tested["output"][-3000:],
            })

        for item in mapping.get("productive_errors", []):
            with tempfile.TemporaryDirectory() as tmp:
                check = Path(tmp) / "MCLExpectedFailure.lean"
                check.write_text(
                    f"import {module}\n\n{item['code']}",
                    encoding="utf-8",
                )
                tested = run([lake, "env", "lean", str(check)], lean_root, timeout=180)
            rejected = tested["returncode"] != 0
            productive_errors.append({
                "id": item["id"],
                "kernel_rejected": rejected,
                "expected": "reject",
                "lean_output_tail": tested["output"][-3000:],
            })
            if not rejected:
                issues.append(f"{item['id']} debía ser rechazado por Lean")

    formal_pass = (
        build["status"] == "pass"
        and bool(results)
        and all(r["formal_verified"] for r in results)
        and all(x["kernel_rejected"] for x in productive_errors)
        and not issues
    )
    semantic_pass = bool(results) and all(r["semantic_reviewed"] for r in results)
    pedagogical_pass = bool(results) and all(r["pedagogical_reviewed"] for r in results)

    report = {
        "schema_version": "1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "profile": profile.get("profile_id"),
        "lesson_id": lesson_id,
        "source_sha256": source_sha,
        "lean_file": lean_rel,
        "build": build,
        "results": results,
        "productive_errors": productive_errors,
        "formal_pass": formal_pass,
        "semantic_pass": semantic_pass,
        "pedagogical_pass": pedagogical_pass,
        "closed": formal_pass and semantic_pass and pedagogical_pass,
        "issues": issues,
        "note": "lean-pass no concede por sí solo revisión semántica ni pedagógica.",
    }
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Adaptador MCL para MA-Lean")
    sub = parser.add_subparsers(dest="command", required=True)
    cmd = sub.add_parser("audit")
    cmd.add_argument("--source", required=True, type=Path)
    cmd.add_argument("--mapping", required=True, type=Path)
    cmd.add_argument("--profile", required=True, type=Path)
    cmd.add_argument("--repo-root", required=True, type=Path)
    cmd.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    report = audit(
        args.source, args.mapping, args.profile, args.repo_root, args.output
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["formal_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
