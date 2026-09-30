**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/spiral-scale-prior-art.md` · Original SHA-256: `b18ec40fdd71e418bbfa129cf9b23c624f9a26ec2d38436c9f8770878b55d859`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Spiral / scale-flow / fractal strings: 一次文献と論理境界

調査日: 2026-09-29 (JST)。ユーザーの追加探索座標を、数学的な尺度作用・複素次元・保存量へ限定して照合した記録。物理添付・黄金比・DNA 等を証明前提にしない。新規性・RH 証明・文献の網羅性を主張しない。全資料について全文の独立検証は **NO**。以前の [support propagation 監査](support-propagation-prior-art.md) と [accumulation/spectrum 監査](../../../reports/research/notes/accumulation_spectrum.md) を再利用する。

## 1. 最初に区別する対象

\[
 x^{-s}=e^{-u/2}e^{-\alpha u}e^{-itu},
 \quad x=e^u,\ s=\tfrac12+\alpha+it
\]

は恒等式である。「すべての非自明零点に対応する残余 flow が pure rotation」は \(\alpha=0\) を同じ零点集合に要求するため RH の言い換えである。さらに **unitary 作用素のスペクトルは単位円上**であり、実スペクトルを持つのはその自己共役生成子である。零点を生成子の \(L^2\) 固有値・一般化スペクトル値・解析接続された resonance のどれに対応させるかを固定しない議論は無効。

## 2. Lapidus–Maier: D=1/2 では逆問題が失敗する

**一次原論文:** Michel L. Lapidus / Helmut Maier, *The Riemann Hypothesis and Inverse Spectral Problems for Fractal Strings*, JLMS (2) 52 (1995), 15–34, [DOI 10.1112/jlms/52.1.15](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/52.1.15)。査読公刊 **YES**。出版社 PDF は取得失敗。著者自身がアップロードした [原論文全文](https://www.researchgate.net/publication/236856082_The_Riemann_Hypothesis_and_Inverse_Spectral_Problems_for_Fractal_Strings) の §§2–3 を照合した。OCR の崩れがあるため、原著者の [2015 解説 v1](https://arxiv.org/pdf/1505.01548v1) の §6、Remark 13、Theorems 14–15 と併せて条件を確認した。

長さ列 \(\mathcal L=(\ell_j)\)、\(\ell_j>0,\sum_j\ell_j<\infty\) からなる一次元 fractal string を考える。周波数を \(n/\ell_j\) に正規化すると

\[
 N_\nu(x)=\sum_j\lfloor\ell_jx\rfloor,\quad
 W(x)=|\Omega|x,\quad N_{\mathcal L}(x)=\#\{j:\ell_j^{-1}\le x\}.
\]

固定 \(D\in(0,1)\) に対する **1995 年版の weak inverse problem** は、ある非零 \(C\) と \(\varepsilon>0\) について

\[
 N_\nu(x)=W(x)-Cx^D+
 O\!\left(\frac{x^D}{(\log x)^{1+\varepsilon}}\right)
\]

を満たすすべての該当 string が Minkowski measurable となるか、という命題。Dirichlet 条件では \(C>0\)。結論は適当な \(M>0\) による \(N_{\mathcal L}(x)\sim Mx^D\) と同値である。

**原著 Theorem 2.3** は \(\zeta(D+it)\ne0\) が全 \(t\in\mathbb R\) で成り立てば weak converse が成立すること、**Theorem 2.4** は逆向きを示す。したがって

\[
 (\mathrm{ISP}^{weak})_D
 \iff \zeta(s)\ne0\quad(\Re s=D).
\]

**\(D=1/2\)** では臨界線零点の存在によって逆問題が無条件に失敗する。全 \(D\in(0,1)\setminus\{1/2\}\) で成功するという命題が RH 同値である。任意の一個の self-similar string を調べる定理でも、全 fractal dimensions が \(1/2\) に制限される定理でもない。

**条件差:** 2015 解説 (27) は誤差 \(o(x^D)\) を掲げるが、Remark 13(b) はその改善を Titus Hilberdink の **未公刊**仕事に帰属させる。本ノートは1995年版の対数付き誤差を主たる照合済み statement とし、改善版を原著に読み込まない。RH 同値定理の成立は RH を仮定しないが、逆問題の全 \(D\ne1/2\) に対する真は未証明である。

## 3. Self-similarity は一般には非臨界の複素次元を生む

上と同じ周波数正規化では、絶対収束域 \(\Re s>1\) で

\[
 \zeta_\nu(s)=\zeta(s)\zeta_{\mathcal L}(s),
 \qquad \zeta_{\mathcal L}(s)=\sum_j\ell_j^s .
\]

geometry の振動が spectrum で見えなくなる機構は、幾何 zeta の pole と \(\zeta\) の zero の cancellation である。これが逆問題との接続であり、正値性保存則ではない。

Lapidus [2015 解説 §7、(33)–(37)](https://arxiv.org/pdf/1505.01548v1) の Cantor string は、長さ \(3^{-n-1}\) を重複度 \(2^n\) で持ち、

\[
 \zeta_{\rm CS}(s)=\frac{3^{-s}}{1-2\,3^{-s}},\quad
 \mathcal D_{\rm CS}=
 \left\{\frac{\log2}{\log3}+\frac{2\pi i k}{\log3}:k\in\mathbb Z\right\}.
\]

これは exact self-similarity と log-periodicity の具体例であるが、実部は \(1/2\) ではない。また \(\mathcal D_{\rm CS}\) は **幾何 zeta の poles** で、Riemann zeta の zeros ではない。どちらの集合も「spectrum」と呼んで同一視してはならない。2015 解説は本人の一次的解説資料として使用し、今回その公刊査読状況は追加確認していない。

## 4. Herichi–Lapidus の作用素版: normal と self-adjoint、quasi と full

Hafedh Herichi / Michel L. Lapidus, *Fractal Complex Dimensions, Riemann Hypothesis and Invertibility of the Spectral Operator*, [arXiv:1210.0882v3](https://arxiv.org/pdf/1210.0882v3)（2013-02-05）、Contemporary Mathematics 600 (2013)。公刊章、査読手続は今回未確認。著者による自らの作用素研究の解説であり、以下の定理は先行 memoir [HerLa1] に帰属される。

**Theorems 3.7, 3.9、Appendix B:** \(\mathcal H_c=L^2(\mathbb R,e^{-2cu}du)\) 上、所定の weighted Sobolev domain の \(\partial_c=d/du\) は normal、\(\partial_c^*=2c-\partial_c\)、\(\sigma(\partial_c)=c+i\mathbb R\)、point spectrum は空。\(V_c=(\partial_c-c)/i\) は自己共役。

**Theorems 3.15, 3.17:** \(\mathfrak a_c=\zeta(\partial_c)\) を functional calculus で定義すると、\(c\ne1\) で

\[
 \sigma(\mathfrak a_c)=
 \overline{\{\zeta(c+it):t\in\mathbb R\}}.
\]

平行移動和 \(\sum_{n\ge1}f(u-\log n)\) の有界作用素としての定理は \(c>1\)。critical strip への形式的代入でノルム収束・Euler 積・正値性を継承できない。

**Definition 5.3, Theorems 5.9, 6.1:** quasi-invertibility は「各高さ切断 \(T>0\) の \(\mathfrak a_c^{(T)}\) が可逆」という定義であり、\(\zeta\) の線 \(\Re s=c\) 上の非消滅と同値。これを全 \(c\in(0,1)\setminus\{1/2\}\) に要求すれば RH 同値。通常の有界逆作用素の存在は **Theorem 6.8** の \(0\notin\overline{\zeta(c+i\mathbb R)}\) であり、点ごとの非消滅より強い。切断は一般に有限次元行列ではない。

## 5. Dilation を厳密化しても ζ の同定は残る

Jean-François Burnol, *On some bound and scattering states associated with the cosine kernel*, [arXiv:0801.0530v2](https://arxiv.org/pdf/0801.0530v2)（2008）。今回査読公刊情報は未確認。

**Definition 5、Theorems 7–8、(13)–(16):** cosine kernel \(2\cos(2\pi xy)\)、cutoff \(a>0\)、\(u=\log a\) から Fredholm determinant による係数 \(\mu(u)\) を作り、\(s=1/2+iE\) に対して

\[
 (\partial_u+\mu)A=-EB,\qquad
 (\partial_u-\mu)B=EA .
\]

対応する自己共役 Dirac 作用素は
\[
 H_0=-i(x\,d/dx+1/2)
\]
の \(L^2(0,\infty;dx)\) 上の実現に unitary equivalent。Theorem 8 はそのスペクトル変換を明示する。これはユーザーの log-scale/dilation 座標と直接関連する厳密な先行例である。

しかし原著 **Introduction 最終段落**は、Riemann 零点を **exact に**生じさせる作用素を得る問題を扱わないと明記する。bound states の asymptotic density と ζ 零点集合の一致を混同しない。Sonine 評価ベクトルの完全性の限界は [既存監査](../../../reports/research/notes/accumulation_spectrum.md) の Burnol 2004 節も参照。

M. V. Berry / J. P. Keating, [*The Riemann Zeros and Eigenvalue Asymptotics*, SIAM Review 41 (1999), 236–266](https://epubs.siam.org/doi/10.1137/S0036144598347497) は、出版社 abstract の時点で未知の Hermitian operator と \(XP\) への提案を区別する。査読公刊 **YES**。今回この論文から証明定理を採用せず、数学的な spectral prior art の帰属のみを使用する。

## 6. Burnol の scattering causality 自体が RH 同値

Jean-François Burnol, *An adelic causality problem related to abelian L-functions*, J. Number Theory 87 (2001), 253–269、[最終稿 arXiv:math/0001013v3](https://arxiv.org/pdf/math/0001013v3)（2000-09-14）。査読公刊 **YES**。初稿も照合したが、本ノートの番号・条件は v3 に固定。

**Definitions 1.1, 1.4、Lemma 1.5、Theorem 1.7:** global field \(K\) の idele class group \(C_K\) 上で、Poisson–Tate map

\[
 E\varphi(v)=|v|^{1/2}\sum_{q\in K^\times}\varphi(qv)
 -|v|^{-1/2}\int_{\mathbb A_K}\varphi(x)\,dx
\]

と所定の support class \(S_{\le1}\) を用い \(D_+=E(S_{\le1})^\perp\)、\(D_-=E(\widetilde S_{\le1})^\perp\) を作る。incoming/outgoing の尺度不変性等は成立するが、causality

\[
 D_-\perp D_+
 \iff \text{全 abelian }L\text{-functions of }K\text{ の RH}
\]

が残る。v3 序論は \(\Re\rho>1/2\) の零点が、causal なら存在しないはずの scattering pole として現れることを説明する。**unitarity や双方向の尺度作用を持つことだけから causality を導いてはいない**。ζ に限る閉包問題は §2 の Nyman 型 criterion。全 abelian \(L\) の定理を「ζ のみ」と無断で量化変更しない。

## 7. 実スペクトルと複素共鳴は両立する

Maciej Zworski, [*Mathematical study of scattering resonances*, Bull. Math. Sci. 7 (2017), 1–85](https://link.springer.com/article/10.1007/s13373-017-0099-4)。査読公刊 **YES**。物理的解釈ではなく **§§2.1–2.2、Theorem 2、Definitions 1–2、(2.20)–(2.24)** の解析的定義を使用する。実有界 compact-support potential \(V\) に対して \(P_V=-\Delta+V\) は \(H^2\subset L^2(\mathbb R^3)\) 上自己共役。一方、resolvent の meromorphic continuation は \(L^2_{\rm comp}\to L^2_{\rm loc}\) という別の関数空間で行われ、その poles が resonances。§2.6 の complex scaling はそれを非自己共役作用素の固有値として実現する。したがって resonance を元の Hilbert 空間の固有値とみなし実数性を課す推論は成立しない。

Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068v1](https://arxiv.org/pdf/math/9811068v1)、Selecta Math. 5 (1999), 29–106、査読公刊 **YES**。**Abstract、§III Theorem 1 / Corollary 2、§VIII pp.44–47** で、critical zeros の absorption spectrum と hypothetical noncritical zeros の resonances を明確に分ける。§III の weighted quotient のスペクトル実現は臨界線零点に限り、重複度には \(\delta\) 制限がある。全零点を unitary generator の実スペクトルとして無条件捕捉する主張ではない。大域 trace criterion の体・近似射影の注意は既存台帳 ST-Connes1998GlobalCriterion を維持する。

## 8. Canonical-system 保存量を何に使えるか

Suzuki 2021/2026、Krein accelerant の条件は [support 監査 §§2–4](support-propagation-prior-art.md) に整理済み。特に Suzuki [1606.05726v3 Theorem 2.4](https://arxiv.org/html/1606.05726v3) の大域 determinant 非消滅と endpoint 条件を省略しない。

以下はその canonical equation からの直接計算であり、新定理ではない。\(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\)、実対称 \(H\)、\(Y'=-zJHY\) なら係数行列の trace は0なので、同一 \(z\) の fundamental matrix の determinant は保存される。これは **複素 \(z\)** に対しても成立する。一方、一つの解について

\[
 \frac d{du}(Y^*JY)=2i\,\Im z\,Y^*HY .
\]

よって \(H\ge0\)、解の可積分性、両端の boundary flux が等しいこと、積分 \(\int Y^*HY>0\) が揃えば \(\Im z=0\) を導ける。しかしそれは適切な自己共役境界条件を満たす状態についての機構であり、すべての ζ zeros がその状態を与えることは別義務である。determinant / Wronskian 保存だけから非実零点を排除できない。

## 9. 本探索への判定

| 候補 | 一次資料上の確かな構造 | 未解決・誤用防止 |
|---|---|---|
| pure rotational scale character | Mellin/log 座標と半密度 | 全 ζ zeros への要求は RH の言い換え |
| Lapidus–Maier inverse spectrum | geometry と frequencies の厳密対応 | 全 \(D\ne1/2\) の逆問題は RH 同値 |
| exact self-similarity | Cantor の complex dimensions と log-periodicity | poles と ζ zeros は別。実部 \(1/2\) を強制しない |
| \(\zeta(\partial_c)\) | normal functional calculus、切断可逆性 | normal≠self-adjoint、quasi≠full inverse |
| dilation / Dirac / Sonine | unitary identification、実スペクトル | ζ 全零点の exact identification は別 |
| scattering causality | Burnol の incoming/outgoing 構成 | 必要な直交性が RH 同値 |
| flux / Wronskian | 境界恒等式・determinant 保存 | 正計量・境界条件・ζとの同定が必要 |

今回の文献確認から、上の既知の同値条件より弱い、独立に証明済みの算術的保存則が全 ζ zeros の radial drift を禁止するとは結論できない。root / builder の具体的反例・global form の監査と分けた判定であり、未探索の全手法が不可能だとする主張ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/support-propagation-prior-art.md`](support-propagation-prior-art.md)
- [`research/notes/accumulation_spectrum.md`](../../../reports/research/notes/accumulation_spectrum.md)
