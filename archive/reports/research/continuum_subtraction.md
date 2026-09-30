**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/continuum_subtraction.md` · Original SHA-256: `7addbc84dc0d59d69ff42dcb187e3b89cbd1c9633e4c494a7d95e7cbe8a24148`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 標準Gaussianの和−積分補正：収束の修復と正値性の境界

2026-09-29。内部構築 cycle 22。**補正近似は有効、そこからの正値性伝播は棄却。RH未証明。**
最新論文の証明追跡ではなく、前巡で発散した整数和を第一原理から組み直した。
Gaussian・整数格子・完成関数の規約を固定し、連続密度の積分だけを差し引く。
任意のcounterterm、RHを前提とする補正、物理資料の主張は使わない。

## 1. 候補と、独立に成立する収束

\(D=\partial_t\)、\(L=-D^2+1/4\) とし、実数 \(x>0\) について

\[
v_x(t)=e^{t/2}e^{-\pi x^2e^{2t}},\qquad
\phi_x=(D^2-1/4)v_x
=e^{t/2}(4\pi^2x^4e^{4t}-6\pi x^2e^{2t})e^{-\pi x^2e^{2t}}.
\]

実Riemann核は \(\Phi=\sum_{n\ge1}\phi_n\)、
\(\int_{\mathbb R}\Phi(t)e^{izt}dt=\xi(1/2+iz)\)。自然な部分和は全実線で
\(L^2\) 収束しないことを [前巡](selfdual_theta_boundary.md) で証明した。
今回の補正は

\[
q_N=\sum_{n=1}^Nv_n-\int_0^Nv_x\,dx,\quad U_N=-2q_N,\qquad
R_N=\frac12LU_N
=\sum_{n=1}^N\phi_n+2\pi N^3e^{5t/2}e^{-\pi N^2e^{2t}}. \tag{1}
\]

最後の等号は \(\phi_x=\partial_x[-2\pi x^3e^{5t/2}e^{-\pi x^2e^{2t}}]\)
の直接積分。密度1の整数格子と同じ区間 \([0,N]\) を使う補正である。
全ての自然な補正の中で唯一だとは主張しない。

単位区間ごとの部分積分から

\[
q_N(t)=\int_0^N\{x\}\partial_xv_x(t)dx,\qquad
U_N(t)=4\pi e^{5t/2}\int_0^Nx\{x\}e^{-\pi x^2e^{2t}}dx. \tag{2}
\]

従って \(0<U_N\uparrow U\)。Poissonの恒等式で

\[
U(t)=2\cosh(t/2)-\Psi(t),\qquad
\Psi(t)=e^{t/2}\sum_{n\in\mathbb Z}e^{-\pi n^2e^{2t}},\qquad LU=2\Phi.
\]

\(U\) は正の偶関数で \(U(t)\sim e^{-|t|/2}\)。また

\[
0\le U-U_N\le2e^{t/2}e^{-\pi N^2e^{2t}}. \tag{3}
\]

これは一様収束と \(L^1\) 収束も与える。例えば右辺のsupは
\(\sqrt2\pi^{-1/4}e^{-1/4}N^{-1/2}\)。ただし正のprimitiveから
正のsourceは従わない。全ての固定 \(N\) で

\[
R_N(t)=-\pi N(3N+1)e^{5t/2}+O_N(e^{9t/2})\quad(t\to-\infty). \tag{4}
\]

さらに、全ての整数 \(k\ge0\) について強い収束が成立する。
\(v=v_1,\ k_0=\phi_1,\ P_2(D)=(D-3/2)(D-1/2)\) とすると

\[
\begin{aligned}
\|U-U_N-N^{-1/2}v(\cdot+\log N)\|_{H^k}
&\le\frac{N^{-3/2}}6\|P_2(D)v\|_{H^k},\\
\|R_N-\Phi-\tfrac12N^{-1/2}k_0(\cdot+\log N)\|_{H^k}
&\le\frac{N^{-3/2}}{12}\|P_2(D)k_0\|_{H^k}. \tag{5}
\end{aligned}
\]

証明は各単位区間の厳密な台形誤差

\[
\int_N^\infty f_xdx-\sum_{n>N}f_n
=\tfrac12f_N-\tfrac12\int_N^\infty\{x\}(1-\{x\})\partial_x^2f_xdx
\]

と \(f_x=x^{-1/2}f_1(\cdot+\log x)\) を使う。
\(\|\partial_x^2f_x\|_{H^k}=x^{-5/2}\|P_2(D)f_1\|_{H^k}\)、
\(\{x\}(1-\{x\})\le1/4\) より定数も得られる。
台形公式はまず有限上端で適用し、和−積分の差をまとめて極限へ通す。
二階微分を含む剰余の \(x\)-積分はBochner積分として絶対収束するので、
そこで極限・\(t\)-微分を交換できる。左辺の和と積分は、まず各 \(t\) で差を取る。
生の \(\int_N^\infty f_xdx\) は \(H^k\) の絶対Bochner積分ではない。
特に \(f=v\) の生のtailは \(L^2\) にも属さない。元の無補正級数や
この生のtailに対して同じ交換をしたわけではない。
従って \(\sqrt N\|R_N-\Phi\|_{H^k}\to\|k_0\|_{H^k}/2>0\)。
発散した前巡の近似を修復しているが、零点の結論は含まない。

## 2. 正の増分は実在するが、別の核である

\(y=e^{2t}\)、\(\rho(r)=\{\sqrt{r/\pi}\}\) と置くと

\[
V_N(y):=\frac{U_N((\log y)/2)}{2y^{5/4}}
=\int_0^{\pi N^2}\rho(r)e^{-yr}dr. \tag{6}
\]

これは完全単調関数で、\(y_j>0\) に対して

\[
\sum_{i,j}c_i\overline{c_j}V_N(y_i+y_j)
=\int_0^{\pi N^2}\rho(r)\left|\sum_i c_i e^{-y_i r}\right|^2dr\ge0. \tag{7}
\]

\(N\to N+1\) の増分も同じ積分の新しい区間だけであり、厳密に正。
全 \(N\) は一つの \(L^2((0,\infty),\rho(r)dr)\) における制限で、極限も存在する。
これは任意の正測度について成り立つLaplace型Gram恒等式である。
一方、Weil／\(K_\Phi\) の正値性と (7) を同定する恒等式は得られていない。
以下では、この単調性を微分後のエネルギーや実際の \(K\) に移す候補を検査する。

## 3. 自然なresolvent energyは最初の段階で減少する

\[
\mathcal E_N=\langle U_N,LU_N\rangle
=\int_{\mathbb R}(|U_N'|^2+|U_N|^2/4)dt\ge0.
\]

Gaussian積分だけで

\[
\langle v_x,Lv_y\rangle=\frac{3x^2y^2}{2(x^2+y^2)^{5/2}},
\]

従って

\[
\mathcal E_N=
6\sum_{n,m\le N}\frac{n^2m^2}{(n^2+m^2)^{5/2}}
-4N^3\sum_{n\le N}\frac1{(n^2+N^2)^{3/2}}+\sqrt2N. \tag{8}
\]

\(\int_0^N\|v_x\|_{H^1}dx=2\sqrt N\|v_1\|_{H^1}<\infty\) なので、
\(x=0\) 自体に \(H^1\) ベクトルを定義する必要はなく、有限区間積分は絶対Bochner積分。
上の二重energy核も可積分で、\(x\ge\epsilon\) からの \(H^1\) 極限でも正当化できる。

特に

\[
\mathcal E_1=\frac3{2\sqrt2},\qquad
\mathcal E_2=\frac{17}{4\sqrt2}-\frac{112}{25\sqrt5},\qquad
\boxed{\mathcal E_2-\mathcal E_1
=\frac{11}{4\sqrt2}-\frac{112}{25\sqrt5}<0.} \tag{9}
\]

符号は正量同士を平方した整数比較 \(378125<401408\) で厳密。
数値は約 \(-0.0589732595768\)。一般 \(N\) の減少性は主張しない。
正で単調に増える \(U_N\) から、このenergyの正増分を導く案は終了。

## 4. actual corrected kernel のGram反例は全Nで成立

\(Z_N(s)=\sum_{n\le N}n^{-s}\) とし、\(R_N\) の完成変換を計算する：

\[
B_N(s):=\int_{\mathbb R}R_N(t)e^{(s-1/2)t}dt
=\pi^{-s/2}\Gamma(1+s/2)
\left[(s-1)Z_N(s)+N^{1-s}\right]. \tag{10}
\]

積分の正則域は \(\Re s>-2\)。先に \(0<\Re s<1\) でGaussian Mellin積分と
部分積分を用い、その後はこの半平面へ正則延長する。
一般には右辺の有理型接続は整関数ではないので、有限近似に整関数の定理を適用しない。

元の \(R_N\) は偶関数でない。最も直接の対称化
\(\eta_N(t)=(R_N(t)+R_N(-t))/2\) に対して

\[
F_N(z)=\int\eta_N(t)e^{izt}dt
=\tfrac12[B_N(s)+B_N(1-s)],\qquad s=1/2+iz,
\]

は \(|\Im z|<5/2\) で正則。そのまま微分すると

\[
\begin{gathered}
B_N(0)=0,\quad B_N(1)=1/2,\quad F_N(i/2)=1/4,\\
a_N:=B_N'(0)=N+\log N!-N\log N\ge1,\\
B_N'(1)=\frac{1+H_N-\log N}{2}-\frac{\gamma+\log(4\pi)}4
\le1-\frac{\gamma+\log(4\pi)}4. \tag{11}
\end{gathered}
\]

ここで \(H_N\) は調和数。\(a_{N+1}-a_N=1-N\log(1+1/N)>0\)、
\(H_N\le1+\log N\) が上の不等式を与える。

実偶関数 \(\eta\) の核とその二重Fourier変換は、正値性を前提とせず

\[
K_\eta(a,b)=\frac12\int_{|(a+b)/2|}^{\infty}
y\eta(y+(a-b)/2)\eta(y-(a-b)/2)dy,
\]
\[
\iint e^{iza-i\bar wb}K_\eta(a,b)\,da\,db
=D_F(w,z):=\frac{F(z)F'(\bar w)-F'(z)F(\bar w)}{4(z-\bar w)}. \tag{12}
\]

この恒等式は変数変換とFubiniによる（以前の接続計算と同じ規約）。
(4) により \(|\eta_N(t)|\le C_Ne^{-5|t|/2}\)。従って
\(|K_{\eta_N}(a,b)|\le C'_N(1+a^2+b^2)e^{-(5/2)(|a|+|b|)}\) であり、
(12) の積分は \(|\Im z|,|\Im w|<5/2\) で絶対収束する。

\(z=w=i/2\) を代入すると

\[
\boxed{D_{F_N}(i/2,i/2)
=\frac{B_N'(1)-B_N'(0)}{16}
\le-\frac{\gamma+\log(4\pi)}{64}<0.} \tag{13}
\]

\(N=1\) で等号、約 \(-0.0485662486230\)。正値核ならcompactに切断した
\(e^{-a/2}\) の二次形式も非負となるはずだが、支配収束で (13) に収束する。
従って実際の有限補正核に負方向があり、全 \(N\) のPSD伝播候補は反証された。
\(\xi\) 自身の反例ではない。

同じ失敗は零点でも見える：
\(B_N(-1)=-\pi N\)、\(B_N(2)=(Z_N(2)+1/N)/\pi\le2/\pi\) より
\([B_N(s)+B_N(1-s)]/2\) は実区間 \((-1,0)\) に零点を持つ。
これは**通常の臨界帯の外の、有限近似だけの零点**。RHの線外零点とは呼ばない。

## 5. どの極限が失敗したか

(5) の全 \(H^k\) 収束と (13) は矛盾しない。指数重みを持つ評価はその位相で連続でない：

\[
F_N(i/2)=1/4\quad\hbox{for every }N,
\qquad F_\Phi(i/2)=\xi(0)=1/2. \tag{14}
\]

片側の \(B_N\) は \(\Re s>0\) のcompact上で \(\xi\) に収束するが、
対称化には \(s\) と \(1-s\) の両方が必要で、確保される域は \(0<\Re s<1\)。
そこでの局所一様収束を境界 \(s=0,1\) へ拡張しない。
負方向の極限から actual \(K_\Phi\) の負方向を結論することもできない。

## 6. 構成後の既知性照合・判定

導出後、[DLMF 25.2.8](https://dlmf.nist.gov/25.2.E8) の小数部分による
ζの和−積分表示、[25.2.9](https://dlmf.nist.gov/25.2.E9) の
Euler–Maclaurin補正と周期Bernoulli剰余に照合した。
この補正原理は既知。今回の具体的なenergy差・負Gram式の掲載先は網羅調査しておらず、
独立導出を新規性の主張に置き換えない。外部RH proof claimは使っていない。

|候補|独立検査の結果|RHへの扱い|
|---|---|---|
|連続密度の補正で全実線収束を修復する|全 \(H^k\)、鋭い率 \(N^{-1/2}\) を証明|RHを使わない補助恒等式|
|共通の正測度上の制限として正増分を得る|Laplace核 (7) で成立|Weil／\(K_\Phi\) との同定なし|
|\(U_N\) の順序から自然なenergyの正増分を得る|最初の増分 (9) が厳密に負|棄却|
|補正後の有限核でGram PSDを伝播する|全 \(N\) に厳密な負方向 (13)|棄却|
|全Sobolev収束から指数重み付き評価を移す|端点値 (14) が異なる|棄却|

BUILDERは (5) とMellin域、LITERATURE担当は (2)、(7)、(8)〜(9) を内部導出。
DESTROYERは (11)〜(13) と積分域をROOTと独立検算した。
[検算スクリプト](../../../artifacts/experiments/scripts/continuum_subtraction_checks.py)は有理計算、Arb192bitの
符号包含、独立な有限区間積分を区別する。最後の積分は非認証sanity check。
解析証明・全称の評価は本ノートにあり、Lean形式化はしていない。

**本補正を正値性伝播の手段とする候補は終了。**
近似の次数、\(N\)、数値精度の増加を続けない。別の補正全般の不可能性は主張しない。
主RHグラフ合流0、追加採用仮定0。収束の修復をRH証明距離の短縮とは記録しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/scripts/continuum_subtraction_checks.py`](../../../artifacts/experiments/scripts/continuum_subtraction_checks.py)
- [`research/selfdual_theta_boundary.md`](selfdual_theta_boundary.md)
