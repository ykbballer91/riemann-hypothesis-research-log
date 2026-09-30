**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/zhu-reduction-audit.md` · Original SHA-256: `368f9bd6cfdc775a60069b0aba731a089a18422622f3db225531654ebc194836`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Zhu v2: finite reduction と L=0.8 認証の破壊監査

日付: 2026-09-29。担当: DESTROYER。**RH は未解決。**

固定一次資料: Xuefeng Zhu, [arXiv:2608.24827v2 HTML](https://arxiv.org/html/2608.24827v2), [固定 PDF](https://arxiv.org/pdf/2608.24827v2)。ヘッダは 2026-09-02、本文日付は September 3, 2026。取得担当が保存した TeX の §4–5 とも照合した。著者名・版を v1 の検索要約から引き継いでいない。

**結論:** 正しい高域 envelope と正しいブロック誤差を仮定した有限→無限還元は独立に確認できた。一方、本文の一般的な行列成分上界は偽であり、実際の symbol を使う反例を下記 §3 で構成した。threshold の漸近記述にも訂正が必要。ただし指定された $L=0.8,T=200,N=200$ の tail/coupling は、誤った一般上界を使わずに **両方 $10^{-100}$ 未満を独立再認証**できる。これによって 200 次 leading block の正性を認証したことにはならない。公開取得物の不足と丸め誤差の検証は別問題として残る。

旧版の $L=1.19$ は v2 §7 が明示的に撤回した主張であり、採用しない。以下の反例は表示された補助不等式への反例であり、ζ/RH の反例ではない。

## 1. 高域 envelope、符号、pole の独立確認

$H(t)=\Re\psi(1/4+it/2)-\log\pi$、
$P_L(t)=\sum_{\log n<2L}2\Lambda(n)n^{-1/2}\cos(t\log n)$、
$A_L=\sum_{\log n<2L}2\Lambda(n)n^{-1/2}$、
$\Psi_L=H-P_L$ とする。

### 1.1 Envelope の向きは v2 では正しい

すべての係数が正なので $P_L(t)\le A_L$。従って必要なのは comb の **上界**。下界 $P_L\ge-A_{\mathrm{eff}}$ からは $\Psi_L\le H+A_{\mathrm{eff}}$ が出るだけで、正性の lower certificate にならない。

この方向問題は単一の素数ブロック $a\cos\theta+b\cos2\theta$、$a,b>0$ だけでも見える。上端は $\theta=0$ の $a+b$ である。下端の絶対値を上端の代わりに使うことはできない。全有限 comb も $t=0$ で $A_L$ に達し、連続時間の torus equidistribution によって任意に高い $t$ で再び $A_L$ に近づく。$\{\log p\}$ の整数一次関係がないことは素因数分解の一意性による。この議論は離散時刻の equidistribution と混同していない。

Lemma 3.1 の解析計算も確認した。$z=5/4+it/2$ に digamma の Binet 表示を使い、$\psi(1/4+it/2)=\psi(z)-(1/4+it/2)^{-1}$ とする。積分部分の絶対値は

\[
2\frac{4}{5t}\int_0^\infty\frac{u\,du}{e^{2\pi u}-1}
=\frac1{15t}.
\]

対数項の実部は $\log(t/2)$ 以上、残る2項の損失は $5/(2t^2)+1/t^2$ 以下。$t\ge15/4$ で合計は $1/t$ 以下となる。従って

\[
\Psi_L(t)\ge \log(t/(2\pi))-1/t-A_L.
\tag{Z1}
\]

$\beta(T)=\log(T/(2\pi))-1/T-A_L>0$ なら $T>2\pi e^{A_L}\ge2\pi>15/4$。Lemma の適用開始点を別途取り落としてはいない。$(\log t-1/t)'=1/t+1/t^2>0$ なので全 $t\ge T$ で $\Psi_L(t)\ge\beta(T)$。

### 1.2 還元不等式

実偶 $f$、$F=\widehat f$ に対して Parseval は
$\pi^{-1}\int_0^\infty|F|^2=\|f\|_2^2$。pole をそのまま残すと

\[
Q(f)\ge R_T(f)=2\left|\int f(x)\cosh(x/2)\,dx\right|^2
+\frac1\pi\int_0^T(\Psi_L-\beta(T))|F|^2\,dt
+\beta(T)\|f\|_2^2.
\tag{Z2}
\]

実偶の範囲で絶対値を普通の二乗に換えてよい。**任意の複素 $f$ へ $2F(i/2)^2$ をそのまま延長してはいけない。** $f$ を $if$ に替えるだけで二乗は符号を変える一方、Hermitian form は変わらない。

一般の複素関数では pole は

\[
2\Re\!\left(F(i/2)\overline{F(-i/2)}\right)
=2|c|^2-2|s|^2,\quad
c=\int f\cosh(x/2),\ s=\int f\sinh(x/2).
\tag{Z3}
\]

実偶・実奇の分解、さらに実部・虚部の分解で形式は直和になる。実奇 sector の $-2|s|^2$ を落とすことは lower bound を上げてしまい、不正である。v2 §6 は符号反転を保持しているので、その点は破壊できなかった。

## 2. 明確な訂正 E1: threshold の差は O(T1^{-1}) ではない

$T_1=2\pi e^{A_L}$ とし、$\beta(T_0)=0$ の唯一の正根を $T_0$ とする。本文 Theorem 1.1 の直後の差のオーダーは、方程式

\[
\log(T_0/T_1)=1/T_0
\]

と整合しない。$T_0=T_1+\delta$ を代入して展開すると

\[
\delta=1-\frac1{2T_1}+\frac{2}{3T_1^2}+O(T_1^{-3}).
\tag{Z4}
\]

したがって **絶対差は $1+O(T_1^{-1})$**。$O(T_1^{-1})$ は絶対差ではなく、例えば相対差の尺度である。本文の $119.1$ 対 $120.1$ という例も差が約1であることに対応する。これは $\beta>0$ を数値で直接検査する run の無効化ではない。

## 3. 明確な誤り E2: 一般 entry bound の反例

正規直交 Legendre basis で $\nu_n=n+1/2$、
$\widehat T_n(t)=2i^n\sqrt{L\nu_n}\,j_n(Lt)$ とする。偶次数なら実数である。$W=\Psi_L-\beta$、$M=\sup_{[0,T]}|W|$ と置く。

本文 §4 の displayed bound は

\[
|C_{nm}|\ \le\
M\,2\sqrt{L\nu_n}\frac{(TL)^n}{(2n+1)!!}
\,2\sqrt{L\nu_m},
\quad
C_{nm}=\frac1\pi\int_0^T W(t)\widehat T_n(t)\widehat T_m(t)\,dt.
\tag{Z5-FALSE}
\]

一般には積分長が抜けている。$\left|j_n(x)\right|\le x^n/(2n+1)!!$ と $\left|j_m(x)\right|\le1$ を実際に積分して得られるのは

\[
|C_{nm}|\le
\frac{T}{\pi(n+1)}\,M\,
2\sqrt{L\nu_n}\frac{(TL)^n}{(2n+1)!!}
\,2\sqrt{L\nu_m}.
\tag{Z5}
\]

粗く両 factor を上端の supremum で置くなら $T/\pi$ が必要である。$T/[\pi(n+1)]\le1$ を別途確認した高次数行では原文の大きさも上界になるが、全ての行・全ての $L$ に成り立つわけではない。

### 3.1 実際の symbol による解析的反例族

$T\to\infty$ とし $L=T^{-2}$、$n=m=0$ を採る。この範囲では prime comb は空、$\beta=\log(T/(2\pi))-1/T>0$。

\[
\widehat T_0(t)=\sqrt{2L}\operatorname{sinc}(Lt).
\]

$H(t)=\log(t/(2\pi))+O(t^{-2})$ を用いると

\[
\int_0^T(H(t)-\beta)\,dt=-T+O(1),
\quad
C_{00}=-\frac{2}{\pi T}+O(T^{-2}).
\]

一方 $H$ は単調増加し $M=\log T+O(1)$ なので (Z5-FALSE) の右辺は
$2LM=2\log T/T^2+O(T^{-2})$。左辺と右辺の比は $T/(\pi\log T)\to\infty$。従って一般不等式は厳密に偽である。

### 3.2 具体的な区間演算反例

$L=1/1000,T=100,n=m=0$ で、独立な Arb 求積によって

\[
C_{00}\in -0.063502230872332937975144652576374
\ \pm 3.18\times10^{-34},
\]

\[
2LM\in0.016258953077608822933416561868014470848987894563
\ \pm2.53\times10^{-49}
\]

を得た。$-C_{00}>2LM$ を ball の厳密比較で確認した。再現コードは次の通り。複素積分上では real-part 関数を評価せず、正しい meromorphic な half-sum を使う。

~~~python
from flint import arb, acb, ctx
ctx.prec = 160
L, T, pi, I = arb(1)/1000, arb(100), arb.pi(), acb(0,1)
beta = (T/(2*pi)).log()-1/T
h0 = (arb(1)/4).digamma()-pi.log()
hT = acb(arb(1)/4,T/2).digamma().real-pi.log()
M = beta-h0
assert M > abs(hT-beta)  # monotonicity of H makes this the exact maximum
def integrand(z, analytic):
    h = ((acb(arb(1)/4)+I*z/2).digamma()
         +(acb(arb(1)/4)-I*z/2).digamma())/2-pi.log()
    return (h-beta)*2*L*(L*z).sinc()**2/pi
r = acb.integral(integrand, 0, T, abs_tol=arb('1e-35'),
                 rel_tol=arb('1e-35'), eval_limit=200000, depth_limit=40)
assert r.is_finite() and r.imag.contains(0)
assert -r.real > 2*L*M
~~~

実行環境は既存の python-flint 0.9.0。返却された包含 ball と不等式を使い、要求 tolerance を達成したという仮定には依存しない。特殊関数実装への信頼は必要。§3.1 の解析的反例はこの数値計算に依存しない。

## 4. L=0.8 の tail/coupling は修復して独立認証できる

以下は $L=4/5,T=200$、先頭の偶次数 $0,2,\ldots,398$ と、それ以後 $400,402,\ldots$ に限定する。本文の誤った一般 bound を流用せず、積分長 $T/\pi$ を全て保持する。

まず実軸で $M<10$ と置ける。実際、prime mass は $\{2,3,4\}$ の有限和 $A_L<3$、$0<\beta<1$。既に独立確認した digamma の単調性と上界から $-6<H(t)<4$ on $[0,200]$。従って $|H-P_L-\beta|<10$。

各偶次数について

\[
a_n=2\sqrt{L\nu_n}\frac{160^n}{(2n+1)!!}
\]

と置く。$|\widehat T_n(t)|\le a_n$ on $[0,200]$ であり

\[
\frac{a_{n+2}}{a_n}
=\sqrt{\frac{n+5/2}{n+1/2}}\,
\frac{160^2}{(2n+3)(2n+5)}
\le \frac{a_{402}}{a_{400}}<\frac1{25}\quad(n\ge400).
\tag{Z6}
\]

各因子は $n$ とともに減少する。$a_{400}<4.3\times10^{-108}$、従って discarded evaluation vector のノルムは

\[
\|v_D(t)\|_2\le
\eta:=\frac{a_{400}}{\sqrt{1-1/25^2}}
<1.001\,a_{400}.
\]

head evaluation vector は Legendre 展開と Parseval により

\[
\|v_A(t)\|_2^2
\le\int_{-L}^L|\cos(tx)|^2dx\le2L.
\]

よって operator-valued integral の三角不等式で

\[
\|B_C\|\le\frac{MT}{\pi}\sqrt{2L}\,\eta,\qquad
\|D_C\|\le\frac{MT}{\pi}\eta^2.
\tag{Z7}
\]

これは無限に多い tail 次数を一度に含む評価である。有限個を数値検査して無限和を推測したものではない。

pole coefficient $p_n=\langle T_n,\cosh(x/2)\rangle$ は Bessel の積分表示から

\[
|p_n|\le
2\sqrt{L\nu_n}\,e^{L/2}\frac{(L/2)^n}{(2n+1)!!}.
\]

$L/2=0.4$ なので $p_{400}$ の bound は $a_{400}e^{0.4}/400^{400}$、偶次数比は再び $1/25$ 以下。
$e^{0.4}<3/2$、$\|\cosh(x/2)\|_2<3/2$ を使えば

\[
\|B_{\rm pole}\|\le3\|p_D\|,\qquad
\|D_{\rm pole}\|\le2\|p_D\|^2.
\tag{Z8}
\]

同じ絶対値評価は奇 sector の負の pole にも使える。ただし下の具体的 first discarded order は偶 sector のものなので、奇 sector の頭行列の認証まで含むとは主張しない。

### 有理演算のみの再現コード

平方を取れば $a_{400}$ と ratio の比較まで有理演算で済む。$\pi>3,\sqrt{1.6}<1.3$ という安全な簡約を使う。次の全 assert は実行して PASS した。

~~~python
from fractions import Fraction as F
from math import factorial
n, L, x = 400, F(4,5), 160
a_squared = 4*L*F(2*n+1,2)*(
    F(2**n*factorial(n),factorial(2*n+1)))**2*x**(2*n)
ratio_squared = F(2*n+5,2*n+1)*(
    F(x*x,(2*n+3)*(2*n+5)))**2
a_upper = F(43,10**109)
assert a_squared < a_upper**2
assert ratio_squared < F(1,25)**2
q = F(1001,1000)
assert q*q*(1-F(1,25)**2) > 1
eta = q*a_upper
bC = 10*F(200,3)*F(13,10)*eta
dC = 10*F(200,3)*eta**2
p_tail = F(3,2)*eta/F(400**400)
bP, dP = 3*p_tail, 2*p_tail**2
assert bC+bP < F(1,10**100)
assert dC+dP < F(1,10**100)
~~~

得られた安全な有理上界の十進表示は
$\varepsilon_B<3.731\times10^{-105}$、
$\varepsilon_D<1.236\times10^{-212}$。
これにより本文のこの2つの **最終的な $10^{-100}$ 上界は独立に修復・確認**できる。entry bound の誤りを根拠に $L=0.8$ の正性定理そのものを反証したとは言わない。

## 5. Head/tail cross と無限次元の論理

### 5.1 Frequency split は compact-window space の直交分解ではない

実周波数上の積分を $|t|\le T$ と外側に分けること自体は厳密で、(Z2) は正しい。しかし $f$ を Fourier low-pass/high-pass に分けた2関数は一般に元の有限 support に残らない。非零関数が time と frequency の両方で compact support を持つことは Paley–Wiener と恒等定理で不可能である。

有限窓上で圧縮した band projection は prolate/time-band-limiting operator であり、射影ではない。このため frequency split に cross がないことから、Legendre/prolate の head と tail の cross が消えるとは言えない。v2 は $B$ を残しており、還元の中心部分はこの誤りを犯していない。

有限反例として
$\left(\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\right)$
は diagonal blocks が正でも最小固有値 $-1$。実・複素のいずれでも

\[
R_T\ge
\left(\min(\lambda_{\min}(A),\beta-\varepsilon_D)
-\varepsilon_B\right)I
\tag{Z9}
\]

は $2|\langle x,By\rangle|\le\|B\|(\|x\|^2+\|y\|^2)$ から正しく従う。

### 5.2 Form domain

$Q$ の有限値を持つ自然な domain は

\[
\mathcal D_L=\left\{f\in L^2[-L,L]:
\int_{\mathbb R}\log(2+|t|)|\widehat f(t)|^2dt<\infty\right\}.
\tag{Z10}
\]

固定窓では pole は bounded form、prime 部分も bounded form で、$\Psi_L(t)=\log|t|+O_L(1)$。従って $Q$ はこの domain 上の閉じた半有界形式として扱える。全 $L^2$ の任意の関数に有限の数値 $Q(f)$ が定義できるわけではない。全 $L^2$ についての定理文は、domain 外で $Q(f)=+\infty$ と定めた拡張実数形式と解釈するか、有限値 domain を明記すべきである。

他方 $R_T$ は固定有限 band 上の bounded form と bounded pole と $\beta I$ の和なので、全 $L^2[-L,L]$ 上で有界。$C$ は連続核を持つ compact operator でもある。従って (Z9) は無限 tail に対して意味を持ち、finite-dimensional dense span の点ごとの値だけを根拠にしてはいない。

### 5.3 量化

得られる含意は、**各固定 $L$** について、高域 floor、leading block、tail、cross の4条件を全て認証すれば全窓の lower bound が得られる、というもの。$L=0.8$ の一例や任意有限個の窓を認証しても、全 $L>0$ への含意はない。

$T$ を動かすときも $\beta$ を再計算する必要がある。実偶 $f$ について

\[
\frac{d}{dT}R_T(f)
=\frac{\Psi_L(T)-\beta(T)}{\pi}|F(T)|^2
+\beta'(T)\left(\|f\|^2-\frac1\pi\int_0^T|F|^2\right)\ge0
\]

なので、許容域の $T$ 増加に関する monotonicity は確認できる。$N$ の増加で個々の実装が返す certificate の下界が必ず単調増加することまでは保証しない。新旧の有効下界の最大を採れば単調な台帳は作れる。

## 6. L=0.8 の残る認証条件

Theorem 1.2 の最終値には、以下がまだ必要である。

1. exact leading block と保存された numerical block の operator-norm 誤差。
2. quadrature nodes/weights、digamma、Miller recurrence、pole 積分を含む assembly の丸め・評価誤差。
3. shifted block の Cholesky factor と、その **誘導無限ノルム（最大絶対行和）** による認証残差。最大 entry 誤差と取り違えると次元 factor が失われる。

v2 §5 の Cholesky residual lemma は、全 residual bound を厳密に持てば正しい。$\widetilde L\widetilde L^t$ は PSD であり、残差が spectral norm 以下に抑えられていれば Weyl の不等式が使える。factorization が失敗しただけでは負固有値の認証にならない。

quadrature の幾何は確認した。幅 $1/4$ の panel と ellipse parameter $6.55$ の半短径は $(6.55-6.55^{-1})/16=0.399833\ldots<0.4$。real-part digamma を meromorphic half-sum に替える点も正しい。しかし $|\Psi_L-\beta|\le20$ の複素 ellipse 全域での証明や、実際の saved matrix の値・丸め slack を独立に認証したわけではない。

細かい丸め注意: 原文の $M=49000$ をそのまま掲示 Gauss bound に入れると panel error は $1.3328\times10^{-47}$ で、$1.3\times10^{-47}$ より大きい。表示されたより細かな product bound $M\le48367.849$ でも約 $1.3156\times10^{-47}$ となる。したがってその「i.e.」の丸めは上向きでない。ただし $C_{nm}$ の integrand に含まれる $1/\pi$ と panel の縮尺を正しく使えば余裕があるため、この観察だけで主認証値を否定しない。必要なのは一貫した上向き誤差台帳である。

取得担当の報告では、固定 v2 source archive に入っていたのは TeX/README/画像で、本文が言及する行列・factor・verification script・JSON 一式は見つからなかった。本監査はその欠落を「計算が偽である」と解釈しないが、原著の 200 次 head certificate の再現完了とも記録しない。

## 7. 採用境界

- **独立確認:** Lemma 3.1 の符号・定数、正しい prime-comb bound、$\beta>0$ 下の $Q\ge R_T$、pole の parity signs、正しい2ブロック還元。
- **厳密反証・必要訂正:** threshold の絶対差のオーダー、一般 entry bound (Z5-FALSE)。
- **独立修復:** 指定偶 sector の infinite tail/coupling $<10^{-100}$。有理演算だけの再現コードを含む。
- **未認証:** 原著の 200 次 leading block の strict positivity、丸め込みの全誤差台帳、奇 sector の head certificate、全窓、RH、新規性。
- **不採用:** 撤回済み $L=1.19$ の lower certificate。正しい $A_L$ で $\beta(1100)<0$ となる run の finite matrix PSD から全形式の PSD は導けない。

編集はこの監査ファイルだけ。原著コードの取得・親担当の小例再現は、この独立解析と区別している。
