**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/lemmas/global_kernel_energy.md` · Original SHA-256: `6751b902f7bfd6f9459a6c572bc3ad1cbc0400ffa1da72b93281c944ef6c938f`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 全実線上の非負密度に対する補助的エネルギー不等式

作成: 2026-09-29、ROOT。状態: PROVED（記載の仮定の下での解析的証明。独立監査済み、未形式化）。
新規性: 既知の汎関数・cosine最小化機構の再導出。新規性を主張しない。

目的は、既知の固定窓 kernel 最適化の外側にも同じ人工的な汎関数を延長した場合に、
その汎関数の最小値を正確に計算すること。実際のゼータ pair-correlation 公式が
窓の外でも同じ形で成立するとは仮定しないし、結論しない。

## G1. 主張

\(f:\mathbb R\to[0,\infty)\) は可測、\(f\in L^1\cap L^2\)、
\(\int f=1\)、\(\int |x|f(x)dx<\infty\) とする。

\[
 F(x)=\int_{-\infty}^x f(t)dt,\qquad
 E(f)=\int f^2+\iint |x-y|f(x)f(y)dxdy.
\]

このとき

\[
 \boxed{E(f)-\frac{\pi}{2\sqrt2}
 =\int_{\mathbb R}\left(f(x)-\sqrt{2F(x)(1-F(x))}\right)^2dx\ge0.}
\tag{G1}
\]

等号は、ある \(c\in\mathbb R\) について a.e. に

\[
 f(x)=\begin{cases}
 \frac1{\sqrt2}\cos(\sqrt2(x-c)),&|x-c|\le\pi/(2\sqrt2),\\
 0,&\text{otherwise}
 \end{cases}
\tag{G2}
\]

の場合、かつその場合に限る。

## G2. 導出

まず \(|x-y|\le|x|+|y|\) から相互作用エネルギーは有限。
区間指示関数を用いて \(|x-y|\) を積分表示し、非負 integrand に Tonelli を適用すると

\[
 \iint |x-y|f(x)f(y)dxdy=2\int_\mathbb R F(t)(1-F(t))dt.\tag{G3}
\]

端点の等号／不等号の違いは積分に影響しない（密度は原子を持たない）。
したがって \(b=\sqrt{2F(1-F)}\in L^2\)。
\(F\) は各有限区間で絶対連続、\(F'=f\) a.e.、
\(F(-\infty)=0\)、\(F(+\infty)=1\)。

\[
 A(u)=\int_0^u\sqrt{t(1-t)}dt\quad(0\le u\le1)
\]

は \(C^1\) で導関数有界なので、有限区間 \([-R,R]\) で chain rule により

\[
 \int_{-R}^R f(x)\sqrt{F(x)(1-F(x))}dx=A(F(R))-A(F(-R)).
\]

被積分関数は非負。\(R\to\infty\) で単調収束し、右辺は \(A(1)-A(0)\)。
\(t=(1+\sin u)/2\) と置換すると

\[
 \int_0^1\sqrt{t(1-t)}dt
 =\frac14\int_{-\pi/2}^{\pi/2}\cos^2u\,du=\frac\pi8.
\]

従って \(2\int fb=2\sqrt2(\pi/8)=\pi/(2\sqrt2)\)。
\(f,b\in L^2\) の平方完成 \(\int(f-b)^2=\int f^2+\int b^2-2\int fb\)
と (G3) で (G1) を得る。無限遠の境界項を省略する処理はない。

## G3. 等号の分類

(G1) の等号は \(f=b\) a.e. と同値。
\(F\) の連続性・単調性・両端極限から、\(J=\{x:0<F(x)<1\}\) は空でない区間。
その任意のコンパクト部分区間上で

\[
 \frac{d}{dx}\arcsin(2F(x)-1)
 =\frac{F'(x)}{\sqrt{F(x)(1-F(x))}}=\sqrt2\quad\text{a.e.}
\]

である。分母はそのコンパクト上で正の下界を持つので chain rule が合法。
ゆえに \(\arcsin(2F(x)-1)=\sqrt2(x-c)\) on \(J\)。
値域 \((-\pi/2,\pi/2)\) と端点での連続性・全質量条件により
\(J=(c-\pi/(2\sqrt2),c+\pi/(2\sqrt2))\)。
外側では \(F\) はそれぞれ0と1であり、微分すると (G2) を得る。
逆に (G2) は非負、質量1、有限 support を持ち、対応する \(F\) を直接計算すれば
\(f=\sqrt{2F(1-F)}\) a.e.。したがって等号を達成する。

## G4. Candidate policy / 限界

- RH同値か: いいえ。任意の非負確率密度に関する実解析の命題。
- 特殊ケース: 固定窓の cosine 最適化と整合。ただし係数・制約が異なる。
- 非負性仮定: 必須。符号付き \(f\) ではCDFが [0,1] 内とは限らない。
- 領域: \(L^1\cap L^2\) と有限1次モーメントを明示。原子測度は対象外。
- 交換: 非負 integrand は Tonelli、chain rule は有限区間、その後単調収束。
- 数値: (G1) の根拠は数値計算ではない。
- 先行研究: aggregation-diffusion / Gini mean difference との関係を検索したが、
  この正確な式の優先権は未確認。検索不発は新規性の証拠でない。
- ゼータへの適用: 実際の pair-correlation の許容 support を拡張する定理はない。
  したがって \(2-\pi/(2\sqrt2)\) を新しい零点割合として報告してはならない。
- 結果の意味: 同じ人工的エネルギーの最適化には厳密な下限がある。
  Weil 形式の普遍的正値性も RH も証明しない。

独立監査: `proofs/audits/global-kernel-candidate.md`。非負性を落とすと E=−61/12 となる明示反例があり、仮定を保持する。

先行研究照合: `literature/notes/global-energy-prior-art.md`。Carrillo et al. (2019) のaggregation–diffusion汎関数と、Tschukin et al. (2017) のdouble-obstacle界面プロファイルに対応。平方剰余の同じ記述の最古出典は未特定だが、新規性の根拠にはしない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/global-energy-prior-art.md`](../../../literature/literature/notes/global-energy-prior-art.md)
- [`proofs/audits/global-kernel-candidate.md`](../../../audits/proofs/audits/global-kernel-candidate.md)
