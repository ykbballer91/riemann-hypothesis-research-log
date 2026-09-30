# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/one_prime/check_returns.py
# Original SHA-256: 7aac7a8822280fe7b74a3f27b412d74a77c6ffb109064718e6fcc57abfbf3dd9
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Finite diagnostics for analytic counterexamples; not zeta-zero experiments."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import mpmath as mp

mp.mp.dps = 70

def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def transpose(a):
    return [list(row) for row in zip(*a)]

def power(a, n):
    result = [[F(1), F(0)], [F(0), F(1)]]
    for _ in range(n):
        result = matmul(result, a)
    return result

I = [[F(1), F(0)], [F(0), F(1)]]
T = [[F(1), F(1)], [F(0), F(1)]]
Ti = [[F(1), F(-1)], [F(0), F(1)]]
for n in range(1, 21):
    assert power(T, n) == [[F(1), F(n)], [F(0), F(1)]]
    assert matmul(power(T, n), power(Ti, n)) == I

D = [[F(5,4), F(0)], [F(0), F(4,5)]]
B = [[F(0), F(1)], [F(1), F(0)]]
assert matmul(transpose(D), matmul(B, D)) == B
hyperbolic = {str(n): str(F(5,4)**abs(n)) for n in [-20,-10,-1,0,1,10,20]}

# Diagnostic complex frequency is synthetic, not an actual zeta zero.
alpha = mp.mpf(1)/5
interpolation = []
for theta in [mp.mpf(0),mp.mpf('0.1'),mp.mpf('0.2'),mp.mpf('0.3'),mp.mpf(1)]:
    a = theta
    interpolation.append({
        'theta':str(theta),
        'return_log_rate':str(a*mp.log(2)),
        'synthetic_evaluation_bounded':bool(a>alpha),
        'evaluation_norm_squared':str(a/(a*a-alpha*alpha)) if a>alpha else None,
    })

# Local Haar unitary, dense intertwiner, but linear global norm growth.
intertwiner_errors = []
linear_growth_ratios = []
for j in [4,10,30]:
    eta = mp.exp(2j*mp.pi/(2**j))
    delta = abs(eta-1)
    U = mp.matrix([[1,0],[0,eta]])
    J = mp.matrix([[delta,1],[0,delta]])
    A = mp.matrix([[1,(eta-1)/delta],[0,eta]])
    intertwiner_errors.append(mp.norm(J*U-A*J))
    n = 10
    linear_growth_ratios.append({'j':j,'offdiagonal_over_n':str(abs(eta**n-1)/(delta*n))})
assert max(intertwiner_errors) < mp.mpf('1e-60')

# A unitary Poisson dilation is not an intertwiner: test f(z)=z^{-1}.
r = F(1,2)
assert F(1) != r*r

# Dense synthetic kernel of off-axis evaluation in bare L2:
# e^{-alpha R} translated Gaussian has fixed evaluation and norm -> 0.
gaussian_correction_norms = [
    {'R':R,'l2_norm':str(mp.exp(-alpha*R)*(mp.pi/2)**mp.mpf('0.25'))}
    for R in [10,100,1000]
]

# Fixed finite Jordan blocks are polynomial; no uniform-in-block-size estimate.
block_diagnostics = []
for size in [64,256,1024]:
    a, n = 0.5, 8
    vp = [1/math.sqrt(size)]*size
    vm = [(-1)**i/math.sqrt(size) for i in range(size)]
    for _ in range(n):
        vp = [vp[i]+a*(vp[i+1] if i+1<size else 0) for i in range(size)]
        y = [0.0]*size
        y[-1] = vm[-1]
        for i in range(size-2,-1,-1): y[i] = vm[i]-a*y[i+1]
        vm = y
    block_diagnostics.append({
        'block_size':size,'iterate':n,
        'positive_norm_over_exponential_bound':math.sqrt(sum(v*v for v in vp))/(1+a)**n,
        'inverse_norm_over_exponential_bound':math.sqrt(sum(v*v for v in vm))*(1-a)**n,
    })
assert all(0.7<d['positive_norm_over_exponential_bound']<=1 for d in block_diagnostics)
assert all(0.7<d['inverse_norm_over_exponential_bound']<=1 for d in block_diagnostics)

out = {
    'exact_fraction_checks_passed':True,
    'scope':'Synthetic counterexample diagnostics; not an actual-zeta norm estimate',
    'certified_asymptotic_claims':False,
    'analytic_proofs_in_notes':True,
    'prime':2,
    'hyperbolic_norms':hyperbolic,
    'interpolation_thresholds':interpolation,
    'dense_intertwiner_max_error':str(max(intertwiner_errors)),
    'dense_intertwiner_linear_growth_diagnostic':linear_growth_ratios,
    'dilation_counterexample':{'PUf':'1','TPf':str(r*r)},
    'dense_kernel_correction_norms':gaussian_correction_norms,
    'jordan_block_uniformity_diagnostic':block_diagnostics,
    'mpmath_precision':mp.mp.dps,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_name('return_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
