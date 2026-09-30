**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/hierarchical_selection/notes/support_hierarchy.md` · Original SHA-256: `49d4eaae5246290681ff45d30fd551b590aead13e9161df1880ec844df95c03e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Actual Weil form の固定有限階 support hierarchy

2026-09-30。RH OPEN。新規性主張なし。旧 [境界率ノート](../../rate_history/notes/boundary_rate_analysis.md) は読み取りのみ。
以下の全極限で \(m\) は固定。Fourier 射影 \(P_N\) は入れない。

## SH1. 定理と規約

\[
k=\Phi/4,\quad \widehat k(z)=\Xi(z)/4,\quad f_j=k^{(2j)},\quad
Y=\pi e^{2a},\quad \beta=2Y,
\]
\[
B_Y=e^{a/2-Y}=\pi^{-1/4}Y^{1/4}e^{-Y},\qquad
\kappa_Y=\frac{2B_Y^2}{\beta}=\pi^{-1/2}Y^{-1/2}e^{-2Y}.
\tag{SH1}
\]
\(R_a\) は \([-a,a]\) への sharp restriction と零延長。
\(Q\) は標準の全 archimedean・polar・prime-power 項を持つ Weil 形式。
\(M_{ij}=Q(R_af_i,R_af_j)\)、\(G_{ij}=\langle R_af_i,R_af_j\rangle\)。

**定理。** 任意の固定整数 \(m\ge0\) について、十分大きい \(a\) では
\(M\) と \(G\) は正定値で、一般化最小固有値は単純である。
単位最小固有関数 \(u_{a,m}\) の位相を \(\langle u_{a,m},k\rangle>0\) とすれば
\[
u_{a,m}\to k/\|k\|_2\quad\text{in }L^2(\mathbb R),
\tag{SH2}
\]
\[
\mu_{a,m}\sim
\frac{a(m!)^2}{\sqrt\pi\,\|k\|_2^2}
Y^{7/2-2m}e^{-2Y}.
\tag{SH3}
\]
raw 係数 \(u_{a,m}=R_a\sum_{j=0}^m c_j(a)f_j\) は
\[
c_0\to1/\|k\|_2,\qquad
\frac{c_j}{c_0}\sim
\frac{(-1)^j\binom mj}{4^jY^{2j}}\quad(1\le j\le m).
\tag{SH4}
\]
特に \(m=2,3\) の最小値は、それぞれ
\(4aY^{-1/2}e^{-2Y}/(\sqrt\pi\|k\|_2^2)\)、
\(36aY^{-5/2}e^{-2Y}/(\sqrt\pi\|k\|_2^2)\) に漸近する。
これは有限 radical 部分空間に制限した support-only signed 最小化であり、全窓の ground や RH の定理ではない。

## SH2. Exact jet 座標：相殺する方向も含めて正規化する

実際の theta 級数を
\[
f_j(t)=e^{t/2}\sum_{n\ge1}P_{2j}(\pi n^2e^{2t})e^{-\pi n^2e^{2t}},
\quad P_{r+1}=2yP_r'+(1/2-2y)P_r,
\]
\[
P_0=y^2-\tfrac32y,\qquad P_{2j}(y)=4^jy^{2j+2}(1+O_j(y^{-1}))
\tag{SH5}
\]
とする。各多項式の次数は \(d_j=2j+2\)。
\(W_{\ell j}(Y)=P_{2j}^{(\ell)}(Y)/\ell!\)、\(0\le\ell,j\le m\) と置くと
\[
W(Y)=\operatorname{diag}(Y^{-\ell})\,C_Y\,
       \operatorname{diag}(4^jY^{d_j}),\qquad
C_Y=C+O_m(Y^{-1}),\quad C_{\ell j}=\binom{d_j}{\ell}.
\tag{SH6}
\]
\(C\) は多項式 \(\binom{x}{\ell}\) を相異なる点 \(d_j\) で評価した Vandermonde 行列なので可逆。
従って大きい \(Y\) で \(W\) は可逆。

