# Dependency roadmap

**STATUS: RIEMANN HYPOTHESIS OPEN**

CORE-S, completed on 2026-10-06 and published here on 2026-10-07, derives simplicity from strict parity ordering in the actual finite Weil family. This removes one independent condition in the joint route. Counting obligations does not measure the distance or difficulty remaining before RH.

## Current direction

| Branch or obligation | Required input | Status |
|---|---|---|
| Capture on one sequence | $C_j=\|(I-G_{+,j})P_{N_j}R_{a_j}k\|_2\to0$, with $a_j\to\infty$ and $a_j/(N_j+1)\to0$ | Actual capture OPEN |
| Strict parity ordering | Eventual $e_->e_+$ on that same sequence | OPEN; compatibility and incompatibility with capture also unproved |
| CORE-S supplies ES | Strict parity forces a one-dimensional even ground eigenspace | Auxiliary PROVED result at each finite point; no separate $\Delta_+>0$ condition |
| Adopted joint transfer | ES gives finite real zeros and LP membership; strong L² capture and Clunie–Kuijlaars give complex local uniform convergence | Accepted conditionally; actual hypotheses remain unproved |
| Value normalization and zero preservation | After checking the nonzero limit and all hypotheses, use known proxy convergence and Hurwitz/Rouché | Existing implications; RH OPEN |
| Earlier CMP-R | Without assuming ES, prove $\lambda^rD_{\lambda,N}\to0$ and the corresponding projection rate for every $0<r<1/2$ | Retained separate sufficient condition; actual estimate OPEN |

The shortest joint sufficient route is **same-sequence capture + strict parity → CORE-S supplies ES → adopted transfer → RH**. Capture and parity results on unrelated sequences cannot be combined. Neither a uniform gap nor the old CMP-R rate is added as a hypothesis of this branch.

## Why this direction

The [2026-10-05 joint-transfer record](updates/2026-10-05-joint-transfer.md) listed capture, parity ordering and simplicity separately. CORE-S removes the independent simplicity check. Boundary mass and individual prime terms remain auxiliary records. The derivative hierarchy is also retained as auxiliary work, not a mandatory stage of the current joint branch.

## Next action and stopping point

CMP/ES remain the main route. The research questions concern capture and strict parity on the same resolving cofinal sequence. This publication synchronization does not launch the next research task.

**CASE D — CMP OPEN + ES OPEN.** The earlier delegation of **12 of 19 items** of generic or fixed-scope theory is unchanged. Newly discharged actual asymptotic obligations: **0**. [Latest finite lemma and hypotheses](updates/2026-10-07-core-s.md) · [Earlier CMP-R](updates/2026-10-01-cmp-es.md).

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

**COFINAL COMPATIBILITY: NOT ESTABLISHED.**

**COFINAL INCOMPATIBILITY: NOT ESTABLISHED.**

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
