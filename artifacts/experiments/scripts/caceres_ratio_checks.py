#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/caceres_ratio_checks.py
# Original SHA-256: 546262155bfe9161598108cdbc0f07f3521293fa0f18755dd60c64c0bc0f00c0
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Finite checks of the printed X/Y, plus an all-N elementary error bound.

The proof that Q_N -> 1 throughout 0<Re(s)<1 is analytic, not inferred
from this finite table. No zero-finding and no RH assumption are used.
"""
import hashlib
import json
from pathlib import Path
import flint
from flint import acb, arb, ctx

ctx.prec = 192
windows = [16, 256, 4096, 65536]
rows = []
for sigma_text, t_text in [('0.25', '0'), ('0.75', '0'),
                           ('0.25', '1'), ('0.75', '1'), ('0.5', '1')]:
    sigma, t = arb(sigma_text), arb(t_text)
    s = acb(sigma, t)
    partial = acb(0)
    for n in range(1, windows[-1] + 1):
        term = (-s * arb(n).log()).exp()
        partial += term
        if n not in windows:
            continue
        x = partial + term / 2
        y = ((1 - s) * arb(n).log()).exp() / (1 - s)
        ratio = abs(x / y) ** 2
        # Elementary sum-vs-integral proof, valid for every integer N>=1:
        # |X-Y| <= 1/|1-s| + 3/2 + |s|/sigma.
        epsilon = (1 + abs(1 - s) * (arb(3)/2 + abs(s)/sigma)) * arb(n)**(sigma-1)
        assert abs(x/y - 1) < epsilon
        assert abs(ratio - 1) < 2*epsilon + epsilon**2
        rows.append(dict(sigma=sigma_text, t=t_text, N=n,
                         ratio=ratio.str(35, more=True),
                         analytic_epsilon=epsilon.str(35, more=True)))

out = dict(status='FINITE_CHECKS_PASS_ANALYTIC_RIGIDITY_REFUTATION',
           proves_RH=False, refutes_RH=False,
           refutes_external_theorem='Caceres 2609.28529v1 Theorem 4.1 / equation (55)',
           analytic_statement='For every fixed 0<Re(s)<1, printed Q_N(s) tends to 1',
           proof='proofs/audits/caceres-asymptotic-adversarial.md',
           author_code_executed=False, precision_bits=ctx.prec,
           python_flint_version=flint.__version__, rows=rows,
           source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
dest = Path('experiments/results/caceres-ratio-checks.json')
dest.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(dict(saved=str(dest), checks=len(rows), status=out['status']), indent=2))
