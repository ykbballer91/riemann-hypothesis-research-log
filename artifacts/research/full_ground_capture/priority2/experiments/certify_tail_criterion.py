# STATUS: RIEMANN HYPOTHESIS OPEN
# Public credit: @ykbballer91; AI-assisted
# SPDX-License-Identifier: MIT
# Source: research/full_ground_capture/priority2/experiments/certify_tail_criterion.py
# Original SHA-256: fee1b9b6f7fae6598c2e567e876ad792d70a8ab2277eb05098a31ef823a75c3e
"""Arb interval verification of a proved finite-head sufficient condition.

No floating-rank inference. Uses rigorous acb evaluation of completed zeta,
exact rational derivative polynomials, and the analytic L1 tail majorant.
Dependency: python-flint 0.9.0. RH is not assumed by any call.
"""
from fractions import Fraction
from pathlib import Path
import json
import flint
from flint import arb, acb, ctx


def polys(order):
    out = [[Fraction(0), Fraction(-3, 2), Fraction(1)]]
    for _ in range(order):
        p = out[-1]
        q = [Fraction(0)]*(len(p)+1)
        for l, c in enumerate(p):
            q[l] += (Fraction(1, 2)+2*l)*c
            q[l+1] -= 2*c
        out.append(q)
    return out


def ball(q):
    return arb(q.numerator)/q.denominator


def xi(w):
    s = acb(arb(1)/2, w)
    ans = s*(s-1)/2 * (-(s/2)*acb(arb.pi()).log()).exp() * (s/2).gamma()*s.zeta()
    assert ans.imag.contains(0), 'Xi is real on the real axis; enclosure must contain 0'
    return ans.real


def certify(a_string, N, bits):
    ctx.prec = bits
    a = arb(a_string)
    Y = arb.pi()*(2*a).exp()
    record = {'a': a_string, 'N': N, 'm': N, 'precision_bits': bits}
    if not Y >= 4*N+4:
        record.update(status='TAIL_MAJORANT_PRECONDITION_NOT_VERIFIED', Y=str(Y))
        return record
    t = [(arb.pi()*n/a)**2 for n in range(N+1)]
    D = []
    for n in range(N+1):
        value = xi(arb.pi()*n/a)
        if value.contains(0):
            record.update(status='GRID_NONZERO_NOT_CERTIFIED', row=n)
            return record
        D.append(abs(value)/(4*((2*a).sqrt() if n == 0 else a.sqrt())))
    L2 = arb(0)
    for n in range(N+1):
        beta = arb(1)
        for r in range(N+1):
            if r != n:
                beta *= (1+t[r])/abs(t[n]-t[r])
        L2 += (beta/D[n])**2
    L = L2.sqrt()
    pp = polys(2*N)
    tail2 = arb(0)
    common = 2*arb.pi()**(-arb(1)/4)*(-Y).exp()/(1-(-Y/2).exp())
    for j in range(N+1):
        T = common*sum((ball(abs(c))*Y**(arb(l)-arb(3)/4)
                        for l, c in enumerate(pp[2*j]) if c), arb(0))
        tail2 += T*T
    tau = ((arb(2*N+1)/(2*a))*tail2).sqrt()
    eta = L*tau
    record.update(
        status='CERTIFIED_FULL_RANK' if eta < 1 else 'SUFFICIENT_CRITERION_INCONCLUSIVE',
        inverse_norm_upper_enclosure=str(L),
        ideal_sigma_min_lower_enclosure=str(1/L),
        tail_norm_upper_enclosure=str(tau),
        eta_upper_enclosure=str(eta),
        actual_sigma_min_lower_enclosure=str(1/L-tau),
        Xi_nonzero_rows_certified=N+1,
    )
    return record


def main():
    cases = [('0.5', 2), ('1', 2), ('1', 4), ('1.5', 4),
             ('2', 4), ('2', 6), ('3', 6),
             ('1.5 +/- 0.000001', 4), ('2 +/- 0.000001', 6)]
    records = [certify(a, N, bits) for bits in (256, 384) for a, N in cases]
    out = {'method': 'Arb interval enclosure of L*tau < 1',
           'python_flint_version': flint.__version__, 'RH_assumed': False,
           'noncertificate_does_not_mean_rank_loss': True,
           'records': records}
    path = Path(__file__).parent/'tail_certificates.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    for r in records:
        print(r['precision_bits'], r['a'], r['N'], r['status'], r.get('eta_upper_enclosure', ''))


if __name__ == '__main__':
    main()
