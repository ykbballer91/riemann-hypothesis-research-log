#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/spiral_scale_checks.py
# Original SHA-256: ab779348ed4487693dbade52b4fd69e86eb5b4f5764900b21509d306afb1dad2
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact/Arb countermodel checks for the spiral-scale audit, never for RH itself.

Rational matrix identities are exact. Arb checks of symbolic entire identities
are consistency checks; equality and all-parameter statements are proved in
proofs/audits/spiral-scale-adversarial.md. Winding samples are explicitly floats.
"""
from fractions import Fraction as Q
from pathlib import Path
import cmath
import hashlib
import json
import math

import flint
from flint import arb, acb, ctx


def mul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return list(map(list, zip(*A)))


def det(A):
    if len(A) == 1:
        return A[0][0]
    return sum(((-1)**j*A[0][j]*det(
        [r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A))), Q(0))


def ident(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def serial_matrix(A):
    return [[str(x) for x in row] for row in A]


def gaussian_mul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def main():
    ctx.prec = 192
    R = [[Q(3,5), -Q(4,5)], [Q(4,5), Q(3,5)]]
    M = [[Q(0) for j in range(4)] for i in range(4)]
    J = [[Q(0) for j in range(4)] for i in range(4)]
    G = [[Q(0) for j in range(4)] for i in range(4)]
    C = [[Q(0) for j in range(4)] for i in range(4)]
    for i in range(2):
        for j in range(2):
            M[i][j], M[i+2][j+2] = 2*R[i][j], R[i][j]/2
        J[i][i+2], J[i+2][i] = Q(1), Q(-1)
        G[i][i+2] = G[i+2][i] = Q(1)
        C[i][i+2] = C[i+2][i] = Q((-1)**i)
    assert det(M) == 1
    assert mul(mul(tr(M), J), M) == J
    assert mul(mul(tr(M), G), M) == G
    assert mul(C, C) == ident(4)
    assert mul(mul(mul(C, M), C), M) == ident(4)
    gram = mul(tr(M), M)
    assert gram == [[Q(4 if i < 2 else 1, 1 if i < 2 else 4)
                     if i == j else Q(0) for j in range(4)] for i in range(4)]
    v = [[Q(1)], [Q(0)], [Q(1)], [Q(0)]]
    orbits = []
    for k in range(11):
        conserved = mul(mul(tr(v), G), v)[0][0]
        norm2 = mul(tr(v), v)[0][0]
        assert conserved == 2
        assert norm2 == Q(4)**k+Q(1,4)**k
        orbits.append(dict(iterate=k, indefinite_energy=str(conserved),
                           euclidean_norm_squared=str(norm2)))
        v = mul(M, v)

    real_scattering = []
    for t in map(Q, [-5,-2,-1,0,1,2,5]):
        nr, ni = t*t-5, -2*t
        dr, di = t*t-5, 2*t
        assert nr*nr+ni*ni == dr*dr+di*di > 0
        real_scattering.append(dict(t=str(t), modulus_squared="1"))
    for x in (Q(-2), Q(2)):
        z = (x,Q(-1))
        z2 = gaussian_mul(z,z)
        iz2 = gaussian_mul((Q(0),Q(2)),z)
        D = (z2[0]+iz2[0]-5,z2[1]+iz2[1])
        N = (z2[0]-iz2[0]-5,z2[1]-iz2[1])
        assert D == (0,0) and N != (0,0)

    def polynomial(z, a):
        return ((z-a)**2+1)*((z+a)**2+1)
    winding = []
    for a in (0.0,0.125,0.25):
        values = [polynomial(2*cmath.exp(2j*math.pi*k/2048),a)
                  for k in range(2048)]
        number = sum(cmath.phase(values[(k+1)%len(values)]/values[k])
                     for k in range(len(values)))/(2*math.pi)
        winding.append(dict(a=a, sampled_winding=number,
                            status="float diagnostic; exact root count is 4"))

    pi, log8 = arb.pi(), arb(8).log()
    floor = arb(3)/2-arb(2).sqrt()
    assert floor > 0
    def selfsimilar(z):
        return (1-2*(-z*log8).exp())*(1-2*(-(1-z)*log8).exp())
    def cosh_formula(z):
        return arb(3)/2-arb(2).sqrt()*((z-arb(1)/2)*log8).cosh()
    zeros = []
    for numerator in (1,2):
        for k in range(-2,3):
            z = acb(arb(numerator)/3,2*pi*k/log8)
            ball = selfsimilar(z)
            assert ball.contains(0) and abs(ball) < arb(2)**-160
            zeros.append(dict(real_part=f"{numerator}/3", period_index=k,
                              value_enclosure=str(ball)))
    z = acb(arb(1)/5,arb(3)/7)
    checks = [selfsimilar(z)-cosh_formula(z),
              selfsimilar(z)-selfsimilar(1-z),
              selfsimilar(z+acb(0,2*pi/log8))-selfsimilar(z)]
    assert all(v.contains(0) for v in checks)
    ratio = Q(1,4)
    finite_sum = sum((ratio**j for j in range(9)),Q(0))
    exact_tail = ratio**9/(1-ratio)
    assert finite_sum+exact_tail == Q(4,3)

    z1 = acb(1,arb(1)/4)
    z2 = z1.conjugate()
    w1 = (acb(0,1)*z1).exp()
    w2 = -(acb(0,1)*z2).exp()
    jq = (w1*w2.conjugate()+w2*w1.conjugate()).real
    assert jq.contains(-2)
    out = dict(
        kind="spiral_scale_countermodels", rh_status="OPEN",
        proves_RH=False, disproves_RH=False,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        arithmetic=dict(rational="Python Fraction", balls="Arb/ACB",
                        python_flint_version=flint.__version__, precision_bits=192),
        expanding_reversible_flow=dict(
            matrix=serial_matrix(M), determinant="1",
            symplectic_identity=True, indefinite_energy_identity=True,
            involutive_time_reversal=True, positive_norm_preserved=False,
            eigenvalue_moduli=["2","2","1/2","1/2"], orbits=orbits),
        meromorphic_unitary_boundary=dict(
            formula="((z-i)^2-4)/((z+i)^2-4)",
            genuine_poles=["-2-i","2-i"], real_samples=real_scattering,
            scope="unitary meromorphic scalar toy; no zeta identification"),
        quartet_winding=winding,
        selfsimilar_model=dict(
            formula="(1-2*8^(-s))*(1-2*8^(-(1-s)))",
            symbolic_identity="3/2-sqrt(2)*cosh((s-1/2)*log(8))",
            critical_line_uniform_positive_floor=floor.str(50),
            zeros=zeros, identities_consistent=True,
            identity_status="symbolically proved; balls only check consistency",
            geometric_sum_at_s1=str(finite_sum),
            geometric_tail_at_s1=str(exact_tail), total_at_s1="4/3"),
        indefinite_pair_translation=dict(
            parameter="1", frequencies=["1+i/4","1-i/4"],
            original_energy="-2", translated_energy=jq.str(50)),
        limitations=[
            "Synthetic models only; no counterexample to zeta or RH.",
            "Finite floating winding values are not a topology certificate.",
            "No Hilbert eigenmode identification for zeta is asserted.",
            "No fixed-window expansion or numerical Weil certificate is attempted."
        ])
    path = Path(__file__).resolve().parents[1]/"results"/"spiral-scale-checks.json"
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(path)
    print("PASS: exact matrix identities, rational scattering poles, Arb model checks")


if __name__ == "__main__":
    main()
