**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/fixed-window-reduction.md` · Original SHA-256: `4db59f1de9c281cc6cb432131d08535335522b04fdfabdaca221fb726ccddc6b`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定 support の Weil 形式 — 有限 head から全 mode への十分条件

作成日: 2026-09-29。状態: **解析的な有限還元と明示 tail 定数を独立導出。別工程の有限 head 認証が完了し、§7.2 で接続した。** RH を仮定しない。新規性を主張しない。`a=1/2,T=32,d=64` で、検証すべき有限行列の条件を具体的な数値閾値まで与える。

[Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2) は同型の有限還元を扱う参考資料として確認したが、そこで主張される認証結果、最小固有値、tail bound は本証明の前提にしない。明示公式の規約は [Connes–Consani–Moscovici v1, §3](https://arxiv.org/html/2511.22755v1) と主 repo に合わせる。特殊関数の恒等式は [DLMF §5.7](https://dlmf.nist.gov/5.7)、[DLMF §10.54](https://dlmf.nist.gov/10.54) と照合し、必要な不等式を本文で導く。

## 1. Hilbert 空間、form domain、有限素数項、極の rank

`a>0` を固定し、`H_a=L²([-a,a],dx)` の元を実線上へ零延長する。内積は第一変数に線形とし、

\[
 F_f(t)=\int_{-a}^af(x)e^{itx}dx,\qquad
 \mathcal F_+f(t)=(2\pi)^{-1/2}F_f(t)
\]

とする。`F_+` は零延長と unitary Fourier transform の合成である。`H_a` 上の form domain を

\[
 \mathcal D_a=\left\{f\in H_a:
 \int_{\mathbb R}\log(2+|t|)|\mathcal F_+f(t)|^2dt<\infty\right\}
                                                               \tag{1.1}
\]

とする。これは `C_c^∞(-a,a)` を含み `H_a` に稠密。重み付き Fourier ノルムで完備である。実際、同ノルム Cauchy 列は `L²(R)` でも収束し、その極限の support は閉集合 `[-a,a]` 内に残る。零延長した polynomial は bounded variation なので Fourier transform が `O(1/|t|)`、従って (1.1) に属する。

\[
 h(t)=\Re\psi(1/4+it/2)-\log\pi,
 \quad \mathcal P_a=\{n\ge2:\Lambda(n)>0,\ \log n<2a\},
\]

\[
 A_a=\sum_{n\in\mathcal P_a}\frac{2\Lambda(n)}{\sqrt n},
 \quad
 \Psi_a(t)=h(t)-\sum_{n\in\mathcal P_a}
                   \frac{2\Lambda(n)}{\sqrt n}\cos(t\log n).
                                                               \tag{1.2}
\]

`P_a` は有限集合。境界 `log n=2a` では自己相関が零なので、strict inequality でよい。複素の任意の `f∈D_a` について Weil 形式は

\[
 Q_a(f)=\int_{\mathbb R}\Psi_a(t)|\mathcal F_+f(t)|^2dt
       +2|\langle f,c_a\rangle|^2
       -2|\langle f,s_a\rangle|^2,                     \tag{1.3}
\]

\[
 c_a(x)=\cosh(x/2),\quad s_a(x)=\sinh(x/2),\quad
 \|c_a\|^2=\sinh a+a,\quad\|s_a\|^2=\sinh a-a.        \tag{1.4}
\]

極項の導出は `F_f(i/2)=<f,c_a>-<f,s_a>`、`F_f(-i/2)=<f,c_a>+<f,s_a>` を
`2 Re(F_f(i/2) overline(F_f(-i/2)))` に代入するだけである。したがって極は一般には **rank 2 で不定符号**、even sector で正の rank 1、odd sector で負の rank 1。odd の負項を落としてはいけない。

`tau_b f(x)=f(x+b)` を零延長上で考え、区間へ圧縮するとその作用素ノルムは `≤1`。素数作用素は各 `n` で `Lambda(n)/sqrt(n)` 倍の `tau_log n+tau_-log n` だから、総ノルムは `≤A_a`。同じ評価は (1.2) の cosine multiplier の絶対値からも得られる。

`h` は下に有界で `h(t)=log(|t|/(2pi))+o(1)`。従って十分大きな定数を加えた (1.3) の form norm は (1.1) のノルムと同値で、(1.3) は下に有界な閉形式になる。既知の滑らかな明示公式からこの domain へ拡張された幾何側の形式を扱い、全 `L²` 元に未定義の零点和を置かない。

## 2. 高周波下界を自力で導く

### 2.1 Digamma の下界

`u=t/2>0`、`alpha=1/4` とする。digamma の級数から

\[
 \Re\psi(\alpha+iu)
 =\lim_{m\to\infty}\left(\log m-
 \sum_{k=0}^{m-1}\frac{k+\alpha}{(k+\alpha)^2+u^2}\right).
\]

非負単峰関数 `b_u(x)=(x+alpha)/((x+alpha)²+u²)` は最大値 `≤1/(2u)` を持つ。単峰関数の superlevel 集合は区間であり、区間の整数点数はその長さより高々 `1` 大きい。layer-cake 積分により、有限区間へ切った関数にも

\[
 \sum_{k=0}^{m-1}b_u(k)\le\int_0^m b_u(x)dx+\sup b_u
\]

が成立する。積分を評価して極限を取ると

\[
 \Re\psi(1/4+it/2)
 \ge\log|1/4+it/2|-1/t
 \ge\log(t/2)-1/t.
\]

ゆえに、任意の `t>0` に対して

\[
 \boxed{h(t)\ge\log(t/(2\pi))-1/t.}                  \tag{2.1}
\]

`h` と `Psi_a` は偶。`T>0` を取り

\[
 \beta=\log(T/(2\pi))-1/T-A_a                         \tag{2.2}
\]

と置けば、`log(t/(2pi))-1/t` の単調増加から

\[
 \Psi_a(t)\ge\beta\quad(|t|\ge T).                    \tag{2.3}
\]

`beta>0` が有用な還元の第一条件になる。

### 2.2 低周波 symbol の明示的な大きさ

級数の差を取ると

\[
 h(t)=h(0)+\sum_{k=0}^{\infty}
 \frac{(t/2)^2}{(k+1/4)((k+1/4)^2+(t/2)^2)}.
\]

各項は非負なので `h(t)≥h(0)`。被和関数は `k` に関して減少するため初項＋積分で

\[
 -6<h(0)=-\gamma-\pi/2-3\log2-\log\pi<0,
\]

\[
 h(t)\le4+\tfrac12\log(1+4t^2).                       \tag{2.4}
\]

従って `M_T=sup_{|t|≤T}|Psi_a(t)-beta|` は有限で、例えば

\[
 M_T\le\max\{6,4+\tfrac12\log(1+4T^2)\}+A_a+|\beta|.
                                                               \tag{2.5}
\]

これは精密な interval evaluation に代わる保守的な上界である。有限 head の組立には `Psi_a` の実際の符号を保ち、(2.5) への置換は **tail と coupling の評価だけ**で使う。

## 3. 認証対象の bounded lower operator

band Fourier operator を

\[
 B_T:H_a\to L^2([-T,T]),\quad B_Tf=\mathcal F_+f|_{[-T,T]}
\]

とする。`||B_T||≤1`、`||B_T||HS²=2aT/pi`。`C_T(t)=Psi_a(t)-beta` とおき

\[
 R_T=\beta I+B_T^*M_{C_T}B_T
                 +2|c_a\rangle\langle c_a|
                 -2|s_a\rangle\langle s_a|             \tag{3.1}
\]

と定める。rank-one 記号は `f -> <f,c_a>c_a` の意味である。`C_T` は **signed** symbol であり、正作用素とは仮定しない。`R_T` は `H_a` 全体上の有界自己共役作用素。`beta I` 以外は compact。

(2.3) と Plancherel により、全 `f∈D_a` で

\[
 Q_a(f)-\langle R_Tf,f\rangle
 =\int_{|t|>T}(\Psi_a(t)-\beta)|\mathcal F_+f(t)|^2dt
 \ge0.                                                        \tag{3.2}
\]

これは高周波の prime を `A_a` で抑える一方、低周波の prime・archimedean・正負両 pole をそのまま保持する還元である。別候補の positive-part kernel に置換してはいない。

## 4. Legendre head と band tail の Hilbert–Schmidt 上界

正規直交基底

\[
 \phi_n(x)=\sqrt{\frac{2n+1}{2a}}\,P_n(x/a),\qquad n\ge0
\]

を使う。`Pi_d` は `phi_0,...,phi_{d-1}` への射影、`E_d=I-Pi_d`。以下 `d` は **全 mode 数**であり、各 parity の mode 数ではない。

Rodrigues 公式を `n` 回部分積分すると

\[
 F_{\phi_n}(t)=\sqrt{2a(2n+1)}\,i^n j_n(at),
\]

\[
 j_n(z)=\frac{z^n}{2^{n+1}n!}
                \int_{-1}^{1}e^{izu}(1-u^2)^n du.
\]

Beta 積分を評価すれば、全 **実数** `z` で

\[
 |j_n(z)|\le\frac{|z|^n}{(2n+1)!!}.                    \tag{4.1}
\]

これは `n=0` を含む。従って `X=aT` とおくと

\[
 \begin{aligned}
 \kappa_d&:=\|B_TE_d\|_{\rm HS}^2
 =\sum_{n\ge d}\frac{a(2n+1)}\pi
                        \int_{-T}^{T}|j_n(at)|^2dt\\
 &\le\frac{2X}\pi\sum_{n\ge d}
                        \frac{X^{2n}}{((2n+1)!!)^2}.
 \end{aligned}                                                \tag{4.2}
\]

積分を正確に行うと `2n+1` が相殺する点が重要である。`b_n=X^(2n)/((2n+1)!!)²` の比は `b_{n+1}/b_n=X²/(2n+3)²`。したがって `X<2d+3` のとき

\[
 \boxed{\kappa_d\le K_d:=\frac{2X}\pi
     \frac{X^{2d}}{((2d+1)!!)^2}
     \frac1{1-X^2/(2d+3)^2}.}                          \tag{4.3}
\]

even/odd tail を別々に扱う場合は、和を対応する `n` のみに制限できる。例えば最初の tail mode が `m` の parity では、(4.3) の geometric ratio を
`X^4/((2m+3)²(2m+5)²)` として `m,m+2,...` を評価できる。以下の全 tail 上界は両 parity に共通して安全に使える。

### 4.1 位相規約

低周波行列の `(j,k)` 成分は

\[
 \frac{a\sqrt{(2j+1)(2k+1)}}\pi\,i^{k-j}
       \int_{-T}^{T}C_T(t)j_j(at)j_k(at)dt.             \tag{4.4}
\]

異なる parity 間は零。同 parity では `i^(k-j)=(-1)^((k-j)/2)` が実符号として残る。この符号を基底変換に吸収する場合、pole vector 側も同じ変換を施す必要がある。Fourier 側だけの符号変更は別の行列になる。

## 5. Pole の Legendre tail を別に抑える

`b=a/2` とする。(4.1) の積分表示を虚引数で使うと

\[
 |j_n(ib)|\le e^b\frac{b^n}{(2n+1)!!}.
\]

`d_n=<exp(x/2),phi_n>` は `sqrt(2a(2n+1))` 倍の modified spherical Bessel 値。even `n` では `d_n=<c_a,phi_n>`、odd `n` では `d_n=<s_a,phi_n>` になる。よって

\[
 \eta_d^2:=\|E_dc_a\|^2+\|E_ds_a\|^2
 \le2ae^{2b}\sum_{n\ge d}(2n+1)
                   \frac{b^{2n}}{((2n+1)!!)^2}.
\]

隣接項の比は `b²/((2n+1)(2n+3))`。`b²<(2d+1)(2d+3)` なら

\[
 \boxed{\eta_d^2\le J_d:=2ae^a(2d+1)
  \frac{(a/2)^{2d}}{((2d+1)!!)^2}
  \frac1{1-(a/2)^2/((2d+1)(2d+3))}.}                 \tag{5.1}
\]

極項は band Fourier tail と同じものではないため、この追加評価が必要である。odd の負 pole tail の作用素ノルムは `≤2J_d`。positive even pole tail は下界を悪くしない。

## 6. 有限 head と無限 tail の厳密な結合条件

`H_d=Pi_d R_T Pi_d` の `d×d` 行列を interval quadrature 等で認証し

\[
 H_d\succeq\mu I_d                                      \tag{6.1}
\]

が得られたとする。ここで `mu` は **すべての entry error と eigenvalue / LDL 認証誤差を含む**下界である。非認証の浮動小数点最小固有値ではない。

`||B_T||≤1` と (4.3) より signed band perturbation の各 block は

\[
 \|E_dB_T^*M_{C_T}B_TE_d\|\le M_TK_d,
 \quad
 \|\Pi_dB_T^*M_{C_T}B_TE_d\|\le M_T\sqrt{K_d}.           \tag{6.2}
\]

前者は `||B_TE_d||²≤||B_TE_d||HS²`、後者は積の作用素ノルムから従う。`Pi_d` は parity を保存するので、正負 pole の head vectors と tail vectors も各側で直交する。従って

\[
 E_dR_TE_d\succeq\delta E_d,\qquad
 \delta:=\beta-M_TK_d-2J_d,
\]

\[
 \|\Pi_dR_TE_d\|\le\Gamma,
 \qquad \Gamma:=M_T\sqrt{K_d}
                       +2\sqrt{\sinh a+a}\sqrt{J_d}.  \tag{6.3}
\]

parity ごとのより鋭い pole 項では、even coupling は `2||Pi c_a|| ||E c_a||`、odd coupling は `2||Pi s_a|| ||E s_a||`。上の共通上界はその両方を含む。

`f=x+y`、`x=Pi_df`、`y=E_df` と分けると

\[
 \langle R_Tf,f\rangle
 \ge\mu\|x\|^2-2\Gamma\|x\|\|y\|+\delta\|y\|^2.
                                                               \tag{6.4}
\]

従って検証可能な十分条件は

\[
 \boxed{\quad\mu>0,\qquad\delta>0,\qquad
                    \mu\delta>\Gamma^2.\quad}          \tag{6.5}
\]

これは `2×2` Schur complement である。成立すれば全 `f∈D_a` に対して

\[
 Q_a(f)\ge\lambda\|f\|^2,\quad
 \lambda=\frac{\mu+\delta-
        \sqrt{(\mu-\delta)^2+4\Gamma^2}}2>0.            \tag{6.6}
\]

数値的な cancellation を避けるには
`lambda≥(mu delta-Gamma²)/(mu+delta)` を使える。各 parity の head を別に認証し、(6.5) を両方に適用してもよい。片方だけの認証で任意の複素 test function の結論には進まない。

この還元は元の非有界 form の cross term を暗黙に operator norm で評価していない。最初に (3.2) で **有界な lower operator** に移り、その operator の block を評価しているため domain の問題が閉じている。

## 7. 具体例 `a=1/2,T=32,d=64`

`[-1/2,1/2]` では素数項は `n=2` のみで

\[
 A_a=\sqrt2\log2<1,
 \qquad \beta=\log(16/\pi)-1/32-\sqrt2\log2>15/32.
                                                               \tag{7.1}
\]

後者は `pi<16/5`、`log5>3/2` から得る保守的下界。さらに `beta<2`、(2.4) から `sup_{|t|≤32}|h(t)|<9`、従って **`M_T<12`**。

`X=16`、`d=64`、`D=129!!` とすると、`pi>3` と `e^(1/2)<2` だけで (4.3), (5.1) を有理数に上から抑えられる。

\[
 K_{64}<\frac{32}{3}\frac{16^{128}}{D^2}
                   \frac1{1-256/131^2}
       <3.215\times10^{-64},                           \tag{7.2}
\]

\[
 J_{64}<2\cdot129\frac{(1/4)^{128}}{D^2}
                \frac1{1-1/(16\cdot129\cdot131)}
       <4.934\times10^{-294}.                          \tag{7.3}
\]

小数上界はこれらの有理数との整数比較で確認できる。近似値を証明へ代入する必要はない。さらに `sqrt(sinh(1/2)+1/2)<1.1` なので

\[
 \delta>0.46,\qquad
 \Gamma<2.153\times10^{-31},\qquad
 \Gamma^2<4.64\times10^{-62}.                          \tag{7.4}
\]

従って次は **64 mode の有限認証だけで閉じる、具体的な十分条件**である。

> `H_64=Pi_64 R_32 Pi_64` の両 parity を含む行列について、
> `H_64 >= 2×10^-61 I` を丸め・積分・行列誤差込みで認証できれば、
> 全 `f∈D_(1/2)` に対し `Q_(1/2)(f) >= 9×10^-62 ||f||²` が成立する。

実際、(6.4) で下界を `mu_0=2e-61, delta_0=.46, Gamma²<4.64e-62` に弱めると、対応する `2×2` 行列の determinant は `>4.56e-62`、trace は `<.47`。最小固有値は determinant/trace 以上だから `>9e-62`。

ここまでは head に対する**条件付き**の解析定理であり、head 条件の検証は別の計算を要する。その後に得た認証結果は §7.2 に記録する。一般には有限 head に負方向が出ればこの選択の lower operator を棄却または改善する。`R_T` が負であっても `Q_a` が負とは限らない。

### 7.1 cutoff / mode 数を変える場合

同じ有理上界の計算で次を得る。`d` は full Legendre mode 数、偶数 `d` のとき各 parity が `d/2` modes。

| `a` | `T` | `d` | `X=aT` | `K_d` の上界 | `J_d` の上界 |
|---:|---:|---:|---:|---:|---:|
| `1/2` | `32` | `64` | `16` | `3.215e-64` | `4.934e-294` |
| `1/2` | `64` | `96` | `32` | `2.810e-70` | `1.289e-473` |
| `1/2` | `64` | `128` | `32` | `1.598e-124` | `1.359e-662` |

`T=64` では粗い定数として `beta>63/64`、`M_T<14` が使える。前者は `log(32/pi)>log10>2`、後者は (2.4), `A_a<1`, `beta<3` による。正確な `beta` と signed symbol を head 組立から置き換えず、tail/coupling の上界だけに利用する。

有理数上界の再計算には `d=64,96,128` について `D=∏_{k=0}^d(2k+1)`、
`Kupper=(2X/3) X^(2d)/D² /(1-X²/(2d+3)²)`、
`Jupper=2(2d+1) 4^(-2d)/D² /(1-1/(16(2d+1)(2d+3)))`
を exact rational arithmetic で評価すれば足りる。Python `fractions.Fraction` で独立確認した。

### 7.2 実行済み head 認証との接続

[小窓の計算証明](window-half-certificate.md) とその [Arb 証明書](../../../../artifacts/experiments/results/window-half-T32-cut64.json) は、上と同じ `R_32` の even/odd 各 32 次 head について、求積誤差を含めて

\[
 H_{64}\succeq10^{-7}I                              \tag{7.5}
\]

を認証した。両 parity の各行列から厳密な `10^-7 I` を引き、その interval LDL の全 32 pivot が正であることによる。最小固有値の浮動小数点近似を (7.5) の代わりに使用していない。[独立監査](window-half-independent.md) は別精度での再実行と保存された head に対する別実装の interval Cholesky を記録する。

(7.5) を本ノートの独立な tail/coupling 評価 (7.4) と組み合わせても、全複素 `f∈D_(1/2)` に対して

\[
 \boxed{Q_{1/2}(f)\ge9\cdot10^{-8}\|f\|_2^2.}       \tag{7.6}
\]

が従う。実際 `ell=9e-8` とし、(6.4) から `ell(||x||²+||y||²)` を引く。残る `2×2` 行列の対角下界は `1e-8` と `.46-9e-8>.45`、その determinant は `>4.5e-9-4.64e-62>0`。従って非負である。この議論は、計算側が別の保守的 coupling bound `3.785e-29` から導いた同じ結論を、別の解析的 tail 評価で照合している。

証明書の数値検証は別工程の成果である。本ノートの担当は実装の読み取り監査、証明書の結果・hash と現在のソースの一致、解析的還元との規約の一致を確認した。検証済み head から一つの固定窓の結論へ進んだもので、全窓の正値性や RH への拡張ではない。

## 8. 監査上の境界

有限 head の positivity だけでは無限 mode へ進まない。必要な追加情報は、高周波下界 `(2.3)`、明示 band tail `(4.3)`、負 pole tail `(5.1)`、head–tail coupling `(6.3)` と Schur 条件 `(6.5)` である。本ノートはその全てを fixed support で定義した。

これは一つの固定窓に対する十分条件であり、全 `a>0` での成功や RH を結論しない。cutoff や mode 数を変えた場合は、対応する head 行列と tail constants を一組として再認証する。Zhu の数値証明書、原資料の物理モデル、非認証の固有値を数学的前提として採用していない。他のファイル、主証明 graph、既存 theorem の状態は変更していない。

## 9. 認証実装の読み取り監査

対象は [window_half_certificate.py](../../../../artifacts/experiments/scripts/window_half_certificate.py) と interval LDL helper [groskin_independent_certificate.py](../../../../artifacts/experiments/scripts/groskin_independent_certificate.py)。本文 §7.2 の JSON が保存する SHA-256 は、それぞれ `d4b176096168c13f53459f27e1ae9a9db9e045a4b774c097f49a9939d5c408d0` と `a8d277e17898f39a86d4729a9c47534a6db0d087f4a1ccbaca58d891f7e239e8` であり、監査時の実ファイルと一致した。

以下を読み取りと独立計算で確認した。

- `a=1/2` の Fourier 振幅、`(-1)^floor(n/2)` の parity 位相、正の pole 係数、pole の符号と係数 `±2` は (1.3), (4.1) と整合する。正周波数だけの求積の係数は `1/pi` であり、panel の変数変換後の `weight*step/(2pi)` は正しい。
- 幅 `1/4` の panel、Bernstein ellipse `rho=6` では `|Im t|≤35/96<.4`。digamma の解析的半和の引数の実部は `.05` より大きく、pole を避ける。級数からの symbol 上界と Legendre 積分からの Fourier 振幅上界は、コードの全成分共通上界を与える。
- Gauss の誤差 `4*T*M*rho^(1-2*q)/(rho-1)` は、次数 `2q-1` の Chebyshev 切断誤差と正の Gauss weights から独立に再導出できる。各成分 ball への誤差半径追加が保持される。
- 代替の全次数 tail 和では `b_(n+1)/b_n=X/sqrt((2n+1)(2n+3))≤X/(2d+1)` を使っており、保守的な幾何級数上界である。evaluation vector の Parseval と pole ノルムを使った cross bound は、`T/pi` を含め正しい。
- interval LDL は正と証明できる pivot のみを採用する。0 を跨ぐ ball の平方に `x*x` を使う修正後の実装を対象とした。全 pivot の正値性と head の固有値下界を混同していない。

JSON に保存された両 parity 各 32 個の正 pivot、head shift `1e-7`、全窓下界 `>9.9e-8` を確認した。別の adaptive 積分と JSON 再読込の結果は [crosscheck 記録](../../../../artifacts/experiments/results/window-half-crosscheck.json) にある。この読み取り監査自体は Arb/FLINT の実装や全解析を Lean で形式検証したという意味ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/window-half-T32-cut64.json`](../../../../artifacts/experiments/results/window-half-T32-cut64.json)
- [`experiments/results/window-half-crosscheck.json`](../../../../artifacts/experiments/results/window-half-crosscheck.json)
- [`experiments/scripts/groskin_independent_certificate.py`](../../../../artifacts/experiments/scripts/groskin_independent_certificate.py)
- [`experiments/scripts/window_half_certificate.py`](../../../../artifacts/experiments/scripts/window_half_certificate.py)
- [`proofs/audits/window-half-certificate.md`](window-half-certificate.md)
- [`proofs/audits/window-half-independent.md`](window-half-independent.md)
