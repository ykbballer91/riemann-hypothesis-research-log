#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/groskin_compare_assemblies.py
# Original SHA-256: 4a56265d9e26b267d4105aba476d99e6b81b00c4b5b06cf08cb03b9de5e9e8fd
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Replay small independent certificates and compare pinned, inspected v3 code.

Download instructions and provenance: literature/notes/groskin-certificate-audit.md.
The optional comparison executes only the exact previously inspected source hash.
"""
import hashlib
import json
import runpy
from pathlib import Path

from flint import arb, ctx
from groskin_independent_certificate import build, ldlt, serial

root = Path(__file__).resolve().parents[2]
author_path = root/'literature/source_cache/groskin/arxiv-v3/anc/arb_ldlt_certify.py'
source_hash = hashlib.sha256(author_path.read_bytes()).hexdigest()
assert source_hash == 'ea475850cc79b80a2eb33b439435f3602b8d04523ecd3c08312e53ae3a735089'
author = runpy.run_path(str(author_path))
checks = []
for N in (0,1,4):
    M,_,K = build(13,N,192)
    D,_ = ldlt(M)
    A,dim = author['build_arb_tau'](13,N,384)
    containing = sum(M[i][j].contains(A[i,j]) for i in range(dim) for j in range(dim))
    overlaps = sum(M[i][j].overlaps(A[i,j]) for i in range(dim) for j in range(dim))
    L = arb(13).log()
    KK = author['arb_kappa'](L)+author['arb_J'](L)
    assert K.overlaps(KK) and overlaps == dim*dim and all(d>0 for d in D)
    checks.append(dict(c=13,N=N,dimension=dim,positive_pivots=dim,entry_balls_overlap=overlaps,
                       author_balls_contained_in_direct_quadrature_balls=containing,entries=dim*dim,
                       K_identity_overlap=K.overlaps(KK),pivots=[serial(d) for d in D]))
ctx.prec = 192
saved = json.loads((root/'experiments/results/groskin-c13-n4-independent.json').read_text())
M = [[arb(v) for v in row] for row in saved['matrix']]
D,_ = ldlt(M)
assert all(x>0 for x in D)
result = dict(kind='independent_vs_author_assembly_comparison',rh_status='OPEN',proves_RH=False,
              author_script_sha256=source_hash,cases=checks,
              serialized_matrix_replay_positive_pivots=len(D),
              distinction='overlap/containment checks agree; analytic identities need separate derivation')
(root/'experiments/results/groskin-assembly-comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: N=0,1,4; all 91 author entry balls contained; serialized 9x9 matrix certifies positive.')
