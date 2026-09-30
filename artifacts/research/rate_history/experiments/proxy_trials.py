# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/rate_history/experiments/proxy_trials.py
# Original SHA-256: 622d3db94923a4f66465a29d94890099f8e55c7c784eae04f6a6e88376dc45d2
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Read-only reuse of existing actual prolate construction for comparison."""
from pathlib import Path
import sys,json,math
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/common_parent/experiments'))
from rayleigh_probe import proxy_samples
import numpy as np
out=[]
for cut in (9,25,49,81,121,169):
    a=math.log(cut)/2
    ns=sorted(set((max(4,math.ceil(a*a)),max(4,math.ceil(a*a*a)))))
    values={}
    for degree,quad in ((192,32),(256,48)):
        t,w,k,norm2,diag=proxy_samples(cut,degree,quad)
        for N in ns:
            inds=np.arange(-N,N+1)
            basis=np.exp(-1j*math.pi*inds[:,None]*(t[None,:]+a)/a)/math.sqrt(2*a)
            coef=basis@(w*k);coef/=np.linalg.norm(coef)
            values[degree,N]=(coef,diag)
    for N in ns:
        c,diag=values[256,N];lo,_=values[192,N]
        overlap=abs(np.vdot(c,lo));change=math.sqrt(max(0,2*(1-overlap)))
        out.append({'cut':cut,'N':N,'coefficients':[[float(z.real),float(z.imag)] for z in c],
          'resolution_projective_distance':change,'diagnostics':diag,
          'scope':'Floating-point projected proxy comparison only, not certified.'})
        print(cut,N,'proxy resolution distance',change,flush=True)
Path(__file__).with_name('prolate_trials.json').write_text(json.dumps(out,indent=2)+'\n')
