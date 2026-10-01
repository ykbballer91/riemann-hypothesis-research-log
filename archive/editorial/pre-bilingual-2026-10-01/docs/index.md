# Riemann Hypothesis Research Log

**STATUS: RIEMANN HYPOTHESIS OPEN**

An adversarial research log of AI-assisted exploration: auxiliary results, failed approaches, counterexamples, numerical diagnostics, literature audits, and an unresolved global comparison.

This record asks how the arithmetic of the Riemann zeta function could force all its nontrivial zeros onto the line $\Re s=1/2$. It follows several formulations of that question and records when a reformulation merely transfers the same unresolved requirement to a new language.

Curated by **[@ykbballer91](https://github.com/ykbballer91)**, with AI assistance. The research record begins on 2026-09-29; the original editorial snapshot is dated 2026-09-30. The latest public update below was added on 2026-10-01. Research dates and public update dates are recorded separately. The actual public release occurred on 2026-09-30, as recorded in the publication report.

## 2026-10-01 更新 — CMP と ES に集中する

**CASE D — CMP OPEN + ES OPEN.**

**更新。** 既存研究を洗い直した結果、有限試験関数の構成や固定範囲の作用素論など、19項目中12項目の一般部分は既存定理へ委譲できることが分かった。12個のRH障害を解決したという意味ではなく、actual moving-Weil の未解決漸近評価が新たに解決した件数は0である。

現在採用している直接ルート上の未証明の中心義務は、二種類に絞られた。**ES**は、実際の有限Weil最低状態が最終的に単純かつ偶になること。**CMP**は、その最低状態が、$\Xi$へ収束する既知のプロレート近似に、値で規格化したフーリエ変換として複素帯域 $|\Im z|<1/2$ のコンパクト集合上でも一様に近づくこと。どちらも未証明だが、ESは偶・奇の最低値差と偶側内部の固有値差、CMPは一つの十分条件として必要な収束速度まで具体化した。

**なぜ変えたか。** 一般論をさらに作るより、既存数学で閉じている部分を外し、実際のゼータに固有の未証明部分を明確にするため。ここからは面を広げず、CMPとESの二点に集中する。

**NEXT ACTION。** 実際の最低状態とプロレート近似が必要な速度で近づく理由と、最低状態が最終的に一意な偶状態になる理由を、それぞれ独立に検証する。

[今回の更新全文：収束速度の十分条件・有限認証の範囲・同じ共終列という条件](updates/2026-10-01-cmp-es.md)。**STATUS: RIEMANN HYPOTHESIS OPEN.**

## Three ways to read

**For the result and its limits:** start with [current state](current-state.md), then the [dependency roadmap](roadmap.md). The earlier auxiliary results concern even-$L^2$ cyclicity and exact spanning of fixed finite even Fourier heads. Uniform estimates for changing heads and full-ground comparison remain unresolved.

**For the reasoning across attempts:** read the [timeline](timeline.md). Each track explains its starting idea, what was tested, what survived, what failed, and the reason for the next question. Tracks that ran independently are not presented as a single chronological proof.

**For verification or reuse:** use the [source map](source-map.md), [references](references.md), and [reproducibility notes](reproducibility.md). Archived source reports, internal audits, experiment records, and formal fragments remain distinguishable.

## The recurring obstruction

Several natural structures already retain the zeta zeros. The difficult step is obtaining an independent arithmetic estimate strong enough to exclude exponential growth away from the critical line. A positive metric, a bounded scaling action, a square-root Möbius estimate, or convergence of real-zero approximants can each encode this missing step. Naming one of them does not prove it.

The later work focuses on finite Weil quadratic forms and prolate concentration proxies. A restricted family of trial states can be analyzed, but a trial-space result does not yet identify the ground state of the full finite system.

## Reading the labels

`PROVED` is an auxiliary argument with stated hypotheses. `KNOWN` is a result from the cited literature. `CONDITIONAL` retains unproved assumptions. `NUMERICAL` is finite computational evidence. `FALSE` and `REJECTED` preserve unsuccessful claims or inadequate routes. `OPEN` is an obligation not discharged by this record. The [status legend](status-legend.md) gives the full distinctions.

An internal AI audit is not external peer review. A successful script run is not a proof of an asymptotic statement. A known sufficient condition is not asserted to be a sharp threshold.

## Previous updates — 2026-09-30

The [cyclicity update](tracks/18-even-l2-cyclicity.md) establishes that $\{k,k'',k^{(4)},\ldots\}$ spans a dense subspace of even $L^2(\mathbb R)$ without using RH. It does not supply the conditioning, joint-limit estimates, or form-domain control needed for full ground capture.

The subsequent [finite-head update](tracks/19-finite-even-head-spanning.md) gives a rank theorem, explicit tail criteria, and two finite interval certificates. Exact representation in a fixed projected space does not control a moving ground or its Weil energy.

[Publication report](../../../../audit/publication_report.md) · [Phase 3 publication review](../../../../audit/phase3_final_content_review.md) · [Methodology](methodology.md) · [Licensing](licensing.md)

