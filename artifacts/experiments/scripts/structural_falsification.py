#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/structural_falsification.py
# Original SHA-256: e506ed716790741da3d417fd3abf36e1343b52c72e9986f970d9ce139445cfac
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Structural-track falsification; toy models, NOT tests or evidence for RH.

Uses exact rational identities where indicated, otherwise NumPy binary64.
No physical constants or equations from the inspiration PDF are inputs.
"""
import json
import math
import cmath
from fractions import Fraction as F
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
u = np.linspace(-16.0, 16.0, 32769)
integrate = lambda v: float(np.trapezoid(v, u))
norm2 = lambda v: integrate(np.abs(v)**2)
a = math.log(2.0)
w = a / math.sqrt(2.0)

def bump(x, scale=1.0):
    y = np.zeros_like(x)
    mask = np.abs(x) < scale
    y[mask] = np.exp(-1.0 / (1.0 - (x[mask]/scale)**2))
    return y

def shift(v, t):
    return (np.interp(u+t, u, v.real, left=0, right=0)
            + 1j*np.interp(u+t, u, v.imag, left=0, right=0))

rng = np.random.default_rng(20260929)
random_env = sum(rng.normal()*np.exp(-((u-c)/s)**2/2)
                 for c,s in zip(np.linspace(-3,3,9), np.linspace(.4,1.2,9)))
profiles = {
    'gaussian': np.exp(-u*u/8),
    'compact_smooth': bump(u, 3),
    'highly_localized': np.exp(-u*u/(2*.15**2)),
    'oscillatory': np.exp(-u*u/8)*np.cos(2*u),
    'high_frequency': np.exp(-u*u/8)*np.exp(20j*u),
    'near_boundary': bump(u-13, 2),
    'random_combination': random_env,
    'approximate_translation_eigenfunction': np.exp(-u*u/32),
}
prime_rows=[]
for label, env in profiles.items():
    samples=[]
    for k in np.linspace(-24,24,193):
        f=env*np.exp(1j*k*u)
        rayleigh=w*integrate((np.conj(f)*(shift(f,a)+shift(f,-a))).real)/norm2(f)
        samples.append((float(rayleigh),float(k)))
    val,k=min(samples)
    prime_rows.append(dict(family=label,minimum_rayleigh=val,carrier=k,
                           negative_candidate=val < -1e-8))

# Even polynomial with real coefficients and an exact off-axis quartet.
aa=F(1,4); bb=F(1)
coeff=[F(1),F(0),2*(bb*bb-aa*aa),F(0),(aa*aa+bb*bb)**2]
roots=np.roots([float(x) for x in coeff])
poly=lambda z: z**4+F(15,8)*z**2+F(289,256)
assert poly(complex(.25,1)) == 0
# P(i*t)=(t^2-15/16)^2+1/4, not just a sampled positivity claim.
assert F(289,256)-F(15,16)**2 == F(1,4)

unitary=[]
for beta in [-1.0,0.0,.5,1.0,2.0]:
    for gamma in [beta,.5]:
        t=.7
        # V_beta U_t^(gamma) f_beta, with V_beta f_beta=exp(-u²/2).
        v=np.exp((gamma-beta)*t)*np.exp(-(u+t)**2/2)
        ratio=norm2(v)/norm2(np.exp(-u*u/2))
        exact=math.exp(2*(gamma-beta)*t)
        unitary.append(dict(beta=beta,gamma=gamma,norm_ratio=ratio,
                            exact_ratio=exact,error=abs(ratio-exact)))

# One exact invariant infinite structure with positive small restrictions.
H=np.array([[1.,2.,0.],[2.,1.,0.],[0.,0.,3.]])
nested=[dict(dimension=n,min_eigenvalue=float(np.linalg.eigvalsh(H[:n,:n])[0]))
        for n in [1,2,3]]
assert F(1)+F(1)-4 == -2

def prime_power_weights(N):
    sieve=np.ones(N+1,dtype=bool);sieve[:2]=False
    for p in range(2,math.isqrt(N)+1):
        if sieve[p]:sieve[p*p::p]=False
    items=[]
    for p in np.flatnonzero(sieve):
        n=int(p)
        while n<=N:
            items.append((n,math.log(int(p))/math.sqrt(n)))
            n*=int(p)
    return sorted(items)

f=bump(u,.4).astype(complex)
f/=math.sqrt(norm2(f))
weights=prime_power_weights(10000)
corr={n:integrate((np.conj(f)*shift(f,math.log(n))).real)
      for n,_ in weights if math.log(n)<.8}
jump=[]
for cutoff in [2,10,100,1000,10000]:
    S=sum(wt for n,wt in weights if n<=cutoff)
    prime=2*sum(wt*corr.get(n,0.) for n,wt in weights if n<=cutoff)
    energy=2*S-prime
    jump.append(dict(cutoff=cutoff,S=S,jump_energy=energy,
                     subtracted_diagonal=2*S,renormalized_prime_term=energy-2*S))

# Discrete Fourier sampling toy. Gaussian is Schwartz, not compactly supported.
zeros=np.array([-2.,-1.,1.,2.])
sampling=[]
for R in [1.,2.,4.,8.,16.,32.,64.]:
    vec=np.exp(-(R*(zeros-1.))**2/2)
    nextvec=np.exp(-((2*R)*(zeros-1.))**2/2)
    sampling.append(dict(R=R,L2_norm_squared=1/(2*math.sqrt(math.pi)*R),
                         sampling_form=float(vec@vec),
                         sampling_difference=float((vec-nextvec)@(vec-nextvec))))

# Actual Weil mixed form for two disjoint normalized smooth bumps separated
# by log(3). Only that prime point lies in the correlation support.
# The smooth part is obtained from Connes--Consani (2023), (2.6)--(2.8),
# after setting the value at zero to zero and changing to logarithmic variables.
v=np.linspace(-1,1,4097)
dv=v[1]-v[0]
psi=bump(v)
psi/=math.sqrt(float(np.trapezoid(psi*psi,v)))
fft_size=16384
conv=np.fft.irfft(np.fft.rfft(psi,fft_size)**2,fft_size)[:8193]*dv
t=np.linspace(-2,2,8193)
a3=math.log(3.)
w3=a3/math.sqrt(3.)
cross=[]
for eps in [1/64,1/128,1/256,1/512]:
    x=a3+eps*t
    kernel=2*np.cosh(x/2)-np.exp(-x/2)/(1-np.exp(-2*x))
    smooth=eps*float(np.trapezoid(conv*kernel,t))
    b=smooth-w3
    cross.append(dict(epsilon=eps,mixed_Weil_form=b,prime_limit=-w3,
                       smooth_correction=smooth,
                       window_difference_2x2_determinant=-b*b))

# Nonnegative even compact kernel with a known off-axis Laplace zero.
h=bump(u,.4)
k=math.cosh(.25)*h+.5*bump(u-1,.4)+.5*bump(u+1,.4)
z=.25+1j*math.pi
laplace=np.trapezoid(k*np.exp(z*u),u)
kernel_counterexample=dict(z=[z.real,z.imag],minimum_sampled_kernel=float(k.min()),
    direct_Laplace_residual=abs(complex(laplace)),
    exact_factor_numerical_residual=abs(math.cosh(.25)+cmath.cosh(z)),
    exact_identity='L_k(z)=H(z)*(cosh(1/4)+cosh(z))')

# Simple self-adjoint truncation has linear, not T log T, eigenvalue count.
counts=[]
for T in [100,1000,10000]:
    L=1.
    counts.append(dict(T=T,periodic_dilation_positive_eigenvalues=math.floor(L*T/math.pi),
        Riemann_von_Mangoldt_main_term=T/(2*math.pi)*(math.log(T/(2*math.pi))-1),
        note='Second quantity is only the known main term, not an exact zeta zero count.'))

coercivity=[]
for R in [1.,2.,4.,8.,16.]:
    # t0=0 avoids the finite real sample set; norm is fixed.
    vec=math.sqrt(R)*np.exp(-(R*zeros)**2/2)
    coercivity.append(dict(R=R,L2_norm_squared=1/(2*math.sqrt(math.pi)),
                           sampling_form=float(vec@vec)))

ground_examples=[]
for label,M in [('positive_ground_vector_negative_energy',[[0.,-1.],[-1.,0.]]),
                 ('positive_eigenvector_not_ground_state',[[1.,2.],[2.,1.]])]:
    M=np.asarray(M)
    vpos=np.array([1.,1.])
    ground_examples.append(dict(name=label,spectrum=np.linalg.eigvalsh(M).tolist(),
        positive_vector_rayleigh=float(vpos@M@vpos/(vpos@vpos))))

def zeta_em(s, N=1000):
    # Finite Euler--Maclaurin approximation. This is a binary64 diagnostic,
    # with no interval claim. DLMF 25.11(iii) / 25.11.43.
    ans=sum(cmath.exp(-s*math.log(n)) for n in range(1,N))
    ans+=N**(1-s)/(s-1)+.5*N**(-s)
    for k,B in enumerate([1/6,-1/30,1/42,-1/30],1):
        rising=1.
        for j in range(2*k-1):rising*=s+j
        ans+=B/math.factorial(2*k)*rising*N**(-s-2*k+1)
    return ans

euler_probability=[]
for eps in [.1,.01,.001,.0001]:
    sigma=1+eps
    for tval in [0.,.5,2.]:
        zratio=zeta_em(sigma+1j*tval)/zeta_em(sigma)
        euler_probability.append(dict(sigma=sigma,t=tval,
              ratio=[zratio.real,zratio.imag],absolute_value=abs(zratio)))

out=dict(status='EXPERIMENTAL EVIDENCE — NOT RH EVIDENCE',
    arithmetic='Exact Fraction identities plus non-certified NumPy binary64 quadrature/eigenvalues',
    seed=20260929, source_paper_physical_inputs=[],
    symmetry=dict(coefficients=[str(x) for x in coeff],
                  roots=[[float(z.real),float(z.imag)] for z in roots],
                  exact_critical_axis_square_remainder='1/4'),
    dilation_norms=unitary,
    prime_translation=dict(form='(log 2)/sqrt(2) * (tau_log2 + tau_minus_log2)',
                           samples_per_family=193,families=prime_rows,
                           exact_gaussian_rayleigh_at_pi_over_log2=-2*w*math.exp(-a*a/4)),
    exact_restrictions=nested,
    prime_jump_renormalization=jump,
    nonclosable_sampling_toy=sampling,
    actual_Weil_window_cross_term=cross,
    positive_even_kernel=kernel_counterexample,
    dilation_eigenvalue_count=counts,
    uniform_coercivity_sampling_toy=coercivity,
    ground_state_counterexamples=ground_examples,
    Euler_probability_boundary=euler_probability,
    zeta_EM_sanity_error_at_2=abs(zeta_em(2)-math.pi**2/6),
    caveats=['No zeta zero search or RH conclusion.',
             'Positive prime coefficients do not make a translation sum positive semidefinite.',
             'Physical claims and constants from the source PDF are excluded.',
             'Discrete spectral samples are a toy, not substituted for the full Weil form.'])
path=ROOT/'experiments/results/structural_falsification.json'
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(output=str(path),negative_prime_families=sum(x['negative_candidate'] for x in prime_rows),
      tested_prime_samples=193*len(prime_rows),max_unitarity_error=max(x['error'] for x in unitary),
      polynomial_roots=out['symmetry']['roots'],nested_min_eigenvalues=nested,
      jump_energy_first_last=[jump[0],jump[-1]]),ensure_ascii=False,indent=2))
