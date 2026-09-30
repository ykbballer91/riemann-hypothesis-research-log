#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/joint_symbol_certificate.py
# Original SHA-256: 7cb0c430b247d1f9097ad3912a6159d5cc62545860f841fdca6f9a0946135012
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Certify a joint-symbol floor on a finite cover plus an analytic infinite tail.

This certifies only Psi_a(t)>=beta for |t|>=T, not positivity of Q_W.
Use python-flint 0.9.0. Each saved dyadic cover can be checked with --verify.
The analytic input h(t)>=log(t/(2*pi))-1/t is documented in the audit note.
"""
import argparse
import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path

import flint
from flint import arb, ctx


TARGETS = [('0.8', 111), ('1', 1552), ('1.19', 5549),
           ('1.2', 21231), ('1.4', 132510)]


def serial(x):
    return x.str(50, more=True)


def exact_decimal(s):
    q = Fraction(s)
    return arb(q.numerator) / q.denominator


def setup(a_text):
    a = exact_decimal(a_text)
    # The floating value chooses a candidate bound only; Arb verifies it below.
    bound = int(math.exp(2 * float(a_text))) + 2
    assert arb(bound).log() > 2*a
    data = []
    for p in range(2, bound):
        if any(p % d == 0 for d in range(2, math.isqrt(p)+1)):
            continue
        n = p
        while n < bound:
            v = arb(n).log()
            if v < 2*a:
                data.append((n, p, 2*arb(p).log()/arb(n).sqrt(), v))
            else:
                assert v > 2*a, 'Undecided support boundary'
            n *= p
    data.sort()
    A = sum((w for _, _, w, _ in data), arb(0))
    return a, data, A


def g(t, data):
    return (t/(2*arb.pi())).log()-1/t-sum(
        (w*(t*v).cos() for _, _, w, v in data), arb(0))


def add_run(runs, level):
    if runs and runs[-1][0] == level:
        runs[-1][1] += 1
    else:
        runs.append([level, 1])


def certify(a_text, T, beta_text, bits, max_level):
    ctx.prec = bits
    a, data, A = setup(a_text)
    beta = exact_decimal(beta_text)
    assert a > 0 and T >= 4 and beta > 0
    U = math.ceil(2*math.pi*math.exp(float(A)+float(beta_text)))+2
    assert U >= T
    # Envelope E is increasing for t>0, so this handles the whole [U,infinity).
    envelope = (arb(U)/(2*arb.pi())).log()-1/arb(U)-A
    assert envelope > beta
    runs, count, max_depth = [], 0, 0
    min_margin = None
    start = time.monotonic()

    def cover(k, level):
        nonlocal count, max_depth, min_margin
        # Exactly [k/2^level,(k+1)/2^level], including both endpoints.
        center = arb(2*k+1) / (2**(level+1))
        radius = arb(1) / (2**(level+1))
        interval = arb(center, radius)
        value = g(interval, data)
        if value > beta:
            add_run(runs, level)
            count += 1
            max_depth = max(max_depth, level)
            margin = (value-beta).lower()
            min_margin = margin if min_margin is None else min(min_margin, margin)
            return
        midpoint = g(center, data)
        assert not midpoint < beta, ('Counterexample to proposed g-floor, not necessarily to Psi-floor', a_text, serial(center), serial(midpoint))
        assert level < max_level, ('Unresolved interval', k, level, serial(value))
        cover(2*k, level+1)
        cover(2*k+1, level+1)

    for k in range(T, U):
        cover(k, 0)
    # Exact coverage, including contiguous endpoints, rather than a floating grid.
    assert sum((Fraction(c, 2**d) for d, c in runs), Fraction(0)) == U-T
    return dict(a=a_text, T=T, U=U, beta=beta_text,
                prime_powers=[dict(n=n, p=p) for n, p, _, _ in data],
                constant_prime_bound=serial(A),
                old_zero_floor_height=serial(2*arb.pi()*A.exp()),
                envelope_at_U=serial(envelope),
                finite_cover_min_certified_margin=serial(min_margin),
                leaf_count=count, maximum_dyadic_level=max_depth,
                cover_encoding='Starting at T, each [d,c] means c consecutive closed intervals of width 2^(-d); end at U.',
                cover_runs=runs, certificate_passed=True,
                elapsed_seconds=round(time.monotonic()-start, 3))


def verify(path, bits):
    doc = json.loads(Path(path).read_text())
    ctx.prec = bits
    checked = 0
    for item in doc['certificates']:
        _, data, A = setup(item['a'])
        assert item['prime_powers'] == [dict(n=n, p=p) for n,p,_,_ in data]
        beta = exact_decimal(item['beta'])
        assert item['T'] >= 4 and beta > 0
        U = arb(item['U'])
        assert (U/(2*arb.pi())).log()-1/U-A > beta
        x, count = Fraction(item['T']), 0
        for level, n in item['cover_runs']:
            assert isinstance(level, int) and 0 <= level <= 24
            assert isinstance(n, int) and n > 0
            width = Fraction(1, 2**level)
            for _ in range(n):
                center = x+width/2
                z = arb(arb(center.numerator)/center.denominator,
                        arb(width.numerator)/(2*width.denominator))
                assert g(z, data) > beta, (item['a'], str(x), level)
                x += width
                count += 1
        assert x == item['U'] and count == item['leaf_count']
        checked += count
        print('verified', item['a'], 'leaves', count, flush=True)
    print(json.dumps(dict(verification='PASS', precision_bits=bits,
                          intervals_checked=checked, proves_RH=False)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--bits', type=int, default=160)
    p.add_argument('--max-level', type=int, default=20)
    p.add_argument('--beta', default='0.2')
    p.add_argument('--verify')
    p.add_argument('--output', default='experiments/results/joint-symbol-tail-certificates.json')
    args = p.parse_args()
    assert args.bits >= 128
    if args.verify:
        verify(args.verify, args.bits)
        return
    cases = []
    for a, T in TARGETS:
        v = certify(a, T, args.beta, args.bits, args.max_level)
        cases.append(v)
        print('certified', a, 'T', T, 'U', v['U'], 'leaves', v['leaf_count'],
              'time', v['elapsed_seconds'], flush=True)
    out = dict(kind='joint_symbol_infinite_frequency_tail_floor', rh_status='OPEN',
               proves_RH=False, proves_full_window_positivity=False,
               source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               arithmetic='python-flint Arb', python_flint_version=flint.__version__,
               precision_bits=args.bits, certificates=cases,
               analytic_input='h(t)>=log(t/(2*pi))-1/t for t>=4; Psi is even, so g(abs(t)) supplies its lower bound.',
               scope='Five fixed supports. Tail symbol only. No head, coupling, or all-window claim.')
    Path(args.output).write_text(json.dumps(out, indent=2)+'\n')
    print('saved', args.output, flush=True)


if __name__ == '__main__':
    main()
