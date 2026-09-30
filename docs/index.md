# A research log, including the dead ends

**STATUS: RIEMANN HYPOTHESIS OPEN**

This record asks how the arithmetic of the Riemann zeta function could force all its nontrivial zeros onto the line $\Re s=1/2$. It follows several formulations of that question and records when a reformulation merely transfers the same unresolved requirement to a new language.

Curated by **[@ykbballer91](https://github.com/ykbballer91)**, with AI assistance. The research record begins on 2026-09-29; the current editorial snapshot is dated 2026-09-30. These are research and preparation dates, not a public release date.

## Three ways to read

**For the result and its limits:** start with [current state](current-state.md), then the [dependency roadmap](roadmap.md). The newest unconditional auxiliary result is even-$L^2$ cyclicity of a theta-kernel derivative family. The unresolved problem is quantitative full-ground comparison.

**For the reasoning across attempts:** read the [timeline](timeline.md). Each track explains its starting idea, what was tested, what survived, what failed, and the reason for the next question. Tracks that ran independently are not presented as a single chronological proof.

**For verification or reuse:** use the [source map](source-map.md), [references](references.md), and [reproducibility notes](reproducibility.md). Archived source reports, internal audits, experiment records, and formal fragments remain distinguishable.

## The recurring obstruction

Several natural structures already retain the zeta zeros. The difficult step is obtaining an independent arithmetic estimate strong enough to exclude exponential growth away from the critical line. A positive metric, a bounded scaling action, a square-root Möbius estimate, or convergence of real-zero approximants can each encode this missing step. Naming one of them does not prove it.

The later work focuses on finite Weil quadratic forms and prolate concentration proxies. A restricted family of trial states can be analyzed, but a trial-space result does not yet identify the ground state of the full finite system.

## Reading the labels

`PROVED` is an auxiliary argument with stated hypotheses. `KNOWN` is a result from the cited literature. `CONDITIONAL` retains unproved assumptions. `NUMERICAL` is finite computational evidence. `FALSE` and `REJECTED` preserve unsuccessful claims or inadequate routes. `OPEN` is an obligation not discharged by this record. The [status legend](status-legend.md) gives the full distinctions.

An internal AI audit is not external peer review. A successful script run is not a proof of an asymptotic statement. A known sufficient condition is not asserted to be a sharp threshold.

## Latest update

The [cyclicity update](tracks/18-even-l2-cyclicity.md) proves that $\{k,k'',k^{(4)},\ldots\}$ spans a dense subspace of even $L^2(\mathbb R)$ without using RH. It does not supply the conditioning, joint-limit estimates, or form-domain control needed for full ground capture.

[Publication review](../audit/phase2_publication_review.md) · [Methodology](methodology.md) · [Licensing](licensing.md)

