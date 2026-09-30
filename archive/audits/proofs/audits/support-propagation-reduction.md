**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/support-propagation-reduction.md` · Original SHA-256: `fed11481f3db31bd5c30a3dee71f38e5905131f0333ceb2cd4890c000e3db984`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Support の局所延長 — 閉 Weil 形式の block 分解と Schur 補形式

2026-09-29。担当: BUILDER。**厳密な内側 gap を仮定した局所延長の十分条件を記録する。全窓の正値性と RH は未証明。** 新規性を主張しない。停止済み imbalance route や中断した `a=4/5` の head 計算を再開するものではない。

Weil 形式の規約は [固定窓ノート](fixed-window-reduction.md)。digamma の積分・級数は [DLMF §5.9](https://dlmf.nist.gov/5.9)、[§5.7](https://dlmf.nist.gov/5.7) のものを使用する。以下は実際の非有界な閉形式を対象とし、有界な lower operator への置換ではない。

## S1. 空間と archimedean kernel

`0<L<M=L+delta`、`delta>0`、

\[
 I=[-L,L],\quad S=[-M,-L)\cup(L,M],
 \quad H_0=L^2(I),\quad H_1=L^2(S),\quad H_M=H_0\oplus H_1.
\]

端点の選択は `L²` の元に影響しない。すべて零延長し、`Uf(t)=(2pi)^(-1/2)∫f(x)e^(itx)dx`。形式 domain は

\[
 V_M=\{f\in H_M:\int\log(2+|t|)|Uf(t)|^2dt<\infty\}.
\]

`q_M` は既存の閉 Weil 形式、`h(t)=Re psi(1/4+it/2)−log pi` を用いた archimedean 部分を `a_infty` と呼ぶ。

digamma の積分表示の差を取ると、実数 `t` について

\[
 h(t)-h(0)=2\int_0^\infty k(r)(1-\cos(tr))\,dr,
 \qquad k(r)=\frac{e^{-r/2}}{1-e^{-2r}}.              \tag{S1.1}
\]

従って、非負積分と Plancherel から

\[
 a_\infty(f,f)=h(0)\|f\|^2+
       \int_0^\infty k(r)\|\tau_rf-f\|^2dr.         \tag{S1.2}
\]

ここで `tau_r f(x)=f(x−r)`。この表示から得られる閉形式 domain は `V_M` に等しい。これは `h(t)=log(2+|t|)+O(1)` と `h(0)>−6` による。

内側の `x` と shell の `y` の台が交わらない場合、偏極して

\[
 b_\infty(x,y):=a_\infty(x,y)
 =-\int_I\int_S k(|u-v|)x(u)\overline{y(v)}\,dv\,du.
                                                        \tag{S1.3}
\]

符号は負であり、`k(r)~1/(2r)`。まず piecewise smooth BV の `x,y` に対して (S1.2) の偏極を使えばよい。異なる台なので対角項は 0。下記の絶対積分 bound により Fubini が正当化され、その後全 `L²` に有界延長できる。

## S2. 接する区間間でも mixed block は L² 有界

`1/(e^(2r)−1)≤1/(2r)` により

\[
 0<k(r)\le1+\frac1{2r}\qquad(r>0).                  \tag{S2.1}
\]

半直線の Carleman kernel `1/(u+v)` は `L²(R_+)` 上でノルム高々 `pi`。これは重み `v^(-1/2)` に対する Schur test と

\[
 \int_0^\infty\frac{v^{-1/2}}{u+v}\,dv=\pi u^{-1/2}
\]

だけから従う。左右の接点に各々適用し、定数 kernel のノルム `sqrt(|I||S|)=2sqrt(L delta)` を加えると

\[
 |b_\infty(x,y)|\le K_\infty\|x\|\|y\|,
 \qquad K_\infty=\pi+2\sqrt{L\delta}.               \tag{S2.2}
\]

左右をまとめる係数 `pi` は保守的な上界であり、最良定数を主張しない。絶対値を積分の内側へ入れた同じ評価が成立する。

全 Weil mixed block にも明示上界がある。素数冪の総係数

\[
 A_M=\sum_{\log n<2M}\frac{2\Lambda(n)}{\sqrt n}
\]

により、圧縮された有限 translation 和のノルムは `≤A_M`。pole の mixed block は even/odd 各 rank 1 で、ノルム高々

\[
 K_{\rm pole}=2\sqrt{(\sinh L+L)
                        (\sinh M-\sinh L+\delta)}.
\]

従って

\[
 \boxed{K=\pi+2\sqrt{L\delta}+A_M+K_{\rm pole},
 \qquad |q_M(x,y)|\le K\|x\|\|y\|.}                \tag{S2.3}
\]

これは mixed form が単に form-bounded というより強い `L²` bound である。`M` の prime 集合と係数を使用する。`q_M` の内側 restriction は `q_L` に一致する。新しい prime terms は内側の自己相関の support の外側にあり、`log n=2L` の端でも自己相関は 0 だからである。

## S3. Sharp support projections は form domain を保つ

`P=1_I`、`Q=1_S` とする。以下に weighted Hilbert transform の定理を使わない直接証明を与える。

まず `C_c∞(-M,M)` は `V_M` に稠密である。実際、内向き dilation `f_r(x)=r^(-1/2)f(x/r)`、`r↑1` は support を `[-rM,rM]` へ縮め、log-Fourier norm で `f_r→f`。Fourier 側の dilation の強連続性は、compact-support frequency functions の稠密性と `r` が 1 の近くでの log weight の一様比較から従う。その後、support の余白より小さい mollifier を使えば、Fourier 側の有界 multiplier と優収束により同じ norm で滑らかに近似できる。

`f∈C_c∞(-M,M)` なら `Pf,Qf` は compact support の piecewise smooth BV 関数で、Fourier 変換は `O(1/|t|)`。従って両者とも `V_M` に属する。

正の archimedean form

\[
 e(f)=\int(h(t)+7)|Uf(t)|^2dt
\]

を取る。`h(0)>−6` より `e(f)≥||f||²`、その norm は log-Fourier norm と同値である。(S2.2) から

\[
\begin{aligned}
 e(Pf)+e(Qf)
 &=e(f)-2\Re b_\infty(Pf,Qf)\\
 &\le e(f)+2K_\infty\|Pf\|\|Qf\|
 \le(1+K_\infty)e(f).                              \tag{S3.1}
\end{aligned}
\]

稠密性で全 `f∈V_M` へ延長できる。`L²` 極限も同じ `Pf,Qf` なので、形式的な別の extension を作っているのではない。よって

\[
 \boxed{PV_M\subset V_M,\quad QV_M\subset V_M,
 \quad V_M=V_0\oplus V_1,\qquad V_j=V_M\cap H_j.}   \tag{S3.2}
\]

直和は form norm の意味でも連続である。各 restriction は閉で稠密な形式となる。`V_0=V_L`、`V_1` は shell に support を持つ log-Fourier domain である。

独立な確認として、Fourier 側の interval projection kernel `sin(L(t−s))/(pi(t−s))` を dyadic annuli に分けると、離れた block の norm は `O(2^(−|j−k|/2))`、log weight は annulus `j` で `j+1` と同値である。重みの比を掛けても離散 Schur test で有界になる。これは同じ domain 保存を与える別証明であり、境界での点値を仮定しない。

## S4. 非有界閉形式の正確な block 分解

`a=q_L` on `V_0`、`d=q_M|_(V_1)`、`b(x,y)=q_M(x,y)` とする。内積を第一変数線形とし、(S2.3) による有界作用素 `B:H_1→H_0` を

\[
 b(x,y)=\langle x,By\rangle
\]

で定める。全 `x∈V_0,y∈V_1` に

\[
 q_M(x+y)=a(x)+2\Re\langle x,By\rangle+d(y).        \tag{S4.1}
\]

対角の自己共役作用素を `A`、`D` とすれば、対応する全作用素は

\[
 \mathcal A_M=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},
 \qquad D(\mathcal A_M)=D(A)\oplus D(D).             \tag{S4.2}
\]

これは対角の閉形式に有界な off-diagonal perturbation を加えた結果である。全作用素を有界と扱っているわけではない。

`A+kappa≥I,D+kappa≥I` となる共通 shift を取れば、

\[
 |b(x,y)|\le K\|(A+\kappa)^{1/2}x\|
                    \|(D+\kappa)^{1/2}y\|.          \tag{S4.3}
\]

従って必要な relative form boundedness も成立する。ただしこの評価の定数が小さいとは主張しない。

## S5. 正の gap がある場合の variational Schur form

**仮定:** 内側形式に既知の厳密な `c>0` があり、`a(x)≥c||x||²`。このとき `A^(-1)` は全 `H_0` 上で有界、`||A^(-1)||≤1/c`。

shell の variational reduction を

\[
 s(y)=\inf_{x\in V_0}q_M(x+y),\qquad y\in V_1
\]

と定める。`A^(-1)By∈D(A)⊂V_0` なので、平方完成により

\[
\begin{aligned}
 q_M(x+y)&=a(x+A^{-1}By)
                +d(y)-\langle By,A^{-1}By\rangle,\\
 \boxed{s(y)&=d(y)-\|A^{-1/2}By\|^2.}
                                                        \tag{S5.1}
\end{aligned}
\]

infimum は唯一の `x=−A^(-1)By` で達成される。`B* A^(-1)B` は非負で norm `≤K²/c` の有界作用素である。従って `s` は正確に domain `V_1` を持つ閉・下有界形式で、対応する作用素は

\[
 S=D-B^*A^{-1}B,\qquad D(S)=D(D).
\]

ここから

\[
 \boxed{q_M\ge0\text{ on }V_M
            \quad\Longleftrightarrow\quad s\ge0\text{ on }V_1.}
                                                        \tag{S5.2}
\]

両方向とも (S5.1) による。これは内側 gap の下での**同値な還元**であり、shell 側の非負性を証明した定理ではない。全形式が非負のとき、これが shell へ short した非負形式となる。

`s(y)≥eta||y||²`、`eta>0` も得られた場合、`||A^(-1)B||≤K/c` と

\[
 \|x\|^2+\|y\|^2
 \le2\|x+A^{-1}By\|^2+(1+2K^2/c^2)\|y\|^2
\]

から、全形式の明示 gap

\[
 q_M(f)\ge
 \min\left\{\frac c2,\frac\eta{1+2K^2/c^2}\right\}\|f\|^2
                                                        \tag{S5.3}
\]

が従う。

## S6. 小さい shell の明示的な coercivity と局所延長

ノルム 1 の `y∈H_1` について、support の測度は `2delta` なので

\[
 |Uy(t)|^2\le\frac\delta\pi.
\]

確率密度 `p=|Uy|²` のこの点ごとの上界だけを用いる。増加する重み `log(2+|t|)` の積分は、密度 `delta/pi` を中心区間 `[-R,R]`、`R=pi/(2delta)` に詰めたとき最小になる。実際、内側と外側で `(p−p_*)(log(2+|t|)−log(2+R))≥0` を積分すればよい。

従って

\[
 \int\log(2+|t|)|Uy(t)|^2dt\ge J(\delta),
\]
\[
 \boxed{J(\delta)=
 (1+4\delta/\pi)\log\left(2+\frac\pi{2\delta}\right)
          -1-(4\delta/\pi)\log2\longrightarrow\infty.} \tag{S6.1}
\]

全実数 `t` で `h(t)≥log(2+|t|)−8`。`|t|≤1` では `h≥−6`、`|t|≥1` では既知の下界 `h≥log(|t|/(2pi))−1/|t|` を使えばこの保守的定数で足りる。prime norm と負の shell pole を加えて

\[
 d(y)\ge\ell_{\rm shell}\|y\|^2,
\]
\[
 \boxed{\ell_{\rm shell}
 =J(\delta)-8-A_{L+\delta}
       -2\{\sinh(L+\delta)-\sinh L-\delta\}.}       \tag{S6.2}
\]

内側 gap `c>0` がある場合の**検証可能な局所十分条件**は

\[
 \boxed{\ell_{\rm shell}>K^2/c,}                    \tag{S6.3}
\]

ここで `K` は (S2.3)。成立すれば `eta=ell_shell−K²/c>0` を (S5.3) に代入できる。

各固定 `L,c>0` に対し、(S6.3) を満たす十分小さい `delta>0` は存在する。実際、`0<delta≤delta_0` では有限和 `A_(L+delta)≤A_(L+delta_0)`、`K` は有界、pole 項は 0 へ行く一方 `J(delta)→∞`。従って **一つの厳密な gap から、そのすぐ外への延長は可能**である。

これは延長幅の一様下界を与えない。`c` が小さくなれば右辺 `K²/c` が増え、必要な幅は極端に小さくなり得る。繰り返した幅の総和が無限になること、gap が有限の `L` で 0 にならないことは証明していない。

## S7. Zero-gap の障害と固定窓での compactness

一般の無限次元では `A>0` が単に injective/nonnegative の意味なら、(S5.1) の有界逆作用素を使用できない。例えば `H_0=ell²`、`A=diag(1/n)`、shell を 1 次元として `By=y(1/n)_n` と置く。`B` は有界だが

\[
 \|A^{-1/2}B1\|^2=\sum_{n\ge1}\frac1n=\infty.
\]

内側を有限座標で最適化すると、固定 `y=1` に対する infimum は `−∞`。shell の有限な対角値では救えない。`B1=(n^(-3/2))` に替えると energy は有限だが、形式上の最小化点 `A^(-1)B1=(n^(-1/2))` は `ell²` に属さず、infimum は達成されない。kernel がある場合は、mixed functional がその kernel を消さなければ直ちに infimum が `−∞` になる。

gap のない一般形では少なくとも `By∈D(A^(-1/2))` が finite Schur energy の条件となる。これを全 shell domain に対して仮定せず、記号 `A^(-1)` だけを挿入してはいけない。

**実際の固定 Weil 窓に固有の補足。** `V_L→H_L` の埋め込みは compact。form norm の有界集合の Fourier tail は `O(1/log(2+R))`、有限 band 部分は Hilbert–Schmidt operator による compact approximation になるからである。従って下有界な `A_L` は compact resolvent を持つ。この場合、非負性と kernel がないことの両方を証明できれば、質的には正の gap が存在する。しかし (S6.3) を数値的に使うには実際の下界 `c` が必要であり、全 `L` で kernel がないことや一様 gap を本ノートは示していない。上の抽象例を、そのまま固定 Weil 窓のスペクトルの例だとは扱わない。

## S8. delta→0 の固定座標と境界の障害

shell の固定 Hilbert 空間を `K=L²(0,1)⊕L²(0,1)` とし、unitary `J_delta:K→H_1` を

\[
 (J_\delta g)(L+\delta r)=\delta^{-1/2}g_+(r),
 \quad(J_\delta g)(-L-\delta r)=\delta^{-1/2}g_-(r)
\]

で定める。各 `delta>0` の form domain は、零延長した各成分が log-Fourier domain に属する共通空間へ移る。固定 `delta` の dilation で log weights が同値だからである。ノルムの同値定数が `delta↓0` でも有界とは言っていない。

thin shell でも `B_delta J_delta` の norm は 0 へ行かない。`delta<L` として、右境界の両側の正規化 box

\[
 x_\delta=\delta^{-1/2}1_{[L-\delta,L]},
 \qquad y_\delta=\delta^{-1/2}1_{[L,L+\delta]}
\]

を取る。両者は form domain に属し、(S1.3) と `k(r)=1/(2r)+O(1)` から

\[
 b_\infty(x_\delta,y_\delta)
 \longrightarrow-\frac12\int_0^1\int_0^1
                         \frac{du\,dv}{u+v}
 =-\log2.                                           \tag{S8.1}
\]

`2delta<log2` ならこの二つの box 間の prime translation はすべて 0、pole cross は `O(delta)`。従って **実際の Weil mixed form** も同じ極限を持つ。結合の norm が `O(delta)` という近似は成立しない。

ただし固定の正 gap を持つ内側 `A_L` では、`A_L^(-1/2)` が compact であるため、Schur correction 自体には質的な小ささが得られる。外側を一つの固定 `M_0>L` に埋め込むと、各固定 `x∈H_0` に `||(B_delta J_delta)^*x||→0` が shell restriction の絶対連続性から従う。有界性と compactness により

\[
 \|A_L^{-1/2}B_\delta J_\delta\|\longrightarrow0,
 \qquad
 \|J_\delta^*B_\delta^*A_L^{-1}B_\delta J_\delta\|
                       \longrightarrow0.            \tag{S8.2}
\]

ここでは有限 rank で `A_L^(-1/2)` を近似すれば証明できる。定量的速度や微分可能性は主張しない。局所延長の explicit condition (S6.3) はこの compactness 改善を使わず成立する。

独立読み取り監査で (S6.1)–(S6.3) の定数と (S8.2) を再確認した。特に strong convergence が `B_delta J_delta` 自身ではなくその adjoint 側にあること、および固定した外窓への restriction による同定が必要であることを確認済みである。

形式 domain は境界の trace/evaluation が連続な空間ではない。`delta=0` において shell の対角形式は (S6.1) のように発散し、mixed block は (S8.1) の集中を持つ。したがって境界の点値を未知数にした通常の有限行列 Riccati ODE を、そのまま導入することはできない。

共通の form spaces 上で `A(t),B(t),D(t)` が十分に微分可能で、`A(t)` の coercivity が一様に保持されると別途証明できた場合に限り、Banach 空間 `V→V*` の逆写像微分として

\[
 S'=D'-B'^*A^{-1}B-B^*A^{-1}B'
                   +B^*A^{-1}A'A^{-1}B              \tag{S8.3}
\]

が正当化できる。各項はその form-space pairing で読む。この条件を実際の sharp-shell family の `delta=0` に対して検証したとは主張しない。

## S9. 局所延長から全窓へ飛躍しない

同じ domain と局所機構を持ち、全窓では負になる単純なモデルがある。

\[
 q^{\rm toy}(f)=\int\log(1+t^2)|Uf(t)|^2dt-c_0\|f\|^2,
 \qquad c_0>0.
\]

この形式は小さい support では (S6) と同じ Fourier 質量上界から正になる。mixed kernel は `−e^(−|x−y|)/|x−y|` で Carleman 有界性を持つ。一方、ノルム 1 の `g∈C_c∞(-1,1)` を `g_L(x)=L^(-1/2)g(x/L)` と伸ばすと

\[
 q^{\rm toy}(g_L)=\int\log(1+t^2/L^2)|Ug(t)|^2dt-c_0
                              \longrightarrow-c_0<0.
\]

優収束には `log(1+t²/L²)≤t²` と `g` の滑らかさを使える。従って domain 分割、mixed block の有界性、thin-shell coercivity、正 gap からの局所延長の四つが揃っても、全 support の正値性は従わない。これは Weil/RH の反例ではなく、延長論法の論理的限界を示す例である。

本ノートの到達点は (S5.2) の正確な同値還元と (S6.3) の局所十分条件である。全 `L` に渡る gap の非消滅、step size の累積、shell Schur positivity を新しい既知補題として置かない。主証明 graph に全窓正値性の node を追加していない。

## S10. 固定座標 flow・archimedean 増分の読み取り監査

[support-propagation-flow-renormalization.md](support-propagation-flow-renormalization.md) の式 (1)–(4)、(6)、(8) と最後の `2×2` 例を独立に検算した。**指定範囲は PASS。** 同ファイルは変更していない。

- `f_L(x)=L^(-1/2)g(x/L)` に対し `F_(f_L)(t)=sqrt(L)G(Lt)` なので archimedean 積分は `h(u/L)`。prime 相関は `C_g(log n/L)`、pole は `2L∫∫cosh(L(x−y)/2)g(x)overline(g(y))` となる。微分で archimedean の係数 `−1/(2pi L²)`、prime の係数 `+2Lambda(n)log n/(sqrt(n)L²)`、pole の `cosh(Lv/2)+(Lv/2)sinh(Lv/2)` が得られ、すべて一致する。固定 smooth `g` という適用範囲が保持されている。
- `L=1/2` から `L+delta=3/5` に入る新しい prime power は 3 だけ。中心 `±log3/2` に置いた同形の十分狭い正規化 bump の相関は shift `log3` で 1。prime 項の行列は厳密に `−(log3/sqrt3)[[0,1],[1,0]]` で、係数 2 の取り違えはない。
- 式 (8) は `A>0` と有界な Gram factors の下で正しい。`W=V−UA^(-1)B` と置き、`z*Az+||Uz+Wy||²` を `z` について最小化すると `W*(I+UA^(-1)U*)^(-1)W` を得る。元の `M` の PSD は不要である。これは固定分割・固定 support における PSD 増分への式であり、support の拡大を含意しない。
- 節点 `0,1`、測度 `delta_2+delta_3` の Cauchy–Stieltjes 行列は `D=[[13/36,2/3],[2/3,5/4]]`、`det D=1/144`。`M=[[1,2],[2,1]]` を足すと `det(M+D)=−583/144`。Schur complement は `−3` から `−583/196` へ増え、増分は `5/196>0` だが最終値は負のまま。全数値を有理数で再計算した。

また cutoff `T≥7` での archimedean tail の正性について、[groskin-tail.md §3](groskin-tail.md) の独立な有理証明が `h(7)>0` と `h'(t)>0` を与えることを確認した。補助的な 224 bit Arb 計算でも `h(7)=0.1071796712756…>0` と一致した。これらの確認は fixed-cutoff tail の復元を正当化するが、全 `L` にわたる shell Schur positivity を証明するものではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/fixed-window-reduction.md`](fixed-window-reduction.md)
- [`proofs/audits/groskin-tail.md`](groskin-tail.md)
- [`proofs/audits/support-propagation-flow-renormalization.md`](support-propagation-flow-renormalization.md)
