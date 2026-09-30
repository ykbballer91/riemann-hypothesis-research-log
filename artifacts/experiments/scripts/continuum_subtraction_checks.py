#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/continuum_subtraction_checks.py
# Original SHA-256: 2c1537e5c30fddab4608acf1818b542e8084ae81b768cadced74878685408df9
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Bounded checks of a canonical corrected theta family, not of RH."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import mpmath as mp
from flint import arb, ctx


def minus_half_dilation(p):
    # (D_t - 1/2)[e^(t/2) p(x)e^(-x)], x=pi e^(2t).
    out = [Q(0)] * (len(p) + 1)
    for j, c in enumerate(p):
        out[j] += 2*j*c
        out[j+1] -= 2*c
    return out


def product(p, q):
    out = [Q(0)]*(len(p)+len(q)-1)
    for j, a in enumerate(p):
        for k, b in enumerate(q):
            out[j+k] += a*b
    return out


def gaussian_norm_sqrt_two(p):
    # sqrt(2)|| e^(t/2) p(pi e^(2t))e^(-pi e^(2t)) ||_2^2.
    # Integral moment times sqrt(2) is (1/2)_j / 2^(j+1).
    ans, rising = Q(0), Q(1)
    for j, c in enumerate(product(p, p)):
        if j:
            rising *= Q(2*j-1, 2)
        ans += c*rising / 2**(j+1)
    return ans


def main():
    kpoly = [Q(0), Q(-6), Q(4)]
    assert gaussian_norm_sqrt_two(kpoly) == Q(33, 32)
    assert gaussian_norm_sqrt_two(minus_half_dilation(kpoly)) == Q(1203, 128)
    # Exact square comparison proves E_2 < E_1; no rounding is involved.
    square_gap = Q(112**2, 25**2*5) - Q(11**2, 4**2*2)
    assert square_gap == Q(23283, 100000) > 0
    assert 378125 < 401408

    ctx.prec = 192
    c = arb.const_euler() + (4*arb.pi()).log()
    d1 = -c/64
    e1 = 3/(2*arb(2).sqrt())
    e2 = 17/(4*arb(2).sqrt()) - 112/(25*arb(5).sqrt())
    assert d1 < 0 and e2-e1 < 0
    def exact_energy_ball(nmax):
        double = arb(0)
        for n in range(1, nmax+1):
            for m in range(1, nmax+1):
                q = arb(n*n+m*m)
                double += 6*n*n*m*m/(q*q*q.sqrt())
        cross = arb(0)
        for n in range(1, nmax+1):
            q = arb(n*n+nmax*nmax)
            cross += 4*nmax**3/(q*q.sqrt())
        return double-cross+arb(2).sqrt()*nmax
    assert (exact_energy_ball(1)-e1).contains(0)
    assert (exact_energy_ball(2)-e2).contains(0)

    # Independent finite-interval integration, WITHOUT certified tails.
    mp.mp.dps = 60
    def r1(t):
        x = mp.pi*mp.exp(2*t)
        return 4*x*(x-1)*mp.exp(t/2-x)
    fhalf = mp.quad(lambda t: r1(t)*mp.cosh(t/2), [-50, -10, 0, 2, 4])
    dyhalf = mp.quad(lambda t: t*r1(t)*mp.sinh(t/2), [-50, -10, 0, 2, 4])
    d_quad = fhalf*dyhalf/2
    d_formula = -(mp.euler+mp.log(4*mp.pi))/64
    assert abs(fhalf-mp.mpf(1)/4) < mp.mpf('1e-40')
    assert abs(d_quad-d_formula) < mp.mpf('1e-39')

    energies = []
    for nmax in (1, 2):
        def u_and_derivative(t):
            et = mp.exp(t)
            a = mp.exp(-t/2)*mp.erf(mp.sqrt(mp.pi)*nmax*et)
            vs = [mp.exp(t/2-mp.pi*n*n*et*et) for n in range(1,nmax+1)]
            u = a-2*mp.fsum(vs)
            du = -a/2+2*nmax*mp.exp(t/2-mp.pi*nmax*nmax*et*et)
            du -= 2*mp.fsum((mp.mpf(1)/2-2*mp.pi*n*n*et*et)*v
                           for n,v in enumerate(vs,1))
            return u, du
        def energy_integrand(t):
            u,du = u_and_derivative(t)
            return du*du+u*u/4
        value = mp.quad(energy_integrand, [-25, -5, 0, 3, 20, 100])
        formula = (3/(2*mp.sqrt(2)) if nmax == 1 else
                   17/(4*mp.sqrt(2))-112/(25*mp.sqrt(5)))
        assert abs(value-formula) < mp.mpf('1e-38')
        energies.append({'N': nmax, 'quadrature': mp.nstr(value, 42),
                         'absolute_difference': mp.nstr(abs(value-formula), 8)})

    result = {
        'status': 'CONVERGENCE_REPAIRED_PSD_PROPAGATION_REJECTED',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proves_RH': False, 'refutes_RH': False, 'main_graph_merge': False,
        'exact_checks': {
            'k_norm_squared_times_sqrt_two': '33/32',
            'k_flux_norm_squared_times_sqrt_two': '1203/128',
            'energy_square_comparison_gap': str(square_gap),
            'all_N_negative_D_bound': '-(EulerGamma+log(4*pi))/64',
            'finite_endpoint_value': '1/4', 'actual_xi_endpoint_value': '1/2',
        },
        'interval_checks': {
            'precision_bits': 192, 'energy_N1': str(e1), 'energy_N2': str(e2),
            'energy_increment': str(e2-e1), 'D_N1_at_i_over_2': str(d1),
            'energy_increment_negative': True, 'D_negative': True,
        },
        'noncertified_independent_integrals': {
            'precision_decimal_digits': 60, 'certified': False,
            'method': 'mpmath quad on fixed finite intervals; no certified tails',
            'F1_at_i_over_2': mp.nstr(fhalf, 42),
            'D1_from_integrals': mp.nstr(d_quad, 42),
            'D_absolute_difference': mp.nstr(abs(d_quad-d_formula), 8),
            'energies': energies,
        },
        'scope': 'Canonical finite corrected kernels; no negativity claim about actual K_Phi or Weil form',
        'analytic_proofs': 'research/continuum_subtraction.md',
    }
    root = Path(__file__).resolve().parents[2]
    (root/'experiments/results/continuum-subtraction-checks.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
