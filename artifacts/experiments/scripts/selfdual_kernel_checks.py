#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/selfdual_kernel_checks.py
# Original SHA-256: e6b4435965c0de88e18bb53460e72eec0ebd259a20660beff61f803be74fe5c7
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact modular countermodel checks. This is NOT a counterexample to RH."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import mpmath as mp
from flint import acb, arb, ctx


def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def plus(p,q):
    return trim([(p[j] if j<len(p) else Q(0))+(q[j] if j<len(q) else Q(0))
                 for j in range(max(len(p),len(q)))])


def scale(p,c):
    return trim([x*c for x in p])


def times(p,q):
    out=[Q(0)]*(len(p)+len(q)-1)
    for j,x in enumerate(p):
        for k,y in enumerate(q):
            out[j+k]+=x*y
    return trim(out)


def dilation(p):
    out=[Q(0)]*(len(p)+1)
    for j,c in enumerate(p):
        out[j]+=(Q(1,2)+2*j)*c
        out[j+1]-=2*c
    return trim(out)


def complex_product(x,y):
    return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])


def evaluate_complex(p,z):
    out=(Q(0),Q(0))
    for c in reversed(p):
        out=complex_product(out,z)
        out=(out[0]+c,out[1])
    return out


def main():
    R=[Q(1)]
    for _ in range(2): R=dilation(R)
    R2=R
    for _ in range(2): R=dilation(R)
    R4=R
    assert R2==[Q(1,4),Q(-6),Q(4)]
    assert R4==[Q(1,16),Q(-39),Q(166),Q(-112),Q(16)]
    assert R4==plus(times([Q(0),Q(-14),Q(4)],[Q(0),Q(-14),Q(4)]),
                    [Q(1,16),Q(-39),Q(-30)])
    V0=[Q(0),Q(-6),Q(4)]
    V2=dilation(dilation(V0))
    V4=dilation(dilation(V2))
    assert V2==plus(times(V0,[Q(33,4),Q(-22),Q(4)]),[Q(0),Q(12)])
    assert V4==plus(times(V0,[Q(-1983,16),Q(-727),Q(934),Q(-240),Q(16)]),
                    [Q(0),Q(-978)])
    r4_lower=Q(1,16)-30*7**2-39*7
    v4_ratio_lower=-240*15**3-727*15-Q(1983,16)-Q(489,3)
    assert r4_lower==Q(-27887,16)
    assert v4_ratio_lower==Q(-13139071,16)
    # For x>=15 the remaining positive part of V4/V0 is increasing and >0.
    assert 934*15**2-727*15-Q(1983,16)-Q(489,27)>0

    denominator=16385**2
    a,b=Q(524256,denominator),Q(256,denominator)
    seed_lower=1-2*a+b*r4_lower
    theta_lower=1-Q(87,4)*a+b*v4_ratio_lower
    assert seed_lower==Q(266973521,denominator)>0
    assert theta_lower==Q(46840521,denominator)>Q(1,6)
    normalizer=1+a/4+b/16
    assert normalizer==Q(268599305,denominator)
    factor=scale(times([Q(16385,16),Q(-1,2),Q(1)],
                       [Q(16385,16),Q(1,2),Q(1)]),b)
    assert factor==[Q(1),Q(0),a,Q(0),b]
    exact_roots=[]
    for real_sign in [-1,1]:
        for imag_sign in [-1,1]:
            w=(Q(real_sign,4),Q(32*imag_sign))
            assert evaluate_complex(factor,w)==(0,0)
            exact_roots.append([str(w[0]+Q(1,2)),str(w[1])])

    # Separate check: standard xi is NONZERO at the inserted zero.
    ctx.prec=192
    def ball(q):return arb(q.numerator)/q.denominator
    def xi(s):
        return s*(s-1)/2*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()
    s=acb(arb(1)/4,32)
    xi_at_s=xi(s)
    assert abs(xi_at_s)>0
    z=acb(32,arb(1)/4)
    dp=-2*ball(a)*z+4*ball(b)*z**3
    modified_derivative=dp*xi_at_s/ball(normalizer)
    modified_at_zero=xi(acb(arb(1)/2))/ball(normalizer)
    cross=-modified_derivative*modified_at_zero/(4*z)
    gram_det=-abs(cross)**2
    assert gram_det<0

    # A bounded, non-certified check of the independently proved escaping profile.
    mp.mp.dps=50
    profile=[]
    limit=-2*mp.pi*mp.exp(-mp.pi)
    for nmax in [8,16,32]:
        value=mp.fsum((4*(mp.pi*(mp.mpf(n)/nmax)**2)**2
                       -6*mp.pi*(mp.mpf(n)/nmax)**2)
                      *mp.exp(-mp.pi*(mp.mpf(n)/nmax)**2)
                      for n in range(1,nmax+1))/nmax
        profile.append({'N':nmax,'normalized_partial_sum_at_minus_log_N':mp.nstr(value,35)})
    root=Path(__file__).resolve().parents[2]
    result={
        'status':'EXACT_POSITIVE_SELFDUAL_THETA_COUNTERMODEL_VERIFIED',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proves_RH':False,'refutes_RH':False,
        'standard_xi_changed':True,'Euler_core_zeta_changed':False,
        'standard_zero_free_gamma_factor_preserved':False,
        'parameters':{'a':str(a),'b':str(b),'normalizer':str(normalizer)},
        'R2':[str(x) for x in R2], 'R4':[str(x) for x in R4],
        'theta_derivative_polynomials':{'V0':[str(x) for x in V0],
                                        'V2':[str(x) for x in V2],
                                        'V4':[str(x) for x in V4]},
        'global_unnormalized_seed_lower_ratio':str(seed_lower),
        'global_unnormalized_theta_lower_ratio':str(theta_lower),
        'exact_added_s_zeros':exact_roots,
        'interval_checks':{'precision_bits':192,
            'standard_xi_at_one_quarter_plus_32i':str(xi_at_s),
            'standard_xi_nonzero_certified':True,
            'modified_D_two_point_determinant':str(gram_det),
            'modified_negative_determinant_certified':True},
        'groundstate_partial_sum_probe':{
            'method':'mpmath finite sums at 50 digits, non-certified; analytic Riemann-sum proof in note',
            'limit_at_u_zero':mp.nstr(limit,35),
            'values':profile,
            'claims_L2_convergence':False},
        'scope':'Modified Mellin factor; a counterexample to broad structural forcing, not RH',
    }
    (root/'experiments/results/selfdual-kernel-checks.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
