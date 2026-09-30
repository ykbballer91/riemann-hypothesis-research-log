# STATUS: RIEMANN HYPOTHESIS OPEN
# Public credit: @ykbballer91; AI-assisted
# SPDX-License-Identifier: MIT
# Source: research/full_ground_capture/priority2/experiments/finite_head_probe.py
# Original SHA-256: 3a958083eea64a993cb3c23188b32c23bacd03536de3f6469b34b49a0c49251c
"""Priority 2 only: actual sharp-support even Fourier heads.

Floating high-precision diagnostics are NOT rank certificates.
The companion Arb program certifies the analytic sufficient criterion.
Run: python finite_head_probe.py --dps 85 --quad 144 --output probe_85.json
Dependencies: mpmath. No old research file is read or modified.
"""
from pathlib import Path
import argparse
import json
import mpmath as mp


def polynomials(order):
    out = [[mp.mpf(0), -mp.mpf(3)/2, mp.mpf(1)]]
    for _ in range(order):
        p = out[-1]
        q = [mp.mpf(0)] * (len(p)+1)
        for l, c in enumerate(p):
            q[l] += (mp.mpf('0.5') + 2*l)*c
            q[l+1] -= 2*c
        out.append(q)
    return out


def xi(w):
    s = mp.mpf('0.5') + 1j*w
    return mp.re(s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s))


def derivatives(t, polys):
    y0 = mp.pi*mp.exp(2*t)
    out = [mp.mpf(0)] * len(polys)
    # Diagnostics only: explicit finite theta sum, checked by precision change.
    for q in range(1, 17):
        y = y0*q*q
        fac = mp.exp(t/2-y)
        for r, p in enumerate(polys):
            out[r] += mp.polyval(p[::-1], y)*fac
    return out


def base_tail(a, w):
    """Integral over |t|>a of k(t) exp(-iwt), via upper incomplete Gamma."""
    ans = mp.mpf(0)
    for q in range(1, 17):
        b = mp.pi*q*q
        y = b*mp.exp(2*a)
        factor = b**(-mp.mpf(1)/4 + 1j*w/2)
        gamma = (mp.gammainc(mp.mpf(9)/4-1j*w/2, y, mp.inf)
                 - mp.mpf(3)/2*mp.gammainc(mp.mpf(5)/4-1j*w/2, y, mp.inf))
        ans += mp.re(factor*gamma)
    return ans


def matrices(a, N, m, polys):
    A, E = mp.matrix(N+1, m+1), mp.matrix(N+1, m+1)
    boundary = derivatives(a, polys)
    samples = []
    for n in range(N+1):
        w = mp.pi*n/a
        q = -w*w
        kappa = 1/mp.sqrt(2*a) if n == 0 else (-1)**n/mp.sqrt(a)
        d = mp.sqrt(2/a) if n == 0 else 2/mp.sqrt(a)
        samples.append(xi(w))
        A[n, 0] = kappa*samples[-1]/4
        E[n, 0] = kappa*base_tail(a, w)
        for j in range(1, m+1):
            A[n, j] = q*A[n, j-1]
            E[n, j] = q*E[n, j-1] - d*boundary[2*j-1]
    return A, E, A-E, samples


def quadrature(a, N, m, polys, nodes, weights):
    B, G = mp.matrix(N+1, m+1), mp.matrix(m+1)
    for x, wt in zip(nodes, weights):
        t = a*(x+1)/2
        weight = a*wt  # twice the integral on [0,a]
        f = derivatives(t, polys)[::2]
        for j in range(m+1):
            for l in range(m+1):
                G[j, l] += weight*f[j]*f[l]
        for n in range(N+1):
            scale = (1/mp.sqrt(2*a) if n == 0 else (-1)**n/mp.sqrt(a))
            scale *= mp.cos(mp.pi*n*t/a)*weight
            for j in range(m+1):
                B[n, j] += scale*f[j]
    return B, G


def singular(A):
    return list(mp.svd(A, compute_uv=False))


def specnorm(A):
    return singular(A)[0]


def true_gram_singular(B, G):
    L = mp.cholesky(G)
    return singular(B*(L.T**-1))


def fmt(x):
    return mp.nstr(x, 35)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dps', type=int, default=85)
    ap.add_argument('--quad', type=int, default=144)
    ap.add_argument('--output', default='probe_85.json')
    args = ap.parse_args()
    mp.mp.dps = args.dps
    nodes, weights = mp.gauss_quadrature(args.quad, 'legendre')
    polys = polynomials(12)
    _, Gfull = quadrature(mp.mpf(4), 0, 6, polys, nodes, weights)
    cases = [('regular', mp.mpf(a), N) for a, N in
             [('0.5', 2), ('1', 2), ('1', 4), ('1.5', 4), ('2', 4), ('2', 6)]]
    gamma1 = mp.im(mp.zetazero(1))
    cases.append(('grid_hit_diagnostic_not_exact_numeric_equality', mp.pi/gamma1, 1))
    records = []
    for label, a, N in cases:
        m = N
        A, E, B, samples = matrices(a, N, m, polys)
        Bquad, Gsupport = quadrature(a, N, m, polys, nodes, weights)
        raw = singular(B)
        ideal = singular(A)
        physical = true_gram_singular(B, Gfull[:m+1, :m+1])
        support = true_gram_singular(B, Gsupport)
        ideal_whitened_tail = None
        if label == 'regular':
            ideal_whitened_tail = specnorm(E*(A**-1))
        record = {
            'label': label, 'a': fmt(a), 'N': N, 'm': m,
            'Xi_grid_values': [fmt(v) for v in samples],
            'ideal_sigma_min': fmt(ideal[-1]),
            'actual_sigma_min': fmt(raw[-1]),
            'actual_raw_condition': fmt(raw[0]/raw[-1]),
            'tail_operator_norm': fmt(specnorm(E)),
            'tail_relative_to_ideal_min': fmt(specnorm(E)/ideal[-1]),
            'tail_times_ideal_inverse_norm': None if ideal_whitened_tail is None else fmt(ideal_whitened_tail),
            'actual_global_Gram_singular_values': [fmt(v) for v in physical],
            'actual_support_Gram_singular_values': [fmt(v) for v in support],
            'largest_global_subspace_angle_radians': fmt(mp.acos(min(mp.mpf(1), physical[-1]))),
            'quadrature_crosscheck_relative': fmt(mp.norm(B-Bquad)/max(1, mp.norm(B))),
            'diagnostic_full_rank_relative_1e_45': bool(raw[-1] > raw[0]*mp.mpf('1e-45')),
            'minimal_m_diagnostic': N,
            'rank_is_a_proof': False,
            'projected_subspace_angles_if_full_rank': 'all zero by equality with the head; this is not a lift-cost estimate',
        }
        records.append(record)
        print(label, fmt(a), N, 'sigma', fmt(raw[-1]), 'physical', fmt(physical[-1]), flush=True)
    result = {
        'scope': 'PRIORITY 2 ONLY; RH OPEN; floating diagnostics, not rank proof',
        'mpmath_version': mp.__version__, 'decimal_precision': args.dps,
        'Gauss_Legendre_nodes': args.quad, 'theta_terms': 16,
        'global_Gram_integration_interval': [-4, 4],
        'global_Gram_tail': 'omitted only for numerical diagnostics; no theorem uses these quadratures',
        'records': records,
    }
    output = Path(__file__).parent/args.output
    output.write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