\(q_{r,Y}\in\operatorname{span}\{P_0,P_2,\ldots,P_{2m}\}\) を
\[
\frac{q_{r,Y}^{(\ell)}(Y)}{\ell!}=\delta_{r\ell}
\quad(0\le\ell\le m)
\tag{SH7}
\]
で一意に定義する。\(q_{r,Y}=\sum_j T_{jr}(Y)P_{2j}\) の係数は exact に
\[
T_{jr}(Y)=4^{-j}Y^{r-d_j}(C_Y^{-1})_{jr}.
\tag{SH8}
\]
特に \(|T_{jr}|\le C_mY^{r-d_j}\)。Taylor 展開は有限和であり
\[
q_{r,Y}(Y+w)=w^r+
\sum_{\ell=m+1}^{2m+2}O_m(Y^{r-\ell})w^\ell.
\tag{SH9}
\]
したがって全 \(r\le m\) について、重み \(e^{-w}\) を掛ければ、多項式およびその有限階微分が \(w^re^{-w}\) へ一様な weighted \(L^1,L^2\) 評価で収束する。

ここで polynomial を実際の全 theta 級数へ戻す：
\[
g_{r,Y}=\sum_jT_{jr}(Y)f_j.
\tag{SH10}
\]
\(g_{r,Y}\) は第1 theta 項だけの模型ではなく、全 \(n\ge1\) を持つ actual 関数である。
一般の \(f_c=\sum c_jf_j\) の exact jet 係数は \(z=Wc\)、従って \(c=Tz\)。

## SH3. Actual tail の有限 profile 空間と一様余項

