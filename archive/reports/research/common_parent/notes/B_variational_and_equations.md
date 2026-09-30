**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/common_parent/notes/B_variational_and_equations.md` · Original SHA-256: `500a498c6a8e841882fe54fd5f0d7e52a6d58a050b9e7ab563ad44768e441b7f`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# B の正確な構成と A/B の変分方程式

2026-09-30、COMMON PARENT VARIATIONAL Track B。RH OPEN。指定された既存の算術写像と二つの作用素を比較する限定監査であり、新しい共通親を定義して正しさを作る作業ではない。旧ファイルは読取のみ。

## B0. 結論・一次資料

CCM §7 の \(h_\lambda\) は prolate の第0・第4モードを積分ゼロにする組合せ、\(k_\lambda\) はその算術和である。**\(h_\lambda\) は concentration ground でも prolate 固有関数でもない。自然な even・積分ゼロ制約の concentration 問題でも停留点ではない。** \(k_\lambda\) が Weil ground だという定理も原典にはなく、§8 はその比較を未解決とする。

正当な引き戻し \(QW_\lambda(B_\lambda h)\) は定義できるが、計量は \(G_\lambda=B_\lambda^*B_\lambda\) となる。これは元の \(L^2(dx)\) 計量ではなく、concentration operator とも可換でない。以下はこれらを実際の式で確認する。

|一次資料|確認箇所・取得範囲|
|---|---|
|Connes–Consani–Moscovici, *Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1), 2025-11-27|§3 (3.19)–(3.20), Props.3.3–3.4, Thm.3.6；§7 (7.1)–(7.12), Lemmas7.1–7.3、§8。今回 HTML 原文を再確認。|
|D. Slepian–H. O. Pollak, *Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty—I*, BSTJ40 (1961),43–63|[原論文の大学公開 scan](https://www.math.ucdavis.edu/~saito/data/ONR15/PSWF-I.pdf)／[DOI](https://doi.org/10.1002/j.1538-7305.1961.tb03976.x)。§III (8)–(11) p.45、§4.3 pp.54–56 の最大化、§V (23)–(27) pp.57–58、§VI pp.59–62 の非退化・順序の証明を確認。SHA256 `0d2cf92b5e1ce6f9894e93d765c2fd1a9a3b6d33c57d540cbc2b4a19d6f20ecd`。|
|H. J. Landau–H. O. Pollak, *同—II*, BSTJ40 (1961),65–84|[原論文 scan](https://www.math.ucdavis.edu/~saito/data/ONR15/PSWF-II.pdf)／[DOI](https://doi.org/10.1002/j.1538-7305.1961.tb03977.x)。§I p.68 の定理、§II Thm.1 pp.71–72 の least-angle 証明、§III Thm.2 pp.74–77 の extremizer を確認。SHA256 `e0919b2dd9917f4ec8591fe240582a8fd335027a1d4b186fb444f5d0b3c7d4b2`。|

1961 年 scan は text layer がないため OCR と必要な原頁画像を併用した。OCR に崩れた不等号は画像で確認した。原論文全内容を再検証したとはしない。旧 [local-to-global ノート](../../local_to_global/notes/spectral_approximants_and_exact_gap.md) の \(\Xi/4\) 規格化・Gaussian tail 補足・ground 比較未解決の結論を再利用し、再発見と数えない。

## B1. 実験で再現すべき B の式

Fourier を \(\mathcal Ff(y)=\int_\mathbb R f(x)e^{2\pi ixy}dx\)、\(\lambda>1\) と固定する。
\[
P_\lambda=1_{[-\lambda,\lambda]},\quad
T_\lambda=P_\lambda\mathcal FP_\lambda,\quad
C_\lambda=T_\lambda^*T_\lambda
=P_\lambda\mathcal F^{-1}P_\lambda\mathcal FP_\lambda.
\tag{B.1}
\]
\(C_\lambda\) は time-limited 空間上で
\[
(C_\lambda f)(x)=\int_{-\lambda}^{\lambda}
\frac{\sin(2\pi\lambda(x-y))}{\pi(x-y)}f(y)dy.
\tag{B.2}
\]
原典 I の時間長 \(T=2\lambda\)、angular bandwidth \(\Omega=2\pi\lambda\) なので、その \(c=\Omega T/2\) は
\[
c=2\pi\lambda^2. \tag{B.3}
\]

CCM (7.5) は
\[
PW_\lambda=-\partial_x[(\lambda^2-x^2)\partial_x]+(2\pi\lambda x)^2.
\]
\(x=\lambda y\) とすると正確に
\[
\mathscr P_c=-\partial_y[(1-y^2)\partial_y]+c^2y^2,
\qquad -1<y<1. \tag{B.4}
\]
regular endpoint の自己共役実現を用いる。形式領域は、\(L^2\)、局所絶対連続、\(\sqrt{1-y^2}\,f'\in L^2\) という weighted Sobolev 領域で、対応する固有関数は両端で regular。対数特異解を境界条件なしに加えない。

その実固有関数を \(\psi_{j,\lambda}\)、固有値を \(d_j\) とし、通常の次数で数える。\(d_0<d_1<\cdots\)。同じ関数が \(C_\lambda\) の固有関数で、
\[
1>\kappa_0>\kappa_1>\cdots>0,\qquad
T_\lambda\psi_j=\tau_j\psi_j,\quad
\tau_{2m}=(-1)^m\sqrt{\kappa_{2m}}.
\tag{B.5}
\]
\(C\) の固有値 \(\kappa_j\)、有限 Fourier の固有値 \(\tau_j\)、微分作用素の固有値 \(d_j\) を区別する。原典 I §VI は integral eigenvalues の非退化を endpoint identity と Sturm–Liouville 非退化から証明し、\(c\downarrow0\) からの連続性で順序を固定する。

\(I_j=\int_{-\lambda}^{\lambda}\psi_j(x)dx\) と置く。\(I_0\ne0\) で、CCM の直線は
\[
h_\lambda\ \propto\ I_0\psi_4-I_4\psi_0
\ \propto\ \psi_4-\frac{I_4}{I_0}\psi_0.
\tag{B.6}
\]
\(I_j=\tau_j\psi_j(0)\) により、係数は有限 Fourier の固有値と原点値からも計算できる。二つの \(\psi_j\) を別々の非零定数で変更しても、最初の式は全体スカラーしか変わらない。

Hermite 正規化に合わせた \(h_{0,\lambda},h_{4,\lambda}\) を使う場合、一つの便利な選択は
\[
h_\lambda=\frac{\sqrt3}{2^{11/4}}
\left(h_{4,\lambda}-\frac{I_4}{I_0}h_{0,\lambda}\right).
\tag{B.7}
\]
CCM (7.10)–(7.11) に現れる Meixner–Schäfke の \(\operatorname{ps}_j\) 規約では、同論文の漸近係数を解くと
\[
h_{j,\lambda}(x)=\sqrt{\frac{2j+1}{2\lambda}}
\operatorname{ps}_j(x/\lambda;c^2),\qquad j=0,4.
\tag{B.8}
\]
すなわち原文の \(c_j\lambda^{-1/2}\operatorname{ps}_j\) の定数は \(c_0=1/\sqrt2,c_4=3/\sqrt2\)。数値 library の angular normalization と同一だと仮定せず、各 mode を \(L^2[-\lambda,\lambda]\) 単位化・原点で正にしてから (B.6) を使えば、方向・Rayleigh 比はこの曖昧さに依存しない。

極限は CCM (7.4) の
\[
h=\frac{\sqrt3}{2^{11/4}}h_4-\frac3{2^{17/4}}h_0
=\frac\pi2x^2(2\pi x^2-3)e^{-\pi x^2},\qquad
\|h\|_2=\frac{\sqrt{33}}{2^{17/4}}.
\tag{B.9}
\]
印刷されたこの \(h\)、\(du/u\)、\(\mathcal E\) の組合せでは Fourier 画像の極限は \(\Xi/4\)。\(4h\) に変更すれば \(\Xi\) になる。この既確認スカラー差は Rayleigh 比に影響しない。

最後に \(h_\lambda\) を \([-\lambda,\lambda]\) 外で零に延長し、
\[
k_\lambda(u)=\sqrt u\sum_{1\le m\le\lfloor\lambda/u\rfloor}h_\lambda(mu),
\quad \lambda^{-1}\le u\le\lambda;
\qquad k_\lambda=0\quad\text{outside}.
\tag{B.10}
\]
有限和の cutoff と外側の multiplicative cutoff は両方必要。端点の平均値の選択は \(L^2\)・積分値を変えない。

### B1.1 有限 \(\lambda\) で勝手に偶化しない

全実線 Fourier 自己双対は compact support の非零関数には成立しない。CCM §7 の記述は、実験に使う零延長関数については、後続の有限 Fourier 固有式 \(T_\lambda h_j=\tau_jh_j\) と区別して読む必要がある。特に \(\tau_0>\tau_4>0\) なので、(B.7) について
\[
h_\lambda(0)=\frac{\sqrt3}{2^{11/4}}h_{4,\lambda}(0)
\left(1-\frac{\tau_4}{\tau_0}\right)\ne0,
\qquad\int h_\lambda=0.
\tag{B.11}
\]
極限 \(h\) の \(h(0)=\widehat h(0)=0\)、\(\widehat h=h\) から導く Poisson symmetry の証明を有限 \(h_\lambda\) に流用しない。従って \(k_\lambda(u)=k_\lambda(1/u)\) を入力条件にしない。

また \(h_\lambda(\lambda)\ne0\) なら \(u=\lambda/m\) の内点に jump がある。\(\lambda^2\) が一般の非整数なら、これらの点は反転後の \(m/\lambda\) と一致しないため、対応する jump は inversion symmetry を直接破る。全 \(\lambda\) で端点値が非零とまでは主張しない。実験では full \(k_\lambda\) を用い、even projection は別の trial vector として区別する。

## B2. 本当に成立する集中度変分原理と非適用証明

time-limited \(f\) に対する集中度は
\[
\mathcal R_C(f)=\frac{\|P_\lambda\mathcal Ff\|_2^2}{\|f\|_2^2}
=\frac{\langle f,C_\lambda f\rangle}{\langle f,f\rangle}.
\tag{B.12}
\]
最大値は \(\kappa_0\)、最大化関数は \(\psi_0\) の非零スカラー倍に限る。Euler 方程式は \(Cf=\kappa f\)。同じ \(\psi_0\) は \(PW_\lambda\) の最小固有値の関数である。Landau–Pollak の時間・周波数二つの割合を固定した問題も、基本となる extremal pair は第0 bandlimited mode とその time restriction であり、第0・第4 mode の積分ゼロ混合ではない（II, Thm.1；Thm.2 の equality formula (12)）。

(B.6) の両係数は非零。ここで全 even index \(j\) に \(I_j\ne0\) であることを確認する。regular even ODE 解は \(\psi_j'(0)=0\) であり、\(\psi_j(0)=0\) なら ODE の一意性から零解となる。さらに \(T_\lambda\) は injective：compact-supported 入力の Fourier 画像が区間で零なら entire identity から入力は零。従って \(\tau_j\ne0\) であり、\(I_j=\tau_j\psi_j(0)\ne0\)。

**積分ゼロ制約でも停留点ではない。**
\[
S_0=\{f\in L^2[-\lambda,\lambda]^{\rm even}:\langle1,f\rangle=0\}.
\]
この空間で (B.12) の停留点なら、ある実 \(r\) と複素 \(\eta\) に対し
\[
Ch= r h+\eta1. \tag{B.13}
\]
\(h=I_0\psi_4-I_4\psi_0\) として \(\psi_2\) との内積を取ると、左辺と \(rh\) は零、\(I_2\ne0\) だから \(\eta=0\)。次に \(\psi_0,\psi_4\) 成分を比較すると \(r=\kappa_0=\kappa_4\) が必要で、厳密な固有値順序に矛盾する。

もし \(\overline{\operatorname{span}}\{\psi_0,\psi_4,\psi_8,\ldots\}\) という finite-Fourier positive branch に候補を制限しても、制約の representer は \(1\) のこの空間への射影であり、\(\psi_8\) 成分が非零。同じ証明が使える。\(PW\) の制約最小化も \(\kappa_j\) を \(d_j\) に変えれば同様。

\(\operatorname{span}\{\psi_0,\psi_4\}\cap S_0\) だけを domain にすれば一次元であり、(B.6) はどんな Rayleigh 商にも自動的に stationary になる。それはこの直線を選んだ理由を説明する変分原理ではない。**ここで排除したのは上記の具体的な集中度・prolate 変分同定であって、未知の別の作用素・制約をすべて排除したのではない。**

実際に満たす微分方程式は、二つの固有方程式から得る
\[
(PW_\lambda-d_0)(PW_\lambda-d_4)h_\lambda=0
\tag{B.12a}
\]
という四階方程式である。例えば \(h=I_0\psi_4-I_4\psi_0\) なら
\((PW_\lambda-d_0)h=I_0(d_4-d_0)\psi_4\ne0\)。
同様に \((C-\kappa_0)(C-\kappa_4)h=0\)。これは二モード span の性質で、\(h\) が二階 ground equation を満たすことや四階形式の一意な ground であることを意味しない。

## B3. A の Euler 方程式は算術項を含む別の式

\(Y_\lambda=L^2(I_\lambda,du/u)\)、\(I_\lambda=[\lambda^{-1},\lambda]\)、\(\widehat k(t)=\int k(u)u^{-it}du/u\) とする。実際の Weil form は CCM (3.19) の
\[
q_\lambda(k)=\frac1{2\pi}\int_{\mathbb R}2\theta'(t)|\widehat k(t)|^2dt
+2\Re\{\widehat k(i/2)\overline{\widehat k(-i/2)}\}
-\sum_{1<n\le\lambda^2}\Lambda(n)\langle k,T(n)k\rangle,
\tag{B.14}
\]
\[
\theta(t)=-\frac t2\log\pi+\Im\log\Gamma(1/4+it/2),\quad
\langle f,T(n)g\rangle=n^{-1/2}\{(f^**g)(n)+(f^**g)(n^{-1})\}.
\]
polar と有限 prime-power 項を省かない。この閉・下半有界形式の自然な領域は
\[
\mathcal D_\lambda=\left\{k\in Y_\lambda:
\int\log(2+|t|)|\widehat k(t)|^2dt<\infty\right\}.
\tag{B.15}
\]
残りの項が固定窓で有界で、archimedean symbol が \(\log(2+|t|)+O(1)\) であるためである。対応する自己共役作用素を \(A_\lambda\) とすると ground の弱 Euler 式は
\[
q_\lambda(v,\xi_\lambda)=e_0\langle v,\xi_\lambda\rangle_{Y_\lambda}
\quad(\forall v\in\mathcal D_\lambda).
\tag{B.16}
\]
固定窓での作用素・離散 spectrum の存在は CCM §3 の入力。ground の simplicity/evenness と \(k_\lambda\) との一様比較は §8 が残した条件である。

有限 \(k_\lambda\) は piecewise smooth/BV なので、log 座標での Fourier 変換は \(O(1/|t|)\) となり (B.15) に属する。従って Rayleigh 挿入は正当である。ただし内点 jump を無視して周期 \(H^1\) 誤差評価を使うことはできない。作用素残差 \(A_\lambda k\) を使う場合は、その強い domain を別に確認する。形式残差なら (B.16) の双対で定義できる。

## B4. 算術写像の canonical pullback と inherited metric

偶関数を正の半直線へ制限して、ここだけ source を \(X_\lambda=L^2((0,\lambda),dx)\) とする。全 even \(L^2[-\lambda,\lambda]\) 計量はその二倍なので、全区間規約に戻すと source adjoint には \(1/2\) が掛かる。以下では半区間規約を一貫して用いる。

\[
(B_\lambda h)(u)=\sqrt u\sum_{m\le\lambda/u}h(mu),\quad u\in I_\lambda.
\tag{B.17}
\]
各 summand の作用素 norm は高々 \(m^{-1/2}\) なので
\[
\|B_\lambda\|\le\sum_{m\le\lambda^2}m^{-1/2}<\infty.
\]
変数変換 \(x=nu\) から adjoint と metric を直接得る：
\[
(B_\lambda^*k)(x)=\sum_{n\le\lambda x}\frac{k(x/n)}{\sqrt{nx}},
\qquad 0<x<\lambda,
\tag{B.18}
\]
\[
(G_\lambda h)(x)=(B_\lambda^*B_\lambda h)(x)
=\sum_{n\le\lambda x}\frac1n\sum_{m\le\lambda n/x}h(mx/n).
\tag{B.19}
\]
\(G\) は有理数比の dilation と multiplicity を含む。\(G\ne I\)。特に \((0,\lambda^{-1})\) に support を持つ全関数は \(\ker B\) に入る。

逆に \(B\) は \(Y\) 上 onto である。bounded な有限 Möbius right inverse は
\[
(J_\lambda k)(x)=
\begin{cases}
\displaystyle\sum_{m\le\lambda/x}\mu(m)\frac{k(mx)}{\sqrt{mx}},
&\lambda^{-1}\le x\le\lambda,\\
0,&0<x<\lambda^{-1}.
\end{cases}
\tag{B.20}
\]
有限二重和を \(r=mn\) でまとめ、\(\sum_{m\mid r}\mu(m)=1_{r=1}\) を用いると \(BJ=I_Y\)。積分ゼロを source に要求しても、\(\ker B\) 内の小区間関数を足して積分を調整できるので onto のままである。

引き戻しの正確な domain は
\[
\mathcal D_B=\{h\in X_\lambda:B_\lambda h\in\mathcal D_\lambda\},
\quad q_B(v,h)=q_\lambda(Bv,Bh),\quad
g_B(v,h)=\langle Bv,Bh\rangle=\langle v,Gh\rangle.
\tag{B.21}
\]
十分大きい定数を足した \(A_\lambda+c\ge0\) に対し、
\(\|h\|_X^2+\|(A_\lambda+c)^{1/2}Bh\|_Y^2\) という graph norm で pullback は閉じる。密度は \(h=(h-JBh)+JBh\) と分解し、最初の項が \(\ker B\)、第二項の \(Bh\) を \(\mathcal D_\lambda\) 内で近似することで従う。勝手に \(G\) を恒等計量に交換しない。

\(Bh\ne0\) の Rayleigh 商の Euler 式は
\[
q_\lambda(Bv,Bh)=r\langle Bv,Bh\rangle
\quad(\forall v\in\mathcal D_B).
\tag{B.22}
\]
強い domain では \(B^*A_\lambda Bh=rGh\)。onto 性により (B.22) は **\(A_\lambda Bh=rBh\) と同じ方程式**であり、\(PW h=d h\) や \(Ch=\kappa h\) へ変わったわけではない。\(X/\ker B\) を \(g_B\) で扱えば target と等長同定されるが、それは元の Weil 問題の正確な書き換えに留まる。

自然な写像の関係は次の図式で尽くされる：
\[
\begin{array}{ccc}
(X_\lambda,\langle\ ,\ \rangle_{dx};\ PW,C)
&\xrightarrow{\quad B_\lambda\quad}&
(Y_\lambda,\langle\ ,\ \rangle_{du/u};\ A_\lambda)\\
\big\downarrow\scriptstyle{\text{metric pullback}}&&\big\Vert\\
(X_\lambda/\ker B_\lambda,g_B;q_B)
&\xrightarrow{\quad\text{isometry}\quad}&
(Y_\lambda,\langle\ ,\ \rangle_{du/u};q_\lambda).
\end{array}
\]
下段は exact。同じ矢印が上段の \(PW\) または \(C\) と \(A_\lambda\) を intertwine する等式は得られていない。下段の等長性を上段の計量に戻して使うことが誤った同一視となる。

## B5. 比較を阻む二つの計算可能な defect

### B5.1 inherited metric は concentration と可換でない

半区間の even concentration operator を \(C^{\rm ev}\) とする。その kernel は (B.2) の \(K(x-y)+K(x+y)\) である。非零 \(h\in C_c^\infty(0,\lambda^{-1})\) を取ると \(Gh=0\)。一方 \(C^{\rm ev}h\) は区間内で analytic かつ非零（\(C\) の injectivity）。

\(\max(\lambda/2,\lambda^{-1})<u<\lambda\) では算術和の項は \(m=1\) だけなので
\[
B(C^{\rm ev}h)(u)=\sqrt u(C^{\rm ev}h)(u).
\]
analytic な非零関数はこの開区間全体で零になれない。従って \(BC^{\rm ev}h\ne0\)、\(GC^{\rm ev}h\ne0\)、
\[
[G,C^{\rm ev}]h\ne0. \tag{B.23}
\]
これは actual finite arithmetic summation による metric defect であり、抽象的に「別の norm だから違う」と言っただけではない。

同じ witness は \(C^{\rm ev}\ker B\not\subset\ker B\) も示す。従って source 全体で \(\widetilde C B=BC^{\rm ev}\) を満たす target の線形作用素 \(\widetilde C\) は存在しない：左辺はこの \(h\) に対して零、右辺は非零である。これは **指定された \(B\) による concentration operator の descent** の不可能性に限る。

### B5.2 最も直接な form 同一視も kernel で破綻する

同じ小区間 support の \(h\ne0\) について
\[
q_\lambda(Bh)=\|Bh\|^2=0,\qquad
\langle h,(I-C^{\rm ev})h\rangle
\ge(1-\kappa_0)\|h\|^2>0.
\]
従って natural source space 全体で
\[
q_\lambda(Bh)=a_\lambda\langle h,(I-C^{\rm ev})h\rangle
+b_\lambda\|Bh\|^2
\tag{B.24}
\]
という単純な affine identity を主張すれば \(a_\lambda\ne0\) では反例となる。小区間内で \(\int h=0\) ともできる。\(PW\) の正の energy への同一視も同じ witness で破綻する。

これは別の制約・quotient・追加算術項を備えた全ての可能な共通親の不存在定理ではない。そのような候補を採用するなら、消える kernel、source metric、全 polar/prime 項、境界 domain を含む新たな exact identity が必要になる。本ノートではその identity を発見していない。

## B6. 停止判断

現時点で B に厳密に付いている構造は「二つの prolate mode の積分ゼロ直線」と「その有限算術和」、および既知の \(\Xi/4\) への strip 収束である。concentration の最大化や constrained minimum を B の既証明性質として使うことはできない。

root の actual Rayleigh 挿入は (B.14) による別の有効な診断であるが、有限値・小さい値だけで \(k_\lambda\) の ground 最適性や一様 gap を証明しない。今回の exact pullback は A を書き換えるだけで、prolate Euler equation との一致を供給しなかった。**この比較から新しい RH 非依存の共通変分親は得られない。ここで限定探索を停止する。**

独立読取監査：DESTROYER は B2 の \(\psi_2/\psi_8\) による非停留点証明、B4 の adjoint・metric・有限 Möbius right inverse・domain 密度、B5 の kernel witness・非可換性・affine leakage identity の限定反証を独立に再計算し PASS とした。原論文全体の独立監査を意味しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/local_to_global/notes/spectral_approximants_and_exact_gap.md`](../../local_to_global/notes/spectral_approximants_and_exact_gap.md)
