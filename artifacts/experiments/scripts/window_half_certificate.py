#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/window_half_certificate.py
# Original SHA-256: d4b176096168c13f53459f27e1ae9a9db9e045a4b774c097f49a9939d5c408d0
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Independent full-window certificate for support [-1/2,1/2].

Certified Gauss nodes/weights and ball arithmetic; analytic quadrature and
infinite Legendre-tail bounds are recorded separately in the audit note.
No zero data, RH assumption, or downloaded author implementation is used.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import flint
from flint import arb, acb, arb_mat, ctx
from groskin_independent_certificate import ldlt, serial


def dfact(n):
    out = arb(1)
    for k in range(1, 2*n+2, 2):
        out *= k
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=32)
    parser.add_argument('--cut', type=int, default=64)
    parser.add_argument('--bits', type=int, default=192)
    parser.add_argument('--shift', default='1e-7')
    args = parser.parse_args()
    assert args.T >= 4 and args.cut >= 2 and args.cut % 2 == 0
    ctx.prec = args.bits
    a, T, pi = arb(1)/2, arb(args.T), arb.pi()
    A = 2*arb(2).log()/arb(2).sqrt()  # Only n=2 has log(n)<1.
    beta = (T/(2*pi)).log()-1/T-A
    assert beta > 0
    q, rho, panels = 32, arb(6), 4*args.T
    step, shift = arb(1)/4, arb(args.shift)
    assert shift > 0
    nodes = [arb.legendre_p_root(q,k,weight=True) for k in range(q)]
    denominators = [dfact(n) for n in range(args.cut+1)]
    normalizers = [arb(2*n+1).sqrt() for n in range(args.cut)]
    rows = [[] for _ in range(args.cut)]
    weights = []
    start = time.monotonic()
    for panel in range(panels):
        center = step*(arb(panel)+arb(1)/2)
        for x,w in nodes:
            t = center+step*x/2
            z = a*t
            symbol = acb(arb(1)/4,t/2).digamma().real-pi.log()-A*(t*arb(2).log()).cos()
            weights.append(w*step/(2*pi)*(symbol-beta))
            power = arb(1)
            for n in range(args.cut):
                j = power/denominators[n]*(-z*z/4).hypgeom_0f1(arb(n)+arb(3)/2)
                rows[n].append((-1)**(n//2)*normalizers[n]*j)
                power *= z
        if (panel+1) % 32 == 0:
            print(f'quadrature panels {panel+1}/{panels}; {time.monotonic()-start:.1f}s',flush=True)

    # For |Im t|<=.4 and |Re t|<=T+.3, |psi(1/4+-it/2)|<T+22.2.
    # Prime term <=2A, log(pi)<2. M bounds the full C integrand /pi.
    symbol_bound = T+25+2*A+beta.abs_upper()
    M = symbol_bound*(2*args.cut-1)*arb('0.4').exp()/pi
    quad_error = 4*T*M*rho**(1-2*q)/(rho-1)
    results = []
    for parity in (0,1):
        indices = list(range(parity,args.cut,2))
        V = arb_mat([rows[n] for n in indices])
        W = arb_mat([[v*weight for v,weight in zip(rows[n],weights)] for n in indices])
        C = W*V.transpose()
        p = []
        z = a/2
        for n in indices:
            p.append(normalizers[n]*z**n/denominators[n]*(z*z/4).hypgeom_0f1(arb(n)+arb(3)/2))
        dim = len(indices)
        head = [[C[i,j]+arb(0,quad_error)+(-1)**parity*2*p[i]*p[j]
                 +(beta if i==j else 0) for j in range(dim)] for i in range(dim)]
        shifted = [[head[i][j]-(shift if i==j else 0) for j in range(dim)] for i in range(dim)]
        try:
            pivots, lower = ldlt(shifted)
        except AssertionError as exc:
            diagnostic=Path(f'experiments/results/window-half-T{args.T}-cut{args.cut}-unverified.json')
            diagnostic.write_text(json.dumps(dict(certificate_passed=False,parity=parity,
                reason=str(exc),head=[[serial(v) for v in row] for row in head],
                beta=serial(beta),quad_error=serial(quad_error),shift=serial(shift)),indent=2)+'\n')
            raise
        positive = sum(d>0 for d in pivots)
        print(f'parity={parity}: positive shifted pivots {positive}/{dim}',flush=True)
        results.append(dict(parity='even' if parity==0 else 'odd',dimension=dim,
                            positive_shifted_pivots=positive,negative_shifted_pivots=dim-positive,
                            head=[[serial(v) for v in row] for row in head],
                            shifted_pivots=[serial(d) for d in pivots],
                            unit_lower=[[serial(v) for v in row] for row in lower]))

    # All orders n>=cut, rather than just one parity: deliberately conservative.
    b0 = arb(2*args.cut+1).sqrt()*(a*T)**args.cut/denominators[args.cut]
    ratio = a*T/arb(2*args.cut+1)
    assert ratio < 1
    fourier_tail = b0/(1-ratio*ratio).sqrt()
    p0 = arb(2*args.cut+1).sqrt()*(a/2)**args.cut/denominators[args.cut]*(a/2).exp()
    pole_ratio = (a/2)/arb(2*args.cut+1)
    pole_tail = p0/(1-pole_ratio*pole_ratio).sqrt()
    # Evaluation vector norm is sqrt(2a)=1 by Parseval, on each parity <=1.
    eps_B = symbol_bound*T/pi*fourier_tail + 2*(a/2).exp()*pole_tail
    eps_D = symbol_bound*T/pi*fourier_tail**2 + 2*pole_tail**2
    assert beta-eps_D > shift
    lower_bound = shift-eps_B
    passed = all(v['negative_shifted_pivots']==0 for v in results) and lower_bound>0
    out = dict(kind='independent_full_fixed_window_certificate',rh_status='OPEN',proves_RH=False,
               support=['-1/2','1/2'],arithmetic='python-flint Arb',precision_bits=args.bits,
               python_flint_version=flint.__version__,
               source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               ldlt_helper_sha256=hashlib.sha256(Path(__file__).with_name('groskin_independent_certificate.py').read_bytes()).hexdigest(),
               T=args.T,cut_order=args.cut,gauss_order=q,panel_width='1/4',
               prime_mass=serial(A),beta=serial(beta),ellipse_parameter='6',
               ellipse_symbol_bound=serial(symbol_bound),ellipse_integrand_bound=serial(M),
               per_entry_quadrature_error=serial(quad_error),head_shift=serial(shift),
               fourier_tail_vector_bound=serial(fourier_tail),pole_tail_vector_bound=serial(pole_tail),
               coupling_bound=serial(eps_B),tail_deviation_bound=serial(eps_D),
               full_window_lower_bound=serial(lower_bound),certificate_passed=bool(passed),
               sectors=results,analytic_audit='proofs/audits/window-half-certificate.md',
               scope='all complex form-domain functions supported in this one window; not all windows')
    path=Path(f'experiments/results/window-half-T{args.T}-cut{args.cut}.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('saved',path,'certificate_passed=',passed,'lower=',lower_bound,'elapsed=',time.monotonic()-start,flush=True)


if __name__=='__main__':
    main()
