**STATUS: RIEMANN HYPOTHESIS OPEN**

> Dated auxiliary research snapshot, 2026-09-30. Priority 2 only: fixed finite heads, not full-ground capture or RH.
> Public credit: @ykbballer91 · AI-assisted · Original text: CC BY 4.0.
> Source: `research/full_ground_capture/priority2/notes/algebraic_rank.md`; original SHA-256: `a7b88f62d53d9c7a8ed92c97cd74a0bc750fdc2167f8ae3b64f1e2192c0bc95a`. Publication formatting does not constitute a new mathematical audit.

---

# Priority 2 — 有限偶 Fourier head の exact rank

2026-09-30。**STATUS: RIEMANN HYPOTHESIS OPEN.** 新規性は主張しない。

本ノートは通常の有限次元線形代数と \(L^2\) cyclicity だけを扱う。
Weil 形式の正値性、growing-\(m\)、全空間の ground capture は結論に含めない。
旧研究ファイル・state・proof graph・公開用コピーは変更しない。

## AR1. 核、窓、shifted phase、偶 head

既存の [CY1](../../cyclicity.md) および
[BR1/BR5](../../../rate_history/notes/boundary_rate_analysis.md) と同じ規約を使う：

\[
\widehat f(x)=\int_{\mathbb R}f(t)e^{-ixt}\,dt,
\qquad \Xi(x)=\xi(1/2+ix),\qquad \widehat k(x)=\Xi(x)/4,
\qquad f_j=k^{(2j)}.
\tag{AR1}
\]

実際の \(k\) は実偶 Schwartz 関数で、
\(\widehat f_j(x)=(-x^2)^j\Xi(x)/4\)。

\(a>0\)、整数 \(N\ge0\)、\(\omega_n=\pi n/a\) とし、以下の基底関数 \(V_n,b_n\) はすべて
\([-a,a]\) の外で零とする。実験に使う shifted basis は

\[
V_n(t)=\frac{(-1)^n e^{i\omega_nt}}{\sqrt{2a}},\quad -N\le n\le N,
\qquad E_N=\operatorname{span}_{\mathbb C}\{V_{-N},\ldots,V_N\}.
\tag{AR2}
\]

\(P_N\) はこの空間への直交射影、\(R_af=\mathbf1_{[-a,a]}f\)。
\((-1)^n\) を除いた unshifted basis も同じ射影を与えるが、列の符号は異なる。
偶部分空間 \(E_N^+=E_N\cap L^2_{\rm even}(\mathbb R)\) の正規直交基底は

\[
b_0(t)=\frac1{\sqrt{2a}},\qquad
b_n(t)=\frac{V_n(t)+V_{-n}(t)}{\sqrt2}
=\frac{(-1)^n}{\sqrt a}\cos(\omega_nt),\quad 1\le n\le N.
\tag{AR3}
\]

したがって \(\dim_{\mathbb C}E_N^+=N+1\)。実係数 cosine sector の実次元も \(N+1\)。
全 head の \(2N+1\) を偶 head の次元と取り違えない。
内積は \(\langle f,g\rangle=\int f\overline g\) とする。

## AR2. 全線 Fourier 標本による ideal rank

\[
q_n=-\omega_n^2,\qquad
\eta_0=1/\sqrt2,\quad \eta_n=(-1)^n\ (n\ge1),
\]
\[
A_{nj}(a)=a^{-1/2}\eta_n\,\frac{\Xi(\omega_n)}4\,q_n^j,
\qquad 0\le n\le N,\quad 0\le j\le m,
\tag{AR4}
\]
と定める。\(q_0^0=1\)。これは全線の Fourier 積分を各行に入れた **ideal 行列** であり、
sharp support 後の行列ではない。

\[
Z_{a,N}=\{n\in\{0,\ldots,N\}:\Xi(\pi n/a)=0\},\quad
r_{a,N}=N+1-|Z_{a,N}|.
\]

**補題 AR2.1.** 任意の \(a,N,m\) で

\[
\operatorname{rank}A_m(a)=\min\{m+1,r_{a,N}\}.
\tag{AR5}
\]

証明：零行を除けば、非零対角行列と相異なる節点 \(q_n\) の Vandermonde 行列の積になる。
任意の \(s\le\min(m+1,r_{a,N})\) 個の行と最初の \(s\) 列の小行列式は非零である。

零点・重複度についての範囲を固定する。

- \(\Xi(0)=4\int k>0\) なので \(n=0\) は零行にならない。実際、\(t\ge0\) の theta 表示で
  \(P_0(y)=y^2-3y/2>0\)、\(y\ge\pi\) であり、偶性から \(k>0\)。
