#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/silva_jacobi_certificate.py
# Original SHA-256: dbb9aaaadd6339a1453a547660c958edddfb103dbea558172b3736cbdb5b7d9c
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Test only the E=0,2,4,6 monic Silva sequence for a Jacobi recurrence.

No author code is imported. The profile quadrature and uniform omitted-term
bound follow the already audited silva_degree_four_certificate.py.
"""
from fractions import Fraction
from math import comb, factorial
import hashlib
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx

ctx.prec = 192
pi = arb.pi()
K, T = 4, 2


def tail_coefficient(y):
    return 4*pi*pi*(y*y/pi + 2*y/(pi*pi) + 2/(pi*pi*pi))


first = K + 1
n_tail = (tail_coefficient(arb(1))*first**4*(-pi*first**2).exp()
          / (1 - 16*(-pi*(2*first+1)).exp()))
y = arb(2*T).exp()
v_tail = tail_coefficient(y)*(-pi*y).exp() / (1 - 16*(-3*pi*y).exp())
tail = n_tail + v_tail
assert tail > 0 and tail < arb('1e-29')


def aq(q):
    return arb(q.numerator)/q.denominator


def profile(x):
    p = x*(1-x)

    def integrand(v, analytic):
        exp2 = (2*v).exp()
        phi = acb(0)
        for n in range(1, K+1):
            phi += (4*pi*pi*n**4*(arb(9)/2*v).exp()
                    - 6*pi*n*n*(arb(5)/2*v).exp()) * (-pi*n*n*exp2).exp()
        sh = (v/2).sinh()
        return 2*phi*(v/2).cosh() / (1 + 4*p*sh*sh)

    value = acb.integral(integrand, 0, T,
                         rel_tol=arb('1e-32'), abs_tol=arb('1e-32'))
    assert value.is_finite() and value.imag.contains(0)
    return value.real + arb(0, tail.upper())


def exact_transform_rows(E):
    """Group j,E-j before interval arithmetic; retain z=s-1/2 powers."""
    rows = {}
    for j in range(E+1):
        x = min(Fraction(j, E), Fraction(E-j, E))
        p = [Fraction(1)]
        for k in range(E):
            c = Fraction(E-j-k)-Fraction(1, 2)
            new = [Fraction(0)]*(len(p)+1)
            for degree, value in enumerate(p):
                new[degree] += c*value
                new[degree+1] -= value
            p = new
        factor = Fraction((-1)**j*comb(E, j), factorial(E))
        row = rows.setdefault(x, [Fraction(0)]*(E+1))
        for k in range(E+1):
            row[k] += factor*p[k]
    assert all(row[k] == 0 for row in rows.values() for k in range(1, E+1, 2))
    return {x: row[::2] for x, row in rows.items()}


rows = {E: exact_transform_rows(E) for E in (2, 4, 6)}
points = sorted({x for r in rows.values() for x in r})
assert points == [Fraction(0), Fraction(1, 6), Fraction(1, 4),
                  Fraction(1, 3), Fraction(1, 2)]
samples = {x: profile(aq(x)) for x in points}
assert samples[Fraction(0)].contains(arb(1)/2)
coeffs = {}
monic = {0: [arb(1)]}
for E, r in rows.items():
    c = [sum((aq(row[k])*samples[x] for x, row in r.items()), arb(0))
         for k in range(E//2+1)]
    assert all(v.is_finite() for v in c) and c[-1] > 0
    coeffs[E] = c
    monic[E//2] = [v/c[-1] for v in c[:-1]] + [arb(1)]

# Independent closed E=4 coefficient dictionary from the prior audit.
a4 = samples[Fraction(1, 4)]/samples[Fraction(0)]
b4 = samples[Fraction(1, 2)]/samples[Fraction(0)]
closed4 = [(35+20*a4+9*b4)/64, (43-28*a4-15*b4)/24,
           (1-4*a4+3*b4)/12]
assert all((v/samples[Fraction(0)]).overlaps(w)
           for v, w in zip(coeffs[4], closed4))

# p1=u+a; p2=u²+b*u+c; p3=u³+d*u²+e*u+f.
a = monic[1][0]
c, b = monic[2][0:2]
f, e, d = monic[3][0:3]
alpha1 = a-b
beta1 = -alpha1*a-c
alpha2 = b-d
beta2 = c-alpha2*b-e
# p3 = (u-alpha2)*p2 - beta2*p1 + gamma*p0.
gamma = f+alpha2*c+beta2*a
assert gamma.is_finite() and not gamma.contains(0)
assert arb('21578447.73') < gamma < arb('21578447.74')
assert beta1 > 0 and beta2 > 0


def display(x):
    return x.str(45, more=True)


root = Path(__file__).resolve().parents[2]
source = root/'literature/source_cache/silva-2609.25564v1.html'
expected_source_hash = '907fd6a586d03f412da55be6fcbd89d73580170ec6fb6a013a20ffa655ac4d4d'
if source.is_file():
    assert hashlib.sha256(source.read_bytes()).hexdigest() == expected_source_hash
    source_cache_check = 'PRESENT_HASH_VERIFIED'
else:
    source_cache_check = 'ABSENT_EXPECTED_HASH_RECORDED_ONLY'
out = dict(
    status='FIXED_JACOBI_SEQUENCE_REJECTED',
    proves_RH=False, refutes_RH=False, refutes_Silva_stated_theorems=False,
    author_code_executed=False, degrees=[0, 2, 4, 6],
    p0_convention='1; monic normalization of any nonzero constant',
    variable='u=(s-1/2)^2', recurrence='p3=(u-alpha2)*p2-beta2*p1+gamma*p0',
    gamma_excludes_zero=True, gamma_coarse_enclosure=['21578447.73', '21578447.74'],
    beta1_positive=True, beta2_positive=True, precision_bits=ctx.prec,
    python_flint_version=flint.__version__, theta_terms=K, integration_endpoint=T,
    omitted_theta_bound=display(n_tail), integration_tail_bound=display(v_tail),
    profile_samples={str(x): display(v) for x, v in samples.items()},
    exact_coefficient_rows={str(E): {str(x): [str(v) for v in row]
                                  for x, row in r.items()} for E, r in rows.items()},
    coefficients_ascending_u={str(E): [display(v) for v in c] for E, c in coeffs.items()},
    monic_ascending_u={str(n): [display(v) for v in c] for n, c in monic.items()},
    alpha1=display(alpha1), beta1=display(beta1),
    alpha2=display(alpha2), beta2=display(beta2), gamma=display(gamma),
    limitations=['No exclusion of index-dependent changes of variable or other operators.',
                 'No extension beyond E=6; no claim about zeros from this recurrence test.'],
    source_html_sha256=expected_source_hash, source_cache_check=source_cache_check,
    source_cache_required_for_computation=False,
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
dest = root/'experiments/results/silva-jacobi-certificate.json'
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(dict(saved=str(dest), alpha2=out['alpha2'], beta2=out['beta2'],
                     gamma=out['gamma'], status=out['status'],
                     script_sha256=out['script_sha256']), indent=2))
