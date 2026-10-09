# A guide to the research log {#a-guide-to-the-research-log}

**STATUS: RIEMANN HYPOTHESIS OPEN**

The Riemann Hypothesis asks whether every nontrivial zero of the zeta function has real part $1/2$. This log follows attempts to find arithmetic information strong enough to enforce that conclusion. It subsequently turns to B, investigating the provability and possible ZFC independence of fixed RH. **B PROGRAM: CONTINUE. L7 complete. L8 not started.**

Curated by **@ykbballer91**, with AI assistance. Research dates, public-update dates, and the release date are distinguished throughout. The current editorial state is maintained on the [current-state page](current-state.md); earlier pages remain dated records.

## Three ways to read {#three-ways-to-read}

**For the result and its limits:** the [latest L7 update](updates/2026-10-09-logic-rh-l7.md) explains the change of question, arithmetization, prime-support normalization and proof cost. Both B obligations I/II remain OPEN, 2 → 2; finite-Weil CAP/PAR belong to a separate HOLD route. Start with [current state](current-state.md), then the [roadmap](roadmap.md). The [update through Cycle 17](updates/2026-10-08-cycles-6-17.md) explains fixed-trial oscillation and its limits. [CORE-S](updates/2026-10-07-core-s.md) and the [October 5 joint-transfer update](updates/2026-10-05-joint-transfer.md) remain dated history.

**For the reasoning across attempts:** read the [timeline](timeline.md). Each track records its starting idea, tests, retained results, stopping point, and next question. Parallel investigations are not presented as a single serial proof.

**For verification or reuse:** complete new L0–L7 proofs, internal audits and code remain privately preserved. The public summaries alone do not provide full third-party reproduction evidence. Use the [source map](source-map.md), [references](references.md), and [reproducibility notes](reproducibility.md). Original research reports, scoped internal audits, numerical outputs, and formal fragments have different evidential roles.

## The recurring obstruction {#the-recurring-obstruction}

Several natural structures already retain the zeta zeros. The difficult step is obtaining an independent arithmetic estimate that excludes growth away from the critical line. A positive metric, a bounded scaling action, a square-root Möbius estimate, or convergence of real-zero approximants may encode this requirement without proving it.

The earlier analytic route studied finite Weil forms and prolate proxies. Minimization within a restricted trial family does not identify the ground state of the whole finite system. Qualitative density and exact spanning of a fixed finite head do not supply uniform control as the parameters grow.

## Reading the labels {#reading-the-labels}

`PROVED` refers to a particular auxiliary argument with its hypotheses. `KNOWN` is imported literature. `CONDITIONAL` retains unproved premises. `NUMERICAL` describes finite computations. `FALSE` and `REJECTED` preserve failed claims or routes. `OPEN` means the stated obligation is not discharged. See the [full legend](status-legend.md).

An internal AI audit is not external peer review. A successful script does not establish an untested asymptotic statement. A sufficient resolution condition is not asserted to be a sharp threshold.

## Earlier auxiliary updates {#earlier-auxiliary-updates}

The [cyclicity result](tracks/18-even-l2-cyclicity.md) proves that the even derivatives of $k$ are dense in even $L^2$, without RH. The [finite-head result](tracks/19-finite-even-head-spanning.md) gives exact rank statements, tail criteria, and two finite interval certificates. Neither closes the full-ground or complex-transform comparison.

[Methodology](methodology.md) · [Licensing](licensing.md) · [Publication report](../../audit/publication_report.md)
