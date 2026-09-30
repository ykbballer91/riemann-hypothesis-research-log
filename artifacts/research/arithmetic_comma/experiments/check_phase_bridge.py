#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/arithmetic_comma/experiments/check_phase_bridge.py
# Original SHA-256: 493515927886e4cfd51cbe0121e67479aff4ef86e253c83b02426ace3fb22283
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Finite exact combinatorics and diagnostic phase sampling; not RH evidence."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import cmath
import json
import math
import mpmath as mp

mp.mp.dps = 60
OUT = Path(__file__).with_name("results.json")

def mobius(n):
    k, d = 0, 2
    while d*d <= n:
        if n % d == 0:
            n //= d
            k += 1
            if n % d == 0:
                return 0
        d += 1
    if n > 1:
        k += 1
    return (-1)**k

def subsets(primes):
    ans = []
    for k in range(len(primes)+1):
        for s in combinations(primes, k):
            ans.append((math.prod(s), (-1)**k, s))
    return sorted(ans)

def moments(X, order):
    nums = [(n, mobius(n)) for n in range(1, X+1) if mobius(n)]
    signed, positive = {1: 1}, {1: 1}
    for _ in range(order):
        a, b = Counter(), Counter()
        for r, v in signed.items():
            for n, mu in nums:
                a[r*n] += v*mu
        for r, v in positive.items():
            for n, _ in nums:
                b[r*n] += v
        signed, positive = a, b
    # All ordered tuples with the same product have the same parity.
    assert set(signed) == set(positive)
    assert all(abs(signed[n]) == positive[n] for n in signed)
    sm = sum(v*v for v in signed.values())
    pm = sum(v*v for v in positive.values())
    assert sm == pm
    return {"X": X, "absolute_moment_order": 2*order,
            "haar_mobius": sm, "haar_all_positive": pm,
            "distinct_tuple_products": len(signed)}

def finite_time_mean_square(X, T, signed):
    nums = [(n, mobius(n) if signed else 1)
            for n in range(1, X+1) if mobius(n)]
    # Integral over [0,T] of cos(t log(n/m)) is sin(T log(n/m))/log(n/m).
    val = mp.mpf(len(nums))
    for i, (m, a) in enumerate(nums):
        for n, b in nums[i+1:]:
            u = T*mp.log(mp.mpf(n)/m)
            val += 2*a*b*mp.sin(u)/u
    return mp.nstr(val, 25)

toy = []
for P in [(2,3), (2,3,5), (2,3,5,7,11)]:
    rows, cumulative = [], 0
    for n, mu, factors in subsets(P):
        cumulative += mu
        rows.append({"birth_product": n, "mu": mu,
                     "factors": factors, "cumulative": cumulative})
    assert cumulative == 0
    # Direct finite-product identity, evaluated numerically at non-special times.
    max_error = mp.mpf(0)
    for t in [mp.mpf("0.137"), mp.sqrt(2), mp.mpf("19.25")]:
        direct = sum(mu*mp.exp(-1j*t*mp.log(n)) for n,mu,_ in subsets(P))
        product = mp.mpc(1)
        for p in P:
            product *= 1-mp.exp(-1j*t*mp.log(p))
        max_error = max(max_error, abs(direct-product))
    assert max_error < mp.mpf("1e-50")
    toy.append({"primes": P, "rows": rows, "product_identity_max_error": str(max_error)})

identity = []
for X in [10, 30, 100, 1000]:
    values = [mobius(n) for n in range(1, X+1)]
    N = sum(abs(v) for v in values)
    identity.append({"X": X, "M": sum(values), "squarefree_count": N,
                     "shared_haar_second_moment": N,
                     "all_positive_identity_value": N,
                     "mobius_value_at_all_minus_one": N})

moment_rows = [moments(X,r) for X,r in [(10,1),(10,2),(10,3),(30,2),(30,3),(100,2)]]

