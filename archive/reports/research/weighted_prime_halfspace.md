**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/weighted_prime_halfspace.md` · Original SHA-256: `06dafdd010fa75265f64c78b132fb24199accbb73d7ac3ab3189678a14f73b85`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Weighted Prime Half-space / Boolean Parity Correlation

2026-09-30。RH は **OPEN**。既存の全 track、state、proof graph は保持し、本トラックから自動 merge しない。

**判定：三つの主要試行を終了。今回の success ladder では Level 0。** 正確な構造・反例・既知定理の適用範囲を明確化したが、新しい算術固有 identity、新しい相殺機構、固定 power saving は得られていない。前トラックでの「exact bridge＝Level 1」と今回の基準は違うため、その水準を引き継がない。

最も明確になったのは、平方自由生成族の \(z=-1\) で **Selberg–Delange の全局所漸近係数が消える**ことと、**それでも Mertens 和全体が剰余として残る**ことの区別である。これは有限状態の exact bulk cancellation や低次元化を証明しない。以下は三系統の比較・直接計算・独立監査の記録である。

## 1. Actual threshold と正規化

\(X\ge2,\ P_X=\{p\le X\},\ m=\pi(X),\ L=\log X\) とする。Boolean vector \(\epsilon\) について
\[
W(\epsilon)=\sum_{p\le X}\epsilon_p\log p,\qquad
\chi(\epsilon)=(-1)^{\sum_p\epsilon_p},\qquad
f_X(\epsilon)=1_{W(\epsilon)\le L}.
\]
素因数分解の一意性により
\[
\boxed{M(X)=\sum_{\epsilon\in\{0,1\}^m}\chi(\epsilon)f_X(\epsilon)
             =2^m\widehat f_X([m]).}                         \tag{1}
\]
empty vector は \(n=1,\mu(1)=1\)。squarefree でない整数の係数は0。以下では常に counting scale に戻す。uniform cube 上で極端に小さい coefficient であること自体を成果と数えない。

前トラックの phase law だけではこの値を制御できないという反例を保持する。本トラックで対象を rectangular cutoff に置き換えず、state-count matching、random signs、人工的な norm へは移らない。

## 2. 優先 Track B：\(z=-1\) で何が消えるか

\[
S_z(X)=\sum_{n\le X}\mu(n)^2z^{\omega(n)},\qquad
\mathcal F(s,z)=\sum_n\mu(n)^2z^{\omega(n)}n^{-s}.
\]
\(\Re s>1\) で絶対収束する恒等式は
\[
\mathcal F(s,z)=\prod_p(1+zp^{-s})=\zeta(s)^zG(s,z),\quad
G(s,z)=\prod_p(1+zp^{-s})(1-p^{-s})^z.                       \tag{2}
\]
大素数の因子は \(1+O_R(p^{-2\Re s})\) なので、\(G\) は \(\Re s>1/2\) へ正則に拡張する。これは \(\zeta(s)^z\) の大域的一価性や、元の Euler 積の critical strip での収束を意味しない。

端点では因子ごとに厳密に
\[
\boxed{G(s,-1)=1,\qquad \mathcal F(s,-1)=1/\zeta(s),\qquad
S_{-1}(X)=M(X).}                                          \tag{3}
\]
ここで \(\sum z^{\omega(n)}\) の全整数版や \(z^{\Omega(n)}\) に変更しない。

### 2.1. 全局所係数の消失

\(Z(s)=(s-1)\zeta(s)\) は \(s=1\) の近くで正則・非零、\(Z(1)=1\)。同近傍で
\[
\frac{Z(s)^zG(s,z)}s=\sum_{j\ge0}h_j(z)(s-1)^j
\]
と展開すると、Selberg–Delange の局所漸近項は
\[
X(\log X)^{z-1}
\sum_{j=0}^J\frac{h_j(z)}{\Gamma(z-j)(\log X)^j}.            \tag{4}
\]
\(h_j(-1)\) は有限、\(1/\Gamma(-1-j)=0\) なので、**全ての有限次数の係数が厳密に0**となる。

これは既知である。de la Bretèche–Tenenbaum の原典 p.3、式(1.9)–(1.10)直後にも非正整数で全係数が消えることが明記されている。[Remarks on the Selberg–Delange method](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf)

### 2.2. 剰余は何を与え、何を与えないか

同原典 Theorem 1.2 に \(\varrho=-1,r=1,f=\mu\) を適用できる。素数上の差 \(g(p)=f(p)-\varrho\) は0、高素数冪係数も0。固定パラメータの誤差評価から、任意の固定 \(K>0\) に
\[
M(X)=O_K\!\left(\frac{X}{(\log X)^K}\right)                 \tag{5}
\]
という既知の評価を回収できる。定数の \(K\) 依存を無視して \(K=K(X)\) にしてはいけない。古典的な零点自由領域を含む強い定理からの既知の \(Xe^{-c\sqrt{\log X}}\) 型評価も、固定 \(\delta>0\) の \(X^{1-\delta}\) とは異なる。

特にこの原典の証明は、\(\zeta(s)^\varrho\) の係数 \(\tau_\varrho\) の既存漸近に依存する。\(\tau_{-1}=\mu\) なので、(5) をこの方法からの独立な新しい PNT 証明とは数えない。RH を仮定した循環ではないが、既知の難しい入力を再使用している。

Granville–Koukoulopoulos の Theorem 1 は有界な複素 \(z\) 集合で適用可能な**加法誤差**を与える。零になる主係数で割った相対誤差の一様性は別である。[Beyond the LSD method](https://dms.umontreal.ca/~koukoulo/documents/publications/LSD.pdf)

\(z=-1+\delta\) では
\[
\frac{G(1,-1+\delta)}{\Gamma(-1+\delta)}
   =-\delta+O(\delta^2).
\]
従って先頭局所項は
\[
\frac{X}{(\log X)^2}\,e^{\delta\log\log X}
                         [-\delta+O(\delta^2)].            \tag{6}
\]
縮む \(\delta\) ではこの主項が加法誤差以下になり得る。端点に近づく main term の見かけだけを外挿して \(M(X)\) を評価できない。

### 2.3. 「bulk 消失」の正確な意味

\(1/\zeta(s)=(s-1)/Z(s)\) は \(s=1\) で正則な零点を持つ。その局所 Hankel 主項が消える一方、他の \(\zeta\) 零点での \(1/\zeta\) の極は残る。局所情報は大域的な Perron 輪郭や remainder を制御しない。

このことを synthetic Dirichlet series でも検査した。固定 \(\beta\in(1/2,1)\) に対し
\[
D_\beta(s)=\zeta(s+1-\beta)
  -\frac{\zeta(2-\beta)}{\zeta(2)}\zeta(s+1)
\]
は \(s=1\) で正則で値0だが、その係数和は
\[
\frac{X^\beta}{\beta}
 -\frac{\zeta(2-\beta)}{\zeta(2)}\log X+O_\beta(1).
\]
これは actual Euler factors を保持しないので RH の反例・候補理論には採用しない。「局所的な零点だけで平方根 remainder が出る」という推論だけを反証する。

したがって「RH は bulk main term が消えた後の remainder の問題」と読むことは可能だが、**その remainder が低次元である、別の易しい既知量に支配される、という新定理は得ていない**。

### 2.4. \(\omega(n)\) の分布と parity 周波数

標準化された Erdős–Kac の CLT の固定周波数と、元の \((-1)^{\omega(n)}\) の周波数 \(\pi\) は異なる。後者は標準化座標で \(\pi\sqrt{\log\log X}\) へ発散する。局所個数を近似しても、交代和の誤差を別途制御しなければならない。

ただし全ての強化分布定理が \(\pi\) を扱えないわけではない。Kowalski–Nikeghbali §4 の mod-Poisson theorem は全整数版でこの周波数を扱う。対象が平方自由版の \(M(X)\) と違うこと、精度が固定 power saving を自動的に与えないことを分けた。[Mod-Poisson convergence](https://people.math.ethz.ch/~kowalski/mod-poisson.pdf)

詳細な定理の仮定・版・remainder は [Track B note](weighted_prime_halfspace/notes/selberg_delange_endpoint.md)。

## 3. Track A：有限差分・境界の構造

\(\tau_a f(u)=f(u-a),\ J(u)=1_{u\ge0}\) とすれば
\[
F_m(L)=\left[\prod_{p\le X}(I-\tau_{\log p})J\right](L).
                                                               \tag{7}
\]
\(H_L(u)=1_{u\le L}\) を0で評価する別表記では \(\tau_{-\log p}\) が必要。元の符号のまま \(\tau_{+\log p}\) を \(H_L(0)\) に使うと目的の subset sum にならない。

順序によらず
\[
F_k(L)=F_{k-1}(L)-F_{k-1}(L-\log p_k).                       \tag{8}
\]
block も全 subset shifts を残した signed convolution となる。これは exact self-similarity だが、contraction ではない。

正の重み \(a_1,\ldots,a_m\) について
\[
\prod_j(I-\tau_{a_j})f(L)
=\int_0^{a_1}\cdots\int_0^{a_m}
          f^{(m)}(L-u_1-\cdots-u_m)\,du.                    \tag{9}
\]
箱関数の畳み込み \(B=\mathbf1_{[0,a_1]}*\cdots*\mathbf1_{[0,a_m]}\) は非負だが、目的量は分布として \(D^{m-1}B\)。非負 spline 自体ではない。smooth step を幅 \(h\) で使う直接評価は
\[
\left(\prod_j a_j\right)h^{-m}\|\psi^{(m-1)}\|_\infty
\]
を支払い、\(m=\pi(X)\) と共に微分次数が増大する。

\(F_m\) の support は \([0,\sum a_j]\) に含まれるだけ。actual prime logs では右端 \(\vartheta(X)\sim X\) に対し readout は \(\log X\) であり、「狭い境界帯」ではない。distinct subset sums により全変動は正確に \(2^m\)。標準 \(L^\infty\) operator norm も \(2^m\) で、一般の収縮を与えない。

### 3.1. 一般 threshold の sharp bound と失敗例

任意の downset \(D\subset\{0,1\}^m\) に対し
\[
\boxed{\left|\sum_{\epsilon\in D}(-1)^{|\epsilon|}\right|
\le {m-1\choose\lfloor(m-1)/2\rfloor}.}                    \tag{10}
\]
normalized layer densities の単調性から直接証明し、既知の convex-hull theorem と照合した。equal-weight threshold で等号。normalized coefficient では \(O(m^{-1/2})\) だが、counting scale では \(2^m/\sqrt m\) である。\(m=\pi(X)\) への代入は自明界 \(O(X)\) さえ改善しない。

equal weights では
\[
\sum_{k=0}^r(-1)^k{m\choose k}=(-1)^r{m-1\choose r}
\quad(0\le r<m).
\]
threshold の margin を保つ任意小の rationally independent perturbation でもこの値は変わらない。distinct subset sums や generic irrationality 自体は利得にならない。

Kozlov の原論文 Theorem 4.1 と §5 を確認した。[Convex Hulls of f- and β-Vectors](https://doi.org/10.1007/PL00009326)。noise、influence、Littlewood–Offord、hypercontractivity は一般 bound として監査し、counting normalization、unsigned shell、\(\rho^{-m}\) の noise 復元費用を保持した。martingale/permutation averaging も最終的に同じ parity coefficient を返し、追加の算術相関は与えない。

### 3.2. 大素数 block と共有 parent

\(Y=\sqrt X\)、\(A_{\le Y}(X)=\sum_{n\le X,\ P^+(n)\le Y}\mu(n)\) とすると
\[
\boxed{M(X)=A_{\le Y}(X)-\sum_{Y<p\le X}M(X/p)
=A_{\le Y}(X)-\sum_{r\le X/Y}\mu(r)[\pi(X/r)-\pi(Y)].}       \tag{11}
\]
平方根は一つの \(n\le X\) が \(Y\) より大きい素因数を高々一つ持つことから現れる。共有 parent の multiplicity を \(\pi(X/r)-\pi(Y)\) のまま残した。PNT でこの係数の平均密度を近似しても、\(\mu(r)\) との signed correlation は未評価。これは既知の prime-factor decomposition の再構成であり、新 identity とは数えない。

詳細と sharp-bound proof は [Track A note](weighted_prime_halfspace/notes/finite_difference_boolean.md)。

## 4. Track C：境界に適応した傾斜測度

有限 \(P_X\) 上で任意の実 \(\sigma\) に
\[
Z_\sigma=\prod_{p\le X}(1+p^{-\sigma}),\quad
\mathbb P_\sigma(S)=Z_\sigma^{-1}e^{-\sigma W(S)}
\]
と置く。独立 Bernoulli の選択確率は \(1/(1+p^\sigma)\)。exact reconstruction は
\[
\boxed{M(X)=Z_\sigma\,
\mathbb E_\sigma[\chi e^{\sigma W}1_{W\le L}].}             \tag{12}
\]
積で計算できる \(\mathbb E_\sigma\chi=\prod(1-p^{-\sigma})/(1+p^{-\sigma})\) は、この readout correlation と異なる。

\(G_\sigma=e^{\sigma W}1_{W\le L}\)、\(N_X=\sum_{n\le X}\mu(n)^2\) とすれば
\[
M(X)=N_X\,\mathbb E_\sigma\chi
      +Z_\sigma\operatorname{Cov}_\sigma(\chi,G_\sigma).     \tag{13}
\]
\(X=3,\sigma=1\) の exact countertest は
\[
Z=2,\quad \mathbb E\chi=1/6,\quad
\mathbb EG=3/2,\quad \mathbb E(\chi G)=-1/2.
\]
よって \(M(3)=-1=1/2-3/2\)。相関を捨てると符号まで誤る。

### 4.1. Saddle の存在と非Gaussianな揺らぎ

平均 \(\sum_{p\le X}\log p/(1+p^\sigma)\) は \(\sigma\) に関して厳密に減少。その値を \(L\) に合わせる有限 saddle が存在する条件は \(0<L<\vartheta(X)\)、positive saddle の条件は \(L<\vartheta(X)/2\)。大きい \(X\) では PNT により成立するが、\(X=2\) には有限解がなく、\(X=3\) の解は負である。

PNT と部分和分から \(\sigma=1\) に
\[
\mathbb EW\sim L,\quad \operatorname{Var}W\sim L^2/2,\quad
\mathbb E e^{-tW/L}\longrightarrow
\exp\left(\int_0^1\frac{e^{-tu}-1}{u}\,du\right).             \tag{14}
\]
この極限は非Gaussian。saddle も \((\sigma_X-1)L\to0\) なので同じ極限が残る。単に平均を境界へ合わせても、相対的に狭い正規分布へ集中するわけではない。これらは既知の確率的構造と整合する直接導出であり、新規性や RH への利得を主張しない。

全素数の probability interpretation では \(\sigma>1\) が別途必要。その域で
\[
Z_\sigma^{(\infty)}=\zeta(\sigma)/\zeta(2\sigma),\qquad
\mathbb E_\sigma\chi=\zeta(2\sigma)/\zeta(\sigma)^2.
\]
\(\sigma\le1\) では almost surely 無限個の素数を選び \(W=\infty\) となるので、通常の finite parity variable は定義されない。有限積の値が0に近づく場合も、それを \(M(X)=0\) へ転用できない。有限 \(P_X\) の (12) 自体は問題なく、残る障害は covariance の評価である。

### 4.2. Sieve parity barrier の限定監査

非負列 \(\mu(n)^2+\mu(n)\) と \(\mu(n)^2-\mu(n)\) は反対の squarefree parity に支えられるが、各固定 divisor \(d\) に対して同じ leading density を持つ。符号付き誤差を捨てた local density だけでは parity を決定できない。全ての正確な divisor data は別であり、それを与えれば逆変換できる。

有限差分の積は inclusion–exclusion の alternating product と同じ代数を持つ。しかし本対象は cutoff を選んだ squarefree divisor weight であり、通常の sifted count の \(\lfloor X/d\rfloor\) 重みとは同一ではない。どちらも exact expansion を知ることと、残る signed sum を評価することは別である。

Tao の原著者解説を確認し、divisor-sum の誤差を明記した補題として保存した。広い意味の parity barrier には informal な範囲があるため「あらゆる篩手法が不可能」とは主張しない。[2007 parity problem](https://terrytao.wordpress.com/2007/06/05/open-question-the-parity-problem-in-sieve-theory/)、[2015 notes §5](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/comment-page-1/)

詳細は [Track C note](weighted_prime_halfspace/notes/tilt_and_sieve_parity.md)。

## 5. Ordered squarefree readout と有限実験

ordered signed process は \(\sum_{n\ {\rm sf}}\mu(n)\delta_{\log n}\)。整数性は \(|\log a-\log b|\ge1/\max(a,b)\) を与えるが、隣接符号は強制しない。例えば squarefree な 2,3 は共に負、13,14 は負・正、14,15 は共に正。spacing だけから deterministic alternation は出ない。反証にはこの有限例で十分で、random sign model は使わない。

[実験コード](../../../artifacts/research/weighted_prime_halfspace/experiments/check_halfspace.py) と [結果](../../../artifacts/research/weighted_prime_halfspace/experiments/results.json) を保存した。

- actual prime recursion：\(X=30,100,1000\)。差分 recurrence と Möbius sieve の一致。
- equal weights：次元1〜20の全 rank cutoff を整数で検算。全 downsets の総当たりは次元1〜4。
- 最初の6素数の全720順序：\(X=100\) の最終値は4で不変、途中の最大振幅は順序により4または5。これは6素数 subsystem で、actual \(M(100)=1\) とは区別。
- 各素数の pivotal shell の符号付き和、\(X=30,100,1000,10000\) の大素数分解と parent multiplicity。
- 7種類の重み：actual prime logs、equal、等間隔、乱数サンプル、微小摂動、nonprime logs、有理関係を持つ重み。同一総重み・同一 cutoff で比較した。乱数は診断用だけ。
- \(\omega\) 別個数、\(z=-1\) 近傍の exact rational polynomial values、有限 Gibbs identity、saddle の数値診断。

例として \(S_z(100)=1+25z+30z^2+5z^3\) なので \(S_{-1}(100)=1\)。全局所漸近係数が0でも有限の値は0にならない。近似 equal-weight の次元12・rank5では、rationally independent な重みでも discrepancy \(-462\) を保持する。

全 assertion は通過。有限計算・saddle の数値値は一般定理の証明や growth fit に使用しない。証明は上記の直接恒等式、反例、原典の適用条件による。

## 6. Strategy review

| Track | 保存した構造 | 終了理由 |
|---|---|---|
| A finite difference / Boolean | 正しい符号、spline derivative、sharp downset bound、actual block recursion | 一般 bound は counting scale で改善せず、derivative/noise の費用を打ち消す算術内容なし |
| B Selberg–Delange endpoint | \(G(s,-1)=1\)、全局所係数消失、端点を含む加法誤差 | Mertens 全体が既知の remainder に残り、独立の新評価なし |
| C tilt / saddle / readout | exact Gibbs・covariance、saddle 条件、非Gaussian極限、限定 parity barrier | covariance を評価できず、unsigned 分布・local densities では不足 |

今回新しく固定 \(\theta<1\) の \(M(X)=O(X^\theta)\) を得ていないため、Dyadic Reduction へ新しい exponent bridge は作成しない。既存の \(2^{(\theta-1/2)n}\) の条件付き関係も変更しない。

第4候補へ移らず終了する。再開には、actual arithmetic cutoff の signed correlation または \(z=-1\) の remainder に対する、既知算術からの具体的な新評価が必要。その評価自体を仮定することは再開条件を満たさない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/weighted_prime_halfspace/experiments/check_halfspace.py`](../../../artifacts/research/weighted_prime_halfspace/experiments/check_halfspace.py)
- [`research/weighted_prime_halfspace/experiments/results.json`](../../../artifacts/research/weighted_prime_halfspace/experiments/results.json)
- [`research/weighted_prime_halfspace/notes/finite_difference_boolean.md`](weighted_prime_halfspace/notes/finite_difference_boolean.md)
- [`research/weighted_prime_halfspace/notes/selberg_delange_endpoint.md`](weighted_prime_halfspace/notes/selberg_delange_endpoint.md)
- [`research/weighted_prime_halfspace/notes/tilt_and_sieve_parity.md`](weighted_prime_halfspace/notes/tilt_and_sieve_parity.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_halfspace.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/results.json` — SOURCE REFERENCE NOT INCLUDED
