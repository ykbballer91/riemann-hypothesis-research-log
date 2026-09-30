**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/imbalance-reduction.md` · Original SHA-256: `d26fc754d8543c2515926554f023032f5c91dd62d407659d3cec0ea784a91920`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定積の imbalance energy — 収束域、作用素表示、停止判定

2026-09-29。担当: BUILDER。**この証明ルートは停止する。** 以下の非負性・差分公式は正しいが、零点で energy が消えるという追加命題は RH そのものであり、導出していない。構造だけから零点消滅を推論する一般論には厳密な反例がある。RH の証明・反証、新規性の主張はない。

既知入力は [DLMF 27.4.3 の Euler 積](https://dlmf.nist.gov/27.4.E3)、[27.4.12 の対数微分級数](https://dlmf.nist.gov/27.4.E12)、[25.2 の解析接続と極](https://dlmf.nist.gov/25.2) に照合した。以下の式はそれらから直接導く。

## I1. 一項の恒等式と正確な消滅条件

`n≥2`、実数 `sigma=1/2+delta` に対し、ユーザーの量を

\[
 E_n(\sigma)=(n^{-\sigma}-n^{-(1-\sigma)})^2,
 \qquad e_n(\delta):=E_n(1/2+\delta)
\]

と区別する。固定積 `n^(-sigma)n^(-(1−sigma))=1/n` より

\[
 e_n(\delta)=\frac4n\sinh^2(\delta\log n)
 =\frac2n\{\cosh(2\delta\log n)-1\}\ge0.            \tag{I1.1}
\]

`n≥2` なので、`e_n(delta)=0 iff delta=0`。これは実数指数の代数恒等式であり、`zeta(s)=0` を仮定した帰結ではない。

## I2. Regulator を入れた素数冪総和

\[
 w_0(n)=\frac{\Lambda(n)}{\log n},\qquad
 w_1(n)=\Lambda(n),\qquad n\ge2.
\]

`n=p^k` では `w_0=1/k`、`w_1=log p`、それ以外では 0。`s_0=1+u` とし、実数 `u>2|delta|` に対して

\[
 \mathcal E_j(u,\delta)=\sum_{n\ge2}w_j(n)n^{-u}e_n(\delta)
 \qquad(j=0,1)
\]

を定める。両者は絶対収束し、

\[
 \boxed{\mathcal E_0(u,\delta)
 =\log\zeta(s_0+2\delta)+\log\zeta(s_0-2\delta)
                       -2\log\zeta(s_0),}          \tag{I2.1}
\]
\[
 \boxed{\mathcal E_1(u,\delta)
 =F(s_0+2\delta)+F(s_0-2\delta)-2F(s_0),
 \qquad F(s)=-\zeta'(s)/\zeta(s).}                  \tag{I2.2}
\]

この範囲では三つの実数引数がすべて 1 より大きく、`log zeta` は正の実数 `zeta(s)` の実対数である。枝の選択や極を横切る操作はない。

**証明。** Euler 積の絶対収束から `log zeta(s)=Σ_pΣ_(k≥1)p^(-ks)/k=Σ_n w_0(n)n^(-s)`。対数微分は `F(s)=Σ_n w_1(n)n^(-s)`。一方

\[
 n^{-u}e_n(\delta)
 =n^{-(s_0+2\delta)}+n^{-(s_0-2\delta)}-2n^{-s_0}.
\]

三つの絶対収束級数を合成すれば結論が従う。∎

`delta≠0` では、実数 `u` に関する収束条件は **必要十分に `u>2|delta|`** である。`d=|delta|>0` とすると

\[
 n^{-u}e_n(\delta)
 =n^{-(1+u-2d)}(1-n^{-2d})^2.                        \tag{I2.3}
\]

`u>2d` なら `w_0≤1`、`w_1≤log n` と比較して収束する。`u≤2d` なら十分大きい素数に限った項が定数倍の `1/p` 以上となり、`Σ_p1/p=∞` から両方とも `+∞` へ発散する。最後の既知事実は Euler 積と調和級数の発散からも従う。`delta=0` だけは各項が厳密に 0 で、任意の `u` で零級数になる。ただしそれによって `log zeta(1)` や `F(1)` の差を定義したことにはならない。

特に regulator を `u↓0` と外すとき、固定された `delta≠0` では先に `u=2|delta|` の発散境界に達する。`v=u−2d↓0` では

\[
 \mathcal E_0=-\log v+O_d(1),\qquad
 \mathcal E_1=v^{-1}+O_d(1).                         \tag{I2.4}
\]

これは `zeta(1+v)=v^(-1)+O(1)` と (I2.1)–(I2.2) による。`delta` も同時に 0 にすれば自動的に消えるわけでもない。例えば `delta=c u`、`0<c<1/2` なら

\[
 \mathcal E_0(u,cu)\longrightarrow-\log(1-4c^2)>0,
 \qquad
 \mathcal E_1(u,cu)\sim\frac{8c^2}{(1-4c^2)u}.
                                                        \tag{I2.5}
\]

## I3. Hessian と正作用素としての正しい意味

`G_0(s)=log zeta(s)`、`G_1(s)=F(s)` とする。収束域の compact subsets で対数冪を掛けた級数も一様収束するため、項別微分できる。

\[
 G_j''(s)=\sum_{n\ge2}w_j(n)(\log n)^2n^{-s}>0
 \qquad(s>1).
\]

`r=2|delta|` とすれば中心二階差分は正しい Hessian 積分

\[
 \mathcal E_j(u,\delta)
 =\int_{-r}^{r}(r-|v|)G_j''(s_0+v)\,dv             \tag{I3.1}
\]

になる。また

\[
 \partial_\delta^2\mathcal E_j(u,\delta)
 =8\sum_{n\ge2}w_j(n)n^{-s_0}(\log n)^2
                                  \cosh(2\delta\log n)>0.
                                                        \tag{I3.2}
\]

これは実変数 `delta` の厳密凸性を表すだけで、zeta の複素零点の Hessian や、零点を消す恒等式ではない。

作用素としては、素数冪を添字とする `ell²` 上で

\[
 (Av)_n=(\log n)v_n,\qquad
 D(A)=\{v:\sum_n(\log n)^2|v_n|^2<\infty\}
\]

と置けば、`A` は正の自己共役作用素である。ベクトル

\[
 v_{j,u}(n)=\sqrt{w_j(n)}\,n^{-(1+u)/2}
\]

について、`u>2|delta|` なら

\[
 \mathcal E_j(u,\delta)
  =\|(e^{\delta A}-e^{-\delta A})v_{j,u}\|^2
  =2\int\{\cosh(2\delta\lambda)-1\}\,d\mu_{v_{j,u}}(\lambda).
                                                        \tag{I3.3}
\]

指数作用素の共通定義域条件はここで必要であり、(I2.3) と整合する。右の表示は spectral integral による**形式**の値である。形式 domain の元を無条件に `cosh(2delta A)` の operator domain に属すると扱わない。

通常の dilation についても同じ spectral calculus が使える。`L²(R_+,dx/x)` の `U_t f(x)=f(e^t x)` を `r=log x` へ移すと、`U_t=e^(itD)` の生成子は `D=−i∂_r`、domain は `H¹(R)`、スペクトルは `R` である。**この生成子自体は正ではない。** 正なのは `2(cosh(2delta D)−I)` が与える閉二次形式で、`delta≠0` の形式 domain は `D(e^(|delta||D|))`。上の離散的 `A` は別の明示的モデルであり、通常の dilation 生成子や zeta 零点の作用素と同一視できない。

## I4. Weil 形式へ移す際の符号と cross term

Fourier 規約は `F_g(z)=∫g(x)e^(izx)dx`、`z_rho=(rho−1/2)/i=gamma−i delta`。`g∈C_c∞(R)`、`tau_b g(x)=g(x−b)`、`f=tau_b g−g` とすると

\[
 F_f(z)=(e^{ibz}-1)F_g(z),
\]
\[
 F_f(z)\overline{F_f(\bar z)}
   =2(1-\cos(bz))F_g(z)\overline{F_g(\bar z)}.        \tag{I4.1}
\]

従って autocorrelation の差分が与える spectral multiplier は `2(1−cos(bz))` である。実軸 `z=t` では `4sin²(bt/2)≥0` だが、軸外では

\[
 2(1-\cos(b(\gamma-i\delta)))
 =2(1-\cos(b\gamma)\cosh(b\delta))
                   -2i\sin(b\gamma)\sinh(b\delta).  \tag{I4.2}
\]

実部も符号不定である。例として `b=2log n`、`gamma=0` という複素引数では、この因子は

\[
 2(1-\cosh(2\delta\log n))=-n e_n(\delta).          \tag{I4.3}
\]

これは zeta の零点を挙げた例ではなく、hyperbolic imbalance と Weil 差分の符号を比較する正確な式である。`F_g(z)overline(F_g(bar z))` も軸外では一般に絶対値平方ではない。共役零点を組にした後にも cross term の実部が残るため、(I4.1) を `e_n(delta)` の正の和へ読み替えられない。

## I5. 消滅推論の破綻と厳密な停止条件

第一に、実数値関数 `e_n(Re z)` は holomorphic でない。その holomorphic な候補 `4n^(-1)sinh²(z log n)` と同じものではない。例えば

\[
 z=\frac{i\pi}{2\log2}:
 \qquad e_2(\Re z)=0,\qquad 2\sinh^2(z\log2)=-2.
                                                        \tag{I5.1}
\]

第二に、解析接続は正係数級数の非負性を保存しない。(I2.2) の meromorphic な右辺を `u=1/10,delta=1/5` に評価すると、Arb/Acb により

\[
 F(3/2)+F(7/10)-2F(11/10)
       =-21.3487410999574\ldots<0                  \tag{I5.2}
\]

が認証される。この場所は `u>2|delta|` の外であり、元の非負級数は `+∞` に発散する。解析接続値がその級数の energy であるという主張は偽である。

第三に、正測度・反転対称性・実係数だけでは零点で imbalance は消えない。

\[
 L(z)=\cosh(1/4)+\cosh z
\]

は正の偶測度 `cosh(1/4) delta_0+(delta_1+delta_(-1))/2` の両側 Laplace 変換で、

\[
 L(1/4+i\pi)=0,\qquad
 e_2(1/4)=\frac{3\sqrt2}{4}-1>0.                    \tag{I5.3}
\]

これは `cosh(a+iπ)=−cosh a` による厳密な反例であり、数値的な零包含を等号の証明として使用していない。zeta/RH への反例ではなく、構造だけによる一般推論への反例である。

最後に、次の命題は既存の非自明零点の帯 `0<Re rho<1` の下で**それぞれ RH と同値**である。

\[
 \forall\rho\ (\zeta(\rho)=0\text{ nontrivial}
          \Longrightarrow e_2(\Re\rho-1/2)=0),      \tag{I5.4: RH-equivalent}
\]
\[
 \forall\rho\ (\zeta(\rho)=0\text{ nontrivial}
   \Longrightarrow\mathcal E_0(3,\Re\rho-1/2)=0).   \tag{I5.5: RH-equivalent}
\]

(I5.4) は (I1.1) から直ちに同値。(I5.5) は `u=3>2|Re rho−1/2|` なので収束し、`n=2` の正係数項だけでも、総和が 0 なら `Re rho=1/2` と分かる。RH からの逆向きは各項が 0。従って「零点では energy が消える」を新しい補助補題として仮定することを**この時点で停止する**。Euler 積、凸性、自己共役性、対称性のいずれからもその消滅式は導いていない。

## I6. 数値スクリプトの読み取り監査

[imbalance_checks.py](../../../../artifacts/experiments/scripts/imbalance_checks.py) と [保存結果](../../../../artifacts/experiments/results/imbalance-checks.json) を確認した。SHA-256 `9f7d952a6d460cafe12eb25157fda00ced57b6cf3fb73659c96ad7378112f17f` がソースと JSON で一致する。**読み取り監査 PASS。** この担当によるスクリプト編集・再実行は行っていない。

`u=3`、`delta=1/10,1/4,2/5`、`N=1000` の各チェックで、整数 prime-power 列挙と係数 `1/k` は (I2.1) に一致する。`v=u−2|delta|>0` について、コードの保守的評価

\[
 0\le\sum_{n>N}w_0(n)n^{-u}e_n(\delta)
 \le2\sum_{n>N}n^{-1-v}\le\frac{2N^{-v}}v           \tag{I6.1}
\]

は正しい。実際には (I2.3) から係数 2 を 1 に改善できるが、現実装の上界は有効である。保存された remainder の全てが正で、この上界より小さいことを 224 bit の Arb ball が認証している。

`acb_series([x,1],prec=2).zeta()` の一次係数は `zeta'(x)` なので、`−z[1]/z[0]` の符号・正規化は正しい。実数引数での実性は zeta の既知の共役対称性によるもので、虚部 ball の零包含だけに依存していない。対象の `x=3/2,7/10,11/10` は極でも零点でもない。holomorphic example の厳密値 −2 と toy transform の厳密零点は (I5.1), (I5.3) の代数恒等式が根拠であり、数値の包含は補助確認である。

信頼基盤は既知の解析恒等式と python-flint 0.9.0 / Arb/Acb の包含演算であり、Lean の形式検証ではない。採用する成果は (I1)–(I4) の限定された恒等式と収束条件、棄却する推論は「構造的正性から全 zeta 零点での energy 消滅が従う」という部分である。この路線を RH 証明へ延長しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/imbalance-checks.json`](../../../../artifacts/experiments/results/imbalance-checks.json)
- [`experiments/scripts/imbalance_checks.py`](../../../../artifacts/experiments/scripts/imbalance_checks.py)
