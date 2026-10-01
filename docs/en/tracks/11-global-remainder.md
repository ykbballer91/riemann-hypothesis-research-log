# 11. The global remainder beyond local asymptotic orders

**STATUS: RIEMANN HYPOTHESIS OPEN**

Recorded 2026-09-30. Date of the recorded report; individual start and finish times are not reconstructed.

## Starting idea

If every coefficient in a local asymptotic expansion vanishes, where does the Möbius sum remain? The work used a fixed Gaussian readout to separate local expansion data from global singularities.

## What was tested

For R(u) = Σ μ(n)e^{−(u−log n)²}, absolute convergence gives the transform √π e^{s²/4}/ζ(s) for Re s > 1. Contour shifts were checked with explicit height grouping and multiplicities.

## What survived

- Finite left shifts yield a controlled grouped residue description. This is not an arbitrarily reordered or absolutely convergent sum over individual zeros.

- For this fixed readout, forward subexponential growth of A(u) = e^{−u/2}R(u) is equivalent to RH. Finite-jet models demonstrate that finite local data can miss global poles.

## What failed or remains unproved

An infinite shift to the left and the proposed unrestricted trivial-zero series fail their convergence requirements. A full analytic germ does determine its connected meromorphic continuation; it cannot be changed while keeping every Taylor coefficient. Vanishing Selberg–Delange coefficients are not vanishing Taylor coefficients of 1/ζ.

## Why the work moved on

The program paused new constructions for an inventory of actual arithmetic estimates and the precise pointwise gap.

## Current scope

Exact transform and finite-shift statements retained; the target growth estimate remains equivalent to RH.

“Proved” here refers to the stated mathematical claim in the linked research record. Internal AI-agent checks are scoped checks, not external peer review. Numerical and formal checks have separate limits described in [Reproducibility](../reproducibility.md). No priority or novelty claim is made.

## Canonical records

- [Detailed source report](../../../archive/reports/research/global_remainder_beyond_all_orders.md)
- [Completion report](../../../archive/reports/research/global_remainder/completion_report.txt)
- [Scoped internal audit](../../../archive/audits/proofs/audits/global_remainder_adversarial.md)
- [Historical state record](../../../data/source-records/research/global_remainder_state.json)
- [Recorded validation](../../../data/source-records/research/global_remainder/validation.json)

The source archive preserves the original Japanese research prose. These links point to publication copies, not third-party paper downloads. The [source map](../source-map.md) explains historical state files and [references](../references.md) distinguish publication status from verification.

[Research timeline](../timeline.md)
