#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/window_half_crosscheck.py
# Original SHA-256: 28dd67d1240e50b2e38eb9f10bfa5b76535887b7b4cfd112b812c8b486aa2a93
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Independent adaptive-integral entry checks and saved-matrix LDL replay."""
import json
from pathlib import Path
from flint import arb,acb,ctx
from groskin_independent_certificate import ldlt,serial
from window_half_certificate import dfact

ctx.prec=256
root=Path(__file__).resolve().parents[2]
data=json.loads((root/'experiments/results/window-half-T32-cut64.json').read_text())
a,T,pi,I=arb(1)/2,arb(32),arb.pi(),acb(0,1)
A=2*arb(2).log()/arb(2).sqrt()
beta=(T/(2*pi)).log()-1/T-A
tol=arb(2)**(-192)
checks=[]

def amp(n,z):
    x=a*z
    return (-1)**(n//2)*arb(2*n+1).sqrt()*x**n/dfact(n)*(-x*x/4).hypgeom_0f1(arb(n)+arb(3)/2)

def pole(n):
    x=a/2
    return arb(2*n+1).sqrt()*x**n/dfact(n)*(x*x/4).hypgeom_0f1(arb(n)+arb(3)/2)

for n,m in [(0,0),(0,2),(1,1),(1,3),(62,62)]:
    def integrand(t,_):
        h=((acb(arb(1)/4)+I*t/2).digamma()+(acb(arb(1)/4)-I*t/2).digamma())/2-pi.log()
        return (h-A*(t*arb(2).log()).cos()-beta)*amp(n,t)*amp(m,t)/pi
    z=acb.integral(integrand,0,T,abs_tol=tol,rel_tol=tol,eval_limit=300000)
    assert z.is_finite() and z.imag.contains(0)
    value=z.real+(-1)**(n%2)*2*pole(n)*pole(m)+(beta if n==m else 0)
    enclosure=arb(data['sectors'][n%2]['head'][n//2][m//2])
    assert enclosure.overlaps(value)
    checks.append(dict(n=n,m=m,adaptive_integral=serial(value),
                       contained=enclosure.contains(value),overlap=enclosure.overlaps(value)))
    print(n,m,'contained',enclosure.contains(value),flush=True)

for sector in data['sectors']:
    H=[[arb(x) for x in row] for row in sector['head']]
    shift=arb('1e-7')
    M=[[H[i][j]-(shift if i==j else 0) for j in range(len(H))] for i in range(len(H))]
    pivots,_=ldlt(M)
    assert all(d>0 for d in pivots)
result=dict(rh_status='OPEN',proves_RH=False,independent_adaptive_entry_checks=checks,
            serialized_matrix_shift_replay={'even':32,'odd':32},
            note='All five integral balls contained in original Gauss-error enclosures.'
                 if all(x['contained'] for x in checks) else 'Overlaps only; inspect widths.')
(root/'experiments/results/window-half-crosscheck.json').write_text(json.dumps(result,indent=2)+'\n')
print('Both saved parity blocks certify the exact 1e-7 shift.')