\(v=\beta(t-a)\ge0\) で
\[
F_{r,Y}(v)=B_Y^{-1}g_{r,Y}(a+v/\beta).
\]
\(w=Y(e^{v/Y}-1)\) を用いると、第1 theta 項は exact に
\[
(1+w/Y)^{1/4}q_{r,Y}(Y+w)e^{-w}.
\tag{SH11}
\]
\(w\ge v\) と (SH9) により、この項とその \(v\) 微分は
\(C_m(1+w)^{K_m}e^{-w}\le C'_me^{-v/2}\) で抑えられる。
\(v\le Y^{1/3}\) の Taylor 展開と残りの exponential tail を分けると、
weighted \(L^1,L^2\) および一回の微分の \(L^1\) で
\[
F_{r,Y}(v)=v^re^{-v}+O_m(Y^{-1})
\tag{SH12}
\]
となる。ここで \(O(Y^{-1})\) は上述の各ノルムの意味。

第2項以降もこの主張を妨げない。(SH8) から \(q_{r,Y}(n^2y)\) は
\(Y^m\) と \(n^2y/Y\) の固定次数多項式で抑えられる。
\(y\ge Y\)、\(n\ge2\) では指数の比は \(e^{-n^2y+Y}\) だから、
これらの総和と必要な微分の各ノルムは
\(O_m(Y^{K_m}e^{-3Y})\)。これは全素数・全整数の寄与を捨てる近似仮定ではなく、実級数の絶対余項評価である。

同じ分割は任意の固定整数 \(d,L\ge0\) に適用できる。
半直線上で
\[
\|(1+v)^L\{D_v^dF_{r,Y}-D_v^d(v^re^{-v})\}\|_{L^1\cap L^2}
=O_{m,d,L}(Y^{-1}).
\tag{SH12a}
\]
\(D_v\) を掛けると \(w'=1+w/Y\) と polynomial の微分が加わるだけで、
固定次数の polynomial times \(e^{-w}\) という majorant は保たれる。
これは例えば \(d\le3\) と有限 \(v\)-moments を含む。
half-line の smooth profile の主張であり、even extension の原点 cusp が消えるという主張ではない。

従って \(F_{z,Y}=\sum z_rF_{r,Y}\) は **全 \(z\in\mathbb C^{m+1}\) に一様に**
\[
|F_{z,Y}(v)|\le C_m|z|e^{-v/2},\quad
\|F_{z,Y}\|_1+\|F'_{z,Y}\|_1\le C_m|z|,
\]
\[
\int_0^\infty |F_{z,Y}|^2dv=z^*Hz+O_m(Y^{-1})|z|^2,
\quad H_{rs}=\int_0^\infty v^{r+s}e^{-2v}dv
=\frac{(r+s)!}{2^{r+s+1}}.
\tag{SH13}
\]
\(H>0\) は多項式の \(L^2(e^{-2v}dv)\) Gram 行列。
この一様性が、高次消去後の小さい方向を保護する。

## SH4. 全 Weil 形式：prime/pole は jet 座標で下位

旧ノート BR2 の weighted-BV test class で、すべての \(g_{r,Y}\) は global radical。
従って \(r=(I-R_a)f_c\) に対して exact に \(Q(R_af_c)=Q(r)\)。
sharp cut の jump を variation に含め、零点側・算術側とも絶対収束による延長を用いる。
global \(L^2\) closability は使わない。

実際の算術表示は
\[
Q(r)=\frac1{2\pi}\int h(\omega)|\widehat r(\omega)|^2d\omega
+2\Re\{\widehat r(i/2)\overline{\widehat r(-i/2)}\}
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\Re C_r(\log n),
\]
\[
h(\omega)=\Re\psi(1/4+i\omega/2)-\log\pi,
\quad C_r(d)=\int r(x+d)\overline{r(x)}dx.
\tag{SH14}
\]
(SH13) により片 edge の Fourier profile は
\(|\widehat{F_{z,Y}}(\xi)|\le C_m|z|/(1+|\xi|)\)。
\(h(\beta\xi)-\log(\beta/(2\pi))\) は
\(C+|\log|\xi||\) 以下なので、archimedean 項の log moment は \(O_m(|z|^2)\)。
左右 edge の混合 kernel は
\(-e^{-|x-y|/2}/(1-e^{-2|x-y|})\)、距離 \(\ge2a\)。
従って
\[
Q_{\rm arch}(r)
=\kappa_Y\left[2a\,z^*Hz+
O_m(1+a/Y)|z|^2\right].
\tag{SH15}
\]

同じ一様 envelope を用いると、pole は
\(O_m(B_Y^2Y^{-3/2})|z|^2\)。同じ側の prime 相関は
\(O_m(B_Y^2Y^{-1}e^{-Yd})|z|^2\)。反対側は \(d<2a\) で零、
\(d=2a+s\ge2a\) で \(O_m(B_Y^2s e^{-Ys})|z|^2\)。
ここでは (SH13) の指数 \(e^{-v/2}\) と \(v=2Y(t-a)\) を使った。
\(X=Y/\pi\) とすれば \(\Lambda(n)\le\log n\) のみで
\[
\sum_{n>X}\frac{\log n}{\sqrt n}\log(n/X)(n/X)^{-Y}
\le C\frac{\log Y}{Y^{3/2}}.
\tag{SH16}
\]
証明は \(X<n\le2X\) で \(r=n-X\) とし、各項を
\(C(\log X)X^{-3/2}r e^{-\pi r/2}\) で抑えて整数間隔1で和を取る。
\(n>2X\) は積分比較。定数は \(X\) が素数冪の直前か直後かによらない。
同じ側の和は \(O_m(B_Y^2Y^{-1}2^{-Y})|z|^2\)。
結局、全 polar・prime 項は
\[
O_m(B_Y^2\log Y/Y^{3/2})|z|^2
=O_m(\kappa_Y\log Y/\sqrt Y)|z|^2.
\tag{SH17}
\]

以上より、actual matrix を exact jet 座標へ移すと
\[
\boxed{Q(R_af_c)=2a\kappa_Y\,z^*H_Yz,\qquad
H_Y=H+O_m(a^{-1})\quad\text{in operator norm}.}
\tag{SH18}
\]
とくに大きい \(Y\) で \(c_m|z|^2\le z^*H_Yz\le C_m|z|^2\)。
これは個々の raw 列の絶対誤差ではなく、全 profile 空間での relative coercivity。
高次の boundary cancellation 後に prime/pole が主項へ昇格することは、固定 \(m\) の範囲ではこの評価が排除する。

## SH5. 最小固有方向と最小値：直接の有限次元証明

\(G(a)\to G_\infty=(\langle f_i,f_j\rangle)>0\)。正定値性は
\(\sum c_jf_j=0\Rightarrow[\sum c_j(-1)^jz^{2j}]\Xi(z)=0\Rightarrow c=0\)。
\(\eta=Y^{m-2}z\)、\(L_Y=Y^{2-m}T(Y)\) と置くと raw 係数は \(c=L_Y\eta\)。
(SH8) から
\[
L_Y\longrightarrow e_0\ell^*,\qquad
\ell_r=0\ (r<m),\quad \ell_m=(C^{-1})_{0m}=(-1)^m/2^m.
\tag{SH19}
\]
最後の等式は相異なる点 \(2,4,\ldots,2m+2\) の Lagrange weights：
\[
(C^{-1})_{jm}=\frac{m!}{\prod_{h\ne j}(d_j-d_h)}
=\frac{(-1)^{m-j}}{2^m}\binom mj.
\tag{SH20}
\]
したがって physical Gram は
\[
\widetilde G_Y=L_Y^*G(a)L_Y
\longrightarrow\|k\|_2^2\,4^{-m}e_me_m^*.
\tag{SH21}
\]
\(\widetilde G_Y\) は各有限 \(Y\) では正定値。
最小化する Rayleigh 商は exact に
\[
2a\kappa_YY^{4-2m}
\frac{\eta^*H_Y\eta}{\eta^*\widetilde G_Y\eta}.
\tag{SH22}
\]
\(H_Y>0\) を使って逆の商を取り、
\(H_Y^{-1/2}\widetilde G_YH_Y^{-1/2}\) の最大固有値を取る。
その極限は非零 rank-one 正行列で、唯一の正固有値は
\[
\lambda_* =\|k\|_2^2\,4^{-m}(H^{-1})_{mm}
=\frac{2\|k\|_2^2}{(m!)^2}.
\tag{SH23}
\]
従って大きい \(Y\) で最大固有値は単純、対応する original 最小固有値も単純。
(SH22)–(SH23) は (SH3) を与える。

定数と方向は次の elementary polynomial minimization で確認できる。
\(L_m(x)=e^x(m!)^{-1}D_x^m(e^{-x}x^m)\) とすると、部分積分により
\(\int_0^\infty e^{-x}L_m(x)x^r dx=0\) for \(r<m\)、
\(\int e^{-x}L_m^2dx=1\)。従って指定された最高係数
\(\eta_m=(-1)^m2^m/\|k\|_2\) に対する唯一の最小多項式は
\[
\sum_{r=0}^m\eta_r v^r=\frac{m!}{\|k\|_2}L_m(2v),\qquad
\eta^*H\eta=\frac{(m!)^2}{2\|k\|_2^2}.
\tag{SH24}
\]
最高係数を固定した monic polynomial の squared norm は
\((m!)^2/2^{2m+1}\) なので、逆 Gram entry は (SH23) の値。
有限次元固有射影の収束から \(\eta_Y\) は (SH24) の係数へ位相を除いて収束。
(SH8)、(SH20) に戻すと (SH4)、次いで (SH2) が従う。

切る前の最小関数を \(f_a^{\rm pre}=\sum_{j=0}^m c_j(a)f_j\) とすると、その失われた外側 tail の profile は
\[
\frac{Y^m f_a^{\rm pre}(a+v/(2Y))}{c_0(a)k(a)}
\longrightarrow m!L_m(2v)e^{-v}\qquad(v>0)
\tag{SH25}
\]
となる。零延長した \(u_{a,m}=R_af_a^{\rm pre}\) 自体は外側で零なので、その値と取り違えない。

## SH6. Exact Schur hierarchy と同時に運ぶ Gram

大きい \(Y\) で \(Q\) はこの有限 span 上正定値なので、逆順の Gram–Schmidt が一意にできる。
\[
\widetilde f_{j,Y}=f_j+\sum_{i>j}b_{ij}(Y)f_i,
\quad Q(R_a\widetilde f_{j,Y},R_af_i)=0\quad(i>j).
\tag{SH26}
\]
これは \(c_j=1\)、\(c_i=0\) for \(i<j\) の下での exact quadratic minimization。
\(q=m-j\) とし、block \(f_j,\ldots,f_m\) に SH2–SH4 を適用する。
jet の次数は \(0,\ldots,q\)、評価点は \(2j+2,2j+4,\ldots,2m+2\)。
最高逆行列係数は同じ \((-1)^q/2^q\)。
条件 \(c_j=1\) の下で正規化された limiting polynomial は
\(4^j q!L_q(2v)\)。従って
\[
b_{ij}(Y)\sim
\frac{(-1)^{i-j}\binom{m-j}{i-j}}{4^{i-j}Y^{2(i-j)}},
\tag{SH27}
\]
\[
\boxed{d_j(Y):=Q(R_a\widetilde f_{j,Y})
\sim a\kappa_Y\,16^j((m-j)!)^2Y^{6j+4-2m}.}
\tag{SH28}
\]
これは各 high block を消去した exact Schur pivot の漸近式。
導出で必要な全 prime/pole 余項は block ごとの jet 空間で (SH18) に従う。
raw 行列の粗い \(O(a^{-1})\) 誤差を小 pivot へ流用してはいない。

列 \(\widetilde f_j\) を raw \(f_i\) で表す下三角行列を \(U_Y\) とすると
\[
U_Y^*M U_Y=\operatorname{diag}(d_0,\ldots,d_m),\qquad
U_Y\to I,\qquad U_Y^*G(a)U_Y\to G_\infty.
\tag{SH29}
\]
**Gram も同時に合同変換している。** 一般化固有値問題の exact Schur は \(M-\mu G\) に対するもの。
(SH28) の \(d_j\) 自体を一般化固有値と同一視しない。

| \(m\) | \((d_0,\ldots,d_m)/(a\kappa_Y)\) の漸近 |
|---|---|
| 1 | \((Y^2,16Y^8)\) |
| 2 | \((4,16Y^6,256Y^{12})\) |
| 3 | \((36Y^{-2},64Y^4,256Y^{10},4096Y^{16})\) |

隣接 pivot の比は \(Y^6\) の尺度で分離する。
極限 profile の Laguerre orthogonality から来る hierarchy であり、素数を一個加える更新と同一であるとは主張しない。

## SH7. Γ-development を内部証明する

固定 compact 空間
\(S=\{c\in\mathbb C^{m+1}:c^*G_\infty c=1\}\) に通常の有限次元位相を入れる。
位相の自由度を除くにはその projective quotient を取る。追加の metric は設計しない。
\[
s_m(Y)=a\kappa_Y16^mY^{4m+4},\qquad \varepsilon=Y^{-6},
\]
\[
\mathcal F_Y(c)=\frac{c^*M c}{s_m(Y)c^*G(a)c}.
\tag{SH30}
\]
\(r=0,\ldots,m\) に対して、\(\varepsilon^{-r}\mathcal F_Y\) の Γ-limit は
\[
\mathcal F^{(r)}(c)=
\begin{cases}
\dfrac{(r!)^2}{16^r}|c_{m-r}|^2,
 &c_m=\cdots=c_{m-r+1}=0,\\
+\infty,&\text{otherwise}.
\end{cases}
\tag{SH31}
\]
\(r=0\) では上の制約は空。

**Liminf。** \(c_Y\to c\) とし \(b_Y=U_Y^{-1}c_Y\to c\)。
(SH28)–(SH29) によりエネルギーは正な対角項の和であり、
\(j>m-r\) の係数が極限で非零なら発散する。
そうでなければ \(j=m-r\) の項だけ残して (SH31) の下界を得る。
分母 \(c_Y^*G(a)c_Y\to1\)。

**Recovery。** 有限値を取る \(c\) に対し、\(b=c\)、\(c_Y=U_Yb\) とし、
最後に \(G_\infty\) norm で \(S\) へ戻す。
\(U_Y\to I\) なので \(c_Y\to c\)。高い \(b_j\) は exact に零、低い項は scale 比により消える。
これが (SH31) の値を与える。

\(S\) は compact なので minimizer の equicoercivity は自動。
\(r<m\) の各 limit minimum は0で、次の scale へ進む際の subtraction は0。
minimizer sets は順に最高 raw 成分を消す flag となり、最後に
\(c_1=\cdots=c_m=0\)、すなわち projective \(\operatorname{span}k\) が残る。
\(r=m\) は最後の最小値の係数 \((m!)^2/(16^m\|k\|_2^2)\) を与える。
これは通常の有限次元 Γ 証明であり、外部定理の名から選択を推論していない。

<a id="sh8-一様に正な-jet-形式への有限次元-transfer-lemma"></a>

## SH8. 一様に正な jet 形式への有限次元 transfer lemma

この節は条件付きの代数補題。別の realization \(\mathcal T_a\) について、同じ raw 固定基底の physical Gram を \(G_a^{\mathcal T}\) とする。
仮定は
\[
G_a^{\mathcal T}\to G_\infty>0,\qquad
Q(\mathcal T_af_c)=2a\kappa_Y z^*K_Yz,\qquad
b_-I\le K_Y\le b_+I,
\tag{SH32}
\]
ここで \(z=Wc\)、\(0<b_-\le b_+<\infty\) は固定 \(m\) に対して一様。
\(K_Y\) の極限の存在は仮定しない。

\(\eta=Y^{m-2}z\)、\(c=L_Y\eta\) とすれば
\(L_Y^*G_a^{\mathcal T}L_Y\to\|k\|_2^24^{-m}e_me_m^*\)。
逆 Rayleigh 商の行列を
\[
A_Y=K_Y^{-1/2}L_Y^*G_a^{\mathcal T}L_YK_Y^{-1/2}
\]
と置く。これは
\[
\|k\|_2^24^{-m}(K_Y^{-1/2}e_m)(K_Y^{-1/2}e_m)^*+o(1)
\tag{SH33}
\]
であり、\(o(1)\) は operator norm。
非零 rank-one eigenvalue は \(Y\) に一様に正で有界、残りは0なので、
大きい \(Y\) では \(A_Y\) の最大固有値は単純。
従って元の restricted minimum は単純である。

physical norm 1 の minimizer の \(\eta\) は一様有界である。
実際、\(\eta=e_m\) を適当に規格化した trial の quotient は有界で、
\(K_Y\ge b_-I\) だから最小点の \(|\eta|\) も有界。
(SH19) と規格化条件より、その raw 係数は位相を選べば
\(c\to e_0/\|k\|_2\)。よって、さらに各固定 \(j\) で
\(\mathcal T_af_j\to f_j\) in \(L^2\) なら physical 最小方向は \(k/\|k\|_2\) へ収束する。
これは \(K_Y\) が oscillate しても成り立つ。
最小 energy の Laguerre 定数は \(K_Y\to H\) の場合のもので、一般 \(K_Y\) には転用しない。

可変係数に対する Gram の一様性も明記する。
固定有限本の \(\mathcal T_af_j\to f_j\) から raw Gram は operator norm で収束する。
さらに \(L_Y\) は (SH19) により一様有界なので
\(L_Y^*(G_a^{\mathcal T}-G_\infty)L_Y\to0\)。
従って \(a\)-dependent jet vector を使うことによる未制御な Gram 誤差増幅はない。
正規化前の \(T(Y)\) 自体が大きくなり得ることと、\(L_Y=Y^{2-m}T(Y)\) の有界性は区別する。

例えば canonical \(P_NR_a\) の raw fixed-column convergence は \(N/a\to\infty\) で成り立つ。
証明は各 \(f_j\) を fixed compact smooth \(g\) で \(L^2\) 近似し、射影の contraction を使う。
\(a\) が \(\operatorname{supp}g\) を含めば Fourier 係数は \(\widehat g(\pi n/a)/\sqrt{2a}\)。
任意 \(r>1\) に対する \(|\widehat g(\omega)|\le C_r(1+|\omega|)^{-r}\) から
射影 tail は \(O_r((N/a)^{1-2r})\) となる。
ただしこの \(L^2\) convergence だけでは (SH32) の **形式** coercivity は出ない。
full realization への適用には、それを独立に証明する必要がある。

## SH9. 止める量化

各定数・開始窓 \(a_m\) は \(m\) に依存する。
\(m\to\infty\) の一様性、\(P_N\) を入れた行列、任意の cofinal path、全 \(H_a\) の ground 比較、prolate proxy、RH はこの証明の対象外。
得られたのは **全 fixed finite \(m\) の support-only hierarchical selection** である。

独立監査：DESTROYER は SH1–SH9 を読み、exact jet 基底・全 actual arithmetic 余項・一様 coercivity、逆 Rayleigh の rank-one metric、固定 \(m\) の Schur 定数、Γ liminf/recovery、oscillatory \(K_Y\) の transfer を独立に再計算し PASS とした。
行列 \(U_Y\) の三角方向は列規約に合わせ下三角と修正した。
これは内部数学の監査であり、原論文全体の再検証や full ground/RH の証明を意味しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/rate_history/notes/boundary_rate_analysis.md`](../../rate_history/notes/boundary_rate_analysis.md)
