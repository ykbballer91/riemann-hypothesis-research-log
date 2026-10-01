# Dependency roadmap

**STATUS: RIEMANN HYPOTHESIS OPEN**

The current route separates the comparison of two families from the spectral properties of the actual finite ground. Both require new actual estimates. The two categories are not a measure of the distance or difficulty remaining before RH.

## Current direction

| Obligation | What must be shown | Boundary |
|---|---|---|
| CMP | Value-normalized transforms of the actual ground and prolate proxy approach each other uniformly on compact subsets of $\lvert\Im z\rvert<1/2$ | OPEN; reduction to a sufficient rate is not a proof of comparison |
| ES | Eventual strict even/odd ground ordering and simplicity within the even sector | OPEN; one finite certificate does not settle a cofinal sequence |
| Common sequence | Both obligations hold on the same admissible cofinal sequence | OPEN; separate existence results cannot be combined automatically |
| Downstream implications | Apply the finite real-zero theorem, proxy convergence to $\Xi$, and Hurwitz/Rouché after checking every hypothesis | Existing theorems are available; the application is incomplete |

**Shortest dependency chain:** CMP + ES on the same sequence → verify the imported hypotheses → finite real-zero property and known proxy convergence → zero preservation in the required complex domain. RH remains OPEN.

## Why this direction

The import audit separates existing general mathematics from the unresolved arithmetic estimates. Earlier auxiliary results remain in the record; they need not all be rebuilt as compulsory stages of the direct route.

## Next action

Examine the required ground/proxy comparison rate and eventual simple-even ground condition independently. Keep the common-sequence requirement explicit; do not introduce a third main route automatically.

## Technical audit context

**CASE D — CMP OPEN + ES OPEN.** General theory or fixed-scope proofs for **12 of 19 items** can be delegated. Newly resolved asymptotic estimates for the actual moving family: **0**. This is not the resolution of 12 RH obstacles. [Exact CMP-R and ES conditions](updates/2026-10-01-cmp-es.md).

## Retained derivative-route roadmap — 2026-09-30

The table and discussion below preserve the earlier roadmap before the import/CMP/ES update. Its then-pending order is historical. The program is a set of conditional dependencies, not a sequence whose later conclusions have already been proved.

| Step | Exact role | Current status |
|---|---|---|
| Actual finite arithmetic system | Finite Fourier restrictions of the Weil form retain the arithmetic input used in the cited construction | Defined; scope recorded in local-to-global and common-parent tracks |
| Restricted hierarchical selection | Minimizing directions in each fixed finite derivative trial space approach $k$, under the stated support/projection hypotheses | Auxiliary PROVED result in the record |
| Even-$L^2$ cyclicity | The union of derivative trial spaces is dense in even $L^2$ | Auxiliary PROVED, without RH |
| Fixed even-head spanning | Each fixed head is exactly spanned by some finite derivative prefix; minimal prefix is certified in stated ranges | Auxiliary PROVED; not a uniform moving-ground theorem |
| Uniform finite-head approximation | Quantify the needed order, physical lift cost and form error along changing cutoffs | OPEN |
| Growing-order hierarchy | Control every fixed-order constant as the derivative order grows | OPEN |
| Quantitative full-even-ground capture | Approximate the varying full even ground state with controlled dimension, coefficients, and error | OPEN |
| Parity and ES | Identify a simple even lowest state on a suitable sequence of full finite systems | OPEN in the required global passage |
| $G^*$ comparison | Compare value-normalized Fourier transforms of the actual ground and prolate proxy uniformly on the required complex sets | OPEN |
| Proxy to $\Xi$ | Use the known proxy approximation with its exact parameter and normalization restrictions | KNOWN literature input, not a statement about the actual ground |
| Real-zero preservation | The actual finite ground has the required real-zero property when the applicable theorem's hypotheses, including ES, hold | CONDITIONAL application of a KNOWN theorem |
| Global passage | Nonzero locally uniform limit of real-zero entire approximants has no off-real zeros | KNOWN Hurwitz/Rouché implication |
| RH | Identify that limit with the actual $\Xi$ while fulfilling every preceding obligation | OPEN |

## Why density is not the missing comparison

For a fixed even function $f$ and a fixed error tolerance, cyclicity supplies a finite derivative combination close to $f$ in $L^2$. The ground state here changes with the cutoffs. An estimate uniform in those cutoffs is a stronger statement. Small singular values, increasing derivative order, and the gap between a trial-space minimum and the full-system minimum all remain relevant.

Priority 2 adds fixed-head rank results and explicit finite conditioning certificates. The pending order is now uniform conditioning and lift estimates for changing heads, growing-dimension constants, full even-ground capture, then parity. No full-ground conclusion follows from the finite-head update.

## Conditions for reopening a route

A new input must discharge an existing obligation rather than restate it. Examples include a quantitative conditioning bound for the actual derivative columns, an error estimate uniform in an admissible joint limit, or a verified comparison to the full ground state. A new name for positivity, bounded scaling, or zero-free convergence is not such an input.

See [local-to-global](tracks/14-local-to-global.md), [common parent](tracks/15-common-parent.md), [rate/history](tracks/16-rate-history.md), and [hierarchical selection](tracks/17-hierarchical-selection.md) for the provenance of these obligations.
