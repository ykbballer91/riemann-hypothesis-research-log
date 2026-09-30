#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/weighted_prime_halfspace/experiments/check_halfspace.py
# Original SHA-256: 93ae739976b4c8b6568fe9aaf2069289101fd08d6fe518ff731bf52067221adc
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact finite checks and high-precision diagnostics; no asymptotic fits."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import json
import math
import random
import mpmath as mp

mp.mp.dps = 80
OUT = Path(__file__).with_name("results.json")

def sieve(N):
    spf = list(range(N+1))
    for p in range(2, math.isqrt(N)+1):
        if spf[p] == p:
            for n in range(p*p, N+1, p):
                if spf[n] == n:
                    spf[n] = p
    primes = [p for p in range(2, N+1) if spf[p] == p]
    mu, omega, largest = [0]*(N+1), [0]*(N+1), [0]*(N+1)
    mu[1] = 1
    for n in range(2, N+1):
        p, r = spf[n], n//spf[n]
        mu[n] = 0 if r % p == 0 else -mu[r]
        omega[n] = omega[r] + (r % p != 0)
        largest[n] = max(p, largest[r])
    return primes, mu, omega, largest

primes, mu, omega, largest = sieve(10000)

def sf_subsets(P):
    rows = [(1, 1, 0)]
    for p in P:
        rows += [(p*n, -s, k+1) for n,s,k in rows]
    return sorted(rows)

def recurrence(P, X):
    old, rows = {1:1}, []
    for p in P:
        before = sum(old.values())
        shifted = sum(s for n,s in old.items() if n*p <= X)
        addition = {n*p:-s for n,s in old.items() if n*p <= X}
        assert not (old.keys() & addition.keys())
        old.update(addition)
        after = sum(old.values())
        assert after == before-shifted
        rows.append({"prime":p,"before":before,"shifted_value":shifted,
                     "after":after,"unsigned_terms":len(old),
                     "absolute_amplitude_increased":abs(after)>abs(before)})
    return old, rows

recurrences=[]
for X in [30,100,1000]:
    P=[p for p in primes if p<=X]
    coeff, rows=recurrence(P,X)
    assert sum(coeff.values())==sum(mu[1:X+1])
    assert coeff=={n:mu[n] for n in range(1,X+1) if mu[n]}
    recurrences.append({"X":X,"steps":rows})

equal=[]
for m in range(1,21):
    for r in range(m):
        val=sum((-1)**k*math.comb(m,k) for k in range(r+1))
        assert val==(-1)**r*math.comb(m-1,r)
    r=(m-1)//2
    val=(-1)**r*math.comb(m-1,r)
    equal.append({"dimension":m,"cutoff_rank":r,"counting_parity":val,
                  "normalized_parity":str(Fraction(val,2**m))})

