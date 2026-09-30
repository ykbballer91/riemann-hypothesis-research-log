**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_to_global/notes/semilocal_and_real_zero_theorems.md` · Original SHA-256: `af93adbc55b1118d8c1eff24cfced7aa59c89bd1df70af47001ed0e9da78e4a4`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Track B — Sonin stability と real-zero theorem の原典監査

2026-09-30。Local-to-Global Zero Confinement の限定監査。**RH OPEN。**
既知定理の適用条件を固定する作業であり、全証明の独立再証明・新規性・主 graph の進展は主張しない。
旧記録は読取のみ。本稿では素数集合 \(S\)、support 長 \(L\)、行列次数 \(N\) の三つの極限を区別する。

## B0. 版・参照位置

|一次資料|固定版と使用箇所|
|---|---|
|Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators: Semilocal adelic operators*|[2310.18423v2 HTML](https://arxiv.org/html/2310.18423v2)、[PDF](https://arxiv.org/pdf/2310.18423v2)、2024-05-04、30頁。§§4.1–4.8、特に Defs.4.4–4.5、Props.4.5–4.8、Thm.4.6、原稿 pp.20–24。刊行先 Ann. Funct. Anal. 15 (2024), article 87 は CvS 参考文献[9]とも一致。以下 CCM。|
|Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*|[2511.23257v1 HTML](https://arxiv.org/html/2511.23257v1)、[PDF](https://arxiv.org/pdf/2511.23257v1)、2025-11-28、26頁。§4 (6)、Remark 4.3 p.9、Thm.5.6 p.11、Thm.6.1 p.13、Appendix A pp.15–18。以下 CvS。|

頁は arXiv PDF の印刷頁（PDF page index + 1）。CCM HTML では一部 Proposition 番号が壊れるため PDF で照合した。
CCM は **Proposition 4.6** と **Theorem 4.6** が別に存在する。
CvS の精密版は Theorem 6.1。Introduction の Theorem 1.2 だけでは境界 distribution の情報が不十分である。

## B1. Sonin 空間の対象と support

\(S\ni\infty\) は有限集合、
\[
\mathbb A_S=\prod_{v\in S}\mathbb Q_v,\quad
\Gamma=\mathbb Q_S^\times
=\{\pm\prod_{p\in S\setminus\{\infty\}}p^{n_p}\},\quad
X_S=\mathbb A_S/\Gamma.
\]
\(C_S=\mathbb A_S^\times/\Gamma\)、\(K_S=\ker(|\cdot|_S:C_S\to\mathbb R_+^\times)\)。
使用 Hilbert sector は \(\mathcal H_S=L^2(X_S)^{K_S}\)。
加法 Fourier 変換 \(\mathbb F_S\) は、実成分 \(e^{2\pi ix}\) と
\(\mathbb Q_p/\mathbb Z_p\to\mathbb Q/\mathbb Z\to\mathbb T\) の積 character に対応する。
\[
\mathbf S_\lambda(X_S,\alpha)=
\{h\in\mathcal H_S:h=\mathbb F_Sh=0\text{ a.e. on }|x|_S<\lambda\}.
\tag{B1}
\]
archimedean 側は今回の写像の domain に合わせて
\[
\mathbf S_\lambda^\mathrm{ev}(\mathbb R)
=\{f\in L^2(\mathbb R)^\mathrm{ev}:f=\widehat f=0
\text{ a.e. on }(-\lambda,\lambda)\}.
\]
**これは関数と Fourier 変換の双方に原点周辺の穴を要求する条件。
双方を有限区間に support させる条件ではない。**
原著 Def.4.4 は一般 local \(L^2(\mathbb K)\) を定義するが、
Thm.4.6 の写像・証明は \(L^2(\mathbb R)^\mathrm{ev}\) を使う。
全 odd sector まで同型であるとは読み替えない。
[CCM §§4.1,4.5–4.6](https://arxiv.org/html/2310.18423v2#S4.SS5)。

## B2. \(\eta_S\)、\(\theta_S\) と保存する構造

\(\eta_S f\) は \((\otimes_{p\in S_f}1_{\mathbb Z_p})\otimes f\) の class。
一方 Sonin stability に使う写像は
\[
\epsilon_{p,n}=1_{\{|x|_p=p^n\}},\quad
\sigma_p=\epsilon_{p,0}-p^{-1}\epsilon_{p,1},\quad
\theta_S f=[(\otimes_{p\in S_f}\sigma_p)\otimes f],\quad S_f=S\setminus\{\infty\}.
\tag{B2}
\]
Prop.4.5 pp.20–21 は \(\mathbb Z_p^\times\)-不変
\(\mathbf S_1(\mathbb Q_p,e_p)\) が \(\sigma_p\) で生成され、
\(\mathbb F_{e_p}\sigma_p=\sigma_p\) とする。
Props.4.6–4.7 pp.21–23 と Thm.4.6 p.23 は
\[
\theta_S:\mathbf S_\lambda^\mathrm{ev}(\mathbb R)
\overset{\cong}{\longrightarrow}\mathbf S_\lambda(X_S,\alpha),\quad
\mathbb F_S\theta_S=\theta_S\mathbb F_\infty,\quad
\langle\theta_S f,\eta_S g\rangle=\langle f,g\rangle
\tag{B3}
\]
を与える。最後は \(\theta_S\) と \(\eta_S\) の **混合 pairing** であり、
\(\langle\theta_S f,\theta_S g\rangle=\langle f,g\rangle\) ではない。
[CCM §§4.6–4.7, (57)–(59)](https://arxiv.org/html/2310.18423v2#S4.SS7)。

Haar/Plancherel 定数を全 \(S\) で揃えた unitary Mellin 座標
\(U_S:\mathcal H_S\to L^2(\mathbb R,dt)\) を用いると
\[
U_S\theta_Sf=m_S\,U_\infty f,\qquad
m_S(t)=\prod_{p\in S_f}(1-p^{-1/2-it}). \tag{B4}
\]
原著 §3.1.4 p.10 では \(U_\infty=\pi^{-1/2}\mathbb F_\mu w_\infty\)、
§4.4 では \(U_S=\mathbb F_\mu w_S\) と記す。ここでは前者の unitary 規約に
合わせ、(B4) の両辺に同一の定数を用いる。raw Mellin 積分と unitary
Mellin 変換を定数なしに混同しない。この共通定数は multiplier を変えない。
従って直接計算により
\[
\|\theta_S f\|^2=\int_{\mathbb R}|m_S(t)|^2|U_\infty f(t)|^2dt,
\qquad
c_S\|f\|\le\|\theta_Sf\|\le C_S\|f\|,
\]
\[
c_S=\prod_{p\in S_f}(1-p^{-1/2}),\qquad
C_S=\prod_{p\in S_f}(1+p^{-1/2}). \tag{B5}
\]
これは各有限 \(S\) の bounded isomorphism。等長性ではない。
ambient \(L^2\) の inverse norm は実際に \(c_S^{-1}\)：
連続な multiplier は \(t=0\) で最小値 \(c_S\) を取るため essential infimum も同じ。
全素数への exhaustion では \(c_S\to0\) なので、**ambient map の inverse は一様有界でない**。
これは (B4) からの限定的な監査計算であり、
Sonin subspace に制限した全ての改善評価を反証したという主張ではない。

completed Mellin realization では
\[
E_S(t)=\prod_{v\in S}L_v(1/2+it),\qquad
\upsilon_S=E_SU_S,\qquad
\upsilon_S\theta_S=\upsilon_\infty. \tag{B6}
\]
Prop.4.8 p.24 は同じ entire-function vector space \(\mathcal B_\lambda\) を実現し、
その norm は
\[
\|F\|_S^2=\int_{\mathbb R}
\frac{|F(1/2+it)|^2}{|E_S(t)|^2}\,dt. \tag{B7}
\]
ここで \(F\) は (B6) の規格化であり、原著 (60) の raw completed Mellin
積分をそのまま \(F\) と呼ぶ場合は、対応する共通 Plancherel 定数を (B7) に補う。
したがって対応する **個別の entire function は同一で、既存の零点と重複度も保存される**。
新たにその零点を中心線へ移す定理ではなく、任意の \(\mathcal B_\lambda\) の元が
全て中心線零点だけを持つという意味でもない。
[CCM §4.8, (60)–(62)](https://arxiv.org/html/2310.18423v2#S4.SS8)。

## B3. spectrum と Weil positivity への過大な移送を排除

scaling の Mellin multiplier 表示の対応は使えるが、
Sonin の空間同型だけから、選択した prolate/Weil 作用素の同値性や ground state の対応は出ない。
実際、原著 **Remark 4.2(i), p.19** は
\[
N_S\eta_S\ne\eta_SN_\infty\quad(S\ne\{\infty\})
\]
を明記する。保存されるのは polynomial filtration であり、
\(S\) 依存 norm による orthogonalization は変わる。
同 remark (iii), (50) は \(|\cdot|_S^2\) との非可換性も示す。
これを \(\theta_S\) についての未記載の作用素定理へ勝手に拡張しない。
[CCM §4.3](https://arxiv.org/html/2310.18423v2#S4.SS3)。

特に保存済みでないものは、Weil form の同値な positive pairing、
ground-state gap、最小固有値の符号、prolate negative subspace と Sonin の誤差なし同定、
actual ξ への指定ベクトルの同定である。
「任意の相似で spectrum は変わる」とは主張しない。
必要な作用素 intertwining と domain の一致が別に成立すれば相似による spectrum 保存は通常通り成立する。
ここではその actual Weil/prolate の仮定が供給されていない。

なお原著 **Proposition 3.6, p.15** は、それとは別の正確な零点回収を与える：
\[
\mathbb F_\mu(\mathcal E(\psi_\ell^\pm))(s)
=R_\ell^\pm(s)\Xi(s).
\]
全 polynomial multiples が得られ、order \(\le1\) の entire functions の
Hadamard topological ring \(\mathcal H_{\le1}\) をその span の閉包で割ると、
\(s\) の乗算作用素の spectrum は \(\frac12+is\) が非自明 ζ 零点となる集合。
これは正の Hilbert 商上の自己共役実現ではなく、spectrum の実性を結論しない。
この命題文だけから spectral multiplicity まで断定しない。
[CCM §3.6, Proposition 3.6](https://arxiv.org/html/2310.18423v2#S3.SS6)。
また **Definition 2.2, p.6** の formal prolate operator
\(\omega(D,\xi,\lambda)=-D^2+\lambda^2N\) は、そこで domain を固定せず、
selfadjoint extension の選択を別問題として明記している。

## B4. CvS real-zero theorem の精密な全前件

\(\mathcal H=L^2([0,L],dx)\)、\(L>0\)。
\(U_n=L^{-1/2}e^{2\pi inx/L}\) を \([0,L]\) の外で零に延長する。
\(\mathcal D\) は \(C^\infty([0,L])\) 上の実 distribution、
\(f^*(x)=\overline{f(-x)}\) として三角多項式上で
\[
Q(f,g)=\mathcal D\big((f^*\ast g)(x)+(f^*\ast g)(-x)\big). \tag{B8}
\]
左右は区間上の smooth な関数として pairing する。
**Theorem 6.1, p.13 の前件**は次の全て：

1. (B8) がその三角多項式 domain 上で下に有界な本質的自己共役作用素を定める。
2. 自己共役 closure \(A\) の spectrum の最小点 \(a_0\) が固有値である。
3. \(a_0\) は isolated かつ simple。
4. 対応する非零固有関数 \(\xi\) が \(x\mapsto L-x\) に関して even。

結論は零延長の Fourier transform \(\widehat\xi\) の **全零点が実数**。
中心化のための平行移動は Fourier 側の非消滅指数因子なので零点に影響しない。
form closability や Friedrichs extension の存在だけを、前件1の operator-core 条件で置換しない。
simple なら反転固有値は ±1 のいずれかになるが、even はそのうち +1 を要求する追加条件。
[CvS §6, Theorem 6.1](https://arxiv.org/html/2511.23257v1#S6)。

**境界の重要な限定：** Remark 4.3 p.9 は最初から単なる
even distribution on \([-L,L]\) として扱うと情報が失われることを示す。
例 \(\mathcal D=\delta'_0\) は (B8) では非零 form を与えるが、
通常の smooth test 上の even symmetrization は零になる。
従って「translation-invariant な distribution kernel だから同じ定理が自動適用」としない。
[CvS §4.2, Remark 4.3](https://arxiv.org/html/2511.23257v1#S4.SS2)。

最小固有値 \(a_0\ge0\) は前件ではない。
\(\mathcal D\) への \(\delta_0\) の定数倍追加で \(A-a_0I\) にでき、固有ベクトルは変わらない。
したがってこの実零点定理は、元の **Weil form 自体の非負性**を証明するものではない。
これは一律に RH 同値な定理という分類も誤りであり、独立に成立する条件付き一般定理である。
actual arithmetic への前件検証と ξ への同定が未達。

## B5. 有限行列・固定窓・全窓

有限版 **Theorem 5.6, p.11** は
\[
q_{ii}=a_i,\quad q_{ij}=\frac{b_i-b_j}{i-j}\ (i\ne j),\quad
a_{-i}=a_i,\ b_{-i}=-b_i,\quad i,j=-N,\dots,N,
\tag{B9}
\]
という特定構造の実対称 PSD 行列と、one-dimensional even kernel を仮定する。
その kernel vector による (21) の polynomial と、対応する有限三角多項式の Fourier transform に実零点結論を与える。
任意の有限 PSD 行列に適用する定理ではない。
最小固有値を引けば PSD にはなるが、simple/even はそれでは証明されない。
[CvS §5, Theorem 5.6](https://arxiv.org/html/2511.23257v1#S5)。

原文で実行される §6 の極限は **固定 \(L\)、固定 \(A\) に対する \(N\to\infty\)**。
gap \(\delta>0\) と operator-core 近似 \(\eta_\epsilon\) を既に得た上で
\[
\|\xi-\xi_N\|\le\epsilon+\sqrt{\epsilon/\delta} \tag{B10}
\]
を導く（p.13、\(\xi_N=P_N\eta_\epsilon\) はこの段階では単位 norm とは限らない）。
これは genuine な条件付き収束評価だが、
\(\delta\) の \(S,L\) 一様下界や \(\epsilon\) と \(N,S,L\) の算術的関係を与えない。

直接 Cauchy–Schwarz で、中心化した support \([-L/2,L/2]\)、\(|\Im z|\le R\) に対して
\[
|\widehat f(z)-\widehat g(z)|
\le\sqrt L\,e^{RL/2}\|f-g\|_2. \tag{B11}
\]
固定 \(L\) ではこれが compact 一様収束を保証する。
\(L\to\infty\) にはこの評価の定数も管理する必要があり、
fixed-window convergence をそのまま全窓へ移せない。
別の weighted norm による改善を不可能と主張しているわけではない。

**Appendix A, pp.15–18** は有限 truncation の最小・最大固有値が単純でも、
極限で重複度2になる distribution の例を与える。
有限次数の simple/even 検査だけから極限の simple isolated ground state を推論しない。
CvS 本文には actual 全有限素数集合の (B8) について前件1–4を検証する定理はない。
有限素数集合は有限 Fourier 次数と異なり、残る archimedean/operator domain もある。
[CvS Appendix A](https://arxiv.org/html/2511.23257v1#A1)。

## B6. root 側の prolate–Hermite estimate との接続判定

root が別原典で照合している \(k_\lambda\to\Xi\) と prolate→Hermite 評価について、
本稿の2論文から得る追加評価は (B10) までである。
**正規化した true Weil ground state と、その明示的 \(k_\lambda\) の差の評価は取得できない。**
Sonin の (B6) は同一関数の二つの表示であり、その差を小さくする評価ではない。

実零点な ground-state transform を非零の \(\Xi\) へ locally uniformly 収束させれば、
Hurwitz は利用できる。しかし必要なのは全平面の収束とは限らず、
全非自明零点を含む開 strip \(|\Im z|<1/2\) の各 compact 上の収束でも零点排除には足りる。
その形に弱めても、上の missing ground-state approximation がこの2原典からは供給されない。

**判定：** Sonin stability と CvS real-zero theorem は有効な既知道具として KEEP。
それだけで finite prime construction→actual ξ の global confinement が閉じるという主張は REJECT。
新しい uniform arithmetic estimate 0、RH OPEN。別論文の Lemma 7.2/7.3 を本稿が独立監査済みとはしない。
