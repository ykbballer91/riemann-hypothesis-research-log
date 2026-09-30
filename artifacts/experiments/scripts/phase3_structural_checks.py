#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/phase3_structural_checks.py
# Original SHA-256: bcf2b66ee7c2db4544fc6b90ea2ca2f8e8390babf8bd1c990122718fd7ff26b3
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact finite algebra and diagnostic floats; all-n proofs are in the note."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]

def mul(a, b):
    return [[sum(x*y for x, y in zip(row,col)) for col in zip(*b)] for row in a]

def tr(a): return [list(c) for c in zip(*a)]
def scale(c,a): return [[c*x for x in row] for row in a]
def mu(n):
    parity=0; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; parity+=1
            if n%p==0: return 0
        while n%p==0: n//=p
        p+=1
    if n>1: parity+=1
    return (-1)**parity

F=[[0,-9],[1,7]]; J=[[0,1],[-1,0]]; H=[[2,7],[7,18]]
A=[[1,0],[0,-1]]; I=[[1,0],[0,1]]
adj=lambda a:mul(mul(scale(-1,J),tr(a)),J)
assert mul(mul(tr(F),J),F)==scale(9,J)
assert mul(mul(tr(F),H),F)==scale(9,H)
assert mul(adj(F),F)==scale(9,I)
assert adj(A)==scale(-1,A)
assert H[0][0]*H[1][1]-H[0][1]*H[1][0]==-13
S=[2,7]
for n in range(2,201): S.append(7*S[-1]-9*S[-2])
N=[9**n+1-S[n] for n in range(201)]
b=[]
for n in range(1,201):
    num=sum(mu(d)*N[n//d] for d in range(1,n+1) if n%d==0)
    assert num%n==0 and num>0
    b.append(num//n)
bound=Fraction(4,9)+Fraction(4,81)+Fraction(1,8)+Fraction(1,81)
assert bound==Fraction(409,648) and bound<1
mp.mp.dps=100
alphas=[(7+mp.sqrt(13))/2,(7-mp.sqrt(13))/2]
gamma_checks=[]
for s in ['0.5','1','2','3','7']:
    s=mp.mpf(s); a=s/2
    # Fixed-step fourth-order difference avoids mp.diff's tiny-step
    # cancellation in Hurwitz zeta at a=1/4. Diagnostic, not an enclosure.
    f=lambda w: mp.pi**w*mp.zeta(w,a)
    h=mp.mpf('1e-16')
    deriv=(f(-2*h)-8*f(-h)+8*f(h)-f(2*h))/(12*h)
    lhs=mp.exp(-deriv); rhs=mp.sqrt(2)*mp.pi**a/mp.gamma(a)
    gamma_checks.append({'s':str(s),'absolute_error':mp.nstr(abs(lhs-rhs),8)})
    assert abs(lhs-rhs)<mp.mpf('1e-55')
result={
    'scope':'algebraic checks exact; mpmath diagnostic only; all-n proof in research note',
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'q':9,'F':F,'J':J,'indefinite_symmetric_H':H,'det_H':-13,
    'formal_adjoint_negative_trace':-2,
    'positive_integer_closed_point_counts_checked_through':200,
    'first_closed_point_counts':b[:12],
    'all_n_proof_bound_at_2':str(bound),
    'alpha_diagnostics':[mp.nstr(x,45) for x in alphas],
    'zero_real_part_diagnostics':[mp.nstr(mp.log(x)/mp.log(9),45) for x in alphas],
    'archimedean_determinant_noncertified_checks':gamma_checks,
    'numerical_checks_prove_infinite_statement':False,
    'is_actual_curve':False,'is_actual_zeta_counterexample':False,
    'proves_RH':False,'refutes_RH':False,
}
out=ROOT/'experiments/results/phase3-structural-checks.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
