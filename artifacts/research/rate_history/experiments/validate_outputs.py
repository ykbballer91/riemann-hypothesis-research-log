# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/rate_history/experiments/validate_outputs.py
# Original SHA-256: 7e6cfaeab9a054239ae46a1b55433b8d9cf4e3c2a3df9b6c38522695508f5e34
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Validate preservation and saved diagnostics; does not certify numerics or RH."""
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
from datetime import datetime, timezone

import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
TASK = ROOT / "research/rate_history"
mp.mp.dps = 80


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


baseline = json.loads((TASK / "preservation_baseline.json").read_text())
changed = [p for p, h in baseline["sha256"].items()
           if not (ROOT / p).is_file() or digest(ROOT / p) != h]
head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
assert not changed and head == baseline["head"], (changed, head)

required = [
    "research/rate_history_selection.md",
    "research/radical_degeneracy_lifting.md",
    "research/ground_state_trajectory.md",
    "research/rate_history_candidate_matrix.md",
    "proofs/audits/rate_history_selection_adversarial.md",
    "research/rate_history_state.json",
]
assert all((ROOT / p).is_file() for p in required)
artifacts = sorted(set([ROOT / p for p in required]
                       + [p for p in TASK.rglob("*") if p.is_file()]))
json_files, python_files, markdown_files = [], [], []
bad_links, bad_math, bad_controls = [], [], []
for p in artifacts:
    if p.suffix == ".json":
        json.loads(p.read_text())
        json_files.append(str(p.relative_to(ROOT)))
    elif p.suffix == ".py":
        ast.parse(p.read_text(), filename=str(p))
        python_files.append(str(p.relative_to(ROOT)))
    if p.suffix in (".md", ".txt", ".py", ".json"):
        s = p.read_text()
        if any(ord(c) < 32 and c not in "\n\r\t" for c in s):
            bad_controls.append(str(p.relative_to(ROOT)))
    if p.suffix == ".md":
        markdown_files.append(str(p.relative_to(ROOT)))
        if s.count(r"\[") != s.count(r"\]"):
            bad_math.append(str(p.relative_to(ROOT)))
        for target in re.findall(r"\]\(([^\s)]+)\)", s):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            target = target.split("#")[0]
            if not (p.parent / target).exists():
                bad_links.append([str(p.relative_to(ROOT)), target])
assert not bad_links and not bad_math and not bad_controls, (bad_links, bad_math, bad_controls)

data = json.loads((TASK / "experiments/splitting_results.json").read_text())
cases = data["cases"]
assert len(cases) == 11 and sum(len(c["restricted"]) for c in cases) == 33
max_rounded_residual = mp.mpf(0)
max_rounded_unit_error = mp.mpf(0)
for c in cases:
    for r in c["restricted"]:
        d = r["m"] + 1
        M = mp.matrix([[mp.mpf(c["M_normalized_columns"][i][j]) for j in range(d)] for i in range(d)])
        G = mp.matrix([[mp.mpf(c["G_normalized_columns"][i][j]) for j in range(d)] for i in range(d)])
        v = mp.matrix([mp.mpf(x) for x in r["selected_column_coefficients"]])
        eigenvalues = list(map(mp.mpf, r["eigenvalues"]))
        assert eigenvalues == sorted(eigenvalues)
        residual = mp.norm(M*v-eigenvalues[0]*G*v) / max(mp.mpf(1), mp.norm(M)*mp.norm(v))
        unit_error = abs((v.T*G*v)[0]-1)
        max_rounded_residual = max(max_rounded_residual, residual)
        max_rounded_unit_error = max(max_rounded_unit_error, unit_error)
assert max_rounded_residual < mp.mpf("1e-40")
assert max_rounded_unit_error < mp.mpf("1e-39")

state = json.loads((ROOT / "research/rate_history_state.json").read_text())
assert state["rh_status"] == "OPEN" and state["rh_closed"] is False
assert state["G_star_proved"] is False and state["proof_graph_merged"] is False
assert state["support_only_R1_lowest_direction_selection_proved"] is True
assert state["rate_selected_direction_found"] is False

audit_text = (ROOT / required[4]).read_text()
audit_hashes = re.findall(r"\|((?:research|proofs)/[^|]+)\|([0-9a-f]{64})\|", audit_text)
assert len(audit_hashes) == 15
audit_mismatches = [p for p, h in audit_hashes if digest(ROOT / p) != h]
assert not audit_mismatches, audit_mismatches

result = {
    "time_utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS",
    "rh_status": "OPEN",
    "baseline_files_checked": len(baseline["sha256"]),
    "baseline_files_changed": changed,
    "head_unchanged": head == baseline["head"],
    "head": head,
    "required_deliverables_present": required,
    "json_syntax_checked": json_files,
    "python_ast_checked_without_execution": python_files,
    "markdown_checked": markdown_files,
    "broken_local_links": bad_links,
    "unbalanced_display_math": bad_math,
    "control_characters": bad_controls,
    "finite_endpoints": 11,
    "restricted_generalized_problems": 33,
    "saved_rounded_matrix_max_generalized_residual": mp.nstr(max_rounded_residual, 12),
    "saved_rounded_matrix_max_unit_error": mp.nstr(max_rounded_unit_error, 12),
    "independent_audited_artifact_hashes_matched": len(audit_hashes),
    "artifact_sha256": {str(p.relative_to(ROOT)): digest(p) for p in artifacts
                        if p.name != "validation.json"},
    "scope": "Preservation, artifact syntax, saved numerical consistency and matching independent audit snapshot. Not an interval certificate, formal proof, external literature re-audit, or RH proof. Support-only R1 selection is distinct from unproved full canonical selection.",
}
(TASK / "validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: result[k] for k in (
    "status", "baseline_files_checked", "baseline_files_changed", "head_unchanged",
    "finite_endpoints", "restricted_generalized_problems",
    "saved_rounded_matrix_max_generalized_residual", "saved_rounded_matrix_max_unit_error",
    "independent_audited_artifact_hashes_matched")}, indent=2))
