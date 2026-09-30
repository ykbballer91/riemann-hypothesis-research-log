#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/silva_degree_four_certificate.py
# Original SHA-256: 97cc252a36fbc4bd32ac219e306ddc3ebae42741d079ae010c91e73525b84409
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Certify the degree-four numerator obstruction, not an RH result.

Integrate the theta profile with Arb complex ball quadrature and bound
both omitted theta terms and the infinite integration tail analytically.
The transform Z_4 is checked separately: U_4 and Z_4 have different loci.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import flint
from flint import acb, arb, ctx

ctx.prec = 160
pi = arb.pi()
K, T = 4, 2

# For v>=0, Phi(v) = sum (4*pi²*n⁴*exp(9v/2)
# -6*pi*n²*exp(5v/2))*exp(-pi*n²*exp(2v)).
# This is the bilateral kernel; its even extension transforms to Xi.
# The paired profile integrand is <= 8*pi²*sum n⁴ exp(5v-pi*n²*exp(2v)).
# y=exp(2v), y^(3/2)<=y² (y>=1) gives the following tail majorants.
def coefficient(y):
    return 4*pi**2*(y*y/pi + 2*y/pi**2 + 2/pi**3)

first = K + 1
n_tail = coefficient(arb(1)) * first**4 * (-pi*first**2).exp() / (1 - 16*(-pi*(2*first+1)).exp())
y = arb(2*T).exp()
v_tail = coefficient(y) * (-pi*y).exp() / (1 - 16*(-3*pi*y).exp())
tail = n_tail + v_tail
assert tail < arb('1e-29')

def profile(x):
    p = x*(1-x)
    def integrand(v, analytic):
        # Meromorphic operations only: poles automatically give nonfinite balls.
        exp2 = (2*v).exp()
        phi = acb(0)
        for n in range(1, K+1):
            phi += (4*pi**2*n**4*(arb(9)/2*v).exp()
                    - 6*pi*n*n*(arb(5)/2*v).exp()) * (-pi*n*n*exp2).exp()
        return 2*phi*(v/2).cosh() / (1 + 4*p*(v/2).sinh()**2)
    z = acb.integral(integrand, 0, T, rel_tol=arb('1e-27'), abs_tol=arb('1e-27'))
    assert z.is_finite() and z.imag.contains(0)
    return z.real + arb(0, tail.upper())

p0 = profile(arb(0))
assert p0.contains(arb(1)/2)
a, b = profile(arb(1)/4)/p0, profile(arb(1)/2)/p0
d = 4*a*a - 6*b + 2
assert d < arb('-0.00024124')
# Z_4/P0 = A*z^4 + B*z² + C, z=s-1/2.
A = (1-4*a+3*b)/12
B = (43-28*a-15*b)/24
C = (35+20*a+9*b)/64
disc = B*B-4*A*C
assert A > 0 and B > 0 and C > 0 and disc > 0
# Thus both roots in z² are negative: all four Z4 roots are on Re(s)=1/2.
ga, gb = Fraction(1133,1508), Fraction(377,502)
gd = 4*ga*ga-6*gb+2
assert gd == Fraction(-35390625,142697516)
ga2, gb2 = Fraction(1493,1508), Fraction(497,502)
AA, BB, CC = (1-4*ga2+3*gb2)/12, (43-28*ga2-15*gb2)/24, (35+20*ga2+9*gb2)/64
generic_z_disc = BB*BB-4*AA*CC
assert generic_z_disc == Fraction(-425455975,143268306064)
out = dict(status='DEGREE_FOUR_CERTIFIED', proves_RH=False, refutes_RH=False,
           refutes_Silva_stated_theorems=False,
           U4_has_no_unit_circle_zero=True, Z4_all_zeros_on_critical_line=True,
           precision_bits=ctx.prec, python_flint_version=flint.__version__,
           theta_terms=K, integration_endpoint=T,
           omitted_theta_bound=n_tail.str(40,more=True),
           integration_tail_bound=v_tail.str(40,more=True),
           P0=p0.str(40,more=True), a=a.str(40,more=True), b=b.str(40,more=True),
           numerator_quarter_discriminant=d.str(40,more=True),
           Z4_coefficients={k:v.str(40,more=True) for k,v in [('A',A),('B',B),('C',C),('discriminant',disc)]},
           generic_Stieltjes_counterexample_discriminant=str(gd),
           generic_Stieltjes_Z4_counterexample_discriminant=str(generic_z_disc),
           author_code_executed=False,
           source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
dest = Path('experiments/results/silva-degree-four-certificate.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(saved=str(dest),U4_discriminant=out['numerator_quarter_discriminant'],
                     Z4_discriminant=out['Z4_coefficients']['discriminant']),indent=2))
