#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/window_four_fifths_certificate.py
# Original SHA-256: cfd0fbd304e25d7dd698238005f2b6c4f207dc2ee353c4d51892b71588fd8e7a
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""INTERRUPTED PROTOTYPE: no head or full-window certificate was produced.

The only run was stopped by user steering at panel 160/444, exit 130.
Do not resume as the main research route: the user prohibited brute window
enlargement and prioritized support-propagation structure.

Probe/certify the exact lower Weil operator on support [-4/5,4/5].

Arb head assembly has an analytic quadrature enclosure. A full-window claim
requires positive shifted heads AND analytic all-mode tail/coupling bounds.
An indefinite lower operator does not refute Q_W positivity or RH.
"""
import argparse
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

import flint
from flint import acb, arb, arb_mat, ctx
from groskin_independent_certificate import ldlt, serial


def exact(s):
    q = Fraction(s)
    return arb(q.numerator)/q.denominator


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--T',type=int,default=111)
    p.add_argument('--cut',type=int,default=192)
    p.add_argument('--bits',type=int,default=224)
    p.add_argument('--shift',default='1e-20')
    p.add_argument('--floor',choices=['joint','envelope'],default='joint')
    p.add_argument('--output')
    args=p.parse_args()
    assert args.T>=4 and args.cut>=2 and args.cut%2==0 and args.bits>=160
    ctx.prec=args.bits
    a,T,pi=arb(4)/5,arb(args.T),arb.pi()
    data=[(n,p,2*arb(p).log()/arb(n).sqrt(),arb(n).log())
          for n,p in [(2,2),(3,3),(4,2)]]
    assert arb(4).log()<2*a and arb(5).log()>2*a
    A=sum((w for _,_,w,_ in data),arb(0))
    if args.floor=='joint':
        assert args.T>=111
        beta=arb(1)/5
        floor_path=Path('experiments/results/joint-symbol-tail-certificates.json')
        cert=json.loads(floor_path.read_text())
        row=next(v for v in cert['certificates'] if v['a']=='0.8')
        assert row['T']==111 and row['beta']=='0.2' and row['certificate_passed']
        floor_evidence=dict(path=str(floor_path),sha256=hashlib.sha256(floor_path.read_bytes()).hexdigest())
    else:
        beta=(T/(2*pi)).log()-1/T-A
        floor_evidence=dict(formula='log(T/(2*pi))-1/T-A')
    assert beta>0
    shift=exact(args.shift)
    assert shift>0
    q,rho,step=32,arb(6),arb(1)/4
    nodes=[arb.legendre_p_root(q,k,weight=True) for k in range(q)]
    den=[arb(1)]
    for n in range(1,args.cut+1):den.append(den[-1]*(2*n+1))
    norms=[(2*a*(2*n+1)).sqrt() for n in range(args.cut)]
    rows=[[] for _ in range(args.cut)]
    weights=[]
    start=time.monotonic()
    for panel in range(4*args.T):
        center=step*(arb(panel)+arb(1)/2)
        for x,w in nodes:
            t=center+step*x/2
            z=a*t
            symbol=acb(arb(1)/4,t/2).digamma().real-pi.log()-sum(
                (weight*(t*logn).cos() for _,_,weight,logn in data),arb(0))
            weights.append(w*step/(2*pi)*(symbol-beta))
            power=arb(1)
            for n in range(args.cut):
                j=power/den[n]*(-z*z/4).hypgeom_0f1(arb(n)+arb(3)/2)
                rows[n].append((-1)**(n//2)*norms[n]*j)
                power*=z
        if (panel+1)%32==0:
            print('panels',panel+1,'/',4*args.T,'elapsed',round(time.monotonic()-start,1),flush=True)

    # Same rho=6, width=1/4 ellipses as the certified a=1/2 implementation.
    # |Im(t)|<.4, |Re(t)|<T+.3; log n<1.6 gives |cos(t log n)|<2.
    M0=T+25+2*A+beta.abs_upper()
    M=M0*2*a*(2*args.cut-1)*(arb(4)/5*a).exp()/pi
    entry_error=4*T*M*rho**(1-2*q)/(rho-1)
    sectors=[]
    for parity in (0,1):
        inds=list(range(parity,args.cut,2))
        dim=len(inds)
        V=arb_mat([rows[n] for n in inds])
        W=arb_mat([[v*w for v,w in zip(rows[n],weights)] for n in inds])
        C=W*V.transpose()
        y=a/2
        poles=[norms[n]*y**n/den[n]*(y*y/4).hypgeom_0f1(arb(n)+arb(3)/2) for n in inds]
        head=[[C[i,j]+arb(0,entry_error)+(-1)**parity*2*poles[i]*poles[j]
               +(beta if i==j else 0) for j in range(dim)] for i in range(dim)]
        record=dict(parity=['even','odd'][parity],indices=inds,dimension=dim,
                    head=[[serial(v) for v in r] for r in head])
        try:
            ds,L=ldlt(head)
            record.update(unshifted_inertia_certified=True,n_positive=sum(d>0 for d in ds),
                          n_negative=sum(d<0 for d in ds),
                          unshifted_pivots=[serial(d) for d in ds])
            if any(d<0 for d in ds):
                # Exact rationalized congruence witness for a negative leading pivot.
                k=next(i for i,d in enumerate(ds) if d<0)
                v=[arb(0) for _ in range(k+1)]
                v[k]=arb(1)
                for j in range(k-1,-1,-1):
                    v[j]=-sum((L[i][j]*v[i] for i in range(j+1,k+1)),arb(0))
                rationals=[Fraction(str(float(x))) for x in v]
                # Float coefficients specify exact rationals; the sign is rechecked in Arb.
                ev=[arb(x.numerator)/x.denominator for x in rationals]
                ray=sum((head[i][j]*ev[i]*ev[j] for i in range(k+1) for j in range(k+1)),arb(0))
                record.update(negative_witness_coefficients=[str(x) for x in rationals],
                              negative_witness_value=serial(ray),negative_witness_certified=bool(ray<0))
        except AssertionError as exc:
            record.update(unshifted_inertia_certified=False,unshifted_failure=str(exc))
        try:
            shifted=[[head[i][j]-(shift if i==j else 0) for j in range(dim)] for i in range(dim)]
            ds,L=ldlt(shifted)
            record.update(shifted_pivots=[serial(d) for d in ds],
                          shifted_head_positive=all(d>0 for d in ds))
        except AssertionError as exc:
            record.update(shifted_head_positive=False,shifted_failure=str(exc))
        sectors.append(record)
        print('head',record['parity'],'positive',record.get('n_positive'),
              'negative',record.get('n_negative'),'shifted_positive',record['shifted_head_positive'],flush=True)

    # Hilbert--Schmidt Fourier tail, all n>=d; pole tail from modified Bessel.
    d=args.cut
    X=a*T
    r=X/arb(2*d+3)
    assert r<1
    K=2*X/pi*X**(2*d)/(den[d]*den[d])/(1-r*r)
    y=a/2
    rp=y/arb(2*d+1)
    assert rp<1
    pole_tail_squared=2*a*(2*d+1)*y**(2*d)/(den[d]*den[d])*(2*y).exp()/(1-rp*rp)
    real_bound=max(arb(6),4+(1+4*T*T).log()/2)+A+beta.abs_upper()
    coupling=real_bound*K.sqrt()+2*(a.sinh()+a).sqrt()*pole_tail_squared.sqrt()
    tail_floor=beta-real_bound*K-2*pole_tail_squared
    lower=min(shift,tail_floor)-coupling
    passed=all(v['shifted_head_positive'] for v in sectors) and lower>0
    out=dict(kind='fixed_window_lower_operator_audit',a='4/5',support=['-4/5','4/5'],
             T=args.T,cut_order=d,head_shift=args.shift,beta=serial(beta),floor_mode=args.floor,
             floor_evidence=floor_evidence,arithmetic='python-flint Arb',precision_bits=args.bits,
             python_flint_version=flint.__version__,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             ldlt_helper_sha256=hashlib.sha256(Path(__file__).with_name('groskin_independent_certificate.py').read_bytes()).hexdigest(),
             gauss_order=q,panel_width='1/4',ellipse_parameter='6',
             ellipse_symbol_bound=serial(M0),ellipse_integrand_bound=serial(M),
             per_entry_quadrature_error=serial(entry_error),
             fourier_tail_HS_squared=serial(K),pole_tail_squared=serial(pole_tail_squared),
             real_band_symbol_bound=serial(real_bound),coupling_bound=serial(coupling),
             tail_floor=serial(tail_floor),conditional_full_window_lower_bound=serial(lower),
             full_window_certificate_passed=bool(passed),sectors=sectors,rh_status='OPEN',proves_RH=False,
             scope='Full-window positivity only if shifted heads and all-mode tail/coupling pass; R negative does not refute Q.')
    output=Path(args.output or f'experiments/results/window-four-fifths-T{args.T}-cut{d}-{args.floor}.json')
    output.write_text(json.dumps(out,indent=2)+'\n')
    print('saved',output,'full_window_certificate_passed',passed,'lower',lower,
          'elapsed',round(time.monotonic()-start,1),flush=True)


if __name__=='__main__':main()