- 一つの標本 \(\omega_n\) が Xi の多重零点でも、消える行は一行だけである。
  ここで必要なのは **hit した非負 grid index の個数** であって零点重複度の和ではない。
- \(+n,-n\) の重複は偶基底 (AR3) により既に除いた。
- 微分列 \(k^{(2j)}\) は Fourier 側で \((-x^2)^j\Xi(x)\) を与える。
  \(\Xi^{(r)}(\omega_n)\) を観測する列ではないため、confluent Vandermonde への置換は不要であり、
  それによって零行が回復することもない。
- 実 grid は実周波数の零点だけを検出する。RH や零点の単純性は仮定していない。

特に \(m\ge N\) の ideal full rank は、全標本の非消失と同値である。
実零点 \(\gamma>0\) に対し \(a=\pi n/\gamma\) と選べば grid hit が起こるので、
任意の窓について対角因子が非零だとは置けない。

## AR3. Actual 列と exact endpoint recurrence

実際の列は

\[
v_j=P_NR_af_j,\qquad B_{nj}(a)=\langle R_af_j,b_n\rangle
=a^{-1/2}\eta_n\int_{-a}^a f_j(t)\cos(\omega_nt)\,dt.
\tag{AR6}
\]

\(\cos(\omega_0t)=1\) と読む。全 \(a,n,j\) で

\[
B_{nj}=A_{nj}-a^{-1/2}\eta_n
\int_{|t|>a}f_j(t)\cos(\omega_nt)\,dt.
\tag{AR7}
\]

これは exact identity で、tail が小さいという仮定はない。
したがって ideal の零行から actual の零行は従わない。

\[
d_0=\sqrt{2/a},\qquad d_n=2/\sqrt a\quad(n\ge1)
\]
とおくと、\(j\ge1\) に対して

\[
\boxed{B_{nj}=q_nB_{n,j-1}+d_n k^{(2j-1)}(a).}
\tag{AR8}
\]

