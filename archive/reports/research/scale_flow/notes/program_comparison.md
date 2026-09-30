**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/scale_flow/notes/program_comparison.md` · Original SHA-256: `3d3d2d5a96cd3520b2e55e9c580e8abfe85cf3dc245251af1747c2165e183a97`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Continuous scale flow — 必須8プログラムの独立比較

2026-09-29。DESTROYER。Phase III／IV・主状態は変更しない。
一次資料の指定箇所を照合する限定監査であり、各分野の全成果を網羅した現状調査ではない。
RH は OPEN。既知の prime orbit／Frobenius monodromy は新成果に数えない。

## 1. 比較表：何が exact で、どの spectrum を扱うか

| プログラム | exact な入力／類推の位置 | 正計量・作用の実在 | actual ζ の全零点／不足 |
|---|---|---|---|
| Berry–Keating | \(H_{cl}=xp\)、\(x(t)=e^tx_0,p(t)=e^{-t}p_0\)。phase-space cutoff による平均計数との一致は semiclassical。指定された ζ 系そのものは未同定。[BK §2,§6] | 標準 dilation の自己共役量子化はあるが、裸の系は連続 spectrum。古典 flow 自体には伸長と収縮がある | 正しい arithmetic boundary/domain と全零点同定を要する。平均密度・相関の一致を completeness としない |
| Connes spectral realization | 1999 §III Thm1 は weighted Hilbert quotient に臨界零点を実現。非臨界零点は resonance として区別。2007 の nuclear quotient は全零点 trace を持つ。[C99, CCM07] | 1999 の δ-weighted 作用を unitary と言い切らない。原文は almost unitary。多重零点で Jordan blocks を許す | Thm1 の multiplicity は δ により切られる。2007 全零点・自然重複度と正 Hilbert realization は別の主張 |
| Connes–Consani scaling Hamiltonian | 半局所 \(L^2(X_S)\)、Fourier、cutoff trace の漸近公式は厳密。有限部分の全域 Weil 正性は別段階。[SH19 Thm2.5, Conj4.1] | 正 Hilbert norm と scaling は具体的。cutoff・principal value を含む差の符号を ambient norm から読めない | 全 S／全 support への正性と zero quotient 比較を要する。局所・半局所の実成果を全域 RH としない |
| scaling site／adèle class space | \(C_p=\mathbb R_+^\times/p^\mathbb Z\)、長さ log p。lift は Frobenius 乗法の mapping torus。有限 abelian covers でも arithmetic Frobenius monodromy。[CC24 Thm1.1; CC25 Thm3.12] | compact profinite fibre \(H_p=\prod_{q\ne p}\mathbb Z_q^\times\) の Haar Koopman 作用は unitary。局所計量は既にある | これは weight 0 の compact-group translation。曲線 H¹ の weight 1／全零点 quotient への同定ではない。滑らかな横断面の derivative cocycle を供給したとはしない |
| Deninger flow program | 実際の算術動力空間・局所 Gamma 構成と、global trace／positive-star の予想を区別。[D10; D24] | 指定された Kähler–Riemann 葉層には正 Hodge pairing の実定理がある。[DS02 §4] | actual arithmetic H¹ の全 divisor、正 star、conformal compatibility、domain を同時に結ぶ定理が不足。プログラム全体を単なる RH 同値とは分類しない |
| dynamical zeta functions | 本物の Anosov flow では transfer operator／flat trace／resolvent による厳密理論がある。単なる長さリストより強い仮定を使う。[R76; DZ16] | measure-preserving flow の L² Koopman は unitary でも、Pollicott–Ruelle resonances は異方的 distribution 空間の対象 | ζ(s) と同じ scalar orbit product を書くだけでは、その generator と全算術零点を同定できない。resonance を L² eigenvalue としない |
| Selberg trace formula | 双曲曲面では長さ spectrum と Laplace spectrum を結ぶ厳密式。反復重みには \(2\sinh(k\ell/2)\) が入る。[S, §2下記] | 自然な正 L² metric、正自己共役 Laplacian がある | Riemann ζ の零点との同一性は出ない。非コンパクト modular surface の actual ζ 対応は scattering poles、L² 固有値ではない |
| Gutzwiller periodic-orbit analogy | 一般の孤立周期軌道に対する semiclassical 展開。action、Maslov phase、stability determinant が必要。[G71/G80; BK (2.9)] | quantum Hamiltonian が別途自己共役なら unitary。古典 monodromy は通常 hyperbolic | 一般式は exact Riemann explicit formula ではない。特殊な Selberg 系での exactness を任意 arithmetic flow に移さない |

Connes 1999 の追加限定：§III Theorem1 は \(\delta>1\) で、固有値の multiplicity は
\(n<(1+\delta)/2\) かつ零点次数以下という切り詰めを伴う。
同節直後は多重零点の Jordan form と skew-symmetry の不整合を明記している。
「全零点を完全な自己共役 spectrum にした既知定理」として引用しない。

## 2. orbit logarithm の exact な範囲と、重みの相違

Re s>1 で実際の primitive prime orbits の長さを log p とすると

\[
 \prod_p(1-e^{-s\log p})^{-1}=\zeta(s),\qquad
 \log\zeta(s)=\sum_p\sum_{k\ge1}\frac{e^{-sk\log p}}k.
\]

log は実 s>1 で実値となる枝を採る。絶対収束により展開・交換は正当。
微分して得る正時間 event distribution は
\(\sum_{p,k\ge1}\log p\,\delta_{k\log p}\)。
これは全 finite Euler data を保持する exact な scalar identity である。
一方、Gamma、極0,1、regularization、flow の trace space はこの積にはまだ入っていない。

長さだけを指定した円周の disjoint union でも同じ積を作れる。
従って、この等式単独では genuine Ruelle/Fredholm determinant theorem の仮定、
正しい function space、trace、spectral completeness を供給しない。
これは actual scaling-site construction を synthetic 円周族と同一視する主張ではなく、
scalar identity だけからの推論の不足である。

Ruelle zeta の積を逆数で定義する文献もあるため、規約を固定する必要がある。
DZ16 は \(\prod_{\gamma^\#}(1-e^{i\lambda T_\gamma})\) の規約。
ここで使う逆 Euler 積とは \(\lambda=is\) と逆数の変更を伴う。
generator の符号と resonance parameter の変換を省略しない。

compact hyperbolic surface の Selberg product を

\[
 Z_X(s)=\prod_{\gamma\,\mathrm{primitive}}\prod_{j\ge0}
 (1-e^{-(s+j)\ell_\gamma})
\]

とすれば、収束域で直接展開して

\[
 \log Z_X(s)=-\sum_{\gamma,k\ge1}
 \frac{e^{-sk\ell_\gamma}}{k(1-e^{-k\ell_\gamma})}.
\]

さらに trace formula の hyperbolic orbital term は、標準の conjugacy-class 規約で
\(\ell_\gamma g(k\ell_\gamma)/(2\sinh(k\ell_\gamma/2))\)。
primitive orbit の向きを二重に数えるかで全体の因子を変えないよう規約を固定する。
追加の \(1-e^{-k\ell}\)／stability 因子を落として Riemann の素数和へ同一視できない。
Gutzwiller でも \(|\det(I-P_\gamma^k)|^{-1/2}\) と phase が残る。
Riemann 側への一致には、この全重み・符号・archimedean terms の独立同定が必要である。

## 3. 三つの growth exponent を混同しない

### 3.1 zero-bearing representation の指数

実在する表現 \(\phi^u\) の domain に eigenvector v があり、
\(\phi^uv=e^{\rho u}v\) が証明されていれば、normalized flow
\(U_u=e^{-u/2}\phi^u\) に対して

\[
 \|U_uv\|=e^{(\Re\rho-1/2)u}\|v\|.
\]

この指定された mode の norm growth は厳密に α=Re ρ−1/2。
正の invariant norm を独立に構成し、v がその完成で非零のまま残るなら α=0。
全零点への適用には、全零点・重複度の回収と domain が必要。
formal Mellin character や resolvent continuation の pole だけでは、この norm 式を
Hilbert eigenvector に適用できない。

### 3.2 geometric transverse Lyapunov 指数

こちらは \(D\varphi^u\) の接束上の伸長率であり、上の表現の指数とは別の定義。
定曲率−1の compact hyperbolic surface の geodesic flow では、横断 Jacobi 方程式

\[
 J''-J=0
\]

から指数±1を持つ。ところが Liouville measure を保存するので、同じ flow の
L² Koopman 表現は unitary である。従って
「positive invariant L² metric ⇒ geometric transverse Lyapunov=0」は偽。
接束の derivative cocycle 自体を等長にする invariant metric なら別の強い条件である。

compact profinite mapping-torus fibre の Haar metric も、接束上の Riemannian metric
ではない。そこに通常の微分 Lyapunov exponent が指定なしに存在するとは言わない。
Frobenius 乗法の Haar unitarity は正しいが、零点指数への比較写像を伴わない。

### 3.3 resonance の実部

異方的空間や解析接続に現れる resonance は、unitary L² flow と共存できる。
その実部は correlation decay などに関係しても、単一の geometric Lyapunov exponent
と一般に等しくない。半平面の向きは generator 規約による。
全算術零点への resonance 対応があっても、unitarity だけでそれらを虚軸へ押せない。

actual modular scattering の例では、\(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) として

\[
 \varphi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},\qquad
 \rho\longmapsto s_\rho=\rho/2.
\]

分子は \(\Lambda(\rho-1)=\Lambda(2-\rho)\ne0\) なので pole order は零点次数と一致。
しかし Laplace parameter の虚部は
\(\Im[s_\rho(1-s_\rho)]=\gamma(1-\beta)/2\ne0\)。
これは RH の場合も L² 固有値にならない。unitary channel Re s=1/2 と
ζ の臨界線に対応する Re s=1/4 を取り違えない。
この既存の内部検算は比較に再利用しただけで、新成果には数えない。

## 4. Li(x) 座標と、本比較の candidate card

\(\theta(x)=2\pi\operatorname{Li}(x)\) は素数密度を描く座標である。
実 counting を使った位相との差を \(2\pi(\pi(x)-\operatorname{Li}(x))\) と置いても、
新しい誤差評価は導かれない。explicit formula へ接続するには、元の零点和・収束・
smoothing の扱いがそのまま必要。図形の rotation／spiral は証明入力にしない。

```text
Continuous flow: existing arithmetic scaling; comparison only
Prime periodic orbit: actual C_p in the scaling site
Orbit length: log p
Prime-power iterates: k log p; exact within Euler convergence region
Frobenius relationship: mapping-torus monodromy; not automatically a tangent return derivative
Normalized flow: exp(-u/2) phi^u on a specified zero-bearing representation
Candidate transverse exponent: representation growth alpha; geometric Lyapunov is a separate object
Relation to Re(rho)-1/2: exact only after the eigenmode/domain identification
Invariant metric: ambient or local Haar metrics exist; complete arithmetic metric not supplied here
Arithmetic source of metric: Haar invariance does not supply global weight-one polarization
Known prior art: the eight rows above; actual mapping torus is an established theorem
New content: no new arithmetic no-growth mechanism from the comparison
RH-equivalent assumption?: no alpha=0 hypothesis adopted
Counterexample status: unitary Koopman coexists with transverse Lyapunov +/-1; no RH counterexample
Decision: stop if the candidate is only Euler-log recoding or existing monodromy plus local unitarity
```

## 5. 一次 locator と読取範囲

- **BK:** Berry–Keating, [The Riemann Zeros and Eigenvalue Asymptotics](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf), SIAM Review 41 (1999), §§2,6。特に (2.9) は asymptotic、(6.1)–(6.5) は xp と未解決 boundary の区別。
- **C99:** Connes, [Trace Formula in Noncommutative Geometry and the Zeros of the Riemann Zeta Function](https://alainconnes.org/wp-content/uploads/selecta.ps-2.pdf), §III Theorem1 と直後、§VIII。全論文再証明ではない。
- **CCM07:** [math/0703392v1](https://arxiv.org/html/math/0703392), Theorem4.16、§6。全零点を数える nuclear topology と正性の区別を既存監査から再照合。
- **SH19:** Connes–Consani, [1910.14368v1](https://arxiv.org/html/1910.14368v1), §2.2、Theorem2.5、Conjecture4.1。
- **CC24/25:** [2401.08401v1 Theorem1.1](https://arxiv.org/html/2401.08401v1)、[2501.06560v1 Theorem3.12](https://arxiv.org/html/2501.06560v1)。orbit lift と有限 abelian cover の monodromy。向きによる Frobenius／inverse の規約は別担当の原文監査を参照し、ここで Poincaré derivative と読み替えない。
- **D10/D24/DS02:** [1001.1621](https://arxiv.org/abs/1001.1621) §2、[1807.06400v4](https://arxiv.org/pdf/1807.06400v4) intro/§10、[math/0204111v1](https://arxiv.org/pdf/math/0204111v1) §4。既存の指定箇所監査を再利用し、119頁全体を再読したとはしない。
- **R76/DZ16:** Ruelle, [1976 original paper scan](https://pdodds.w3.uvm.edu/files/papers/others/1976/ruelle1976c.pdf), introduction/Theorems1–3（scan の文字抽出に難あり）。Dyatlov–Zworski, [Dynamical zeta functions for Anosov flows via microlocal analysis](https://arxiv.org/pdf/1306.4203), opening theorem と generator／flat-trace framework。定義規約の逆数を明記した。
- **S:** Selberg1956の原著 [TIFR収録](https://mathweb.tifr.res.in/Documents/Publications/Studies/Zeta_Functions.pdf) は今回 web の本文展開が失敗。係数は著者講義資料 [Assing, The Selberg Trace Formula](https://www.math.uni-bonn.de/people/assing/lectures/trace_formula.pdf), Lemma5.5／Theorem5.7 pp.44–48 の直接導出で照合した。原著全文を読んだとはしない。
- **G71/G80:** Gutzwiller1971 [DOI](https://doi.org/10.1063/1.1665596) の本文取得は今回失敗。著者の1980 [publisher abstract](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.45.150) と BK (2.9) の係数・asymptotic 指定を使用。Gutzwiller 原論文の全証明確認は主張しない。

新しい算術的 invariant metric、global no-growth lemma、spectral completeness は得ていない。
8プログラムとの比較と、候補を混同しないための限定で停止する。
