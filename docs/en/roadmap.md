# Dependency roadmap {#dependency-roadmap}

**STATUS: RIEMANN HYPOTHESIS OPEN**

**B PROGRAM: CONTINUE. L7 complete. L8 not started.**

As of 2026-10-09, B investigates the ZFC independence of $\rho$, the arithmetic RH sentence fixed in L2-D 1.0.0. L7 normalization and proof transfer with costs are retained limited results; no new independence connection has been obtained.

## Current B and its open obligations

| Object | Established scope | Remaining gap |
|---|---|---|
| Fixed $\rho$ | Explicit arithmetic construction; arithmetic equivalence in PA and RH equivalence in ZFC at the usual-mathematics level | A proof, negation or unprovability result for $\rho$ itself |
| L7 normalization | Elimination of prime-support gaps, with integer and precision bounds | PA-internal certification of global violation preservation; machine proof |
| Transfer in the same proof system | An additional-character upper bound from a restricted section to the original section | Lower bounds for all proofs; a new reduction or model input relevant to independence |
| I / II | $\operatorname{Con}(\mathrm{ZFC}+\neg\rho)$ / $\operatorname{Con}(\mathrm{ZFC}+\rho)$ | Both OPEN, **2 → 2** |

B continues by the researcher's choice. General incompleteness, restriction of an input family and proof-length upper bounds do not close these obligations. No concrete L8 plan has been adopted; L8 and Cycle 18 are not started. See the [update through L7](updates/2026-10-09-logic-rh-l7.md).

## Finite-Weil route: HOLD

The roadmap below preserves **the conditional route adopted through Cycle 17, 2026-10-08**. CAP/PAR are two conditions separate from B's I/II; both remain OPEN, 2 → 2. The conditional transfer and CORE-S are retained. No universal impossibility of this route has been established.


## Dependencies through Cycle 17 {#current-direction}

| Node | Requirement | Status |
|---|---|---|
| CAP | $\|(I-G_{+,j})P_{N_j}R_{a_j}k\|_2\to0$ | Actual capture in the full even ground space remains unproved |
| PAR | Eventually $e_->e_+$ on that same sequence | Strict parity remains unproved |
| CORE-S → ES | At each finite point, strict parity gives a simple even ground | Auxiliary finite result; no independent $\Delta_+>0$ obligation |
| Adopted transfer | Real-zero structure from ES and strong-L² capture give complex locally uniform convergence | Conditional implication; actual antecedents unproved |
| Value normalization and zero preservation | After nonzero-limit and convention checks, use proxy convergence and Hurwitz/Rouché | Existing implications; RH remains unproved |

The resolving sequence satisfies $a_j\to\infty$ and $a_j/(N_j+1)\to0$. CAP and PAR must hold on the same sequence.

$$a_j\to\infty,\qquad\frac{a_j}{N_j+1}\to0,$$

$$\mathrm{CAP}:\quad\|(I-G_{+,j})P_{N_j}R_{a_j}k\|_2\to0,$$

$$\mathrm{PAR}:\quad e_-(a_j,N_j)>e_+(a_j,N_j)\quad\text{eventually}.$$

$$\mathrm{CAP}+\mathrm{PAR}\Longrightarrow\mathrm{CORE\text{-}S}/\mathrm{ES}\Longrightarrow\text{adopted transfer}\Longrightarrow\mathrm{RH}.$$

[CORE-S](updates/2026-10-07-core-s.md) and the [joint transfer](updates/2026-10-05-joint-transfer.md) remain adopted. The ES-independent [earlier CMP-R](updates/2026-10-01-cmp-es.md) is a separate sufficient condition; its rate is not added to the joint branch. **CASE D — CMP OPEN + ES OPEN.**

## Branches kept off the main route {#branches-kept-off-the-main-route}

- A1's boundary-visible direction remains an auxiliary finite theorem. Actual cofinal shortening through visibility and canonical convergence was not obtained; future shortening is not proved impossible.
- F-RM and C-QP were rejected only in their specified connection classes. B-PO remains an unproved parked candidate.
- Prime-only minimization and positive affine/isometric phase representations preserving its minimizers fall under the Cycle 15 no-go. The completed form does not.
- Cycle 17 excludes a fixed-profile completed residual with one sign for all sufficiently large continuous parameters. It does not exclude selected cofinal subsequences, adaptive trials or ordering of the true minima.

## Stopping point of the earlier route {#next-question-and-stopping-point}

No third route, truncation or generic operator theory is started automatically. The remaining question in this route is actual CAP and PAR on one sequence. Rebuilding existing transfer theory does not establish its antecedents. Cycle 17 ended without starting Cycle 18.

**CMP: NOT ESTABLISHED. ES: NOT ESTABLISHED.**

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

**COFINAL COMPATIBILITY: NOT ESTABLISHED.**

**COFINAL INCOMPATIBILITY: NOT ESTABLISHED.**

[Research update through Cycle 17](updates/2026-10-08-cycles-6-17.md) · [Timeline](timeline.md) · [State record](../../data/current-state-2026-10-08.json)

## Retained derivative-route roadmap — 2026-09-30 {#retained-derivative-route-roadmap-2026-09-30}

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

## Why density is not the missing comparison {#why-density-is-not-the-missing-comparison}

For a fixed even function $f$ and a fixed error tolerance, cyclicity supplies a finite derivative combination close to $f$ in $L^2$. The ground state here changes with the cutoffs. An estimate uniform in those cutoffs is a stronger statement. Small singular values, increasing derivative order, and the gap between a trial-space minimum and the full-system minimum all remain relevant.

Priority 2 adds fixed-head rank results and explicit finite conditioning certificates. The pending order is now uniform conditioning and lift estimates for changing heads, growing-dimension constants, full even-ground capture, then parity. No full-ground conclusion follows from the finite-head update.

## Conditions for reopening a route {#conditions-for-reopening-a-route}

A new input must discharge an existing obligation rather than restate it. Examples include a quantitative conditioning bound for the actual derivative columns, an error estimate uniform in an admissible joint limit, or a verified comparison to the full ground state. A new name for positivity, bounded scaling, or zero-free convergence is not such an input.

See [local-to-global](tracks/14-local-to-global.md), [common parent](tracks/15-common-parent.md), [rate/history](tracks/16-rate-history.md), and [hierarchical selection](tracks/17-hierarchical-selection.md) for the provenance of these obligations.
