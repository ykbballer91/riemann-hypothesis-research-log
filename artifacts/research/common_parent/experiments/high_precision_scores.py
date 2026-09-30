# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/common_parent/experiments/high_precision_scores.py
# Original SHA-256: 01fda43df351f0d40340eb1f3438a0deff9d687de867ef8f2c53aba95c8810f8
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Recheck selected Step31 gaps using Arb-assembled matrices and mpmath.

The trial coefficients remain the floating-point Legendre/quadrature
approximation to the actual proxy. Arb matrix midpoints are passed to
mpmath, so this is NOT an interval certificate for eigenvalues, gaps,
scores, the actual proxy, or its eigenvector overlap.
"""
from pathlib import Path
import sys, json, re
sys.dont_write_bytecode = True
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'experiments/scripts'))
from groskin_independent_certificate import build
import mpmath as mp

mp.mp.dps=75
HERE=Path(__file__).parent
data=json.loads((HERE/'rayleigh_results.json').read_text())
num_re=re.compile(r'[-+]?\d+(?:\.\d*)?(?:e[-+]?\d+)?')
def num(s):
    return mp.mpf(num_re.search(s).group())
def out(x):
    return mp.nstr(x,35)

selected={(2,4),(3,4),(5,4),(5,8),(9,4),(9,8),(13,4),(13,8),(25,4)}
records=[]
for case in data['cases']:
    cut,N=case['prime_power_cutoff'],case['N']
    if (cut,N) not in selected:
        continue
    balls,_,_=build(cut,N,288)
    strs=[[x.str(90,more=True) for x in row] for row in balls]
    Q=mp.matrix([[num(s) for s in row] for row in strs])
    e,U=mp.eigh(Q)
    b=mp.matrix([mp.mpc(str(z[0]),str(z[1])) for z in case['unit_trial_coefficients']])
    b/=mp.sqrt(mp.re((b.H*b)[0]))
    R=mp.re((b.H*Q*b)[0]); gap=e[1]-e[0]; exc=R-e[0]
    amp=U.H*b
    exc2=sum((e[j]-e[0])*abs(amp[j])**2 for j in range(len(e)))
    assert abs(exc-exc2)<mp.mpf('1e-65')
    assert gap>0
    dist=1-abs(amp[0])**2
    assert dist<=exc/gap+mp.mpf('1e-60')
    # Even and odd compressed sectors, with real antisymmetric basis sufficient.
    Pe=mp.matrix(2*N+1,N+1); Pe[N,0]=1
    Po=mp.matrix(2*N+1,N)
    for j in range(1,N+1):
        Pe[N-j,j]=Pe[N+j,j]=1/mp.sqrt(2)
        Po[N-j,j-1]=1/mp.sqrt(2); Po[N+j,j-1]=-1/mp.sqrt(2)
    ee=mp.eigsy(Pe.T*Q*Pe,eigvals_only=True)
    eo=mp.eigsy(Po.T*Q*Po,eigvals_only=True)
    er=max(abs((Q*U-U*mp.diag(e))[i,j]) for i in range(len(e)) for j in range(len(e)))
    rec={'prime_power_cutoff':cut,'lambda':case['lambda'],'N':N,
      'lambda_0':out(e[0]),'lambda_1':out(e[1]),'gap':out(gap),
      'R_B_rounded_trial':out(R),'energy_excess_rounded_trial':out(exc),
      'excess_over_gap_rounded_trial':out(exc/gap),
      'ground_overlap_squared_rounded_trial':out(abs(amp[0])**2),
      'squared_distance_to_ground_line':out(dist),
      'residual_norm_rounded_trial':out(mp.norm(Q*b-R*b)),
      'even_ground':out(ee[0]),'odd_ground':out(eo[0]),
      'eigenbasis_residual_max':out(er),
      'floating_proxy_resolution_R_change':case['resolution_changes']['R_B'],
      'floating_proxy_projection_relative_tail':case['projection_relative_L2_tail']}
    records.append(rec)
    print(cut,N,'e0',out(e[0]),'gap',out(gap),'ratio',out(exc/gap),
          'overlap',out(abs(amp[0])**2),flush=True)

result={'rh_status':'OPEN','kind':'HIGH_PRECISION_DIAGNOSTIC_NOT_PROXY_CERTIFICATE',
  'matrix_assembly':'existing independent Arb build, 288 bits, read-only imported source',
  'mpmath_digits':mp.mp.dps,'trial_source':'float64 projected raw prolate proxy coefficients',
  'cases':records,'scope':'High-precision diagnostic of Arb matrix midpoints and rounded trial coefficients. Eigenvalues, gaps, scores, proxy truncation, all-parameter limits, and G* are not interval-certified.'}
(HERE/'high_precision_results.json').write_text(json.dumps(result,indent=2)+'\n')
