**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/window-four-fifths-reduction.md` · Original SHA-256: `32553a9bec5878b382e35ebc3f315f843738ed73612a34fa7984f47ab6c8007f`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定窓 a=4/5 — Gauss 誤差と無限 Legendre tail の独立評価

2026-09-29。担当: BUILDER。**ユーザーの方針変更により窓拡大を中断。有限 head の正値性は仮定・認証していない。** このノートは `a=4/5,T=111,beta=1/5` に対する解析的な定数を提供する。RH は OPEN、新規性を主張しない。停止済み imbalance route とは独立の作業である。

tail floor は [joint symbol 認証と独立監査](joint-symbol-reduction.md#j7-joint-symbol-scanner-の独立監査) により `Psi_a(t)>1/5` for `|t|≥111`。全 mode 還元・定義域は [fixed-window-reduction.md](fixed-window-reduction.md)、球 Bessel 積分は [DLMF §10.54](https://dlmf.nist.gov/10.54) の規約に合わせる。head の組立・求積・丸め認証は別工程である。root の実行は 444 panels 中 160 panels の時点で中断され、head / 全窓の証明書は得られていない。このノートの解析的な部分結果だけを保存し、拡大計算を続行しない。

## W1. 基底、Fourier、pole の正規化

`H=L²([-a,a];C)` を零延長し、`F_f(t)=∫f(x)e^(itx)dx`、`U f=F_f/sqrt(2pi)`。形式 domain は

\[
 \mathcal D=\{f\in H:\int_{\mathbb R}\log(2+|t|)|Uf(t)|^2dt<\infty\}.
\]

素数冪は `n=2,3,4` のみで、

\[
 P_a(t)=\sqrt2\log2\cos(t\log2)
       +\frac{2\log3}{\sqrt3}\cos(t\log3)
       +\log2\cos(t\log4),
\]
\[
 A_a=\sqrt2\log2+\frac{2\log3}{\sqrt3}+\log2<3.
                                                        \tag{W1.1}
\]

`n=4` の係数は `log2` であり `log4` ではない。`h(t)=Re psi(1/4+it/2)−log pi`、`Psi=h−P_a`、`C(t)=Psi(t)−1/5` と置く。`B_T=1_[−T,T] U` を用いて

\[
 R=\tfrac15 I+B_T^*M_C B_T
       +2|c\rangle\langle c|-2|s\rangle\langle s|,
 \quad c(x)=\cosh(x/2),\ s(x)=\sinh(x/2).
                                                        \tag{W1.2}
\]

tail floor と Plancherel から `Q_a(f)≥<Rf,f>` for `f∈D`。

正規直交 Legendre 基底とその変換は

\[
 \phi_n(x)=\sqrt{\frac{2n+1}{2a}}P_n(x/a),
 \qquad F_{\phi_n}(t)=\sqrt{2a(2n+1)}\,i^n j_n(at).
                                                        \tag{W1.3}
\]

同 parity の行列に使う実振幅は

\[
 V_n(t)=(-1)^{\lfloor n/2\rfloor}
              \sqrt{\tfrac85(2n+1)}\,j_n(4t/5).
                                                        \tag{W1.4}
\]

even では `F=V`、odd では `F=iV`。両 parity の混合項は 0。従って低周波行列は

\[
 C_{jk}=\frac1\pi\int_0^{111}C(t)V_j(t)V_k(t)dt
 \quad(j\equiv k\pmod2).                            \tag{W1.5}
\]

半幅 `a=1/2` で使った `sqrt(2n+1)` だけでは不足し、ここでは Fourier と pole の**双方に** `sqrt(8/5)` が必要である。

`b=a/2=2/5`、`D_n=(2n+1)!!` とすると pole 係数は

\[
 p_n=\sqrt{\tfrac85(2n+1)}\,
       \frac{(2/5)^n}{D_n}
       {}_0F_1\left(n+\tfrac32;\tfrac1{25}\right)>0.
                                                        \tag{W1.6}
\]

even `n` では `<c,phi_n>`、odd `n` では `<s,phi_n>` に等しい。head の pole 行列は even `+2p_jp_k`、odd `−2p_jp_k`。Fourier の位相 `(-1)^floor(n/2)` をこの pole vector に移さない。同じ基底に対する二つの別の変換の係数だからである。

## W2. 複素 ellipse 上の厳密な integrand bound

`[0,111]` を幅 `h=1/4` の **444 panels** に分け、各 panel で 32 点 Gauss–Legendre を使う。正規化された `[-1,1]` の Bernstein ellipse parameter を `rho=6` とする。

複素 `t=center+(h/2)z` は

\[
 |\Im t|\le\frac{h}{4}(\rho-\rho^{-1})
       =\frac{35}{96}<\frac25,
 \qquad -\frac{25}{96}\le\Re t\le111+\frac{25}{96}.
                                                        \tag{W2.1}
\]

`h(t)` の解析的延長は

\[
 \widetilde h(t)=\frac12\{
      \psi(1/4+it/2)+\psi(1/4-it/2)\}-\log\pi.
\]

ellipse 上では両 digamma 引数 `z` に対し `Re z>1/20`、`|z|<111/2+3/5`。級数

\[
 \psi(z)=-\gamma-\frac1z+
        \sum_{k\ge1}\frac{z}{k(k+z)}
\]

と `|k+z|≥k`、`gamma<1`、`Σk^(-2)<2` より

\[
 |\psi(z)|\le1+20+2|z|<111+22.2.
\]

さらに `log pi<2`、`log4<7/5`、`|cos(t log n)|≤exp(|Im t|log n)<exp(14/25)<2`。従って ellipse 上の全 symbol に

\[
 |\widetilde\Psi(t)-1/5|
 <111+25+2A_a+1/5<\boxed{143}=:S.                  \tag{W2.2}
\]

**次数に依存しない Fourier 上界。** `||phi_n||₂=1` と Cauchy–Schwarz から、全複素 `t` に対して

\[
 |F_{\phi_n}(t)|
 \le\left(\int_{-a}^ae^{-2(\Im t)x}dx\right)^{1/2}
 \le\sqrt{2a}\,e^{a|\Im t|}.                       \tag{W2.3}
\]

この式には `2n+1` の因子がない。`V_n` は `F_phi_n` の定数位相倍なので同じ上界が使える。したがって (W1.5) の `1/pi` 込みの被積分関数は、**head の全次数に共通して**

\[
 \left|\frac{\widetilde C(t)V_j(t)V_k(t)}\pi\right|
 <\frac{143(8/5)e^{16/25}}\pi
 <\boxed{\frac{2288}{15}}=:M_Q.                     \tag{W2.4}
\]

最後は `exp(16/25)<2`、`pi>3` による保守的な有理上界。これは指数 `2a|Im t|<16/25` を含み、半幅変更の因子を取り落としていない。一般の head vector に正規化されていない基底を使う場合には (W2.3) をそのまま流用できない。

## W3. Gauss 誤差と行列への移し方

ellipse 上の解析関数の絶対値が `M_Q` 以下なら、Chebyshev 係数は `2M_Q rho^(-k)` 以下。次数 `2q−1` までの切断誤差は

\[
 \varepsilon_{\rm poly}\le
      \frac{2M_Q\rho^{1-2q}}{\rho-1}.
\]

`q` 点 Gauss はこの多項式に exact。`[-1,1]` の積分と正の Gauss weights の和は各 2 なので、差の作用素ノルムは高々 4。panel の Jacobian `h/2` と全幅 `T=111` を戻せば、各行列成分の絶対誤差は

\[
 \boxed{\varepsilon_{\rm entry}
   \le\frac{4TM_Q\rho^{1-2q}}{\rho-1}
   =\frac{4\cdot111\cdot(2288/15)}5\,6^{-63}
   <1.284\cdot10^{-45}.}                            \tag{W3.1}
\]

ここで `q=32,rho=6`。式右辺は完全な有理数なので、最後の小数との大小を整数比較できる。

実装で Gauss node/weight `x,w` を使う場合、`t=center+h*x/2`、実振幅積に掛ける係数は `w*h/(2pi)*C(t)`。これに全 panel を足し、`beta I` と pole を加える。特殊関数・nodes・weights・演算の丸めも enclosure とし、(W3.1) の半径を各成分に追加する必要がある。

`d` は **full modes n=0,…,d−1 の数** とし、偶数 `d` の各 parity は `m=d/2` 次元。各 entry の誤差が `epsilon_entry` なら、その誤差行列の作用素ノルムは `≤m epsilon_entry`。従って `d=192` で `<1.233e-43`、`d=256` で `<1.644e-43`。entry ball を既に含めた interval LDL 等で認証するなら、この行列ノルム誤差を二重に引く必要はない。

これは解析的な求積誤差であって、全ての数値丸め誤差をこの値だけで覆ったと主張してはいない。

## W4. 実 band の bound と Hilbert–Schmidt tail

固定窓ノートで証明した `−6<h(t)≤4+(1/2)log(1+4t²)` により、`|t|≤111` では `|h(t)|<10`。`A_a<3` と `beta=1/5` を加えて

\[
 \boxed{\sup_{|t|\le111}|\Psi_a(t)-1/5|<14}=:M_R.
                                                        \tag{W4.1}
\]

この実 band の上界は ellipse の `S=143` より鋭い。tail/coupling には `M_R`、解析的 Gauss 誤差には `M_Q` を使い、混同しない。

`Pi_d` を最初の `d` modes への射影、`E_d=I−Pi_d`、`X=aT=444/5`、`D_d=(2d+1)!!` とする。Bessel 積分から実数 `z` に対し `|j_n(z)|≤|z|^n/(2n+1)!!`。従って

\[
 \|B_TE_d\|_{HS}^2
 \le\frac{2X}{\pi}\sum_{n\ge d}\frac{X^{2n}}{((2n+1)!!)^2}
 \le\frac{2X}{\pi}\frac{X^{2d}}{D_d^2}
                        \frac1{1-X^2/(2d+3)^2}.
\]

全 mode の共通上界として、`X<2d+3` の下で有理数

\[
 \boxed{K_d^+=\frac{2X}{3}\frac{X^{2d}}{D_d^2}
                        \frac1{1-X^2/(2d+3)^2}}      \tag{W4.2}
\]

を使える。積分すると `2n+1` が相殺するため、各 Fourier 変換を単に `t=T` の値で抑える方法より鋭い。

pole tail について、`b=2/5`、`exp(a)<9/4` から

\[
 \|E_dc\|^2+\|E_ds\|^2
 <\boxed{J_d^+=\frac{18}{5}(2d+1)
   \frac{(2/5)^{2d}}{D_d^2}
   \frac1{1-(2/5)^2/((2d+1)(2d+3))}}.              \tag{W4.3}
\]

また `sqrt(sinh a+a)<4/3`。例えば `exp(4/5)<9/4` から `sinh(4/5)<65/72`、従って `sinh(4/5)+4/5<16/9` と分かる。

これらを (W1.2) の block に適用して

\[
 E_dRE_d\succeq\delta_d E_d,
 \quad\delta_d=\frac15-14K_d^+-2J_d^+,
\]
\[
 \boxed{\|\Pi_dRE_d\|\le\Gamma_d
       :=14\sqrt{K_d^+}+\frac83\sqrt{J_d^+}.}        \tag{W4.4}
\]

band coupling は `||B_T||≤1` を使い `M_R sqrt(K_d^+)`。pole は各 parity で rank 1、head と tail の even/odd vectors はそれぞれ直交するため、共通の最大値で上から抑えている。

## W5. 実用的な次数と厳密定数

下表の `K,J` は (W4.2)–(W4.3) の有理数に対する上向きの十進上界。`Gamma` と tail loss `1/5−delta` も上界である。

| full modes `d` | parity 次元 | `K_d^+` 上界 | `J_d^+` 上界 | `Gamma_d` 上界 | tail loss 上界 |
|---:|---:|---:|---:|---:|---:|
| 160 | 80 | `2.047e-43` | `5.426e-793` | `6.334e-21` | `2.866e-42` |
| 168 | 84 | `1.538e-52` | `1.239e-839` | `1.736e-25` | `2.153e-51` |
| 176 | 88 | `5.421e-62` | `1.323e-886` | `3.260e-30` | `7.589e-61` |
| 192 | 96 | `7.953e-82` | `1.766e-981` | `3.949e-40` | `1.114e-80` |
| 224 | 112 | `7.321e-125` | `1.311e-1174` | `1.198e-61` | `1.025e-123` |
| 256 | 128 | `7.317e-172` | `1.030e-1371` | `3.787e-85` | `1.025e-170` |

検算は Python の exact `Fraction` で (W4.2)–(W4.3) を作り、平方根部分を 224 bit Arb で囲んで行った。`d=160` はこの上界によって `Gamma<1e-20` と判定できる最初の偶数次数である。`d=168` で既に `Gamma<2e-25`、`d=176` なら `4e-30` 未満。`d=192` は `1e-20` より十分小さくする目的に対して大きい余裕がある。最適次数だという主張ではない。

`d=256` では解析的な coupling は `1e-84` より小さいが、固定した 32 点 Gauss の行列誤差は `1e-43` 程度である。head が要求する余裕がそれより小さい場合、次数だけを増やしても現在の求積精度では認証できず、Gauss 次数・panel 幅・球演算精度等を変更する必要がある。

## W6. 前 cycle の pointwise tail を移す場合の注意

前の半幅 `1/2` の実装を直接拡張するときは

\[
 v_d^2=2a(2d+1)\frac{X^{2d}}{D_d^2}
       \frac1{1-X^2/((2d+1)(2d+3))}
\]

が real band 上の tail evaluation vector の二乗ノルム上界となる。全 evaluation vector には Parseval で `Σ_n|F_phi_n(t)|²=2a=8/5`。従って pointwise 方式の band coupling は

\[
 \frac{T}{\pi}M_R\sqrt{2a}\,v_d,
 \qquad\text{tail deviation は }\frac{T}{\pi}M_R v_d^2.
                                                        \tag{W6.1}
\]

半幅 `1/2` のコードにあった evaluation vector norm `1` をそのまま使ってはいけない。pole の全 exponential vector に対しても、粗い上界は `sqrt(2a) exp(a/2)` であり、`exp(a/2)` だけではない。本ノートの HS 方式 (W4.4) はこの pointwise 評価を必要とせず、(W6.1) より鋭い coupling を与える。

## W7. 有限 head に残る認証条件

両 parity の exact compression に対して、全数値誤差込みで `Pi_d R Pi_d≥mu Pi_d` を得た場合に限り、

\[
 \mu>0,\quad\delta_d>0,\quad\mu\delta_d>\Gamma_d^2
                                                        \tag{W7.1}
\]

から固定窓の全複素 `f∈D` に正の下界が従う。あるいは `delta_d≥mu>Gamma_d` なら `Q_a(f)≥(mu−Gamma_d)||f||²`。これはまだ条件文である。

本ノートによって確認したのは tail floor の再利用、全係数、Gauss 誤差、無限 tail と交差項の上界である。有限 head の最小固有値・PSD・gap は計算していない。従って本ノートだけから `a=4/5` の全 `Q_W` の正値性や RH は結論しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/fixed-window-reduction.md`](fixed-window-reduction.md)
- [`proofs/audits/joint-symbol-reduction.md`](joint-symbol-reduction.md)
