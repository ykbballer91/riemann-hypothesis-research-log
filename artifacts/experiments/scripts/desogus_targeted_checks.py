#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/desogus_targeted_checks.py
# Original SHA-256: 9c2b2045b65419380496a5c8475345a8c5afa57c4df856c46d09a126a8f3ad65
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Independent targeted checks, NOT verification of the external RH claim.

Exact Fraction arithmetic checks the printed interval matrix and Schur models.
Arb direct logarithms check selected arithmetic budgets from their definitions.
The original author code is neither imported nor executed.
"""
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import arb, ctx

ctx.prec = 256
source = Path('literature/source_cache/desogus-2609.20367v2/main.tex')
tex = source.read_text()
report = dict(external_claim_status='UNVERIFIED EXTERNAL PROOF CLAIM',
              proves_RH=False, refutes_RH=False,
              verifies_external_full_proof=False,
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              paper_tex_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              precision_bits=ctx.prec, python_flint_version=flint.__version__)

# The printed final 7x7 family is checked independently of its production.
entries = re.findall(r'(\d) & (\d) & \\texttt\{([^}]+)\} & \\texttt\{([^}]+)\}', tex)
assert len(entries) == 28
matrix = [[None]*7 for _ in range(7)]
for i,j,mid,rad in entries:
    i,j=int(i)-1,int(j)-1
    matrix[i][j]=matrix[j][i]=(F(mid),F(rad))
raw_d = re.findall(r'd_([1-7])&=([\d.]+)\\times10\^\{(-?\d+)\}',tex)
assert len(raw_d)==7
diagonal = [None]*7
for i,m,e in raw_d:diagonal[int(i)-1]=F(m)*F(10)**int(e)
margins=[]
for i in range(7):
    mid,rad=matrix[i][i]
    q=(mid-rad)/diagonal[i]**2
    for j in range(7):
        if i!=j:
            m,r=matrix[i][j]
            q-=(abs(m)+r)/(diagonal[i]*diagonal[j])
    assert q>F('0.5198729787')
    margins.append(q)
show=lambda x:x.str(45,more=True)
report['printed_matrix'] = dict(dimension=7,
    exact_rational_gershgorin_pass=True,
    minimum_margin_exceeds='0.5198729787',
    margin_enclosures=[show(arb(q.numerator)/q.denominator) for q in margins],
    verifies_from_weil_form_assembly=False,
    verifies_infinite_complement=False)

# Only selected k, with direct prime-power generation and direct Arb logs.
targets=[2,3,7,8,32,33,34,4999,5000]
limit=max(targets)
prime=[True]*(limit+1);prime[:2]=[False,False]
for p in range(2,limit+1):
    if prime[p]:
        for n in range(p*p,limit+1,p):prime[n]=False
powers=[]
for p in range(2,limit+1):
    if prime[p]:
        n=p
        while n<=limit:
            powers.append((n,arb(p).log()))
            n*=p
powers.sort(key=lambda v:v[0])
log2=arb(2).log();beta=log2+arb(1)/2
checks=[]
for k in targets:
    bins={};sigma=arb(0)
    for n,lam in powers:
        if n>k:break
        if k%n==0:continue
        m=k//n
        if m not in bins:bins[m]=[arb(0),arb(0),0]
        bins[m][0]+=lam*lam/n;bins[m][1]+=lam;bins[m][2]+=n
        sigma+=lam*lam/(n*(arb(n).log()+beta))
    variance=arb(0);safeW=arb(0)
    for m,(squares,logs,total_n) in bins.items():
        variance+=squares-logs*logs/total_n
        safeW+=squares*(arb('0.0145') if m==1 else arb('0.0301')/(m*m))
    awgc=sigma-variance/log2
    master=arb(1)/2+arb(k).log()-arb(439)/(250*log2)*variance
    aligned=master-arb(5)/2*safeW
    assert (not bins) if k==2 else awgc>0
    if k>=7:assert aligned>0
    checks.append(dict(k=k,awgc_margin=show(awgc),
                       master_margin=show(master),safe_aligned_margin=show(aligned)))
report['selected_arithmetic_budgets']=dict(values=checks,
    all_integers_certified=False, analytic_tail_certified=False,
    operator_lift_verified=False)

# Missing sign hypothesis: old positive block does not imply positive new pivot.
def folded_model(beta):
    old=1-beta;gamma=beta/old;cut=1-gamma
    xleft=beta/old;xright=F(1)
    assert old>0
    assert (1-beta)*xleft-beta*xright==0
    E=F(1);u=F(1);Q=cut;D=cut
    assert Q-D==E*(1-u)==0
    return dict(beta=str(beta),old_pivot=str(old),x=[str(xleft),'1'],
                cut_pivot=str(cut),Q=str(Q),D=str(D),formal_Q_minus_D='0')
report['pivot_sign_models']=[folded_model(F(3,4)),folded_model(F(1,4))]

# Literal two-arm form in v2 (same b in each arm) costs twice b^2/P.
P=b=Q=F(2,3);x=F(1);t=-b*x/P
value=Q*x*x+P*(t*t+t*t)+2*b*x*(t+t)
assert b*b/P==F(2,3)
assert value==Q-2*b*b/P==F(-2,3)
assert Q-b*b/P==0
report['two_arm_model']=dict(P=str(P),b=str(b),Q=str(Q),
    minimizing_t=[str(t),str(t)],one_arm_debit=str(b*b/P),
    exact_two_arm_schur=str(value),one_debit_expression='0',
    actual_weil_counterexample=False,
    scope='Printed finite algebra and missing premise only; no arithmetic realization assumed')

out=Path('experiments/results/desogus-targeted-checks.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(saved=str(out),printed_matrix='PASS as supplied',
    selected_k=targets,two_arm_schur=str(value),
    full_external_proof='UNVERIFIED'),indent=2))
