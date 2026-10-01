# 07. Dyadic arithmetic reduction

**STATUS: RIEMANN HYPOTHESIS OPEN**

Recorded 2026-09-30. Date of the recorded report; individual start and finish times are not reconstructed.

## Starting idea

Can the representative of a class be pushed into one side of the logarithmic line with a quantitatively small norm after repeated dilation by 2?

## What was tested

The construction used full integer Möbius inversion of the arithmetic sum, a smooth cutoff and a moment correction. Sampling the flow at powers of 2 does not restrict the arithmetic input to powers of 2.

## What survived

- For arbitrary admissible input, an explicit representative cancels the right tail. An unconditional upper bound has rate 2ⁿᐟ²(1 + n).

- A conditional Mertens estimate M(X) = O(X^θ) improves the same construction to rate 2⁽θ⁻¹ᐟ²⁾ⁿ. The endpoint family of subexponential estimates, with the reverse implication established in the notes, is equivalent to RH.

## What failed or remains unproved

The construction supplies no independent endpoint cancellation. The unconditional exponent 1/2 was not proved optimal. A compactly supported folding argument is obstructed by the actual arithmetic subspace, rather than repaired by the cutoff.

## Why the work moved on

The inquiry moved to the signed combinatorics of Möbius cancellation: first a prime complex, then prime phases and a weighted halfspace.

## Current scope

Explicit reduction and unconditional rate retained; the desired endpoint is an equivalent reformulation, not progress toward proving RH.

“Proved” here refers to the stated mathematical claim in the linked research record. Internal AI-agent checks are scoped checks, not external peer review. Numerical and formal checks have separate limits described in [Reproducibility](../reproducibility.md). No priority or novelty claim is made.

## Canonical records

- [Detailed source report](../../../archive/reports/research/dyadic_arithmetic_reduction.md)
- [Completion report](../../../archive/reports/research/dyadic/completion_report.txt)
- [Scoped internal audit](../../../archive/audits/proofs/audits/dyadic_reduction_adversarial.md)
- [Historical state record](../../../data/source-records/research/dyadic_reduction_state.json)
- [Recorded validation](../../../data/source-records/research/dyadic/validation.json)

The source archive preserves the original Japanese research prose. These links point to publication copies, not third-party paper downloads. The [source map](../source-map.md) explains historical state files and [references](../references.md) distinguish publication status from verification.

[Research timeline](../timeline.md)
