**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/strategy_reset/notes/correlations_and_short_intervals.md` · Original SHA-256: `33a8719df23d5ad9753df8d4b342e45eb5761f1cd0094a5f75c9461195fa7613`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Candidate C: Möbius 短区間・相関を使うための条件監査

2026-09-30。STRATEGY RESET の inventory / audit のみ。旧ファイルは変更しない。一次資料の定理文・適用範囲を確認した限定調査であり、列挙した論文の全証明を独立検証したとは記録しない。新しい RH 証明経路・新規性・網羅的な最良記録を主張しない。

**判定:** 短区間と相関には actual \(\mu\) に適用できる強い既知定理がある。しかし以下で確認した定理から、固定 Gaussian の全 \(u\) subexponential bound は得られない。新たに正当化できた大域算術入力は **0 件**。平均評価から点ごとの評価への移行が原理的に不可能という意味ではない。

## C1. 比較する対象と量化

\[
 R(u)=\sum_{n\ge1}\mu(n)e^{-(u-\log n)^2},\qquad
 A(u)=e^{-u/2}R(u),\qquad x=e^u.
 \tag{C1.1}
\]

目標は \(\forall\epsilon>0,\ |A(\log x)|\ll_\epsilon x^\epsilon\) が**すべての十分大きい \(x\)** で成り立つこと。既存 [Gaussian ノート](../../global_remainder/notes/gaussian_global_decomposition.md) G6 が確認した通り、これは RH 同値である。今回同値性を新しい入力として数えない。

以下の量化は別物である。

- 全区間: 各 \(x\) について \(\sum_{x<n\le x+H}\mu(n)\) を評価する。
- ほとんどすべての短区間: \(x\in[X,2X]\) の例外集合を許す。
- shift 平均: \(\sum_{h\le H}|\sum_{n\le X}\mu(n)\mu(n+h)|\) を評価する。
- 対数平均: \(\sum_{X/\omega<n\le X}\mu(n)\mu(n+h)/n\) を評価する。
- ほとんどすべての scale: natural average は評価するが、\(X\) の対数密度零の例外を許す。

小さい例外密度は例外の不存在ではなく、qualitative \(o(1)\) は平方根規模の誤差ではない。

## C2. 一次資料で確認した範囲

### S1. MR: 短区間は arbitrarily slowly growing でも、almost all

Matomäki–Radziwiłł, *Multiplicative functions in short intervals*, Annals of Mathematics 183 (2016), 1015–1056。確認版 [arXiv:1501.04585v4](https://arxiv.org/pdf/1501.04585v4), 2017-10-15、Theorem 1, pp1–2。

実数値 multiplicative \(f:\mathbb N\to[-1,1]\)、\(2\le h\le X\) に対し、短平均と \([X,2X]\) の長平均の差を \(\delta+C\log\log h/\log h\) で、明示的例外集合の外で抑える。例えば本文の \(\delta=(\log h)^{-1/200}\) の選択では、誤差 \(O((\log h)^{-1/200})\)、例外数 \(O(X(\log h)^{-1/100})\)。\(\mu\) と長平均の PNT を用いれば \(h\to\infty\) 任意に遅くても almost-all cancellation。査読刊行済み。これは \(\mu\) を completely multiplicative と仮定しない。

### S2. MR II: 例外集合には power saving もある

同著者、*Multiplicative functions in short intervals II*, [arXiv:2007.04290v1](https://arxiv.org/pdf/2007.04290v1), 2020-07-08、Corollary 1.1, p3、Theorem 1.7, p7。

Corollary 1.1 の \(\mathcal N=\mathbb N\) への特殊化では、実 multiplicative \(|f|\le1\)、\(2\le h\le X\)、\(0<\delta<1/1000\) で短平均と長平均の差が \(\delta\) 以上となる整数 \(x\) は \(O(Xh^{-\delta^\kappa})\)、ある絶対 \(\kappa>0\)。さらに明示的な改善も記載される。今回の刊行確認は arXiv 指定版まで。

従って「既知の例外評価はすべて対数冪だけ」とは言わない。ただし節約は例外数に対するもので、全区間の平方根 cancellation ではない。例えば \(\delta=X^{-1/2+\epsilon}\) にすると \(\delta^\kappa\log h\to0\) で、この bound は例外を除去しない。Theorem 1.7 でも誤差閾値と例外数の交換条件を落としてはいけない。

### S3. 全短区間で確認した actual \(\mu\) の評価

Matomäki–Teräväinen, *On the Möbius function in all short intervals*, JEMS 25 (2023), 1207–1225、[刊行 PDF](https://ems.press/content/serial-article-files/32826)、DOI [10.4171/JEMS/1205](https://doi.org/10.4171/JEMS/1205)、Theorem 1.1, p1208, (1.2)。

固定 \(\theta>0.55,\eta>0\)、十分大きい \(x\)、\(H\ge x^\theta\) で
\[
 \sum_{x<n\le x+H}\mu(n)
   =O_{\theta,\eta}\!\left(H(\log x)^{-1/3+\eta}\right).
 \tag{C2.1}
\]
これは全 \(x\) の結果であるが、\(H\) に対する対数の節約を \(x^{1/2+\epsilon}\) に置き換えられない。Theorem 1.5 の Fourier twist には別に \(\theta>3/5\) が要る。査読刊行済み。ここではこの primary の有効範囲を固定し、2026年時点の全論文について最良指数を証明したとは主張しない。

### S4. MRT: unweighted correlations の shift 平均

Matomäki–Radziwiłł–Tao, *An averaged form of Chowla's conjecture*, Algebra & Number Theory 9 (2015), 2167–2196、[arXiv:1503.05121v3](https://arxiv.org/pdf/1503.05121v3)、Theorem 1.1, p2, (1.3) と p6 の \(\lambda\to\mu\) 明記。

固定 \(k\)、\(10\le H\le X\) について
\[
 \sum_{1\le h_2,\ldots,h_k\le H}
 \left|\sum_{n\le X}\mu(n)\mu(n+h_2)\cdots\mu(n+h_k)\right|
 \ll_k \left(\frac{\log\log H}{\log H}
       +(\log X)^{-1/3000}\right)H^{k-1}X.
 \tag{C2.2}
\]
\(H\to\infty\) なら平均で \(o(1)\)。固定したすべての \(h\) の主張ではなく、\(X\) とともに増える任意の重み・最大部分和も自動ではない。Theorem 1.6 はより一般の multiplicative input と nonpretentiousness を明記している。査読刊行済み。

### S5. Tao: 固定 affine forms に対する log two-point correlation

Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum of Mathematics, Pi 4 (2016), e8、[arXiv:1509.05422v4](https://arxiv.org/pdf/1509.05422v4)、Theorem 1.3 / Corollary 1.5, pp5–6。

固定 \(a_i\in\mathbb N,b_i\in\mathbb Z\)、\(a_1b_2-a_2b_1\ne0\)、\(1\le\omega(X)\le X,\omega(X)\to\infty\) で actual \(\mu\) には
\[
 \sum_{X/\omega<n\le X}
 \frac{\mu(a_1n+b_1)\mu(a_2n+b_2)}n=o(\log\omega).
 \tag{C2.3}
\]
Theorem 1.3 の一般版は、全 \(\operatorname{cond}\chi\le B,\ |t|\le BX\) で nonpretentious distance の下界 \(B\) を要求し、閾値 \(B\) は affine forms と許容誤差に依存する。p6 は \(\mu\) 適用を明記。査読刊行済み。固定 \(\omega=2\) をこの漸近へ代入したり、\(h\asymp X\) までの一様性を読み足したりしない。

### S6. unweighted へ移せても exceptional scales は残る

Tao–Teräväinen, *The structure of correlations of multiplicative functions at almost all scales, with applications to the Chowla and Elliott conjectures*, Algebra & Number Theory 13 (2019), 2103–2150、[arXiv:1809.02518v2](https://arxiv.org/pdf/1809.02518v2)、Corollaries 1.13–1.14, pp8–9。

固定 distinct shifts の二点相関は \(\sum_{n\le X}\mu(n+h_1)\mu(n+h_2)=o(X)\) が対数密度零の例外 scale 集合の外で成立。Corollary 1.13(i) は固定許容誤差について logarithmic Banach density zero、(ii) は共通の logarithmic-density-zero exceptional set を与える。Corollary 1.14 は \(k\) が奇数または \(2\) の場合を扱い、\(\lambda\) を一部または全部 \(\mu\) に置換できる。査読刊行済み。全 scale / 平方根誤差への昇格ではない。

### S7. 2026版の higher uniformity も exceptional interval を許す

Matomäki–Radziwiłł–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, [arXiv:2411.05770v2](https://arxiv.org/pdf/2411.05770v2), 2026-01-23、Theorem 1.1(i),(iv), pp3–4。[刊行版 DOI](https://doi.org/10.1007/s00222-026-01408-6), Inventiones Mathematicae 244 (2026), 967–1091。

固定度数・次元・complexity・Lipschitz norm の nilsequence に対する maximal correlation を扱う。star は区間内 arithmetic progression に関する supremum。

- (i) \(X^{1/3+\epsilon}\le H\le X^{1-\epsilon}\): \(\mu\) 相関は \(H\log^{-B}X\) 以下、例外 measure は \(O_{B,\epsilon,\mathrm{complexity}}(X\log^{-B}X)\)、任意固定 \(B>0\)。
- (iv) \(X^\epsilon\le H\le X^{1-\epsilon}\)、さらに \(F\) が 1-bounded: 相関は任意固定 \(\eta H\) 以下、例外 measure は \(O_{B,\epsilon,\eta,\mathrm{complexity}}(X\log^{-B}X)\)。

(iii),(v) や Theorem 1.8 の divisor-function power saving を \(\mu\) に移さない。査読刊行済み。固定 \(B,\eta\) を無断で \(X\)-dependent に選ばない。

### S8. 近年の quantitative correlation: 節約は log、例外も残る

Pilatte, *Improved bounds for the two-point logarithmic Chowla conjecture*, [arXiv:2310.19357v3](https://arxiv.org/pdf/2310.19357v3), 2026-08-25、Theorem 1.1 p3:
\(\sum_{n\le X}\lambda(n)\lambda(n+1)/n\ll(\log X)^{1-c}\)。
Remark 2.8, p10 は unweighted two-point correlation の絶対値を scale で対数平均した節約を与える。**この定理文は \(\lambda\)** であり、p3 の「より一般へ拡張できるはず」を \(\mu\) 定理に昇格しない。今回確認した刊行状況は arXiv 版まで。

Tao–Teräväinen, *Quantitative correlations and some problems on prime factors of consecutive integers*, [arXiv:2512.01739v2](https://arxiv.org/html/2512.01739v2#S3), 2026-04-25、Theorem 3.1(ii), (3.3)–(3.4) は 1-bounded **multiplicative** \(g_1,g_2\) を許す。記号
\[
 \mathcal M(g;Y,Q)=\inf_{\substack{|t|\le Y\\q\le Q,\ \chi\bmod q}}
       \sum_{p\le Y}\frac{1-\Re(g(p)\overline{\chi(p)}p^{-it})}{p}
\]
を使い、\(1\le\mathcal L\le\log X\) と
\(\exp\mathcal M(g_1;X^2,\log^{1/125}X)\gg\mathcal L\) を仮定する。ある小さい絶対 \(c>0\) について、共通例外 \(\mathcal E\subset[\sqrt X,X]\) の外で
\[
 \frac{W}{N}\sum_{\substack{N<n\le2N\\n\equiv b\pmod W}}
     g_1(n+h_1)g_2(n+h_2)\ll\mathcal L^{-c},
 \quad
 \frac1{\log X}\int_{\mathcal E}\frac{dt}{t}\ll\mathcal L^{-c},
 \tag{C2.4}
\]
\(W\le\mathcal L^c,\ b,h_i=O(\mathcal L^c),h_1\ne h_2\)。
\(\mu(p)=\lambda(p)=-1\) のため prime distance は同一で、既知の nonpretentious lower bound を使って actual \(\mu\) に適用可能。ただし affine-form の \(\lambda\) 用 completely-multiplicative identity を \(\mu\) に転用しない。これは polylogarithmic shifts・例外 scale つき対数節約であり、必要な \(h\asymp X\)、全 scale、平方根規模を同時には供給しない。全証明の再監査・査読状況の確定は今回行わない。

以上は対象に近い定理の inventory である。検索で現れた他の2026年プレプリントを未読のまま採用せず、これ以上の文献巡回はしない。

## C3. 固定 Gaussian の実際の窓と尾

\(|\log(n/x)|\le B\) の窓は
\[
 xe^{-B}\le n\le xe^B,\qquad H_B=2x\sinh B.
\]
固定 \(B>0\) では \(H_B\asymp_B x\)。幅 1 の log Gaussian は additive short interval \(H=o(x)\) ではない。

ただし Gaussian は compact support でもない。\(B\ge1\) で unimodal sum–integral bound を左右の尾に使うと
\[
 \sum_{|\log(n/x)|>B}e^{-\log^2(n/x)}
 \le x\int_{|v|>B}e^{-v^2+v}\,dv+2e^{-B^2}
 \ll \frac{x e^{-(B-1/2)^2}}{B-1/2}+2e^{-B^2}.
 \tag{C3.1}
\]
従って normalized absolute tail は概ね
\(x^{1/2}e^{-(B-1/2)^2}/B\)。
固定 \(B\) で尾を目標 \(x^\epsilon\) 以下にできるとは言えない。固定 \(0<\epsilon<1/2\) の目標を絶対値だけで処理するなら \(B\) を \(\sqrt{\log x}\) 程度へ増やす必要があり、相関定理の範囲・定数の一様性を再確認しなければならない。

窓を狭めると対象そのものが変わる。固定 \(\sigma>0\) の
\(\phi_\sigma(v)=e^{-v^2/\sigma^2}\) は Mellin multiplier
\(\sqrt\pi\sigma e^{\sigma^2s^2/4}\ne0\) を持ち、同じ fixed-kernel criterion を満たす。一方、第一原理で
\[
 \sum_{n\ge1}|\phi_\sigma(\log(n/x))|
 \le 2+\sqrt\pi\,\sigma x e^{\sigma^2/4}.              \tag{C3.2}
\]
\(\sigma(x)=x^{-1/2}\) なら normalized sum は **全係数を \(+1\)** としても bounded である。これは narrowing による標本数の減少で、算術 cancellation ではない。実際の \(\mu\) の反例を作ったのではなく「可変幅で bounded だから元の RH criterion」という推論を排除する。可変幅は convolution と stationary bilateral Laplace factorization を壊すため、固定 \(A\) へ bound を戻すには別の誤差評価が必要。

## C4. compact-window weighted autocorrelation の exact formula

任意の bounded measurable compactly supported 実関数 \(W\) と実 \(v\) に対し
\[
 \mathcal C_W(v)=
 \int_\mathbb R W(u)A(u+v/2)A(u-v/2)\,du .
 \tag{C4.1}
\]
各 \(\mu\) 和と全導関数は compact \(u\)-sets で絶対・一様収束する。従って二重和との交換は絶対収束によって正当化される。例えば \(c>1\) を固定し、各 Gaussian を \(C_{W,v,c}n^{-c}\) で優越すれば足りる。

\[
 r_{mn}=\tfrac12\log(mn),\quad d_{mn}=\log(n/m),\quad
 H_W(r)=\int W(u)e^{-2(u-r+1/4)^2}\,du
\]
と置くと平方完成だけで
\[
 \boxed{\mathcal C_W(v)=e^{1/8}
  \sum_{m,n\ge1}\frac{\mu(m)\mu(n)}{\sqrt{mn}}\,
    e^{-(d_{mn}-v)^2/2}H_W(r_{mn}).}                 \tag{C4.2}
\]
これは任意の幅 \(\eta>0\) の
\(W(u)=W_0((u-u_0)/\eta)\) にも同じ規約で成立する。
\(W\ge0,v=0\) では \(\mathcal C_W(0)\ge0\) だが、\(\mu(m)\mu(n)\) の off-diagonal cancellation の大きさを証明したことにはならない。\(W\) が非定常なら \(\mathcal C_W(v)\) 自体を stationary positive-definite autocorrelation と呼ばない。

additive shift \(n=m+h\) を導入すれば
\[
 d_{m,m+h}=\log(1+h/m),\qquad
 r_{m,m+h}=\log m+\tfrac12\log(1+h/m).                \tag{C4.3}
\]
固定 log-ratio と固定 additive shift は同じではない。\(m\asymp x\) で \(d\asymp1\) は通常 \(h\asymp x\)。核は \(m,h\) の双方に依存する。固定 \(h\) の Chowla 定理や polylogarithmic shifts の定理を、全二重和へ無条件に移せない。shift 平均の定理を使う場合も、対応する重みへの partial summation・可変 upper limits・全 tails の評価が別に必要になる。

導関数 energy も同じ方法で正確に書ける。\(t=u-r_{mn}+1/4\) とすると
\[
 \boxed{\int W(u)|A'(u)|^2du
  =e^{1/8}\sum_{m,n\ge1}\frac{\mu(m)\mu(n)}{\sqrt{mn}}
       e^{-d_{mn}^2/2}
       \int W(u)(4t^2-d_{mn}^2)e^{-2t^2}du.}        \tag{C4.4}
\]
実際、各項の derivative multiplier は
\(-1/2-2(u-\log n)=d_{mn}-2t\)、他方は \(-d_{mn}-2t\)。

**禁止する交換:** \(W\equiv1\) として (C4.2) をそのまま無限 energy にすること。既存 Gaussian ノート G7 は actual \(A\notin L^2(\mathbb R)\) を無条件に示している。compact \(W\) での Fubini は、全実線の無限 energy、任意の並べ替え、window limit の有限性を与えない。

## C5. saving の規模と、平均から点への正当な橋

まず finite block \(n\asymp X\) の bounded weight \(w_n\) なら
\[
 \left|\sum_n\mu(n)w_n\right|^2
 =\sum_n\mu(n)^2|w_n|^2+
     2\Re\sum_{h\ge1}\sum_n
          \mu(n)\mu(n+h)w_n\overline{w_{n+h}}.
 \tag{C5.1}
\]
diagonal は \(O(X)\)。**仮に**対象の重みと triangular range に合わせた off-diagonal total \(o(X^2)\) を得ても、結論は weighted sum \(o(X)\) にとどまる。目標の平方は \(O_\epsilon(X^{1+2\epsilon})\) であり、\(X^2/(\log X)^B\) は任意固定 \(B\) でも足りない。単なる \(o(1)\) の rate を平方根 cancellation と取り違えない。また相関全部の絶対値を取ることは十分条件を強くし、必要条件ではない。

平均から pointwise への標準的な橋は実在する。各 \(F\in H^1(u_0-1,u_0+1)\) には絶対定数 \(C\) で
\[
 |F(u_0)|^2\le C\int_{u_0-1}^{u_0+1}
                  (|F(u)|^2+|F'(u)|^2)\,du.       \tag{C5.2}
\]
これは区間平均と \(F(u_0)-F(t)=\int_t^{u_0}F'\) から直接従う。従って欠けている具体的入力の一例は、全 \(u_0\ge1\) で一様に
\[
 \int_{u_0-1}^{u_0+1}(|A|^2+|A'|^2)\,du
      \ll_\epsilon e^{2\epsilon u_0}
 \quad\text{for every }\epsilon>0.                \tag{C5.3}
\]
である。(C4.2),(C4.4) はここに入る actual arithmetic kernel を明示するが、(C5.3) 自体を証明してはいない。MR/MRT/log Chowla と上記改訂版の定理をそのまま適用して得られる式でもない。例外 \(u_0\) のない sliding-window estimate と derivative control が要る。

ゆえに「平均から点へは絶対に移れない」は誤りである。一方、平均・almost-all の結論だけから例外点も含む (C5.3) を読み出すのも誤りである。RH 下では既存ノート G6 の同じ Gaussian partial summation が \(A,A'\) に subexponential bounds を与えるため、(C5.3) は結局既知 RH criterion の強さを持つ。新しい独立算術評価として採用しない。

## C6. entropy・orthogonality・model の位置付け

S4/S5 の entropy decrement や Kátai 型手法は定理の証明機構であり、独立な「\(\mu\) の各符号が確率的に独立」という仮定を提供しない。Sarnak 型 zero-entropy orthogonality や qualitative Daboussi–Delange 型 \(o(X)\) 結論を用いるだけでも、必要な \(X^{1/2+\epsilon}\) の rate は別問題になる。今回これらの一般論を新たな適用定理として採用せず、人工 zero-entropy realization や random replacement も構成しない。

有限次の相関予想・既知の平均 cancellation から、未確認の高次一様性や強い確率 tail bound を補ってはいけない。全固定 shifts の qualitative Chowla を仮定しても、\(h\) が \(X\) とともに増える weighted double sum に必要な rate・一様性がその文言だけで与えられるわけではない。

**最終判断:** inventory と exact compact-window identities を保持する。現時点で Candidate C から RH 距離を縮めると正当化できた入力はない。これは当該定理の現在確認した量化・率との比較であり、相関法一般への universal no-go でも、未検査の改良定理を永久に排除する宣言でもない。

## C7. 追補: BSZ 判定の正確な仮定と Gaussian への適用限界

Bourgain–Sarnak–Ziegler, *Disjointness of Mobius from horocycle flows*, [arXiv:1110.0992v1](https://arxiv.org/pdf/1110.0992v1), 2011-10-05、Theorem 2, p2, (1.3)–(1.4) を確認した。\(F:\mathbb N\to\mathbb C,\ |F|\le1\)、\(\nu\) は multiplicative、\(|\nu|\le1\)。十分小さい**固定** \(\tau>0\) について、全ての異なる素数 \(p,q\le e^{1/\tau}\) で、十分大きい \(M\) に
\[
 \left|\sum_{m\le M}F(pm)\overline{F(qm)}\right|\le\tau M
 \tag{C7.1}
\]
なら、十分大きい \(N\) に
\[
 \left|\sum_{n\le N}\nu(n)F(n)\right|
       \le2\sqrt{\tau\log(1/\tau)}\,N.              \tag{C7.2}
\]
actual \(\nu=\mu\) は許される。原証明 p6 は coprime な因子にのみ乗法性を使い、complete multiplicativity は要求しない。別個の random sign 仮定もない。各 \(\tau\) の閾値を保持すれば qualitative \(o(N)\) に使えるが、\(\tau=\tau(N)\) を任意に小さくできる定理文ではない。

有限性の意味を補う一次資料として Harper, [*A different proof of a finite version of Vinogradov's bilinear sum inequality*](https://warwick.ac.uk/fac/sci/maths/people/staff/harper/finitebilinearnotes.pdf), 2011-10-16、Theorem 1, p1 も確認した。同仮定が全 \(M\ge M_\tau\) に成立するとき、より弱いが閾値を露出した bound
\[
 \left|\sum_{n\le N}\nu(n)F(n)\right|
 \le\frac{N}{\sqrt{\log(1/\tau)+O(1)}}+
 O\!\left(\frac{N}{\log(1/\tau)}
       +\sqrt{Ne^{1/\tau}}+M_\tau e^{1/\tau}\right)  \tag{C7.3}
\]
を与える。これは author research note であり、査読済みと記録しない。固定パラメータの漸近結論から平方根誤差を取り出すとき、finite-range losses を無視できないことが明瞭になる。

本稿の Gaussian readout に \(F_X(n)=e^{-\log^2(n/X)}\) をそのまま入れると、固定した異なる素数 \(p,q\) に対し Riemann sum から
\[
 \frac1X\sum_{m\le X}F_X(pm)F_X(qm)
 \longrightarrow
 c_{p,q}:=\int_0^1 e^{-\log^2(py)-\log^2(qy)}\,dy>0.
 \tag{C7.4}
\]
例えば \(p=2,q=3\) を固定し \(\tau<c_{2,3}/2\) を十分小さく取れば、自然な scale \(M=X\) で (C7.1) は一様に成立しない。\(X\) を固定した後 \(M\to\infty\) とすれば \(F_X\) は絶対総和可能なので (C7.1) はやがて成立するが、その閾値は \(X\) とともに動き、求める diagonal regime \(N\asymp X\) を評価しない。これは raw positive Gaussian weight への直接適用の監査であり、BSZ の他の利用法一般の反証ではない。

また、任意の bounded approximant \(G\) に対して
\[
 \left|\sum_{n\le N}\mu(n)(F(n)-G(n))\right|
       \le\sum_{n\le N}|F(n)-G(n)|.                \tag{C7.5}
\]
従って qualitative \(o(N)\) closure だけでは不十分で、この三角不等式で平方根規模を移すには右辺と approximant の評価を \(O_\epsilon(N^{1/2+\epsilon})\) で、対象と尺度に一様に制御する必要がある。sup norm の誤差 \(\delta\) は \(\delta N\) に増幅される。

同じ BSZ 一次本文 p1, (1.1) は一般 zero-topological-entropy 系の Sarnak statement を **conjecture** として述べる。Theorem 1, p2 は lattice quotient の horocycle flow に対する actual \(\mu\) の \(o(N)\) を証明し、Note 1 は rate を供給しないことを明記する。これは Gaussian family の square-root rate や、未構成の zero-entropy closure を正当化しない。Daboussi–Delange / Kátai という名前だけを追加の算術仮定の代用品にせず、今回 primary で固定した有効な criterion は上の (C7.1)–(C7.2) に限定する。新規に正当化された目標用入力は引き続き 0 件。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/global_remainder/notes/gaussian_global_decomposition.md`](../../global_remainder/notes/gaussian_global_decomposition.md)
