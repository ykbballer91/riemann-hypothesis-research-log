# Riemann Hypothesis Research Log

**STATUS: RIEMANN HYPOTHESIS OPEN**

An AI-assisted research record curated by **[@ykbballer91](https://github.com/ykbballer91)**. This repository documents attempts, auxiliary results, counterexamples, and unresolved dependencies. It does not establish the Riemann Hypothesis.

The organizing question is what additional arithmetic information could constrain every nontrivial zero of the Riemann zeta function to real part $1/2$. The record follows several approaches through their successes and stopping points. Failed approaches are part of the evidence, rather than material removed from the final story.

## Start here

- [Reader's guide](docs/index.md): the question, terminology, and how to read the evidence.
- [Research timeline](docs/timeline.md): 17 tracks in the original inventory, followed by dated auxiliary-result and research-status updates.
- [Current state](docs/current-state.md): established auxiliary results and the remaining gap.
- [Dependency roadmap](docs/roadmap.md): which implications are conditional or open.
- [Methodology](docs/methodology.md) and [status legend](docs/status-legend.md): what each label means.
- [Source map](docs/source-map.md), [references](docs/references.md), and [reproducibility](docs/reproducibility.md): the supporting record.
- [Build the documentation site](docs/site-building.md): local preview and the gated Pages workflow.

## Latest update — 2026-10-01

[既存定理の委譲と CMP / ES](docs/updates/2026-10-01-cmp-es.md)：19項目中12項目の一般理論・固定範囲の証明を既存定理へ委譲。新たに解決した actual moving-Weil の漸近評価は0。現在採用する直接ルートの未証明の中心義務は、複素領域での最低状態・プロレート近似の比較（CMP）と、同じ共終列上での最終的な単純・偶性（ES）の二種類に絞られた。

**CASE D — CMP OPEN + ES OPEN.** 通常の $L^2$ 収束や一点の有限認証でこれらを置き換えない。**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

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

Cyclicity itself is qualitative density. A subsequent [finite-head update](docs/tracks/19-finite-even-head-spanning.md) proves exact spanning by some finite derivative prefix for each fixed head, and minimal-prefix spanning on specified ranges. It separates coordinate conditioning from physical lift cost. Neither result supplies uniform approximation of a parameter-dependent ground state or Weil-form control. **Growing-order selection, full finite-ground capture, the required even/simple ground-state condition, the transform comparison $G^*$, and RH remain open.** See the [current state](docs/current-state.md) for the exact boundaries.

## What is in this repository

The edited English guide is intended to stand alone. The supporting research archive retains its original language, predominantly Japanese, with publication edits for portable references and context. Historical states remain historical; the editorial summary does not silently overwrite them.

`PROVED` refers to the scope of a particular auxiliary argument. Internal independent AI audits, numerical checks, and selected Lean declarations have different evidential roles. They are not external peer review or formal verification of the complete research program.

The [source manifest](data/source-manifest.json) records original and exported hashes separately. Third-party papers, private working material, machine environments, and old binary release bundles are not included.

## Publication and citation

Version **0.1.0** was published on **2026-09-30**, after the Phase 3 review and final private-branch CI passed. Read the [documentation website](https://ykbballer91.github.io/riemann-hypothesis-research-log/) and [publication report](audit/publication_report.md). The [pre-publication content review](audit/phase3_final_content_review.md) records the release gate. The Pages workflow retains its explicit deployment guard.

If you use this research log, please cite this repository using [CITATION.cff](CITATION.cff). The author display is `@ykbballer91`; AI assistance is disclosed in [methodology](docs/methodology.md).

## Licenses

- Original Markdown/text/figures are licensed under **CC BY 4.0**, unless otherwise noted: [LICENSE-TEXT](LICENSE-TEXT).
- Original source code and experiment scripts are licensed under the **MIT License**, unless otherwise noted: [LICENSE-CODE](LICENSE-CODE).
- Third-party quotations and cited works remain under their original rights. Links and bibliographic descriptions do not relicense the cited works.

Original prose in structured records follows the text license; original executable code and formal proof source follow the code license. Historical attribution/license fields are preserved as snapshot data, not as the current publication policy. See [licensing and attribution](docs/licensing.md).
