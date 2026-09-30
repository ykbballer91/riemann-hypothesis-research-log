# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/arithmetic_restoring_force/experiments/check_scalar_theta.py
# Original SHA-256: 32282d7dd8b1097fec4943f58f358d7e61e07d6f0f5791385e924186b3d3985f
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Finite diagnostics for the restoring-force audit. No RH inference.

mpmath values are precision cross-checks, not interval certificates.
The prime-sign domination margin is an exact rational inequality.
"""
from pathlib import Path
from fractions import Fraction
import json
import mpmath as mp

HERE = Path(__file__).resolve().parent
mp.mp.dps = 50

def xi(s):
    return s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)/2

def log_derivative(s):
    z = mp.zeta(s)
    return (1/s + 1/(s-1) - mp.log(mp.pi)/2
            + mp.digamma(s/2)/2 + mp.zeta(s, derivative=1)/z)

def curvature(s):
    z = mp.zeta(s)
    dz = mp.zeta(s, derivative=1)
    return (-1/s**2 - 1/(s-1)**2 + mp.polygamma(1, s/2)/4
            + mp.zeta(s, derivative=2)/z - (dz/z)**2)

def text(x):
    return mp.nstr(x, 32)

def complex_text(x):
    return {"real": text(mp.re(x)), "imag": text(mp.im(x))}

def phi(x):
    # Positive-half kernel. The first omitted n is 9; no new kernel is defined.
    return sum((4*mp.pi**2*n**4*mp.exp(9*x/2)
                -6*mp.pi*n**2*mp.exp(5*x/2))
               *mp.exp(-mp.pi*n*n*mp.exp(2*x)) for n in range(1,9))

def theta_parts(a,t):
    intervals = [mp.mpf(x) for x in ("0",".125",".25",".5",".75","1","1.5","2","3","4")]
    real=2*mp.quad(lambda x:phi(x)*mp.cosh(a*x)*mp.cos(t*x), intervals)
    imag=2*mp.quad(lambda x:phi(x)*mp.sinh(a*x)*mp.sin(t*x), intervals)
    return real,imag

grid=[]
for a0 in ("-.75","-.45","-.2","-.05",".05",".2",".45",".75"):
    for t0 in (0,1,5,8,10,12,14,15,18,20,25,30,40,50,75,100):
        a,t=mp.mpf(a0),mp.mpf(t0)
        s=mp.mpf(".5")+a+1j*t
        q=mp.re(log_derivative(s))
        grid.append({"a":str(a0),"t":t0,"a_times_dlogxi":text(a*q),
                     "curvature":text(mp.re(curvature(s)))})

center=[]
for t in (0,1,5,8,10,12,14,15,18,20,25,30,40,50,75,100):
    s=mp.mpf(".5")+1j*t
    center.append({"t":t,"dlogxi":text(mp.re(log_derivative(s))),
                   "curvature":text(mp.re(curvature(s)))})

gamma=mp.im(mp.zetazero(1))  # diagnostic ordinate only, not a simplicity assumption
near=[]
for a0 in (".01",".1",".3"):
    for dt0 in ("-.2","-.01","0",".01",".2"):
        a,dt=mp.mpf(a0),mp.mpf(dt0)
        s=mp.mpf(".5")+a+1j*(gamma+dt)
        near.append({"a":a0,"t_offset_from_first_zero":dt0,
                     "dlogxi":text(mp.re(log_derivative(s))),
                     "curvature":text(mp.re(curvature(s)))})

prime=[]
for t in (mp.mpf(0),mp.pi/mp.log(2)):
    s=8+1j*t
    prime.append({"sigma":8,"t":text(t),
                  "dlogzeta":text(mp.re(mp.zeta(s,derivative=1)/mp.zeta(s)))})
# log 2 > 1/2, log 3 < 2. For decreasing f(x)=log(x)/x^8:
# sum_{n>=3} f(n) <= f(3)+int_3^infty f(x)dx.
main_lower=Fraction(1,512)
tail_upper=Fraction(2,3**8)+Fraction(1,3**7)*(Fraction(2,7)+Fraction(1,49))
margin=main_lower-tail_upper
assert margin>0

integrals=[]
for a0,t0 in (("0","0"),(".2","0"),(".2","5"),(".3","14.1"),("-.2","25")):
    a,t=mp.mpf(a0),mp.mpf(t0)
    real,imag=theta_parts(a,t)
    exact=xi(mp.mpf(".5")+a+1j*t)
    err=abs(real+1j*imag-exact)
    assert err<mp.mpf("1e-42")
    integrals.append({"a":a0,"t":t0,"theta_real":text(real),"theta_imag":text(imag),
                      "xi":complex_text(exact),"absolute_difference":text(err)})

cross=[]
for a0,t0 in ((".1","0"),(".1",text(gamma)),("0","20"),(".45","100")):
    a,t=mp.mpf(a0),mp.mpf(t0)
    s=mp.mpf(".5")+a+1j*t
    q50=log_derivative(s); k50=curvature(s)
    with mp.workdps(80):
        q80=log_derivative(s); k80=curvature(s)
        cross.append({"a":a0,"t":t0,"q_difference_50_80dps":text(abs(q50-q80)),
                      "curvature_difference_50_80dps":text(abs(k50-k80))})

result={
 "purpose":"Finite identity/sign diagnostics and synthetic falsification; not an RH test",
 "precision_dps":50,"cross_check_dps":80,"interval_certification":False,
 "grid":grid,"center_curvature":center,"near_known_zero":near,
 "prime_sign_examples":prime,
 "prime_sign_exact_rational_margin":{
     "main_lower":str(main_lower),"tail_upper":str(tail_upper),
     "margin":str(margin),
     "proof":"log2>1/2, log3<2, Lambda(n)<=log n, integral tail; positive margin proves opposite signs at sigma8,t0 and t=pi/log2"},
 "theta_identity_checks":integrals,
 "theta_numeric_truncation":{"n_max":8,"x_max":4,"rigorous_integral_certificate":False},
 "precision_cross_checks":cross,
 "observations":{
   "grid_points":len(grid),
   "global_force_sign_counterexample_found":any(mp.mpf(r["a_times_dlogxi"])<=0 for r in grid),
   "negative_horizontal_curvature_found":any(mp.mpf(r["curvature"])<0 for r in grid+near),
   "negative_center_curvature_found":any(mp.mpf(r["curvature"])<0 for r in center),
   "global_sign_or_RH_proved_from_data":False
 }
}
(HERE/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({"observations":result["observations"],"prime_margin":str(margin),
 "maximum_theta_difference":text(max(mp.mpf(r["absolute_difference"]) for r in integrals)),
 "results":str(HERE/'results.json')},ensure_ascii=False,indent=2))
