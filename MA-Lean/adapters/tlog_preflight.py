"""Validate TLOG preparation data. This does not compile or verify Lean proofs."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate(root: Path, source_root: Path | None = None, inventory=None, units=None):
    profile = json.loads((root / 'MA-Lean/profiles/tlog.json').read_text())
    inventory = inventory if inventory is not None else json.loads((root / 'MA-Lean/mapeos/TLOG/inventory.json').read_text())
    units = units if units is not None else json.loads((root / 'MA-Lean/mapeos/TLOG/units.json').read_text())
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    entries = inventory['entries']
    ids = [e['id'] for e in entries]
    require(len(ids) == len(set(ids)), 'duplicate source IDs')
    require(len(ids) == inventory['human_closed_results'] == 667, 'result count')
    require(set(ids) == set(units), 'unit coverage')
    order = inventory['topological_order']
    require(len(order) == len(ids) and set(order) == set(ids), 'topological coverage')
    positions = {key: i for i, key in enumerate(order)}
    total_edges = 0
    candidates = 0
    require(inventory['compiled'] == inventory['verified'] == 0, 'preparation cannot assert compiled or verified proofs')
    chapters = inventory['chapters']
    require(len(chapters) == 24 and {c['chapter'] for c in chapters} == set(range(24)), 'chapter coverage')
    by_chapter = {c['chapter']: c for c in chapters}
    counts = Counter(e['chapter'] for e in entries)
    for e in entries:
        key = e['id']
        require(bool(re.fullmatch(profile['source_id_pattern'], key)), 'invalid ID: ' + key)
        deps = e['depends_on']
        total_edges += len(deps)
        require(len(deps) == len(set(deps)), 'duplicate edge: ' + key)
        for dep in deps:
            require(dep in positions, 'orphan dependency: ' + key + ' -> ' + dep)
            require(dep in positions and positions.get(dep, len(ids)) < positions.get(key, -1), 'cycle or incorrect order: ' + key + ' -> ' + dep)
        require(e['human_status'] == 'closed', 'human status: ' + key)
        require(e['formal_status'] == 'unmapped' and e['semantic_review'] == 'pending' and e['lean_file'] is None and e['lean_declaration'] is None, 'unearned formal evidence: ' + key)
        require(e['formalization_selection'] in ('candidate', 'not-selected'), 'selection: ' + key)
        candidates += e['formalization_selection'] == 'candidate'
        require({'signature', 'semantic-correspondence', 'axiom-audit'} <= set(e['obligations']), 'missing obligations: ' + key)
        if key in units:
            text = units[key]['text']
            digest = sha(text.encode())
            require(digest == units[key]['sha256'] == e['source']['unit_sha256'], 'unit hash: ' + key)
            require('result-id: ' + key in text, 'unit identity: ' + key)
        c = by_chapter.get(e['chapter'], {})
        require(e['source']['file'] == c.get('source_file') and e['source']['document_sha256'] == c.get('source_sha256'), 'chapter source: ' + key)
        if source_root is not None:
            path = source_root / e['source']['file']
            if path.is_file():
                original = path.read_text()
                unit = original[e['source']['unit_start']:e['source']['unit_end']].rstrip() + '\n'
                require(key in units and unit == units[key]['text'], 'source interval: ' + key)
            else:
                require(False, 'missing source: ' + str(path))
    require(total_edges == inventory['edges'] == 2573, 'edge count')
    require(candidates == inventory['candidates'] == 297, 'candidate count')
    for c in chapters:
        require(counts[c['chapter']] == c['units'], 'chapter result count')
        if source_root is not None:
            path = source_root / c['source_file']
            require(path.is_file() and sha(path.read_bytes()) == c['source_sha256'], 'document hash: ' + c['source_file'])
    require(profile['mode'] == 'preparation-only' and profile['separate_lake_project'] is False, 'profile mode')
    require(profile['lean_root'] == 'lean' and profile['module_root'] == 'MatematicaAbierta.TLOG', 'shared library contract')
    for field, observed in [('toolchain_file', 'toolchain_sha256'), ('manifest', 'manifest_sha256')]:
        path = root / profile[field]
        require(path.is_file() and sha(path.read_bytes()) == profile['observed_environment'][observed], 'environment changed: ' + field)
    return {'preparation_valid': not errors, 'formal_verification': False, 'results': len(ids), 'edges': total_edges, 'candidates': candidates, 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--source-root', type=Path)
    args = parser.parse_args()
    result = validate(args.repo_root, args.source_root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['preparation_valid'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
