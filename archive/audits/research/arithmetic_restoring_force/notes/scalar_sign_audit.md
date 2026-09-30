**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_restoring_force/notes/scalar_sign_audit.md` · Original SHA-256: `1d6cd61bb2a0c418ef44319162dfcd98de2868406a59501299ac393ed3aa92f6`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic restoring force — scalar 符号・曲率の独立監査

2026-09-30 JST。Track A の限定監査。標準の完成 ξ を固定する。新しい作用素・位相・計量を導入せず、旧ファイルを変更しない。以下の解析的反例と RH 同値条件を区別する。RH の証明・反証、新規性の主張はない。

## S1. 規約・正確な完成対数微分

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
s=\frac12+a+it,\quad X(z)=\xi(\tfrac12+z).
\]
\(X\) は実係数の偶整関数。零点以外で
\[
U(a,t)=\log|\xi(\tfrac12+a+it)|,\qquad q(s)=\xi'(s)/\xi(s)
\]
と置く。実数値 U に複素 log の枝の選択は不要である。
\[
q(s)=\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)},                 \tag{S1}
\]
\[
q'(s)=-\frac1{s^2}-\frac1{(s-1)^2}+\frac14\psi_1(s/2)
+\frac{\zeta''(s)}{\zeta(s)}-\left(\frac{\zeta'(s)}{\zeta(s)}\right)^2.
                                                                    \tag{S2}
\]
個別項の極がある 0,1,負の偶数では、完成 ξ に従って相殺した極限を取る。個別の prime 部分・Gamma 部分を落とした式とは区別する。
\[
U_a=\Re q,\quad U_t=-\Im q,\quad
U_{aa}=\Re q',\quad U_{tt}=-\Re q',\quad U_{at}=-\Im q'.     \tag{S3}
\]
従って U は零点以外で調和的。二変数 Hessian の固有値は \(\pm|q'|\) であり、水平凸性と二変数の凸性も同一ではない。

完成関数の定義・反射規約は [DLMF 25.4](https://dlmf.nist.gov/25.4)、対数微分と水平微分の関係は Matiyasevich–Saidak–Zvengrowski, Lemma 2.1 と §3 に一致する。[一次論文 v1](https://arxiv.org/pdf/1205.2773)

## S2. 対称性が与えるもの

\[
q(1-s)=-q(s),\qquad q(\overline s)=\overline{q(s)},\qquad
U(-a,t)=U(a,t)=U(a,-t).
\]
特に \(\xi(1/2+it)\ne0\) なら \(\Re q(1/2+it)=0\)。これは **中心で一階微分がゼロ**という恒等式で、二階微分の正性、全水平線での最小性、全零点の中心線所属は導かない。

ξ の零点 \(\rho\) の重複度を \(m\ge1\) とすると
\[
q(s)=\frac m{s-\rho}+\frac{h'(s)}{h(s)},\qquad
\xi(s)=(s-\rho)^mh(s),\quad h(\rho)\ne0.                 \tag{S4}
\]
零点では q は pole であり、\(q=0\) という有限の equilibrium 条件ではない。\(|\xi|^2\) の微分が零点で消えることと、log-potential がそこで滑らかであることも異なる。

## S3. 全域の「復元方向」一階符号は既知の RH 同値条件

正確な命題は
\[
\boxed{a\Re q(\tfrac12+a+it)>0
\quad\text{for every }a\ne0,t\in\mathbb R
\text{ such that }\xi(\tfrac12+a+it)\ne0.}               \tag{S5}
\]
**(S5) ⇔ RH。** a=0 も strict >0 の対象に含めると、S2 によって誤った命題になる。

RH ⇒ (S5)：正の ordinate γ を重複度込みで並べる。対称 Hadamard product と \(\sum_{\gamma>0}\gamma^{-2}<\infty\) により
\[
X(z)=X(0)\prod_{\gamma>0}\left(1+\frac{z^2}{\gamma^2}\right),
\]
\[
\Re q(\tfrac12+a+it)
=\sum_{\gamma>0}\left[
\frac{a}{a^2+(t-\gamma)^2}+\frac{a}{a^2+(t+\gamma)^2}
\right].                                                    \tag{S6}
\]
零点を避ける compact sets で微分でき、実部の和は絶対収束する。各項の符号は a と一致し、零点は存在するので strict となる。単純零点の仮定は不要。

(S5) ⇒ RH：もし \(\rho=\beta+i\gamma\)、\(\beta>1/2\) が零点なら、十分小さい ε>0 に対し \(s=\rho-\epsilon\) は依然 \(\Re s>1/2\) で零点でない。(S4) より \(\Re q(s)=-m/\epsilon+O(1)<0\) となり矛盾。左半分の零点には \(s=\rho+\epsilon\) を使うか、反射を使えばよい。零点そのものを定義域から除外しても、この局所的矛盾は残る。

これは新しい算術入力ではない。Sondow–Dumitrescu, Theorem 1 / Corollary 1 は zero-free 半平面の水平単調性と RH 同値性を示す。[一次論文](https://arxiv.org/pdf/1005.1104)
Lagarias (1999), Introduction (1.4)–(1.5) にも \(\Re(\xi'/\xi)>0\) の同値条件が明記される。ここで引用するのはこの導入部分だけで、同論文の後続の別の定理を採用していない。[著者公開原稿](https://websites.umich.edu/~lagarias/doc/positivity.pdf)

## S4. 実際に無条件でいえる領域

全零点 \(\rho=\beta+i\gamma\) を使う、共役対でまとめた対数微分から
\[
\Re q(\sigma+it)=\sum_\rho
\frac{\sigma-\beta}{(\sigma-\beta)^2+(t-\gamma)^2}.       \tag{S7}
\]
実部の和は零点以外で絶対収束する。\(0<\beta<1\) なので
\[
\Re q(\sigma+it)>0\ (\sigma\ge1),\qquad
\Re q(\sigma+it)<0\ (\sigma\le0)
\]
は無条件。一般に「すべての零点の実部より右」という half-plane 条件があれば同じ結論になる。ある一点の近傍だけに零点がないことから、この符号を導くのではない。

これらの領域と式は上記 Matiyasevich–Saidak–Zvengrowski §2, Theorem 1.1 の証明 / Corollary 2.5 とも一致する。臨界帯内部の全点へ拡張する段階を既証明扱いしない。

t=0 には別の無条件の正性がある。標準の正の偶 theta kernel Φ を用いた
\[
X(a)=\int_{\mathbb R}\Phi(v)e^{av}dv>0
\]
は全実 a で成り立つ。正規化した tilted measure \(d\nu_a=\Phi(v)e^{av}dv/X(a)\) により
\[
\frac{d^2}{da^2}\log X(a)=\operatorname{Var}_{\nu_a}(v)>0.
                                                                    \tag{S8}
\]
核は一点集中ではなく、全指数 moment が有限なので strict。偶性から \(a\,d\log X(a)/da>0\) for a≠0。

従って \(V=-\log|\xi|\) を potential とした場合、t=0 で中心は strict **最大**であり、\(-\partial_aV=U_a\) は外向きになる。これが \(-\log|\xi|\) を全域で復元 potential と呼ぶ案への actual analytic 反例。反対に \(V=+\log|\xi|\) の force \(-U_a\) が全域で内向きという条件は (S5) そのもので、未証明の RH 同値条件である。

## S5. 曲率：中心、水平全域、二変数を区別

\(F(t)=\xi(1/2+it)\) は実数値の実整関数。F(t)≠0 での中心水平曲率は
\[
\kappa(t)=U_{aa}(0,t)
=-\frac{d^2}{dt^2}\log|F(t)|
=\frac{F'(t)^2-F(t)F''(t)}{F(t)^2}.                       \tag{S9}
\]
分子は古典的な第一 Laguerre expression。RH 下では (S6) から
\[
\kappa(t)=\sum_{\gamma>0}
\left((t-\gamma)^{-2}+(t+\gamma)^{-2}\right)>0
\]
（t が ordinate でない場合）。従って中心曲率の符号変化を「必ず見つかる」と予告してはならない。Laguerre difference を使う既存研究は Csordas–Ruttan–Varga (1991)。ここでは publisher abstract の式と用途を確認し、同論文の全証明を再監査したとは扱わない。[一次出版情報・abstract](https://doi.org/10.1007/BF02142328)

一方、**log|ξ| の全水平凸性は無条件に偽**。既知の臨界線上零点 \(\rho=1/2+i\gamma\) を一つ取り、その重複度を m≥1 とする。十分小さい a≠0 に対し
\[
U(a,\gamma)=m\log|a|+\log|h(\rho+a)|,\qquad
U_{aa}(a,\gamma)=-m/a^2+O(1)<0.                           \tag{S10}
\]
臨界線上零点の既知の存在だけを使い、RH や単純性を仮定しない。[既知の零点事実：DLMF 25.10](https://dlmf.nist.gov/25.10)
S8 の正曲率と S10 の負曲率は異なる t、または中心と非中心での比較。中心曲率がどこか負だと証明したわけではない。

二変数の joint convexity は S3 の調和性でさらに制限される。U または −U が非空 open region 上で凸なら Hessian の trace zero と半正定値性から q'=0 がその region で成り立ち、解析接続により ξ は exponential となって実際の零点と矛盾する。これは水平一変数の凸性とは別の障害である。

**|ξ|² の凸性へ反例を転用しない。** 全 t に対する \(a\mapsto|\xi(1/2+a+it)|^2\) の全域凸性は、実際には RH 同値。RH 下の有限対称 Hadamard product では各対の modulus squared が
\[
\frac{(a^2+(t-\gamma)^2)(a^2+(t+\gamma)^2)}{\gamma^4}
\]
で、全積は a² の非負係数多項式となる。局所一様極限と微分で凸性が従う。逆に偶・非負の凸 profile が ±a₀≠0 でゼロなら、その間全部でゼロになり整関数の孤立零点性に反する。既知 Jensen/Pólya 型条件であり、上記 2012 論文 §2, Corollary 2.5 後の説明にも記載される。

## S6. 全中心点での strict local minimum だけでは足りない模型

ROOT 提案を独立検算した次の模型を、actual ξ と分離して記録する：
\[
F_{\rm syn}(w)=\cos(10w)P(w),\quad
P(w)=((w-1)^2+1/16)((w+1)^2+1/16),\quad
X_{\rm syn}(z)=F_{\rm syn}(-iz).
\]
実・偶・order 1 であり、F_syn は \(w=\pm1\pm i/4\) に非実零点を持つ。従って X_syn の off-axis quartet は \(z=\pm1/4\pm i\) にある。

実 t では P(t)>0。F_syn(t)≠0 なら
\[
-\frac{d^2}{dt^2}\log|F_{\rm syn}(t)|
=100\sec^2(10t)-(\log P)''(t)\ge100-64=36.
\]
ここで \(\bigl(\log((t-c)^2+b^2)\bigr)''
=2(b^2-(t-c)^2)/((t-c)^2+b^2)^2\le2/b^2=32\)、b=1/4 を二因子に使った。
したがって **全ての正則な中心点**で log modulus は水平 strict local minimum でも、off-axis zero は存在する。これは一般的な中心曲率から全零点へ進む推論への厳密反例。標準 Euler/Gamma、正の theta kernel、実際の ξ を保持する模型とは主張しない。actual ξ の中心曲率条件だけと RH の関係をこの模型だけで決着させない。

## S7. prime log derivative の actual 符号反転

σ>1 では絶対収束して
\[
\Re\frac{\zeta'}{\zeta}(\sigma+it)
=-\sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}\cos(t\log n).   \tag{S11}
\]
係数 Λ(n)≥0 は和全体の一定符号を意味しない。数値計算なしで、同じ σ=4 に両符号があることを示せる。

t=0 では厳密に負。\(t_*=\pi/\log2\) では n=2 項は \(\log2/16\)、残りの絶対値は
\[
\sum_{n\ge3}\frac{\log n}{n^4}
\le\frac{\log3}{81}+\int_3^\infty\frac{\log x}{x^4}dx
=\frac{\log3}{81}+\frac1{27}\left(\frac{\log3}{3}+\frac19\right)
<\frac{41}{1215}.
\]
\(\log2>2/3\)、\(\log3<6/5\) を用いた。前者は log の標準積分下界、後者は \(e^{6/5}>1+6/5+(6/5)^2/2+(6/5)^3/6>3\) から従う。従って
\[
\boxed{\Re\frac{\zeta'}{\zeta}(4+it_*)>
\frac1{24}-\frac{41}{1215}=\frac{77}{9720}>0.}          \tag{S12}
\]
Λ(n)≤log n と decreasing integrand の integral bound だけなので認証数値への依存はない。これは **ζ'/ζ の prime 部分の符号固定**への actual counterexample。S1 の他の完成項を足した ξ'/ξ の σ≥1 における正性とは矛盾しない。

## S8. 停止判定

| 命題 | 判定 |
|---|---|
| symmetry ⇒中心一階微分ゼロ | 無条件・正しい |
| log|ξ| の全域復元方向の一階符号 | 正確に量化すると既知 RH 同値、未証明 |
| −log|ξ| を全域復元 potential とする | t=0 の actual theta 正性で逆符号 |
| log|ξ| の全水平凸性 | 既知の on-line zero の近傍で無条件に偽 |
| 中心曲率 κ の positivity ⇒一般の全零点排除 | S6 の解析模型が反例 |
| |ξ|² の全水平凸性 | log の凸性とは異なる既知 RH 同値条件 |
| 正の Λ 係数 ⇒prime drift の固定符号 | S12 の actual ζ 値で偽 |

数値 grid の通過、中心付近の正曲率、既知の零点なし領域での符号は、S5 の全点量化を供給しない。新しい独立した算術復元評価はこの限定監査から得られていない。
