# 10. Weighted prime halfspaces

**STATUS: RIEMANN HYPOTHESIS OPEN**

Recorded 2026-09-30. Date of the recorded report; individual start and finish times are not reconstructed.

## Starting idea

Write squarefree integers as prime subsets subject to a logarithmic weight bound. The question was whether this structure forces cancellation between even and odd subset sizes.

## What was tested

The track checked finite-difference bounds, exact large-prime decompositions, Gibbs tilts and the Selberg–Delange family S_z(X) = Σ_{n≤X} μ²(n)z^{ω(n)}. Here μ is the Möbius function and ω counts distinct prime factors.

## What survived

- The finite combinatorial identities preserve parent multiplicities and the actual signs. Generic central-binomial bounds can be sharp even with rationally independent weights.

- At z = −1, S_z is M(X). All local Selberg–Delange asymptotic coefficients vanish through reciprocal-Gamma factors; this is a statement about an asymptotic expansion.

## What failed or remains unproved

Vanishing local coefficients is not a finite-X pairing and does not bound the remaining global term. Unsigned influence or anti-concentration estimates do not evaluate the needed signed covariance. Tilt reconstruction is exact only when its normalization and covariance terms are retained.

## Why the work moved on

The next track isolated the global remainder and asked what a smoothed explicit formula actually determines.

## Current scope

Local expansions and exact finite identities retained; no fixed-power cancellation estimate obtained.

“Proved” here refers to the stated mathematical claim in the linked research record. Internal AI-agent checks are scoped checks, not external peer review. Numerical and formal checks have separate limits described in [Reproducibility](../reproducibility.md). No priority or novelty claim is made.

## Canonical records

- [Detailed source report](../../../../reports/research/weighted_prime_halfspace.md)
- [Completion report](../../../../reports/research/weighted_prime_halfspace/completion_report.txt)
- [Scoped internal audit](../../../../audits/proofs/audits/weighted_prime_halfspace_adversarial.md)
- [Historical state record](../../../../../data/source-records/research/weighted_prime_halfspace_state.json)
- [Recorded validation](../../../../../data/source-records/research/weighted_prime_halfspace/validation.json)

The source archive preserves the original Japanese research prose. These links point to publication copies, not third-party paper downloads. The [source map](../source-map.md) explains historical state files and [references](../references.md) distinguish publication status from verification.

[Research timeline](../timeline.md)
