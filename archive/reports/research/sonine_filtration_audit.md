**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/sonine_filtration_audit.md` · Original SHA-256: `57154ab8795bf1c0068cd523fb3a8c36defb8a3808d1c1a9afbe3ad54a4ea05c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Sonine / canonical chain と actual finite Weil restriction の辞書監査

2026-09-30。Hierarchical Selection Track C。RH OPEN。
旧ファイルは変更しない。既知 framework の照合と直接計算であり、新規性を主張しない。

**判定：一変数の既知 Hilbert chain はある。しかし current \(P_NR_a\) の
Weil energy・ground・階層選択を保存する辞書は得られない。**
自然な log-unitary の下で、Sonine chain と current finite space の直接同定は
非零ベクトル一本についても成立しない。一方、support-only ambient space は
trivial Paley–Wiener chain と正確に同定できる。この二つを混同しない。

## C1. 一次資料・版・監査範囲

1. Jean-François Burnol, *Two complete and minimal systems associated with
   the zeros of the Riemann zeta function*, JTNB **16** (2004), 65–94。
   [公刊原文](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.434.pdf)、
   [DOI](https://doi.org/10.5802/jtnb.434)。
   数式 OCR の欠落は [arXiv:math/0203120v6, 2004-02-24](https://arxiv.org/pdf/math/0203120v6)
   の §§1–3 と照合した。以下は公刊頁を優先し、必要時 v6 頁を併記する。
2. **Masatoshi Suzuki**, *Chains of reproducing kernel Hilbert spaces generated
   by unimodular functions*, AIF **75** (2025), 1463–1508。
   [公刊原文](https://aif.centre-mersenne.org/item/10.5802/aif.3705.pdf)、
   [DOI](https://doi.org/10.5802/aif.3705)。
   複素共役・HB の overbar は
   [arXiv:2012.11121v2, 2023-10-03](https://arxiv.org/html/2012.11121v2)
   と照合した。**以下の定理番号は公刊版**。draft の番号とは異なる。

公刊論文の使用箇所は確認したが、論文全証明の独立再証明とはしない。
以下 C4–C8 の current-object 比較は記載した式からの直接導出。
文献の抽象存在定理を actual cutoff の一様評価として代用しない。

## C2. Burnol の空間・ノルム・zero evaluator

正半直線の \(H=L^2(0,\infty;dx)\) と、unitary involution
\[
 (\mathcal Cg)(x)=2\int_0^\infty\cos(2\pi xy)g(y)\,dy
\]
を使う。right Mellin は \(\widehat g(s)=\int_0^\infty g(x)x^{-s}dx\)。
critical-line norm の測度は \(d\tau/(2\pi)\)。
Burnol §2 pp.70–71 は
\[
 K_b=\{g:g=\mathcal Cg=0\text{ on }(0,b)\},\quad
 L_b=\{g:g,\mathcal Cg\text{ are constant on }(0,b)\}
 \tag{C1}
\]
という closed infinite-dimensional Hilbert subspaces を使う。
これは **lower support gap** であって double upper cutoff ではない。

Theorem 2.1 / Proposition 2.2（§2、v6 p.5）による completed Mellin
\[
 M(g)(s)=\pi^{-s/2}\Gamma(s/2)\widehat g(s)
 \tag{C2}
\]
は \(K_b\) では entire、\(L_b\) では possible poles \(0,1\) のみ。
適切な点・jet evaluation は連続である。
de Branges norm は元の \(L^2(dx)\) norm を運ぶものである。

Theorem 3.1（pp.71–72、v6 p.6）は、全 nontrivial zero \(\rho\) と
\(0\le j<m_\rho\) の evaluators について、
\(L_b\) で minimal iff \(b\le1\)、complete iff \(b\ge1\)、
\(b<1\) で orthogonal complement が co-Poisson subspace であるとする。
Theorems 3.2–3.3（pp.72–73、v6 pp.6–7）は \(K_b\) と
\(\zeta(s)/(s-\rho)^\ell\) の対応も扱う。
**RH も zero simplicity も仮定しない**。全 jets が multiplicity を保持する。

したがって「零点を完備系の添字にする」ことは既知だが、その添字が
self-adjoint operator の実固有値になるという定理ではない。
一般の Sonine-space element の零点と、その空間を生成する structure
functions の零点も別物である（同論文 §8 pp.92–93）。
後者の線上零点を \(\zeta\) に移す同定はここではない。

## C3. Suzuki の仮定と、正値 Hamiltonian が現れる箇所

Fourier convention は \(\mathsf Ff(z)=\int f(x)e^{izx}dx\)。
unimodular \(u\) から
\[
 \mathsf K_u=\mathsf F^{-1}M_u J^\sharp\mathsf F,\qquad
 F^\sharp(z)=\overline{F(\bar z)}
 \tag{C3}
\]
を定義する。Proposition 2.1 p.1468 の \(\mathsf K_u\) は
**antilinear isometric involution**。linear self-adjoint Hamiltonian と読まない。
\(P_t=1_{(-\infty,t)}\)、\(\mathsf K[t]=P_t\mathsf K_uP_t\)。

基礎条件 U1–U2（p.1467）は原点で exponent \(>1/2\) の Hölder regularity、
原点非零値、実軸を含む共役対称 domain 上の meromorphic continuation と
両側 nontangential boundary values。
主要条件 O1–O8（pp.1468–1473）は次の通り。

| 条件 | 本監査で省略できない内容 |
|---|---|
| O1 | ある \(t\) で \(\|\mathsf K[t]\|<1\) |
| O2 | integral equations の解 \(\Phi,\Psi\) の \(t\)-distribution derivatives と Fourier との交換 |
| O3 | \(\Phi(t,t),\Psi(t,t)\) が定義され非零 |
| O4 | \(P_t\mathsf K\delta_t\in L^2\)、または指定 distribution space 上の \(I\pm\mathsf K[t]\) の real-linear kernel が零 |
| O5 | 後述 \(\mathcal V_t(u)\ne0\) となる \(t\) の存在 |
| O6 | 全 \(t<t_0\) で \(\|\mathsf K[t]\|<1\) |
| O7 | 全 \(t<t_0\) で \(\operatorname{Re}(\Phi(t,t)\overline{\Psi(t,t)})>0\) |
| O8 | \(t_0<\infty\) なら \(\mathcal V_{t_0}(u)=0\) |

ここで \(\Phi+\mathsf K P_t\Phi=1\)、\(\Psi-\mathsf K P_t\Psi=1\)。
Theorem 2.2 pp.1470–1471 は O1–O4 から first-order system を作る。
式 (2.9) の Hamiltonian は、\(d=\operatorname{Re}(\Phi\overline\Psi)\) として
\[
 H=\frac1d
 \begin{pmatrix}|\Phi|^2&\operatorname{Im}(\Phi\overline\Psi)\\
 \operatorname{Im}(\Phi\overline\Psi)&|\Psi|^2\end{pmatrix},\qquad \det H=1 .
 \tag{C4}
\]
正定値を保証するのは O7 の正符号である。
unimodularity / formal differential equation だけから正定値化しない。

\[
 \mathcal V_t(u)=L^2[t,\infty)\cap\mathsf K_u L^2[t,\infty),\qquad
 t_0=\sup\{t:\mathcal V_t(u)\ne0\}.
 \tag{C5}
\]
包含写像は isometric、\(t\) 増加で空間は減少する。
Theorem 2.3 p.1471 は O1–O5 と当該 \(t\) の strict norm を使う RKHS 式。
Theorem 2.5 p.1472 は O2–O7 の下の inner/model-space 同定。
Theorem 2.6 p.1473 はさらに O8 と
\(u=M^\sharp/M\)、\(M\) meromorphic、upper half-plane と実軸で holomorphic、
upper half-plane で zero-free を使う。
Theorem 2.8 p.1474 は既に \(E\in\mathbb{HB}\) である入力の逆問題を扱う。
本文の \(\overline{\mathbb{HB}}\) は real zeros を許し、
\(\mathbb{HB}\) は real zeros なしの subclass である。

O6 は各有限 \(t\) の strict inequality であり、一様な margin ではない。
Propositions 7.1, 7.3, 7.4 pp.1504–1506 に追加十分条件があるが、
current \(a,N\) に関する energy/gap estimate は述べていない。
Theorem 2.6 直後も、\(E(t,z)\) 自身の endpoint asymptotic は研究しないと明記する。

## C4. Burnol と Suzuki の間には exact Gamma dictionary がある

これは current finite Weil matrix との同定ではなく、両定義の直接比較である。
\[
 (Jg)(t)=e^{t/2}g(e^t),\qquad
 J:L^2(0,\infty;dx)\longrightarrow L^2(\mathbb R;dt)
 \tag{C6}
\]
は unitary。\(s=1/2-iz\) で \(\mathsf FJg(z)=\widehat g(s)\)。
Burnol §1 式 (7) p.69 は
\[
 \widehat{\mathcal Cg}(s)=\chi(s)\widehat g(1-s),\qquad
 \chi(s)=\pi^{s-1/2}
 \frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\]
よって complex conjugation を \(C_0g=\overline g\) とすると
\[
 J\mathcal C C_0J^{-1}=\mathsf K_{u_\Gamma},\qquad
 u_\Gamma(z)=\pi^{-iz}
 \frac{\Gamma(1/4+iz/2)}{\Gamma(1/4-iz/2)} .
 \tag{C7}
\]
実軸上の modulus は 1、norm は保存される。さらに定義だけから
\[
 \boxed{\mathcal V_t(u_\Gamma)=J K_{e^t}.}
 \tag{C8}
\]
\(u_\Gamma\) は upper poles を持つので inner ではない。
\(\chi=\zeta(s)/\zeta(1-s)\) の functional-equation 表示から
RH を読み取ることもできない。この比では対応する零点情報が消える。

\(M_\Gamma(z)=\pi^{iz/2}\Gamma(1/4-iz/2)\) なら
\(u_\Gamma=M_\Gamma^\sharp/M_\Gamma\)。
これは completed Mellin の Gamma normalization とも一致する。
ただし (C8) の証明は Suzuki の全 technical axioms O2–O8 を
この入力について独立検証したという主張を含まない。

strict norm と uniform margin の差はここで直接示せる。
\(b=e^t\) とすると \(\mathsf K[t]\) の norm は
\[
 \|1_{(0,b)}\mathcal C1_{(0,b)}\|
 \tag{C9}
\]
に等しい。有限 \(b\) では continuous finite-square kernel により compact。
norm 1 が達成されれば、ある非零 \(g\) と \(\mathcal Cg\) がともに
\([0,b]\) に support を持つ。しかし \(\mathcal Cg\) は entire なので不可能。
したがって有限 \(b\) では norm \(<1\)。
他方、固定 compactly supported \(g\ne0\) に対し
\(\|1_{(0,b)}\mathcal Cg\|\to\|g\|\) だから、(C9) は \(b\to\infty\) で 1 に近づく。
この既知型の chain 自体から cutoff-uniform resolvent control は出ない。

## C5. Current arithmetic sum と co-Poisson の exact 接点

current limiting seed \(h\) は Gaussian times polynomial、even self-Fourier、
\(h(0)=\int_0^\infty h=0\) である。
\(S_h(x)=\sum_{n\ge1}h(nx)\)、\(k(t)=e^{t/2}S_h(e^t)\) とする。
\[
 (Ih)(x)=h(1/x)/x,\qquad
 \mathcal P_{\rm co}g(x)=\sum_{n\ge1}\frac{g(x/n)}n-
                       \int_0^\infty\frac{g(y)}y\,dy .
\]
絶対収束を使う直接代入により
\[
 \mathcal P_{\rm co}(Ih)(x)=\frac1x S_h(1/x)=I S_h(x),\qquad
 J\mathcal P_{\rm co}(Ih)(t)=k(-t)=k(t).
 \tag{C10}
\]
\(Ih\) は原点近傍で急減衰し、無限遠で \(O(x^{-3})\) なので必要な二積分も収束する。
これは Burnol §1 式 (4)–(9) pp.68–70 の framework に属する。
Müntz/Mellin の \(\zeta\) factor は既知の算術接点である。

しかし \(Ih\) は \([b,1/b]\) に compact support を持たない。
Burnol §2 の support-gap conclusion を (C10) に適用できない。
実際 \(J^{-1}k=S_h\) は \(x>0\) で nonzero real analytic、
無限遠で零に近づく。したがって任意の区間 \((0,b)\) で零や定数にはならない。
自然な map (C6) の下で \(k\) はどの正 \(b\) の \(K_b,L_b\) の element でもない。
co-Poisson に属する構成と compact-input co-Poisson subspace を区別する。

## C6. Current finite cutoff との直接同定は失敗する

\(E_N(a)\) を \([-a,a]\) 上の periodic Fourier modes \(|n|\le N\) の span、
外側を零として扱う current space とする。
非零 \(p\in E_N(a)\) なら
\[
 J^{-1}p(x)=x^{-1/2}p(\log x),\qquad
 \operatorname{supp}(J^{-1}p)\subset[e^{-a},e^a].
\]
これは compactly supported \(L^1\cap L^2\) なので cosine transform は entire。
もし \(J^{-1}p\in L_b\) なら、その cosine transform は \((0,b)\) で定数。
analytic identity theorem で全域定数となり、Riemann–Lebesgue により定数は 0、
Fourier injectivity により \(p=0\) となる。ゆえに
\[
 \boxed{J^{-1}E_N(a)\cap L_b=\{0\},\qquad
 J^{-1}E_N(a)\cap K_b=\{0\}\quad(b>0).}
 \tag{C11}
\]
同じ証明は support-only \(L^2[-a,a]\) にも使える。

これは **この自然な log-unitary による literal dictionary** の否定であり、
全ての抽象 unitary map や将来の別近似を否定するものではない。
Sonine projection を新たに掛ける操作は現在の finite form を変更する。
Weil form・physical norm・boundary covector・ground projector を同時に保存する
intertwining identity またはその定量誤差は、確認した原典にはない。
また current \(P_N\) は periodic expansion の有限切断で、
full-line Fourier band projector ではない。

## C7. Support-only には exact Paley–Wiener chain がある

反対方向の過大な否定も避ける。\(u\equiv1\) を (C3) に入れれば
\(\mathsf K_1f(t)=\overline{f(-t)}\) なので
\[
 \boxed{\mathcal V_{-a}(1)=L^2[-a,a].}
 \tag{C12}
\]
これは Suzuki §3.1 p.1478 の Paley–Wiener example の平行移動形であり、
physical \(L^2\) norm をそのまま保存する。
したがって「一変数 Hilbert filtration が存在しない」は誤り。

ただし (C12) は全ての compact tests を含む算術非依存の support chain。
\(P_N\) の頻度切断、Weil form、radical の \(k,k'',\ldots\) の区別を
この chain 自身は選択しない。
\(k\) は再生核・構造関数・特別な extremal vector のどれとも同定されていない。
有限次元 Ritz basis の replacement に使うには、新たな norm/form 辞書が必要。

## C8. Bounded decision と未解決の正確な一段

| 求めた bridge | 今回の判定 |
|---|---|
| Burnol Sonine ↔ Suzuki conjugation chain | (C7)–(C8) の exact unitary dictionary |
| Current arithmetic sum ↔ co-Poisson | (C10) は exact、compact-input gap は伴わない |
| Current support-only ambient ↔ one-parameter chain | (C12) は exact Paley–Wiener chain |
| Current finite \(P_NR_a\) ↔ Sonine gap space under natural map | (C11) で literal equality は不成立 |
| Physical norm と actual Weil energy の simultaneous transport | 未供給 |
| Chain が \(k\) を unique selector とする theorem | 未供給 |
| Uniform norm/resolvent/gap bound controlling \(a,N\) limit | 未供給。O6 はその代替ではない |

必要な一段は、actual finite form と既知 chain の間で energy と norm を運び、
残差を current boundary scale より小さく抑える算術的な写像・評価である。
単なる isomorphism of separable Hilbert spaces では足りない。

Suzuki Introduction p.1464 の
\(E_\xi(z)=\xi(1/2-iz)+\xi'(1/2-iz)\in\overline{\mathbb{HB}}\)
は RH と同値である。これを入力として canonical chain を作っても、
不足する global positivity を独立に供給したことにはならない。
Thm 2.8 の real-zero-free HB assumption も省略しない。

**Track C は「既知一変数 chain へ移るだけで hierarchical selection が解決する」
という案を終了する。** (C8), (C10), (C12) は再利用可能な正確な接点として残す。
Burnol/Suzuki の定理を反証したのではなく、current object への未証明適用を退けた。
主 RH graph の距離短縮・新しい全域正値性の証明はない。
