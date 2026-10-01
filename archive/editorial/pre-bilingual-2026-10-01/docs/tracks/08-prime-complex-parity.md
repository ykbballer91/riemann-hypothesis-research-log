# 08. Prime complexes and parity pairing

**STATUS: RIEMANN HYPOTHESIS OPEN**

Recorded 2026-09-30. Date of the recorded report; individual start and finish times are not reconstructed.

## Starting idea

The Möbius sum is a signed Euler characteristic. Could a canonical matching on a prime complex leave only a square-root-sized obstruction?

## What was tested

The complex Δ_X consists of finite prime subsets whose product is at most X. The convention is M(X) = − reduced χ(Δ_X). Toggling the smallest prime, 2, yields an explicit matching and filtered chain description.

## What survived

- The unmatched cells correspond to odd squarefree integers in (X/2, X]; their total number, and hence the relevant total Betti count, has linear asymptotic 2X/π².

- The filtration has explicit bars [n, 2n), including the augmented initial bar. The doubling map has the recorded chain-homotopy consequence.

## What failed or remains unproved

The unsigned topological remainder is linear, so this matching does not give the desired signed cancellation. A prime-vertex pairwise-product graph is not the complex: at X = 15 all three edges on {2,3,5} exist but the triple face does not. Its flag completion would change the topology. This is not a no-go theorem for every possible nonlocal pairing.

## Why the work moved on

The next track tested whether prime-logarithm phase statistics supplied the missing signs.

## Current scope

Exact combinatorial identities retained; no square-root estimate for M(X) obtained.

“Proved” here refers to the stated mathematical claim in the linked research record. Internal AI-agent checks are scoped checks, not external peer review. Numerical and formal checks have separate limits described in [Reproducibility](../reproducibility.md). No priority or novelty claim is made.

## Canonical records

- [Detailed source report](../../../../reports/research/prime_complex_parity_pairing.md)
- [Completion report](../../../../reports/research/prime_complex/completion_report.txt)
- [Scoped internal audit](../../../../audits/proofs/audits/prime_complex_adversarial.md)
- [Historical state record](../../../../../data/source-records/research/prime_complex_state.json)
- [Recorded validation](../../../../../data/source-records/research/prime_complex/validation.json)

The source archive preserves the original Japanese research prose. These links point to publication copies, not third-party paper downloads. The [source map](../source-map.md) explains historical state files and [references](../references.md) distinguish publication status from verification.

[Research timeline](../timeline.md)