# Exhaustive small downsets, not only linear thresholds.
downsets=[]
for m in range(1,5):
    count=0
    maximum=0
    for family in range(1 << (1 << m)):
        good=True
        for face in range(1 << m):
            if family & (1 << face):
                for j in range(m):
                    if face & (1 << j) and not family & (1 << (face ^ (1 << j))):
                        good=False
                        break
            if not good:
                break
        if good:
            count+=1
            discrepancy=sum((-1)**face.bit_count() for face in range(1 << m)
                            if family & (1 << face))
            maximum=max(maximum,abs(discrepancy))
    bound=math.comb(m-1,(m-1)//2)
    assert maximum==bound
    downsets.append({"dimension":m,"downsets":count,"maximum_absolute_parity":maximum,
                     "sharp_binomial_bound":bound})

# Exact recurrence and ordering independence for every permutation of six primes.
P=primes[:6]
orders=[]
for order in permutations(P):
    _, rows=recurrence(order,100)
    orders.append((rows[-1]["after"],max(abs(r["after"]) for r in rows)))
assert len({x[0] for x in orders})==1

# Exact influence = unsigned pivotal shell / 2^(m-1).
influences=[]
X=30
P=[p for p in primes if p<=X]
full=sum(s for n,s,k in sf_subsets(P) if n<=X)
for p in P:
    other=sf_subsets([q for q in P if q!=p])
    shell=[(n,s) for n,s,k in other if n<=X and n*p>X]
    signed=sum(s for n,s in shell)
    assert signed==full
    influences.append({"prime":p,"unsigned_shell_count":len(shell),
                       "signed_shell_count":signed,
                       "influence":str(Fraction(len(shell),2**(len(P)-1))),
                       "normalized_top_coefficient":str(Fraction(full,2**len(P)))})

# Every p>sqrt(X) occurs at most once; shared parents are retained separately.
large_splits=[]
for X in [30,100,1000,10000]:
    y=math.isqrt(X)
    smooth=sum(mu[n] for n in range(1,X+1) if largest[n]<=y)
    terms=[{"prime":p,"parent_cutoff":X//p,"parent_M":sum(mu[1:X//p+1])}
           for p in primes if y<p<=X]
    rhs=smooth-sum(t["parent_M"] for t in terms)
    assert rhs==sum(mu[1:X+1])
    parent_multiplicity=Counter()
    for t in terms:
        for n in range(1,t["parent_cutoff"]+1):
            if mu[n]: parent_multiplicity[n]+=1
    large_splits.append({"X":X,"smooth_signed_sum":smooth,"large_prime_terms":terms,
                         "M":rhs,"parent_multiplicity_max":max(parent_multiplicity.values()),
                         "parent_one_multiplicity":parent_multiplicity[1]})

# Six requested weight classes with equal total weight and the same readout L.
P=primes[:10]
actual=[mp.log(p) for p in P]
total=sum(actual)
rng=random.Random(20260930)
weight_specs={
    "actual_prime_logs":actual,
    "equal_weights":[mp.mpf(1)]*10,
    "equally_spaced_rational_weights":[mp.mpf(j) for j in range(1,11)],
    "sampled_continuous_weights":[mp.mpf(str(.5+rng.random())) for _ in P],
    "perturbed_prime_logs":[mp.log(p)+mp.mpf(j-5)/1000 for j,p in enumerate(P)],
    "nonprime_generator_logs":[mp.log(n) for n in [4,6,8,9,10,12,14,15,18,20]],
    "exact_rational_relations":[mp.mpf(j) for j in [1,1,2,2,3,3,4,4,5,5]]
}
comparisons=[]
L=mp.log(mp.mpf("29.5"))  # no integer boundary ambiguity in the actual case
for label,ww in weight_specs.items():
    weights=[w*total/sum(ww) for w in ww]
    atoms=[(mp.mpf(0),1,0)]
    for w in weights:
        atoms += [(u+w,-sign,k+1) for u,sign,k in atoms]
    selected=[(u,s,k) for u,s,k in atoms if u<=L]
    gap=min(abs(u-L) for u,s,k in atoms)
    assert gap>mp.mpf("1e-60")
    val=sum(s for u,s,k in selected)
    comparisons.append({"model":label,"dimension":len(weights),
                        "total_weight":mp.nstr(sum(weights),25),
                        "cutoff":mp.nstr(L,25),"selected_count":len(selected),
                        "counting_parity":val,"normalized_parity":str(Fraction(val,2**len(weights))),
                        "minimum_cutoff_gap":mp.nstr(gap,20),
                        "weight_values":[mp.nstr(w,25) for w in weights]})

# Irrational perturbations preserve an extremizing cardinality threshold.
m=12
r=(m-1)//2
weights=[1+mp.sqrt(p)/10000 for p in primes[:m]]
atoms=[(mp.mpf(0),1,0)]
for w in weights:
    atoms += [(u+w,-s,k+1) for u,s,k in atoms]
cut=mp.mpf(r)+mp.mpf(".5")
assert all((u<=cut)==(k<=r) for u,s,k in atoms)
perturbed_extremum=sum(s for u,s,k in atoms if u<=cut)
assert perturbed_extremum==(-1)**r*math.comb(m-1,r)

omega_rows=[]
for X in [30,100,1000,10000]:
    counts=Counter(omega[n] for n in range(1,X+1) if mu[n])
    assert sum((-1)**k*v for k,v in counts.items())==sum(mu[1:X+1])
    responses=[]
    for delta in [Fraction(-1,10),Fraction(-1,100),Fraction(0),Fraction(1,100),Fraction(1,10)]:
        z=-1+delta
        val=sum(v*z**k for k,v in counts.items())
        responses.append({"delta":str(delta),"S_z_exact":str(val)})
    omega_rows.append({"X":X,"squarefree_omega_counts":dict(sorted(counts.items())),
                      "M":sum(mu[1:X+1]),
                      "S_prime_at_minus_one":sum(k*v*(-1)**(k-1) for k,v in counts.items() if k),
                      "near_endpoint_values":responses})
gamma_zeros=[str(mp.rgamma(-1-j)) for j in range(10)]
assert all(x=="0.0" for x in gamma_zeros)

# Finite tilt: exact rational arithmetic at sigma=1.
tilts=[]
for X in [3,10,30]:
    P=[p for p in primes if p<=X]
    Z=math.prod(Fraction(p+1,p) for p in P)
    Echi=math.prod(Fraction(p-1,p+1) for p in P)
    N=sum(abs(v) for v in mu[1:X+1])
    M=sum(mu[1:X+1])
    EG=Fraction(N,1)/Z
    EchiG=Fraction(M,1)/Z
    cov=EchiG-Echi*EG
    assert Z*EchiG==M
    assert N*Echi+Z*cov==M
    tilts.append({"X":X,"Z":str(Z),"parity_expectation":str(Echi),
                  "readout_expectation":str(EG),"joint_expectation":str(EchiG),
                  "bulk_product":str(N*Echi),"covariance_remainder":str(Z*cov),"M":M})

saddles=[]
for X in [3,10,30,100,1000,10000]:
    P=[p for p in primes if p<=X]
    L=mp.log(X); weights=[mp.log(p) for p in P]
    mean=lambda sigma: sum(w/(1+mp.exp(sigma*w)) for w in weights)
    lo,hi=mp.mpf(-2),mp.mpf(3)
    for _ in range(230):
        mid=(lo+hi)/2
        if mean(mid)>L: lo=mid
        else: hi=mid
    sigma=(lo+hi)/2
    var=sum(w*w*mp.exp(sigma*w)/(1+mp.exp(sigma*w))**2 for w in weights)
    assert abs(mean(sigma)-L)<mp.mpf("1e-60")
    saddles.append({"X":X,"sigma":mp.nstr(sigma,25),"mean":mp.nstr(mean(sigma),25),
                    "variance_over_logX_squared":mp.nstr(var/L**2,25),
                    "normalization_log_Z_plus_sigma_logX":mp.nstr(
                        sum(mp.log1p(mp.exp(-sigma*w)) for w in weights)+sigma*L,25)})

data={"rh_status":"OPEN","purpose":"identity checks and counterexample diagnostics; no growth fits",
      "prime_recursions":recurrences,"equal_weight_extrema":equal,
      "all_small_downsets":downsets,
      "permutation_audit":{"orders":len(orders),"final_value":orders[0][0],
                           "intermediate_max_min":min(x[1] for x in orders),
                           "intermediate_max_max":max(x[1] for x in orders)},
      "pivotal_shells":influences,"large_prime_splits":large_splits,
      "weight_comparisons":comparisons,
      "independent_irrational_extremizer":{"dimension":m,"rank":r,"parity":perturbed_extremum,
                                          "weights":"1+sqrt(p_j)/10000","cutoff":str(cut)},
      "omega_endpoint":omega_rows,"reciprocal_gamma_endpoint_values":gamma_zeros,
      "finite_tilts":tilts,"saddle_diagnostics":saddles,
      "numerical_values_are_interval_certificates":False,"all_assertions_passed":True}
OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"output":str(OUT),"all_assertions_passed":True,
                  "permutations":len(orders),"weight_models":len(comparisons)}))
