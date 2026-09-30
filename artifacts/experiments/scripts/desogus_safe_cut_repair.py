#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/desogus_safe_cut_repair.py
# Original SHA-256: 5a8a0e4bb782200b4cb0670262055e419093adb06a4b1a6c29f8648666e71eab
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Independent Arb reconstruction of the finite safe-cut bound, k=7..4999.

Use harmonic quotient blocks and prefix sums rather than the author's
long-double branch-by-branch interval algorithm. This repairs only the finite
scalar obligation, not the analytic tail or the operator identification.
"""
import hashlib
import json
from pathlib import Path
import flint
from flint import arb, ctx

ctx.prec=192
N=4999
spf=list(range(N+1))
for p in range(2,N+1):
    if spf[p]==p:
        for n in range(p*p,N+1,p):
            if spf[n]==n:spf[n]=p
weights=[arb(0) for _ in range(N+1)]
for p in range(2,N+1):
    if spf[p]==p:
        lam2=arb(p).log()**2
        n=p
        while n<=N:
            weights[n]=lam2/n
            n*=p
prefix=[arb(0)]
for n in range(1,N+1):prefix.append(prefix[-1]+weights[n])
logw=[None]+[((arb(1)+arb(1)/k).log()).log() for k in range(1,N+1)]
d0=arb('0.422785')
assert d0>1-arb.const_euler()
half=arb(1)/2
min_lower=None;min_k=None;selected=[]
for k in range(7,N+1):
    # floor(k/n) is constant for n from n0 to k//floor(k/n0).
    sigma=arb(0);n0=2
    while n0<=k:
        m=k//n0;n1=k//m
        denom=half+logw[m]-logw[k]-d0
        assert denom>0
        sigma+=(prefix[n1]-prefix[n0-1])/denom
        n0=n1+1
    # Remove precisely the prime-power divisors, as required by the statement.
    remaining=k
    while remaining>1:
        p=spf[remaining];power=1
        while remaining%p==0:
            power*=p;remaining//=p
            denom=half+logw[k//power]-logw[k]-d0
            sigma-=weights[power]/denom
    gap=half-logw[k]-sigma
    assert gap>arb('1.5202196525'),(k,gap)
    lo=gap.lower()
    if min_lower is None or lo<min_lower:min_lower=lo;min_k=k
    if k in [7,8,33,4998,4999]:selected.append({'k':k,'gap':gap.str(50,more=True)})
out=dict(status='FINITE_SCALAR_REPAIR_VERIFIED',proves_RH=False,refutes_RH=False,
    verifies_external_full_proof=False,range=[7,N],integers_checked=N-6,
    precision_bits=ctx.prec,python_flint_version=flint.__version__,
    algorithm='Arb prefix sums and harmonic quotient blocks; prime-power divisor removal',
    author_code_executed=False,uniform_gap_exceeds='1.5202196525',
    minimum_lower_endpoint=min_lower.str(50,more=True),minimum_at=min_k,
    selected=selected,analytic_tail_verified=False,operator_lift_verified=False,
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
dest=Path('experiments/results/desogus-safe-cut-repair.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(saved=str(dest),status=out['status'],integers=out['integers_checked'],
    min_at=min_k,minimum=out['minimum_lower_endpoint']),indent=2))
