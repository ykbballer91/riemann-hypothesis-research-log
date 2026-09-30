**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/scale_flow/notes/spectral_growth.md` · Original SHA-256: `7674fd336b867ff463d23a95f7493e4be48ff96f898da0b9b93448a7500a772d`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 算術スケール表現の成長率と、不変正計量に必要な条件

2026-09-29。独立 parallel track の限定監査。Phase III / IV、主定理グラフは変更しない。既知の算術表現と初等的な表現論の帰結を分離する。新しい正計量は得られておらず、RH の進展・新規性は主張しない。

**結論。** 全零点を保持する CCM の位相的表現では、正規化した双対固有指標の指数成長率を厳密に \(\Re\rho-\tfrac12\) と同定できる。これを geometric transverse tangent の Lyapunov 指数と同定する定理はない。正の不変形式から Hilbert 完備化を作るだけでなく、**各零点の非零固有汎関数を、その同じ完備化の有界双対に保持すること**が必要である。素数軌道の profinite Haar 計量は正であるが、この全零点比較を供給しない。

## SG1. 正規化、位相、算術商

\(K=\mathbb Q\) の trivial compact-character sector を取る。乗法変数を \(x>0\)、作用時間を \(u\in\mathbb R\)、座標を \(t=\log x\) と区別する。

\[
 \widehat f(s)=\int_0^\infty f(x)x^s\,\frac{dx}{x},\qquad
 \vartheta_u f(x)=f(e^{-u}x),\qquad
 W_u=e^{-u/2}\vartheta_u.                                      \tag{1}
\]

CCM07 (4.41)–(4.45) の正規化である。中心 \(1/2\) は completed ζ の機能等式と対応する既知の中心化であり、中心化しただけで指数の実部が消えるわけではない。スカラー test space は
\(\mathcal E=\bigcap_{\beta\in\mathbb R}x^\beta\mathcal S(\mathbb R_+^\times)\)。
半密度座標
\[
 \phi(t)=e^{t/2}f(e^t),\qquad
 (VW_uV^{-1}\phi)(t)=\phi(t-u)                                 \tag{2}
\]
を用いると、\(\mathcal E\) は全ての指数重みと全ての導関数に対して急減する Fréchet 空間となる。例えば
\(\sup_t e^{k|t|}(1+|t|)^N|\phi^{(j)}(t)|\)（整数 \(k,N,j\ge0\)）で位相を定められる。

算術入力は任意の translation-invariant 部分空間ではない。CCM07 Definition 4.14 の
\[
 \mathcal V=\left\{x\longmapsto\sum_{a\in\mathbb Q^\times}\xi(ax):
 \xi\in\mathcal S(\mathbb A_\mathbb Q),\quad
 \xi(0)=\int_{\mathbb A_\mathbb Q}\xi=0\right\}
                                                               \tag{3}
\]
の該当 sector と、その指定位相での閉包を使う。以下の \(\mathcal E/\overline{\mathcal V}\) は scalar quotient 記法であり、CCM の cyclic-module cokernel とその次数零双対の説明を勝手な Hilbert 商に置換するものではない。作用の降下、全零点の出現、integrated operator の multiplicity 付き trace は既知入力である。[CCM07, Definition 4.10, Proposition 4.13, Lemma 4.15, Theorem 4.16](https://arxiv.org/pdf/math/0703392v1)

核型・局所凸空間での trace realization であり、未指定の Hilbert norm に関する Schatten trace と読んではならない。Meyer の summable representation では quasi-character の代数的 multiplicity を有限次元 subrepresentation の Jordan–Hölder 因子で数える。[Meyer03, §2.4, pp.10–11](https://arxiv.org/pdf/math/0311468v1)

## SG2. 「零点の radial growth」の正確な意味

非自明零点 \(\rho=\tfrac12+\alpha+i\gamma\) に対し
\[
 \ell_\rho(f)=\widehat f(\rho)
       =\int_{\mathbb R}\phi(t)e^{(\alpha+i\gamma)t}\,dt
                                                               \tag{4}
\]
は \(\mathcal E\) の連続線形汎関数である。変数変換だけで
\[
 \ell_\rho(W_u f)=e^{(\rho-1/2)u}\ell_\rho(f).                    \tag{5}
\]
CCM の零点同定により \(\ell_\rho\) は算術 range を消し、非零の商双対指標として残る。この「非零」は Mellin 評価自体が非零であり、\(\overline{\mathcal V}\subset\ker\ell_\rho\) であることによる。全零点同定は (5) だけからの結論ではなく、SG1 の算術入力である。

ここでは通常の transpose \(W'_u\ell=\ell\circ W_u\) を使う。contragredient を \(\ell\circ W_{-u}\) と定義する規約なら指数の符号が逆になる。
固有指標の一次元空間上の任意の norm で
\[
 \lim_{u\to+\infty}\frac1u
       \log\frac{\|W'_u\ell_\rho\|}{\|\ell_\rho\|}
       =\alpha.                                                \tag{6}
\]
これは **actual arithmetic representation の spectral-character growth** である。商全体の norm、可微分多様体、確率測度、Oseledets 定理を必要としない。

test core 上の微分は
\[
 G_0=-x\partial_x-\tfrac12,\qquad VG_0V^{-1}=-\partial_t,\qquad
 \ell_\rho(G_0f)=(\rho-\tfrac12)\ell_\rho(f).                    \tag{7}
\]
従って normalized generator の双対固有値の実部が (6) と一致する。\(W_u=e^{iuA}\) と書くなら \(G=iA\) であり、裸の \(L^2(dt)\) 表現では \(A=i\partial_t\)、定義域 \(H^1(\mathbb R)\)。順方向 dilation を選ぶ流儀とは符号が逆である。

### SG2.1. generalized modes と resonances

Mellin jets \(\ell_{\rho,j}(f)=\partial_s^j\widehat f(s)|_{s=\rho}\) には test space 上で
\[
 \ell_{\rho,j}(W_uf)
 =e^{(\rho-1/2)u}\sum_{r=0}^j{j\choose r}u^{j-r}\ell_{\rho,r}(f).
                                                               \tag{8}
\]
商へ降りる jet については、有限 Jordan chain の polynomial factor は指数 (6) を変えない。ただし jet の降下・独立性は range の消失次数の確認を要する。trace の multiplicity から勝手に Jordan block や単純零点を推定しない。

Hilbert 空間内の genuine eigenvector、連続双対固有汎関数、analytic continuation での resonance は別物である。unitary generator の spectrum が虚軸上という定理は、別の弱い test-space dual にある off-axis functional、または continued resolvent の pole を排除しない。裸の translation 自体が (4) を test-space dual に全て持つことが最小の例となる。

### SG2.2. geometric transverse exponent は未同定

\(D\varphi_u\) の normal bundle、可測 cocycle の integrability、基礎 flow の invariant measure が指定されて初めて tangent Lyapunov exponent を語れる。profinite fiber は実可微分 transverse tangent bundle ではない。CCM の cohomological character と、そのような derivative cocycle との intertwiner は供給されていない。従って本ノートは geometric transverse growth の構成を達成したとはしない。

## SG3. 正計量から零成長へ進むための最小補題

**補題 SG3-A（completion と全零点保持）。** \(E\) は複素線形空間、\(W_u\) は全 \(u\in\mathbb R\) に定義された群作用とする。次の条件を置く。

1. Hermitian form \(q\) は半正定値で、\(q(W_uv,W_uw)=q(v,w)\)。
2. 各 \(v\in E\) に対し \(q(W_uv-v,W_uv-v)\to0\) as \(u\to0\)。
3. 各非自明零点 \(\rho\) の非零汎関数 \(\ell_\rho\) が \(E\) 上に存在し、(5) と
   \[
   |\ell_\rho(v)|\le C_\rho q(v,v)^{1/2}                         \tag{9}
   \]
   を満たす。\(C_\rho\) は零点依存でよく、一様 bound は不要。

このとき全ての非自明零点の \(\Re\rho=\tfrac12\)。

**証明。** Cauchy–Schwarz により \(N_q=\{v:q(v,v)=0\}\) は radical であり、不変である。\(E/N_q\) を完備化した Hilbert 空間 \(H_q\) に、\(W_u\) は isometry として一意に延長する。\(W_{-u}\) が逆なので onto、従って unitary。条件 2 と稠密性により強連続になる。条件 3 により \(\ell_\rho\) は \(N_q\) を消し、非零の有界 functional として \(H_q\) に延長する。すると
\[
 \|\ell_\rho\|=\|\ell_\rho\circ W_u\|
 =e^{\alpha u}\|\ell_\rho\| \quad(u\in\mathbb R),
\]
よって \(\alpha=0\)。□

条件 2 は、元の位相で \(W\) が強連続かつ \(q(v,v)^{1/2}\) が連続 seminorm なら従う。単に形式的な正性、あるいは単に \(q(G_0v,w)+q(v,G_0w)=0\) を記すだけでは、この群・定義域・完備化の条件を満たさない。
なお実部ゼロという結論だけには条件 2 は不要である。条件 1 と 3 で unitary 延長と双対 norm の等式は成立する。条件 2 は、本課題が要求する \(C_0\) 群と閉 generator を得るために置いた。

この構成で得られる generator の定義域は
\[
 D(G)=\left\{v\in H_q:\lim_{u\to0}(W_uv-v)/u
                      \text{ が }H_q\text{ に存在}\right\}.
\]
Stone の定理で \(G^*=-G\)。元の微分作用素 \(G_0\) がこの \(G\) に一致するには、core と Hilbert norm での微分を別途確認する。非正規化 generator \(\Theta=G+\tfrac12I\) なら同じ domain 上で
\[
 \Theta^*=I-\Theta.                                            \tag{10}
\]
これが有限体の adjoint 関係に対応する正確な連続群側の等式である。ただし、その正 Hilbert 空間の算術的構成が未解決である。

**必要な completeness の強さ。** RH のこの帰結には「全ての零点が少なくとも一つの非零 bounded character として残る」が足りる。Hilbert 空間の全 spectrum が零点だけであるという逆向き completeness や、trace の全 multiplicity 保存までは不要。他方、有限個・critical-line 零点のみの保持では足りない。

**Jordan の注意。** unitary 群は非自明有限 Jordan block を持てない。固有値 \(i\gamma\) の \(e^{u(i\gamma I+N)}\), \(N\ne0\) nilpotent は polynomial に非有界となる。従って「既存の generalized eigenspace 全体を忠実に Hilbert unitary 化する」は、単なる各零点の実部条件より強い義務になり得る。RH だけから全 Jordan chain のそのような保持を結論しない。

## SG4. 計算可能な重み付き norm が教えること

以下は明示的な **補助 Hilbert 空間** であり、CCM の未証明の不変 norm として採用しない。半密度座標で
\[
 H_k=L^2(\mathbb R,e^{2k|t|}dt),\quad k>0.
\]
translation \(W_u\phi(t)=\phi(t-u)\) は \(C_0\) 群で
\[
 \|W_u\|_{H_k\to H_k}=e^{k|u|}.                                \tag{11}
\]
上界は \(|t|\le|t-u|+|u|\)、等号は適切な半直線に support を置いて得る。\(C_c^\infty\) の稠密性と局所有界性から \(C_0\) 性が従う。

Riesz/Cauchy–Schwarz により (4) の functional は **ちょうど \(k>|\alpha|\) のとき** \(H_k\) 上有界で、
\[
 \|\ell_\rho\|_{H_k'}^2
  =\int_{\mathbb R}e^{2\alpha t-2k|t|}dt
  =\frac{k}{k^2-\alpha^2}.                                    \tag{12}
\]
境界 \(k=|\alpha|\) では片側の積分が発散する。jet についても strict inequality なら多項式因子を吸収できる。全零点は \(0<\Re\rho<1\) にあるので \(k>\tfrac12\) の ambient norm は全ての (4) を保持できるが、(11) は成長を許す。逆に \(k\downarrow0\) で unitarity に近づけても off-axis functional の boundedness が失われる。\(k=0,\alpha=0\) でも単一点 Fourier 評価は裸の \(L^2\) に有界でない。

したがって「各 \(H_k\) で bound がある」「全ての導関数も含む重み付き Sobolev norm の交叉で Fréchet test space を記述できる」は、同じ全零点商に不変正 norm があることを意味しない。算術 range の閉包も位相を変えるたびに再検証が必要である。CCM07 Proposition 6.4(2) は、算術 range を加えることで半密度 \(L^2\) norm を任意に小さくできることを明示する。[同 p.29](https://arxiv.org/pdf/math/0703392v1) 元の quotient をそのまま bare \(L^2\) quotient に移せない理由である。

## SG5. 一周期の unitary return が本当に与えるもの

**補題 SG5-A。** 同じ Hilbert 空間 \(H\) 上の \(C_0\) 群 \(W_u\) があり、ある \(L>0\) で \(W_L\) が unitary とする。このとき全時間で一様有界で、全非零 \(v\) について
\[
 \lim_{u\to\pm\infty}\frac{\log\|W_uv\|}{|u|}=0.
                                                               \tag{13}
\]
さらに元の norm と等価な不変 Hilbert 内積が存在する。

**証明。** 一様有界性原理により \(M=\sup_{0\le r\le L}\|W_r\|<\infty\)。\(u=nL+r\), \(n\in\mathbb Z\), \(0\le r<L\) と書けば \(\|W_u\|\le M\)。逆時間にも同じ bound を使い、
\(M^{-1}\|v\|\le\|W_uv\|\le M\|v\|\)。さらに
\[
 \langle v,w\rangle_{\mathrm{av}}
   =\frac1L\int_0^L\langle W_tv,W_tw\rangle\,dt                 \tag{14}
\]
を定める。被積分関数は \(L\)-periodic なので全ての \(W_u\) に不変であり、
\(M^{-2}\|v\|^2\le\|v\|_{\mathrm{av}}^2\le M^2\|v\|^2\)。□

元の norm 自体で全時刻 unitary とは限らない。例えば
\(W_u=S R_{2\pi u/L}S^{-1}\), \(S=\operatorname{diag}(2,1)\) は \(W_L=I\) だが四分の一周期では元の Euclidean norm を保存しない。

もし **同じ空間と同じ元の norm** で \(W_{\log2}\) と \(W_{\log3}\) が unitary なら、\(\log2/\log3\notin\mathbb Q\)、稠密部分群および強連続性から全 \(W_u\) が元の norm で unitary。異なる \(p\) の異なる fiber にある unitary operator をここへ代入してはいけない。

周期線形 cocycle の場合も同じ点がある。基本解 \(X(t)\)、周期 \(L\)、monodromy \(M=X(L)\)、正行列 \(G_0\) に対し
\[
 M^*G_0M=G_0
 \quad\Longrightarrow\quad
 G(t)=X(t)^{-*}G_0X(t)^{-1}                                   \tag{15}
\]
は正の periodic metric である。有限次元の compact period では上下の一様 norm 比較が自動的に成立し、指数はゼロ。無限次元では bounded invertibility と uniform coercivity を確認する。単に各時刻で正の \(G(t)\) が存在するだけでは足りない。

**全零点への適用条件。** SG3 の zero-bearing \(H_q\) と同じ忠実な空間で上の return 条件を証明し、(9) を保持できれば RH に至る。この条件を未知の局所–大域比較として残すことが必要であり、「Frobenius monodromy がある」ことの言い換えではない。

## SG6. actual Frobenius fiber の正性と、その範囲

CC25 Proposition 3.4 は
\[
 \pi^{-1}(C_p)\simeq
 (\mathbb R_+^\times\times H_p)/p^{\mathbb Z},
 \quad H_p=\prod_{q\ne p}\mathbb Z_q^\times,\qquad
 (r,h)\sim(pr,ph)                                             \tag{16}
\]
を与える。[版固定原文 §3.1](https://arxiv.org/html/2501.06560v1#S3.SS1)
正の \(r\)-scaling を時間正方向に取り、section \(r=1\) に戻すと
\([p,h]=[1,p^{-1}h]\) なので return は \(h\mapsto p^{-1}h\)。原文の mapping-torus generator / arithmetic Frobenius \(p\) との表記差は向きの選択による。Theorems 3.9, 3.12 の abelian Galois interpretation は同一論文の算術入力である。

乗法平行移動 \(h\mapsto p^{\pm1}h\) は compact group \(H_p\) の正規化 Haar measure を保存する。従って
\[
 (K_pF)(h)=F(p^{-1}h)
 \quad\text{は }L^2(H_p,dh)\text{ 上 unitary}.                 \tag{17}
\]
同じことは Haar と有限長 \(dt\) を用いた mapping-torus suspension の Koopman 群にも成り立つ。これは独立に成立する局所の正性である。

しかし (17) は fiber translation の表現であり、有限体曲線の polarized \(H^1\) の重さ1純性ではない。まして (1) の全零点商と同一でない。\(K_p\) に形式的に \(p^{-1/2}\) を掛けるとむしろ strict contraction となり、零点表現の半密度正規化を局所 Haar 表現へ無差別に移せない。全零点を保持する intertwiner、Gamma/極項、同じ adjoint の比較が欠けている。

## SG7. 最小反例：同じ prime periods と保存則は drift を禁じない

\(a>0\) を固定し、
\[
 X(u)=\begin{pmatrix}e^{au}&0\\0&e^{-au}\end{pmatrix},\quad
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 B=R=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
直接計算で
\[
 X(u)^TJX(u)=J,\quad \det X(u)=1,\quad
 X(u)^TBX(u)=B,\quad RX(u)R=X(-u).                             \tag{18}
\]
従って symplectic、体積保存、非退化な二次保存量 \(2v_1v_2\)、time reversal を全て持つ。指数は \(+a,-a\)。

各 actual prime \(p\) に対して base circle
\(\mathbb R/(\log p)\mathbb Z\) 上の cocycle
\[
 (\theta,v)\longmapsto
       (\theta+u\bmod\log p,\ X(u)v)
\]
を置く。base の primitive length はちょうど \(\log p\)、monodromy は
\(M_p=\operatorname{diag}(p^a,p^{-a})\)、\(k\)-fold return は \(M_p^k\)。
これは実際の算術 fiber や ζ の cohomology を構成した例ではなく、**period と (18) から純性を推論する論理への反例**である。

この base の無重み orbit product は、絶対収束する \(\Re s>1\) で
\(\sum_{p,k}e^{-sk\log p}/k=\log\zeta(s)\) を再現できる。一方、追加した vector cocycle の trace 重みは \(p^{ka}+p^{-ka}\) となり、actual ζ の trace ではない。base Euler log を保ったことは、zero spectrum の同定を保ったことではない。

正の \(G_0\) で \(M_p^TG_0M_p=G_0\) は不可能。固有ベクトル \(e_1\) に適用すると \(p^{2a}\|e_1\|_{G_0}^2=\|e_1\|_{G_0}^2\) と矛盾する。時間依存 \(G(u)=\operatorname{diag}(e^{-2au},e^{2au})\) は transport を等長にできるが、periodic でも uniformly coercive でもない。任意の正 metric の存在と、流れに不変な正 metric の存在は異なる。

### SG7.1. actual Weil 保存形式も正性を自動供給しない

実際の test space には
\[
 Q_W(f,g)=\sum_\rho m_\rho\,
       \widehat f(\rho)\,
       \overline{\widehat g(1-\bar\rho)}
                                                               \tag{19}
\]
という自然な Hermitian trace pairing がある。test-space decay と零点計数により和は絶対収束し、(5) により各項の指数が相殺され
\[
 Q_W(W_uf,W_ug)=Q_W(f,g).                                     \tag{20}
\]
off-line pair \(\lambda,\,-\bar\lambda\) でもこの相殺は成立する。対応する二次元 pairing は非対角の不定 \(J\)-型でよい。従って (20) は無条件だが、(19) の全 test positivity は既知の Weil criterion、すなわち RH と同値である。[CCM07, Proposition 6.2 / Corollary 6.3](https://arxiv.org/pdf/math/0703392v1)

## SG8. 要求された candidate fields と判定

| Field | 全零点 scaling 表現に正 metric を作る候補 | 局所 Frobenius Haar metric の転用候補 |
|---|---|---|
| Continuous flow | SG1 の \(W_u\)。位相的群として既知 | (16) の suspension / Koopman flow |
| Prime periodic orbit | 算術空間の \(C_p\)。本ノートでは source 確認に限定 | (16) の base orbit |
| Orbit length | \(\log p\) | 同じ |
| Prime-power iterates | \(k\log p\)、Euler log は \(\Re s>1\) で exact | return の \(k\) 乗 |
| Frobenius relationship | 算術 cohomology の scaling と fiber monodromy の同一視は別義務 | 向きを固定した \(p\) / \(p^{-1}\) の abelian monodromy は exact |
| Normalized flow | \(e^{-u/2}\vartheta_u\) | Haar Koopman は既に unitary。半密度を同じ意味で再挿入しない |
| Candidate transverse exponent | spectral-character exponent (6)。tangent exponent は未構成 | profinite tangent exponent は未定義 |
| Relation to Re(rho)-1/2 | 全零点商の連続双対上で exact | 未同定 |
| Invariant metric | 不変 Hermitian 形式 (19) はあるが正性未証明 | \(L^2(H_p,dh)\) は正で return は unitary |
| Arithmetic source of metric | Weil trace / explicit formula。ただし positivity は既知 RH 同値 | compact-group Haar measure |
| Known prior art | CCM07 / Meyer03。既知 trace realization を再利用 | CC25 mapping torus / abelian class field interpretation |
| New content | 完備化・有界双対保持・一周期条件の監査整理。新定理主張なし | scope の切り分けのみ |
| RH-equivalent assumption? | (19) の全域正性は YES。任意別 metric は SG3 を満たせば RH を含意するが一般の逆は未証明 | 局所 unitary 自体は NO。全零点への faithful unitary transfer を加えれば RH を含意 |
| Counterexample status | SG7 が保存則・対称性だけの推論を否定 | 別 fiber の unitary を共通全零点表現へ移す定理なし。actual CC 構成への反例ではない |
| Decision | 新しい正 metric がないため Level 4 の候補として STOP | 局所既知結果として KEEP、全域 metric の代用として STOP |

**到達レベル。** Level 1 の monodromy は既知定理。Level 2–3 は spectral-character の意味で既知構成上に厳密化できるが、幾何学的 transverse tangent との同定は未達。Level 4–5 は未達。

Berry–Keating、Connes 初期 Hilbert realization、scaling Hamiltonian、scaling site、Deninger、dynamical zeta、Selberg、Gutzwiller との八項比較は、同巡の [program_comparison.md](program_comparison.md) に分担した。本ノートが利用するのは CCM の全零点位相的表現であり、裸の dilation の自己共役性、半局所 cutoff trace、または semiclassical orbit correspondence を全零点 Hilbert 同定へ格上げしない。

**最小の未解決 bridge。** 零点を定義入力にしない算術構成から、(i) 正規化群の不変正形式、(ii) その norm での強連続性、(iii) 全零点の非零 character に対する (9) を、同じ算術 quotient 上で得る必要がある。特定の周期の unitary return で置き換えるなら、SG5 の同じ空間・忠実性・局所有界性が必要となる。いずれも本巡では得られていない。

**独立確認の範囲。** DESTROYER が SG3 の含意と SG5 の一周期・平均内積補題を別計算で確認した。SG5 は全整数冪、局所有界性、逆時間下界、被積分関数の周期性を含む PASS。一次文献の全証明を再検証したという意味ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/scale_flow/notes/program_comparison.md`](program_comparison.md)
