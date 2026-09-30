**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_comma/notes/nonresonance_audit.md` · Original SHA-256: `bed9c58961b692549503df6432787dd615590048705f14878750e9cdc72e3ef0`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Comma：非共鳴・時間平均・符号相殺の独立監査

2026-09-30。旧 track のファイルは変更しない。ここでは有限 prime logs、有限 torus flow、cutoff 付き平方自由和の間の論理だけを調べる。RH の新しい証明や反例、新規性は主張しない。

**判定：** unique factorization は exact nonresonance を与え、固定有限次元では qualitative equidistribution を証明できる。しかし mixing ではなく、時間平均から固定恒等位相の Mertens cancellation への移行は別の義務である。同じ actual prime logs と同じ cutoff monomials を保った全正符号模型が、Möbius 模型と Haar 分布・極限時間分布を完全に共有するため、これらの分布情報だけから固定点評価を制御する一般則は成立しない。

## NC1. Unique factorization と elementary gap

異なる素数 \(P=\{p_1,\ldots,p_k\}\)、\(\omega_j=\log p_j\) とする。
\[
\sum_j m_j\omega_j=0,\quad m_j\in\mathbb Z
\quad\Longrightarrow\quad
\prod_{m_j>0}p_j^{m_j}=\prod_{m_j<0}p_j^{-m_j}
\quad\Longrightarrow\quad m=0.                         \tag{NC1.1}
\]
従って有限 prime logs は \(\mathbb Q\)-linearly independent。ここに Baker の深い定理は不要である。

異なる正整数 \(a,b\) について、例えば (a>b) なら
\[
\log(a/b)=\int_b^a\frac{du}{u}\ge\frac{a-b}{a}\ge\frac1a.
\]
よって
\[
|\log(a/b)|\ge\frac1{\max(a,b)},\qquad
a,b\le X\Longrightarrow |\log(a/b)|\ge X^{-1}.          \tag{NC1.2}
\]
一方、一般の \(0\ne m\in\mathbb Z^k\)、\(\|m\|_\infty\le H\) には numerator、denominator がそれぞれ \((\prod p_j)^H\) 以下なので
\[
|m\cdot\omega|\ge\exp\!\left(-H\sum_j\log p_j\right). \tag{NC1.3}
\]
二つの Fourier modes が各々 \(\|m\|_\infty\le H\) なら、その差には (2H) を使う。actual cutoff monomials \(a,b\le X\) の比較では (NC1.2) が使えるため、より弱い (NC1.3) へわざわざ戻して指数時間障害を主張してはならない。

nonresonance は全整数係数に対する一様な正の gap ではない。例えば \(\log2/\log3\) の有理近似により、非零の \(q\log2-r\log3\) は任意に小さくなる。係数の上限 \(H\) を指定せずに gap を正の定数で下から抑えることはできない。

## NC2. Exact time correlation と qualitative equidistribution

(a,b>0)、\(\delta=\log(a/b)\) とし、\(\operatorname{sinc}u=\sin u/u\)、\(\operatorname{sinc}0=1\) とする。
\[
\frac1{2T}\int_{-T}^{T}a^{it}\overline{b^{it}}\,dt
=\operatorname{sinc}(T\delta).                         \tag{NC2.1}
\]
([0,T]) 規約なら
\[
\frac1T\int_0^T e^{it\delta}dt
=e^{iT\delta/2}\operatorname{sinc}(T\delta/2).            \tag{NC2.2}
\]
従ってそれぞれ絶対値は \(\min(1,(T|\delta|)^{-1})\)、\(\min(1,2/(T|\delta|))\) 以下。factor (2) や位相因子を混ぜない。

torus を \(\mathbb T^k=(\mathbb R/2\pi\mathbb Z)^k\)、flow を
\(\theta\mapsto\theta+t\omega\) とする。非自明 character \(e^{im\cdot\theta}\) の continuous time average は (NC1.1), (NC2.2) により (0)。trigonometric polynomials の一様近似により、任意の continuous test function の時間平均は normalized Haar 平均へ収束する。これで今回使う finite-dimensional Kronecker–Weyl statement は直接証明できる。

これは **continuous time** の statement。離散 sampling \(t=n\tau\) に同じ結論を使うには \(\tau m\cdot\omega\notin2\pi\mathbb Z\) という別条件を確認する必要がある。unique factorization だけから任意の sampling interval の非共鳴性を得たとはしない。

## NC3. Pure point flow は mixing ではない

Haar \(L^2(\mathbb T^k)\) の Koopman action に対し
\[
U_t\chi_m=e^{it(m\cdot\omega)}\chi_m,
\qquad \langle U_t\chi_m,\chi_m\rangle=e^{it(m\cdot\omega)}
\quad(m\ne0).
\]
\(\int\chi_m=0\) である一方、相関の絶対値は常に (1)。従って mixing でも weak mixing でもない。時間平均した相関が (0) になることと、相関自体が \(t\to\infty\) で消えることは異なる。Haar 上の character basis は pure point spectrum を与える。

独立な Haar 座標の存在も、一つの deterministic orbit の異なる時刻の独立性を意味しない。return census に独立試行の確率計算を適用するには、別の仮定が必要である。

## NC4. Baker / Matveev の一次資料と適用範囲

Baker の原論文の書誌は [*Linear forms in the logarithms of algebraic numbers*, Mathematika 13 (1966), 204–216](https://doi.org/10.1112/S0025579300003971) の出版社ページで確認した。今回はその全文・原証明を再監査していない。以下の quantitative statement は直接読めた Matveev の原論文を使う。

[Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izv. Math. 64:6 (2000), 1217–1269](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng) の §2、p.1219、Corollary 2.3/Eq.(2.6) を確認した。そこでは
\[
\log|\Lambda|>-C_1(k,\kappa)D^2\Bigl(\prod_j A_j\Bigr)
 \log(eD)\log(eB)
\]
を与え、\(B\) を \(\max_j|b_j|\) に置き換えられる。

prime logs では \(D=\kappa=1\)、\(A_j=\log p_j>0.16\)、\(B\le H\) として
\[
|m\cdot\omega|>
\exp\!\left[-C_1(k,1)\Bigl(\prod_j\log p_j\Bigr)\log(eH)\right].
                                                               \tag{NC4.1}
\]
\(C_1(k,1)\) は原文 Eq.(2.6) の明示的な次元依存定数であり、\(k\) について指数型の因子を持つ。固定 prime set では \(H\) に対して polynomial lower bound になるが、\(k\to\infty\) で固定指数にはならない。本監査は定理の statement と適用条件の確認であり、その長い原証明の再実行ではない。

(NC1.2), (NC1.3), (NC4.1) のうち対象に合う強い bound を使うべきである。Baker/Matveev 型 bound が巨大な定数を持つことは、そのまま actual return time の必要下界や全 phase methods の不可能性を証明しない。

## NC5. 正の return と anti-alignment の区別

有限 Boolean Euler polynomial
\[
E_P(\theta)=\prod_{p\in P}(1-e^{i\theta_p})
=\sum_{S\subseteq P}(-1)^{|S|}e^{i\sum_{p\in S}\theta_p}
\]
を考える。各 \(|\theta_p|_{2\pi}\le\eta\) なら
\[
|E_P(\theta)|\le\eta^k.                                \tag{NC5.1}
\]
反対に各 \(|\theta_p-\pi|_{2\pi}\le\eta<\pi\) なら
\[
|E_P(\theta)|\ge[2\cos(\eta/2)]^k.                     \tag{NC5.2}
\]
従って \(t\log p\approx0\pmod{2\pi}\) という return は、Möbius 符号付き full product を小さくする。大きい値へそろえるのは \(\pi\) 側の anti-alignment である。両方に有限次元の dense orbit は近づくが、それらの役割は逆。

実際の \(n\le X\) cutoff は全 \(2^k\) subsets の product とは異なる。cutoff 後に (NC5.1) をそのまま流用できない。恒等位相での値は (M(X)) であり、この値の小ささは別途必要となる。

## NC6. Actual logs と cutoff geometry を保つ distribution 反例

\(P_X=\{p:p\le X\}\)、\(k=\pi(X)\)、squarefree \(n\le X\) の exponent vector を \(\kappa(n)\in\{0,1\}^k\) とし
\[
C_X(z)=\sum_{n\le X\atop n\text{ sf}}z^{\kappa(n)},\qquad
F_X^\mu(z)=\sum_{n\le X\atop n\text{ sf}}\mu(n)z^{\kappa(n)}.
\]
\(\mu(n)=(-1)^{\sum_j\kappa_j(n)}\) なので
\[
\boxed{F_X^\mu(z)=C_X(-z).}                            \tag{NC6.1}
\]
torus の multiplication by \((-1,\ldots,-1)\) は Haar measure を保つ。従って \(C_X\) と \(F_X^\mu\) の **complex-valued pushforward distribution が完全に同一**。全 \(L^q\) norms、mixed moments \(\int F^a\overline F^{\,b}\)、tail probabilities も一致する。特に
\[
\int|C_X|^2=\int|F_X^\mu|^2=Q_{\rm sf}(X),\quad
Q_{\rm sf}(X)=\sum_{n\le X}\mu(n)^2
=\frac{6X}{\pi^2}+O(\sqrt X).                         \tag{NC6.2}
\]
最後の漸近は \(\sum_{d\le\sqrt X}\mu(d)\lfloor X/d^2\rfloor\) から初等的に得られる。

固定 \(X\) について NC2 を用いれば、actual orbit \(z_p(t)=e^{it\log p}\) 上の極限時間分布も両者で同じ。さらに Haar-random initial point から始めた有限個の時刻での joint law まで同じである。これは (-z) への平行移動が flow と可換だからである。

しかし恒等位相では
\[
F_X^\mu(1)=M(X),\qquad C_X(1)=Q_{\rm sf}(X)\asymp X.  \tag{NC6.3}
\]
全正符号模型は same logs・same cutoff を持ち、RMS は \(\asymp\sqrt X\) であるのに、固定点の値は \(\asymp X\)。従って mean square、equidistribution、さらには marginal distribution 全体だけから、固定恒等位相の平方根 bound を導く一般則は偽。

**これは actual (M(X)) の平方根 bound が偽という意味ではない。** 符号を phase shift に吸収しても Haar law は変わらないので、law に捨てられた initial phase と reconstruction kernel の相関が必要、という限定された情報不足である。cutoff kernel を固定した joint correlations は一般に変わり、そのような情報を使う全ての手法を否定していない。

### NC6.1. Actual finite Möbius polynomial の全時間 supremum

\(F_X^\mu(-1,\ldots,-1)=Q_{\rm sf}(X)\) と三角不等式、dense orbit から
\[
\boxed{\sup_{t\ge t_0}\left|\sum_{n\le X}\mu(n)n^{it}\right|
=Q_{\rm sf}(X)}\qquad(t_0\ge0).                       \tag{NC6.4}
\]
任意の正の時間 tail も dense であることは、positive-measure open sets への equidistribution から従う。supremum の厳密達成や小さい時刻での到達は主張しない。この式は actual logs 自体に対する「全 \(t\) 一様の平方根 cancellation」を否定するが、\(t=0\) の (M(X)) について新しい情報は与えない。

## NC7. 非共鳴性だけへの別の finite cutoff test

これは actual primes を置換した **synthetic diagnostic** であり、zeta の反例ではない。\(L=1\)、異なる補助素数 \(q_j\)、正の有理数 \(\varepsilon\) を
\(\varepsilon\sqrt{\max q_j}<1/4\) となるよう選び、
\[
\alpha_j=\frac34+\varepsilon\sqrt{q_j}\in(1/2,1)
\]
とする。\(1,\sqrt{q_1},\ldots,\sqrt{q_k}\) は \(\mathbb Q\)-linearly independent なので \(\alpha_j\) も independent。この事実は multiquadratic field の各平方根を独立に符号反転する automorphisms から確認できる。

cutoff \(\sum_{j\in S}\alpha_j\le1\) を満たす subsets は empty と singletons だけ。従って signed count は
\[
A(1)=\sum_{S:\sum_{j\in S}\alpha_j\le1}(-1)^{|S|}=1-k,
\]
unsigned count は (k+1)。任意に大きい \(k\) で maximal-order bias が残る一方、continuous torus flow は equidistributed である。ここで不足するのは非共鳴性ではなく、actual prime distribution と cutoff/parity を結びつける追加の算術構造。

## NC8. Quantitative census：何を評価し、何を言えないか

Fourier polynomial \(f(\theta)=\sum_m c_me^{im\cdot\theta}\) に対し、symmetric time average の exact formula から
\[
\left|\frac1{2T}\int_{-T}^T f(\theta+t\omega)dt-c_0\right|
\le\sum_{m\ne0}|c_m|
 \min\left(1,\frac1{T|m\cdot\omega|}\right).            \tag{NC8.1}
\]
一般の \(\|m\|_\infty\le H\) に NC1.3 を使えば粗い十分条件として
\(T\gg\epsilon^{-1}\sum|c_m|\exp(H\sum_p\log p)\) を得る。
Fourier modes の個数自体も \((2H+1)^k\)。ただしこれはこの粗い proof による **十分時間** であって、実際の必要時間の下界ではない。

actual cutoff sum \(D_X(t)=\sum_{n\le X}c_nn^{it}\) なら
\[
\frac1{2T}\int_{-T}^T|D_X(t)|^2dt
=\sum_n|c_n|^2+
\sum_{a\ne b}c_a\overline{c_b}\operatorname{sinc}(T\log(a/b)).
\]
NC1.2 による直接の誤差上界は
\[
\frac XT\left[\left(\sum_n|c_n|\right)^2-\sum_n|c_n|^2\right].
                                                               \tag{NC8.2}
\]
より鋭い平均値評価の可能性を否定しない。この式も平均値と \(D_X(0)\) の同一視を正当化しない。

return box \(|\theta_j|_{2\pi}<\eta\)（\(0<\eta<\pi\)）の Haar mass は \((\eta/\pi)^k\)。固定 \(k,\eta\) の時間密度はこの値に収束するが、\(k\to\infty\) で一様な誤差評価ではない。box の exponentially small volume だけから deterministic earliest-return time がその逆数以上と結論してはいけない。とくに initial point が box 内なら時刻 (0) ですでに入っている。

**量化の確認：** 固定 \(P,X,H\) の \(T\to\infty\) と、\(P=P_X\)、\(X,H\to\infty\) の同時極限を交換するには明示的な uniform bounds が必要。finite return census はそのまま infinite-dimensional statement の証明にはならない。

## NC9. Cutoff reconstruction の限定読取検算

builder から提示された正規化も確認した。\(\phi\in C_c^\infty(\mathbb R)\)、\(\sigma>1\)、
\(g_\sigma(v)=e^{-\sigma v}\phi(v)\)、\(\widehat g(t)=\int g(v)e^{-itv}dv\) なら
\[
\sum_{n\ge1}\mu(n)\phi(L-\log n)
=\frac{e^{\sigma L}}{2\pi}
\int_\mathbb R\widehat g_\sigma(t)e^{itL}
 \frac{dt}{\zeta(\sigma+it)}.                           \tag{NC9.1}
\]
\(\phi(L-\log n)=e^{\sigma L}n^{-\sigma}g_\sigma(L-\log n)\) と Fourier inversion から従い、\(\sum n^{-\sigma}\) の絶対収束で交換できる。これは log orbit の marginal statistics だけではなく、固定 reconstruction kernel との相関を保持する式である。

非負で質量 (1)、台 ([-h,h]) の mollifier を使って sharp cutoff を平滑化した場合、差は \([Xe^{-h},Xe^h]\) 内の整数だけに支えられ、
\[
|\mathrm{smoothed}-M(X)|\le2X\sinh h+1.                \tag{NC9.2}
\]
signed mollifier では同じ定数 (1) を自動的には使えない。有限 prime cutoff \(y\ge X\) は sharp sum に、\(y\ge Xe^h\) はこの compact smoothing に no-tail exactness を与える。Gaussian など非compact smoothing にこの endpoint を転用しない。

## NC10. 停止判定

| Statement | 判定 |
|---|---|
| finite prime logs の exact nonresonance | 無条件、unique factorization で証明 |
| fixed finite torus の continuous equidistribution | exact character averages で証明 |
| Kronecker flow は mixing | 偽、非自明 character の相関の絶対値は (1) |
| phase marginal law/RMS だけから固定恒等位相の cancellation | 偽、same-cutoff 全正符号模型 |
| actual finite Möbius sum の全時間一様平方根 bound | 偽、supremum は \(Q_{\rm sf}(X)\) |
| 全ての joint phase/cutoff methods | 否定対象外、具体的相関評価が必要 |
| generic gap bound の悪さは必要 return time 下界 | 導けない、十分 bound と必要 bound を区別 |

数値計算はこの監査の根拠にしていない。Baker の書誌確認と Matveev の適用条件確認を超える新しい外部 proof-claim 監査も行っていない。