証明：\(b_n'(\pm a)=0\)、\(b_n''=q_nb_n\)、偶関数 \(f\) に対し
\(f'(-a)=-f'(a)\) である。二回部分積分すると

\[
\int_{-a}^a f''b_n
=q_n\int_{-a}^a fb_n+2f'(a)b_n(a).
\]

ここで \(b_0(a)=1/\sqrt{2a}\)、\(b_n(a)=1/\sqrt a\) であり (AR8) を得る。
従って

\[
B_{nj}=q_n^jB_{n0}
+d_n\sum_{r=1}^j q_n^{j-r}k^{(2r-1)}(a).
\tag{AR9}
\]

特に \(B_{0j}=\sqrt{2/a}\,k^{(2j-1)}(a)\) for \(j\ge1\)。
この endpoint 項は shifted phase の相殺により \(n\ge1\) で同符号の係数になる。

**微分の順序：** 本列は \(R_a(D^{2j}k)\) を射影したものであり、
\(D^{2j}(R_ak)\) ではない。後者には一般に端点の delta 分布とその微分が入り、
ここでの \(L^2\) 列として扱えない。

## AR4. Cyclicity から、各固定 head の有限 prefix が張る

既に証明された CY1 は

\[
\overline{\operatorname{span}\{f_j:j\ge0\}}^{L^2}
=L^2_{\rm even}(\mathbb R).
\tag{AR10}
\]

**定理 AR4.1.** 任意の固定 \(a>0,N\ge0\) について有限整数 \(m(a,N)\ge N\) が存在し、

\[
\operatorname{span}\{P_NR_af_j:0\le j\le m(a,N)\}=E_N^+.
\tag{AR11}
\]

証明：\(T=P_NR_a\) は even \(L^2\) から \(E_N^+\) への有界全射である。
もし \(v\in E_N^+\) が全 \(Tf_j\) に直交すれば、\(Tv=v\) と射影の自己共役性から
\(\langle f_j,v\rangle=0\) for every \(j\)。CY1 より \(v=0\)。
有限次元なので、全列の代数的 span は既に \(E_N^+\) に等しい。
その中の有限個の基底列を取り、最大 index を \(m\) とすれば initial prefix も張る。

これは **exact spanning** であり、近似だけの結論ではない。一方、この証明だけでは

\[
m(a,N)=N,\quad \text{explicit な次数上界},\quad
\text{最小特異値の数値下界や conditioning}
\]

は得られない。\(N=0\) だけは \(B_{00}>0\) により \(m=0\) が全窓で明示的に十分。

cyclicity 単独から一律の初期次数を推定できないことは、actual \(k\) と異なる模型で確認できる。
固定 \(a>0\) と任意 \(M\) に対し、
\(g(t)=e^{-t^2}p(t^2),\ \deg p\le M+1\) の \(M+2\) 次元空間に
\(\int_{-a}^a g^{(2j)}=0\), \(0\le j\le M\), という \(M+1\) 個の線形条件を課せば
非零解がある。その Fourier 変換は非零多項式と Gaussian の積なので、
指数 moment による polynomial density と同じ議論で even derivatives は cyclic。
しかし \(N=0\) の最初の \(M+1\) 列は零である。
これは actual 正値 theta 核の反例ではなく、cyclicity だけを使う推論の限界である。

## AR5. 固定 \(N\)、大窓での最初の \(N+1\) 列

ここだけの極限では \(N\) を固定し、\(m=N\)、\(a\to\infty\) とする。
次数を窓と同時に増やす主張ではない。

**補題 AR5.1（ideal の最小特異値）。** raw derivative coefficient の Euclidean norm を使うと

\[
\sigma_{\min}(A_N(a))=\Theta_N(a^{-2N-1/2}).
\tag{AR12}
\]

証明：

\[
A_N(a)=a^{-1/2}D(a)W\,\operatorname{diag}(1,a^{-2},\ldots,a^{-2N}),
\]
\[
D(a)_{nn}=\eta_n\Xi(\pi n/a)/4,
\qquad W_{nj}=(-\pi^2n^2)^j.
\tag{AR13}
\]

\(W\) は固定の可逆 Vandermonde 行列。
\(D(a)\to D_\infty=\operatorname{diag}(\eta_n\Xi(0)/4)\) は可逆なので、
十分大きい \(a\ge1\) で \(\sigma_{\min}(D(a)W)\ge c_N>0\)。
行列積の最小特異値不等式から (AR12) の下界を得る。
上界は単位列ベクトル \(e_N\) を入れて
\(\sigma_{\min}(A_N)\le\|A_Ne_N\|\le C_Na^{-2N-1/2}\)。
これは列を rescale した後の条件数ではなく、(AR6) と同じ raw 座標の評価である。

**補題 AR5.2（actual tail）。** \(Y=\pi e^{2a}\) とすると

\[
\|B_N(a)-A_N(a)\|_{\rm op}
\le C_Na^{-1/2}Y^{2N+5/4}e^{-Y}
\qquad(a\ge1).
\tag{AR14}
\]

証明を theta 表示から与える。

\[
k^{(r)}(t)=e^{t/2}\sum_{\nu\ge1}
P_r(\pi\nu^2e^{2t})e^{-\pi\nu^2e^{2t}},\quad t\in\mathbb R,
\]
\[
P_0(y)=y^2-\tfrac32y,\qquad
P_{r+1}(y)=2yP_r'(y)+(1/2-2y)P_r(y).
\tag{AR15}
\]

これは \(k=\frac18(D_t^2-\frac14)
[e^{t/2}\sum_{\nu\in\mathbb Z}e^{-\pi\nu^2e^{2t}}]\) を項別微分した級数である。
全実 \(t\) の compact 上で収束し、以下の tail 評価では \(t\ge0\) の側を用いる。

\(\deg P_r=r+2\) なので、固定 \(j\) と \(y\ge\pi\) で

\[
|P_{2j}(\nu^2y)|\le C_j\nu^{4j+4}y^{2j+2},\qquad
\sum_{\nu\ge1}\nu^{4j+4}e^{-(\nu^2-1)y}\le C_j.
\]

従って \(|f_j(t)|\le C_j y^{2j+9/4}e^{-y}\)、\(y=\pi e^{2t}\)。
偶性と \(dt=dy/(2y)\) から

\[
\int_{|t|>a}|f_j(t)|\,dt
\le C_j\int_Y^\infty y^{2j+5/4}e^{-y}\,dy
\le C_j'Y^{2j+5/4}e^{-Y}.
\tag{AR16}
\]

最後の不等式は固定 exponent の incomplete-Gamma tail bound であり、
\(y=Y+v\) として \((1+v/Y)^d\le(1+v)^d\), \(Y\ge1\), を積分すれば直接従う。
(AR7)、\(|\cos|\le1\)、有限個の行列成分から (AR14) を得る。

**定理 AR5.3（eventual minimal prefix）。** 各固定 \(N\) について \(a_N<\infty\) が存在し、
すべての \(a\ge a_N\) で

\[
\operatorname{rank}B_N(a)=N+1,
\qquad \sigma_{\min}(B_N(a))=\Theta_N(a^{-2N-1/2}).
\tag{AR17}
\]

実際、(AR14) と (AR12) の比は
\(O_N(a^{2N}Y^{2N+5/4}e^{-Y})\to0\)。
\(|\sigma_{\min}(B)-\sigma_{\min}(A)|\le\|B-A\|\) により結論が従う。
ここでは Xi の grid は原点へ近づき、\(\Xi(0)>0\) によりやがて hit がなくなる。
一般の窓について hit がないと仮定したわけではない。

さらに determinant の先頭定数も固定できる：

\[
\det B_N(a)\sim C_N^*a^{-(N+1)(N+1/2)},
\]
\[
C_N^*=\frac1{\sqrt2}\left(\frac{\Xi(0)}4\right)^{N+1}
\pi^{N(N+1)}\prod_{0\le r<s\le N}(s^2-r^2)>0.
\tag{AR18}
\]

empty product は1。証明は (AR13) の determinant と
\(\|A_N^{-1}(B_N-A_N)\|\to0\) による。
shifted row phase の符号と負の Vandermonde nodes の符号が相殺する。
この式の定数を、\(N\) に一様な定数として使用してはならない。

## AR6. Exceptional windows は離散的（実際には有限）

**補題 AR6.1.** \(F_N(a)=a^{-(N+1)/2}\det B_N(a)\) は \(a>0\) で real analytic。
さらに \(a=0\) の近傍にも real analytic に延長する。

証明：変数を \(t=ax\) に替えると

\[
B_{nj}(a)=\sqrt a\,C_{nj}(a),\qquad
C_{nj}(a)=\eta_n\int_{-1}^1 f_j(ax)\cos(\pi nx)\,dx.
\tag{AR19}
\]

従って \(F_N=\det C\)。theta 表示 (AR15) は複素 \(t\) について
\(|\Im t|<\pi/4\) の compact 上絶対一様収束する。
実際、そこで \(\Re(e^{2t})>0\) は compact ごとに正の下界を持ち、各有限階微分の
多項式増大を \(e^{-c\nu^2}\) が抑える。よって \(f_j\) はこの strip で holomorphic。
\(|\Im a|<\pi/4\)、\(x\in[-1,1]\) なら \(ax\) も同じ strip 内なので、
(AR19) の積分は複素 \(a\) の compact 上 holomorphic である。これには \(a=0\) も含まれる。

**系 AR6.2.** 各固定 \(N\) について

\[
\mathcal E_N=\{a>0:\det B_N(a)=0\}
\tag{AR20}
\]

は離散集合であり、さらに **有限集合** である（空かもしれない）。

証明：(AR17) より \(F_N\) は恒零でなく、十分大きい正の \(a\) で零点を持たない。
real-analytic 非恒零関数の零点は内部で孤立する。0 の近傍にも analytic に延長しているため、
正の零点が0に集積することもない。残る compact 区間で無限個の零点があれば集積点を持ち、
恒零性を強いる。ゆえに有限。

ここで exceptional なのは **最初の \(N+1\) actual 列** の rank である。
\(\mathcal E_N\) を ideal grid-hit 集合と同一視していない。
またこの証明は \(\mathcal E_N\) の具体的位置、個数、空集合性を与えない。
そこでの eventual finite-prefix spanning 自体は AR4.1 が保証する。

## AR7. 証明した量化と停止点

本ノートが与えるものは次の区別である。

1. 任意の固定 \((a,N)\)：有限の initial prefix が actual \(E_N^+\) を exact に張る。
2. 任意の固定 \(N\)：十分大きい \(a\) では最短可能な \(m=N\) で張る。
3. 同じ固定 \(N\)：\(m=N\) が失敗し得る正の窓幅は有限個。ただしそのリストは未同定。
4. ideal rank は全 \(a,N,m\) について (AR5) で明示できるが、actual rank とは異なる。

これらは通常の \(L^2\) head の像についての定理である。
Weil energy、全窓 ground、係数の一様な小ささ、増大する \(N,m\) に対する定量制御へは拡張しない。
有限次元の exact spanning が得られても、その lift の conditioning は別に評価する必要がある。

根拠は既存 CY1、actual theta 表示と Fourier 規約、および上で示した有限次元の直接証明。
新しい外部純粋性・正値性・RH 相当仮説は入力していない。

独立検算：DESTROYER は (AR8) の端点規格化、(AR12)–(AR17) の固定 \(N\) 評価、
および (AR19)–(AR20) の解析性と有限例外の推論を確認した。
これは新しい外部論文全体の再監査や数値 rank 認証を意味しない。
