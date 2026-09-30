# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/dyadic/check_reduction.py
# Original SHA-256: e66b23c603eafecee6ff690ab7865a647dcb830160ec2a3c09370332f363d6f2
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact arithmetic checks and numerical falsification probes, not RH evidence.

Run from the repository root with .venv-cert/bin/python.
All sums in the compact-bump numerical model are finite, including the
Möbius inverse. Quadrature / point samples do not certify the global bound.
"""
from pathlib import Path
import json
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 40
OUT = Path(__file__).with_name('reduction_checks.json')


def mobius_table(limit):
    mu = [1] * (limit + 1)
    primes = []
    marked = [False] * (limit + 1)
    for p in range(2, limit + 1):
        if not marked[p]:
            primes.append(p)
            for k in range(p, limit + 1, p):
                marked[k] = True
                mu[k] *= -1
            for k in range(p*p, limit + 1, p*p):
                mu[k] = 0
    mu[0] = 0
    return mu


MU = mobius_table(4096)
divisor_checks = [sum(MU[d] for d in range(1, r+1) if r % d == 0)
                  == (1 if r == 1 else 0) for r in range(1, 513)]
assert all(divisor_checks)


def bump(y, derivative=0):
    """Smooth compact H on [1,2]; its endpoints are exactly zero."""
    if y <= 1 or y >= 2:
        return mp.mpf(0)
    b = (y-1)*(2-y)
    h = mp.exp(-1/b)
    return h if derivative == 0 else h*(3-2*y)/(b*b)


integral_h = mp.quad(bump, [1, mp.mpf('1.5'), 2])


def chi(x, derivative=0):
    if x <= mp.mpf('.5'):
        return mp.mpf(0)
    if x >= 1:
        return mp.mpf(1 if derivative == 0 else 0)
    z = 2*x-1
    left, right = mp.exp(-1/z), mp.exp(-1/(1-z))
    val = left/(left+right)
    if derivative == 0:
        return val
    return 2*val*(1-val)*(1/z**2+1/(1-z)**2)


def psi(x, derivative=0):
    # Support [5/8,7/8] is a compact subset of the required open interval.
    return (4**(derivative+1))*bump(4*x-mp.mpf('1.5'), derivative)/integral_h


def raw(a, x, derivative=0):
    top = int(mp.floor(2*a/x))
    assert top < len(MU)
    return mp.fsum(MU[m]*(mp.mpf(m)/a)**derivative
                   *bump(m*x/a, derivative)
                   for m in range(1, top+1) if MU[m])/(2*mp.sqrt(a))


def moment(a):
    # Change variable y=mx/a. Break at both cutoff transition endpoints.
    terms = []
    for m in range(1, 4*a+1):
        if not MU[m]:
            continue
        points = sorted(set([mp.mpf(1), mp.mpf(2)] +
                            [z for z in [mp.mpf(m)/(2*a), mp.mpf(m)/a]
                             if 1 < z < 2]))
        val = mp.quad(lambda y: chi(a*y/m)*bump(y), points)
        terms.append(mp.mpf(MU[m])*val/m)
    return mp.sqrt(a)*mp.fsum(terms)/2


def corrected(a, x, c, derivative=0):
    if derivative == 0:
        return chi(x)*raw(a, x)-c*psi(x)
    return chi(x, 1)*raw(a, x)+chi(x)*raw(a, x, 1)-c*psi(x, 1)


def summed(a, x, c, derivative=0):
    return 2*mp.fsum((mp.mpf(m)**derivative)*corrected(a, m*x, c, derivative)
                    for m in range(1, int(mp.floor(2*a/x))+1))


rows = []
moments = {a: moment(a) for a in [1, 2, 4, 8, 16]}
for n in range(1, 5):
    a, c = 2**n, moments[2**n]
    right_errors = []
    recurrence_errors = []
    left_samples = []
    for x in [mp.mpf(1), mp.mpf('1.2'), mp.mpf('1.5'),
              mp.mpf(2), mp.mpf('2.3'), mp.mpf(3), mp.mpf(5),
              mp.mpf(9), mp.mpf(17)]:
        right_errors.append(abs(summed(a, x, c)-bump(x/a)/mp.sqrt(a)))
    for x in [mp.mpf(k)/16 for k in [3, 8, 10, 13, 16, 21, 29, 35]]:
        half = a//2
        k = ((chi(x)-chi(x/2))*raw(half, x/2)/mp.sqrt(2)
             -c*psi(x)+moments[half]*psi(x/2)/mp.sqrt(2))
        recurrence_errors.append(abs(corrected(a, x, c)
                                     -corrected(half, x/2, moments[half])/mp.sqrt(2)-k))
    for x in [mp.mpf(k)/16 for k in [2, 3, 4, 6, 8, 10, 12, 14, 16]]:
        hx = bump(x/a)/mp.sqrt(a)-summed(a, x, c)
        hp = bump(x/a, 1)/(a*mp.sqrt(a))-summed(a, x, c, 1)
        r, rt = mp.sqrt(x)*hx, mp.sqrt(x)*(hx/2+x*hp)
        weighted = (1-mp.log(x))/x*max(abs(r), abs(rt))
        left_samples.append(weighted)
    row = {
        'n': n, 'a': a,
        'moment_c_a': mp.nstr(c, 22),
        'max_right_identity_abs_error': mp.nstr(max(right_errors), 8),
        'max_archimedean_recurrence_abs_error': mp.nstr(max(recurrence_errors), 8),
        'sampled_left_p1_not_supremum': mp.nstr(max(left_samples), 18),
        'sampled_left_p1_div_sqrt_a_logfactor': mp.nstr(
            max(left_samples)/(mp.sqrt(a)*(1+mp.log(a))), 18)
    }
    assert max(right_errors) < mp.mpf('1e-30')
    assert max(recurrence_errors) < mp.mpf('1e-30')
    rows.append(row)

# Exact dyadic-only Beurling closure obstruction, as interval constants.
# Tail A/x ->0 forces A->0; the first two intervals force c0=-1,c1=1.
c0, c1 = Fraction(-1), Fraction(1)
nb_constants = [-c0, -2*c0-c1, -3*c0-c1]
assert nb_constants == [1, 1, 2]

# Synthetic off-line character checks preserve, rather than project away,
# the forward growth 2^(delta*n). The reflection partner supplies +|delta|.
synthetic = [{'delta': str(d), 'n': 40,
              'absolute_multiplier': mp.nstr(mp.power(2, d*40), 18)}
             for d in [mp.mpf('-.2'), mp.mpf(0), mp.mpf('.2')]]

result = {
    'rh_status': 'OPEN',
    'purpose': 'finite arithmetic identities and numerical falsification only',
    'precision_decimal_digits': mp.mp.dps,
    'exact_divisor_identities_checked': len(divisor_checks),
    'compact_bump': 'H(x)=exp(-1/((x-1)(2-x))) for 1<x<2, zero otherwise',
    'rows': rows,
    'dyadic_beurling_interval_limits': list(map(str, nb_constants)),
    'synthetic_offline_character': synthetic,
    'all_checks_passed': True,
    'limitations': [
        'Quadrature and sampled seminorm values are not interval certificates.',
        'Samples do not prove the infinite-series theorem or its global bound.',
        'No zero search, RH inference, or numerical fit to an asymptotic rate.'
    ]
}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
