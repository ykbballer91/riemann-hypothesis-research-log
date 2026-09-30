#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/internal_kernel_checks.py
# Original SHA-256: 3c9b0f626383a1844013bd793b7828e60abdf9549494974a0bd2b2480be0d9ce
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact toy-kernel falsification; the quadrature is only a numerical cross-check.

Run with .venv-cert/bin/python. This neither proves nor refutes RH.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import mpmath as mp
from flint import arb, ctx

ZERO = (0, 0, 0)


def scalar(c):
    return {ZERO: F(c)} if c else {}


def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: v * c for k, v in p.items() if v * c}


def mul(p, q):
    out = {}
    for k, v in p.items():
        for ell, w in q.items():
            j = tuple(a + b for a, b in zip(k, ell))
            out[j] = out.get(j, F(0)) + v * w
    return {k: v for k, v in out.items() if v}


def power(p, n):
    q = scalar(1)
    for _ in range(n):
        q = mul(q, p)
    return q


def complex_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def complex_poly(coefficients, z):
    out = (F(0), F(0))
    for c in reversed(coefficients):
        out = complex_mul(out, z)
        out = (out[0] + c, out[1])
    return out


def main():
    # Symbols are (x, y, U), with U the square of the integration variable.
    x, y, U = ({(1, 0, 0): F(1)}, {(0, 1, 0): F(1)}, {(0, 0, 1): F(1)})
    alpha, b = F(3, 20), F(1, 100)
    D = scale(power(add(x, scale(y, -1)), 2), F(1, 4))
    H = scale(power(add(x, y), 2), F(1, 4))
    A = add(U, D)
    B2 = scale(mul(U, D), 4)
    # p((sqrt(U)+sqrt(D))^2) p((sqrt(U)-sqrt(D))^2).
    P = add(
        power(add(scalar(1), scale(A, alpha), scale(power(A, 2), b)), 2),
        mul(add(scalar(2*b-alpha*alpha), scale(A, -2*alpha*b),
                scale(power(A, 2), -2*b*b)), B2),
        scale(power(B2, 2), b*b),
    )
    C = {}
    for (i, j, k), v in P.items():
        # exp(2H) integral_H^infinity U^k exp(-2U) dU.
        J = add(*[scale(power(H, r), F(factorial(k), factorial(r)*2**(k-r+1)))
                  for r in range(k+1)])
        C = add(C, scale(mul({(i, j, 0): F(1)}, J), v/4))
    assert all(k == 0 and i <= 4 and j <= 4 for i, j, k in C)
    M = [[C.get((i, j, 0), F(0)) for j in range(5)] for i in range(5)]
    assert M == [list(row) for row in zip(*M)]
    assert (M[1][1], M[1][3], M[3][3]) == (F(29,40000), F(3,16000), F(1,40000))
    v = [F(-49,24), F(19,12), F(3), F(-43,12), F(25,24)]
    moments = [sum(v[j-1]*j**k for j in range(1,6)) for k in range(5)]
    assert moments == [0, 1, 0, F(-15,2), 0]
    q = sum(moments[i]*M[i][j]*moments[j] for i in range(5) for j in range(5))
    assert q == F(-109,160000)
    z = (F(6), F(1))
    pz = complex_poly([1732, 0, -72, 0, 1], z)
    dpz = complex_poly([0, -144, 0, 4], z)
    assert pz == (293,-24) and dpz == (-72,284)
    imag_log_derivative = (dpz[1]*pz[0]-dpz[0]*pz[1])/(pz[0]**2+pz[1]**2)-F(1,2)
    assert -imag_log_derivative == F(-76543,172850)
    assert alpha*alpha-2*b == F(1,400)  # all coefficients in h'(u) are positive
    discriminant = (alpha*alpha+4*alpha*b+6*b*b-4*b)/16
    assert discriminant == F(-109,160000)

    # Independent integration of the original kernel. Not interval arithmetic.
    mp.mp.dps = 70
    phi = lambda t: mp.exp(-t*t)*(1+mp.mpf(3)/20*t*t+mp.mpf(1)/100*t**4)
    def kernel(a, b):
        return mp.quad(lambda t: t*phi(t+(a-b)/2)*phi(t-(a-b)/2)/2,
                       [mp.mpf(a+b)/2, mp.inf])
    numerical = mp.fsum(
        mp.mpf(v[i].numerator)/v[i].denominator
        * mp.mpf(v[j].numerator)/v[j].denominator
        * mp.exp((i+1)**2+(j+1)**2)*kernel(i+1,j+1)
        for i in range(5) for j in range(5))
    error = abs(numerical-mp.mpf(q.numerator)/q.denominator)
    assert error < mp.mpf('1e-50')  # cross-check only; exact proof is above

    # Actual theta kernel, not the toy: a rigorous four-point log difference.
    # For X>=100 the relative n>=2 tail is <=64 exp(-3X): successive
    # n^4 factors grow by <6 and successive n^2 differences are >=5.
    # Both geometric-series denominators used below exceed 1/2.
    ctx.prec = 192
    first_logs = []
    for u in [4,5,6,7]:
        t = arb(u).sqrt()
        X = arb.pi()*(2*t).exp()
        assert X > 100
        assert 1-6*(-5*X).exp() > arb(1)/2
        assert 1-arb(3)/(2*X) > arb(1)/2
        first_logs.append((4*arb.pi()**2).log()+arb(9)/2*t-X
                          +(1-arb(3)/(2*X)).log())
    delta = first_logs[3]-3*first_logs[2]+3*first_logs[1]-first_logs[0]
    tail_error = 512*arb(-300).exp()  # sum of absolute difference coefficients is 8
    assert delta+tail_error < 0
    root = Path(__file__).resolve().parents[2]
    result = {
        'status': 'EXACT_TOY_COUNTEREXAMPLE_VERIFIED',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proves_RH': False, 'refutes_RH': False,
        'actual_Riemann_kernel_counterexample': False,
        'arithmetic': 'Python Fraction exact rational arithmetic',
        'coefficient_matrix': [[str(e) for e in row] for row in M],
        'nodes': [1,2,3,4,5],
        'weights_after_Gaussian_cancellation': [str(e) for e in v],
        'feature_moments': [str(e) for e in moments],
        'negative_Gram_value': str(q),
        'odd_block_determinant': str(M[1][1]*M[3][3]-M[1][3]**2),
        'negative_log_derivative_witness': str(-imag_log_derivative),
        'Fourier_quadratic_discriminant': str(discriminant),
        'numerical_cross_check': {
            'method': 'mpmath original integral, non-certified',
            'decimal_precision': 70,
            'value': mp.nstr(numerical,60),
            'absolute_error_against_exact': mp.nstr(error,8),
        },
        'order_one_extension': 'analytic existence by dominated convergence; no numerical epsilon claimed',
        'actual_theta_factor_cone_obstruction': {
            'arithmetic': 'Arb 192 bits plus analytic relative tail bound',
            'u_nodes': [4,5,6,7],
            'n_equals_one_log_third_difference': str(delta),
            'absolute_omitted_tail_bound': str(tail_error),
            'negative_certified': True,
            'scope': 'excludes the Gaussian real-linear-factor cone, not RH',
        },
    }
    (root/'experiments/results/internal-kernel-checks.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
