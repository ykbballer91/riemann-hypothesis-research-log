# Dependency roadmap

**STATUS: RIEMANN HYPOTHESIS OPEN**

## Current direct route — 2026-10-01 update

**CASE D — CMP OPEN + ES OPEN.** 現在採用している直接ルートの未証明の中心義務は二種類であり、RHの残りの難易度や距離を表す数ではない。

| 義務 | 必要な内容 | 状態 |
|---|---|---|
| CMP | 値規格化した実際の有限Weil最低状態とプロレート近似の変換を、$\lvert\Im z\rvert<1/2$ の各コンパクト上で一様に比較 | OPEN。具体的な速度条件への還元は十分条件であり、比較自体の証明ではない |
| ES | 最終的な偶・奇最低値の厳密な順序と、偶側最低固有値の単純性 | OPEN。一点の有限認証は共終列上の証明ではない |
| 同じ列での接続 | CMPとESの双方が同じ許容される共終列上で成立 | OPEN。異なる列での成立を組み合わせない |
| 下流の移行 | 全前件を確認した上で、有限実零点定理、プロレート近似から $\Xi$ への収束、Hurwitz／Rouchéを適用 | 既存定理へ委譲可能。現在は適用を完了していない |

**最短の依存関係：** 同じ共終列上の **CMP + ES（未証明）** → 既存定理の全前件確認 → 有限実零点性・既知の近似収束 → 複素領域での零点保存。終点のRHは引き続きOPEN。

[最新更新の正確な条件と範囲](updates/2026-10-01-cmp-es.md)。19項目中12項目の委譲は一般理論・固定範囲についての整理であり、新たに解決した actual moving-Weil 漸近評価は0。旧補助結果は保存するが、それらをすべて現在の直接ルートの必須段階として再構築しない。

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
