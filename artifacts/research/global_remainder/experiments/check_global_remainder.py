# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/global_remainder/experiments/check_global_remainder.py
# Original SHA-256: 5e1a2f78e6b5e72c6cf437089144c567f3efbe7b97c79a191e129360453ec9a3
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Identity/falsification diagnostics; no RH inference, no interval certification."""
import json
import math
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp

mp.mp.dps = 50
OUT = Path(__file__).with_name("results.json")

def mobius_sieve(n):
    mu = [1] * (n + 1)
    primes = []
    composite = [False] * (n + 1)
    for p in range(2, n + 1):
        if not composite[p]:
            primes.append(p)
            for k in range(p, n + 1, p):
                composite[k] = True
                mu[k] *= -1
            for k in range(p*p, n + 1, p*p):
                mu[k] = 0
    mu[0] = 0
    return mu, primes

def K(s):
    return mp.sqrt(mp.pi) * mp.exp(s*s/4)

def inv_vertical(u, c, T):
    f = lambda t: K(c+1j*t)*mp.exp((c+1j*t)*u)/mp.zeta(c+1j*t)
    cuts = sorted(set([mp.mpf(0), min(mp.mpf(10), T),
                       min(mp.mpf(14), T), min(mp.mpf(15), T), T]))
    return mp.re(mp.quad(f, cuts))/mp.pi

N = 50000
mu, primes = mobius_sieve(N)
logs = [(mp.log(n), mu[n]) for n in range(1, N+1) if mu[n]]
samples = []
for u in [-2, 0, 2]:
    direct = mp.fsum(sign*mp.exp(-(u-v)**2) for v, sign in logs)
    # For n>N>exp(u), the summand is decreasing. The sum of omitted
    # absolute values is <= integral_N^infty exp(-(u-log x)^2) dx.
    tail = (mp.sqrt(mp.pi)/2 * mp.exp(u+mp.mpf(1)/4)
            * mp.erfc(mp.log(N)-u-mp.mpf(1)/2))
    right = inv_vertical(u, mp.mpf("1.5"), mp.mpf(16))
    # Absolute vertical tail at c>1: |1/zeta(c+it)| <= zeta(c)/zeta(2c).
    vertical_tail = (mp.exp(mp.mpf("1.5")*u+mp.mpf("1.5")**2/4)
                     * mp.zeta(mp.mpf("1.5"))/mp.zeta(3) * mp.erfc(8))
    samples.append(dict(u=u, R_truncated=str(direct), inversion=str(right),
                        absolute_series_tail_bound=str(tail),
                        absolute_vertical_tail_bound=str(vertical_tail),
                        observed_error=str(abs(direct-right))))
    assert abs(direct-right) < tail+vertical_tail+mp.mpf("1e-38")

# A finite contour calculation crosses -2 and the first conjugate zero pair.
# Numerically nonzero derivative is used ONLY for this diagnostic residue;
# the research theorem allows every multiplicity.
u = mp.mpf(1)
a, c, T = mp.mpf(-3), mp.mpf("1.5"), mp.mpf(16)
q = lambda s: K(s)*mp.exp(s*u)/mp.zeta(s)
right = inv_vertical(u, c, T)
left = inv_vertical(u, a, T)
top = mp.quad(lambda x: q(x+1j*T), [c, 0, a])/(2j*mp.pi)
bottom = mp.quad(lambda x: q(x-1j*T), [a, 0, c])/(2j*mp.pi)
rho = mp.zetazero(1)
res_nontriv = 2*mp.re(K(rho)*mp.exp(rho*u)/mp.diff(mp.zeta, rho))
res_trivial = K(-2)*mp.exp(-2*u)/mp.diff(mp.zeta, -2)
error = abs(right-left+top+bottom-res_nontriv-res_trivial)
assert error < mp.mpf("1e-35")
contour = dict(c=str(c), a=str(a), T=str(T), u=str(u),
               right=str(right), left=str(left),
               horizontal_sum=str(top+bottom),
               first_zero_pair_residue=str(res_nontriv),
               trivial_minus_two_residue=str(res_trivial), error=str(error))

# An explicitly symmetric meromorphic function has distinct inverse
# transforms in different convergence strips. Its off-axis poles persist.
a = mp.mpf("0.25")
def I(b, u):
    return mp.exp(b*u+b*b)*mp.erfc(-u/2-b)/2
def HR(u):
    return (I(a,u)-I(-a,u))/(2*a)
def HC(u):
    return -(I(-a,u)+I(-a,-u))/(2*a)
synthetic = []
for u in [-8, -2, 0, 2, 8, 24]:
    jump = mp.exp(a*a+a*u)/(2*a)
    reflection = mp.exp(a*a)*mp.sinh(a*u)/a
    assert abs(HR(u)-HC(u)-jump) < mp.mpf("1e-40")
    assert abs(HR(u)-HR(-u)-reflection) < mp.mpf("1e-40")
    synthetic.append(dict(u=u, right_inverse=str(HR(u)),
                          central_inverse=str(HC(u)),
                          contour_jump=str(jump)))

# Nonreal off-axis quartet: no common-amplitude or pointwise envelope
# assumption. Partial fractions give both prescribed inverse transforms.
qa, qgamma = mp.mpf("0.2"), mp.mpf(1)
roots = [qa+1j*qgamma, qa-1j*qgamma, -qa+1j*qgamma, -qa-1j*qgamma]
res = {r: 1/mp.fprod(r-s for s in roots if s != r) for r in roots}
quartet=[]
for u in [mp.mpf(0), 2*mp.pi, 4*mp.pi, 8*mp.pi]:
    qr = mp.fsum(res[r]*I(r,u) for r in roots)
    qc = mp.fsum(res[r]*(I(r,u) if mp.re(r)<0 else -I(-r,-u))
                 for r in roots)
    qjump = mp.fsum(res[r]*mp.exp(r*r+r*u) for r in roots if mp.re(r)>0)
    assert abs(qr-qc-qjump) < mp.mpf("1e-40")
    assert abs(mp.im(qr))+abs(mp.im(qc)) < mp.mpf("1e-40")
    quartet.append(dict(u=str(u), right_inverse=str(mp.re(qr)),
                        central_inverse=str(mp.re(qc)),
                        right_halfplane_residues=str(mp.re(qjump))))

# Exact rational polynomial finite-jet countermodels. Represent complex
# rational values by pairs; Q(z)=1+(z^2-1/4)^(N+1)*(A+B*z^2).
def cmul(x,y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def cinv(x):
    den=x[0]*x[0]+x[1]*x[1]
    return (x[0]/den,-x[1]/den)
def cpow(x,n):
    out=(F(1),F(0))
    for _ in range(n):
        out=cmul(out,x)
    return out
zstar=(F(1,5),F(2))
w=cmul(zstar,zstar)
v=(w[0]-F(1,4),w[1])
jets=[]
for order in [0,1,2,5,8]:
    inv=cinv(cpow(v,order+1))
    target=(-inv[0],-inv[1])
    B=target[1]/w[1]
    A=target[0]-B*w[0]
    val=cmul(cpow(v,order+1),(A+B*w[0],B*w[1]))
    assert val==(F(-1),F(0))
    jets.append(dict(jet_order=order, A=str(A), B=str(B),
                     Q_at_zstar="0 exactly",
                     jet_matching_reason="Q-1 divisible by (z^2-1/4)^(N+1)"))

# Every chosen derivative of the reciprocal Gamma factor has the stated
# nonzero slope. This checks the distinction from lost endpoint values.
gamma_checks=[]
for j in range(7):
    slope=mp.diff(lambda delta: mp.rgamma(-1-j+delta),0)
    exact=(-1)**(j+1)*math.factorial(j+1)
    assert abs(slope-exact)<mp.mpf("1e-40")
    gamma_checks.append(dict(j=j, slope=str(slope), exact=exact))

# Finite X polynomials S_z are exact counts; near-endpoint values are
# diagnostics only, not an asymptotic growth fit.
omega=[0]*(N+1)
for p in primes:
    for n in range(p,N+1,p):
        omega[n]+=1
parameter=[]
for x in [100,1000,10000]:
    coeff=[0]*(max(omega[:x+1])+1)
    for n in range(1,x+1):
        if mu[n]:
            coeff[omega[n]]+=1
    mertens=sum(mu[1:x+1])
    assert sum(c*(-1)**j for j,c in enumerate(coeff))==mertens
    values=[]
    for delta in [mp.mpf("-0.01"),mp.mpf(0),mp.mpf("0.01")]:
        val=mp.fsum(c*(-1+delta)**j for j,c in enumerate(coeff))
        values.append(dict(delta=str(delta), value=str(val)))
    parameter.append(dict(X=x, coefficients=coeff, M=mertens, values=values))

result=dict(purpose="Exact identity and synthetic falsification diagnostics only",
            numerical_status="50-digit floating arithmetic, not interval certified",
            gaussian_samples=samples, finite_contour=contour,
            synthetic_convergence_strips=synthetic, synthetic_nonreal_quartet=quartet,
            exact_finite_jets=jets,
            reciprocal_gamma_slopes=gamma_checks, finite_parameter_polynomials=parameter,
            assertions_passed=True, rh_inference=False)
OUT.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(dict(assertions_passed=True, gaussian_samples=len(samples),
                     finite_contour_error=str(error), finite_jets=len(jets),
                     nonreal_quartet_samples=len(quartet),
                     gamma_slopes=len(gamma_checks), parameter_polynomials=len(parameter),
                     output=str(OUT)),indent=2))
