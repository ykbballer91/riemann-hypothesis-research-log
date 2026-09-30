#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/imbalance_checks.py
# Original SHA-256: 9f7d952a6d460cafe12eb25157fda00ced57b6cf3fb73659c96ad7378112f17f
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Bounded checks for the rejected fixed-product imbalance proof route.

Arb checks are supplementary to the exact derivations in imbalance-reduction.md.
No zeta zero off the critical line is claimed or used.
"""
import hashlib
import json
from math import isqrt
from pathlib import Path

import flint
from flint import arb, acb, acb_series, ctx

ctx.prec = 224
ctx.cap = 4


def ser(x):
    return x.str(60, more=True)


def logderiv(x):
    z = acb_series([acb(x), 1], prec=2).zeta()
    value = -z[1]/z[0]
    assert value.imag.contains(0)
    return value.real


def energy(n, delta):
    return 4/arb(n)*(delta*arb(n).log()).sinh()**2


pp = []
N = 1000
for p in range(2, N+1):
    if any(p % d == 0 for d in range(2, isqrt(p)+1)):
        continue
    n, k = p, 1
    while n <= N:
        pp.append((n, p, k))
        n, k = n*p, k+1
pp.sort()

checks = []
for num, den in [(1,10), (1,4), (2,5)]:
    delta, u = arb(num)/den, arb(3)
    partial = sum((energy(n,delta)*arb(n)**(-3)/k for n,p,k in pp), arb(0))
    exact = (1+u+2*delta).zeta().log()+(1+u-2*delta).zeta().log()-2*(1+u).zeta().log()
    # Lambda(n)/log(n)<=1 and E_n<=2*n^(-1+2|delta|).
    exponent = u-2*delta
    tail_bound = 2*arb(N)**(-exponent)/exponent
    remainder = exact-partial
    assert partial > 0 and remainder > 0 and remainder < tail_bound
    checks.append(dict(delta=f'{num}/{den}', regulator='3', cutoff=N,
                       partial_prime_power_energy=ser(partial),
                       log_zeta_finite_difference=ser(exact),
                       remainder=ser(remainder), elementary_tail_bound=ser(tail_bound),
                       passed=True))

# Removing the regulator crosses a pole. A meromorphic continuation of a
# positive series can be negative; it is no longer the positive series.
u, delta = arb(1)/10, arb(1)/5
continued = logderiv(1+u+2*delta)+logderiv(1+u-2*delta)-2*logderiv(1+u)
assert continued < 0

# Nonzero values on the central line disprove replacement of E(Re(s)) by
# its holomorphic extension. This is an exact point, not a claimed zeta zero.
z = acb(0, arb.pi()/(2*arb(2).log()))
holomorphic = 2*(z*arb(2).log()).sinh()**2
assert holomorphic.real < -arb(19)/10 and holomorphic.imag.contains(0)

# Stronger exact toy: F(z)=cosh(1/4)+cosh(z), the bilateral Laplace transform
# of a positive symmetric three-point measure. F(1/4+i*pi)=0 exactly.
# Numerical inclusion supplements that symbolic identity.
z0 = acb(arb(1)/4, arb.pi())
toy_residual = (arb(1)/4).cosh()+z0.cosh()
toy_energy = energy(2, arb(1)/4)
assert toy_residual.contains(0) and toy_energy > 0

out = dict(kind='fixed_product_imbalance_adversarial_checks',
           rh_status='OPEN', proves_RH=False, refutes_RH=False,
           arithmetic='python-flint Arb/Acb', precision_bits=ctx.prec,
           python_flint_version=flint.__version__,
           source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           convergent_aggregate_checks=checks,
           continuation_counterexample=dict(u='1/10', delta='1/5',
               dirichlet_series_converges=False,
               meromorphic_finite_difference=ser(continued), negative_certified=True),
           holomorphic_extension_counterexample=dict(n=2,
               z='i*pi/(2*log(2))', real_amplitude_energy='0',
               holomorphic_extension=ser(holomorphic), exact_value='-2'),
           positive_measure_counterexample=dict(
               transform='cosh(1/4)+cosh(z)', zero='1/4+i*pi',
               exact_zero_proof='cosh(a+i*pi)=-cosh(a)',
               residual=ser(toy_residual), E2_at_real_part=ser(toy_energy),
               positive_energy_certified=True,
               scope='Refutes structural inference; not a counterexample to zeta/RH.'),
           decision='Stop this proof route: zero-implies-zero-energy is exactly RH; structural-only strengthening is false.')
path = Path('experiments/results/imbalance-checks.json')
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(dict(saved=str(path), checks='PASS',
                     continued_value=ser(continued), toy_energy=ser(toy_energy),
                     rh_status='OPEN'), indent=2))
