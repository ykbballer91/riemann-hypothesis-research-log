**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase4/notes/arakelov_height.md` · Original SHA-256: `50f9583f7c1418e41f833fc3f5e68188bdd3f22596a8fd65129b5787bf36bafb`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase IV — Arakelov 交点形式と Néron–Tate 高さの限定監査

2026-09-29。BUILDER。Phase III、canonical state、theorem graph は変更しない。新規性を主張しない。対象は既知の算術的正値性を actual ζ-zero space へ移せるかという一つの比較であり、Arakelov 理論全体の不可能性を論じない。

**結論:** 有限素点と無限素点を含む真正の算術 pairing と adjoint は存在する。しかし最も直接的な対象 \(\operatorname{Spec}\mathbf Z\) では
\(\widehat{\operatorname{CH}}^1\simeq\mathbf R\)、その次数ゼロ部分は0である。算術**曲面**の次数ゼロ divisor/height theorem をこの対象へ移す候補は、適用次元と quotient の時点で停止する。曲線の Jacobian を追加すれば正の Néron–Tate 空間を得るが、同じ空間が ζ の全零点を担うという同定は得られない。

## AH1. 内部計算: Spec Z の有限・無限素点を一緒に残す

\[
\widehat{\operatorname{Div}}(\mathbf Z)
=\Bigl(\bigoplus_p\mathbf Z[p]\Bigr)\oplus\mathbf R[\infty],\qquad
D=\sum_pn_p[p]+a[\infty]
\]

とする。有限素点の和は有限 support。ここで \(a\) は metric の logarithm の規約であり、Gillet–Soulé の Green 成分 \(g=-\log\|s\|^2\) とは \(a=g/2\) の関係にある。

\[
\widehat{\deg}D=\sum_pn_p\log p+a,
\qquad
\widehat{\operatorname{div}}(r)
=\sum_pv_p(r)[p]-\log|r|[\infty]\quad(r\in\mathbf Q^\times). \tag{AH1}
\]

\(r=\pm\prod_pp^{v_p(r)}\) なので \(\widehat{\deg}\widehat{\operatorname{div}}(r)=0\)。有限素点を消すか infinity を捨てるとこの等式は失われる。

任意の \(D\) について \(r=\prod_pp^{n_p}\) を選べば

\[
D-\widehat{\operatorname{div}}(r)
=\bigl(a+\sum_pn_p\log p\bigr)[\infty]. \tag{AH2}
\]

したがって

\[
\widehat{\operatorname{CH}}^1(\operatorname{Spec}\mathbf Z)
=\widehat{\operatorname{Div}}(\mathbf Z)/
\widehat{\operatorname{div}}(\mathbf Q^\times)
\xrightarrow[\widehat{\deg}]{\ \sim\ }\mathbf R,
\qquad \widehat{\operatorname{CH}}^1{}^{\!0}=0. \tag{AH3}
\]

これは計算の後で一次原典 [GS, §3.4.3, 印刷 p.131] と照合した。同節はこの同型を明記する。

**Test space / topology / completion / kernel.** 有限因子群を離散位相、\(a\) を通常の実位相とする。写像
\((\{n_p\},a)\mapsto(\{n_p\},a+\sum n_p\log p)\) は同相で、主因子部分群を \((\bigoplus_p\mathbf Z)\times\{0\}\) へ送る。従って quotient topology も通常の \(\mathbf R\)。次数ゼロの quotient は文字通り零空間であり、Hausdorff completion を取っても mode は増えない。real finite coefficients を使うなら、対応する実主因子 span を割っても同じ計算となる。この後者を、係数・位相を指定しない単なる tensor 記号で置き換えない。

例えば正の形式 \(B(D,E)=\widehat{\deg}D\,\widehat{\deg}E\) を quotient 上に置くことはできる。しかし rank は1で、degree-zero 部分上では0。これは平方を手で導入したもので、算術 Hodge index の divisor self-intersection ではない。

## AH2. 次元による最小の不適合

Gillet–Soulé の numerical intersection は、\(X\) の絶対次元を \(d+1\) とすると codimension の和が \(d+1\) のとき

\[
\widehat{\operatorname{CH}}^p(X)\times
\widehat{\operatorname{CH}}^q(X)\longrightarrow\mathbf R,
\qquad p+q=d+1
\]

を与える。[GS, §§4.3.1–4.3.2, 5.1.4]。

* 数体上の曲線 \(C/K\) の regular proper flat model \(\mathcal C/\mathcal O_K\) は相対次元1、絶対次元2。ここでは divisor×divisor が数値となる。
* \(\operatorname{Spec}\mathbf Z\) は絶対次元1、相対次元0。codimension1×1 は対象次数を超える。通常の算術 Chow 定義では \(\widehat{\operatorname{CH}}^2(\operatorname{Spec}\mathbf Z)=0\)：codimension2 cycle はなく、複素 fibre は点なので該当 \((1,1)\)-current もない。非零な degree は codimension1 の線形不変量である。

従って「Spec Z は算術曲線だから、算術曲面の divisor Hodge index がそのまま ζ のための正の pairing を与える」は不成立。算術曲線と、数体上の曲線を generic fibre に持つ算術曲面を取り違えている。ここに未知の ζ 零点を入力していない。

## AH3. 実際の有限・無限局所 pairing と符号

正規化を曖昧にしないため、この段落は \(K=\mathbf Q\) とし、smooth projective geometrically connected \(C/\mathbf Q\)、\(J=\operatorname{Jac}(C)\) を固定する。\(D,E\) は次数0の divisors、support は互いに disjoint とする。

各素数 \(p\) で regular model に horizontal closure \(\mathcal D,\mathcal E\) を取り、vertical \(\mathbf Q\)-divisor \(V_p(D)\) を

\[
(\mathcal D+V_p(D),Y)_p=0
\quad\text{for every vertical divisor }Y
\]

となるように補正する。補正は whole fibre の倍を除いて一意で、その不定性は generic degree0 との交差では消える。

\[
\langle D,E\rangle_p
=(\mathcal D+V_p(D),\mathcal E+V_p(E))_p. \tag{AH4}
\]

交差数には \(\log\#k(P)\) を掛ける。任意の固定 \(D,E\) では有限個の bad/intersection primes 以外は0である。個々の局所 pairing を PSD とは主張しない。

無限素点では \(C(\mathbf C)\) 上の degree-zero Green function \(g_E\) を用い、

\[
\langle D,E\rangle_\infty=\sum_Pn_Pg_E(P).
\]

ここで \(g_{\operatorname{div}f}=-\log|f|+\text{constant}\) の規約を採る。GS の squared-norm Green function なら右辺に \(1/2\) が付く。degree0 により Green function の加法定数は消える。全素点の共通の規約は

\[
\langle D,\operatorname{div}f\rangle_v=-\log|f(D)|_v.
\]

積公式からその全局所和は0になるので、**global** pairing が divisor class に降りる。個々の局所 pairing は一般に linear equivalence に不変ではない。

\(\vartheta\) を symmetric theta class とし、二次形式 \(q_L=\hat h_L\) と bilinear form を

\[
B_L(P,Q)=\tfrac12(q_L(P+Q)-q_L(P)-q_L(Q)),
\qquad B_L(P,P)=q_L(P)
\]

で固定すると、Faltings–Hriljac の正規化は

\[
B_{2\vartheta}([D],[E])
=-\sum_{v\le\infty}\langle D,E\rangle_v. \tag{AH5}
\]

この exact convention は [BHM, §§2, 3.1, 4.1, Thm 4.1] で確認した。\(\vartheta\) と \(2\vartheta\)、\(g\) と \(2g\)、height とその bilinear polarization のいずれかを変更すると係数が変わる。一般数体では residue norm と全 Archimedean embedding の重み、および absolute height の \([K:\mathbf Q]^{-1}\) を一貫して扱う必要がある。このノートはそれを暗黙に省いて一般 \(K\) の同じ数値式を主張しない。

## AH4. 正値性の出所、primitive 条件、radical

正の形式は \(-\)intersection、または同値な canonical height である。全 arithmetic divisor space 上の intersection を正定値とはしない。

Moriwaki [M, Thm B, pp.1–2] の正確な射程は regular projective flat arithmetic variety \(X\) と arithmetically ample hermitian \(\bar H\)、相対次元 \(d\ge1\) であり、generic primitive 条件

\[
\deg\bigl(z(x)|_{X_K}\cdot H_K^{d-1}\bigr)=0
\]

の下で

\[
\widehat{\deg}(x^2\widehat c_1(\bar H)^{d-1})\le0. \tag{AH6}
\]

この定理の算術 class \(x\) に対する等号条件は、Stein base \(f':X\to\operatorname{Spec}\mathcal O_K\) から \(nx=f'^*y\) となる \(n>0,y\) が存在すること。したがって full arithmetic class の radical を「torsion だけ」とは呼べない。base metric/constants の pullback が含まれる。相対次元1が Faltings–Hriljac の場合であることを [M, p.4, Theorem1.1 の証明冒頭] が明示する。算術 Chow の primitive 条件 \(L^d x=0\) による strict negativity は [M, Thm A] の別の主張であり、generic degree0 と同じ条件として扱わない。

Jacobians の height 側では \(J(K)_{\rm tors}\) を割り、Mordell–Weil theorem と canonical-height positivity により

\[
V_J=(J(K)/J(K)_{\rm tors})\otimes_\mathbf Z\mathbf R
\]

は有限次元 Euclidean space になる。positivity は ample symmetric line bundle の height を \(4^{-n}h_L([2^n]P)\) で正準化し、bounded height の点の有限性を使う既知の算術定理に由来する。RH は使わない。fixed \(K\) と固定 \(J\) の高さ0の点は torsion だが、arithmetic divisor の lift には前述の base radical が残る。

completion はこの有限次元空間では既に完了している。任意の \(J(\overline K)\) 全体や無限 family へ拡大し、completion と trace を持ち込む操作は、この fixed-field theorem の結論ではない。

## AH5. 得られる arithmetic adjoint と、得られない Frobenius

真正の adjoint relation は存在する。cycle level では、適用条件を満たす proper maps の pullback/pushforward に対して projection formula

\[
\langle f^*x,y\rangle=\langle x,f_*y\rangle
\]

がある。[GS, Thm 4.3.9; §4.4.3]。これを無限次元 Hilbert adjoint と直ちに同一視せず、arithmetical class の同じ intersection pairing に対する等式として読む。

height 側でも、\(A/K\)、symmetric ample \(L\)、\(f\in\operatorname{End}_K A\) が
\(f^*L\simeq L^{\otimes d}\) を満たせば、通常の height functoriality の bounded error を canonical limit で消して

\[
q_L(fP)=d\,q_L(P),\qquad B_L(fP,fQ)=d\,B_L(P,Q),
\quad f^*_{B_L}f=dI\text{ on }V_A. \tag{AH7}
\]

を得る。最後はこの有限次元正の空間における adjoint である。例えば全 abelian variety の \([m]\) は \(d=m^2\) を満たす。より一般に polarization \(\lambda_L\) の Rosati involution \(f^\dagger=\lambda_L^{-1}f^\vee\lambda_L\) があり、\(\lambda_{f^*L}=f^\vee\lambda_L f=d\lambda_L\) から \(f^\dagger f=[d]\)。これは finite-field role の「同じ算術対象上の正の構造と scaling」の真正の部分類似である。[AV, I §§11,14]。

しかし \(V_A\) の eigenvalues は \(A(K)\) の endomorphism の固有値であり、ζ の零点と同定されていない。\([m]/m=I\) の normalized isometry は全 prime-power trace を生成しない。各 reduction の Frobenius は各有限体 fibre の作用であって、標準的な共通 \(\operatorname{End}_K A\) の作用として自動的に持ち上がるわけではない。\(\mathbf Z\) 上の \(x\mapsto x^p\) は加法を保たず、characteristic-zero Frobenius を定義しない。

## AH6. finite-field role mapping と actual-ζ gate

| 有限体での役割 | 今回得られる算術的構造 | 判定 |
|---|---|---|
| 正の polarization / Rosati | fixed Jacobian の height、primitive intersection の符号反転 | **EXACT な局所類似**。別の対象の既知正値性 |
| adjoint と scale | projection formula、polarized endomorphism の (AH7) | **EXACT な部分構造**。ζ を担う作用への同定なし |
| finite places | finite intersection multiplicity × \(\log N\mathfrak p\) | **EXACT**。自動的に \(\Lambda(n)/\sqrt n\) の全 comb にはならない |
| infinity | Hermitian metric、Green function、加法定数の degree0 cancellation | **EXACT**。\(\Gamma_\mathbf R(s)\) の全因子・spectral tower との同定なし |
| poles / degree0 restriction | generic degree、base pullback、torsion の除去 | **PARTIAL な形の類似**。ζ の極 \(s=0,1\) の除去と同じ map とは未証明 |
| 全 zeros を担う同じ spectrum | Spec Z の degree0 quotient は0、fixed \(V_J\) は有限次元 | この具体的候補には **ABSENT** |
| trace/determinant と Euler 積の一致 | この height theorem からは出ない | **ABSENT** |

Spec Z の非自明 zero spectrum を得るには、(AH3) の degree-zero space とは異なる arithmetic complex/quotient を定義し、その正の pairing と actual explicit formula を同時に比較する必要がある。単に Hilbert space を増設する、ζ 零点を添字にする、必要な Weil positivity を仮定する、という操作は独立な算術入力にならない。

**最小 missing bridge:** 素数と infinity から定義した test-space map が (i) 主因子/metric radical と ζ 側の quotient を正しく対応させ、(ii) 全零点を失わない trace identity を保ち、(iii) Weil form を実際の \(-\)primitive intersection に一致させること。今回はその map を構成できない。条件 (iii) と全面的な positivity をそのまま仮説にすれば既知の RH criterion を言い換えるだけになる。この bridge の存在全体が RH と同値である、という逆含意は主張しない。

**Kill decision:** `STOP — DIMENSION / QUOTIENT / ACTUAL-ZETA IDENTIFICATION FAIL`。具体的な Spec Z primitive-height 移植は (AH3) と AH2 で棄却。Néron–Tate positivity、Arakelov theory、別の arithmetic-cohomology program 全般は棄却していない。新しい RH 補題は0。この bounded comparison 後に一般例を追加して回さない。

## AH7. 原典、locators、確認の境界

1. **[GS]** H. Gillet and C. Soulé, *Arithmetic intersection theory*, Publ. Math. IHÉS **72** (1990), 93–174, [原文 PDF](https://www.numdam.org/item/10.1007/BF02699132.pdf)。§3.4.3 p.131（Spec Z の degree 同型、metric の1/2）、§4.3.2 pp.147–151（intersection）、§4.3.8(v), Thm4.3.9 p.152（finite/infinite sum・projection）、§5.1.4 pp.166–167（次数条件）。p.131 を PDF rendering でも確認。SHA256 `fa663fadd299576dcaaa5ba54efd10cf6a7f52ae02ff53d787956816b92f169f`。
2. **[M]** A. Moriwaki, *Hodge index theorem for arithmetic cycles of codimension one*, [arXiv:alg-geom/9403011v4](https://arxiv.org/pdf/alg-geom/9403011v4), 15 March 1994。Thm A p.1、Thm B/1.1 p.2、Lemma1.1.1 p.3（Archimedean Dirichlet energy の負符号）、d=1 の FH 帰着 p.4。p.2 を画像照合。SHA256 `d15f1e52ff183e7bb3d7b6778f2f1f12f6942484f95a047abe316753aa222af5`。この原論文は一般化の一次資料であり、FH の元証明そのものではない。
3. **[BHM]** R. van Bommel, D. Holmes, J. S. Müller, *Explicit arithmetic intersection theory and computation of Néron–Tate heights*, [arXiv:1809.06791v2](https://arxiv.org/html/1809.06791v2), §§2, 3.1, 4.1, Thm4.1。実装・計算法を与える一次論文の明示規約を採用。計算法の論文を RH 証明資料とは扱わない。
4. **[AV]** J. S. Milne, *Abelian Varieties*, [著者講義 PDF](https://www.jmilne.org/math/CourseNotes/AV.pdf), I §§11,14（polarization と Rosati）、II の arithmetic 部分。講義の全証明を新たに検証したという主張ではない。
5. **FH 原出典の取得制約:** G. Faltings, *Calculus on arithmetic surfaces*, Ann. Math. **119** (1984), 387–424, [公式書誌](https://annals.math.princeton.edu/1984/119-2/p04), DOI10.2307/2007043；P. Hriljac, *Heights and Arakelov's intersection theory*, Amer. J. Math. **107** (1985), 23–38, [出版社/JSTOR](https://www.jstor.org/stable/2374455), DOI10.2307/2374455。今回元版本文の取得は失敗した。従って元版の未読 theorem 番号を推測して引用せず、FH の正確な式・scope は上記 [M] と [BHM] の該当箇所で確認した。このアクセス制約を元定理の欠陥とは扱わない。

取得 PDF は一時領域で読み取りに使用。恒久編集は本ノートだけ。原論文全体・高次算術 standard conjectures・無限次元 completion の一般定理を検証済みとはしない。
