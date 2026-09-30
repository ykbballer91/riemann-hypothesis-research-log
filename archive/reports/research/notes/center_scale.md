**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/center_scale.md` · Original SHA-256: `ea656741f911396c8e0e22f7523bdffad16d5a14ae3d1749355798f121bdd5dd`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 中心化と尺度作用の監査ノート — 追加探索 A/B

作成日: 2026-09-29。状態: 無条件の規約・補題・反例と、未証明の追加条件の切り分け。
このノートは RH の証明でも、新規性の主張でもない。着想を与えた原資料は数学的根拠として使用していない。出典は下記の一次文献、計算は本文で検証可能な形で示す。既存の証明 graph への変更はない。

## 0. 判定と記号

| ID | 検査対象 | 判定 |
|---|---|---|
| A1 | 中心対称性だけで全零点が臨界線に固定される | 反例により棄却 |
| A2 | 正の偶関数を核とする積分表示なら全零点が臨界線上 | 反例により棄却 |
| B1 | 尺度作用の unitary 性が重みによらず `1/2` を選ぶ | 棄却。`L²(dx)` を固定すると補正項は `1/2` |
| B2 | 裸の dilation 生成子、または固定有限区間への単純な切断が ζ 零点作用素になる | 明示スペクトルにより棄却 |
| C1 | 全零点を重複度付きで同定する自己共役作用素が存在する | 裸の存在命題は RH と同値。独立な算術的構成が未完成 |
| C2 | 全 Weil 形式を Hilbert 空間の内積に因子分解する | RH と同値。規約と研究目標としてのみ採用 |

以下、標準の完成関数を

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad z=s-\tfrac12,\qquad \Xi(z)=\xi(\tfrac12+z)
\]

とする。本ノートの `Xi(z)` は「中心化した複素変数」の関数であり、別の慣習で `Xi(t)=xi(1/2+it)` と書く関数とは引数が異なる。後者はここでは `E(w)=Xi(iw)` と書く。`z` 平面の臨界線は `iR`、`w` 平面の対応する軸は `R` である。

非自明零点 `rho` は重複度付きで数え、

\[
 z_\rho=(\rho-\tfrac12)/i
          =\Im\rho-i(\Re\rho-\tfrac12)
\]

は `w` 平面の零点座標とする。中心座標 `z=rho-1/2` と添字付き `z_rho` を混同しない。

## 1. A1 — 固定点と固定集合を区別する

### 1.1 無条件の対称性

既知の関数等式と実型性は

\[
 \xi(1-s)=\xi(s),\qquad
 \xi(\overline{s})=\overline{\xi(s)}
\]

である。後者は `Re s>1` の実係数 Dirichlet 級数から解析接続で従う。前者の一次出典は [Riemann (1859), Wilkins 英訳](https://www.claymath.org/wp-content/uploads/2023/04/Wilkins-translation.pdf) の関数等式の導出である。中心化すると

\[
 \Xi(-z)=\Xi(z),\qquad
 \Xi(\overline z)=\overline{\Xi(z)},\qquad
 \Xi(-\overline z)=\overline{\Xi(z)}.                 \tag{A1.1}
\]

したがって零点集合は次の二つの involution で不変になる。

| 写像 | 種類 | 固定集合 |
|---|---|---|
| `H(z)=-z` | holomorphic | `{0}` |
| `R(z)=-conj(z)` | anti-holomorphic | `iR` |

実際、`H(z)=z` は `2z=0`、`R(z)=z` は `2 Re z=0` と同値である。元の座標で後者は `s -> 1-conj(s)`、固定集合は `Re s=1/2`。**集合が写像で不変であることは、その集合の各点が固定点であることを意味しない。** 一般の零点は四点軌道 `{z,-z,conj(z),-conj(z)}` を作りうる。また `Xi(it)` が実数になることも (A1.1) の帰結にすぎない。

### 1.2 正確な候補命題と反例

候補 A1:「非零 entire function `F` が `F(-z)=F(z)` と `F(conj(z))=conj(F(z))` を満たせば、その全零点は `iR` にある」。これは偽である。

`0<a<1/2`, `b>0` に対して

\[
 P_{a,b}(z)=((z-a)^2+b^2)((z+a)^2+b^2)
           =z^4+2(b^2-a^2)z^2+(a^2+b^2)^2             \tag{A1.2}
\]

は実係数の偶多項式で、零点は `±a±ib`。すべて臨界帯 `|Re z|<1/2` にあり、どれも臨界線にない。これは ζ 自体や Euler 積を備えた関数の反例ではなく、上記二対称性からの推論を反証する。

**Prior art.** 対称性の出発点は上記 Riemann の関数等式である。`XP` 型の対称性と零点のスペクトル同定を区別して扱う一次研究は [Berry–Keating (1999), abstract](https://epubs.siam.org/doi/abs/10.1137/S0036144598347497)。ここで (A1.2) を新しい反例として主張しない。

**Numerical falsification plan.** 有理 `a=1/4,b=1` で四根を代入し、対称性と `Re z=±1/4` を検査する。数値根探索より因数表示の直接代入を優先する。実行した二進浮動小数点 sanity check では `P(1/4+i)=0`。証明は (A1.2) で完結する。

**Adoption.** 中心化は規約として採用する。零点が個別に `R` に固定される、すなわち `Z(Xi)⊂Fix(R)` を追加仮定すれば、それは **RH そのもの**であり、対称性から得た補題として採用しない。

## 2. A2 — 正の偶 kernel という追加条件も足りない

候補 A2:「`k∈C_c^∞(R)` が偶、非負、非零なら、両側 Laplace 変換 `L_k(z)=∫k(u)e^{zu}du` の全零点は `iR` 上」。これも偽である。

偶・非負・非零な `h∈C_c^∞(R)` と `0<a<1/2` を取り、

\[
 k(u)=\cosh(a)h(u)+\tfrac12h(u-1)+\tfrac12h(u+1),
 \qquad H(z)=\int_{\mathbb R}h(u)e^{zu}\,du
\]

と置く。`k` は候補の全仮定を満たし、変数変換だけで

\[
 L_k(z)=H(z)(\cosh(a)+\cosh z).                       \tag{A2.1}
\]

`cosh(±a+(2n+1)πi)=-cosh(a)` なので、`L_k` は臨界線外の `±a+(2n+1)πi` に必ず零点を持つ。`H` は entire なので、この因子の零点が極との相殺で消えることはない。`L_k(0)>0` より恒等的零でもない。核を正の測度に緩めれば、`cosh(a)δ_0+(δ_1+δ_{-1})/2` 自体がさらに単純な反例になる。

この反例の変数は **Laplace の `z`** である。Fourier 変数 `w` にすると `L_k(iw)` の因子は `cosh(a)+cos w`、その零点は非実数になる。軸を取り違えてはいけない。核の点ごとの非負性は Weil 形式の全 test function に対する非負性とも異なる。

**Prior art.** ξ の Fourier kernel と、その変形の全実零点性を研究する一次文献は [Rodgers–Tao, arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5)。同論文が扱う特定の theta kernel の零点制御は、任意の非負偶 kernel の定理ではない。一般論をそのまま ξ に適用できるとは扱わない。

**Numerical falsification plan.** `a=1/4` と固定 bump `h` を使い、`z=1/4+πi` で (A2.1) の残差を調べる。積分を直接計算する場合は区間分割と誤差保証を付ける。実行した因子のみの sanity check では `cosh(1/4)+cosh(1/4+πi)` の絶対値は約 `3.1×10^-17`。丸め誤差を含む確認であり、厳密な零点性の根拠は加法公式である。

**Adoption.** 一般的な正 kernel からの実零点性推論は棄却する。ξ 固有の追加構造を使うなら、その構造と必要な定理を別途特定する必要がある。例えば既知の熱変形における `Lambda≤0` を仮定することは RH の同値命題の再導入であり、核の正性からの帰結ではない。

## 3. B1 — 任意の重みで成立する Mellin / dilation の定理

### 3.1 空間と unitary 座標変換

任意の **実数** `beta` について

\[
 \mathcal H_\beta=L^2((0,\infty),x^{2\beta-1}\,dx),
 \quad (V_\beta f)(u)=e^{\beta u}f(e^u)
\]

と定める。`x=e^u` で

\[
 \|V_\beta f\|_2^2
 =\int_{\mathbb R}e^{2\beta u}|f(e^u)|^2du
 =\int_0^\infty |f(x)|^2x^{2\beta-1}dx.
\]

逆写像は `(V_beta^-1 g)(x)=x^-beta g(log x)` だから、`V_beta` は onto unitary である。そこで

\[
 (U_t^{(\beta)}f)(x)=e^{\beta t}f(e^t x),\qquad t\in\mathbb R
                                                               \tag{B1.1}
\]

とすると、

\[
 V_\beta U_t^{(\beta)}V_\beta^{-1}g(u)=g(u+t).          \tag{B1.2}
\]

右辺は強連続 unitary 群なので左辺も同様である。強連続性はまず `C_c^∞(R)` 上で平行移動の連続性を示し、その稠密性と等長性から `L²` 全体へ延長すればよい。

実係数 `c` を使う `e^{ct}f(e^t x)` がこの空間で unitary になる条件は `c=beta`。実際、そのノルム二乗は `e^{2(c-beta)t}||f||²` になる。複素係数まで許せば位相 `e^{iτt}` の自由度が残る。以下はこの位相を `1` とする規約である。

### 3.2 生成子の式だけでなく domain を固定する

本ノートは `U_t=e^{itA_beta}` とする。この符号規約で

\[
 A_\beta f=-i(xf'(x)+\beta f(x)),\qquad
 \mathcal D(A_\beta)=V_\beta^{-1}H^1(\mathbb R).        \tag{B1.3}
\]

微分は弱微分で解釈する。滑らかな compact support 上では

\[
 \frac d{du}(e^{\beta u}f(e^u))
   =e^{\beta u}(e^uf'(e^u)+\beta f(e^u)),
\]

なので `V_beta A_beta V_beta^-1=-i d/du`。この計算だけで自己共役性を主張するのではなく、次の Fourier 表示で domain も確認する。

\[
 (\mathcal Fg)(\lambda)=(2\pi)^{-1/2}
           \int_{\mathbb R}g(u)e^{-i\lambda u}du,
 \quad \mathcal M_\beta=\mathcal F V_\beta.
\]

Plancherel の定理により `M_beta` は `H_beta -> L²(R,dλ)` の unitary。積分可能な test function では

\[
 (\mathcal M_\beta f)(\lambda)
  =(2\pi)^{-1/2}\int_0^\infty f(x)x^{\beta-i\lambda}\frac{dx}{x}.
                                                               \tag{B1.4}
\]

一般の `L²` 元ではこの式は `L²` 延長としての意味を持ち、無条件に各点収束する積分と解釈しない。ここでは Fourier 指数を負にしたので、後述の正指数の `F` とは `M_beta f(lambda)=(2pi)^(-1/2)F_{V_beta f}(-lambda)` の関係になる。`beta=1/2` で複素 Mellin 変数を `s=rho` とする形式的な対応は `lambda=-z_rho` であり、符号を無断で同一視しない。部分積分から

\[
 \mathcal M_\beta A_\beta\mathcal M_\beta^{-1}=M_\lambda,
 \quad \mathcal D(M_\lambda)=\{q\in L^2:\lambda q\in L^2\},
 \quad \mathcal M_\beta U_t^{(\beta)}f
       =e^{i\lambda t}\mathcal M_\beta f.                       \tag{B1.5}
\]

実変数の乗算作用素 `M_lambda` はこの domain で自己共役である。例えば対称性に加え、`M_lambda±i` の逆が有界な乗算 `1/(lambda±i)` で全 `L²` 上に存在することから確認できる。Fourier 側の domain は log 側の `H¹` に一致する。`C_c^∞(R)` は cutoff と mollifier により `H¹` で稠密、したがって graph norm で core。`V_beta` で戻すと `C_c^∞(0,∞)` は `A_beta` の core であり、その上の微分作用素の閉包が (B1.3) になる。`H_beta` 全体を微分作用素の domain と書いてはいけない。

### 3.3 Inversion と二種類の反射

線形写像

\[
 (J_\beta f)(x)=x^{-2\beta}f(1/x)                      \tag{B1.6}
\]

に対して `V_beta J_beta V_beta^-1 g(u)=g(-u)`。よって `J_beta` は線形 unitary、`J_beta²=I`、`J_beta*=J_beta` であり、

\[
 J_\beta U_t^{(\beta)}J_\beta=U_{-t}^{(\beta)},
 \quad J_\beta\mathcal D(A_\beta)=\mathcal D(A_\beta),
 \quad J_\beta A_\beta J_\beta=-A_\beta.                \tag{B1.7}
\]

また `M_beta J_beta f(lambda)=M_beta f(-lambda)`。通常の complex Mellin transform `m_f(s)=∫f(x)x^{s-1}dx` を compact support 上で考えると、直接 `y=1/x` により

\[
 m_{J_\beta f}(s)=m_f(2\beta-s).                       \tag{B1.8}
\]

この **holomorphic** な写像 `s -> 2beta-s` の固定点は `beta` のみである。臨界型の縦線 `Re s=beta` が固定集合になるのは **anti-holomorphic** な `s -> 2beta-conj(s)`。

実際、反線形写像 `K_beta f=J_beta(overline f)` を別に定めれば

\[
 m_{K_\beta f}(s)=\overline{m_f(2\beta-\overline s)},
 \quad V_\beta K_\beta V_\beta^{-1}g(u)=\overline{g(-u)}.
\]

`K_beta` は antiunitary involution で、`K_beta A_beta K_beta=A_beta` となる。これと `K_beta U_t K_beta=U_-t` は矛盾しない。反線形性により `i` も `-i` に変わるからである。線形 `J_beta` と反線形 `K_beta` を同じ記号で扱わない。

### 3.4 半密度の `1/2` の正確な意味

任意の実数 `beta,beta'` について

