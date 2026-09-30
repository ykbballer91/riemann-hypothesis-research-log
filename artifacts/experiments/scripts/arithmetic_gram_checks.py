#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/arithmetic_gram_checks.py
# Original SHA-256: 246542040f0211b97a16d917d0461aae9848331654c997696187d9b1e9cbd708
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact bounded checks of full-arithmetic identities; no RH certificate."""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import hashlib
import json
from flint import arb, ctx


def divisors(n):
    return [d for d in range(1,n+1) if n % d == 0]


def factors(n):
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


def mobius(n):
    exps = list(factors(n).values())
    return 0 if any(e > 1 for e in exps) else (-1)**len(exps)


def totient(n):
    out = n
    for p in factors(n):
        out = out//p*(p-1)
    return out


def sawtooth_gram(m,n):
    cuts = sorted(set([Q(j,m) for j in range(m+1)]
                      +[Q(j,n) for j in range(n+1)]))
    total = Q(0)
    for lo,hi in zip(cuts,cuts[1:]):
        mid = (lo+hi)/2
        a = Q((m*mid).__floor__())+Q(1,2)
        b = Q((n*mid).__floor__())+Q(1,2)
        total += Q(m*n,3)*(hi**3-lo**3)
        total -= Q(m*b+n*a,2)*(hi**2-lo**2)
        total += a*b*(hi-lo)
    return total


def main():
    saw_checks = []
    for m,n in [(1,1),(2,3),(4,6),(5,12),(6,15)]:
        integral = sawtooth_gram(m,n)
        assert integral == Q(gcd(m,n)**2,12*m*n)
        saw_checks.append({'m':m,'n':n,'exact_integral':str(integral)})

    # At alpha=1/2, write input c_n=sqrt(n)*a_n, with rational a_n.
    # Every squared norm and divisor-feature coefficient is then exact.
    vertical_checks = []
    primes = [5,7,11,13]
    weight = sum((Q(1,p) for p in primes),Q(0))
    for d in [1,2,6]:
        a = {}
        for p in primes:
            assert d % p != 0
            for k in divisors(d):
                a[k*p] = a.get(k*p,Q(0))+Q(mobius(d//k),p)/weight
        rows = sorted(set(r for n in a for r in divisors(n)))
        feature = {r:sum((v for n,v in a.items() if n % r == 0),Q(0))
                   for r in rows}
        # Actual feature is sqrt(phi(r))*feature[r].
        assert feature[d] == 1
        assert all(v == 0 for r,v in feature.items()
                   if r != d and r not in [d*p for p in primes])
        for p in primes:
            assert feature[d*p] == Q(1,p)/weight
        input_norm = sum((n*v*v for n,v in a.items()),Q(0))
        expected_norm = sum((Q(k*mobius(d//k)**2) for k in divisors(d)),Q(0))/weight
        assert input_norm == expected_norm
        residual_norm = sum((totient(r)*v*v for r,v in feature.items() if r != d),Q(0))
        expected_residual = totient(d)*sum((Q(p-1,p*p) for p in primes),Q(0))/weight**2
        assert residual_norm == expected_residual
        direct_gram = sum((v*w*gcd(n,m) for n,v in a.items() for m,w in a.items()),Q(0))
        feature_gram = sum((totient(r)*v*v for r,v in feature.items()),Q(0))
        assert direct_gram == feature_gram == totient(d)+residual_norm
        vertical_checks.append({'target_d':d, 'prime_set':primes,
                                'weight':str(weight),
                                'input_norm_squared':str(input_norm),
                                'target_feature_norm_squared':totient(d),
                                'residual_norm_squared':str(residual_norm),
                                'direct_Gram_equals_feature_Gram':True})

    # Formal coefficients of log(prime) verify the conjugation identity.
    mobius_log_cases = 0
    for d in [1,6]:
        for k in range(1,25):
            all_primes = factors(d*k)
            for p in all_primes:
                lhs = sum(mobius(k//j)*factors(d*j).get(p,0) for j in divisors(k))
                if k == 1:
                    rhs = factors(d).get(p,0)
                else:
                    fk = factors(k)
                    rhs = int(len(fk)==1 and p in fk)
                assert lhs == rhs
            mobius_log_cases += 1

    ctx.prec = 192
    negative_form = -arb(2).log()/4
    positive_poisson_derivative = 2*arb(2).sqrt()*arb(2).log()
    assert negative_form < 0 and positive_poisson_derivative > 0
    # Direct two-dimensional form evaluation at y=(1,-1/2).
    y0,y2 = arb(1),-arb(1)/2
    direct = arb(2).log()*y2*y2+arb(2).log()*y0*y2
    assert (direct-negative_form).contains(0)
    result = {
        'status':'FULL_ARITHMETIC_GRAM_AND_CRITICAL_DOMAIN_OBSTRUCTIONS_VERIFIED',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proves_RH':False, 'refutes_RH':False, 'main_graph_merge':False,
        'exact_sawtooth_integrals':saw_checks,
        'exact_divisor_feature_witnesses':vertical_checks,
        'formal_log_prime_identity_cases':mobius_log_cases,
        'interval_checks':{
            'precision_bits':192,
            'critical_B_Hermitian_form_at_e1_minus_half_e2':str(negative_form),
            'negative_certified':True,
            'minus_log_Poisson_alpha_derivative_at_theta_zero_p2':str(positive_poisson_derivative),
            'minus_log_Poisson_alpha_derivative_at_theta_pi_p2':str(-positive_poisson_derivative),
            'opposite_signs_certified':True},
        'all_alpha_domain_classification':'proved analytically in note, not inferred from finite checks',
        'all_beta_unbounded_below':'proved analytically by prime-star Schur complements',
        'scope':'GCD Gram and its specified logarithmic conjugation, not actual Weil form',
        'analytic_record':'research/arithmetic_gram_generator.md',
    }
    root = Path(__file__).resolve().parents[2]
    (root/'experiments/results/arithmetic-gram-checks.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
