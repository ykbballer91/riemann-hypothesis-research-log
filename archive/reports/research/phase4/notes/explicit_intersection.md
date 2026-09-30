**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase4/notes/explicit_intersection.md` · Original SHA-256: `ff1ea1f623077d95076a36af0beda441f26d1b960ede152f00e507f28fb3d144`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase IV — actual explicit formula の intersection 候補

2026-09-29。担当独立トラック。Phase III、canonical state、graph、charter は変更しない。新規性なし。本文で `KNOWN` とする文献定理は一次本文の範囲を確認して引用採用したもので、その全証明を独立に再証明したという意味ではない。

## Candidate generator

新しい作用素を仮設せず、**素数・Gamma・極の項で定義される一つの sesquilinear form** を候補とする。交点に相当する局所分布の和を \(I_{\rm ar}\)、cohomological trace に相当するものを \(B\) と分離する。両者の符号を混ぜない。

\(f,g\in\mathcal D=C_c^\infty(\mathbb R;\mathbb C)\)、\(g^*(t)=\overline{g(-t)}\)、\(h=f*g^*\) と置き、
\[
P(h)=\int_{\mathbb R}h(t)(e^{t/2}+e^{-t/2})dt,
\]
\[
I_{\rm fin}(h)=\sum_p\sum_{k\ge1}\frac{\log p}{p^{k/2}}
\{h(k\log p)+h(-k\log p)\},
\]
\[
I_\infty(h)=(\log(4\pi)+\gamma_E)h(0)
+\int_0^\infty
\frac{e^{t/2}\{h(t)+h(-t)-2e^{-t/2}h(0)\}}
{e^t-e^{-t}}\,dt,
\]
\[
I_{\rm ar}(f,g)=I_{\rm fin}(h)+I_\infty(h),
\qquad B(f,g)=P(h)-I_{\rm ar}(f,g). \tag{IV-I1}
\]
これは actual arithmetic からの定義であり、零点を入力していない。素数和は compact support により有限。最後の積分は原点で分子が \(O(t)\)、分母が \(2t+O(t^3)\)、無限遠で補正項が指数減衰するので絶対収束する。

正規化の一次根拠は Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, 表紙 2021-07-04、[著者 PDF](https://alainconnes.org/wp-content/uploads/Selecta.pdf) Appendix B、(148)–(154)、PDF p.47。\(a_h(u)=u^{-1/2}h(\log u)\) を代入した。\(I_\infty\) は Gamma の対数微分の厳密な局所項であり、任意に選べる補正ではない。

## Arithmetic input

Euler 積の対数微分から
\[
-\frac{\zeta'}{\zeta}(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks}
\quad(\Re s>1).
\]
したがって \(\Lambda(p^k)=\log p\)。\(k\) は同じ prime orbit の反復であり、係数を \(k\log p\) に置き換えない。\(\log\zeta\) の \(1/k\) が微分の \(k\) と相殺する。中心化による重みは \(p^{-k/2}\)。この \(\log p\) を、既に構成済みの代数的交点の整数 length と称することもできない。Arakelov の有限素点寄与との比較には、整数 length と \(\log\#k(v)\) を再現する実際の cycle map が要る。

一次照合は [CCM07](https://arxiv.org/pdf/math/0703392v1) §2.2 (2.32)–(2.34)、PDF pp.8–9、§7.1 (7.5)、pp.30–31 と上記 CC2021 (150)。principal value の正規化は additive character に依存し、都合のよい符号へ変更しない。

## Boundary data

\(A_\pm(f)=\int f(t)e^{\pm t/2}dt\) とすると、極項は厳密に
\[
P(f*g^*)=A_+(f)\overline{A_-(g)}
+A_-(f)\overline{A_+(g)}. \tag{IV-I2}
\]
乗法表示 \(a_f(u)=u^{-1/2}f(\log u)\) では degree \(d(a_f)=\widehat a_f(1)=A_+(f)\)、co-degree \(d'(a_f)=\widehat a_f(0)=A_-(f)\)。CCM07 Definition 7.1、(7.2)–(7.4)、PDF p.30 に対応する。複素 test の自己評価は \(2\Re(d\overline{d'})\) であり、実 correspondence の略記 \(2dd'\) をそのまま複素 test に用いない。

\(\mathcal D_0=\{f\in\mathcal D:A_+(f)=A_-(f)=0\}\) 上では \(B=-I_{\rm ar}\)。これは poles \(0,1\) を annihilate した primitive 候補で、Gamma 項の除去ではない。\(\mathcal D_0\) 上の全正値性も RH と同値：CC2021 Appendix C、Proposition C.1、PDF p.48、有限集合を \(\{0,1\}\) とする。pole subtraction によって RH より弱い問題へ変わったとは数えない。

## Evolution law

乗法畳み込みと \(a^\sharp(u)=u^{-1}\overline{a(u^{-1})}\) が correspondence の合成・双対に対応する。CCM07 §7.1 は scaling graph \(Z_a\) の積分 \(Z(F)=\int F(a)Z_a d^\times a\) を定義する。この分布的 correspondence には actual local fixed-point trace の根拠がある。従って単なる比喩として捨てない。

ただし CCM07 §2.1–2.3 の有限体証明で使うものは、滑らかな射影曲線の \(C\times C\) 上の divisor、principal divisor による線形同値、有効代表、交点数である。Riemann–Roch による有効性と (2.43) の交点数上界が (2.46) の正値性を与える（PDF pp.7–11）。数体側で名前を `intersection` としただけでは、この有効性定理・上界は移植されない。

CCM07 Lemma 7.3 は \(\mathcal V\) を加えて degree を任意に変えられることを証明する（PDF p.33）。同ページの直後には、対応する principal divisor の正しい概念を得ることが未完の課題として残る。degree adjustment と Riemann–Roch/effectivity は別の段階である。

## Why 1/2 appears

\(a_f=u^{-1/2}f(\log u)\) により \(\sharp\) が通常の反転共役 \(*\) に変わり、機能等式 \(s\leftrightarrow1-s\) の中心が \(1/2\) になる。これは正規化の確定であって純粋性の証明ではない。

`KNOWN` な明示公式は、\(F_f(z)=\int f(t)e^{izt}dt\)、\(z_\rho=(\rho-1/2)/i\) として
\[
B(f,g)=\sum_\rho m_\rho F_f(z_\rho)
\overline{F_g(\bar z_\rho)}. \tag{IV-I3}
\]
を与える。全非自明零点とその位数 \(m_\rho\) を保持する。\(\gamma=\Im\rho\) だけへの置換や、RH なしの絶対値平方化はしない。

## What forbids off-line states

現時点では独立な禁止定理を得ていない。自然な \(*\) は \(B\) を Hermitian にするが、正値性までは与えない。RH の下では (IV-I3) が平方和になり、逆は Weil criterion。CCM07 Proposition 7.2、PDF p.31 の transverse-intersection estimate も、定理の内容はその正値性との **同値性** であり、無条件の数体交点上界の証明ではない。

## Known prior art

| 一次資料 | 実際に使える定理と範囲 | この候補へ自動移植できないもの |
|---|---|---|
| [CCM07 v1](https://arxiv.org/pdf/math/0703392v1)、§§2,7 | 有限体の Riemann–Roch/交点による正値性の説明、数体の分布的 fixed-point interpretation、degree adjustment Lemma 7.3 | 数体に対する principal divisors・effectivity と交点上界。Proposition 7.2 は RH iff。 |
| [CC2021 著者版](https://alainconnes.org/wp-content/uploads/Selecta.pdf)、Appendices B,C | actual Gamma/prime/pole 規約、pole-annihilator 上でも RH iff。Theorem 1 は同論文の支持 \([2^{-1/2},2^{1/2}]\) と消失条件の下の archimedean lower bound | 局所の既知正値性を、全素数・全支持の正値性へ昇格させない。Introduction p.3 は Scaling Site の divisor intersection 理論の未完部分を明示する。 |
| A. Moriwaki, [*Hodge index theorem for arithmetic cycles of codimension one*, arXiv:alg-geom/9403011v4](https://arxiv.org/pdf/alg-geom/9403011v4)、Theorems A,B、PDF pp.1–2 | \(X\) regular/projective/flat over \(\mathrm{Spec}\mathbb Z\)、arithmetically ample Hermitian line bundle \(\bar H\) の下で、generic degree-zero arithmetic divisor \(x\) は \(\widehat\deg(x^2\widehat c_1(\bar H)^{d-1})\le0\)。Theorem B は equality criterion も与える。 | CCM の test class を、その scheme 上の cycle と Green current に送り、star・degree・全局所項を保つ写像は未構成。無限素点を単に Gamma と命名して仮定を満たしたことにはできない。 |

Moriwaki の arithmetical ampleness は相対 ample、無限素点の Kähler positivity、水平部分多様体の正の height を含む。この独立な正値性入力を取り除いて「形式的双対性」の定理として引用しない。

### Functional role checklist

| 役割 | 今回の候補での状態 |
|---|---|
| Arithmetic origin | Euler coefficients、指定 Gamma、両極から (IV-I1) を定義。 |
| Iterates | 同じ \(p\) の \(k\) 回反復、係数は \(\log p\)。 |
| Trace | (IV-I3) および CCM の算術的 cyclic quotient の trace は既知。 |
| Spectrum | 全零点・位数を trace に保持。正定値 Hilbert spectrum とは未同定。 |
| Determinant | 今回は新しい determinant theorem を供給しない。Euler/完成因子の一致と交点正値性を混同しない。 |
| Duality | canonical \(\sharp\)/\(*\) と Hermitian 性はある。 |
| Purity | 独立な正値性・Hodge comparison がなく、RH iff が残る。 |

## RH-equivalent hidden assumption?

**YES**：全 \(f\in\mathcal D\) の \(B(f,f)\ge0\)、または全 \(f\in\mathcal D_0\) の \(I_{\rm ar}(f,f)\le0\) を仮定すれば既知 RH criterion そのもの。符号を要求する前に、その形式を本物の Hodge-index 対象へ同定する必要がある。

### Topology / quotient / radical / multiplicity fidelity

compact test の式は通常の LF core で読む。CCM の商へ進む際は \(\mathbf S(C_{\mathbb Q})=\bigcap_{\beta\in\mathbb R}|\cdot|^\beta\mathcal S(C_{\mathbb Q})\) と restriction の像 \(\mathcal V\) を用いる。\(\mathcal V\) は一般に compact core の部分空間ではないので、\(\mathcal D/\mathcal V\) という未定義の商は取らない。Definition 4.10 の閉包は強い test-space topology であり、\(L^2\) 閉包ではない。

CCM Lemma 4.17、Remark 4.18、Proposition 6.4 により trace pairing は \(\mathcal V\) を radical に含む。ところが (6.12) により \(\mathcal V\) は \(\int|a(u)|^2u\,d^\times u\) の完備化で稠密。中心化するとこれは普通の \(\int|f(t)|^2dt\) である。compact-unit averaging 後の ζ sector でも成り立つ。従ってこの Hilbert norm の商は零となる。局所正性を bounded comparison だけでこの quotient へ渡す案は使えない。unbounded form や別の幾何的構成全体を否定するものではない。

Theorem 4.16 の trace class は \(h\in\mathbf S\) で積分した作用に対する nuclear-space の定理。未積分 flow の trace class、Hilbert completion における全 generalized eigenspaces の保持、零点の単純性は追加しない。特に trace の係数 \(m_\rho\) は正確でも、trace pairing の null quotient が全 jet を保つとはこの資料だけでは言えない。

## Synthetic counterexample status

### q=9：primitive にしても formal star は正でない

既存の合成模型を読み取り利用する：\(F=\begin{pmatrix}0&-9\\1&7\end{pmatrix}\)、\(F^2-7F+9I=0\)、\(F^\dagger=9F^{-1}=7I-F\)。この involution は有限体での正の Rosati involution と称しない。

\(A=F-3I\) なら \(A^\dagger A=-3I\)。さらに
\[
R(X)=(X-1)(X-9)(X-3),\quad R(1)=R(9)=0,
\]
なので、\(H^0,H^2\) 上の degree/co-degree 項まで消せる。\((F-I)(F-9I)=-3F\) から
\[
R(F)=-3F(F-3I),\qquad R(F)^\dagger R(F)=-243I,
\quad\operatorname{Tr}_{H^1}=-486.
\]
この計算は直接の行列代数による独立検算。正の閉点数・trace・duality を満たす既存模型でも、primitive star-trace の正性は従わない。**実際の曲線・算術 scheme・ζ を反証していない。**

### actual arithmetic：非零の負 mixed term

実関数 \(\psi\in C_c^\infty(-1,1)\)、\(\|\psi\|_2=1\)、\(a=\log3\) とし、
\(f_\epsilon(t)=\epsilon^{-1/2}\psi(t/\epsilon)\)、\(g_\epsilon(t)=f_\epsilon(t-a)\)。相関は \(-a\) 付近にだけ支持を持ち、そこで値 1。\(0<\epsilon\le1/64\) では素数項は 3 の一項だけで、\(h(0)=0\)。Gamma と poles を**削除せず**、その滑らかな残りを評価すると
\[
B(f_\epsilon,g_\epsilon)=-\frac{\log3}{\sqrt3}+r_\epsilon,
\qquad |r_\epsilon|\le7\epsilon.
\]
これは \(\|h\|_1\le2\epsilon\) と、\(v\in(\log2,\log4)\) 上の
\(\left|2\cosh(v/2)-e^{-v/2}/(1-e^{-2v})\right|<7/2\) から従う。従って mixed term は負かつ絶対値 \(>25/64\)。既存の解析的評価を (IV-I1) から再検算した。新規数値実験は不要。

旧支持の形式を外方向へ零延長して増分を作ると、二次元制限は \(\begin{pmatrix}0&b\\\bar b&d\end{pmatrix}\) となり determinant は \(-|b|^2<0\)。**棄却するのは canonical support increment が自動的に PSD という命題だけ。** 負 mixed term 自体は PSD の反例ではなく、全 \(B\) の負性も証明していない。

## Exact missing lemma

一つに絞ると、必要なのは actual test quotient の primitive classes から、独立に Hodge index が証明された arithmetic cycle/Green-current 空間への写像 \(J\) と、全 test に対する
\[
I_{\rm ar}(f,g)=\widehat\deg\big(J[f]\cdot\overline{J[g]}\cdot\bar H^{d-1}\big)
\]
という比較定理である。degree 条件、principal/radical の処理、Gamma の principal values、prime repetitions、topology と極限を保つ必要がある。これはまだ候補義務であり、構成済みとはしない。単に右辺を左辺で定義して Hodge index と呼ぶのは循環である。

## Decision

**Bounded kill：intersection という名称、canonical star、degree-zero 化から独立に正値性が出る、という経路を終了。** actual bilinear form とその全零点同定は保持できるが、今回の構成は既知 RH criterion の精密化までである。q9 は一般公理の不足、actual log3 は正の支持増分の失敗を、それぞれ限定された範囲で示す。新しい positive geometry/comparison theorem は得られていないため、主証明の成功や距離短縮として数えない。