\[
 (W_{\beta\to\beta'}f)(x)=x^{\beta-\beta'}f(x)
\]

は `H_beta -> H_beta'` の unitary である。ノルムの指数を足すと `2(beta-beta')+2beta'-1=2beta-1` になる。さらに `W=V_beta'^-1 V_beta` だから `U,J,A` をそれぞれ intertwine し、domain も保存する。従って、この unitary 表現論だけから特定の `beta` を選び出すことはできない。

`dx` を Hilbert 空間の測度として**先に指定**すれば `2beta-1=0` なので `beta=1/2`。この場合

\[
 U_t f=e^{t/2}f(e^t x),\quad
 A_{1/2}=-i(x\partial_x+\tfrac12),\quad
 J_{1/2}f=x^{-1}f(1/x).
\]

一方、乗法群の Haar 測度 `dx/x` を指定すれば `beta=0` で補正は消える。`1/2` は `dx` と `dx/x` の unitary 変換で現れる半密度の指数である。ζ の関数等式の中心が `1/2` であることは別の算術的事実であり、任意の重みへの unitary 同値が ζ の零点を別の縦線へ動かすという意味ではない。二つの構造を同定する追加の恒等式が必要である。

**Exact conjecture / 判定.** B1 を「unitary dilation と inversion の存在だけで `beta=1/2` が強制される」と定式化すれば偽。上の全 `beta` に対する構成が解析的反例である。「`L²(dx)` における実の正規化係数は `1/2`」は証明済みの規約上の定理。

**Prior art.** [Connes–Consani (2021 author version), (5), (17), Appendix A](https://alainconnes.org/wp-content/uploads/Selecta.pdf) は尺度作用、半密度による Haar 空間への変換、Mellin / Fourier の規約を与える。[Twamley–Milburn, arXiv:quant-ph/0702107v1, (16), (25), (33)](https://arxiv.org/pdf/quant-ph/0702107) にも `-i(x d/dx+1/2)` と log 座標の変換がある。本ノートの domain は上の Fourier 乗算表示で明記しており、形式的な微分式だけには依存しない。

**Numerical falsification plan.** `g(u)=exp(-u²)`、`f_beta(x)=x^-beta g(log x)` を `beta=-1,0,1/2,2` で比較し、(B1.2)、ノルム保存、`J_beta²=I`、`J_beta U_t J_beta=U_-t` を log 座標で検査する。無限区間の積分を実行するなら Gaussian tail の上界を併記する。実行した `u=.7,t=.4` の点値確認では (B1.2) の差は最大約 `5.6×10^-17`。全重みでの等式は上の変数変換が証明する。

**Adoption.** (B1.1)–(B1.8) を規約と基礎補題として採用する。`1/2` が見えたという一致そのものは RH への進展として数えない。

## 4. B2 — 自己共役性から欠けているのは零点との同定

### 4.1 裸の生成子には離散固有値がない

(B1.5) により `sigma(A_beta)=R` で、スペクトルは純絶対連続である。具体的に任意の `f` のスペクトル測度は

\[
 \mu_f(E)=\int_E |\mathcal M_\beta f(\lambda)|^2d\lambda.
\]

`A_beta f=lambda0 f` なら、Mellin 像は一点 `{lambda0}` の外で零。Lebesgue 測度が零なので `f=0`。ゆえに point spectrum は空である。形式的な固有関数

\[
 f_\lambda(x)=x^{-\beta+i\lambda}
\]

は log 座標で `e^{i lambda u}` になり、全実線では `L²` でない。一般化固有関数と Hilbert 空間の固有ベクトルを区別しなければならない。

### 4.2 固定有限区間に切っても零点計数が合わない

log 座標の区間 `[-L,L]`, `L>0` において

\[
 D_\theta=-i\frac d{du},\qquad
 \mathcal D(D_\theta)=\{g\in H^1[-L,L]:g(L)=e^{i\theta}g(-L)\}
                                                               \tag{B2.1}
\]

を取る。内積を第一変数に線形とすると境界形式は

\[
 \langle Dg,h\rangle-\langle g,Dh\rangle
       =-i[g\overline h]_{-L}^{L}.
\]

(B2.1) はこれを消し、同じ境界条件を満たす adjoint domain を与えるため自己共役。あるいは次の完全正規直交系による実対角化でも確認できる。

\[
 g_n(u)=(2L)^{-1/2}e^{i\lambda_nu},\qquad
 \lambda_n=\frac{\theta+2\pi n}{2L},\qquad n\in\mathbb Z.
                                                               \tag{B2.2}
\]

完全性は通常の Fourier 基底に `exp(i theta u/(2L))` を掛けて得られる。反射 `g(u)->g(-u)` は domain の位相を `theta -> -theta` に変える。同じ domain を保つのは `theta=0` または `pi (mod 2pi)`。これらは正負対称なスペクトルを与えるが、いずれも等差数列である。

固定 `L,theta` について正の固有値計数は

\[
 N_{L,\theta}(T)=\frac{L}{\pi}T+O(1).
\]

一方、既知の Riemann–von Mangoldt 公式は

\[
 N_\zeta(T)=\frac T{2\pi}\log\frac T{2\pi}
                    -\frac T{2\pi}+O(\log T).
\]

従って固定有限区間のこの単純なモデルは ζ 零点と一致しない。計数公式の明示的評価を含む一次文献は [Hasanalizade–Shen–Wong, arXiv:2107.06506](https://arxiv.org/abs/2107.06506)。`L=L(T)` と変えて計数の主項を合わせても、それは異なる domain を持つ作用素の族であり、一つの作用素の完全なスペクトル同定にはならない。また両端で `g=0` とする一次微分作用素は対称だが自己共役でないので、その置換も正当化にならない。

**Exact conjecture.** B2 は「(B1.3) の自己共役性、あるいは (B2.1) の自己共役切断と反射対称性だけで、その固有値が全 `z_rho` に一致する」という命題。上記の空の point spectrum / 線形計数が解析的反証である。

**Prior art.** [Berry–Keating (1999)](https://epubs.siam.org/doi/abs/10.1137/S0036144598347497) は `XP` と零点統計の関係を提案する一次研究であり、上の裸の dilation の固有値同定を証明したものではない。[Connes (1998), abstract](https://arxiv.org/abs/math/9811068v1) の構成も臨界零点の absorption spectrum と、仮にある非臨界零点の resonance を区別し、追加の trace formula を必要とする。両者を「自己共役作用素があるので RH は解決」と読み替えない。

**Numerical falsification plan.** 固定 `L,theta` で (B2.2) の正の計数を `T,2T,4T` で比較する。`N(T)/T` がほぼ定数のモデルと、ζ の `log T/(2pi)` の増加は解析的に異なる。有限差分行列を使う場合、その離散固有値がもとの無限直線モデルに実在する点スペクトルだとは扱わず、格子幅と区間幅を別々に変える。

**Adoption.** 裸の生成子・固定区間モデルを RH 証明候補として棄却する。domain を指定した自己共役性とスペクトル計数は、今後の候補を早く棄却する検査として採用する。

## 5. C1 — 追加構造としての「全零点のスペクトル同定」

### 5.1 正確な存在命題と RH 同値性

命題 C1-exist:「ある Hilbert 空間上に自己共役かつ compact resolvent を持つ作用素 `T` が存在し、その固有値 multiset が **全ての** `z_rho=(rho-1/2)/i` と重複度込みで等しい」。この裸の存在命題は **RH と同値**である。

`C1-exist -> RH`: 自己共役作用素の固有値は実数だから `Im z_rho=-(Re rho-1/2)=0`。

`RH -> C1-exist`: RH の下で、全零点の座標を重複度込みで実列 `lambda_n=z_rho_n` に列挙する。零点は有限領域に有限個なので `|lambda_n|->∞` となる列挙ができる。`ell²(N)` 上で

\[
 (Tc)_n=\lambda_nc_n,\quad
 \mathcal D(T)=\{c:\sum_n\lambda_n^2|c_n|^2<\infty\}
\]

とすれば実対角作用素で自己共役。`(T-i)^-1` の対角元 `(lambda_n-i)^-1` は零に収束するため有限 rank 切断で作用素ノルム近似でき、compact。固有値と重複度は構成通りである。

この逆向き構成は零点列を入力しており、RH を証明する独立構成ではない。「素数・既知 kernel などから零点を使わずに指定された特定の `T`」について同定を証明する課題は意味を持つが、その特定の `T` の成功まで RH と同値と断定はしない。RH が真でも任意に提案された `T` が正しいとは限らない。

### 5.2 弱めると偽になる箇所

「固有値が `Im rho`」という同定では足りない。`Im rho` は RH によらず実数であり、(A1.2) の off-axis quartet に対しても `diag(b,b,-b,-b)` は ordinates を重複度込みで実現する。従ってその主張は実部 `1/2` を検出しない。

「最初の N 個の零点に合う」も全零点同定とは異なる。最初の N 個に合わせた対角作用素の後半を任意の実列で延長することは常に可能である。境界条件や cutoff をその有限データに合わせた場合も、算術的な同定の証明にはならない。

**Prior art.** Hilbert–Pólya 型の課題として上記 Berry–Keating と Connes を参照する。近年の具体的な追加条件の例は [Suzuki, arXiv:2606.09096v3, Corollary 1.6](https://arxiv.org/html/2606.09096v3)（2026-09-23 版）である。そこでは有限区間の自己共役性に加え、選ばれたパラメータと上半平面で解析的な因子を伴う (1.12) の局所一様極限を仮定して RH を導く。**その極限はここでは証明していない。** 旧版と仮定を混在させない。

**Numerical falsification plan.** 候補 `T` を零点データへの fitting 前に完全指定する。最初に自己共役 domain、計数の主項、重複度、対称性を検査し、次に近似 resolvent または提案された entire characteristic function と ξ の双方を、軸上だけでなく複素領域で比較する。負の結果は特定候補を棄却しうる。有限個のスペクトル一致、residual の減少、実軸上の plot だけでは全零点同定を認定しない。厳密な反証とするには truncation・丸め誤差の上界が必要。

**Analytic counterexample.** C1-exist 本体に反例を主張しない。それは RH の反証になる。弱い「ordinates だけ」「対称性だけ」「有限一致だけ」に対する反例は上で与えた。

**Adoption.** 必要な追加構造の仕様として採用するが、現時点で独立に定義し同定まで証明した新作用素はない。C1-exist 自体を解決済みの補題にしない。

## 6. C2 — Weil 形式を内積にする追加条件

本プロジェクトの規約に合わせ、`D=C_c^∞(R)` と

\[
 F_f(w)=\int_{\mathbb R}f(u)e^{iwu}du,\qquad
 Q(f,g)=\sum_\rho F_f(z_\rho)
                   \overline{F_g(\overline{z_\rho})}
                                                               \tag{C2.1}
\]

を取る。固定 support 上の絶対収束・連続性は [既存ノート](../../proofs/lemmas/finite_to_infinite.md) で無条件に確認済みである。

命題 C2:「ある Hilbert 空間 `K` と複素線形写像 `B:D->K` が存在し、全 `f,g∈D` について `Q(f,g)=<Bf,Bg>`」。これは **RH と同値**である。C2 なら全 test function で `Q(f,f)>=0` となり、既知の Weil 判定により RH。逆に RH の下では

\[
 Bf=(F_f(z_\rho))_\rho\in\ell^2(\{\rho\})
\]

と取れる。絶対収束評価より `Bf∈ell²`、`z_rho` が実数なので (C2.1) が内積になる。さらに一般の Hermitian form でも、全非負性が既知なら Cauchy–Schwarz により null space を割って完備化するだけで内積表示は作れる。従って「その Hilbert 空間を構成できる」という抽象的存在は非負性を先取りしている。

**Prior art.** [Connes–Consani, Appendix B と導入](https://alainconnes.org/wp-content/uploads/Selecta.pdf) の Weil 判定と圧縮尺度作用による正の汎関数が直接関係する。ただし圧縮された正の汎関数と全 Weil 形式との間には補正項があり、局所結果を全素数・全 support の非負性と同一視できない。[Suzuki v3](https://arxiv.org/html/2606.09096v3) も Weil 形式の作用素論的実現を研究している。既存理論の追試・規約整理として位置付ける。

**Numerical falsification plan.** 独立に与えられた候補 `B` について固定 support の有限 test family を取り、Gram 行列 `Q(phi_k,phi_j)` と `<Bphi_k,Bphi_j>` の差、および最小固有値を誤差上界込みで検査する。候補との不一致はその因子分解を反証する。負の Weil 値を厳密に得るなら RH 反証となるため、零点打切り・素数項・archimedean 項・規約を独立に監査する。有限 family での一致・PSD は C2 の全称命題の証明ではない。

**Analytic counterexample.** C2 本体の反例は主張しない。省略できない弱い条件への反例として `[[1,2],[2,1]]` は各座標では正でも `(1,-1)` に値 `-2` を与える。一般の Hermitian form や尺度作用の存在だけでは内積表示が得られない。また臨界線外で `overline(F_g(conj z_rho))` を `overline(F_g(z_rho))` に取り替えると、証明したい RH を規約に埋め込んでしまう。

**Adoption.** 全 support に対する算術的な恒等式と非負性を要求する仕様としてのみ採用する。全零点が臨界線にあると仮定した sampling 空間や、非負性を仮定した quotient completion を、無条件に構成された RH 証明として提出しない。

## 7. この探索で残る具体的な作業

採用したのは中心座標、重み付き Mellin の符号と domain、反射の線形性の区別、および候補を反証する検査である。棄却したのは、中心対称性・正の偶 kernel・半密度の `1/2`・裸の自己共役性から全零点の所在へ飛躍する推論である。

独立に指定された算術的作用素または因子分解が次に提案された場合は、その全零点同定または全 Weil 形式との恒等式が中心的な未証明命題になる。現時点ではその新しい候補を構成しておらず、RH に対する新たな下界・零点排除領域・証明を得たとは報告しない。このノートの作用素解析と反例は Lean 形式化の既存範囲には追加されていない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/lemmas/finite_to_infinite.md`](../../proofs/lemmas/finite_to_infinite.md)
