# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/scale_flow/check_flow.py
# Original SHA-256: 101f2803234de82da4e391ba4301d816fc4dfebf5817d79df043f209e645c8f8
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact obstruction checks; optional high-precision diagnostics are not certificates."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import mpmath as mp

def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def tr(a):
    return [list(t) for t in zip(*a)]

def congr(m, g):
    return mul(tr(m), mul(g, m))

I = [[F(1), F(0)], [F(0), F(1)]]
J = [[F(0), F(1)], [F(-1), F(0)]]
B = [[F(0), F(1)], [F(1), F(0)]]
M = [[F(5,4), F(0)], [F(0), F(4,5)]]
assert congr(M, J) == J and congr(M, B) == B
assert mul(B, mul(M, B)) == [[F(4,5), F(0)], [F(0), F(5,4)]]
assert F(1) < F(5,4)**2 < F(2)  # 0 < log(5/4)/log(2) < 1/2

# The invariant symmetric forms have diagonal coefficients zero and free cross term.
diagonal_constraints = [M[0][0]**2-1, M[1][1]**2-1]
assert all(c != 0 for c in diagonal_constraints)

# One-period unitarity is sufficient for an equivalent invariant norm, not the original norm.
Q = [[F(0), F(-2)], [F(1,2), F(0)]]
G = [[F(5,8), F(0)], [F(0), F(5,2)]]
assert congr(Q, G) == G and congr(Q, I) != I
assert mul(mul(Q, Q), mul(Q, Q)) == I

# p=2, finite unramified cyclotomic quotient (Z/5Z)^*: return = inverse Frobenius.
fiber = [1, 2, 3, 4]
deck = {h: 2*h % 5 for h in fiber}
ret = {h: 3*h % 5 for h in fiber}
assert all(deck[ret[h]] == h for h in fiber)
z, orbit = 1, []
while z not in orbit:
    orbit.append(z)
    z = ret[z]
assert len(orbit) == 4 and z == 1

mp.mp.dps = 70
alpha = mp.log(mp.mpf(5)/4)/mp.log(2)
k = mp.mpf(3)/4
weighted_integral = mp.quad(lambda t: mp.exp(2*alpha*t-2*k*abs(t)), [-mp.inf, 0, mp.inf])
weighted_exact = k/(k*k-alpha*alpha)
assert abs(weighted_integral-weighted_exact) < mp.mpf('1e-60')
mode_errors = []
for j in range(4):
    chi_p = mp.exp(2j*mp.pi*j/4)
    for n in [-1, 0, 1]:
        omega = (2*mp.pi*n-2*mp.pi*j/4)/mp.log(2)
        mode_errors.append(abs(chi_p*mp.exp(1j*omega*mp.log(2))-1))
assert max(mode_errors) < mp.mpf('1e-60')

out = {
    'scope': 'Concrete counterexamples and convention checks; not verification of RH',
    'exact_checks_passed': True,
    'symplectic_and_indefinite_conservation': True,
    'time_reversal': True,
    'positive_invariant_matrix_impossible': 'Both diagonal entries forced zero; only off-diagonal forms remain',
    'offline_parameters_in_critical_strip': True,
    'one_period_example_original_norm_invariant': False,
    'one_period_example_averaged_norm_invariant': True,
    'finite_cover_return_cycle': orbit,
    'finite_cover_period_over_log_2': 4,
    'numeric_certified': False,
    'precision_decimal_digits': mp.mp.dps,
    'alpha': str(alpha),
    'weighted_functional_norm_squared': str(weighted_exact),
    'quadrature_error': str(abs(weighted_integral-weighted_exact)),
    'finite_character_descent_max_error': str(max(mode_errors)),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_name('flow_checks.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
