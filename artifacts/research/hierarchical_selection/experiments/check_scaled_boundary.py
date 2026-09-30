# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/hierarchical_selection/experiments/check_scaled_boundary.py
# Original SHA-256: ae8ca40bd771faef22642381e97e5bbd385bbdd6e2248a05e2a37c38ccad0f9e
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact-identity/scale diagnostics, not finite Weil eigenvalue certification."""
import sys
sys.dont_write_bytecode = True
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import mpmath as mp

mp.mp.dps = 85
OUT = Path(__file__).with_name("scaled_boundary_results.json")


def st(x):
    return mp.nstr(x, 48)


def phi(r, t):
    return mp.factorial(r) / (1 + 1j*t)**(r+1)


def matrix_J(m, h):
    H = mp.matrix([[mp.factorial(r+s)/mp.mpf(2)**(r+s+1)
                    for s in range(m+1)] for r in range(m+1)])
    if h is None:
        return H
    return H + mp.matrix([[2/mp.pi*mp.quad(lambda t: mp.re(phi(r,t))*mp.re(phi(s,t)),
                                          [h, mp.inf])
                            for s in range(m+1)] for r in range(m+1)])


profile_tests = []
for h in (mp.mpf(1), mp.mpf(2), mp.mpf(10), None):
    for m in (1, 2, 3):
        J = matrix_J(m, h)
        A = J[:m, :m]
        lower = mp.lu_solve(A, -J[:m, m:m+1])
        c = mp.matrix([lower[r] for r in range(m)] + [mp.mpf(1)])
        vals, _ = mp.eigsy(J)
        profile_tests.append({"h": "infinity" if h is None else st(h), "m": m,
                              "matrix": [[st(J[r,s]) for s in range(m+1)] for r in range(m+1)],
                              "eigenvalues": [st(x) for x in vals],
                              "monic_minimizing_profile_coefficients": [st(x) for x in c],
                              "monic_minimum": st((c.T*J*c)[0])})
        assert min(vals) > 0
        if h is None:
            expected = mp.mpf(factorial(m))**2/mp.mpf(2)**(2*m+1)
            assert abs((c.T*J*c)[0]-expected) < mp.mpf("1e-75")


def xi(w):
    s = mp.mpf("0.5") + 1j*w
    return (s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)/2).real


def theta_tail_profile(v, Y):
    # n>=2 omitted only in this diagnostic. At Y>=4*pi relative size < 1e-14;
    # values are labeled first-theta-term, not exact complete-kernel coefficients.
    y = Y*mp.exp(v/Y)
    return mp.exp(v/(4*Y)-(y-Y))*(y*y-mp.mpf("1.5")*y)/(Y*Y-mp.mpf("1.5")*Y)


fourier_tests = []
for lam in (2, 3, 4, 6):
    a = mp.log(lam); Y = mp.pi*lam**2; beta = 2*Y
    A = mp.exp(a/2-Y)*(Y*Y-mp.mpf("1.5")*Y)
    for target in (mp.mpf("0.35"), mp.mpf("0.5"), mp.mpf("0.8"), mp.mpf(1), mp.mpf(2)):
        n = max(1, int(mp.nint(target*a*beta/mp.pi)))
        w = mp.pi*n/a; x = w/beta
        tail = mp.quad(lambda v: theta_tail_profile(v,Y)*mp.cos(x*v), [0,1,4,16,64,256])
        bulk = beta/(2*A)*(-1)**n*xi(w)/4
        fourier_tests.append({"lambda": lam, "Y": st(Y), "grid_n": n,
                              "scaled_frequency": st(x),
                              "normalized_full_transform": st(bulk),
                              "normalized_first_theta_tail_cosine": st(tail),
                              "limiting_tail_cosine": st(1/(1+x*x)),
                              "normalized_restriction_coefficient_diagnostic": st(bulk-tail),
                              "tail_convention": "First theta term; finite-v quadrature. Not a certified exact coefficient."})

scalar = []
for h in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2), mp.mpf(10)):
    direct = mp.mpf("0.5")+2/mp.pi*mp.quad(lambda t: (1+t*t)**-2,[h,mp.inf])
    closed = 1-(mp.atan(h)+h/(1+h*h))/mp.pi
    assert abs(direct-closed) < mp.mpf("1e-80")
    scalar.append({"h":st(h),"J_e_minus_v":st(closed),"support_score_multiplier":st(2*closed)})

result = {"rh_status":"OPEN", "precision_digits":mp.mp.dps,
          "scope":"Profile identities and finite Fourier scale diagnostics only. No fit, no RH inference, no actual full ground diagonalization.",
          "jet_binomial_matrices": {str(m): [[comb(2*j+2,r) for j in range(m+1)]
                                             for r in range(m+1)] for m in (1,2,3)},
          "effective_profile_tests":profile_tests,
          "first_theta_fourier_diagnostics":fourier_tests,
          "scalar_profile_identity_checks":scalar}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({"output":str(OUT),"profile_problems":len(profile_tests),
                  "Fourier_diagnostics":len(fourier_tests),"scope":result["scope"]},indent=2))
