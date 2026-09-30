# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/strategy_reset/notes/check_finite_identities.py
# Original SHA-256: f6aefd81cc9746468d28e4ebbce6835b647cbe671e7de9367af3e270a7ab04e2
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact finite arithmetic diagnostics for the audit, not an asymptotic proof."""
from collections import defaultdict
from pathlib import Path
import json
from math import prod

LIMIT = 1000
def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p,0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n,0)+1
    return out

def mu(n):
    fs = factor(n)
    return 0 if any(e>1 for e in fs.values()) else (-1)**len(fs)

def poly_power_linear(vec,k):
    r=len(vec)
    poly={(0,)*r:1}
    for _ in range(k):
        new=defaultdict(int)
        for monomial,coef in poly.items():
            for i,a in enumerate(vec):
                if not a: continue
                m=list(monomial); m[i]+=1
                new[tuple(m)]+=coef*a
        poly=dict(new)
    return poly

positive_polynomials=0
for n in range(1,LIMIT+1):
    divs=[d for d in range(1,n+1) if n%d==0]
    assert sum(mu(d) for d in divs)==int(n==1)
    fs=factor(n); ps=list(fs)
    # Coefficients of the independent formal variables log p.
    mu_log={p:sum(mu(d)*factor(n//d).get(p,0) for d in divs) for p in ps}
    log_mu={p:sum(mu(d)*factor(d).get(p,0) for d in divs) for p in ps}
    target={p:int(len(ps)==1) for p in ps}
    assert mu_log==target
    assert log_mu=={p:-v for p,v in target.items()}
    for k in range(1,5):
        result=defaultdict(int)
        for d in divs:
            md=mu(d)
            if not md: continue
            fd=factor(n//d)
            for monomial,c in poly_power_linear([fd.get(p,0) for p in ps],k).items():
                result[monomial]+=md*c
        assert all(c>=0 for c in result.values())
        if len(ps)>k:
            assert all(c==0 for c in result.values())
        positive_polynomials+=1

out={
    "purpose":"Finite exact sanity checks; general convergence and identities proved in the audit note",
    "integer_limit":LIMIT,
    "divisor_closure_cases":LIMIT,
    "signed_log_identity_cases":LIMIT,
    "generalized_mangoldt_polynomial_cases":positive_polynomials,
    "arithmetic":"Exact integer coefficients in formal log-prime variables; no floating point",
    "all_checks_passed":True,
    "asymptotic_or_RH_inference":False
}
Path(__file__).with_name("finite_identity_checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))
