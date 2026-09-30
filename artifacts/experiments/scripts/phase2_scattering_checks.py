#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/phase2_scattering_checks.py
# Original SHA-256: c33d4a7b5edd2acda0c786273434cfc329cb7076bf9b7f7bd8cb27fa5dbd49a0
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Non-certified diagnostics of exact identities; no zero-location theorem."""
from pathlib import Path
import hashlib
import json
import mpmath as mp

mp.mp.dps = 70

def completed(s):
    return mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def scatter(s):
    return completed(2*s-1)/completed(2*s)

def clean(z):
    z = mp.mpc(z)
    return {"re": mp.nstr(z.real, 45), "im": mp.nstr(z.imag, 45)}

def ratio(u):
    return scatter((u+1)/2)*mp.gamma((u+1)/2)/(mp.sqrt(mp.pi)*mp.gamma(u/2))

u=mp.mpc('1.7','0.4')
product=mp.mpc(1)
reconstruction=[]
for j in range(32):
    product *= ratio(u+j)
    if j+1 in (4,8,16,32):
        exact=mp.zeta(u)/mp.zeta(u+j+1)
        reconstruction.append({"factors":j+1,"telescoping_error":mp.nstr(abs(product-exact),8),
                               "remaining_error_to_zeta":mp.nstr(abs(product-mp.zeta(u)),12)})

rho=mp.zetazero(1)  # A single diagnostic point, not completeness or certified isolation.
s0=rho/2
lambda0=s0*(1-s0)
cutoffs=[]
for a in (1,2,10):
    direct=mp.power(a,s0)*completed(2*s0)+mp.power(a,1-s0)*completed(2*s0-1)
    leading=mp.power(a,1-s0)*completed(2-rho)
    cutoffs.append({"a":a,"constant_term_abs":mp.nstr(abs(direct),30),
                    "noncancellation_identity_error":mp.nstr(abs(direct-leading),8)})

test_s=mp.mpc('1.8','0.4')
derivative=mp.diff(scatter,test_s)/scatter(test_s)
rhs=(mp.digamma(test_s-mp.mpf('.5'))-mp.digamma(test_s)
     +2*mp.zeta(2*test_s-1,derivative=1)/mp.zeta(2*test_s-1)
     -2*mp.zeta(2*test_s,derivative=1)/mp.zeta(2*test_s))

out={
 "precision_decimal_digits":mp.mp.dps,
 "certified":False,"proves_RH":False,"refutes_RH":False,
 "purpose":"Catch normalization, parameter and pole-versus-eigenvalue errors; analytic proofs are in the research note.",
 "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "functional_equation_errors":[mp.nstr(abs(scatter(s)*scatter(1-s)-1),8) for s in [mp.mpc('.31','2.3'),mp.mpc('1.2','.7')]],
 "unitarity_errors":[mp.nstr(abs(abs(scatter(mp.mpf('.5')+1j*t))-1),8) for t in [mp.mpf('1.2'),mp.mpf('4.7')]],
 "log_derivative_identity_error":mp.nstr(abs(derivative-rhs),8),
 "boundary_reconstruction":reconstruction,
 "sample_zeta_zero":clean(rho),"scattering_pole_parameter":clean(s0),"continued_laplacian_parameter":clean(lambda0),
 "imaginary_part_identity_error":mp.nstr(abs(lambda0.imag-rho.imag*(1-rho.real)/2),8),
 "actual_constant_term_at_scattering_pole":cutoffs
}
root=Path(__file__).resolve().parents[2]
(root/'experiments/results/phase2-scattering-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
