#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/support_propagation_checks.py
# Original SHA-256: f25195613ea9208998f8f568f36613643d94678038691fe098b9d854ec08bf27
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Exact/interval counterchecks of proposed support-propagation shortcuts.

These are countermodels, not negative values of the actual Weil form.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import arb, ctx

ctx.prec=224
ser=lambda x:x.str(60,more=True)


def schur(a,b,c):
    assert a>0
    return c-b*b/a


# Translation-invariant tridiagonal exact restrictions: the first two blocks
# are positive, but adding an identical diagonal shell yields a negative pivot.
pivots=[F(1)]
for _ in range(2):pivots.append(1-F(9,16)/pivots[-1])
assert pivots==[F(1),F(7,16),F(-2,7)]

# Cauchy-Stieltjes Gram tail: nodes 0,1 and positive atoms at 2,3.
aa=F(1,4)+F(1,9)
bb=F(1,2)+F(1,6)
cc=F(1)+F(1,4)
detD=aa*cc-bb*bb
assert min(aa,bb,cc,detD)>0 and detD==F(1,144)
detM=(1+aa)*(1+cc)-(2+bb)**2
assert detM==F(-583,144)
S0=schur(F(1),F(2),F(1))
S1=schur(1+aa,2+bb,1+cc)
assert S1>S0 and S1<0

# 1+1 version of the positive-update Schur/Woodbury identity, exact rationals.
woodbury=[]
for a,b,c,u,v in [(F(2),F(3),F(1),F(1,2),F(4,3)),
                    (F(1,10),F(2),F(-1),F(3),F(-2))]:
    actual=schur(a+u*u,b+u*v,c+v*v)-schur(a,b,c)
    factored=(v-u*b/a)**2/(1+u*u/a)
    assert actual==factored and actual>=0
    woodbury.append(dict(increment=str(actual),factored=str(factored),passed=True))

# Small A alone is not decisive: coupling of size sqrt(A) can remain safe.
gap=[]
for k in [1,2,4,8,16]:
    a=F(1,10**(2*k))
    safe_b=F(1,2*10**k)
    unsafe_b=F(1,10**k)+F(1,10**(2*k))
    assert schur(a,safe_b,F(1))==F(3,4)
    assert schur(a,unsafe_b,F(1))<0
    gap.append(dict(a=str(a),safe_schur='3/4',unsafe_schur=str(schur(a,unsafe_b,F(1)))))


def bathtub(m):
    R=arb.pi()/m
    return (1+R*R).log()-2+2*R.atan()/R


# q_L=Fourier multiplier log(1+t^2)-1, same logarithmic form-domain class.
small_L=arb(1)/2
small_gap=bathtub(2*small_L)-1
assert small_gap>0
large_L=arb(1)
box_q=(1-(-2*large_L).exp())/large_L+2*(2*large_L).expint(1)-1
assert box_q<0
delta=arb(1)/10**30
shell_lower=bathtub(2*delta)-1
schur_lower=shell_lower-2*arb.pi()*arb.pi()/small_gap
assert schur_lower>0

out=dict(kind='support_propagation_countermodels',rh_status='OPEN',
         proves_RH=False,refutes_RH=False,arithmetic='Fraction and python-flint Arb',
         precision_bits=ctx.prec,python_flint_version=flint.__version__,
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         toeplitz_chain=dict(off_diagonal='-3/4',pivots=[str(v) for v in pivots],
                             decision='positive first two restrictions, negative third Schur pivot'),
         cauchy_stieltjes_tail=dict(nodes=[0,1],measure_atoms=[2,3],
             tail=[[str(aa),str(bb)],[str(bb),str(cc)]],det_tail=str(detD),
             det_after_addition=str(detM),schur_before=str(S0),schur_after=str(S1),
             decision='strictly totally-positive tail improves Schur but does not make it positive'),
         woodbury_identity_checks=woodbury,small_gap_checks=gap,
         logarithmic_countermodel=dict(symbol='log(1+t^2)-1',
             small_L='1/2',all_function_lower_bound=ser(small_gap),
             large_L='1',normalized_box_value=ser(box_q),
             local_extension_delta='1e-30',shell_lower_bound=ser(shell_lower),
             local_schur_lower_bound=ser(schur_lower),
             interpretation='all functions positive at L=1/2 and a certified local extension, but a negative box at L=1'),
         scope='Failures of general propagation assumptions only; no actual Weil negative direction.')
path=Path('experiments/results/support-propagation-checks.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(saved=str(path),checks='PASS',small_gap=ser(small_gap),
                     large_box=ser(box_q),local_schur_lower=ser(schur_lower)),indent=2))
