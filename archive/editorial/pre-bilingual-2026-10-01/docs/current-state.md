# Current state — what the record establishes

**STATUS: RIEMANN HYPOTHESIS OPEN**

Latest public update: **2026-10-01**, summarizing completed research dated **2026-09-30**. Historical source states remain unchanged; the latest editorial status is recorded in [research-state.json](../../../../data/research-state.json).

## 現在の直接ルート — CMP OPEN / ES OPEN

[最新更新](updates/2026-10-01-cmp-es.md)では、既存定理監査の19項目中12項目を一般理論・固定範囲の証明として委譲した。actual moving-Weil の未解決漸近評価が新たに解決した件数は **0**。現在採用する直接ルートの中心義務は次の二種類で、いずれも未証明である。

- **CMP：** 実際の有限Weil最低状態とプロレート近似の値規格化フーリエ変換を、$|\Im z|<1/2$ の各コンパクト集合上で一様に比較する。$\lambda^rD_{\lambda,N}\to0$（すべての $0<r<1/2$）は、記載された解像条件のもとでの十分条件であり、未証明。通常の $L^2$ 収束だけでは足りない。
- **ES：** 同じ共終列上で最終的に $e_->e_+$、$\Delta_+>0$ を示す。一点 $c=13,N=4$ の単純・偶最低状態の有限認証を、最終的なESへ一般化しない。

**CASE D — CMP OPEN + ES OPEN.** 両義務を独立に検証し、同じ列で全前件を満たして初めて、既知の有限実零点定理・プロレート近似の収束・Hurwitz／Rouchéを接続できる。新しい第三ルートへ自動的に広げない。

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

## Retained snapshot — 2026-09-30, before the import/CMP/ES update

The following earlier summary is preserved as history, not as an expanded list of current main tracks. Its evidence is mapped in [source-map](source-map.md).

## Fixed finite derivative spaces

Set $a=\log\lambda$, $Y=\pi\lambda^2$, and

$$\mathcal R_m=\mathrm{span} \lbrace k,k'',\ldots,k^{(2m)}\rbrace,\qquad \widehat k(x)=\Xi(x)/4.$$

The hierarchical-selection record establishes a support-only selection theorem for **each fixed finite $m$**: the minimizing direction within the restricted family tends to $k$. For the canonical support restriction followed by Fourier projection, the same restricted conclusion is obtained under

$$\liminf\frac{N}{aY}>\frac4{\pi^2}.$$

This is a sufficient resolution condition. The record does not identify it as necessary or optimal. Constants in a fixed-$m$ statement have not been made uniform for $m\to\infty$. See [hierarchical selection](tracks/17-hierarchical-selection.md).

## Unconditional cyclicity

The subsequent auxiliary theorem states

$$\overline{\mathrm{span} \lbrace k^{(2j)}:j\ge0\rbrace}^{L^2}=L^2_{\mathrm{even}}(\mathbb R).$$

The proof uses exponential integrability of $|\Xi(x)|^2dx$, a polynomial-density argument, and Plancherel. It does not assume RH or simple zeros. Even polynomials are dense in the **even** weighted sector, not in the entire weighted space. See [cyclicity](tracks/18-even-l2-cyclicity.md).

Qualitative $L^2$ density does not give a uniform approximation rate for a changing ground state. It also does not establish density in a Weil form norm, stability of a finite derivative-column system, or convergence of Fourier transforms throughout a complex strip.

## Fixed finite even heads

The [Priority 2 update](tracks/19-finite-even-head-spanning.md) proves that each fixed head $E_N^+$, of dimension $N+1$, is exactly spanned by a sufficiently long initial derivative family after sharp restriction and projection. The ideal no-tail rank is $\min(m+1,r)$, where $r$ counts nonzero Xi grid samples. Without a grid hit, the ideal minimal order is $m=N$.

For each fixed $N$, the actual minimal prefix $m=N$ works for all sufficiently large windows; the exceptional positive window widths form a finite, not explicitly determined set. Analytic tail bounds plus Arb arithmetic certify two explicit small parameter intervals. These are auxiliary finite-rank results. Physical-Gram diagnostics are distinct from those certificates.

Exact spanning does not give uniform conditioning: with $N=m$ fixed, the physical smallest singular value still decays in the large-window limit. No quantitative order bound or form-norm estimate for a moving ground follows.

## What remains open

1. An explicit optimal derivative cutoff at every parameter, and uniform quantitative conditioning/lift bounds for changing finite heads. The fixed-head exact-spanning existence theorem and specified finite certificates are established.
2. Bounds on every relevant constant when the derivative cutoff $m$ grows with $a,N$.
3. Quantitative capture of a **parameter-dependent full finite even ground state in the joint limit**, rather than fixed-head algebraic representation or minimization within a fixed trial space.
4. The needed relation between even and odd ground levels, together with a simple/even lowest state along the required approximation sequence (the recorded ES condition).
5. The normalized transform comparison $G^*$ between the actual Weil ground state and the prolate proxy, on the complex sets required for zero preservation.
6. Transfer to the actual $\Xi$ through correctly normalized, locally uniform convergence.

None of the auxiliary results above bypasses these obligations. The [roadmap](roadmap.md) separates established arrows from open ones.

## Evidence boundaries

These are written auxiliary arguments with internal independent AI audit records. Selected earlier Lean declarations formalize particular elementary lemmas; they do not formalize the current entire research chain. Numerical overlap, finite spectral agreement, source-preservation checks, and publication validation have their own narrower scopes.

No new unconditional bound on the real parts of all zeta zeros has been obtained here. No percentage of RH completion is assigned.