returns = []
record = mp.inf
# Search bounded integer coefficients, not only a guessed list of approximants.
for b in range(1, 401):
    a = int(mp.nint(b*mp.log(3)/mp.log(2)))
    defect = abs(a*mp.log(2)-b*mp.log(3))
    if defect < record:
        record = defect
        maxint = max(2**a, 3**b)
        assert defect >= mp.mpf(1)/maxint
        returns.append({"coefficient_log2": a, "coefficient_log3": -b,
                        "defect": mp.nstr(defect, 30),
                        "elementary_lower_bound": mp.nstr(mp.mpf(1)/maxint, 15),
                        "time_log2_exact_return": mp.nstr(2*mp.pi*b/mp.log(2), 25),
                        "log3_phase_error": mp.nstr(2*mp.pi*defect/mp.log(2), 25)})

time_rows = []
for T in [10,100,1000,10000]:
    time_rows.append({"X": 30, "T": T,
                      "mobius_mean_square": finite_time_mean_square(30,T,True),
                      "positive_mean_square": finite_time_mean_square(30,T,False),
                      "common_infinite_time_limit": sum(abs(mobius(n)) for n in range(1,31))})

samples = []
for P in [(2,3),(2,3,5)]:
    logs = [math.log(p) for p in P]
    eta, dt, count = .5, .05, 20000
    near_zero = near_pi = 0
    zero_max, pi_min = 0., math.inf
    abs_sum = square_sum = 0.
    for j in range(count):
        t = (j+.5)*dt
        angles = [math.remainder(t*l, 2*math.pi) for l in logs]
        amplitude = math.prod(abs(1-cmath.exp(-1j*a)) for a in angles)
        abs_sum += amplitude
        square_sum += amplitude*amplitude
        if all(abs(a) <= eta for a in angles):
            near_zero += 1
            zero_max = max(zero_max, amplitude)
            assert amplitude <= eta**len(P)+1e-12
        if all(abs(abs(a)-math.pi) <= eta for a in angles):
            near_pi += 1
            pi_min = min(pi_min, amplitude)
            assert amplitude >= (2*math.cos(eta/2))**len(P)-1e-12
    samples.append({"primes":P, "eta":eta,"T":count*dt,"dt":dt,
                    "sample_count":count,"zero_box_hits":near_zero,"pi_box_hits":near_pi,
                    "zero_box_max_amplitude":zero_max,
                    "pi_box_min_amplitude":pi_min if near_pi else None,
                    "haar_box_fraction_reference":(eta/math.pi)**len(P),
                    "sample_mean_amplitude":abs_sum/count,
                    "haar_mean_amplitude_reference":(4/math.pi)**len(P),
                    "sample_mean_square":square_sum/count,
                    "haar_mean_square_reference":2**len(P),
                    "rigorous_continuous_time_census":False})

primes = [n for n in range(51,101) if all(n%d for d in range(2,math.isqrt(n)+1))]
cluster = [(n,mu) for n,mu,_ in subsets(primes) if n<=100]
assert len(cluster) == len(primes)+1
assert sum(mu for _,mu in cluster) == 1-len(primes)

# A nontrivial fourth-moment resonance with distinct squarefree integers.
assert 2*15 == 3*10
assert mobius(2)*mobius(15)*mobius(3)*mobius(10) == 1

data = {"rh_status":"OPEN", "purpose":"finite falsification and identity checks; no asymptotic inference",
        "toy_models":toy, "identity_phase_counterexamples":identity,
        "exact_haar_moments":moment_rows,"two_prime_near_returns":returns,
        "finite_time_mean_squares":time_rows,"sampled_phase_boxes":samples,
        "cutoff_geometry_counterexample":{"X":100,"primes":primes,"admissible_terms":cluster,
                                            "discrepancy":1-len(primes),"not_full_Mertens":True},
        "higher_moment_resonance":{"left":[2,15],"right":[3,10],"product":30,"signed_weight":1},
        "all_assertions_passed":True}
OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"output":str(OUT),"all_assertions_passed":True,
                  "exact_moment_cases":len(moment_rows),"phase_samples":40000}))
