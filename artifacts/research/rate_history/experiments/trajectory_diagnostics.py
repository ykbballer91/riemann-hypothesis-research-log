# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/rate_history/experiments/trajectory_diagnostics.py
# Original SHA-256: 69ad74d2fbae7e6a0e85bebd1333a726d5978e34cd613bd8bf898bc9cff2a9f4
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Projective comparisons in the original log-space, no branch relabeling."""
from pathlib import Path
import json,mpmath as mp
mp.mp.dps=70
HERE=Path(__file__).parent
data=json.loads((HERE/'splitting_results.json').read_text())
cases=data['cases'];G=mp.matrix([[mp.mpf(x) for x in row] for row in data['global_gram_derivatives']])
def out(x): return mp.nstr(x,35)
def ground_overlap(c,d):
    a,b=mp.mpf(c['a']),mp.mpf(d['a']);L=min(a,b)
    v=[mp.mpf(x) for x in c['ground_coefficients']]
    w=[mp.mpf(x) for x in d['ground_coefficients']]
    total=mp.mpf(0)
    for j,x in enumerate(v):
        n=j-c['N']
        for k,y in enumerate(w):
            m=k-d['N'];omega=mp.pi*n/a-mp.pi*m/b
            integ=2*L if abs(omega)<mp.mpf('1e-60') else 2*mp.sin(omega*L)/omega
            total+=x*y*(-1)**(n-m)*integ/(2*mp.sqrt(a*b))
    return total**2
def radical_overlap(c,d,m):
    v=mp.matrix([mp.mpf(x) for x in c['restricted'][m-1]['selected_global_derivative_coefficients']])
    w=mp.matrix([mp.mpf(x) for x in d['restricted'][m-1]['selected_global_derivative_coefficients']])
    return (v.T*G*w)[0]**2/((v.T*G*v)[0]*(w.T*G*w)[0])
samecut=[]
for cut in sorted(set(c['cut'] for c in cases)):
    cc=[c for c in cases if c['cut']==cut]
    if len(cc)==2:
        c,d=cc
        samecut.append({'cut':cut,'Ns':[c['N'],d['N']],
           'ground_overlap_squared':out(ground_overlap(c,d)),
           'radical_m3_global_overlap_squared':out(radical_overlap(c,d,3))})
paths={}
for path in ('quadratic','cubic'):
    seq=[c for c in cases if path in c['paths']]
    paths[path]=[{'from':[c['cut'],c['N']],'to':[d['cut'],d['N']],
        'ground_overlap_squared':out(ground_overlap(c,d)),
        'radical_m3_global_overlap_squared':out(radical_overlap(c,d,3))}
        for c,d in zip(seq[:-1],seq[1:])]
result={'rh_status':'OPEN','same_cutoff_different_N':samecut,'successive_path_points':paths,
 'scope':'Different finite endpoints can have different states. These finite prefixes prove neither distinct path limits nor history dependence at the same endpoint. Ground projectors compared via zero extension in the original real log coordinate.'}
(HERE/'trajectory_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
