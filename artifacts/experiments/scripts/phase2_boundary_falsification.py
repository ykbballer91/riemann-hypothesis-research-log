#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/phase2_boundary_falsification.py
# Original SHA-256: baf35026ab916a96036a21610f404798e282209a9437e84c15039e18da028196
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact rational obstruction and non-certified Newman normalization checks."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import mpmath as mp

mp.mp.dps=55
def phi(u):
    u=abs(u)
    return mp.fsum((4*mp.pi**2*n**4*mp.exp(9*u/2)-6*mp.pi*n**2*mp.exp(5*u/2))
                   *mp.exp(-mp.pi*n*n*mp.exp(2*u)) for n in range(1,13))

p0=phi(mp.mpf(0))
p2=mp.diff(phi,mp.mpf(0),2)
z=mp.mpc('1','.3')
gauss=mp.exp(-z*z/4)
checks=[]
for T in (8,32,128):
    # Fixed finite integration and integer summation: diagnostics, not interval certificates.
    value=2/mp.sqrt(mp.pi)/p0*mp.quad(lambda x: mp.exp(-x*x)*phi(x/mp.sqrt(T))*mp.cos(z*x),[0,1,2,4,8,12])
    expansion=gauss*(1+p2/(2*p0*T)*(mp.mpf('.5')-z*z/4))
    checks.append({'T':T,'error_to_gaussian':mp.nstr(abs(value-gauss),18),
                   'error_to_two_term':mp.nstr(abs(value-expansion),18),
                   'T_squared_error':mp.nstr(T*T*abs(value-expansion),18)})

# For F=((z-1)^2+1/16)((z+1)^2+1/16), m=-F'/F, z=1+i/5.
exact_im=-20+Fraction(20,9)-Fraction(20,1601)+Fraction(180,1681)
assert exact_im<0
root=mp.pi+1j*mp.acosh(2)
out={
 'proves_RH':False,'refutes_RH':False,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'synthetic_herglotz_test':{'point':'1+i/5','imaginary_part_exact':str(exact_im),
                          'strictly_negative_proved_by_rational_arithmetic':True,
                          'has_actual_Euler_Gamma':False},
 'synthetic_heat_test':{'kernel_measure':'2 delta_0 + (delta_1+delta_-1)/2',
                        'time':'0','zero':'pi+i acosh(2)','exact_reason':'cos(pi+i a)=-cosh(a)',
                        'numerical_residual_noncertified':mp.nstr(abs(2+mp.cos(root)),8),
                        'real_zero_threshold':'log(2)','has_actual_Euler_Gamma':False},
 'actual_newman_compactification':{'certified':False,'precision_decimal_digits':55,
                                  'theta_integer_cutoff':12,'integration_cutoff':12,
                                  'purpose':'Sign and normalization diagnostic of analytically proved local uniform asymptotic.',
                                  'samples':checks}}
path=Path(__file__).resolve().parents[2]/'experiments/results/phase2-boundary-falsification.json'
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
