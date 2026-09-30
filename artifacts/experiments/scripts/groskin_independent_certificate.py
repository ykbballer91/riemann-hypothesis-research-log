#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/groskin_independent_certificate.py
# Original SHA-256: a8d277e17898f39a86d4729a9c47534a6db0d087f4a1ccbaca58d891f7e239e8
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Small finite Weil block: independent Arb quadrature and interval LDL.

No zero ordinates, RH assumption, or imported author code is used to assemble
the matrix. See proofs/audits/groskin-computation.md for conventions and scope.
Run with .venv-cert/bin/python. Requires python-flint 0.9.0.
"""
import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path

import flint
from flint import acb, arb, ctx


def serial(x):
    return x.str(60, more=True)


def prime_powers(c):
    for p in range(2, c + 1):
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        q = p
        while q <= c:
            yield q, p
            q *= p


def build(c, N, bits):
    assert c >= 2 and N >= 0 and bits >= 128
    ctx.prec = bits
    L, pi, I = arb(c).log(), arb.pi(), acb(0, 1)
    tol = arb(2) ** (-(bits - 32))
    moments, details = [], []
    for n in range(N + 1):
        w = 2 * pi * n / L

        # x rho(x) = exp(x/2)/(2 sinh(x)/x). sinc handles x=0.
        def base(z):
            return (z / 2).exp() / (2 * (I * z).sinc())

        def integ(fn):
            z = acb.integral(fn, 0, L, abs_tol=tol, rel_tol=tol,
                             eval_limit=200000, depth_limit=40)
            assert z.is_finite() and z.imag.contains(0)
            return z.real

        S = integ(lambda z, _: w * base(z) * (w * z).sinc()) if n else arb(0)
        CC = integ(lambda z, _: -w*w*z/2 * base(z) * (w*z/2).sinc()**2) if n else arb(0)
        XC = integ(lambda z, _: base(z) * (w*z).cos())
        moments.append((S, CC, XC))
        details.append(dict(n=n, S=serial(S), CC=serial(CC), XC=serial(XC)))

    # Integral from L to infinity of rho is atanh(a)+atan(a), a=exp(-L/2).
    a = (-L / 2).exp()
    K = pi.log() - (arb(1)/4).digamma() - 2*a.atanh() - 2*a.atan()
    beta = L / (4*pi)
    pole_pref = L * (arb(c).sqrt() + 1/arb(c).sqrt() - 2)/(2*pi*pi)
    pp = [(arb(p).log()/arb(q).sqrt(), arb(q).log()) for q,p in prime_powers(c)]
    inds = list(range(-N, N+1))

    def signed_S(n):
        return moments[abs(n)][0] * (1 if n >= 0 else -1)

    matrix = [[arb(0) for _ in inds] for _ in inds]
    for j,n in enumerate(inds):
        for k,m in enumerate(inds[j:], j):
            pole = pole_pref * (beta*beta-m*n)/((m*m+beta*beta)*(n*n+beta*beta))
            if n == m:
                _, CC, XC = moments[abs(n)]
                arch = -K - 2*CC + 2*XC/L
                prime = -sum((2*wt*(1-y/L)*(2*pi*n*y/L).cos() for wt,y in pp), arb(0))
            else:
                arch = (signed_S(m)-signed_S(n))/(pi*(m-n))
                prime = -sum((wt*((2*pi*m*y/L).sin()-(2*pi*n*y/L).sin())/(pi*(n-m))
                              for wt,y in pp), arb(0))
            matrix[j][k] = matrix[k][j] = pole + arch + prime
    return matrix, details, K


def ldlt(matrix):
    n = len(matrix)
    lower = [[arb(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for j in range(n):
        lower[j][j] = arb(1)
        # Explicit multiplication also encloses balls straddling zero. In the
        # installed binding, generic arb ** 2 returns nan for such input balls.
        d = matrix[j][j] - sum((lower[j][k]*lower[j][k]*pivots[k] for k in range(j)), arb(0))
        assert d > 0 or d < 0, f"uncertified pivot {j}: {d}"
        pivots.append(d)
        for i in range(j+1, n):
            lower[i][j] = (matrix[i][j]-sum((lower[i][k]*lower[j][k]*pivots[k]
                                           for k in range(j)), arb(0)))/d
    return pivots, lower


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--c', type=int, default=13)
    p.add_argument('--N', type=int, default=4)
    p.add_argument('--bits', type=int, default=192)
    p.add_argument('--output', default='experiments/results/groskin-c13-n4-independent.json')
    args = p.parse_args()
    mat, moments, K = build(args.c, args.N, args.bits)
    pivots, lower = ldlt(mat)
    h7 = acb(arb(1)/4,arb(7)/2).digamma().real-arb.pi().log()
    assert h7 > 0 and h7 < arb('0.1072')
    result = dict(kind='finite_block_interval_certificate', rh_status='OPEN',
                  proves_RH=False, source_code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  python_flint_version=flint.__version__, c=args.c, N=args.N,
                  dimension=len(mat), precision_bits=args.bits,
                  assembly='independent direct analytic Arb quadrature for S, CC, XC; no author import',
                  analytic_justification='proofs/audits/groskin-computation.md',
                  n_positive=sum(x>0 for x in pivots), n_negative=sum(x<0 for x in pivots),
                  h_plus_7=serial(h7), K=serial(K), moments=moments,
                  matrix=[[serial(x) for x in row] for row in mat],
                  ldlt_pivots=[serial(x) for x in pivots],
                  ldlt_unit_lower=[[serial(x) for x in row] for row in lower],
                  limitations=['finite c,N only', 'analytic identities audited on paper, not Lean',
                               'trusted Arb/FLINT implementation and runtime',
                               'does not certify the published c=100,N=200 example'])
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['c','N','dimension','precision_bits','n_positive','n_negative','h_plus_7']}))
    print('pivot balls:', result['ldlt_pivots'])


if __name__ == '__main__':
    main()
