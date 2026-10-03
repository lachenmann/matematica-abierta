#!/usr/bin/env python3
"""Auditoría formal MCL para CI.

No requiere acceso a Obsidian. Verifica únicamente la contraparte Lean ya
mapeada. La huella de la fuente humana se audita por separado.
"""
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from adapters.mcl import (
    ALLOWED_AXIOMS,
    forbidden_tactics,
    parse_axioms,
    read_json,
    run,
    validate_mapping,
    validate_profile,
)


def formal_audit(
    mapping_path: Path,
    profile_path: Path,
    repo_root: Path,
    output_path: Path | None = None,
) -> dict:
    profile = read_json(profile_path)
    mapping = read_json(mapping_path)
    issues = validate_profile(profile) + validate_mapping(mapping)

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
                check = Path(tmp) / "MCLFormalAudit.lean"
                check.write_text(
                    f"import {module}\n#check {declaration}\n#print axioms {declaration}\n",
                    encoding="utf-8",
                )
                tested = run([lake, "env", "lean", str(check)], lean_root, timeout=180)
            parsed, axioms = parse_axioms(tested["output"], declaration)
            verified = (
                tested["returncode"] == 0
                and parsed == "parsed"
                and set(axioms) <= ALLOWED_AXIOMS
            )
            results.append({
                "id": entry["id"],
                "declaration": declaration,
                "formal_verified": verified,
                "axioms": axioms,
                "lean_output_tail": tested["output"][-3000:],
            })
            if not verified:
                issues.append(f"No se verificó formalmente {entry['id']}")

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

    report = {
        "schema_version": "1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "profile": profile.get("profile_id"),
        "lesson_id": lesson_id,
        "source_sha256_expected": mapping.get("source", {}).get("sha256"),
        "lean_file": lean_rel,
        "build": build,
        "results": results,
        "productive_errors": productive_errors,
        "formal_pass": formal_pass,
        "issues": issues,
        "note": "PASS formal no concede revisión semántica ni pedagógica.",
    }
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Auditoría formal MCL")
    parser.add_argument("--mapping", required=True, type=Path)
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    report = formal_audit(
        args.mapping, args.profile, args.repo_root, args.output
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["formal_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
