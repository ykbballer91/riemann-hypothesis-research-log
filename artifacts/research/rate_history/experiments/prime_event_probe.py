# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/rate_history/experiments/prime_event_probe.py
# Original SHA-256: 6ab41fd1f67a94862beef409e3785696fc37c61457616071f28ebf198d976f44
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Diagnostic only for the proved prime-power derivative corner."""
from pathlib import Path
import sys,json,math
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/common_parent/experiments'))
from rayleigh_probe import weil
import numpy as np
out=[]
for n,p,k in ((8,2,3),(9,3,2),(25,5,2)):
    h=math.log(n);N=3
    Q0,_=weil(float(n),N,512)
    target=-2*math.log(p)/(math.sqrt(n)*h)*np.ones((2*N+1,2*N+1))
    for eps in (1e-2,1e-3,1e-4):
        Qp,_=weil(math.exp(h+eps),N,512)
        Qm,_=weil(math.exp(h-eps),N,512)
        corner=(Qp-2*Q0+Qm)/eps
        out.append({'n':n,'k':k,'epsilon_L':eps,
         'max_error_to_rank_one_derivative_jump':float(np.max(abs(corner-target)))})
Path(__file__).with_name('prime_event_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
