**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/strategy_reset/notes/bilinear_and_uniform_estimates.md` · Original SHA-256: `2bf09b27db686d9b5d2eb0b24283c2cad5937555a2fa06ca1a4d15de25d5700d`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Strategy reset — 双線形評価・一様評価の適用範囲監査

2026-09-30 JST。Candidate A の入力棚卸しだけを行う。新しい証明路線、零点仮説、平均から各点への橋は追加しない。既存ファイルは変更しない。

## 1. 対象と採否基準

\[
R(\log x)=\sum_{n\ge1}\mu(n)e^{-\log^2(n/x)},\qquad
A(\log x)=x^{-1/2}R(\log x),\quad x\ge2.
\]

この Gaussian は対数変数で幅が一定であり、加法的な短区間の指示関数ではない。中心の dyadic block に振動位相はない。Candidate A の合格条件は、既存の無条件の係数側評価から、この和または必要な dyadic 和に **各点ごとの既知 PNT 型を超える評価** が実際に出ること。平均だけ、恒等式だけ、適用に未証明の相殺を要する入力は合格としない。

以下の限定した一次資料の棚卸しでは合格入力は **0 件**。`NO JUSTIFIED NEXT TRACK`。これは将来の双線形法一般の不可能性定理ではない。

分類：A は「RH 不使用」と「既知の零点なし領域・Mertens 評価にも非依存」を分ける。B は実際の算術係数を扱うか。C はこの研究での具体的な定理使用の履歴。D は定量的強さ。E は今回の橋の段階で、0＝対象不一致・平均止まり、1＝正確な分解まで、2＝対象への既知 PNT 型評価まで、3＝合格評価。E は確率や研究価値の点数ではない。

## 2. 入力一覧

| 入力 | A：独立性 | B：実算術 | C：過去の使用 | D：定量的対象 | E・採否 |
|---|---|---|---|---|---|
| Möbius の Vaughan 型 Type I/II 分解 | 恒等式は RH・零点領域・M bound と独立 | 実際の μ | 下記検索範囲で具体的適用なし | 任意の有界 test、下記の厳密有限分解 | 1：相殺未供給 |
| Heath–Brown 型有限分解 | 分解自体は独立。原論文の短区間漸近の証明まで独立とはいえない | 原論文は主に Λ。μ 版は下記の代数的導出 | 具体的適用なし | 因子長の再配置、固定 k の有限恒等式 | 1：推定値ではない |
| Davenport 一様加法評価 | RH 不使用。全周波数版の major arc は既知 L 関数入力に依存 | μ を保持 | 具体的適用なし | 全 α、任意固定 B の N/log^B N | 2：既知 PNT 型以下 |
| Möbius–nilsequence の一様評価 | RH 不使用。一般定理の major arc は算術級数評価を使用 | μ を保持 | 具体的適用なし | 固定複雑度で任意固定対数冪 | 2：固定冪節約なし |
| large sieve / Dirichlet polynomial 平均値 | 基礎不等式は零点領域・M bound と独立 | μ も代入可、任意係数にも成立 | 具体的適用なし | 周波数・高さ・character の二乗平均 | 0：指定された一点への改善なし |
| 算術級数の BV 型平均 | 定理・SW 入力ごとの依存を要確認 | 実算術。μ に適用できる形もある | 具体的適用なし | 法 q の平均、しばしば主成分を除去した誤差 | 0：q=1 を消す定義に注意 |
| BFI dispersion の代表例 | 無条件。『すべての零点領域入力と独立』とは認定しない | Λ・素数の実算術 | 具体的適用なし | 固定剰余 a、well-factorable 法重み、Q=x^(4/7−ε) | 0：対象・平均・重み条件が違う |
| mollifier による零点割合 | 無条件。零点を扱う別カテゴリ | ζ と算術 mollifier | 具体的適用なし | 高さ平均から臨界線上の零点の割合 | 0：全零点・各点の R を制御しない |

C は `research/one_prime`, `research/dyadic`, `research/arithmetic_comma`, `research/weighted_prime_halfspace`, `research/global_remainder`, `research/*.md` を用語検索し、今回の具体的な定理適用が見つからなかったという限定記録。全会話・全ファイルに一度も言及がないという主張ではない。既存の Möbius 反転、部分積分、Euler 積展開、Gaussian smoothing を、新たな Type II 相殺評価の使用と数えない。

## 3. 分解恒等式と、今回不足する Type I/II 入力

Green–Tao, *Quadratic uniformity of the Möbius function* (2008), Lemma 4.1, pp.1876–1877 は、正整数 U,V,N、UV≤N に対し
\[
\frac1N\sum_{N<n\le2N}\mu(n)f(n)=-T_I+T_{II},
\]
\[
T_I=\frac1N\sum_{d\le UV}a_d\sum_{N/d<w\le2N/d}f(dw),\quad
a_d=\sum_{bc=d\atop b\le U,c\le V}\mu(b)\mu(c),
\]
\[
T_{II}=\frac1N\sum_{V<d\le2N/U}b_d
\sum_{\max(U,N/d)<w\le2N/d}\mu(w)f(dw),\quad
b_d=\sum_{c\mid d\atop c>V}\mu(c).
\]
これは実際の μ の有限恒等式。引き続く Proposition 4.2 は Cauchy–Schwarz による Type I/II 検出であり、任意の test に小さい上界を保証する定理ではない。[一次論文 PDF](https://www.numdam.org/item/10.5802/aif.2401.pdf)

本対象への直接検査：N=x とし、N<n≤2N で f(n)=exp(−log²(n/x)) とする。この区間で
\[
e^{-(\log2)^2}\le f(n)\le1.
\]
従って裸の Type I 内和は、整数の個数が増大する範囲で N/d と同程度である。加法 minor arc の指数和を小さくする定理の仮定は満たされない。これは a_d 自身の相殺を否定しないし、Type I/II の別の使い方を禁止しない。今回、その相殺を供給する独立評価を確認できなかった、という判定である。

さらに純粋な Mellin phase f(n)=n^{it} に対しては、任意の正整数 d,d',w,w' で
\[
f(dw)\overline{f(dw')}\,\overline{f(d'w)}f(d'w')=1.
\]
乗法的な長方形相関では位相が正確に消える。Gaussian 振幅を掛けても振幅だけが残る。加法位相 e(αn) の長方形相関 e(α(d−d')(w−w')) と異なるので、加法 minor arc の相殺を Mellin 側へ名称だけで移せない。

Heath–Brown (1982), §2 Lemma 1, pp.1366–1368 は有限 Dirichlet 多項式を用いて Λ の分解と因子長の組替えを扱う。原論文の短区間素数漸近は y=x^ϑ、固定 7/12<ϑ≤1。零点密度定理を明示的には使わないその証明でも、p.1365 と §4 は既知の零点なし領域を用いる。したがって「双線形という形だから零点領域と独立」は誤分類である。[一次論文 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D6C21FF61C1489E5856AA5ED276CB0A9/S0008414X00033307a.pdf/prime-numbers-in-short-intervals-and-a-generalized-vaughan-identity.pdf)

μ について必要な有限代数を別に確認する。整数 U,k≥1、m_U(n)=μ(n)1_{n≤U}、M_U(s)=Σ_{n≤U}μ(n)n^{-s} とする。Re s>1 で
\[
\frac1{\zeta(s)}=
\sum_{j=1}^k(-1)^{j-1}\binom{k}{j}\zeta(s)^{j-1}M_U(s)^j
+\frac{(1-\zeta(s)M_U(s))^k}{\zeta(s)}.
\]
最後の項の Dirichlet 係数は n≤U^k でゼロである。ゆえにその範囲で
\[
\mu(n)=\sum_{j=1}^k(-1)^{j-1}\binom{k}{j}
\bigl(m_U^{*j}*\mathbf1^{*(j-1)}\bigr)(n).
\]
ここで j=1 の \(\mathbf1^{*0}\) は畳込み単位。この式は二項定理からの独立確認であり、上記論文の表示式を μ 用定理として誤引用したものではない。因子長は分離できるが、右辺を絶対値で足して固定冪の相殺が出るわけではない。

## 4. Davenport と Gaussian / Mellin の橋

上記 Green–Tao の Example 3, (1.3), §5 は Davenport の評価
\[
\sup_{\alpha\in\mathbb R}
\left|\sum_{n\le N}\mu(n)e(\alpha n)\right|
\ll_B N(\log N)^{-B}\qquad(B>0\text{ 固定})
\]
を記載し再証明する。定数は一般に非効果的。α=0 は M(N) そのものであり、この周波数を minor arc の成功例から除いてはならない。§5 の minor arc 部分と、算術級数評価を使う major arc 部分を分けて扱う。[同一次論文](https://www.numdam.org/item/10.5802/aif.2401.pdf)

実際に本 Gaussian 和へ移すと、任意固定 B に対し
\[
|R(\log x)|\ll_B x(\log x)^{-B},\qquad
|A(u)|\ll_B e^{u/2}u^{-B}.
\]
導出は M(y) の上記評価だけで足りる。Stieltjes 部分積分により
\[
R(u)=2\int_0^\infty M(e^v)(v-u)e^{-(v-u)^2}\,dv.
\]
v<u/2 の部分は Gaussian で小さく、v≥u/2 では v^{-B}≪u^{-B} と M(e^v)≪_B e^v v^{-B} を用いる。残る Gaussian 積分は定数倍の e^u。既知のより強い PNT 型誤差を改善したわけではなく、x^{1−δ} という固定 δ>0 の節約も得ていない。

加法周波数 α の一様性は Mellin 高さ t の一様性と同一ではない。有限 Y なら Fourier 反転により正確に
\[
\sum_{n\le Y}\mu(n)e^{-\log^2(n/x)}
=\frac1{2\sqrt\pi}\int_{\mathbb R}e^{-t^2/4}x^{-it}
\sum_{n\le Y}\mu(n)n^{it}\,dt.
\]
|t|>T を捨てる誤差は ≤Y erfc(T/2)。一方、Y=∞ の無重み Dirichlet 級数をこの式へそのまま代入することは許されない。和と積分の交換を有限段階で済ませ、n 側の tail も評価する必要がある。

固定 smooth w、supp w⊂[1,2] に対して部分積分から得る安全な評価は
\[
\sum_n\mu(n)n^{it}w(n/N)
\ll_{B,w}(1+|t|)N(\log N)^{-B}.
\]
|t|≤log^C N はより大きい B で吸収できるが、これも同じ既知 M bound の移し替えである。加法 Davenport 定理から、全 Mellin 高さで定数一様の冪節約を得たことにはならない。

Green–Tao, *The Möbius function is strongly orthogonal to nilsequences*, Theorem 1.1 は、固定次元・固定次数・Q-rational Malcev basis に関し、Lipschitz test と polynomial nilsequence への相関を Q の所定の冪、Lipschitz norm、任意固定 log^{−B}N で抑える。一般定理は定数 test も含み、§2 の major arc 入力を省略できない。こちらも今回の固定冪評価を供給しない。[一次論文、arXiv:0807.1736](https://arxiv.org/pdf/0807.1736)

## 5. large sieve / Dirichlet polynomial 平均値

Montgomery–Vaughan, *The large sieve* (1973), Theorem 1, (1.4)：S(α)=Σ_{M<n≤M+N}a_ne(nα)、異なる α_r の mod 1 最小間隔 δ>0 に対して
\[
\sum_r|S(\alpha_r)|^2\le(N+\delta^{-1})\sum_n|a_n|^2.
\]
任意係数に成立する一次定理で、μ の特別な符号相殺を仮定しない。[著者公開 PDF](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf)

μ を代入しても、一つの指定周波数への素朴な結論は |S(0)|=O(N)。また Parseval による二乗平均の平方根 O(√N) を、指定された α=0 の値へ移せない。a_n=1 は同じ基本平均不等式を満たしながら S(0)=N となる。これは平均のみを使う推論への反例であり、μ の実際の値への反例ではない。

Montgomery–Vaughan, *Hilbert's inequality* (1974), Corollary 3, p.75, (1.11) の有限 Dirichlet 多項式への帰結は
\[
\int_0^T\left|\sum_{n\le N}a_nn^{it}\right|^2dt
=T\sum_{n\le N}|a_n|^2
+O\left(\sum_{n\le N}n|a_n|^2\right),
\]
絶対定数、任意 T>0。有限和なので収束条件の問題はない。区間の平行移動は係数の位相へ吸収できる。[著者公開 PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)

|a_n|≤1 では誤差 O(N²)。Gaussian Mellin 積分の有効高さは固定程度なので、この平均定理だけから中心和の √N cancellation は得られない。長い高さ平均で対角項が支配的になっても、t=0 という一点の改善を意味しない。Cauchy–Schwarz による有限 Gaussian 積分への適用も、この誤差を保持しなければならない。

## 6. AP、principal character、dispersion の条件

算術級数評価には主成分の定義がある。Granville–Shao, *When does the Bombieri–Vinogradov theorem hold for a given multiplicative function?*, (1.1)–(1.2), Theorem 1.1 は
\[
\Delta(f,x;q,a)=\sum_{n\le x\atop n\equiv a\pmod q}f(n)
-\frac1{\varphi(q)}\sum_{n\le x\atop(n,q)=1}f(n)
\]
の法平均を扱う。通常の BV 範囲は Q=√x/(log x)^B、総誤差 x/(log x)^A。乗法関数と Dirichlet 逆関数の class 条件、および Siegel–Walfisz 条件を含む同論文の移行定理を、無条件の任意関数・任意法の各点評価に変えてはならない。[一次論文 v1](https://arxiv.org/pdf/1706.05710)

この定義では **Δ(f,x;1,0)=0 恒等的**。従って q=1 項が小さいという読み方から M(x) の改善は得られない。逆に character sum を直接評価する定理では、q=1 の principal character はまさに M(x) を含むので、その項を除外できない。例外 character を差し引いた Δ_Ξ の評価なら、除去した character 成分を回復する別の評価が必要になる。固定 q の結果と、q の平均の結果も別である。

Green–Tao 2008 の Example 2 が用いる古典的 character 評価は、任意固定 B に対し Σ_{n≤N}μ(n)χ(n)≪_B q^{1/2}N(log N)^{−B}。固定 q では任意対数冪だが固定冪節約ではなく、非効果性を消していない。principal q=1 は前節の M bound に戻る。

BFI, *Primes in arithmetic progressions to large moduli* (1986), Theorem 10, p.209 は、固定非零 a、ε>0、Q=x^{4/7−ε}、level Q の well-factorable 重み λ(q) について
\[
\sum_{(q,a)=1}\lambda(q)
\left(\psi(x;q,a)-\frac{x}{\varphi(q)}\right)
\ll_{a,\varepsilon,B}x(\log x)^{-B}
\]
を与える。ここで任意 Q=Q_1Q_2 に対する bounded convolution 分解が重みの条件に入る。これは全法・全剰余の最大値評価ではなく、μ の無重み Gaussian 和の定理でもない。[一次論文 PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6385-11511_2006_Article_BF02399204.pdf)

法の指数 4/7 が 1/2 を超えることと、今回の Mertens 型和の大きさの指数を下げることは別問題である。dispersion の算術情報は未使用の実入力だが、この theorem から R への必要な変換は現在ない。平均から各点への新しい deterministic bridge を暗黙に追加しない。

## 7. mollifier と零点側入力の隔離

Conrey, *More than two fifths of the zeros of the Riemann zeta function are on the critical line* (1989), Theorem 1, p.4 は、臨界線上の割合 κ≥0.4077、および単純かつ臨界線上の割合 κ*≥0.401 を与える。ここでは原定理の用途と量化を確認する例として採用し、現在の最高割合とは主張しない。[一次論文 PDF](https://aimath.org/~kaur/publications/24.pdf)

μ を含む有限 mollifier と ζ の高さ平均を制御することは、1/ζ の全高さの各点評価でも、全零点の排除でもない。割合定理は残る零点を許す。有限 Dirichlet 多項式の長さ・高さの範囲を超えて無限 reciprocal series と同一視できない。mollifier の moment 技術は未使用でも、本 Candidate A の到達条件を満たす入力としては残らない。

零点密度、零点なし領域、1/ζ の既知の領域内評価は別の入力カテゴリ。無条件の定理であることだけから「係数側で新しく独立に得た算術相殺」と数えない。他方、零点密度を用いない証明が可能というだけで、既知の零点なし領域からも独立であるとはいえない。Heath–Brown の原文がその具体例である。

## 8. ここで止める理由

未使用だった具体的な双線形分解、large sieve、dispersion、平均値定理は存在する。しかし本対象へ適用すると、確認できた到達点は次の三つに尽きる。

1. 分解恒等式は正確だが、Gaussian の非振動中心 block に必要な相殺推定は供給しない。
2. 全周波数の既知一様評価は、α=0 を含めると既知 PNT 型の対数冪評価へ戻る。
3. 平均の強さは本対象の指定された各点に移っていない。principal 成分を落としたり、新しい平均→各点の橋を仮定したりすれば、別の未証明入力を追加したことになる。

今回の一次定理の照合で、Candidate A の成功条件を満たす surviving input は 0。独立で未使用という二条件だけで次の研究路線を開始しない。`NO JUSTIFIED NEXT TRACK`。RH は未解決であり、この監査は無条件の将来手法一般を排除しない。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `research/arithmetic_comma` — SOURCE REFERENCE NOT INCLUDED
- `research/dyadic` — SOURCE REFERENCE NOT INCLUDED
- `research/global_remainder` — SOURCE REFERENCE NOT INCLUDED
- `research/one_prime` — SOURCE REFERENCE NOT INCLUDED
- `research/weighted_prime_halfspace` — SOURCE REFERENCE NOT INCLUDED
