**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/dyadic_arithmetic_reduction.md` · Original SHA-256: `aa4def06111bd2a43be53917742baf15acde385a805f03f448787003a57dcf80`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Dyadic Arithmetic Reduction / Fundamental Domain — 完了記録

2026-09-30。RH は **OPEN**。旧 Phase I–IV、Continuous Scale Flow、One-Prime
Return のファイル・state・proof graph を変更しない独立トラック。

結論：同じ算術商の中で、任意の入力に対する **明示的な片側代表元** を構成した。
その評価は
\[
 T_2^ng+w_n(g)=R_n(g),\quad w_n(g)\in W,\quad
 \operatorname{supp}R_n(g)\subseteq(-\infty,0],
\]
\[
 \boxed{p_1(R_n(g))\le C\,2^{n/2}(1+n)p_4(g).}                 \tag{A}
\]
従って指定された Level 2、Level 3 の条件を満たす。ただし非コンパクトな左裾が残り、
準指数評価は証明していない。(A) の零点への帰結は既知の Re rho<=1 に留まる。
新しい RH の証明入力・新規性・指数 1/2 の最適性は主張しない。

同じ具体的アルゴリズムの全 epsilon 準指数評価は、既知の Möbius 部分和定理と合わせて
**RH と同値**と判明した。これを独立な橋渡し補題とするルートは終了する。
3 つの主要機構を検査し、別名の第 4 候補へ無限継続しない。

## 1. 固定した空間と一次資料

CCM [math/0703392v1, Eq.(4.20), Def.4.10, Prop.4.13 / Def.4.14](https://arxiv.org/pdf/math/0703392v1)
と Meyer [math/0311468v1, §5.3–5.7](https://arxiv.org/pdf/math/0311468v1)
の Q の compact-unit invariant scalar sector を使う。一般の cyclic module や
bornological space 全体をこの Fréchet 表示と同一視しない。

\[
 \mathcal V=\{\Sigma\eta:\eta\in\mathcal S(\mathbb A_\mathbb Q),
 \eta(0)=\int\eta=0\},\qquad
 \Sigma\eta(x)=\sum_{r\in\mathbb Q^\times}\eta(rx).
\]

K_c=Zhat^times による Haar 平均 P_0、C_Q/K_c=R_+^times、
J h(t)=exp(t/2)h(exp(t)) を用い、
\[
 p_N(g)=\max_{j\le N}\sup_t e^{N|t|}(1+|t|)^N|g^{(j)}(t)|,
 \quad E=\bigcap_{N\ge1}\{p_N<\infty\},\quad
 W=\overline{J P_0\mathcal V}^{\,E},\quad \mathcal Q=E/W.
\]
\[
 q_N([g])=\inf_{w\in W}p_N(g+w),\qquad T_2g(t)=g(t-\log2).
\]

本構成は、既に実際の range に含まれる
\[
 \eta=f_\infty\otimes\prod_p1_{\mathbb Z_p},\quad
 f_\infty\text{ even Schwartz},\quad f_\infty(0)=\int f_\infty=0,
 \quad S f(x)=2\sum_{m\ge1}f(mx)
\]
だけを使う。W の range が閉であるという追加主張さえ今回の構成には不要である。
実成分の scaling と scalar multiplication は両 pole conditions を保存し、P_0 と可換。
E 上の scaling は連続可逆なので、正負いずれも T_2^n W=W。
詳しい有理数倍との区別は [dyadic relations](dyadic/notes/dyadic_relations.md)。

既存の quotient topology、q_1、Gamma/Euler 因子、零点とその jets を一切置換しない。
既存 Banach 完備化を経由する必要もない。

## 2. 片方向だけで十分であることの完全な確認

全非自明零点 rho に対し、alpha=rho-1/2 と置く。
\[
 \ell_\rho(g)=\int_\mathbb Rg(t)e^{\alpha t}\,dt,
 \quad |\ell_\rho([g])|\le4q_1([g]),\quad
 \ell_\rho(T_2^nx)=2^{n\alpha}\ell_\rho(x).                    \tag{1}
\]
この汎関数は非零であり、W に消える。位数 m_rho の零点では t^j の挿入による
j<m_rho の jets も W に消える。これらは既知の critical strip 0<Re rho<1 と
絶対積分評価、actual arithmetic Mellin identity から従い、RH は不要。

仮に全 epsilon>0 に対し、n と x に依存しない M_epsilon,C_epsilon があり
\[
 q_1(T_2^nx)\le C_\epsilon2^{\epsilon n}q_{M_\epsilon}(x)
 \quad(n\ge0)                                               \tag{2}
\]
とする。ell_rho(x)!=0 となる一つの固定 x を選ぶと
\[
 2^{n(\Re\rho-1/2)}|\ell_\rho(x)|
 \le4C_\epsilon2^{\epsilon n}q_{M_\epsilon}(x).
\]
n log2 で対数を割り n→infinity、次いで epsilon→0 として Re rho<=1/2。
関数等式で 1-rho も零点だから、同じ評価をそれに適用すると Re rho>=1/2。
よって RH。逆時間の評価、trace class、compact resolvent、Hilbert basis は不要。
反射はここでだけ使い、算術的 cancellation の証明に隠していない。

さらに、各零点用の別個の入力は不要である。
\[
 g_*(t)=e^{-t^2}\in E,\qquad
 \ell_\rho(g_*)=\sqrt\pi\exp((\rho-1/2)^2/4)\ne0.             \tag{3}
\]
従ってこの一つの零点に依存しない Gaussian class について forward 準指数評価が
あれば十分。これは witness の縮約であって、必要な評価の独立証明ではない。
以下の構成を RH 下で評価すると (3) の準指数条件も出るため、この単一軌道の
endpoint 条件も RH 同値として扱う。

## 3. 明示的 reduction algorithm と定量結果

完全証明は [explicit_mobius_reduction.md](dyadic/notes/explicit_mobius_reduction.md)。
固定 smooth cutoff chi=0 on x<=1/2、chi=1 on x>=1 と、
psi supported in (1/2,1)、integral psi=1 を選ぶ。a=2^n とし
\[
 H_a(x)=a^{-1/2}(x/a)^{-1/2}g(\log(x/a)),\qquad
 F_a(x)=\frac12\sum_{m\ge1}\mu(m)H_a(mx),
\]
\[
 c_a=\int_0^\infty\chi F_a,\qquad
 f_a=\chi F_a-c_a\psi\quad\text{を偶延長},
\quad w_n(g)=-J S f_a.                                     \tag{4}
\]
f_a は pole-free even Schwartz であるから w_n は実際の adèlic range の元。
全整数の divisor identity sum_{d|r}mu(d)=1_{r=1} が x>=1 上の完全相殺を与える。
|mu|<=1 による lattice sum estimate と Poisson の二階微分評価により (A) が出る。
\[
 q_1(T_2^nx)\le C2^{n/2}(1+n)q_4(x).                        \tag{5}
\]

指数 1→1/2 の改善の源は、算術和の逆変換で右裾を正確に消し、残った左裾を
archimedean Poisson formula で評価することにある。単なる norm の取り替えではない。
ただし Möbius の符号 cancellation はこの無条件上界ではまだ使っていない。

q_4 入力を使う inter-seminorm bound なので、q_1 完備化上の full operator norm や
full spectral radius<=sqrt2 は主張しない。各 zero-detected orbit の上界に限れば
指数率 1/2。零点実部の改善や subexponential という意味はない。

### 反復を具体的な shell correction として書く

\[
 F_{2a}(x)=2^{-1/2}F_a(x/2),
\]
\[
 k_a(x)=2^{-1/2}[\chi(x)-\chi(x/2)]F_a(x/2)
             -c_{2a}\psi(x)+2^{-1/2}c_a\psi(x/2).
\]
k_a は .5<=|x|<=2 に台を持つ even Schwartz、値と積分が 0。
初期値は R_0=g-JSf_1 であり、一般に g そのものではない。
\[
 R_{n+1}=T_2R_n-J S k_{2^n}.                                \tag{6}
\]
したがって n=1,2,3,4 は、順に T_2R_0-JSk_1、
T_2^2R_0-T_2JSk_1-JSk_2、
T_2^3R_0-T_2^2JSk_1-T_2JSk_2-JSk_4、
T_2^4R_0-T_2^3JSk_1-T_2^2JSk_2-T_2JSk_4-JSk_8 となる。
これは actual W に属する補正の telescoping だが、補正の大きさは一様にはならない。
k_a の archimedean compact support と、JSk_a の log-compact support を混同しない。

## 4. 到達できない endpoint の正体

仮定 |M(X)|<=K_theta X^theta, 0<theta<1 の下では、**同じ** f_a,w_n,R_n に対し
\[
 p_1(R_n(g))\le C_\theta K_\theta
                   2^{(\theta-1/2)n}p_4(g).                 \tag{7}
\]
M は Möbius 部分和。この条件付き評価では、部分和分に加えて
integral F_a=0 を、Mellin identity と s=1 の既知の極から導く。
moment correction を絶対値だけで評価する方法では、この改善は出ない。

RH⇒M(X)=O_epsilon(X^{1/2+epsilon}) は classical theorem。
[Báez-Duarte v2 §2.1](https://arxiv.org/html/math/0202141v2#S2.SS1) と
[Soundararajan v2, Introduction Eq.(1)](https://arxiv.org/pdf/0705.0723v2) を確認した。
従って (7) と §2 により、固定アルゴリズム (4) の
\[
 \forall\epsilon>0\ \exists C_\epsilon:\quad
 p_1(R_n(g))\le C_\epsilon2^{\epsilon n}p_4(g)
 \quad(\forall g\in E,\ n\ge0)                             \tag{8}
\]
は RH と双方向に同値。ここで逆方向を未検査のまま「より弱い局所条件」と呼ばない。
(8) を新しい独立 bridge として主証明グラフへ採用しない。

## 5. 基本領域への完全折り戻しが不可能な範囲

\[
                         W\cap C_c^\infty(\mathbb R)=\{0\}.\tag{9}
\]
理由：compact g の Laplace transform は exponential type の entire function。
非零なら Jensen で multiplicity を数えた零点数は O(R)。一方 W なら全 rho と
その jets を消すため、Riemann–von Mangoldt の order R log R 個の零点を持つ。
矛盾。transform identically zero なら Fourier injectivity で g=0。

従って二つの compact representatives が同じ class なら等しい。非零 compact g の
遠方 translate を別の固定 compact interval へ exact に折り戻すことはできない。
これは非compact tails、近似 reduction、(4) の構成を禁止する定理ではない。

同じ理由で、全 E について P(T_2)E subset W となる非零有限 Laurent polynomial P は
存在しない。幅が log2 より小さい compact bump を選べば各 translate は互いに
disjoint で、P(T_2)g は非零 compact。それが W に入ることは (9) と矛盾する。
特定の非compact h に関する coboundary relation まで排除するものではない。

## 6. 文献比較・反証・終了判定

Meyer §5.3 には inverse Euler operator と cutoff の既知の組合せがある。
今回の特定の p_1/p_4 estimate と同一の既刊定理であるとは確認しておらず、新規とも
主張しない。Nyman–Beurling との literal な同一性は未証明。ただし endpoint に
戻ってくる Möbius cancellation は RH 同値である。

全整数の Beurling generators を 2^j だけに交換すると、元の target はその閉包に
入らないことを区間ごとの exact 計算で示した。これは今回の full arithmetic W の
中で時間のみ dyadic にすることとは異なる。

主要機構を三つ検査した。

1. Rational/2-adic lattice/odd-even telescoping：正確な恒等式は range 内。
   任意の非零 class の指数的 drift を消さない。無限展開は E 位相で収束しない。
2. Poisson/reflection/compact fundamental-domain folding：固定 compact 領域への
   exact folding は (9) で否定。反射だけで相殺を作る推論も否定。
3. Full-arithmetic Möbius inverse/cutoff：explicit representative と exponent 1/2 は
   成立。準指数 endpoint を独立に証明できず、固定構成では RH 同値と確認。

Gaussian、compact bump、translated bump、one-sided tail、oscillatory input、synthetic
off-line character、quotient collapse、evaluation loss、隠れた density 仮定を監査した。
詳細は [adversarial audit](../../audits/proofs/audits/dyadic_reduction_adversarial.md)。
n=1..4 の具体的有限和計算・数値反証試験も実行。数値標本を無限 n の証明に使わない。

**Strategy review:** 無条件の (A) を保存して、この探索を終了する。算術的同値関係が
すべての準指数 reduction を不可能にすると証明したわけではない。現在の不足は
既存の算術入力から RH 同値の endpoint を仮定せずに exponent 0 へ達する cancellation。
旧 phase への自動 merge は 0。ユーザーの次の方針決定用に
[プレーンテキスト報告](dyadic/completion_report.txt) を保存する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/dyadic_reduction_adversarial.md`](../../audits/proofs/audits/dyadic_reduction_adversarial.md)
- [`research/dyadic/completion_report.txt`](dyadic/completion_report.txt)
- [`research/dyadic/notes/dyadic_relations.md`](dyadic/notes/dyadic_relations.md)
- [`research/dyadic/notes/explicit_mobius_reduction.md`](dyadic/notes/explicit_mobius_reduction.md)
