**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/weighted_prime_halfspace/notes/tilt_and_sieve_parity.md` · Original SHA-256: `818053b00de34e1093d3f5b414156661954275df3be5461a2fcf0b210c204205`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Weighted prime halfspace：Gibbs tilt と sieve parity の独立監査

2026-09-30。Track C の限定監査。旧ファイルを変更せず、有限 Gibbs 表示の exactness、復元相関、境界近傍の分布、divisor-density 情報の範囲だけを扱う。RH は未解決。新規性や一般的な sieve / probability methods 全体の不可能性を主張しない。

**判定：** exponential tilt は正確な変数変換である。しかし cutoff と parity の相関を product expectation に置換することはできない。actual prime weights では平均を境界へ合わせても相対的に狭い Gaussian window にはならず、通常の CLT を前提とする近似はこのままでは使えない。sieve parity については、誤差を明記した divisor-sum 補題と固定 divisor に対する模型を採用し、あらゆる sieve method に対する普遍的不可能性とは区別する。

## TP1. 有限 Gibbs 表示：全実数の tilt に対して exact

(X\ge2)、(L=\log X)、(P_X=\{p:p\le X\}\) とする。subset (S\subseteq P_X\) について
\[
W(S)=\sum_{p\in S}\log p,\qquad \chi(S)=(-1)^{|S|},
\quad Z_\sigma=\prod_{p\le X}(1+p^{-\sigma}).
\]
任意の実 \(\sigma\) に対し
\[
\mathbb P_\sigma(S)=Z_\sigma^{-1}e^{-\sigma W(S)}
\]
は有限集合上の probability measure。各 prime の selection indicators (I_p) は独立 Bernoulli で
\[
q_{p,\sigma}:=\mathbb P_\sigma(I_p=1)=\frac1{1+p^\sigma}.
\]
全ての squarefree (n\le X\) の prime factors は (P_X) に入るから、
\[
\boxed{M(X)=Z_\sigma\,\mathbb E_\sigma
 [\chi\,e^{\sigma W}1_{W\le L}].}                       \tag{TP1.1}
\]
これは近似でなく有限和の恒等式。small / large prime を切り落とした別模型ではない。

積として計算できるのは
\[
\mathbb E_\sigma\chi
=\prod_{p\le X}(1-2q_{p,\sigma})
=\prod_{p\le X}\frac{1-p^{-\sigma}}{1+p^{-\sigma}}.       \tag{TP1.2}
\]
復元重み \(G_\sigma=e^{\sigma W}1_{W\le L}\) は各 prime の独立積ではない。従って (TP1.2) だけでは (TP1.1) を評価できない。

## TP2. Bulk と remainder：相関を明示すれば target がそのまま残る

\(Q_{\rm sf}(X)=\sum_{n\le X}\mu(n)^2\) とすると
\(\mathbb E_\sigma G_\sigma=Q_{\rm sf}(X)/Z_\sigma\)。よって
\[
\boxed{M(X)=Q_{\rm sf}(X)\,\mathbb E_\sigma\chi
       +Z_\sigma\operatorname{Cov}_\sigma(\chi,G_\sigma).} \tag{TP2.1}
\]
ここで covariance は実確率変数の通常のもの。前半を bulk と呼んでも、後半は元の signed cutoff に関する情報を保持する。独立な見積りなしに remainder を小さいと仮定してはいけない。

### Exact finite countertest

(X=3,\sigma=1\) では (P_X=\{2,3\}\)、(Z=2\)。

| (S) | ∅ | {2} | {3} | {2,3} |
|---|---:|---:|---:|---:|
| probability | (1/2) | (1/4) | (1/6) | (1/12) |
| parity \(\chi\) | (1) | (-1) | (-1) | (1) |
| \(G=e^W1_{W\le\log3}\) | (1) | (2) | (3) | (0) |

従って
\[
\mathbb E\chi=\frac16,\quad \mathbb EG=\frac32,\quad
\mathbb E(\chi G)=-\frac12,\quad \operatorname{Cov}(\chi,G)=-\frac34.
\]
復元値は
\[
M(3)=-1=\underbrace{\tfrac12}_{\text{bulk}}
       \underbrace{-\tfrac32}_{Z\operatorname{Cov}}.
\]
product of expectations へ置換すると符号まで間違う。これは tilt の exactness の反例ではなく、独立性を失った observable を独立と扱う推論の反例。

## TP3. Saddle equation の存在範囲

\[
m_X(\sigma)=\mathbb E_\sigma W
=\sum_{p\le X}\frac{\log p}{1+p^\sigma},\qquad
v_X(\sigma)=\operatorname{Var}_\sigma W
=\sum_{p\le X}\frac{p^\sigma(\log p)^2}{(1+p^\sigma)^2}.
\]
有限 prime set が空でないとき
\[
m_X'(\sigma)=-v_X(\sigma)<0,\quad
m_X(-\infty)=\vartheta(X),\quad m_X(+\infty)=0,
\]
ただし \(\vartheta(X)=\sum_{p\le X}\log p\)。従って finite real saddle
\(m_X(\sigma_X)=L\) が存在する必要十分条件は
\[
0<L<\vartheta(X).
\]
存在すれば一意。さらに \(\sigma_X>0\) の必要十分条件は
\(L<\vartheta(X)/2\)。例えば (X=2) は (L=\vartheta(X)\) なので有限 saddle を持たない。

PNT により \(\vartheta(X)\sim X\) なので、十分大きい (X) では positive saddle が存在する。使用する標準入力は PNT のみであり、RH は不要。[DLMF §27.12, Eq.(27.12.5)](https://dlmf.nist.gov/27.12.E5) はこれより強い無条件の prime-count estimate を記録している。

## TP4. Boundary scale の揺らぎ：Gaussian concentration を仮定できない

PNT と部分和分により、固定 (r>0) について
\[
\sum_{p\le X}\frac{(\log p)^r}{p}
\sim\frac{L^r}{r}.
\]
分母 (p+1) と (p) の差は \(\sum (\log p)^r/p^2<\infty\) で処理できる。従って
\[
m_X(1)\sim L,\qquad v_X(1)\sim\frac12L^2.             \tag{TP4.1}
\]
標準偏差は境界位置 (L) と同じ order。この事実だけでも relative narrow-window approximation の根拠にはならない。

### TP4.1. Limiting Laplace transform の直接導出

\(u_p=\log p/L\) と置く。固定 (t\ge0) について
\[
\log\mathbb E_1e^{-tW/L}
=\sum_{p\le X}\log\left(1+\frac{e^{-tu_p}-1}{p+1}\right).
\]
\(|e^{-tu}-1|\le C_tu\) と \(q_{p,1}\le1/3\) により、二次誤差は
\(O_t(L^{-2}\sum_p(\log p)^2/p^2)=o(1)\)。(1/(p+1)) を (1/p) へ替える誤差も (O_t(L^{-1}\sum_p\log p/p^2)=o(1)\)。

PNT の部分和分で
\[
\nu_X:=\frac1L\sum_{p\le X}\frac{\log p}{p}\delta_{u_p}
\ \Longrightarrow\ du\quad\text{on }[0,1].
\]
実際、固定 (0<a\le1) に対する左辺の \([0,a]\) mass は
\(L^{-1}\sum_{p\le X^a}\log p/p\to a\)。
\((e^{-tu}-1)/u\) は (u=0) に連続延長できるので
\[
\boxed{\mathbb E_1e^{-tW/L}\longrightarrow
\exp\left(\int_0^1\frac{e^{-tu}-1}{u}\,du\right).}       \tag{TP4.2}
\]
平均の有界性から (W/L) は tight であり、(TP4.2) と Laplace transform の一意性が極限分布を定める。固定 (z>0) について \(\log\mathbb E e^{zW/L}\le\sum_{p\le X}(e^{zu_p}-1)/(p+1)=O_z(1)\) なので moments も一様可積分。従って mean (1)、variance (1/2)、third cumulant (1/3) の非Gaussian極限である。定数・分類の新規性は主張せず、ここではこの明示的 Laplace transform だけを使う。

### TP4.2. Actual saddle にも同じ極限が残る

固定 (c\in\mathbb R)、\(\sigma=1+c/L\) とすると同じ部分和分から
\[
\frac{m_X(1+c/L)}L\longrightarrow\int_0^1e^{-cu}du.
\]
右辺は (c=0) で (1)、(c>0) で (1) 未満、(c<0) で (1) より大きい。単調性で saddle を挟めば
\[
(\sigma_X-1)L\longrightarrow0.
\]
従って TP4.2 の積の計算は \(\sigma=\sigma_X\) でも同じ極限を与え、
\(v_X(\sigma_X)/L^2\to1/2\)。平均を正確に (L) へ動かすだけでは Gaussian 化しない。

### TP4.3. Lindeberg condition の具体的失敗

\(Y_p=(\log p)(I_p-q_{p,1})\)、\(s_X^2=v_X(1)\) とする。
prime (p\in[X^{1/2},X]\) が selected のとき、十分大きい (X) では
\(|Y_p|>s_X/2\)。その contribution は
\[
\frac1{s_X^2}\sum_{X^{1/2}<p\le X}
q_{p,1}(1-q_{p,1})^2(\log p)^2\longrightarrow\frac34.
\]
従って Lindeberg sum はゼロに向かわない。ordinary Gaussian CLT/LCLT を独立 Bernoulli という語だけで適用することはできない。ただし非Gaussian極限を使う精密な saddle analysis 自体を否定してはいない。

## TP5. Infinite product の存在と parity observable

\(\sigma>1\) では \(\sum_pq_{p,\sigma}<\infty\)。独立 product measure の selected primes は almost surely 有限、(W<\infty\)、\(\chi=(-1)^{\#S}\) は正しく定義できる。この域では
\[
Z_\sigma^{(\infty)}=\frac{\zeta(\sigma)}{\zeta(2\sigma)},\qquad
\mathbb E_\sigma\chi=\frac{\zeta(2\sigma)}{\zeta(\sigma)^2}.
                                                               \tag{TP5.1}
\]
通常の絶対収束 Euler products の計算であり、解析接続による確率解釈ではない。

一方、全実数 \(\sigma\le1\) で \(\sum_pq_{p,\sigma}=\infty\)。second Borel–Cantelli により infinitely many primes が selected、従って (W=\infty\) almost surely。finite parity products は infinitely many selections のたびに符号を反転するので、\((-1)^{\#S}\) はこの極限の通常の random variable として定義されない。

特に (0\le\sigma\le1\) では finite-prime expectations
\(\prod_{p\le y}(1-2q_{p,\sigma})\to0\)。これは arithmetic answer がゼロという意味ではない。存在しない infinite parity を expectation の極限で代用しても、(TP1.1) の weighted cutoff correlation は復元できない。

**負の tilt に関する範囲修正：** finite expectations がゼロに収束するという statement は、全 \(\sigma\le1\) には広げられない。\(-1\le\sigma<0\) では絶対値がゼロに向かうが、\(\sigma<-1\) では \(a=-\sigma>1\) として
\[
\prod_{p\le y}(1-2q_{p,\sigma})
=(-1)^{\pi(y)}\prod_{p\le y}\frac{1-p^{-a}}{1+p^{-a}},
\]
絶対値は \(\zeta(2a)/\zeta(a)^2>0\) へ、符号は振動する。どちらの場合も (W=\infty\) と parity の未定義性は変わらない。

## TP6. Sieve parity：誤差を明記した限定補題

原資料の範囲を区別する。[Tao 2007 の parity problem 解説](https://terrytao.wordpress.com/2007/06/05/open-question-the-parity-problem-in-sieve-theory/) は nonnegative weights (1\pm\lambda(n)\) による divisor-sum argument を説明する。[Tao 2015 Notes 4 §5](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/comment-page-1/) は広い parity barrier を informal とし、pseudorandomness input に依存することを明記している。これを「あらゆる篩手法が不可能」という証明済み定理として採用しない。Selberg 原論文そのものの全面的監査も行っていない。

以下は同じ仕組みを有限和と明示的誤差に限定した補題である。\(\lambda(n)=(-1)^{\Omega(n)}\) は multiplicity 込みの Liouville 関数、(I=(N,2N]\)、\(A\subset I\) 上で \(\lambda=-1\) とする。有限 divisor sum
\[
F(n)=\sum_d c_d1_{d\mid n},\quad
U:=\sum_{n\in I}F(n),\quad
E_\lambda:=\sum_{n\in I}F(n)\lambda(n)
\]
について、

- (F\le1_A) なら (0\ge\sum F(1+\lambda)=U+E_\lambda\)、従って (U\le|E_\lambda|\)。
- (F\ge1_A) なら \(2|A|\le\sum F(1-\lambda)=U-E_\lambda\)、従って (U\ge2|A|-|E_\lambda|\)。

全て有限の exact inequalities。例えば
\[
U=N\sum_dc_d/d+O\!\left(\sum_d|c_d|\right),\qquad
|E_\lambda|\le\sum_d|c_d|
 \left|\sum_{n\in I,d\mid n}\lambda(n)\right|.
\]
後者が claimed main term より小さいと**別途示せる class**では、下限の正の主項や上限の factor (2) 改善が妨げられる。arbitrary weights、arbitrary levels、arbitrary joint correlations でその誤差が小さいとは仮定しない。

## TP7. Local divisor densities が parity を識別しない具体模型

まず \(a_n^\pm=1\pm\lambda(n)\ge0\)。prime (p) では (a_p^+=0\)、(a_p^-=2\) であり、二列は反対の \(\Omega\)-parity に支えられる。しかし
\[
\sum_{n\le X,d\mid n}a_n^\pm
=\lfloor X/d\rfloor\pm\lambda(d)
 \sum_{m\le X/d}\lambda(m).                             \tag{TP7.1}
\]
既知の PNT 同値の \(\sum_{m\le Y}\lambda(m)=o(Y)\) により、**各固定 (d)** に対して両列は同じ leading density (X/d\) を持つ。これだけでは (d\) が (X) とともに増える sieve level の総誤差を制御したことにならない。

本 track は squarefree weights なので、\(\lambda\) と \(\mu\) の区別を残す。対応する非負列は
\[
b_n^\pm=\mu(n)^2(1\pm\lambda(n))=\mu(n)^2\pm\mu(n).
\]
squarefree support 上では parity は \((-1)^{\omega(n)}\) であり、両列は反対の parity に支えられる。固定 squarefree (d) に対して
\[
\sum_{n\le X,d\mid n}b_n^\pm
=\sum_{n\le X,d\mid n}\mu(n)^2
 \ \pm\mu(d)\sum_{m\le X/d,(m,d)=1}\mu(m).              \tag{TP7.2}
\]
前半は
\[
\frac{X}{\zeta(2)d}\prod_{p\mid d}\frac{p}{p+1}+o(X),
\]
後半は固定 (d) で (o(X)\)。後者は (M(Y)=o(Y)\) と、有限集合 (p\mid d) の Euler factors を外す幾何級数から従う：
\(\sum_{(m,d)=1,m\le Y}\mu(m)=\sum_{a\le Y,\,a\text{ is }d\text{-smooth}}M(Y/a)\)、
\(\sum_{a\text{ is }d\text{-smooth}}1/a=\prod_{p\mid d}(1-1/p)^{-1}<\infty\)
に dominated convergence を適用する。nonsquarefree (d) なら両列の divisor sum はともにゼロ。

従って even/odd squarefree parity を完全に分けた列が、同じ固定-divisor leading density を共有する。これは \(\mu^2\) の total mass と \(\mu\) の signed imbalance を混同する推論への具体的な障害である。正確な全 divisor data が与えられれば逆変換できるため、「全ての divisor 情報でも parity が見えない」とは言わない。

## TP8. 結論と未供給の入力

| 対象 | 判定 |
|---|---|
| finite Gibbs reconstruction | 全実 \(\sigma\) で exact |
| “復元 expectation = expectations の積” | 偽、(X=3,\sigma=1\) で符号も逆 |
| saddle の finite existence | (0<\log X<\vartheta(X)\) に限定、大きい (X) では positive |
| boundary tilt だけで狭い Gaussian fluctuation | 偽、normalized variance (1/2\)、非Gaussian極限 |
| infinite \(\sigma\le1\) の通常の parity expectation | parity observable が未定義 |
| local leading densities だけで parity bias を決定 | できない、二つの非負 parity 列が同じ densities を共有 |
| sieve / saddle / nonGaussian methods 全般 | 否定対象外 |

新たに必要なのは、actual cutoff の parity と reconstruction weight の相関に対する具体的な算術評価である。tilt の正性、独立 Bernoulli coordinates、bulk expectation の積表示だけではこの評価を供給しない。本監査に数値実験は用いていない。
