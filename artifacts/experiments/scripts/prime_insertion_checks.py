#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/prime_insertion_checks.py
# Original SHA-256: 5982293321ee7469c7c60614b362432a3ebfa2455fd94d9e0f2a1d33287fe7e7
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Bounded falsification of prime insertion; no RH claim or zero enumeration."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import mpmath as mp
from flint import arb, ctx


def exp_lower(x, n):
    return sum((x**j/F(factorial(j)) for j in range(n+1)), F(0))


def main():
    # Exact inequalities used to control the FULL j>=0 Gaussian resolvent.
    a = F(2,3)
    exp_upper = exp_lower(a,8)+a**9/F(factorial(9))/(1-a/10)
    assert exp_upper < 2
    assert exp_lower(F(7,10),8) > 2
    assert exp_lower(F(4,9),8) > F(3,2)
    assert exp_lower(F(16,9),8) > F(11,2)
    assert exp_lower(F(20,9),8) > 9
    variance_bound = F(1,2)+F(4,11)/(1-F(3,16))
    log_concavity_bound = -2+4*F(7,10)**2*variance_bound
    assert variance_bound == F(271,286)
    assert log_concavity_bound == F(-1021,7150)

    # Actual theta kernel, primes {2}. Smooth-side and omitted-side enclosures.
    ctx.prec = 192
    pi = arb.pi()
    def derivative_term(n):
        x = pi*n*n
        return -x*(8*x*x-30*x+15)*(-x).exp()
    head = sum(derivative_term(n) for n in [1,2,4,8])
    ratio = (arb(17)/16)**6*(-33*pi).exp()
    assert ratio < 1
    smooth_tail = 8*pi**3*16**6*(-256*pi).exp()/(1-ratio)
    omitted_first = -derivative_term(3)
    omitted_tail = 8*pi**3*5**6*(-25*pi).exp()/(1-3*(-11*pi).exp())
    assert head-smooth_tail > omitted_first > 0
    assert head+smooth_tail < omitted_first+omitted_tail
    seed_integral = -(arb(1)/4).gamma()/(8*pi**(arb(1)/4))
    prime2_integral = seed_integral/(1-1/arb(2).sqrt())
    assert prime2_integral < 0

    # Independent non-certified probes. The proof above does not truncate j.
    mp.mp.dps = 60
    ell, r = mp.log(2), mp.sqrt(mp.mpf('0.5'))
    def g(t):
        return mp.fsum(r**j*mp.exp(-(t+j*ell)**2) for j in range(24))
    def h(t):
        return mp.fsum((j+1)*r**j*mp.exp(-(t+j*ell)**2) for j in range(24))
    g0,g1 = g(0),g(1)
    cg = lambda t: g(t)/g0-g(t+1)/g1
    ch = lambda t: h(t)/g0-h(t+1)/g1
    original = mp.quad(lambda t: cg(t)*(t*g(t)/g0-(t+1)*g(t+1)/g1)/2,
                       [0,1,3,6,mp.inf])
    hg = mp.quad(lambda t: cg(t)**2,[0,1,3,6,mp.inf])
    hh = mp.quad(lambda t: ch(t)**2,[0,1,3,6,mp.inf])
    hh_short = mp.quad(lambda t: ch(t)**2,[0,ell])
    ledger = ell/4*(hg-(1-r*r)*hh-r*r*hh_short)
    assert original < 0 and abs(original-ledger) < mp.mpf('1e-50')
    root = Path(__file__).resolve().parents[2]
    result = {
        'status':'PRIME_INSERTION_AND_COMPLETION_CANDIDATES_REJECTED',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proves_RH':False,'refutes_RH':False,
        'actual_full_Riemann_kernel_counterexample':False,
        'full_Gaussian_resolvent_analytic_bounds':{
            'method':'exact rational Taylor inequalities plus analytic infinite tail',
            'variance_upper_bound':str(variance_bound),
            'log_second_derivative_upper_bound':str(log_concavity_bound),
            'strict_negative_two_point_form':'analytic for all t>0; nodes 0,1',
        },
        'actual_prime2_cusp':{
            'precision_bits':192,
            'smooth_head':str(head),
            'smooth_absolute_tail_bound':str(smooth_tail),
            'omitted_n3_lower_bound':str(omitted_first),
            'omitted_remaining_tail_upper_bound':str(omitted_tail),
            'positive_certified':True,
            'integral_of_uncompleted_profile':str(prime2_integral),
            'scope':'right derivative of finite-prime profile; not a zero of xi',
        },
        'numerical_cross_check':{
            'method':'mpmath 60 decimal digits, 24 j terms, not certified',
            'original_form':mp.nstr(original,52),
            'positive_negative_ledger':mp.nstr(ledger,52),
            'absolute_difference':mp.nstr(abs(original-ledger),8),
        },
        'nonreal_zero_result':{
            'family':'psi_P(t)=Phi_P(abs(t)) for finite prime sets P',
            'proof':'positive cusp, Fourier asymptotics, order at most one, Hadamard',
            'zero_enumeration_performed':False,
            'full_xi_zero_claim':False,
        },
    }
    (root/'experiments/results/prime-insertion-checks.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
