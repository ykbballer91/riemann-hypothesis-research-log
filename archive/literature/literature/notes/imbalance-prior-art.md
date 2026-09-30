**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/imbalance-prior-art.md` · Original SHA-256: `ecfd51d19fe02fd3e904df5541759ce975378f39b783098703aa4a094798c6a1`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定積・不均衡量の先行性と零点への接続監査

調査日: 2026-09-29（JST）。対象は数学的一次資料と、その標準公式からの直接計算に限定する。物理資料・定数は使用しない。網羅的な先行調査、新規性の主張、RH の新証明ではない。主経路は「全零点で不均衡量が消える」という未証明条件が RH そのものであるため終了する。

## 1. 確認した一次資料

| ID | 文献・固定版・locator | 使用箇所、仮定、公刊・確認区分 |
|---|---|---|
| I1 | P. Cerone–S. S. Dragomir, *Some convexity properties of Dirichlet series with positive terms*, [著者公開 2005-10-25 PDF](https://rgmia.org/papers/v8n4/IDSLCNew.pdf), §1 (1.5), §3 Proposition 4 と Remark 5 | 正係数 Dirichlet 級数の収束域での対数凸性、von Mangoldt 級数。RH 不要。公刊版は [Math. Nachr. 282 (2009), 964–975, DOI 10.1002/mana.200610783](https://onlinelibrary.wiley.com/doi/10.1002/mana.200610783)。定理番号は公開 PDF に固定。査読誌掲載 YES、全論文独立検証 NO。公開旧稿と公刊要旨で逆数の凹性の範囲が異なるため、その結果は使用しない。 |
| I2 | Frank Nielsen, *A note on some information-theoretic divergences between Zeta distributions*, [arXiv:2104.10548v3](https://arxiv.org/html/2104.10548v3), 2022-06-23, Table 1、Theorem 1 とその直前、Kullback–Leibler divergence の節 | 実パラメータ >1 の ζ 分布、累積関数 log ζ、Jensen／Bhattacharyya および reverse Bregman 表示。RH 不要。ここで固定したのはプレプリント、公刊査読状況は未確認。該当式を確認、全論文独立検証 NO。 |
| I3 | Takashi Nakamura, *A complete Riemann zeta distribution and the Riemann hypothesis*, [公刊電子再録 PDF, arXiv:1504.03438](https://arxiv.org/pdf/1504.03438), Bernoulli 21 (2015), 604–617 | (1.1)、Theorem 1.1、Lemma 2.1、Lemma 2.6 (2.6)。完成 ξ の対称性・正密度表示・零点対と四つ組の積。RH 不要の箇所だけ使用。査読誌掲載 YES、該当箇所読解、全論文独立検証 NO。原文 ξ は通常の 1/2 因子を付けない正規化。 |
| I4 | Masatoshi Suzuki, *Weil’s quadratic form via the screw function*, [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3), 2026-09-23, §1.1、§3 (3.1)、§2 (2.7) | Weil 形式の複素変数・共役の位置、素数項の符号。恒等式は RH 不要、全試験関数の正値性は RH 同値。プレプリント、査読公刊未確認、全論文独立検証 NO。 |

本監査は上記の原文公式と前件の確認であり、引用論文の全主張を認証するものではない。

## 2. 不均衡量は既知の対数凸性の差分

以下の代数計算は本ノート内で直接確認した。\(n>1\)、\(\delta=\sigma-1/2\) とすると

\[
 n^{-s}n^{-(1-s)}=n^{-1},\qquad
 E_n(\sigma)=(n^{-\sigma}-n^{-(1-\sigma)})^2
 =4n^{-1}\sinh^2(\delta\log n).
\]

実数 \(\sigma\) に対し \(E_n\ge0\)、等号は \(\delta=0\) に限る。この式自体は ζ の零点を使用しない。複素数 \(s=\sigma+it\) の差の平方は非負量ではない。絶対値の平方へ変更しても

\[
 |n^{-s}-n^{-(1-s)}|^2
 =n^{-2\sigma}+n^{-2(1-\sigma)}-2n^{-1}\cos(2t\log n)
\]

となり、臨界線上で恒等的に消える量ではなくなる。元の \(E_n\) は虚部 \(t\) を取り除いた振幅の不均衡である。

\(w_n=\Lambda(n)/\log n\)、\(x=1+u\)、\(h=2\delta\)、**\(u>2|\delta|\)** とする。Euler 積を絶対収束域で対数展開すると

\[
 F(x):=\log\zeta(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}\,n^{-x},
\]

\[
 A_u(\delta):=\sum_{n\ge2}w_n n^{-u}E_n(\sigma)
 =F(x+h)+F(x-h)-2F(x). \tag{A}
\]

すべての引数が 1 より大きいことが条件である。重みを \(\Lambda(n)\) にすれば、同じ式の \(F\) を \(G=-\zeta'/\zeta\) に置き換える。I1 (1.5) がこの Dirichlet 級数を記載している。

\[
 F''(x)=\sum_{n\ge2}\Lambda(n)\log n\,n^{-x}
 =\operatorname{Var}_{p_x}(\log n)>0,
 \qquad p_x(n)=\frac{n^{-x}}{\zeta(x)}.
\]

最後の等式は正規化級数の微分から従い、I2 Table 1 の Fisher information に一致する。I1 Proposition 4 の Hölder による対数凸性も同じ正値性の一般形である。新しい正値性原理とは扱わない。

## 3. Jensen／Bregman／Bhattacharyya との正確な一致

I2 Theorem 1 直前の ζ 分布の Bhattacharyya 係数を \(s_1=x-h,s_2=x+h,\alpha=1/2\) に特殊化すると

\[
 \sum_{n\ge1}\sqrt{p_{x-h}(n)p_{x+h}(n)}
 =\frac{\zeta(x)}{\sqrt{\zeta(x-h)\zeta(x+h)}}
 =e^{-A_u(\delta)/2}.
\]

したがって \(A_u/2\) は既知の Bhattacharyya 距離、かつ \(F=\log\zeta\) の中点 Jensen gap である。また

\[
 D_F(y,x)=F(y)-F(x)-F'(x)(y-x)
\]

という向きの Bregman divergence を定義すれば、直接代入により

\[
 A_u(\delta)=D_F(x+h,x)+D_F(x-h,x)
\]

となる。I2 は KL divergence が reverse Bregman divergence になることも述べる。この三者の同定はすべて **実パラメータ >1** の範囲であり、ζ 零点からの新しい制約ではない。

固定 \(u=1\) は \(0<\sigma<1\) の全域で使える。しかし

\[
 (\forall\rho:\zeta(\rho)=0,\ 0<\Re\rho<1)
 \quad A_1(\Re\rho-1/2)=0
 \quad\Longleftrightarrow\quad \mathrm{RH}.
\]

各零点の実部が 1/2 であることを等号条件で書き換えただけである。\(A_1\ge0\) から、零点における等号は従わない。

## 4. 完成 ξ と Weil 形式に移す際の障害

I3 (1.1) の関数等式は、零点集合を \(\rho,1-\rho,\bar\rho,1-\bar\rho\) の対称性で対応させる。I3 Lemma 2.6 (2.6) は臨界線上の共役対と、臨界線外の四つ組を**両方**含む収束積を記載する。四つ組の存在を許す無条件の積表示から、四つ組の因子を除去することはできない。\(n^{-s}n^{-(1-s)}\) の固定積を、各零点が反転の固定点であるという主張へ変える推論も成立しない。

I3 Theorem 1.1 と Lemma 2.1 から、完成関数については全実 \(\sigma\) で正規化された正密度表示があり、特に

\[
 |\xi(\sigma+it)|\le\xi(\sigma)\qquad(t\in\mathbb R)
\]

が RH を仮定せず従う。これは真に複素引数を含む既知の不等式だが、左辺が 0 になることを禁止せず、\(\sigma=1/2\) を強制しない。正の Laplace／Fourier 表示だけを十分条件にする経路は使用できない。

I4 (3.1) の約束では \(\Gamma=\{\gamma\in\mathbb C:\xi(1/2-i\gamma)=0\}\)、\(\widehat v(z)=\int v(x)e^{izx}dx\) であり、\(v\in C_c^\infty(\mathbb R)\) に対して零点側は

\[
 Q_W(v)=\sum_{\gamma\in\Gamma}m_\gamma
 \widehat v(\gamma)\overline{\widehat v(\bar\gamma)}.
\]

一般には \(\sum m_\gamma|\widehat v(\gamma)|^2\) ではない。全 \(\gamma\) を実数と置くのは RH を先取りする。素数側も正の \(E_n\) の総和ではなく、I4 §1.1／(2.7) の負符号付き平行移動・余弦項に極と無限素点の項が加わる。正の差分量を得ただけでは、全 Weil 形式を同定できない。全コンパクト試験関数に対する Weil 正値性は RH 同値であり、その全量化を省略できない。

## 5. 解析接続と監査の結論

\(\delta\ne0\) を固定したまま \(u\downarrow0\) とすると、途中の \(u=2|\delta|\) ですでに一方の引数が 1 に達する。正係数級数はそこで発散する。右辺だけを解析接続しても、非負級数・確率分布・Jensen gap の元の意味を引き継がない。特に \(-\zeta'/\zeta\) の解析接続を「同じ正エネルギー」と呼ぶことはできない。本ノートは root の別途の区間数値反例を再実行・再認証していない。

今回の先行性確認は、標準 Euler 公式、対数凸性、ζ 分布の情報幾何、完成 ξ の対称性、Weil の正確な共役規約で十分である。零点から (A) の等号を導く RH より弱い追加定理は得ていない。等号条件の再命名を新しい十分条件として主 graph に投入しない。零点非存在領域の網羅調査や未知恒等式の探索には拡張しない。
