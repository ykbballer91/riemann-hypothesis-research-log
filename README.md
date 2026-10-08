# Riemann Hypothesis Research Log

[日本語版はこちら](README.ja.md) · [English website](https://ykbballer91.github.io/riemann-hypothesis-research-log/en/)

**STATUS: RIEMANN HYPOTHESIS OPEN**

An AI-assisted research record curated by **[@ykbballer91](https://github.com/ykbballer91)**. This repository documents attempts, auxiliary results, counterexamples, and unresolved dependencies. It does not establish the Riemann Hypothesis.

The organizing question is what additional arithmetic information could constrain every nontrivial zero of the Riemann zeta function to real part $1/2$. The record follows several approaches through their successes and stopping points. Failed approaches are part of the evidence, rather than material removed from the final story.

## Start here

- [Reader's guide](docs/en/index.md): the question, terminology, and how to read the evidence.
- [Research timeline](docs/en/timeline.md): 17 tracks in the original inventory, followed by dated auxiliary-result and research-status updates.
- [Current state](docs/en/current-state.md): established auxiliary results and the remaining gap.
- [Dependency roadmap](docs/en/roadmap.md): which implications are conditional or open.
- [Methodology](docs/en/methodology.md) and [status legend](docs/en/status-legend.md): what each label means.
- [Source map](docs/en/source-map.md), [references](docs/en/references.md), and [reproducibility](docs/en/reproducibility.md): the supporting record.
- [Build the documentation site](docs/en/site-building.md): local preview and the gated Pages workflow.

## Latest research update — 2026-10-08

The [Cycles 6–17 release](docs/en/updates/2026-10-08-cycles-6-17.md) publishes an auxiliary theorem: the completed residual of a fixed smooth endpoint trial takes both signs arbitrarily far out. It is a project-derived consequence of existing unconditional theorems; internal AI audit PASS is not external peer review or formal verification. It does not prove oscillation of the true minimum difference or disprove CAP/PAR. The adopted obligations remain same-sequence capture (CAP) and strict parity (PAR), **2 → 2**. CMP, ES, full even-ground capture, cofinal compatibility/incompatibility and RH remain unproved.

## Retained update — 2026-10-07

[CORE-S](docs/en/updates/2026-10-07-core-s.md) shows that strict parity ordering forces simplicity of the even ground in the actual finite Weil family. The joint route no longer needs an independent simplicity check: it requires theta-kernel capture and strict parity on the same resolving cofinal sequence. Their cofinal validity, CMP, ES and RH remain unproved. The research was completed on 2026-10-06; this publication update adds no new asymptotic estimate or proof search.

## Retained update — 2026-10-05

The [joint-transfer review](docs/en/updates/2026-10-05-joint-transfer.md) accepts a conditional connection: eventual ES and strong L² capture on the same sequence imply complex comparison without a prescribed rate, using the real-zero structure. ES and actual capture remain unproved; CMP and RH remain OPEN. The earlier ES-independent CMP-R is retained. No new actual asymptotic obligation has been discharged.

## Retained update — 2026-10-01

The [CMP / ES update](docs/en/updates/2026-10-01-cmp-es.md) focuses the selected direct route on two unproved obligations: complex comparison of the actual finite Weil ground with the known prolate proxy, and eventual simplicity and evenness on the same cofinal sequence. Neither is proved. Ordinary L² convergence and one finite certificate do not replace these obligations.

The import count, CASE D classification, and sufficient CMP-R rate are retained in the update's technical details. This is not a claim that 12 RH obstacles have been solved or that RH is close to completion.

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

## Retained frontier snapshot — 2026-09-30

The following snapshot predates the import/CMP/ES update and is retained as history.

The latest restricted selection result concerns **each fixed finite** derivative space

$$
\mathcal R_m=\mathrm{span} \lbrace k,k'',\ldots,k^{(2m)}\rbrace.
$$

Here $k$ is the actual Riemann theta kernel in the recorded normalization $\widehat k=\Xi/4$, with $\Xi(x)=\xi(1/2+ix)$. In the support hierarchy, the minimizing direction within that finite space tends to $k$. This restricted conclusion survives the canonical Fourier projection under the recorded **sufficient** resolution condition

$$
\liminf\frac{N}{aY}>\frac4{\pi^2},\qquad a=\log\lambda,\quad Y=\pi\lambda^2.
$$

A subsequent auxiliary theorem proves, without RH,

$$
\overline{\mathrm{span} \lbrace k^{(2j)}:j\ge0\rbrace}^{L^2}
=L^2_{\mathrm{even}}(\mathbb R).
$$

Cyclicity itself is qualitative density. A subsequent [finite-head update](docs/en/tracks/19-finite-even-head-spanning.md) proves exact spanning by some finite derivative prefix for each fixed head, and minimal-prefix spanning on specified ranges. It separates coordinate conditioning from physical lift cost. Neither result supplies uniform approximation of a parameter-dependent ground state or Weil-form control. **Growing-order selection, full finite-ground capture, the required even/simple ground-state condition, the transform comparison $G^*$, and RH remain open.** See the [current state](docs/en/current-state.md) for the exact boundaries.

## What is in this repository

The paired Japanese and English editorial guides are intended to stand alone. The supporting research archive retains its original language, predominantly Japanese, with publication edits for portable references and context. Historical states remain historical; the editorial summary does not silently overwrite them.

`PROVED` refers to the scope of a particular auxiliary argument. Internal independent AI audits, numerical checks, and selected Lean declarations have different evidential roles. They are not external peer review or formal verification of the complete research program.

The [source manifest](data/source-manifest.json) records original and exported hashes separately. Third-party papers, private working material, machine environments, and old binary release bundles are not included.

## Publication and citation

Version **0.1.0** was published on **2026-09-30**, after the Phase 3 review and final private-branch CI passed. Read the [documentation website](https://ykbballer91.github.io/riemann-hypothesis-research-log/) and [publication report](audit/publication_report.md). The [pre-publication content review](audit/phase3_final_content_review.md) records the release gate. The Pages workflow retains its explicit deployment guard.

If you use this research log, please cite this repository using [CITATION.cff](CITATION.cff). The author display is `@ykbballer91`; AI assistance is disclosed in [methodology](docs/en/methodology.md).

## Licenses

- Original Markdown/text/figures are licensed under **CC BY 4.0**, unless otherwise noted: [LICENSE-TEXT](LICENSE-TEXT).
- Original source code and experiment scripts are licensed under the **MIT License**, unless otherwise noted: [LICENSE-CODE](LICENSE-CODE).
- Third-party quotations and cited works remain under their original rights. Links and bibliographic descriptions do not relicense the cited works.

Original prose in structured records follows the text license; original executable code and formal proof source follow the code license. Historical attribution/license fields are preserved as snapshot data, not as the current publication policy. See [licensing and attribution](docs/en/licensing.md).
