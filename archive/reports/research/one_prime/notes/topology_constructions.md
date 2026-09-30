**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/one_prime/notes/topology_constructions.md` · Original SHA-256: `473bc807c4d70bbdfb904c5dbb5b45be3b6cacab5edb18a15eb970b6daed6b01`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# One-prime return：商の順序・補間・自然な解析位相の限定監査

2026-09-29、real interpolation と \(X_1\) の整理を 09-30 に追記。対象は素数 \(p=2\)。既存ファイル、Phase III / IV、主状態を変更しない。本ノートの重みは**診断用**であり、未知の算術計量を採用したものではない。新規性・RH の進展は主張しない。

**結論。** 同じ seminorm を使う限り、商を先に取っても完備化後の商と等長に一致し、dense-range collapse を回避できない。指数重みの complex / real \((\theta,2)\) interpolation は指数成長と Mellin 評価保持の両方を同じ率で弱める。劣指数重みは反復の指数成長を消すが、off-axis 評価を bounded dual から外す。他方、同巡の算術空間監査では、標準 seminorm から全零点評価を保持する具体的 Banach 完備化 \(X_1\) を構成済みである（OT7.1）。未構成なのは、**その全零点保持と両方向 subexponential return を同時に満たす**算術的な estimate / topology である。

## OT1. 算術表現と解析上の診断空間

\(L=\log2\)、半密度座標 \(\phi(t)=e^{t/2}f(e^t)\) を固定する。normalized return は
\[
 (T\phi)(t)=\phi(t-L),\qquad
 \ell_\lambda(\phi)=\int_{\mathbb R}\phi(t)e^{\lambda t}\,dt,
 \quad \lambda=\rho-\tfrac12=\alpha+i\gamma.
\]
従って
\[
 \ell_\lambda(T^n\phi)=2^{n\lambda}\ell_\lambda(\phi),
 \qquad n\in\mathbb Z.                                        \tag{1}
\]

算術 test space \(\mathscr S\) は全指数重みと全導関数で急減する空間、\(\mathscr R\) は actual adelic summation range の trivial compact-character sector とする。ここでの \(E=\mathscr S/\mathscr R\) は必要なら Hausdorff 化を行う記法である。元の高速減衰位相での range closure と、弱い Hilbert norm での closure を同一視しない。

CCM07 の (4.20)、Definitions 4.10 / 4.14、Proposition 4.13、(4.41)–(4.45) により、全非自明零点の (1) は指定位相の商双対に残る。半密度 \(L^2(dt)\) norm では range を加えて norm を任意に小さくできることが Proposition 6.4(2) / (6.12) の内容である。この差が以下の診断の算術入力となる。[版固定原文](https://arxiv.org/pdf/math/0703392v1)

## OT2. quotient-first は同じ seminorm の collapse を回避しない

**補題 OT2-A。** \(S\) を複素線形空間、\(R\subset S\) を線形部分空間、\(N\) を \(S\) 上の seminorm とする。\(X_N\) は \(S/\ker N\) の Banach 完備化、\(j:S\to X_N\) は標準写像とする。\(S/R\) 上で
\[
 q_N([s])=\inf_{r\in R}N(s+r)
\]
と置く。この seminorm の零空間を割った後の完備化は、自然に等長に
\[
 \overline{(S/R)/\ker q_N}^{\,q_N}
 \simeq X_N/\overline{j(R)}^{\,X_N}.                           \tag{2}
\]
\(R\) の閉性も \(N\) の非退化性も仮定しない。

**証明。** \([s]\mapsto j(s)+\overline{j(R)}\) は well-defined で、
\[
 \|j(s)+\overline{j(R)}\|
 =\inf_{y\in\overline{j(R)}}\|j(s)+y\|
 =\inf_{r\in R}N(s+r)=q_N([s]).
\]
従ってその核は \(\ker q_N\)、像は右辺で稠密。右辺は Banach 空間なので等長延長は onto。□

**補題 OT2-B（評価の保持も順序では変わらない）。** 線形 \(\ell:S\to\mathbb C\) が \(R\) を消すとする。このとき
\[
 |\ell(s)|\le C N(s)\quad\forall s
 \quad\Longleftrightarrow\quad
 |\ell(s)|\le C q_N([s])\quad\forall s,                         \tag{3}
\]
かつ最良の \(C\) は同じ。

一方向は \(\ell(s+r)=\ell(s)\) と \(r\) に関する infimum、他方向は \(q_N([s])\le N(s)\) による。従って quotient-first は、元の \(N\) で unbounded な Mellin 評価を bounded に復活させない。\(j(R)\) が \(X_N\) で稠密なら (2) は零空間になる。

\(T^{\pm1}R=R\) かつ \(N(T^ns)\le C_nN(s)\) なら
\[
 q_N(T^n[s])\le C_nq_N([s]).                                  \tag{4}
\]
ただし商での最良定数は ambient の最良定数より小さくなり得る。以下の ambient exact norm を算術商の下界とはしない。新しい算術 cancellation を証明して (4) を改善すること自体は別の未解決問題である。

### OT2.1. Fréchet seminorm 系を使う場合

増大する seminorm 系 \(N_j\) なら \(q_j=\inf_R N_j\) が quotient topology を生成し、
\[
 \bigcap_j\ker q_j=\overline R^{\,S}/R.
\]
個々の \(q_j\) の完備化と、その projective system 全体を取り違えない。高速減衰 Fréchet 商が非零であることは、全ての弱い単一 norm の商が同じ情報を保持することを意味しない。

商を取った二端点を先に補間することにも注意が必要である。例えば \(Y_0=X_0/\overline R^{X_0}=0\)、\(Y_k=X_k/\overline R^{X_k}\ne0\) なら、この二端点には共通の \(S/R\) を両方へ忠実に入れる compatible-couple 同定はない。形式的な couple \((0,Y_k)\) の complex interpolation は \(0<\theta<1\) で零空間である。一方、interpolated ambient norm の商は非零のことがある。closure を異なる norm で取った後、補間と商を無条件に交換してはならない。

## OT3. 指数 Hilbert 重みの補間：正確な定数

\[
 H_a=L^2(\mathbb R,e^{2a|t|}dt),\quad a\ge0.
\]
\(k>0\)、\(0<\theta<1\) について Calderón complex method では等長に
\[
 [H_0,H_k]_\theta=H_{\theta k}.                               \tag{5}
\]

**直接証明。** \(f\in H_{\theta k}\) に
\(F(z,t)=e^{(\theta-z)k|t|}f(t)\) を用いる。二境界でそれぞれ
\[
 \|F(iy)\|_{H_0}=\|F(1+iy)\|_{H_k}=\|f\|_{H_{\theta k}}.
\]
通常の strip class で虚方向の消失を要求する場合は
\(e^{\varepsilon(z-\theta)^2}\) を掛け、\(\varepsilon\downarrow0\) とする。これで補間 norm の上界を得る。
逆に任意の admissible \(F\) と compact support の \(g\in L^2(e^{-2\theta k|t|}dt)\) に
\[
 h(z)=\int F(z,t)e^{(z-\theta)k|t|}\overline{g(t)}\,dt
\]
を用い、境界で Cauchy–Schwarz、strip の three-lines theorem を適用する。
\[
 |h(\theta)|\le\|F\|_{\mathcal F}
                 \|g\|_{L^2(e^{-2\theta k|t|})}.
\]
稠密性と duality から逆向き norm 不等式が出る。□

これは既知の weighted \(L^p\) interpolation の特殊例である。一次文献との照合は Hernández, Proposition 5.3、Theorem 6.1、Proposition 7.1（pp.252–257）を用いた。ここで必要な二端点 \(L^2\) の証明は上記で完結する。[Hernández 1986](https://www.numdam.org/item/ASNSP_1986_4_13_2_245_0.pdf)

変数変換により
\[
 \|T^n\|_{H_a\to H_a}=e^{a|n|L}=2^{a|n|}.                    \tag{6}
\]
上界は \(|t+nL|-|t|\le|n|L\)。\(n\ge0\) なら test function の support を正の半直線に取り、\(n<0\) なら負の半直線に取れば上界を達成する。

Mellin 評価は Riesz 表現から
\[
 \ell_\lambda\in H_a'
 \iff a>|\alpha|,\qquad
 \|\ell_\lambda\|_{H_a'}^2
   =\int_{\mathbb R}e^{2\alpha t-2a|t|}dt
   =\frac{a}{a^2-\alpha^2}.                                  \tag{7}
\]
この iff は \(a>0\) についてである。\(a=0\) では、\(\alpha=0\) を含む全ての \(\lambda\) で非零の単一点評価が unbounded となる。

従って (5) では保持閾値がちょうど \(\theta k>|\alpha|\)、反復 norm が \(2^{\theta k|n|}\)。\(\theta\downarrow0\) の過程で \(\alpha\ne0\) の評価は閾値を越えた時点で失われる。\(\alpha=0\) でも norm は \((\theta k)^{-1/2}\) と発散し、unitary な endpoint \(H_0\) へ bounded に延長できない。

**算術商に対する exact な範囲。** \(\ell_\lambda|_{\mathscr R}=0\) である actual zero については、(3) により (7) は商 norm でも同じ閾値となる。\(a>\tfrac12\) なら全非自明零点の評価を保持するが、(6) だけから subexponential return bound は得られない。\(a=0\) は actual arithmetic range の既知の dense collapse とも一致する。

補間の重みを \(n\) ごとに \(\theta_n\downarrow0\) と変えて (6) を小さくしても、同じ空間の operator powers の評価にはならない。固定した \(\ell_\lambda\) の norm と固定 quotient の識別を保つ一様比較が必要であり、(7) はその比較の破綻を明示する。

### OT3.1. real interpolation \((\theta,2)\) も同じ閾値

\(w(t)=e^{2k|t|}\) とし、補間 parameter は座標 \(t\) と区別して \(\tau>0\) と書く。quadratic \(K\)-functional を
\[
 K_2(\tau,f)^2=
 \inf_{f=f_0+f_1}\left(\|f_0\|_{H_0}^2+
                                  \tau^2\|f_1\|_{H_k}^2\right)
\]
と定めると、点ごとの minimizer は
\[
 f_1=\frac{f}{1+\tau^2w},\qquad
 f_0=\frac{\tau^2w f}{1+\tau^2w}
\]
であり、
\[
 K_2(\tau,f)^2
 =\int_{\mathbb R}|f(t)|^2
                   \frac{\tau^2w(t)}{1+\tau^2w(t)}dt.          \tag{7a}
\]
ここでは \(H_k\subset H_0\) なので \(H_0+H_k=H_0\)、上記 minimizer はそれぞれ指定空間に属する。Tonelli と \(y=\tau\sqrt{w(t)}\) により
\[
 \begin{aligned}
 \int_0^\infty \tau^{-2\theta}K_2(\tau,f)^2\frac{d\tau}{\tau}
 &=\left(\int_0^\infty\frac{y^{1-2\theta}}{1+y^2}dy\right)
                          \int_{\mathbb R}|f(t)|^2w(t)^\theta dt\\
 &=\frac{\pi}{2\sin(\pi\theta)}\|f\|_{H_{\theta k}}^2,
                   \qquad 0<\theta<1.                       \tag{7b}
 \end{aligned}
\]
通常の \(K(\tau,f)=\inf(\|f_0\|+\tau\|f_1\|)\) には
\(K_2\le K\le\sqrt2K_2\)。従って \((H_0,H_k)_{\theta,2}\) は \(H_{\theta k}\) と等価 norm で一致する。usual \(K\)-norm の exact operator norm は主張しないが、norm equivalence の定数は \(n\) に依存しないので
\[
 \lim_{|n|\to\infty}
 \frac{\log\|T^n\|_{(H_0,H_k)_{\theta,2}}}{|n|\log2}
 =\theta k.
\]
評価保持の閾値も (7) と同じ。real method へ変更しても endpoint loss は修復されない。

## OT4. scaling derivatives、多項式重み、Schwartz 位相

### OT4.1. 有限個の scaling derivatives

半密度座標で \(x\partial_x+\tfrac12\) は \(\partial_t\) に移る。整数 \(m\ge0\) に
\[
 N_{a,m}(\phi)^2=\sum_{j=0}^m
       \int e^{2a|t|}|\phi^{(j)}(t)|^2dt
\]
を使うと、translation が導関数と可換なので
\[
 \|T^n\|_{N_{a,m}\to N_{a,m}}=2^{a|n|}.                       \tag{8}
\]
等号は (6) と同じ半直線 support で全導関数に同時に成立する。

評価の閾値も変わらない。\(a>|\alpha|\) は zeroth term で十分。\(|\alpha|>a\) の不連続性は固定 bump の平行移動で示せる。境界 \(\alpha=a\ge0\) では
\[
 \phi_R(t)=e^{-(a+i\gamma)t}\eta(t/R),
 \qquad 0\ne\eta\in C_c^\infty((1,2)),\quad \int\eta\ne0
\]
と置く。\(N_{a,m}(\phi_R)=O(\sqrt R)\)、\(\ell_\lambda(\phi_R)=R\int\eta\) なので unbounded。負の境界は反射する。従って有限個の微分を増やすだけで endpoint は修復されない。固定 \(a\) で全導関数を含む Fréchet topology でも、連続 functional は有限個の seminorm で支配されるので同じ障害が残る。

### OT4.2. 多項式の moment 重みは境界だけを変える

\[
 P_r=L^2(\mathbb R,(1+|t|)^{2r}dt),\quad r\ge0.
\]
直接計算で
\[
 \|T^n\|_{P_r\to P_r}=(1+|n|L)^r,\qquad
 \ell_{i\gamma}\in P_r'\iff r>\tfrac12.
\]
一方、\(\alpha\ne0\) の評価はどの有限 \(r\) でも unbounded。有限個の導関数を併用しても指数対多項式の比較は変わらない。

重み \(e^{a|t|}(1+|t|)^r\) を併用するなら、評価保持は
\[
 |\alpha|<a,\quad\text{または}\quad |\alpha|=a,\ r>\tfrac12
\]
であり、外側 \(|\alpha|>a\) は除外される。境界の細部は変えられるが return の指数成長率 \(a\) は消えない。時間微分と時間 moment、すなわち Fourier 側の微分を混同しない。

通常の Schwartz topology \(\mathcal S(\mathbb R)\) は全ての \(\ell_{i\gamma}\) を保持し、\(\alpha\ne0\) の \(\ell_\lambda\) を連続双対に持たない。例えば \(\alpha>0\) で
\(\phi_j(t)=e^{-\alpha j/2}\eta(t-j)e^{-i\gamma t}\) とすれば、全 Schwartz seminorm で \(\phi_j\to0\) だが \(|\ell_\lambda(\phi_j)|\) は指数発散する（\(\eta\ge0\)、非零）。これを actual all-zero quotient の位相へ変更した時点で、全零点保持の証明義務が生じる。

Schwartz translation の polynomial bounds は equicontinuity ではない。非零固定 bump を平行移動すると正の moment seminorm は非有界になる。指数成長ゼロと全反復の一様有界性も分離する。

## OT5. Beurling / GRS 重み：subexponential 性と評価喪失

連続、正、偶、\(w(0)=1\)、submultiplicative な重み
\[
 w(t+s)\le w(t)w(s)
\]
を仮定し、\(H_w=L^2(w^2dt)\) とする。これは診断用 class である。算術側からこの class の norm が指定されたという主張ではない。

\[
 \|T^n\|_{H_w\to H_w}
 =\sup_t\frac{w(t+nL)}{w(t)}=w(nL).                            \tag{9}
\]
上界は submultiplicativity、下界は \(t=0\) の近傍と連続性を使う。\(w(nL)^{1/n}\to1\) という一素数方向の GRS 条件を置くと、両方向の return は subexponential。

この条件から任意の \(\varepsilon>0\) に対し
\(w(t)\le C_\varepsilon e^{\varepsilon|t|}\) が出る。実際、\(t=nL+r\)、\(|r|\le L\) と書き、GRS と compact interval 上の boundedness を使えばよい。ゆえに
\[
 \|\ell_\lambda\|_{H_w'}^2
   =\int_{\mathbb R}\frac{e^{2\alpha t}}{w(t)^2}\,dt             \tag{10}
\]
は \(\alpha\ne0\) で必ず発散する。\(\alpha=0\) の保持は \(\int w^{-2}<\infty\) と同値。例えば
\(w(t)=e^{c|t|^\beta}\), \(c>0,\ 0<\beta<1\) は両方向 subexponential で全 critical evaluation を保持するが、off-axis evaluation は保持しない。

ここでの GRS は既知の条件であり、weighted convolution algebra の spectral invariance と関連する。しかしその定理は actual arithmetic quotient への全零点保持や unitary metric の構成ではない。[Gröchenig–Leinert, §2.1 (1)–(3), 著者原稿 p.3](https://homepage.univie.ac.at/karlheinz.groechenig/preprints/inverselast.pdf) 本ノートの (9)–(10) は直接計算であり、inverse-closedness の深い定理を使っていない。

**判定。** GRS を norm の設計条件として先に入れれば、成長率ゼロは設計に入っている。その norm に全 actual zero evaluations が残るという追加定理は RH を含意する。全零点保持を未確認のまま選んではいけない。

## OT6. Hardy / Mellin–Paley–Wiener の最短診断

### OT6.1. 両側 strip は指数重みの別表示

\(F(\lambda)=\int_{\mathbb R}\phi(t)e^{\lambda t}dt\) とすると Plancherel より
\[
 \frac1{2\pi}\int_{\mathbb R}|F(b+i\gamma)|^2d\gamma
 =\int_{\mathbb R}e^{2bt}|\phi(t)|^2dt.                        \tag{11}
\]
strip の両境界 \(b=\pm a\) の \(L^2\) norm の和は（完備化後は \(L^2\) boundary value と解釈する）
\(\int2\cosh(2at)|\phi(t)|^2dt\)。これは \(H_a\) と等価であり、translation の exact norm はやはり \(2^{a|n|}\) となる。interior point evaluation を保証する strip 幅をゼロへ潰すと、評価の保証も失われる。holomorphy という名前へ置き換えても OT3 の問題は消えない。

### OT6.2. 半平面 Hardy は片側 semigroup

\(\phi\in L^2(0,\infty)\) なら
\[
 F(\lambda)=\int_0^\infty\phi(t)e^{\lambda t}dt,\quad\Re\lambda<0,
 \qquad \|\ell_\lambda\|^2=-\frac1{2\Re\lambda}.                \tag{12}
\]
右への零延長 shift は isometry だが onto でなく、逆 shift は同じ群作用として定義できない。従って \(\Re\lambda<0\) の bounded dual eigencharacters が存在しても矛盾しない。片側 isometry を両側 unitary return に読み替えてはいけない。

Hardy–Sobolev 拡張にも実際の変換定理はあるが、定義域・境界・微分の配置を伴う。[Galé–Matache–Miana–Sánchez–Lajusticia, arXiv:2401.16091v1, §1 (1.1), §3 Theorem 3.3](https://arxiv.org/html/2401.16091v1#S3) それらが本課題の全実線 arithmetic quotient と等しいという定理は使用していない。

### OT6.3. 有限 exponential type

\(\operatorname{supp}\phi\subset[-A,A]\) なら全ての複素評価が bounded で、
\[
 |\ell_\lambda(\phi)|\le
 \left(\int_{-A}^A e^{2\alpha t}dt\right)^{1/2}\|\phi\|_2.
\]
しかし \(T^n\) は support を \(nL\) だけ動かすので、同じ有限 \(A\) の Hilbert 空間を保存しない。\(A\to\infty\) による評価定数の発散を無視できない。固定 Paley–Wiener 型の norm、周期化 \(t\bmod L\)、または有限 support truncation を actual all-zero representation の faithful return として採用する根拠はない。

## OT7. RH 同値・逆向き含意・停止地点

### OT7.1. 全評価を保持する具体的 \(q_1\) は構成できている

同巡の [arithmetic_space.md, §§3–6](arithmetic_space.md) では、標準 test topology の
\[
 p_N(g)=\max_{0\le j\le N}\sup_t
 e^{N|t|}(1+|t|)^N|g^{(j)}(t)|,\quad
 q_N([g])=\inf_{w\in W}p_N(g+w)
\]
を用いる。ここで \(W\) は指定された算術 range closure。全零点に対し \(|\alpha|<1/2\) なので
\[
 |\ell_\rho(g)|
 \le p_1(g)\int_{\mathbb R}e^{-(1-|\alpha|)|t|}dt
 \le4p_1(g).
\]
算術 range を消すことと (3) より \(|\ell_\rho(x)|\le4q_1(x)\)。
従って \(X_1=\overline{E/\ker q_1}^{\,q_1}\) は全非零評価を保持する Banach 完備化であり、零点配置から norm を定義していない。この具体的構成を「quotient seminorm が未構成」と記述してはならない。

一方、直接の translation bound は
\[
 q_1(T^nx)\le 2^{|n|}(1+|n|\log2)q_1(x),                     \tag{13}
\]
までである。\(X_1\) が全商位相と同値、余分な spectrum がない、または subexponential return を持つことは構成から出ない。OT2 はこの保持結果を否定せず、その seminorm で quotient-first が正当なことを保証している。

### OT7.2. 閉じていない箇所

位相 \(\tau\) で \(\ell_\rho\ne0\) が連続かつ (1) が成立し、両方向の return が各評価を支配する seminorm において subexponential なら \(\alpha=0\)。これは表現論の条件付き帰結であり、成長率 bound の算術的証明ではない。

特に次は独立な入力として採用できない。

- 「全零点評価が残るように」零点列から norm を定義する。
- Weil pairing の全域正性を新しい norm construction と呼ぶ。これは既知の RH 同値条件である。
- off-axis 評価が bounded dual にない空間を選び、その不在を元の算術商での不在とする。
- \(n\) ごとに異なる重み・support・completion を使い、同じ return operator の spectral radius の計算とする。

Gelfand–Shilov、modulation、その他 weighted nuclear spaces は今回全面監査しない。名前や nuclearity 自体から growth bound は出ず、許容される test packet の平行移動による検査と OT2-B の評価保持 gate、さらに同じ算術商上の両方向 bound を通る具体的定義が必要である。compact bump を含まない class では、その class 内の Gaussian 等が使えるかも確認を要する。これを未確認の代替 topology として採用しない。

### OT7.3. RH から equicontinuity への逆を自動化しない

仮に全 character の modulus が1でも、Jordan chain は反復で polynomial growth を作る。\(J=\begin{pmatrix}1&1\\0&1\end{pmatrix}\) が最小例である。

さらに個々の block が semisimple でも、無限個の norm 比較が悪ければ一様 bound は出ない。\(H=\bigoplus_{j\ge1}\mathbb C^2\) 上に
\[
 A=\bigoplus_j A_j,\qquad
 A_j=\begin{pmatrix}1&1\\0&e^{i/j}\end{pmatrix}
\]
を取る。\(A,A^{-1}\) は bounded、各 block は diagonalizable、eigenvectors の有限線形結合は稠密。それでも
\[
 (A_j^n)_{12}=\sum_{r=0}^{n-1}e^{ir/j}\longrightarrow n
 \quad(j\to\infty),\qquad
 n\le\|A^n\|\le n+2.
\]
従って power bounded でない。spectrum は
\(\{1\}\cup\{e^{i/j}:j\ge1\}\subset\{|z|=1\}\)：
この閉集合の外側では各 \(2\times2\) resolvent の分母は一様に離れ、直和 resolvent は bounded となる。
これは topology / conditioning の反例であり、actual arithmetic module の反例ではない。どちらの例も指数成長ゼロ・subexponential bound と両立するので、ここで反証しているのは modulus-one spectrum から equicontinuity / unitary norm への自動的な逆である。純虚 character、良い multiplicity、適切な sequence topology の三者を無条件に同一視しない。

### OT7.4. この巡の判定

| 候補 | 独立に確認できること | 未供給の算術情報 | 判定 |
|---|---|---|---|
| 同じ \(N\) で quotient-first | 等長同定 (2)、評価保持 iff (3) | 新しい cancellation estimate | 順序だけによる修復は STOP |
| 指数重みの complex / real \((\theta,2)\) interpolation | (5)–(7b) の空間・定数同定 | endpoint に全零点を保持する比較 | STOP |
| scaling derivatives の追加 | 閾値と指数率は不変 | 算術 range を使う別 estimate | 単独案 STOP |
| polynomial / GRS 重み | subexponential return と critical 評価 | off-axis を含む全零点の faithful transfer | 全零点案として STOP |
| Hardy strip / half-plane / Paley–Wiener | 明示変換・domain 診断 | 同じ bilateral arithmetic quotient との比較 | 単独案 STOP |
| 標準算術 seminorm \(q_1\) と \(X_1\) | 零点を入力しない定義、全零点評価保持、bounded return | 両方向 subexponential estimate | Level 2 の具体的構成 KEEP、growth step OPEN |

**残る最小課題。** OT7.1 の \(q_1\) が全評価を支配するので、全ての左辺 seminorm の制御を要求する必要はない。各 \(\varepsilon>0\) に対して整数 \(M_\varepsilon\ge1\)、定数 \(C_\varepsilon<\infty\) を取り、
\[
 q_1(T^nx)\le C_\varepsilon\,2^{\varepsilon|n|}
                 q_{M_\varepsilon}(x)
 \quad\text{for all }x\in E,\ n\in\mathbb Z                    \tag{14}
\]
を、range の算術を用いて同じ \(E\) 上で示せれば十分である。\(M_\varepsilon,C_\varepsilon\) は \(x,n\) に依存してはならない。実際、\(\ell_\rho(x)\ne0\) を選び、
\[
 \tfrac14\,2^{n\alpha}|\ell_\rho(x)|
 \le q_1(T^nx)
 \le C_\varepsilon2^{\varepsilon|n|}q_{M_\varepsilon}(x)
\]
で \(n\) の正負を選ぶと \(|\alpha|\le\varepsilon\)、従って \(\alpha=0\)。
(14) は RH を含意するが、今回その逆は証明していない。全零点保持と (14) を同時に満たす独立な算術 estimate は得られておらず、補間や quotient-first の一般論から既証明へ昇格しない。

### 文献監査の範囲

Calderón 1964 の [出版社記録](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/24/2/95688/intermediate-spaces-and-interpolation-the-complex-method) は確認したが、原版 PDF の直接取得は失敗した。原版の定理番号を読んだとはしない。weighted interpolation は上記 Hernández の一次論文と直接証明で確認した。GRS は Gröchenig–Leinert の著者原稿 §2.1、Hardy–Sobolev は Galé ほかの版固定原文の指定箇所を確認した。引用した各分野の全証明や、任意の quotient での interpolation exactness を監査済みとはしない。

**独立監査。** DESTROYER は OT2–OT3 の初稿を読取・別計算で PASS とした。対象は completion の距離等長同定、functional の最良定数一致、complex interpolation の両方向証明、exact return norm、評価閾値と endpoint loss、ambient と quotient の定数の区別である。追記した real interpolation OT3.1 および OT4 以降はこの独立監査の範囲外。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/one_prime/notes/arithmetic_space.md`](arithmetic_space.md)
