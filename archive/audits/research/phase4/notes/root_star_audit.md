**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase4/notes/root_star_audit.md` · Original SHA-256: `b1d3558e21db799a37b4b27785d32a5699da67947218ed4b9e5dabfca117a60b`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase IV — product_formula_star の独立検算

2026-09-29。DESTROYER。対象は `product_formula_star.md` の表示式と scope。
**主要計算 PASS。重大な数式訂正なし。** 以下の測度・domain の精密化を併記する。
Tate 原論文の全証明を再監査したとはしない。RH の証明・反証ではない。

## 1. ambient adjoint と domain

第1変数線形の P について、x=ay の変数変換は

\[
 P(R_af,g)=|a|_\mathbb A P(f,R_{a^{-1}}g)
\]

を与える。正規化した U_a は unitary。積公式は rational a の measure preservation
を与えるが、zero-bearing quotient の norm の同定を与えないという区別は正しい。

実素点の \(\Theta=-x\partial_x\)、\(D=\Theta-1/2\) について、
\(V_\pm f(v)=e^{v/2}f(\pm e^v)\) は左右半直線を L²(dv) へ unitary に移す。
直接微分すると \(V D V^{-1}=-\partial_v\)。従って有限 adele を含めた精密な domain は

\[
 H^1\!\left(\mathbb R;
 L^2(\mathbb A_{\rm fin})\oplus L^2(\mathbb A_{\rm fin})\right)
\]

の逆像である。単なる代数的 tensor product ではなく graph norm completion を使う。
原点で左右の値を一致させる追加境界条件は不要である。
原点から離れた compactly supported smooth functions は変換後の標準 derivative core
を含むため、Schwartz–Bruhat core からこの閉生成子へ至る。
strongly continuous translation group により D は skew-adjoint、
閉作用素として同じ domain 上で \(\Theta^*=1-\Theta\)。
連続 spectrum \(1/2+i\mathbb R\) を得るが、ζ 零点の離散実現ではない。

## 2. Fourier の負方向

実 Fourier 規約は自己双対 Gaussian \(g=e^{-\pi x^2}\) を固定するもの。
\(u=\pi x^2\) とすると、Fourier 側の微分公式から原文の三多項式が得られる。
それらを線形結合すると

\[
8\mathcal F(u^3g)-30\mathcal F(u^2g)+15\mathcal F(ug)
=(-8u^3+30u^2-15u)g=-h_\infty.
\]

有限素点では \(1_{\mathbb Z_p}\) が Fourier 固有値+1を持つ。
従って actual adelic h は固有値−1である。
h(0)=0 と \(\int h=\mathcal Fh(0)=0\) はともに成立する。

norm は近似積分なしで検算できる。

\[
 \int_\mathbb R u^j e^{-2u}dx
 =\frac{(2j-1)!!}{4^j\sqrt2},
\quad
(8u^3-30u^2+15u)^2
=64u^6-480u^5+1140u^4-900u^3+225u^2.
\]

この和から \(\sqrt2\|h\|^2=585/32\)。独立な Python Fraction 演算でも同じ有理数を得た。
従って \(P_\mathcal F(h,h)=-585/(32\sqrt2)<0\)。
これは actual pole-free adelic test 上で候補 pairing の正性を反証する。
Weil pairing 自体の負方向や RH の反例へ読み替えてはいけない。

even subspace 上では \(\mathcal F^2=I\) かつ \(\mathcal F^*=\mathcal F\) なので
twisted pairing は Hermitian。全空間ではこの説明をそのまま使わない。
形式的な twisted adjoint \(\mathcal F\Theta^*\mathcal F=\Theta\) も正しい。

## 3. Mellin 係数と Tate normalization

実素点では \(d^\times x=dx/|x|\)、有限素点では

\[
 d^\times x_p=(1-p^{-1})^{-1}\frac{dx_p}{|x_p|_p},
 \qquad\operatorname{vol}^{\times}(\mathbb Z_p^\times)=1
\]

と明記すれば原文の Gamma／Euler 係数が完全に固定される。
加法自己双対測度だけで乗法 Haar の定数が自動的に指定されたとはしない。
この規約で有限局所積分は \((1-p^{-s})^{-1}\)。
実 Mellin 積分は v=s/2 として

\[
 Z_\infty(h_\infty,s)
 =\pi^{-s/2}\Gamma(s/2)
 [8v(v+1)(v+2)-30v(v+1)+15v]
 =\Gamma_\mathbb R(s)\frac{s(s-1)(2s-1)}2.
\]

Re s>1 では Euler 積との掛け算が直接正当化され、
\(Z(h,s)=(2s-1)\xi(s)\)。その後の等式は解析接続による。
追加多項式は test の Mellin 乗数であり、Euler/Gamma を改変して RH を判定する模型ではない。
極0,1の test による除去と、2s−1という追加因子を明示した scope は適切。

## 4. adjoint 候補の二つの gate

\(\Theta=\operatorname{diag}(3/4,1/4)\)、J を座標交換とすると
\(J\Theta J^{-1}=1-\Theta^*\)。標準内積は正定値だが両固有値は線上にない。
従って J を落とした \(\Theta^*=1-\Theta\) と同一視できない。

literal \(\Theta^{-1}=1-\Theta\) を共通 invariant domain で課せば
\(\Theta^2-\Theta+I=0\)。特に全固有値は \((1\pm i\sqrt3)/2\) の二値に限られる。
実際の ζ の全零点を高さ付き固有値として担う候補にはならない。
unbounded operator の積の定義域を指定した原文の限定は必要である。

なお \(\Theta^*\Theta=C\) を modulus 制約と呼ぶ場合、C は scalar \(cI\) と読む必要がある。
一般の未指定作用素 C なら固定した円周さえ定まらない。この解釈の明記だけで十分である。

## 5. 最終 scope

正 ambient pairing P は実構成、Fourier-twisted pairing の負方向は exact actual test。
ambient の正性・随伴から、算術 quotient の全零点・重複度保持はまだ出ない。
指定された weighted idèle L² に対する dense-radical no-go と、加法 L²(A) は
異なる Hilbert model であるという原文の区別を維持する。
他の全ての正幾何・別 topology の不可能性、RH、新規定理の主張へは拡大しない。
