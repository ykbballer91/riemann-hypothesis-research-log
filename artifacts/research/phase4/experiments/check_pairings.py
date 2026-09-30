#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/phase4/experiments/check_pairings.py
# Original SHA-256: 6fd3d973db55e1a583b40df76d03f1f5fe3f8798de4163fbf9777b796f25445e
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Phase IV scoped falsification checks. Exact algebra, diagnostic quadrature."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import mpmath as mp

def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return [list(x) for x in zip(*a)]
def scale(k,a):return [[k*x for x in row] for row in a]
def sub(a,b):return [[x-y for x,y in zip(u,v)] for u,v in zip(a,b)]
I=[[1,0],[0,1]];J=[[0,1],[-1,0]]
Frob=[[0,-9],[1,7]]
adj=lambda a:matmul(matmul(scale(-1,J),tr(a)),J)
A=sub(Frob,scale(3,I))
R=matmul(matmul(sub(Frob,I),sub(Frob,scale(9,I))),A)
assert matmul(adj(A),A)==scale(-3,I)
assert matmul(adj(R),R)==scale(-243,I)
theta=[[F(3,4),0],[0,F(1,4)]];swap=[[0,1],[1,0]]
assert matmul(matmul(swap,theta),swap)==sub(I,tr(theta))
assert theta[0][0]!=F(1,2)
# P(u)=15u-30u^2+8u^3; Fourier of u^j exp(-pi*x^2).
P=[F(0),F(15),F(-30),F(8)]
FB=[[F(1)],[F(1,2),F(-1)],
    [F(3,4),F(-3),F(1)],
    [F(15,8),F(-45,4),F(15,2),F(-1)]]
FP=[sum(P[j]*(FB[j][k] if k<len(FB[j]) else 0) for j in range(4)) for k in range(4)]
assert FP==[-x for x in P]
sq=[sum(P[j]*P[k-j] for j in range(4) if 0<=k-j<4) for k in range(7)]
mom=[F(1)]
for k in range(1,7):mom.append(mom[-1]*F(2*k-1,4))
norm=sum(x*y for x,y in zip(sq,mom))
assert norm==F(585,32)
# Trace of local jet algebra m=3 has Gram diag(3,0,0) after canonical sharp.
m=3;N=[[0,0,0],[1,0,0],[0,1,0]]
N2=matmul(N,N)
assert sum(N2[i][i] for i in range(3))==0 and any(any(row) for row in N)
mp.mp.dps=60
h=lambda x:(8*(mp.pi*x*x)**3-30*(mp.pi*x*x)**2+15*mp.pi*x*x)*mp.exp(-mp.pi*x*x)
segments=[0,mp.mpf('.5'),1,2,4,mp.inf]
quad_norm=2*mp.quad(lambda x:h(x)**2,segments)
assert abs(quad_norm-mp.mpf(585)/(32*mp.sqrt(2)))<mp.mpf('1e-48')
fourier=[]
for y in ['0','.25','.75','1']:
    y=mp.mpf(y)
    val=2*mp.quad(lambda x:h(x)*mp.cos(2*mp.pi*x*y),segments)
    err=abs(val+h(y))
    assert err<mp.mpf('1e-48')
    fourier.append(dict(y=str(y),absolute_error=mp.nstr(err,10)))
mellin=[]
for s in [mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3')]:
    val=2*mp.quad(lambda x:h(x)*x**(s-1),segments)
    target=s*(s-1)*(2*s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)
    err=abs(val-target)
    assert err<mp.mpf('1e-48')
    mellin.append(dict(s=str(s),absolute_error=mp.nstr(err,10)))
result=dict(phase=4,rh_status='OPEN',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    exact_algebra={'primitive_star_trace':-486,'J_identity_offline_counterexample':True,
        'fourier_polynomial_coefficients':[str(x) for x in FP],
        'positive_norm_squared_times_sqrt2':str(norm),'twisted_pairing_times_sqrt2':str(-norm),
        'jet_model_dimension':3,'jet_trace_pairing_rank':1},
    numerical_diagnostics={'certified':False,'fourier':fourier,'mellin':mellin,
        'norm_absolute_error':mp.nstr(abs(quad_norm-mp.mpf(585)/(32*mp.sqrt(2))),10)},
    scope='Counterexamples to specified pairing/adjoint transfers; not to RH or full arithmetic programs',
    proves_RH=False,refutes_RH=False,zero_side_used_to_define_pairing=False)
out=Path(__file__).with_name('pairing_checks.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
