**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/imbalance-adversarial.md` · Original SHA-256: `1d43e547d33a8ba50064e6e3c21e4fa29f8e273f5e456547f0fa698b54bbfb4d`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Fixed-product imbalance: bounded rejection

2026-09-29。担当 DESTROYER。判定: **各項の最小化は正しいが、零点から最小化を導く構造論的推論は明示的反例で棄却。ここで当該推論の探索を終了する。** RH は OPEN。本稿の整関数は toy model であり、ζ/RH の反例ではない。

## 1. 正しい恒等式と、未証明の含意

$n\ge2,\ \sigma\in\mathbb R,\ \delta=\sigma-1/2$ とする。

$$
E_n(\sigma)
=(n^{-\sigma}-n^{-(1-\sigma)})^2
=\frac4n\sinh^2(\delta\log n)\ge0.
$$

従って $E_n(\sigma)=0\Longleftrightarrow\sigma=1/2$。また

$$
n^{-\sigma}n^{-(1-\sigma)}=n^{-1},\qquad
E_n(\sigma)=n^{-2\sigma}+n^{-2(1-\sigma)}-2/n.
$$

この積の固定、AM–GM、$\sigma\leftrightarrow1-\sigma$ 対称性は、中心がエネルギー最小点であることを与える。それらから「$\xi(\sigma+it)=0$ なら最小点である」は従わない。零点条件とこの最小化問題を結ぶ追加の定理が必要である。

固定重み $w_n\ge0$ で少なくとも一つの $n_0\ge2$ に $w_{n_0}>0$ があるとする。通常の非負項和

$$
\mathcal E(\sigma)=\sum_{n\ge2}w_n E_n(\sigma)
$$

について、和が有限の範囲では、また非負拡張実数値を許しても、

$$
\boxed{\mathcal E(\sigma)=0\Longleftrightarrow\sigma=1/2.}
$$

一つの正の重みの項が既に必要性を与えるため、極限交換や微分は不要である。さらに

$$
\mathcal E(\sigma)\ge
\frac{4w_{n_0}}{n_0}(\log n_0)^2(\sigma-1/2)^2.
$$

従って全非自明零点について

$$
\xi(\rho)=0\Longrightarrow\mathcal E(\Re\rho)=0
$$

という主張は **RH と厳密に同値**。エネルギーの名称、重み選択、有限和への変更によってこの論理的内容は弱まらない。$n=1$ だけの項、全零重み、符号付き重み、零点ごとに退化する重みは非退化性の仮定を失い、上の同値命題とは別物になる。

収束の例として $w_n=n^{-2}$ なら $0\le\sigma\le1$ で一様収束し

$$
\mathcal E(\sigma)
=\zeta(2+2\sigma)+\zeta(4-2\sigma)-2\zeta(3).
$$

これは収束域内の通常の級数の恒等式で、正値性を解析接続から借りていない。しかし $\xi$ の零点上でこの量が零になる理由は依然としてない。

## 2. 対称・実型・order 1 の明示的な反例

$z=s-1/2$ と置き

$$
P(z)=((z-1/4)^2+1)((z+1/4)^2+1),\qquad
G(s)=C\cosh(z)P(z),\qquad
C=\frac{128}{425\cosh(1/2)}>0.
$$

すると次を全て満たす。

- 整関数で order は正確に $1$。多項式倍の $\cosh$ なので上界は指数型、実軸の成長から order $<1$ ではない。
- $P(-z)=P(z)$、$\cosh(-z)=\cosh(z)$ より $G(1-s)=G(s)$。
- 係数と $C$ は実なので $G(\overline s)=\overline{G(s)}$。
- 実軸上では全ての二次因子と $\cosh$ が正なので $G(s)>0$。
- $P(1/2)=425/256$ より $G(0)=G(1)=1/2$。
- $s=3/4+i,3/4-i,1/4+i,1/4-i$ に軸外 quartet の零点がある。$\cosh$ による他の零点は中心線上にある。従って全零点は開いた critical strip 内にある。

一方、全ての複素 $s$ と整数 $n\ge2$ で

$$
n^{-s}n^{-(1-s)}=n^{-1}
$$

は厳密に成立する。これは正の実数 $n$ に対する実対数を用いた指数の恒等式であり、$G$ や $\xi$ の性質に依存しない。

しかし上記の零点 $s_0=3/4+i$ では

$$
G(s_0)=0,\qquad
E_2(\Re s_0)=\frac3{2\sqrt2}-1>0
$$

である。最後の符号は $9>8$ だけで証明できる。全ての固定非負非退化 aggregate に対しても $\mathcal E(3/4)>0$。

従って「fixed product、実型、中心反射対称、order 1、実軸正、critical strip 内の零点」を前提にしても、零点で imbalance が消えるとは言えない。この一般推論は反例で終了する。$G$ に ζ の Euler product、Gamma factor、同じ零点計数、明示公式まであるとは主張していない。それらを使う別定理が実際に提示されない限り、元の推論の救済にはならない。

## 3. 複素平方・絶対値平方は別の量

実数 $\sigma$ の式を holomorphic に延長すると

$$
\widetilde E_n(s)
=(n^{-s}-n^{-(1-s)})^2
=\frac4n\sinh^2((s-1/2)\log n).
$$

中心線上では

$$
\widetilde E_n(1/2+it)=-\frac4n\sin^2(t\log n)\le0.
$$

例えば $n=2,\ t=\pi/(2\log2)$ では正確に $-2$ である。実軸上の非負性を複素引数へ解析接続することはできない。正係数 Dirichlet 多項式でも $D(s)=2^{-s}$ は $s=\sigma+i\pi/\log2$ で $-2^{-\sigma}<0$。

絶対値平方へ置き換えると非負になるが、

$$
|n^{-s}-n^{-(1-s)}|^2
=\frac4n\{\sinh^2((\sigma-1/2)\log n)+\sin^2(t\log n)\}.
$$

その消失には $\sigma=1/2$ に加えて $t\log n\in\pi\mathbb Z$ が必要。$n=2,3$ の両方に正の重みがあれば、同時消失は $t=0$ だけである。非零の $t$ で同時に整数倍なら $\log2/\log3$ が有理となり、一意分解に反する。従ってこの絶対値平方は「中心線上の零点で消える」目的にも適合しない。

元の実数エネルギーは

$$
(|n^{-s}|-|n^{-(1-s)}|)^2=E_n(\sigma)
$$

と書けば保存できるが、この量は非正則であり、零点からの消失は第1節の RH 同値命題のままである。

## 4. 正則化は非負性の証明にならない

正項和の減算正則化は符号を保存しない。具体的に $\varepsilon>0$ で

$$
S(\varepsilon)=\sum_{n=1}^{\infty}e^{-\varepsilon n}
=\frac1{e^\varepsilon-1}>0,\qquad
S(\varepsilon)-\frac1\varepsilon\longrightarrow-\frac12.
$$

この有限部分は負である。$\zeta(0)=-1/2$ も同じ注意の具体例だが、発散する正項級数 $\sum1$ の通常の和を負と主張しているわけではない。[DLMF 25.6.1](https://dlmf.nist.gov/25.6.E1)

したがって numerical cutoff、counterterm subtraction、analytic continuation によって収束量を作れたとしても、元の各項の非負性を完成した量へ自動移植してはいけない。正則化後の量について、独立した正値性と零点条件との同一性の両方が必要。

## 5. 最終判定

成立する部分は中心での imbalance 最小化のみ。構造だけから零点の最小化を結論する候補は $G$ により反証済みであり、この候補の延長は行わない。実際の $\xi$ の零点に限定した消失命題は RH と同値で、未証明のままである。
