**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/dyadic/notes/dyadic_relations.md` · Original SHA-256: `6cc08be88ba0c5c654f2deaaaa77fbf2043879ec2f94ff5f78ff12399c75e789`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Dyadic Arithmetic Reduction：全アデール拡大、2進格子、偶奇和

2026-09-30。既存ファイルを変更しない限定計算。空間・range は [arithmetic_space.md](../../one_prime/notes/arithmetic_space.md)、Gaussian test は [product_formula_star.md](../../phase4/notes/product_formula_star.md) の規約を固定する。既知恒等式の直接再導出であり、新規性・RH の進展は主張しない。

**結論。** 有理数 \(2^n\) の diagonal adelic scaling は summation 上で恒等作用になるが、実成分だけの scaling は別作用である。後者は compact-unit invariant sector では \(2^{-n}\mathbb Z_2\) への格子拡大に対応し、半密度係数 \(2^{-n/2}\) が残る。有限の偶奇分解と Poisson は exact、算術 range \(W\) は両方向に不変。ただし \(W\) 内の Gaussian についての恒等式は非零商類の reduction ではない。無限 dyadic 展開は pointwise / local smooth には収束しても、固定した全指数重みの test topology では一般に収束しない。

## DR1. 定義と二種類の \(2^n\)

\(\mathbb A=\mathbb A_\mathbb Q\)、実 Fourier 規約
\(\widehat f(y)=\int_{\mathbb R}f(x)e^{-2\pi ixy}dx\) を使う。有限素点は標準文字と自己双対測度、\(\operatorname{vol}(\mathbb Z_p)=1\)。global 加法文字は \(\mathbb Q\) 上自明になるものを固定する。

even Schwartz function \(f\) に対し
\[
 \xi_f=f\otimes\mathbf1_{\widehat{\mathbb Z}},\qquad
 \Theta_f(x)=\sum_{m\in\mathbb Z\setminus\{0\}}f(mx)
            =2\sum_{m\ge1}f(mx),\quad x>0.                    \tag{1}
\]
これは idèle \(x=(x_\infty=x,x_p=1)\) における
\(\Sigma\xi_f(x)=\sum_{q\in\mathbb Q^\times}\xi_f(qx)\) である。有限条件が \(q\in\mathbb Z\) を選ぶため (1) となる。

\(R_a\xi(z)=\xi(a^{-1}z)\)、\(U_a=|a|_{\mathbb A}^{-1/2}R_a\) と置く。
次を区別する。

- \(r_n=2^n\in\mathbb Q^\times\) を **全素点へ diagonal に埋めた idèle**。
- \(a_n=(2^n,1,1,\ldots)\) という **実成分のみを変える idèle**。

積公式から
\[
 |r_n|_{\mathbb A}=2^n\,2^{-n}=1,\qquad
 |a_n|_{\mathbb A}=2^n.                                      \tag{2}
\]
\(n\in\mathbb Z\) に対して
\[
 R_{r_n}\xi_f
 =f(x_\infty/2^n)\otimes\mathbf1_{2^n\mathbb Z_2}
                  \otimes\prod_{p\ne2}\mathbf1_{\mathbb Z_p}.
\]
従って summation では
\[
 \Sigma(R_{r_n}\xi_f)(x)
 =\sum_{m\in2^n\mathbb Z\setminus\{0\}}f(mx/2^n)
 =\Theta_f(x).                                               \tag{3}
\]
一般の adelic test にも \(q\mapsto q/2^n\) の reindexing により成立する。これは \(\mathbb Q^\times\)-coinvariant の既知関係である。

一方、
\[
 \Sigma(U_{a_n}\xi_f)(x)=2^{-n/2}\Theta_f(x/2^n).              \tag{4}
\]
半密度
\[
 \phi_f(t)=e^{t/2}\Theta_f(e^t),\quad L=\log2,\quad
 (T^ng)(t)=g(t-nL)
\]
を使うと (4) は \(\phi_f\mapsto T^n\phi_f\) に対応する。(3) を (4) の恒等性へ読み替えてはいけない。

### DR1.1. 実側 scaling を有限側へ移す正確な形

\(a_n r_n^{-1}\) の実成分は1、全有限成分は \(2^{-n}\)。奇素点の \(2^{-n}\) は unit なので、compact-unit invariant sector では
\[
 [a_n]=[b_n],\quad
 (b_n)_\infty=1,\quad(b_n)_2=2^{-n},\quad(b_n)_p=1\ (p\ne2).
                                                               \tag{5}
\]
従って (4) は
\[
 2^{-n/2}
 f(x_\infty)\otimes\mathbf1_{2^{-n}\mathbb Z_2}
             \otimes\prod_{p\ne2}\mathbf1_{\mathbb Z_p}         \tag{6}
\]
の summation と一致する。ここでは \(q\in2^{-n}\mathbb Z\) を選び、\(|b_n|_{\mathbb A}=2^n\)。実側を戻す際に **2進格子を同時に変えた**ことが本質である。

## DR2. 2進格子、Fourier dual、導手の規約

任意の整数 \(j\) について
\[
 \operatorname{vol}(2^j\mathbb Z_2)=2^{-j},\qquad
 (2^j\mathbb Z_2)^\perp=2^{-j}\mathbb Z_2,
\]
\[
 \mathcal F_2\mathbf1_{2^j\mathbb Z_2}
       =2^{-j}\mathbf1_{2^{-j}\mathbb Z_2}.                   \tag{7}
\]
証明は compact additive subgroup 上の文字の積分：文字が自明なら volume、非自明なら平行移動によって積分がゼロとなる。

test function \(\mathbf1_{2^j\mathbb Z_2}\) の additive translation invariance group は \(2^j\mathbb Z_2\)、Fourier support はその annihilator。文字 \(z\mapsto\psi_2(2^{-n}z)\) の kernel は \(2^n\mathbb Z_2\)。本ノートでの conductor / resolution はこの加法的意味に限定し、Dirichlet / Hecke character の multiplicative conductor を新たに \(2^n\) にしたという意味ではない。

実側の Fourier 係数も同時に保持すると
\[
 \mathcal F_\infty[f(\,\cdot\,/2^n)](y)
       =2^n\widehat f(2^ny).
\]
(7) の \(2^{-n}\) と相殺し、
\[
 \mathcal F_{\mathbb A}R_{r_n}
       =R_{r_n^{-1}}\mathcal F_{\mathbb A}.                   \tag{8}
\]
一般 idèle の公式は \(\mathcal F R_a=|a|_{\mathbb A}R_{a^{-1}}\mathcal F\)。全 diagonal での係数相殺を real-only scaling の式へ流用しない。

次の表は (6) の有限側を列挙したもの。

| \(n\) | 格子 test \(B_n\) | 半密度係数 \(c_n=2^{-n/2}\) | \(\mathcal F_2(c_nB_n)\) |
|---:|---|---|---|
| 1 | \(\mathbf1_{2^{-1}\mathbb Z_2}\) | \(1/\sqrt2\) | \(\sqrt2\,\mathbf1_{2\mathbb Z_2}\) |
| 2 | \(\mathbf1_{2^{-2}\mathbb Z_2}\) | \(1/2\) | \(2\,\mathbf1_{4\mathbb Z_2}\) |
| 3 | \(\mathbf1_{2^{-3}\mathbb Z_2}\) | \(1/(2\sqrt2)\) | \(2\sqrt2\,\mathbf1_{8\mathbb Z_2}\) |
| 4 | \(\mathbf1_{2^{-4}\mathbb Z_2}\) | \(1/4\) | \(4\,\mathbf1_{16\mathbb Z_2}\) |

各 \(c_nB_n\) の additive \(L^2(\mathbb Q_2)\) norm は1。これは正しい ambient normalization であり、全零点商上の norm の同定ではない。

## DR3. 偶奇分解と \(n=1,2,3,4\)

\[
 O_f(x)=\sum_{m\in2\mathbb Z+1}f(mx),\qquad
 \Theta_f(x)=\Theta_f(2x)+O_f(x).                              \tag{9}
\]
Schwartz 性により各 \(x>0\) の和は絶対収束し、有限回の reindexing は正当。反復して
\[
 \boxed{\Theta_f(x/2^n)=\Theta_f(x)
                 +\sum_{j=1}^n O_f(x/2^j)},\qquad n\ge1.     \tag{10}
\]
逆方向も
\[
 \Theta_f(2^nx)=\Theta_f(x)-\sum_{j=0}^{n-1}O_f(2^jx).         \tag{11}
\]

有限側では \(B_0=\mathbf1_{\mathbb Z_2}\) とすると
\[
 B_n=B_0+\sum_{j=1}^n A_j,\qquad
 A_j=\mathbf1_{2^{-j}\mathbb Z_2^\times}=B_j-B_{j-1}.          \tag{12}
\]
\(A_j\) は \(q=2^{-j}m\)、\(m\) odd を選ぶので、(12) の summation が (10)。また
\[
 \mathcal F_2 A_j
   =2^j\mathbf1_{2^j\mathbb Z_2}
      -2^{j-1}\mathbf1_{2^{j-1}\mathbb Z_2}.                  \tag{13}
\]
これは符号付きの差であり、Fourier 側の各 shell を正作用素と扱う根拠ではない。\(A_j\) の additive invariance group は \(2^{1-j}\mathbb Z_2\)、Fourier support は \(2^{j-1}\mathbb Z_2\)。

式を四段まで省略せず書くと
\[
 \begin{aligned}
 \Theta_f(x/2)&=\Theta_f(x)+O_f(x/2),\\
 \Theta_f(x/4)&=\Theta_f(x)+O_f(x/2)+O_f(x/4),\\
 \Theta_f(x/8)&=\Theta_f(x)+O_f(x/2)+O_f(x/4)+O_f(x/8),\\
 \Theta_f(x/16)&=\Theta_f(x)+O_f(x/2)+O_f(x/4)+O_f(x/8)+O_f(x/16).
 \end{aligned}                                                \tag{14}
\]

\(d_j(t)=e^{t/2}O_f(e^t/2^j)\) と置くと normalized return は
\[
 \begin{aligned}
 T\phi_f&=(\phi_f+d_1)/\sqrt2,\\
 T^2\phi_f&=(\phi_f+d_1+d_2)/2,\\
 T^3\phi_f&=(\phi_f+d_1+d_2+d_3)/(2\sqrt2),\\
 T^4\phi_f&=(\phi_f+d_1+d_2+d_3+d_4)/4.
 \end{aligned}                                                \tag{15}
\]
ここで \(d_j\) を \(n\) に依存しない固定符号の error budget として estimate したことはない。

## DR4. Poisson と半密度の反転

まず一般の Schwartz \(f\) には
\[
 f(0)+\Theta_f(x)=x^{-1}\bigl(\widehat f(0)+
                                  \Theta_{\widehat f}(1/x)\bigr). \tag{16}
\]
従って \(f(0)=\widehat f(0)=\int f=0\) を課した arithmetic core では
\[
 \Theta_f(x)=x^{-1}\Theta_{\widehat f}(1/x),\qquad
 \phi_f(t)=\phi_{\widehat f}(-t).                              \tag{17}
\]
極に対応する二つの境界項を、条件を課す前に捨てていない。

odd coset の Poisson は
\[
 O_f(x)=\frac1{2x}\sum_{m\in\mathbb Z}(-1)^m
                               \widehat f\!\left(\frac m{2x}\right).
                                                               \tag{18}
\]
これは格子 \(2x\mathbb Z+x\) の Fourier character \((-1)^m\) から得る。従って
\[
 O_f(x/2^j)=\frac{2^{j-1}}x
        \sum_{m\in\mathbb Z}(-1)^m
                      \widehat f\!\left(\frac{2^{j-1}m}x\right).
                                                               \tag{19}
\]
\(j=1,2,3,4\) の係数と引数の倍率は、それぞれ \(1,2,4,8\)。odd/even summation の dual は無重みの正和ではなく alternating sum である。

\(Jg(t)=g(-t)\) とすれば \(JT^n=T^{-n}J\) であり、
\[
 T^n\phi_f=J T^{-n}\phi_{\widehat f}.                          \tag{20}
\]
この二端点を交換する等式自体は return の norm growth をゼロにしない。

## DR5. \(W\) の両向き不変性

\[
 \mathcal S_{00}^{\rm even}
 =\{f\in\mathcal S(\mathbb R):f\text{ even},\
                                    f(0)=\textstyle\int f=0\}.
\]
\(f\) がこの空間にあれば
\[
 f_n(y)=2^{-n/2}f(y/2^n)
\]
もこの空間にあり、\(f\mapsto f_n\) は逆 \(n\mapsto-n\) を持つ。さらに
\[
 \phi_{f_n}=T^n\phi_f.                                       \tag{21}
\]
よって scalar summation range \(V\) は \(T^nV=V\)（全 \(n\in\mathbb Z\)）を満たす。

全 adelic core でも \(U_{a_n}\) は Schwartz–Bruhat 性を保ち、
\((U_{a_n}\xi)(0)=2^{-n/2}\xi(0)\)、
\(\int U_{a_n}\xi=2^{n/2}\int\xi\) なので、二つの vanishing 条件を保つ。compact-unit 平均はこの scaling と可換である。

固定した \(E\) の seminorm
\[
 p_N(g)=\max_{0\le j\le N}\sup_t
       e^{N|t|}(1+|t|)^N|g^{(j)}(t)|
\]
では
\[
 p_N(T^ng)\le
       2^{N|n|}(1+|n|L)^N p_N(g).                            \tag{22}
\]
従って \(T^n\) は \(E\) の homeomorphism。closure を取り、
\[
 W=\overline V^{\,E},\qquad T^nW=W.                           \tag{23}
\]
これは \(E/W\) 上に群作用が降りることの証明であって、その作用が恒等であることの証明ではない。

## DR6. 指定 Gaussian test の独立確認

\[
 f(x)=P(u)e^{-u},\quad u=\pi x^2,\quad
 P(u)=8u^3-30u^2+15u.                                       \tag{24}
\]
明らかに even Schwartz、\(f(0)=0\)。Gaussian moments
\(\int u e^{-u}dx=\tfrac12\)、
\(\int u^2e^{-u}dx=\tfrac34\)、
\(\int u^3e^{-u}dx=\tfrac{15}{8}\) により \(\int f=0\)。

Fourier は
\[
 \begin{aligned}
 \mathcal F(ue^{-u})&=(\tfrac12-u)e^{-u},\\
 \mathcal F(u^2e^{-u})&=(u^2-3u+\tfrac34)e^{-u},\\
 \mathcal F(u^3e^{-u})&=(-u^3+\tfrac{15}2u^2-\tfrac{45}4u+
                                                 \tfrac{15}8)e^{-u},
 \end{aligned}
\]
ゆえに \(\widehat f=-f\)。従って (17)–(20) は
\[
 \phi_f(-t)=-\phi_f(t),\qquad
 \Theta_f(x/2^n)=-\frac{2^n}{x}\Theta_f(2^n/x).                \tag{25}
\]
この非零 \(\phi_f\) は \(V\subset W\) に属する。実際、\(P(u)>0\) for \(u\ge4\) なので \(x=2\) では (1) の全項が正、\(\phi_f(L)>0\)。

Mellin 側も actual Euler / Gamma 因子を保持している。\(\Re s>1\) で
\[
 \int_0^\infty\Theta_f(x)x^s\,\frac{dx}{x}
 =2\zeta(s)\int_0^\infty f(x)x^s\,\frac{dx}{x}
 =(2s-1)\xi(s).                                             \tag{26}
\]
右の多項式は test に由来し、target ζ を別の函数に置換したものではない。(4) には \(2^{n(s-1/2)}\) が掛かる。

有限側の乗法 Haar を \(\operatorname{vol}^\times(\mathbb Z_2^\times)=1\) とすると
\[
 \int_{\mathbb Q_2^\times}\mathbf1_{2^j\mathbb Z_2}(z)
         |z|_2^s\,d^\times z
       =\frac{2^{-js}}{1-2^{-s}},\quad\Re s>0.                \tag{27}
\]
全 diagonal scaling では real factor \(2^{ns}\) と (27) の \(2^{-ns}\) が相殺する。real-only / (6) では \(2^{n(s-1/2)}\) が残る。odd shell では \(\mathbf1_{\mathbb Z_2^\times}\) の local integral が1なので
\[
 \mathcal M O_f(s)
       =(1-2^{-s})\,\mathcal M\Theta_f(s)
       =(1-2^{-s})(2s-1)\xi(s).                              \tag{28}
\]
\(1-2^{-s}\) は \(0<\Re s<1\) でゼロでなく、この局所因子の除去は非自明零点を消さない。

## DR7. 無限 dyadic 展開が収束する位相・しない位相

この節では \(f\in\mathcal S_{00}^{\rm even}\) を固定する。従って \(\phi_f\in E\subset L^2(dt)\)。pole 条件のない一般 Schwartz test に後述の \(L^2\) 結論を適用しない。

整数の一意分解 \(m=2^j m_{\rm odd}\) により、各 \(x>0\) で
\[
 \Theta_f(x)=\sum_{j\ge0}O_f(2^jx)                            \tag{29}
\]
は絶対収束する。compact \(x\)-interval \([a,b]\subset(0,\infty)\) では Schwartz estimates により全導関数も一様収束する。

\(o_f(t)=e^{t/2}O_f(e^t)\) とすると、\(J\) 項までの exact remainder は
\[
 \phi_f(t)-\sum_{j=0}^{J-1}2^{-j/2}o_f(t+jL)
       =r_J(t):=2^{-J/2}\phi_f(t+JL).                         \tag{30}
\]
従って bare \(L^2(dt)\) では
\[
 \|r_J\|_2=2^{-J/2}\|\phi_f\|_2\longrightarrow0.              \tag{31}
\]

しかし \(E\) の topology では違う。固定 \(t_0\) に対し \(\phi_f(t_0)\ne0\) なら
\[
 p_N(r_J)\ge
 e^{N|t_0-JL|}(1+|t_0-JL|)^N
                  2^{-J/2}|\phi_f(t_0)|.                    \tag{32}
\]
全ての \(N\ge1\) で右辺は発散する。指定 Gaussian では \(t_0=L\) とでき、\(J\ge1\) について正確に
\[
 p_N(r_J)\ge
 2^{-N}2^{(N-1/2)J}(1+(J-1)L)^N\phi_f(L)\longrightarrow\infty.
                                                               \tag{33}
\]
従って (29) の無限和を、そのまま \(E\) での convergent reduction / rearrangement に使えない。

**scope。** この Gaussian の各項・残差は \(W\) 内にあり、quotient seminorm では \(q_N(r_J)=0\)。従って (33) は \(E/W\) の非収束の反例ではなく、test-space topology の異なる極限を混同することへの反例である。商では全て零という計算から、任意の非零商類を制御する評価は出ない。

## DR8. \(W\) の test を消すことと、一般 class reduction の区別

(9) の半密度版は
\[
 o_f=(I-2^{-1/2}T^{-1})\phi_f.                               \tag{34}
\]
\(\phi_f\in W\) と (23) により \(o_f,d_j\in W\)。従って (15) は商では \(0=0\) である。

(34) の右辺を任意の \(g\in E\) に定義すること自体はできるが、それが常に \(W\) に属するという主張は偽。actual zero \(\rho\) に対する非零 Mellin functional を使うと
\[
 \ell_\rho((I-2^{-1/2}T^{-1})g)
       =(1-2^{-\rho})\ell_\rho(g).                           \tag{35}
\]
非自明零点は \(\Re\rho>0\) にあるから \(1-2^{-\rho}\ne0\)。
\(\ell_\rho(g)\ne0\) となる compactly supported smooth \(g\) を選べば、(35) は非零となり、その右辺の test は \(W\) に属さない。これは RH を仮定しない反証である。零点は norm の定義入力にはしておらず、普遍的な range-membership 主張を検査する既知 functional としてのみ使った。

一般 class reduction に必要なのは、任意の \(g\) と \(n\) に対する実際の \(w_{n,g}\in W\) の選択と、例えば
\[
 p_1(T^ng+w_{n,g})
    \le C_\varepsilon2^{\varepsilon|n|}p_{M_\varepsilon}(g)
\]
のような一様算術 estimate である。適切な infimum を介した商版との関係も確認を要する。今回の有限 dyadic identities はその選択・estimate を供給しない。係数 \(2^{-n/2}\)、格子変化、Poisson の alternating sign のいずれも、未証明の正性や一様 bound の代わりにはならない。

**Decision:** (2)–(28) の有限 exact dictionary、\(W\) の両方向不変性、(30)–(33) の topology 診断を保持する。Gaussian range relation から一般 class の subexponential reduction を得る候補は、この計算だけでは成立しない。その不足を隠した普遍化は (35) により棄却する。RH は OPEN。

## DR9. 別の arbitrary-input construction に対する exact recurrence

以上の Gaussian 計算と区別して、[explicit_mobius_reduction.md](explicit_mobius_reduction.md) は任意の \(g\in E\) に actual arithmetic representative を与える。この節はその dyadic recurrence の独立検算である。記号の衝突を避け、\(\mathcal J h(t)=e^{t/2}h(e^t)\)、\(Sf(x)=2\sum_{m\ge1}f(mx)\) とする。

固定した smooth cutoff \(\chi\) は \(x\le1/2\) で0、\(x\ge1\) で1。固定 \(\psi\in C_c^\infty((1/2,1))\) は \(\int_0^\infty\psi=1\)。\(H(x)=x^{-1/2}g(\log x)\)、\(H_a(x)=a^{-1/2}H(x/a)\) に対し
\[
 F_a(x)=\frac12\sum_{m\ge1}\mu(m)H_a(mx),\quad
 c_a=\int_0^\infty\chi(x)F_a(x)dx,\quad
 f_a(x)=\chi(x)F_a(x)-c_a\psi(x)                         \tag{36}
\]
を positive axis 上で定義し、\(f_a\) を even に延長する。固定 \(a>0\) で local absolute convergence と全導関数の収束は \(H\) の両端での任意冪の減衰から従う。cutoff により \(f_a\) は原点近傍で0、無限遠で Schwartz、定義した \(c_a\) により \(\int_{\mathbb R}f_a=0\)。従って \(\mathcal JSf_a\in V\)。

\[
 F_{2a}(x)=2^{-1/2}F_a(x/2),\qquad
 c_{2a}=\sqrt2\int_0^\infty\chi(2y)F_a(y)dy.              \tag{37}
\]
第二式は第一式と \(x=2y\) の変数変換である。\(U_2f(x)=2^{-1/2}f(x/2)\) と置くと
\[
\begin{split}
 k_a(x)&:=f_{2a}(x)-U_2f_a(x)\\
 &=2^{-1/2}[\chi(x)-\chi(x/2)]F_a(x/2)
       -c_{2a}\psi(x)+2^{-1/2}c_a\psi(x/2).              \tag{38}
\end{split}
\]
even extension の \(k_a\) は \(\{1/2\le|x|\le2\}\) に supported である。\(f_{2a}\) と \(U_2f_a\) の積分はそれぞれ0なので \(\int k_a=0\)；原点近傍でも0。よって \(k_a\in\mathcal S_{00}^{\rm even}\) かつ \(\mathcal JSk_a\in W\)。この support 結論は \(f_a\) 自体の compact support を意味しない。

\(a=2^n\)、\(R_n=T^ng-\mathcal JSf_{2^n}\) とすると、\(\mathcal JSU_2f=T\mathcal JSf\) により
\[
 \boxed{R_{n+1}=TR_n-\mathcal JSk_{2^n}.}                 \tag{39}
\]
特に \(R_0=g-\mathcal JSf_1\) から
\[
\begin{aligned}
R_1&=TR_0-\mathcal JSk_1,\\
R_2&=T^2R_0-T\mathcal JSk_1-\mathcal JSk_2,\\
R_3&=T^3R_0-T^2\mathcal JSk_1-T\mathcal JSk_2-\mathcal JSk_4,\\
R_4&=T^4R_0-T^3\mathcal JSk_1-T^2\mathcal JSk_2
                    -T\mathcal JSk_4-\mathcal JSk_8.
\end{aligned}                                             \tag{40}
\]
これは一般 \(g\) に対する representative recurrence であり、Gaussian が \(W\) 内で零になるだけの計算ではない。商では正確に \([R_n]=T^n[g]\) を保つ。\(R_0\) を無断で \(g\) と置換してはならない。

ただし (39) は contraction を意味しない。上記 linked note の elementary absolute estimate は
\[
 |c_a|\le C\sqrt a(1+\log a)p_4(g),\qquad
 p_1(R_n)\le C2^{n/2}(1+n)p_4(g)\quad(a=2^n\ge1)
\]
までであり、subexponential bound ではない。(38) の補正も cutoff と moment restoration の費用を保持する必要がある。この追加構成は DR8 の「有限 Gaussian identities だけでは一般 class の estimate を供給しない」という限定と両立する。DR8 (35) が棄却したのは任意 \(g\) に対する \((I-2^{-1/2}T^{-1})g\in W\) という誤った普遍化であり、(36)–(40) の異なる算術補正ではない。

**追加判定：** (37)–(40) の exact arbitrary-input recurrence を保持。未証明の cancellation を contraction と呼ばない。RH は OPEN。

## 出典と検証範囲

- [CCM, math/0703392v1](https://arxiv.org/pdf/math/0703392v1), Definitions 4.10 / 4.14、Proposition 4.11、Lemma 4.15、(4.41)–(4.45)：指定算術 range、作用、半密度正規化。
- [Kudla, *Tate’s Thesis*](https://u.cs.biu.ac.il/~reznikov/courses/kudla-1.pdf), §1 (1.1)、§2 product formula、§3 Fourier / 自己双対測度、§4 Poisson と zeta integral：規約の照合。著者講義資料であり、Tate1950原論文の全面監査とはしない。
- Gaussian Fourier、多項式 moments、有限 \(n=1,2,3,4\) の係数、残差の \(p_N\) 下界は本ノートで直接計算した。外部論文の新しい RH claim は採用していない。
- DR7 の remainder、\(p_N\) 発散、Gaussian の \(\phi_f(\log2)>0\) は DESTROYER が独立に検算して PASS。商内では全て零であるという scope も確認された。DR9 は root の別構成の scaling・support・moment・recurrence を独立に検算したもので、その構成の全解析的 estimate の再監査とは区別する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/dyadic/notes/explicit_mobius_reduction.md`](explicit_mobius_reduction.md)
- [`research/one_prime/notes/arithmetic_space.md`](../../one_prime/notes/arithmetic_space.md)
- [`research/phase4/notes/product_formula_star.md`](../../phase4/notes/product_formula_star.md)
