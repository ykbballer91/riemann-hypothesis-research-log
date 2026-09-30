**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/one_prime/notes/arithmetic_space.md` · Original SHA-256: `061db89fae3b38e14873b20aeb780368945045a5d7250dc8c88f770db6368cc1`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# One-Prime Return：算術的な商空間と一つの Banach 完備化

2026-09-29。指定版の CCM / Meyer のみを照合。既存 Phase I–IV、scale_flow、state、graph は変更しない。既知定理の全面的再証明や新規性の主張はしない。

**今回の限定 Level 2：** 標準の全指数重み付き test topology から \(q_1\) を選び、全非自明零点の Mellin evaluation と有限 jets を保持する Banach 完備化 \(X_1\) を明示する。\(T_2^{\pm1}\) は bounded。ただし準指数的成長、全商位相との同値性、余分なスペクトルがないことは得ていない。

## 1. 固定した一次資料と定理の範囲

| ID | 指定版・locator | 使用 statement |
|---|---|---|
| CCM | Connes–Consani–Marcolli, *The Weil proof and the geometry of the adeles class space*, [math/0703392v1 PDF](https://arxiv.org/pdf/math/0703392v1), 2007-03-13 | Eq.(4.20), p.20：全実指数重みの交叉。Def.4.10, p.21：cyclic cokernel は range の closure で割る。Prop.4.13 / Def.4.14, p.23：全零点の実現と summation range。Lemma 4.15 / Thm.4.16, pp.24–25：商上の convolution、自然重複度付き trace。 |
| M | Ralf Meyer, *On a representation of the idele class group related to primes and zeros of L-functions*, [math/0311468v1 PDF](https://arxiv.org/pdf/math/0311468v1), 2003-11-26 | Def.4.1, p.24：intersection bornology。Thm.5.1, pp.38–39；Lemmas 5.3–5.5 / Eq.(31), pp.40–42：coinvariants、embedding、Poisson。商の定義 p.43；Thm.5.8, pp.43–44：summability。Prop.5.9, pp.45–46：積分作用の strip 評価。Lemma 5.11 / Thm.5.12, pp.48–50：Mellin 側と全零点・極の代数的重複度。 |

頁は PDF 第 n 頁。M は complete convex bornological spaces を使う。核型性の一般 statement は Thm.2.16, p.12。CCM の一般 cyclic module 全体を一つの Fréchet 空間と呼ばない。本ノートの Fréchet 表示は \(\mathbb Q\) の **compact-unit invariant scalar sector** に限定する。

零点側の規約を明示すると、半密度 flow に対し \(\psi\in C_c^\infty(\mathbb R)\) の場合
\[
\operatorname{Tr}\!\left(\int_{\mathbb R}\psi(v)T_{e^v}\,dv\right)
=\sum_\rho m_\rho\int_{\mathbb R}\psi(v)e^{(\rho-1/2)v}\,dv .
\]
CCM では零点の正の自然重複度、M の virtual representation \(\pi_+\ominus\pi_-\) では極が正、零点が負の supertrace となる。ここでいう trace は核型空間上の積分作用のもの。未積分の \(T_2\) 自体や、後述の \(X_1\) 上の Schatten trace を意味しない。

## 2. 算術 range と topology

\(K_c=\widehat{\mathbb Z}^{\times}\)、\(C_\mathbb Q/K_c\simeq\mathbb R_+^\times\) とする。CCM の scalar test space / arithmetic range は

\[
\mathbf S(C_\mathbb Q)=\bigcap_{\beta\in\mathbb R}|x|^\beta\mathcal S(C_\mathbb Q),
\quad
\mathcal V=\left\{\Sigma\eta(x)=\sum_{a\in\mathbb Q^\times}\eta(ax):
\eta\in\mathcal S(\mathbb A_\mathbb Q),\ \eta(0)=\int\eta=0\right\}.       \tag{1}
\]

Haar 平均 \(P_0\) により \(\mathcal V_0=P_0\mathcal V\) を取る。半密度 log 変数

\[
t=\log x,\qquad g(t)=e^{t/2}h(e^t)
\]

を用いると、test space は
\[
E=\{g\in C^\infty(\mathbb R):p_N(g)<\infty\text{ for every }N\ge1\},
\quad
p_N(g)=\max_{0\le j\le N}\sup_t
e^{N|t|}(1+|t|)^N|g^{(j)}(t)|.                              \tag{2}
\]

これは (1) の通常の weighted Schwartz topology と同値な countable seminorm 系。\(N\ge1\) だけを使う。\(E\) は nuclear Fréchet：\(g\mapsto(e^{kt}g)_{k\in\mathbb Z}\) により Schwartz 空間の可算積の閉部分空間と表示できる。半密度変換を \(J\)、\(V=J\mathcal V_0\)、\(W=\overline V^{\,E}\) とし、

\[
\mathcal Q=E/W,\qquad q_N([g])=\inf_{w\in W}p_N(g+w).        \tag{3}
\]

を採用する。\(q_N\) の族は quotient topology を与え、\(\mathcal Q\) は Hausdorff nuclear Fréchet。個々の \(q_N\) が全ての非零 class を分離するとはここでは仮定しない。

### Meyer の商との比較と閉値域の限定

M の記号では \(\mathcal H_+=\mathcal S(\mathbb A_K)/K^\times\) は coinvariants、すなわち \(\lambda_a f-f\) の **閉線形包**で割った空間。一方 \(\mathcal H_-=\mathcal S(C_K)_{\mathbb R}\)。両者を
\[
\mathcal S(C_K)_{><}=\mathcal S(C_K)_{(1,\infty)}
\oplus\mathcal S(C_K)_{(-\infty,0)}
\]
へ \(i_+(f)=(\Sigma f,J_M\Sigma\mathfrak F^*f)\)、\(i_-(h)=(h,h)\) で埋め、
\[
\mathcal H_-^0=\mathcal H_-/(\mathcal H_+\cap\mathcal H_-)
\]
が零点側、\(\mathcal H_+^0\) が \(0,1\) の極の二次元側となる。ここで \(J_Mh(x)=|x|^{-1}h(x^{-1})\) は本ノートの半密度 \(J\) と別物。bornology の有界性を、単一 Hilbert norm の operator norm に置換しない。

次は **Q の固定 scalar sector だけ**について M の結果から導く帰結であり、CCM の全 cyclic range の一般閉値域定理とは区別する。\(\mathbb Q\) では有限素点の valuation が正有理数で実現するので、M Thm.5.1 の sufficiently-large condition に \(S=\{\infty\}\) を使える。この sector の \(\mathcal H_+\) は \(\mathcal S(\mathbb R)\) の \(\{\pm1\}\)-coinvariants、従って even Schwartz functions に同定される。Lemma 5.4 の bornological embedding はこの Fréchet sector では topological embedding。domain が complete なので image は閉じている。

Poisson Eq.(31) によれば diagonal intersection は \(f(0)=\int_{\mathbb R}f=0\) に正確に対応し、その summation range は
\[
\mathcal V_0=
\left\{x\mapsto2\sum_{n\ge1}f(nx):
f\in\mathcal S(\mathbb R)\text{ even},\quad f(0)=\int_{\mathbb R}f=0\right\}. \tag{4}
\]
\(i_-\) は splitting を持つ embedding なので、この range は \(\mathbf S(\mathbb R_+^\times)\) 内で閉じる。従ってこの限定された sector では \(W=V\) と結論できる。(3) では CCM の closure convention を明示して残す。この議論は critical weighted \(L^2\) の closure とは違う。CCM Prop.6.4(2)/(6.12) のそちらの密度から、ここでの quotient をゼロにしてはならない。

## 3. Mellin evaluation と jets：closure によって失われない

\(\rho\) を非自明零点、\(m_\rho\) をその位数、\(\alpha_\rho=\rho-\tfrac12\)、\(\delta_\rho=\Re\alpha_\rho\) とする。\(|\delta_\rho|<1/2\) は既知の critical-strip inclusion だけを使う。

\[
\ell_{\rho,j}(g)=\int_{\mathbb R}t^j g(t)e^{\alpha_\rho t}\,dt
\quad(j\ge0),\qquad\ell_\rho=\ell_{\rho,0}.                  \tag{5}
\]

これは \(h\) の Mellin transform の \(s=\rho\) における \(j\) 階微分。(4) に対して、まず \(\Re s>1\) で
\[
\widehat{\Sigma f}(s)=2\zeta(s)\int_0^\infty f(x)x^s\,d^\times x.       \tag{6}
\]
右の Mellin integral は \(\Re s>0\) で holomorphic、従って全非自明 \(\rho\) で poles による zero cancellation はない。Poisson と二つの vanishing conditions が両端の急減少を与え、(6) を該当域に継続できる。そのため \(j<m_\rho\) なら \(\ell_{\rho,j}(V)=0\)。

直接の絶対値評価により、\(N>|\delta_\rho|\) なら
\[
|\ell_{\rho,j}(g)|
\le p_N(g)\int_{\mathbb R}|t|^j e^{-(N-|\delta_\rho|)|t|}\,dt
=\frac{2j!}{(N-|\delta_\rho|)^{j+1}}p_N(g).                 \tag{7}
\]
従ってこれらの jets は continuous で \(W\) にも消え、infimum を取って
\[
|\ell_{\rho,j}([g])|
\le\frac{2j!}{(N-|\delta_\rho|)^{j+1}}q_N([g]),
\qquad 0\le j<m_\rho.                                      \tag{8}
\]

特に
\[
|\ell_\rho([g])|\le4q_1([g]),\qquad
|\ell_{\rho,j}([g])|\le2^{j+2}j!\,q_1([g]).                 \tag{9}
\]
定数は零点の高さに依存しない。各 \(\rho\) の finite jet family は非零で線形独立：compactly-supported smooth \(g\) 上で線形結合がゼロなら、対応する exponential polynomial \(e^{\alpha_\rho t}\sum c_jt^j\) が分布としてゼロとなり、全係数が消える。有限個の異なる \(\rho\) を合わせても同様。したがって **closure を取ること自体はこれらの jets を潰さない**。

これは「M の全 quotient が unrestricted な全 jet 列の空間と同型」という主張ではない。M §5.7 は Mellin 側の arithmetic ideal に追加の growth 条件も保持する。全零点・no extras・自然な代数的重複度は M Thm.5.12 / CCM Thm.4.16 の既知 theorem の scope で採用し、(8) だけから全面的な spectral synthesis を主張しない。

## 4. 半密度 \(T_2\)、指数上界、quotient 上界

raw action は \(\vartheta(a)h(x)=h(x/a)\)。CCM Eq.(4.41) に合わせ \(T_a=a^{-1/2}\vartheta(a)\) とすると log variable では
\[
T_ag(t)=g(t-\log a),\qquad T_2^ng(t)=g(t-nL),\quad L=\log2.             \tag{10}
\]
range \(W\) は両方向に invariant。\(1+|t+nL|\le(1+|t|)(1+|n|L)\) から
\[
p_N(T_2^ng)\le2^{N|n|}(1+|n|L)^N p_N(g),                  \tag{11}
\]
\[
q_N(T_2^nx)\le2^{N|n|}(1+|n|L)^N q_N(x).                  \tag{12}
\]
後者は \(T_2^nW=W\) によって infimum を取った結果。(11) の test-space bound と、最適な quotient representative による更なる改善の有無は区別する。

評価汎関数の正確な作用は
\[
\ell_\rho(T_2^nx)=2^{n\alpha_\rho}\ell_\rho(x),
\]
\[
\ell_{\rho,j}(T_2^nx)
=2^{n\alpha_\rho}\sum_{r=0}^j\binom jr(nL)^{j-r}\ell_{\rho,r}(x).       \tag{13}
\]
したがって multiplicity は jet/Jordan chain を伴い得る。単一 \(T_2\) は高さを \(2\pi/\log2\) modulo に alias するため、full flow の零点重複度を \(T_2\) の一つの固有値の重複度に無条件で置換しない。

## 5. \(X_1\)：限定 Level 2 の Banach 実現

\[
X_1=\overline{\mathcal Q/\ker q_1}^{\,q_1}.                 \tag{14}
\]
これは標準 seminorm 系 (2) からの、零点配置に依存しない選択。選択は非一意であり、幾何的に一意な canonical metric と呼ばない。

(12) により \(T_2^{\pm1}\) は \(X_1\) 上の可逆 bounded operator へ一意に延長され、
\[
\|T_2^{\pm1}\|_{X_1}\le2(1+\log2),\qquad
\|T_2^n\|_{X_1}\le2^{|n|}(1+|n|\log2).                    \tag{15}
\]

(8)–(9) により、全零点の非零 \(\ell_\rho\) と \(j<m_\rho\) の独立 jets は \(X_1'\) へ bounded に延長する。その結果 \(2^{\alpha_\rho}\) は \(T_2'\) の固有値、従って \(T_2\) の spectrum に含まれる。これは actual arithmetic quotient からの明示的な保持結果であり、synthetic model ではない。

一方、(14) が full quotient topology と同値、\(\mathcal Q\to X_1\) が単射、\(X_1\) に余分な spectrum がない、という三点は未主張。nuclear Fréchet 商での trace theorem / nuclearity を、この Banach 完備化上の trace-class theorem として転用もしない。

uniform power boundedness は subexponential growth より強い。実際、(13) の非自明 Jordan chains が残るため、全重複度を保持した \(X_1\) に二側 uniform bound を課すなら RH に加えて multiple zeros も排除する。準指数的 bound は polynomial jet growth を許す。

## 6. 既知の強い評価と、実際に欠けている評価

M Prop.5.9 は
\[
\int\pi:\varinjlim_{\epsilon\downarrow0}
\mathcal S(C_K)_{[-\epsilon,1+\epsilon]}
\longrightarrow\ell^1(\mathcal H^0)
\]
という **integrated representation** の boundedness。半密度では重みの端点は \(-1/2-\epsilon,\ 1/2+\epsilon\)。これは nuclear な smoothing/integrated operators への既知の算術的評価であり、\(T_2^n\) 自体への \(X_1\)-operator-norm bound と同じ statement ではない。特に weight type 約 \(1/2\) を type \(0\) と読み替えない。

本課題で十分になる missing estimate の一例は
\[
\forall\epsilon>0\ \exists M\ge1,\ C_\epsilon<\infty:
\quad q_1(T_2^nx)\le C_\epsilon\,2^{\epsilon|n|}q_M(x)
\quad(\forall x\in\mathcal Q,\ \forall n\in\mathbb Z).       \tag{16}
\]

(16) の \(M\) と \(C_\epsilon\) は \(n,x\) に依存してはならない。Banach 版 \(\|T_2^n\|_{X_1}\le C_\epsilon2^{\epsilon|n|}\) はさらに強い要求。既知の (12) では \(2^{N|n|}\) が残る。

実際、(9) と (13) から
\[
q_1(T_2^nx)\ge\tfrac14\,2^{n\delta_\rho}|\ell_\rho(x)|.     \tag{17}
\]
\(\ell_\rho(x)\ne0\) となる \(x\) があるので、(16) は \(n\) の正負を選ぶだけで全 \(\delta_\rho=0\) を強制する。従って、(16) を「既知の連続性」「nuclearity」「閉値域」から既証明へ昇格してはならない。逆に RH から (16)、まして Banach operator-norm 版が従うことも今回の確認では証明していない。

**Decision:** (8)–(15) を、新規性を主張しない限定 Level 2 の具体的構成として保持する。今回の原文照合と直接計算から、RH より弱い前件で (16) を与える新しい算術 growth estimate は得られなかった。欠落は actual quotient representative の二側準指数的制御であり、文献表や formal normalization を増やして代替しない。
