# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/common_parent/experiments/rayleigh_probe.py
# Original SHA-256: f6081ea013dd69fb03e96ada816325223565a97aece95b55b29e1083e8eacd74
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Step 31 diagnostic: actual finite Weil form and actual projected prolate proxy.

Only NumPy required. No zero ordinates, RH assumption, or symmetrization of k.
This is floating-point falsification/identity checking, not certification.
The Weil formula is independently assembled from exact prime/pole/arch terms
and checked against a pre-existing Arb matrix. Prolate modes use a Legendre
Ritz matrix; resolution is doubled as a diagnostic only.
"""
from pathlib import Path
from functools import lru_cache
import json, math, re
import numpy as np
from numpy.polynomial.legendre import leggauss, legval

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent


@lru_cache(None)
def gl(n):
    return leggauss(n)


def prime_powers(cut):
    for p in range(2, int(math.floor(cut)) + 1):
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            continue
        q = p
        while q <= cut:
            yield q, p
            q *= p


def weil(cut, N, quad=320):
    """cut=lambda^2, L=log(cut), basis V_j=(-1)^j exp(2pi i j t/L)/sqrt L."""
    L = math.log(cut)
    x, wg = gl(quad)
    x = (x + 1) * L / 2
    wg = wg * L / 2
    base = x * np.exp(x / 2) / (2 * np.sinh(x))  # x*rho(x)
    omega = 2 * math.pi * np.arange(N + 1) / L
    ox = omega[:, None] * x[None, :]
    S = np.sum(wg * base * omega[:, None] * np.sinc(ox / math.pi), axis=1)
    CC = np.sum(wg * base * (-omega[:, None]**2 * x / 2)
                * np.sinc(ox / (2 * math.pi))**2, axis=1)
    XC = np.sum(wg * base * np.cos(ox), axis=1)
    a = math.exp(-L / 2)
    K = math.log(math.pi) + np.euler_gamma + math.pi/2 + 3*math.log(2)
    K -= 2*math.atanh(a) + 2*math.atan(a)
    beta = L / (4 * math.pi)
    pref = L * (math.sqrt(cut) + 1/math.sqrt(cut) - 2) / (2*math.pi**2)
    pp = [(math.log(p)/math.sqrt(q), math.log(q)) for q, p in prime_powers(cut)]
    inds = np.arange(-N, N + 1)
    mats = {k: np.zeros((len(inds), len(inds))) for k in ('arch','pole','prime')}
    for j, n in enumerate(inds):
        for k, m in enumerate(inds):
            mats['pole'][j,k] = pref*(beta*beta-m*n)/((m*m+beta*beta)*(n*n+beta*beta))
            if n == m:
                mats['arch'][j,k] = -K-2*CC[abs(n)]+2*XC[abs(n)]/L
                mats['prime'][j,k] = -sum(2*wt*(1-y/L)*math.cos(2*math.pi*n*y/L)
                                         for wt,y in pp)
            else:
                mats['arch'][j,k] = (np.sign(m)*S[abs(m)]-np.sign(n)*S[abs(n)])/(math.pi*(m-n))
                mats['prime'][j,k] = -sum(wt*(math.sin(2*math.pi*m*y/L)
                                           -math.sin(2*math.pi*n*y/L))/(math.pi*(n-m))
                                         for wt,y in pp)
    Q = sum(mats.values())
    return Q, mats


def prolate(cut, degree):
    """Orthonormal Legendre Ritz P_c, c=2pi lambda^2. Keep indices 0 and 4."""
    c = 2*math.pi*cut
    # Enlarge multiplication matrix so the final retained diagonal of y^2 is exact.
    J = np.zeros((degree+3, degree+3))
    j = np.arange(degree+2)
    off = (j+1)/np.sqrt((2*j+1)*(2*j+3))
    J[j,j+1]=off
    J[j+1,j]=off
    Y2 = (J@J)[:degree+1,:degree+1]
    P = np.diag(np.arange(degree+1)*(np.arange(degree+1)+1)) + c*c*Y2
    even = np.arange(0, degree+1, 2)
    vals, vecs = np.linalg.eigh(P[np.ix_(even,even)])
    coeffs=[]
    for idx in (0,2):  # even eigenmode ordering 0,2,4,...
        coeff = np.zeros(degree+1)
        coeff[even]=vecs[:,idx]
        # Convert orthonormal coefficients to conventional Legendre coefficients.
        coeff *= np.sqrt((2*np.arange(degree+1)+1)/2)
        if legval(0.0,coeff)<0:
            coeff=-coeff
        coeffs.append(coeff)
    h0,h4=coeffs
    ratio=h4[0]/h0[0]  # Integrals are 2*coefficient of P_0.
    h=h4-ratio*h0
    mean_error=2*h[0]
    h[0]=0.0  # exact constraint in the finite Legendre representation
    return h, {'c_prolate':c,'mode_eigenvalues':[float(vals[0]),float(vals[2])],
               'integral_ratio_I4_over_I0':float(ratio),
               'pre_rounding_integral_error':float(mean_error),
               'h_at_zero_unscaled':float(legval(0,h)),
               'h_at_endpoint_unscaled':float(legval(1,h))}


def proxy_samples(cut, degree, segment_quad):
    lam=math.sqrt(cut); a=math.log(lam)
    coeff,diag=prolate(cut,degree)
    # Jump points for the exact floor(lambda/u) sum must be included.
    breaks=sorted(set([-a,a]+[a-math.log(m) for m in range(2,int(cut)+1)
                              if -a<a-math.log(m)<a]))
    # Reflection diagnostic also has jumps at the negatives of these points.
    breaks=sorted(set(breaks+[-x for x in breaks]))
    gx,gw=gl(segment_quad)
    t=np.concatenate([(hi+lo)/2+(hi-lo)*gx/2 for lo,hi in zip(breaks[:-1],breaks[1:])])
    weights=np.concatenate([(hi-lo)*gw/2 for lo,hi in zip(breaks[:-1],breaks[1:])])

    def k_at(ts):
        us=np.exp(ts)
        out=np.zeros_like(us)
        for m in range(1,int(cut)+1):
            y=m*us/lam
            mask=y<1
            out[mask]+=legval(y[mask],coeff)/math.sqrt(lam)
        return np.sqrt(us)*out
    kval=k_at(t)
    kval_reverse=k_at(-t)
    norm2=float(np.dot(weights,kval*kval))
    asym2=float(np.dot(weights,(kval-kval_reverse)**2)/norm2)
    diag['relative_log_reflection_defect']=math.sqrt(max(asym2,0))
    return t,weights,kval,norm2,diag


def probe(cut,N,degree,segment_quad,matrix_quad):
    Q,mats=weil(cut,N,matrix_quad)
    t,w,k,norm2,pdiag=proxy_samples(cut,degree,segment_quad)
    L=math.log(cut)
    inds=np.arange(-N,N+1)
    basis=np.exp(-2j*math.pi*inds[:,None]*(t[None,:]+L/2)/L)/math.sqrt(L)
    coeff=basis@(w*k)
    proj2=float(np.vdot(coeff,coeff).real)
    assert proj2>0
    b=coeff/math.sqrt(proj2)
    ev,U=np.linalg.eigh(Q)
    amplitudes=U.conj().T@b
    RB=float(np.vdot(b,Q@b).real)
    excess=float(np.dot(ev-ev[0],abs(amplitudes)**2))
    gap=float(ev[1]-ev[0]) if N else None
    residue=float(np.linalg.norm(Q@b-RB*b))
    leakage=max(0.,norm2-proj2)
    Pe=np.zeros((2*N+1,N+1)); Pe[N,0]=1
    Po=np.zeros((2*N+1,N))
    for j in range(1,N+1):
        Pe[N-j,j]=Pe[N+j,j]=1/math.sqrt(2)
        Po[N-j,j-1]=1/math.sqrt(2); Po[N+j,j-1]=-1/math.sqrt(2)
    ev_even=np.linalg.eigvalsh(Pe.T@Q@Pe)
    ev_odd=np.linalg.eigvalsh(Po.T@Q@Po) if N else np.array([])
    ground_even_defect=float(np.linalg.norm(U[:,0]-U[::-1,0]))
    scale=float(np.linalg.norm(Q,2))
    ratio=excess/gap if gap and gap>0 else None
    d2=float(1-abs(amplitudes[0])**2)
    if ratio is not None:
        assert d2 <= ratio+2e-10
    record={
      'lambda':math.sqrt(cut),'prime_power_cutoff':cut,'N':N,
      'prolate_legendre_degree':degree,'segment_quadrature':segment_quad,'matrix_quadrature':matrix_quad,
      'lambda_0':float(ev[0]),'lambda_1':float(ev[1]) if N else None,'gap':gap,
      'R_B':RB,'energy_excess_eigen_expansion':excess,'energy_excess_direct':RB-float(ev[0]),
      'excess_over_gap':ratio,'residual_norm':residue,
      'squared_distance_to_ground_line':d2,'ground_overlap_squared':float(abs(amplitudes[0])**2),
      'even_ground':float(ev_even[0]),'odd_ground':float(ev_odd[0]) if N else None,
      'ground_even_defect':ground_even_defect,
      'proxy_projected_even_fraction':float(np.linalg.norm(Pe.T@b)**2),
      'proxy_norm_squared':norm2,'projection_relative_L2_tail':math.sqrt(leakage/norm2),
      'projection_norm_consistency_error':max(0.,proj2-norm2),
      'quadratic_components':{name:float(np.vdot(b,M@b).real) for name,M in mats.items()},
      'unit_trial_coefficients':[[float(z.real),float(z.imag)] for z in b],
      'matrix_norm':scale,'gap_resolved_in_float64':bool(gap and gap>1000*np.finfo(float).eps*scale),
      'prolate_diagnostics':pdiag}
    return record,Q


def main():
    old=json.loads((ROOT/'experiments/results/groskin-c13-n4-independent.json').read_text())
    def midpoint(s):
        return float(re.search(r'[-+]?\d+(?:\.\d*)?(?:e[-+]?\d+)?',s).group())
    ref=np.array([[midpoint(s) for s in row] for row in old['matrix']])
    qm,_=weil(13,4,384)
    diff=float(np.max(abs(ref-qm)))
    assert diff<3e-12, diff
    cases=[]
    for cut in (2,3,5,9,13,25):
        for N in (4,8,16):
            low,Qlo=probe(cut,N,80,32,256)
            high,Qhi=probe(cut,N,128,64,512)
            high['resolution_changes']={key:abs(high[key]-low[key]) for key in
                ('R_B','lambda_0','gap','energy_excess_eigen_expansion','excess_over_gap',
                 'ground_overlap_squared','projection_relative_L2_tail')}
            high['resolution_changes']['matrix_entry_max']=float(np.max(abs(Qhi-Qlo)))
            cases.append(high)
            print('cut=%s N=%s R=%.7g e0=%.7g gap=%.7g ratio=%.7g overlap=%.7g tail=%.3g'
                  %(cut,N,high['R_B'],high['lambda_0'],high['gap'],high['excess_over_gap'],
                    high['ground_overlap_squared'],high['projection_relative_L2_tail']),flush=True)
    result={'rh_status':'OPEN','kind':'FLOATING_POINT_DIAGNOSTIC_NOT_CERTIFICATE',
      'actual_proxy_used':True,'proxy_log_evenness_imposed':False,
      'reference_Arb_midpoint_max_error':diff,
      'known_reference':'experiments/results/groskin-c13-n4-independent.json',
      'numpy_version':np.__version__,'cases':cases,
      'limitations':['finite parameters','Legendre Ritz and quadrature resolution check is not rigorous error enclosure',
                     'No inference of asymptotic excess/gap or RH','Projected proxy P_N k is explicitly used',
                     'No equating of concentration ground with the mean-zero 0/4 combination']}
    (OUT/'rayleigh_results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
