# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/hierarchical_selection/experiments/check_actual_resolution.py
# Original SHA-256: 076ab9c0e3f547bb3d5be39d747d60e7b5ce24e6308f6599fdbb3f25e8f8bf2d
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""One small actual cutoff, several resolutions, restricted matrices only.

Arb midpoints and mpmath quadrature: diagnostic, not interval-certified.
No full-ground diagonalization or large-parameter fit is performed.
"""
from pathlib import Path
import sys, json, importlib.util
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("old_splitting_readonly", ROOT / "research/rate_history/experiments/splitting_probe.py")
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
mp = old.mp
mp.mp.dps = 100
cut, maxN = 9, 40
balls, _, _ = old.build(cut, maxN, 448)
Q = mp.matrix([[old.midpoint(x) for x in row] for row in balls])
B, _ = old.columns(cut, maxN, 256)
Blo, _ = old.columns(cut, maxN, 192)
Gglobal, _ = old.global_gram()
records = []
a = mp.log(cut)/2; Y = mp.pi*cut
for N in (4, 8, 12, 20, 40):
    sl = slice(maxN-N,maxN+N+1)
    q = Q[sl,sl]; b = B[sl,:]
    M = b.T*q*b; G = b.T*b
    item = {"lambda":3, "N":N, "h":old.val(mp.pi*N/(2*a*Y)),
            "k_score_unit":old.val(M[0,0]/G[0,0]), "restricted":[]}
    for m in (1,2,3):
        g = G[:m+1,:m+1]; mat = M[:m+1,:m+1]
        Li = mp.cholesky(g)**-1
        eig,U = mp.eigsy(Li*mat*Li.T)
        c = Li.T*U[:,0]
        if c[0] < 0: c = -c
        c /= c[0]
        item["restricted"].append({"m":m,"eigenvalues":[old.val(x) for x in eig],
            "raw_coefficients_leading_one":[old.val(x) for x in c],
            "hierarchical_prediction":[old.val((-1)**j*mp.binomial(m,j)/(4**j*Y**(2*j))) for j in range(m+1)]})
    records.append(item)
    print("N",N,"h",mp.nstr(mp.pi*N/(2*a*Y),6),"m1 coefficient",item["restricted"][0]["raw_coefficients_leading_one"][1],flush=True)
result = {"rh_status":"OPEN", "scope":"One actual small cutoff; finite diagnostic only, not proof of an asymptotic rate or target zero match.",
          "matrix_bits":448,"digits":100,"column_quadrature_change_192_to_256":old.val(mp.norm(B-Blo)),
          "cases":records}
Path(__file__).with_name("actual_resolution_results.json").write_text(json.dumps(result,indent=2)+'\n')
