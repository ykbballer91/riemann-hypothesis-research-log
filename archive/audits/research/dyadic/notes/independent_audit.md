**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/dyadic/notes/independent_audit.md` · Original SHA-256: `d99f090d89e3740f4a0c03dda8e2d0960ae101e8c27cf3955557c440c744e57f`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Dyadic reduction：独立監査

2026-09-30。DESTROYER による限定監査。対象は今回の dyadic track と既存の固定 scalar arithmetic quotient の接続だけである。旧ノート、state、graph は変更しない。以下は RH の証明でも反例でもなく、新規性を主張しない。

**判定：** forward-only 準指数評価から RH への含意、compact support の exact reduction に対する障害、Möbius cutoff の片側 reduction と無条件の指数 (1/2) 評価を独立に確認した。同じアルゴリズムの準指数 endpoint は、既知の Mertens 評価を用いれば RH と同値であり、独立の新しい入力としては採用できない。compact 障害は非compactな左裾を残す構成を否定しない。

## DA0. 固定する空間と既知の算術入力

記号は `../../one_prime/notes/arithmetic_space.md` に従う。

\[
E=\{g\in C^\infty(\mathbb R):p_N(g)<\infty\ (N\ge1)\},\qquad
p_N(g)=\max_{0\le j\le N}\sup_t
 e^{N|t|}(1+|t|)^N|g^{(j)}(t)|.
\]

even Schwartz 関数 (f) に対し (Sf(x)=2\sum_{m\ge1}f(mx)), (J h(t)=e^{t/2}h(e^t)) と置く。ここでは

\[
V=\{JSf:f\in\mathcal S(\mathbb R)\text{ even},\ f(0)=\textstyle\int_\mathbb R f=0\},
\quad W=\overline V^{\,E},\quad Q=E/W,
\quad q_N([g])=\inf_{w\in W}p_N(g+w).
\]

必要な既知入力は全非自明零点 \(\rho\) の有限 jets の消滅・保持である：

\[
\ell_{\rho,j}(g)=\int_\mathbb R t^j g(t)e^{(\rho-1/2)t}\,dt,
\quad \ell_{\rho,j}(W)=0\quad(0\le j<m_\rho),
\qquad |\ell_{\rho}([g])|\le4q_1([g]).                 \tag{DA0.1}
\]

この消滅は \(\mathcal M(Sf)(s)=2\zeta(s)\mathcal M f(s)\)、二つの pole conditions、連続性から得る。\(\mathcal M f\) は非自明零点の域で正則なので零点を極で相殺しない。今回の議論は (W=V) という更なる閉値域同定を必要としない。

半密度移動 (T_2^ng(t)=g(t-nL)), (L=\log2) は (W) を両方向に保ち、

\[
\ell_\rho(T_2^n x)=2^{n(\rho-1/2)}\ell_\rho(x).       \tag{DA0.2}
\]

これは actual arithmetic quotient の評価であり、任意の人工スペクトルを定義に埋め込んだ模型ではない。今回、全 Banach spectrum の同定や no-extra-spectrum は使わない。

## DA1. Forward-only 準指数評価と反射：PASS

仮に

\[
\forall\epsilon>0\ \exists M_\epsilon,C_\epsilon:
q_1(T_2^n x)\le C_\epsilon2^{\epsilon n}q_{M_\epsilon}(x)
\quad(n\ge0,\ x\in Q)                                  \tag{DA1.1}
\]

が成立するとする。\(M_\epsilon,C_\epsilon\) は (n,x) に依存してはならない。固定した零点 \(\rho=\beta+i\gamma\) と \(\ell_\rho(x)\ne0\) となる固定 (x) に (DA0.1)–(DA0.2) を適用すると

\[
2^{n(\beta-1/2)}|\ell_\rho(x)|
\le4C_\epsilon2^{\epsilon n}q_{M_\epsilon}(x).
\]

(n\to\infty) より \(\beta-1/2\le\epsilon\)、全 \(\epsilon>0\) より \(\beta\le1/2\)。実際の functional equation と複素共役対称性により \(\rho^*=1-\overline\rho\) も零点なので、同じ **forward** 評価を \(\rho^*\) に適用すれば \(1-\beta\le1/2\)。従って RH が従う。負の (n) に対する成長評価は不要である。

これは「任意の片方向作用が全スペクトルを unit circle に置く」という命題ではない。全零点の保持と、実際の零点集合の反射を使用している。反射は [Tao の講義 Corollary 2](https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/) の完成関数の恒等式とも一致する。

## DA2. 零点を入力しない単一の universal witness：PASS

\(g_0(t)=e^{-t^2}\in E\) と置けば

\[
\int_\mathbb R g_0(t)e^{zt}\,dt=\sqrt\pi e^{z^2/4}
\quad(z\in\mathbb C).                                  \tag{DA2.1}
\]

実 (z) の平方完成から得て、compact な (z)-集合上の優収束による正則性と一致定理で全平面へ延ばせる。右辺は零点を持たないので、全 \(\rho\) に対し \(\ell_\rho(g_0)\ne0\)。特に

\[
q_1(T_2^n[g_0])\ge\frac{\sqrt\pi}{4}
 \exp\!\left(\frac{(\beta-1/2)^2-\gamma^2}{4}\right)
 2^{n(\beta-1/2)}.                                      \tag{DA2.2}
\]

よって (DA1.1) より弱い単一軌道条件
\(\forall\epsilon>0\ \exists C_\epsilon:\ q_1(T_2^n[g_0])\le C_\epsilon2^{\epsilon n}\)
でも、DA1 と同じ議論により RH を強制する。高さに応じて前置係数が非常に小さくても、固定零点について (n\to\infty) とするため問題にならない。この条件を無条件には証明していない。

## DA3. (W\cap C_c^\infty(\mathbb R)=\{0\})：PASS

\(g\in W\cap C_c^\infty\)、\(\operatorname{supp}g\subset[-A,A]\) とし、
\(F(z)=\int g(t)e^{zt}dt\) と置く。これは entire で

\[
|F(z)|\le\|g\|_1e^{A|z|}.                              \tag{DA3.1}
\]

仮に (F\not\equiv0) なら (F(z_0)\ne0) となる (z_0) を選べる。Jensen の公式を中心 (z_0)、半径 (2R) に適用すると、半径 (R) 内の零点数 (n_{F,z_0}(R)) を **重複度込みで** 数えて

\[
n_{F,z_0}(R)\log2
\le\frac1{2\pi}\int_0^{2\pi}\log|F(z_0+2Re^{i\theta})|d\theta
 -\log|F(z_0)|\le2AR+O(1).                             \tag{DA3.2}
\]

境界上の零点は半径の近似で処理できる。一方、DA0 の全 jets の消滅により、(F) は各 \(\rho-1/2\) に少なくとも (m_\rho) 次の零点を持つ。Riemann–von Mangoldt 公式

\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)
\]

は無条件である。\(|\Re(\rho-1/2)|<1/2\) なので、十分大きい (R) では (0<\Im\rho\le R/2) の零点が \(|z-z_0|<R\) に全て入る。従って (n_{F,z_0}(R)\ge N(R/2)\gg R\log R) となり (DA3.2) と矛盾する。ゆえに (F\equiv0)、Fourier 変換の単射性から (g=0)。零点計数の参照は [同講義 Theorem 41 とその argument-principle 証明](https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/)。RH や零点の単純性を仮定しない。

**範囲：** compact な (g,h) に (g-h\in W) なら (g=h)。従って任意の compact bump を、固定された compact dyadic interval に exact に移し替えることはできない。ただし非compact な片側裾、近似 reduction、別の topology に関する主張ではない。また単射性だけから (q_1) における定量的な下界は得られない。重複度を消去する jets を用いた点を、distinct zero count だけの議論に置換してはならない。

## DA4. Actual Möbius cutoff reduction：PASS

独立に読み取った対象は `explicit_mobius_reduction.md` §§1–3。以下では (a=2^n\ge1)、(g\in E)、(P=p_4(g)) とする。

\[
H(x)=x^{-1/2}g(\log x),\quad H_a(x)=a^{-1/2}H(x/a),\quad
F_a(x)=\frac12\sum_{m\ge1}\mu(m)H_a(mx).
\]

固定 cutoff は \(\chi=0\) on (x\le1/2)、\(\chi=1\) on (x\ge1)。固定 \(\psi\in C_c^\infty((1/2,1))\) は \(\int_0^\infty\psi=1\)。

\[
c_a=\int_0^\infty\chi F_a,\qquad f_a=\chi F_a-c_a\psi
\]

を positive half-axis 上で作り、even に延ばす。

### DA4.1. Smoothness、poles、exact identity

(g\in E) の全重みにより (H) は原点で flat、無限遠で全微分とともに rapid。(F_a) の級数・各微分は (x>0) で局所一様絶対収束し、無限遠では rapid。cutoff によって (f_a) は原点近傍でゼロになり、even Schwartz 関数になる。\(f_a(0)=0\)、\(\int_\mathbb R f_a=2(c_a-c_a)=0\) が厳密に成立する。

(x\ge1) なら (f_a(kx)=F_a(kx))。さらに

\[
2\sum_{k\ge1}F_a(kx)
=\sum_{r\ge1}H_a(rx)\sum_{m\mid r}\mu(m)=H_a(x).       \tag{DA4.1}
\]

二重和の絶対収束は \(\sum_r d(r)|H_a(rx)|<\infty\) から従う。条件収束の不正な並べ替えではない。

\[
w_n=-JSf_a\in V\subset W,\quad
R_n=T_2^ng+w_n=\sqrt{x}\{H_a(x)-Sf_a(x)\},\quad x=e^t.
\]

pole-free Poisson により (JSf_a\in E) なので (R_n\in E)。また (DA4.1) により (R_n=0) on (t\ge0)。この左裾は一般には compact でなく、DA3 と矛盾しない。(t=0) の smooth matching は exact vanishing と (R_n\in C^\infty) から従う。

### DA4.2. 微分評価と無条件の指数 (1/2)

\(H^{(j)}(y)=y^{-j-1/2}P_j(\partial_t)g(\log y)\)（(P_j) は次数 (j) の固定多項式）から、(j\le4) に対し

\[
y^j|H^{(j)}(y)|\le C_jP\min(y^{7/2},y^{-9/2}).         \tag{DA4.2}
\]

\(b=x/a\) と置き、(b\le1) では (m\le1/b) と残り、(b\ge1) では全項を後者の冪で評価すると

\[
\sum_{m\ge1}\min((mb)^{7/2},(mb)^{-9/2})
\le Cb^{-1}(1+b)^{-7/2}.
\]

これと \(|\mu(m)|\le1\) より、(j\le3) で

\[
|F_a^{(j)}(x)|\le CP\sqrt a\,x^{-j-1}(1+x/a)^{-7/2}.   \tag{DA4.3}
\]

従って

\[
|c_a|+\|f_a''\|_1+\|x f_a'''\|_1
\le CP\sqrt a(1+\log a).                              \tag{DA4.4}
\]

(c_a) は積分を (a) で分ける。微分項では (x\ge1/2) における (x^{-3}) の積分と、固定 compact 区間にある cutoff の微分を評価する。全実線への even extension は固定因子 (2) だけである。

Fourier 規約を \(\widehat f(\xi)=\int f(y)e^{-2\pi iy\xi}dy\) とする。pole-free Poisson と二回部分積分により

\[
Sf(x)=x^{-1}\sum_{k\ne0}\widehat f(k/x),\qquad
|Sf(x)|\le\frac{x}{12}\|f''\|_1.                       \tag{DA4.5}
\]

定数は \((2\pi)^{-2}\sum_{k\ne0}k^{-2}=1/12\)。(D=x\partial_x) とすれば (Df) も even・pole-free：\(\int Df=-\int f=0\)。さらに

\[
(Df)''=2f''+xf''',\qquad
\partial_t JSf=JS(\tfrac12 f+Df).
\]

従って (0<x\le1) で

\[
|JSf_a|+|\partial_t JSf_a|
\le Cx^{3/2}\sqrt a(1+\log a)P.                        \tag{DA4.6}
\]

この領域の (p_1) 重みは (x^{-1}(1-\log x)) であり、
\(\sup_{0<x\le1}x^{1/2}(1-\log x)<\infty\)。直接項 (g(t-\log a)) とその一階微分は (t\le0) 上で (p_1\le Ca^{-4}P)。以上より

\[
\boxed{p_1(R_n(g))\le C2^{n/2}(1+n)p_4(g).}            \tag{DA4.7}
\]

各入力代表元に同じ構成を適用して infimum を取れば
\(q_1(T_2^nx)\le C2^{n/2}(1+n)q_4(x)\) も正しい。(R_n) 自体が (E)-値 map として商へ降りるとは仮定しない。

**この評価の範囲：** 準指数評価ではない。(q_1\) Banach operator norm の評価でも、指数 (1/2) の最適性でもない。零点評価に適用して得る \(\Re\rho\le1\) は既知 strip に含まれる。使用する Möbius 係数は全整数のものであり、prime (2) だけの算術関係を構成したわけではない。

## DA5. Mertens 相殺による条件付き改善：PASS、endpoint は RH 同値

\(0<\theta<1\)、\(|M(X)|\le K_\theta X^\theta\) と仮定する。(K_j(y)=y^jH^{(j)}(y)) と置くと

\[
F_a^{(j)}(x)=\frac{a^{-1/2}x^{-j}}2
 \sum_{m\ge1}\mu(m)K_j(mx/a).
\]

部分和分により

\[
\left|\sum_{m\ge1}\mu(m)K_j(mb)\right|
\le K_\theta b^{-\theta}\int_0^\infty y^\theta|K_j'(y)|dy.
\]

境界項は rapid decay により消える。(j\le3) なら (K_j') に必要な微分は最大 (4) であり、DA4.2 から積分は (C_\theta p_4(g)) 以下。従って

\[
|F_a^{(j)}(x)|\le C_\theta K_\theta p_4(g)
 a^{\theta-1/2}x^{-j-\theta}.                          \tag{DA5.1}
\]

ここで \(\theta<1\) が (F_a\) の原点での可積分性を与える。無限遠は依然 Schwartz。\(\Re s>1\) で絶対収束により

\[
\mathcal M F_a(s)=\frac{\mathcal M H_a(s)}{2\zeta(s)}.
\]

実数 (s\downarrow1) のみを考える。左辺は (x=0) の (x^{-\theta}) 評価と無限遠の rapid decay による優収束で \(\int F_a\) へ、右辺は既知の \(\zeta\) の単純極によりゼロへ収束する。これは \(\Re s>\theta\) に零点がないことを先に仮定する議論ではない。よって

\[
c_a=-\int_0^\infty(1-\chi)F_a,\qquad
|c_a|\le C_\theta K_\theta p_4(g)
 \frac{a^{\theta-1/2}}{1-\theta}.                       \tag{DA5.2}
\]

DA4 の微分・Poisson 評価を繰り返し、直接項の (a^{-4}\le a^{\theta-1/2}) を使えば、**同じ**代表元について

\[
\boxed{p_1(R_n(g))\le C_\theta K_\theta
 2^{n(\theta-1/2)}p_4(g).}                             \tag{DA5.3}
\]

RH から \(M(X)=O_\epsilon(X^{1/2+\epsilon})\) が従う既知の結果は [Soundararajan, arXiv:0705.0723v2, p.1 Introduction Eq.(1)](https://arxiv.org/pdf/0705.0723v2) で確認した。同頁 Theorem 1 はより強い条件付き上界を与える。本監査は同論文の当該 statement を使用し、Littlewood 原論文を独立に再証明・全面監査したとは主張しない。

従って RH はこの固定アルゴリズムの

\[
\forall\epsilon>0\ \exists C_\epsilon:\quad
p_1(R_n(g))\le C_\epsilon2^{\epsilon n}p_4(g)
\quad(g\in E,n\ge0)                                  \tag{DA5.4}
\]

を与える。逆方向は (g_0) だけに (DA5.4) を適用し DA1–DA2 を用いれば足りる。よって **この endpoint は RH 同値**。既存 one-prime ノートの「RH から当該 seminorm bound への逆方向はそこで未証明」という過去の範囲と、今回の条件付き導出は区別する。新たに無条件の相殺原理を得たわけではない。

## DA6. Odd dyadic expansion の topology 監査：PASS

builder の短い補題も独立検算した。\(\Theta_f(x)=\sum_{m\ne0}f(mx)\)、\(O_f\) を odd integers だけの和とすると

\[
\Theta_f(x)=O_f(x)+\Theta_f(2x),\quad
\phi_f(t)=e^{t/2}\Theta_f(e^t),\quad o_f(t)=e^{t/2}O_f(e^t).
\]

従って (J\) 項の dyadic 展開の残差は

\[
r_J(t)=2^{-J/2}\phi_f(t+JL).
\]

固定点 (t_0) で \(\phi_f(t_0)\ne0\) なら

\[
p_N(r_J)\ge2^{-J/2}e^{N|t_0-JL|}
 (1+|t_0-JL|)^N|\phi_f(t_0)|\longrightarrow\infty
\quad(N\ge1).                                         \tag{DA6.1}
\]

一方、固定 (t) では右方の rapid decay により (r_J(t)\to0)。pointwise 展開を (E\) 内での収束に昇格してはならない。具体的な pole-free even Schwartz 関数
\(f(x)=(8u^3-30u^2+15u)e^{-u}\), (u=\pi x^2\)、について (t_0=\log2\) を選ぶと各項の (u\ge4\pi\) で (8u^2-30u+15>0\)、従って \(\phi_f(t_0)>0\)。pole-free 条件は (f(0)=0\) と、Gaussian moments による積分 (15-45/2+15/2=0\) から確認できる。

各有限部分和と残差は (W) にあるので、これは test-space topology での展開の失敗であり、quotient での全ての相殺法を否定するものではない。

## DA7. 採用・停止の区別

| 対象 | 監査結果 | 許される結論 |
|---|---|---|
| forward 準指数評価＋全零点保持＋反射 | PASS | 成立すれば RH。評価自体は未証明 |
| Gaussian 単一軌道 | PASS | 全零点に非零で同じ必要テストを実行できる |
| fixed compact interval への exact reduction | 不可能 | compact 代表元同士の等価は実際の等号のみ |
| Möbius cutoff の片側 noncompact reduction | PASS | actual (W) 内で全 (g\in E) に exact identity |
| 無条件 rate (2^{n/2}(1+n)) | PASS | inter-seminorm bound。RH への改善なし |
| Mertens 条件による rate (2^{n(\theta-1/2)}) | 条件付き PASS | “新しい相殺入力” を証明したことにはならない |
| 同一 algorithm の全 \(\epsilon\) endpoint | RH 同値 | 独立の橋渡しとしては停止 |
| odd dyadic 展開の (E) 収束 | FAIL | pointwise 収束との取り違えを排除 |

数値表、零点探索、finite-window positivity は使用していない。compact 障害を全ての tail reduction に拡大する主張、指数 (1/2) の最適性、RH の解決、新規性のいずれも主張しない。

## DA8. 最終 main の二つの追加：PASS

`../../dyadic_arithmetic_reduction.md` §§2,5 の追加を独立に確認した。

第一に、非零の有限 Laurent polynomial
\(P(z)=\sum_{k=r}^s c_kz^k\) に対して \(P(T_2)E\subseteq W\) は成立しない。
幅が \(L=\log2\) より小さい区間に台を持つ非零 \(g\in C_c^\infty\) を選ぶ。
各 \(T_2^kg\) の台は互いに disjoint なので、ある \(c_k\ne0\) が存在することから
\(P(T_2)g\ne0\)。その台は有限個の compact 集合の和で compact であり、DA3 と矛盾する。
負の Laurent 指数も (T_2) が可逆なので問題ない。特定の noncompact な入力にだけ成立する
coboundary relation を否定する命題ではない。

第二に、Gaussian 一つに対する
\[
\forall\epsilon>0\ \exists C_\epsilon:\quad
q_1(T_2^n[g_0])\le C_\epsilon2^{\epsilon n}\quad(n\ge0)
\]
も RH 同値と分類してよい。十分性は DA1–DA2、必要性は RH から DA5.4 を得て
\(g=g_0\) とし、\(q_1(T_2^n[g_0])\le p_1(R_n(g_0))\) を使う。
単一軌道化は零点依存の witness 選択を除くが、必要な相殺評価を弱い既知入力へ還元したことにはならない。
