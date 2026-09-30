**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/silva-finite-zero-audit.md` · Original SHA-256: `a2c78cba29dc1ab74128e5a837a6d30a23a5233251d880aca1dbbe20f69bf6af`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Silva 2609.25564v1 — finite zero locus の限定敵対監査

2026-09-29、DESTROYER。対象は Alisson M. Silva, [Finite Rodríguez-Villegas Approximants to the Riemann ξ-Function, v1](https://arxiv.org/html/2609.25564v1)。HTML 全文の §§1–5、定理2.1・3.1・4.1と参考文献表示を読んだ。

**分類は ENABLING / PARTIAL APPROXIMATION。著者は RH の証明を主張していない。**
§5 は有限 numerator の単位円零点条件が未証明であること、局所一様収束だけでは有限近似の全零点配置や compact 集合を逃げる零点を制御しないことを明記している。

今回の結論:

- actual theta profile の $U_4$ は **単位円上に零点を一つも持たない**。この点は root の Arb certificate と本担当の独立代数・tail 監査で確認した。
- 同じ actual profile の $Z_4$ は **4零点すべてが $\Re s=1/2$ 上にある**。
- したがって「全 $U_E$ が単位円零点を持つから、そのまま有限 RV 定理を使える」という shortcut は $E=4$ で失敗する。しかし Silva の stated approximation theorems の反証でも、RH の反証でもない。

固定 HTML SHA256:

~~~text
907fd6a586d03f412da55be6fcbd89d73580170ec6fb6a013a20ffa655ac4d4d
~~~

## 1. 定理2.1の独立再導出

論文の bilateral normalization を $\xi(1/2+it)=\int_{\mathbb R}\Phi(v)e^{itv}dv$ とする。$\Phi$ は正・偶で両側に急減衰する。
$k(u)=1/(2\cosh(u/2))$、$w=\Phi*k$、$x=e^u/(1+e^u)$ と置けば $k(u)=\sqrt{x(1-x)}$。

convolution を割って直接計算すると

$$
P(x)=\frac{w(u)}{k(u)}
=\int_{\mathbb R}\Phi(v)
\frac{e^{v/2}}{x+(1-x)e^v}\,dv.
$$

$v$ と $-v$ を組にすることにより

$$
P(x)=G(x(1-x)),\qquad
G(p)=\int_0^\infty
\frac{2\Phi(v)\cosh(v/2)}{1+4p\sinh^2(v/2)}\,dv.
$$

これは正の Stieltjes mixture。有限な正 measure と、急減衰によるすべての moment の可積分性が endpoint continuity と微分を支える。$(-1)^nG^{(n)}(p)>0$ もこの actual measure に対して成立する。

また $0<\Re s<1$ で

$$
\int_{\mathbb R}k(u)e^{(s-1/2)u}du=\frac{\pi}{\sin\pi s}.
$$

Fubini と logistic substitution により

$$
\xi(s)=\frac{\sin\pi s}{\pi}
\int_0^1P(x)x^{s-1}(1-x)^{-s}dx.
$$

**独立判定: YES。** この positivity は実 $x$ 上の profile の positivity であり、複素 $s$ の積分や numerator polynomial の零点位置の positivity theorem ではない。

## 2. 定理3.1の algebra・収束の監査

even $E$ に対し $u_{E,j}=(-1)^j\binom EjP(j/E)$、
$U_E(q)=\sum_j u_{E,j}q^j$、
$Z_E(s)=\sum_j u_{E,j}\binom{E-j-s}{E}$。
Bernstein polynomial を $x=-q/(1-q)$ に代入すると、Möbius identity は直接従う。
対称な samples と even $E$ により係数は reciprocal。

beta integral の $j$ 項について、独立に

$$
\frac{\sin\pi s}{\pi}
\frac{\Gamma(s+j)\Gamma(E-j+1-s)}{\Gamma(E+1)}
=(-1)^j\binom{E-j-s}{E}
$$

を reflection formula から確認した。よって $Z_E$ の積分表示と $Z_E(1-s)=Z_E(s)$ は整合する。

compact $K$ が strip 内にあれば、$0<\delta\le\Re s\le1-\delta$ と取れる。差の絶対値は

$$
C_K\|B_EP-P\|_\infty
\int_0^1x^{\delta-1}(1-x)^{\delta-1}dx
$$

で抑えられ、Bernstein approximation により0へ収束する。ここに零点配置の仮定は要らない。

**独立判定: YES。** 定理4.1の Fock supertrace / Gibbs trace も各 particle sector の次元 $\binom Ej$ を数える恒等式として確認した。
正の Gibbs observable を持つことと、complex fugacity の supertrace の零点が単位円にあることは別命題である。

## 3. $E=4$ の numerator: 正しい判別式

$P_0=P(0)>0$、$a=P(1/4)/P_0$、$b=P(1/2)/P_0$ とすると

$$
\frac{U_4(q)}{P_0}=1-4aq+6bq^2-4aq^3+q^4.
$$

$q\ne0$、$y=q+q^{-1}$ と置けば

$$
\frac{U_4(q)}{P_0q^2}=y^2-4ay+(6b-2).
$$

この $y$ quadratic の判別式は $4d$、ただし

$$
d=4a^2-6b+2.
$$

$d<0$ なら $y$ の二根は非実数。一方 $|q|=1$ なら $y=2\Re q\in[-2,2]$ は実数なので、$U_4$ は単位円上に零点を持たない。

これは reciprocal symmetry に完全に両立する。symmetry が与えるのは reciprocal/conjugate の零点組であり、各零点が固定 locus 上にあることではない。

## 4. actual $U_4$ と actual $Z_4$ は異なる零点配置

root の [certificate script](../../../../artifacts/experiments/scripts/silva_degree_four_certificate.py) と [結果](../../../../artifacts/experiments/results/silva-degree-four-certificate.json) は

$$
a=0.99136318370401902158\ldots,\qquad
b=0.98857418294043949973\ldots
$$

を enclosure し、

$$
\boxed{d<-0.00024124<0}
$$

を Arb の確定比較で証明している。

しかしこれは $Z_4$ の off-critical-line zero を意味しない。binomial polynomial を独立に展開したところ、$z=s-1/2$ に対して

$$
\frac{Z_4(s)}{P_0}=Az^4+Bz^2+C,
$$

$$
A=\frac{1-4a+3b}{12},\qquad
B=\frac{43-28a-15b}{24},\qquad
C=\frac{35+20a+9b}{64}.
$$

同じ certificate が

$$
A>0,\quad B>0,\quad C>0,\quad B^2-4AC>0
$$

を確認する。$z^2$ の二根は実、積が正、和が負なので両方とも負。従って4つの $z$ は purely imaginary である。
参考値は $A\simeq2.2484500\cdot10^{-5}$、$B\simeq0.01721742134$、$C\simeq0.99569423938$、
$B^2-4AC\simeq0.0002068888474$。
小数値は表示用であり、符号は enclosure の確定比較を使っている。

**Rodríguez-Villegas の単位円条件は十分条件であり、必要条件と取り違えてはいけない。**
今回の actual degree four は、その条件が失敗しても critical-line transform が生じる具体例である。

この逆命題の失敗自体は既知。[Rodríguez-Villegas (2002), p.2252, Remark 5](https://frvillegas.github.io/pdf/frv-hilbert-functions.pdf) は $U(q)=q^3+23q^2+23q+1$、分母 $(1-q)^4$ に対して $H(x)=(2x+1)^3$ を挙げている。一次 PDF の該当表示も独立に確認した。今回の actual $U_4/Z_4$ の計算を、一般的な逆命題の初反例とは扱わない。

## 5. 認証 script の normalization・tail の独立監査

本担当は script と出力を read-only で読み、source hash の一致を確認した。別精度での数値再実行は行っていない。

### 5.1 bilateral theta normalization

$v\ge0$ で script は

$$
\Phi(v)=\sum_{n\ge1}
\left(4\pi^2n^4e^{9v/2}-6\pi n^2e^{5v/2}\right)
e^{-\pi n^2e^{2v}}
$$

を使う。$h(v)=e^{v/2}\sum_{n\ge1}e^{-\pi n^2e^{2v}}$ とすれば、
直接微分で $\Phi=h''-h/4$。
theta の modular relation による $h'(0)=-1/4$ と部分積分を使うと
$\xi(s)=2\int_0^\infty\Phi(v)\cosh((s-1/2)v)dv$ となり、bilateral の係数は正しい。
特に

$$
P(0)=2\int_0^\infty\Phi(v)\cosh(v/2)dv=\xi(0)=\frac12.
$$

script の $P_0$ enclosure が $1/2$ を含むことはこの厳密 normalization と一致する。contains だけを独立した等号の証明にはしていない。

### 5.2 二種類の tail majorant

$n\ge1,v\ge0$ で各 theta summand は正。profile denominator は $p\ge0$ に対し1以上なので、paired integrand は

$$
8\pi^2\sum_{n\ge1}n^4 e^{5v-\pi n^2e^{2v}}
$$

以下。$y=e^{2v}$、$dv=dy/(2y)$、$y^{3/2}\le y^2$ により、下端 $y_0\ge1$ からの tail は

$$
4\pi^2\sum n^4\int_{y_0}^\infty y^2e^{-\pi n^2y}dy
$$

以下である。各積分を評価し分母の $n^2,n^4,n^6$ を1に置き換えて大きくすると

$$
\text{各項}\ \le C(y_0)n^4e^{-\pi n^2y_0},
\quad
C(y)=4\pi^2\left(\frac{y^2}{\pi}+\frac{2y}{\pi^2}+\frac2{\pi^3}\right).
$$

隣接項の比は $16e^{-\pi(2n+1)y_0}$ 以下。これが script の
$K=4$ に対する omitted-$n$ tail と、$T=2$ に対する omitted-$v$ tail の幾何級数上界を与える。
両 tail の重複部分は過大評価なので安全。認証出力はそれぞれ約 $1.123\cdot10^{-30}$、$1.220\cdot10^{-70}$。

finite integral の callback は complex variable の meromorphic operations のみを使い、実部を取り出すのは積分後。tail を絶対誤差 radius に加える処理も安全である。

**判定: analytic tail・normalization・有限 degree-four algebra の読取監査 YES。**

~~~text
script SHA256:
97cc252a36fbc4bd32ac219e306ddc3ebae42741d079ae010c91e73525b84409
results SHA256:
ee328b0f1ff57437a9ece334ac922f4b97fdb7dcaf64bf47578867132807182a
~~~

## 6. 一般 Stieltjes profile の厳密有理反例

以下は theta profile ではない。一般的な positivity / symmetry / Stieltjes 性から零点配置を推論する際の有限模型であり、Silva の actual data や $\xi$ の反例とは区別する。

### 6.1 単位円条件は必要条件でない

指定された

$$
G(p)=\frac34+\frac1{4(1+1000p)},\qquad P(x)=G(x(1-x))
$$

は正の二原子 Stieltjes mixture、$P(0)=1$。厳密に

$$
a=\frac{1133}{1508},\qquad b=\frac{377}{502},\qquad
d=-\frac{35390625}{142697516}<0.
$$

従って $U_4$ の全零点は単位円外。しかし

$$
A=\frac{15625}{757016},\quad
B=\frac{674875}{1514032},\quad
C=\frac{10746881}{12112256},
$$

$$
B^2-4AC=\frac{17971015625}{143268306064}>0.
$$

ゆえに対応する $Z_4$ は4零点とも critical line 上にある。

### 6.2 Stieltjes 性だけでは $Z_4$ の critical-line 性も保証しない

独立に mass を変えた模型

$$
\widetilde G(p)=\frac{99}{100}+\frac1{100(1+1000p)}
$$

も同じ positivity・symmetry・strict complete monotonicity を持つ。このとき

$$
a=\frac{1493}{1508},\qquad b=\frac{497}{502},
$$

$$
A=\frac{625}{757016},\quad
B=\frac{26995}{1514032},\quad
C=\frac{12057641}{12112256},
$$

$$
\boxed{B^2-4AC=-\frac{425455975}{143268306064}<0.}
$$

$z^2$ の二根は非実数なので、$z$ は purely imaginary ではなく、$Z_4$ に off-critical-line zeros が存在する。
この反例は **一般 Stieltjes 仮定だけ**を否定する。actual theta profile の $Z_E$ に同じことが起こるとは結論しない。

### 6.3 有理数計算の再現

次の標準 Python コードを実行し、上の全分数を独立確認した。浮動小数点を使わない。

~~~python
from fractions import Fraction as F
for eps in (F(1, 4), F(1, 100)):
    G = lambda p: 1-eps + eps/(1+1000*p)
    a, b = G(F(3, 16)), G(F(1, 4))
    A = (1-4*a+3*b)/12
    B = (43-28*a-15*b)/24
    C = (35+20*a+9*b)/64
    print(a, b, 4*a*a-6*b+2, A, B, C, B*B-4*A*C)
~~~

## 7. 有効な構造と未解決の橋

定理2.1・3.1の具体的 profile representation、exact symmetry、local uniform approximation は今回の反例で失われない。Gibbs trace の構成も有限恒等式として残る。

無限に大きい even $E$ の部分列で actual $Z_E$ の零点がすべて critical line 上にあることを別に証明できれば、左右の half-strip に Hurwitz を適用するルートはある。しかしこれは新しい零点配置の前提であり、現在の positivity・reciprocity・Stieltjes 性だけから出ていない。

逆向きの RH $\Rightarrow$ この特定の $Z_E$ 列の全 finite-degree 零点配置は本監査では証明していない。samples $P(j/E)$ は $E$ に依存するので、固定 Taylor coefficients から作る Jensen polynomials の既知の基準と同一視もしない。RV sufficient condition の逆が一般に偽であること自体の新規性は主張しない。

$U_4$ の反例は「全 even degree の numerator が単位円零点」という一律 shortcut を停止する。より大きな degree の部分列や actual $Z_E$ 自体への別の theorem を否定する blanket impossibility ではない。今回、その未証明条件を補う新しい仮定を採用せず、bounded audit を終了する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/silva-degree-four-certificate.json`](../../../../artifacts/experiments/results/silva-degree-four-certificate.json)
- [`experiments/scripts/silva_degree_four_certificate.py`](../../../../artifacts/experiments/scripts/silva_degree_four_certificate.py)
