**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/window-half-certificate.md` · Original SHA-256: `b4ef75a70c205b23d7952b4b02b53dde9161c18f31b6eb7d4e41b309307b9a78`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定窓 [-1/2,1/2] の全mode正値性 — 独立計算証明

2026-09-29。**RHはOPEN。この1つの窓だけの計算機援用証明。新規性は主張しない。**

## 正確な命題と定義域

F(t)=∫f(x)e^(itx)dx、H=L²([-1/2,1/2])を零延長して考える。

\[
\mathcal D=\{f\in H:\int_{\mathbb R}\log(2+|t|)|F(t)|^2dt<\infty\}.
\]

既存のWeil明示公式と同じ幾何側の形式について、次を認証する。

\[
\boxed{Q_W(f)\ge9\cdot10^{-8}\|f\|_2^2\qquad(f\in\mathcal D).}
\]

複素関数も含む。特にこのsupportを持つ全C_c∞試験関数を含む。
正のlog重みの積分が無限のfには下有界形式を+∞へ拡張して扱えるが、
零点側の絶対収束を全L²で主張するものではない。
全実線L²のclosableなWeil形式や全窓共通のgapの主張ではない。

この窓はZhu v2が主張する[-.8,.8]より小さい。
その公表計算証明書は取得できず、本計算はZhuの数値定理を前提としない。
還元の先行性は [Zhu v2, §§3–5](https://arxiv.org/html/2608.24827v2) に明示する。
同論文の一般entry boundの不備とhead証明書未取得は
[別監査](zhu-reduction-audit.md) と [取得記録](../../../literature/literature/notes/zhu-certificate-audit.md) に残す。

## 有限系へ落とす独立な不等式

a=1/2と置く。log n<2aの素数冪はn=2だけなので

\[
A=\sqrt2\log2,\quad
h(t)=\Re\psi(1/4+it/2)-\log\pi,\quad
\Psi(t)=h(t)-A\cos(t\log2).
\]

一般の複素fに対してpole項は
2|〈f,cosh(x/2)〉|²−2|〈f,sinh(x/2)〉|²。
従ってQは偶・奇の複素部分空間に直和分解する。偶poleは正、奇poleは負。

T=32、β=log(T/(2π))−1/T−Aとする。Binet表示とψ(z+1)=ψ(z)+1/zから、
t≥15/4について h(t)≥log(t/(2π))−1/t を独立に導ける。
z=5/4+it/2とすると積分剰余は1/(15t)、二つの有理項の実部は
それぞれ5/(2t²),1/t²で抑えられ、その和が1/t以下。
全t>0で同じ下界を与える別の初等証明は [fixed-window-reduction.md](fixed-window-reduction.md)。
従って |t|≥T では Ψ(t)≥β>0。

\[
R_T(f)=\beta\|f\|^2+\mathrm{pole}(f)
+\frac1{2\pi}\int_{-T}^{T}(\Psi(t)-\beta)|F(t)|^2dt
\quad\Longrightarrow\quad Q_W(f)\ge R_T(f).
\]

R_TはH全体上のbounded self-adjoint形式。有限基底はこの**同じ**R_Tのexact compression。
Qの高周波部分を誤差の符号不明のまま捨てていない。
R_Tの全H上の正値性を示すので、Legendre基底がQのoperator coreかどうかはここでは不要。
Legendre族の通常のL²完備性とbounded R_Tへの移行だけを使う。

## 基底と数値head

\[
\phi_n(x)=\sqrt{(2n+1)/(2a)}P_n(x/a),\quad
F_{\phi_n}(t)=\sqrt{2a(2n+1)}i^n j_n(at).
\]

球Bessel積分表示は [DLMF 10.54](https://dlmf.nist.gov/10.54) に照合した。
even n=0,2,…,62とodd n=1,3,…,63を別々に32次headへ取る。
C行列の実振幅は (-1)^floor(n/2)√(2n+1)j_n(t/2)。
この位相をpoleへ誤って移さず、pole係数は対応parityで正のmodified Bessel値を用いる。

実装はj_n(z)=z^n/(2n+1)!!·0F1(n+3/2;−z²/4)を使う。
pole係数は√(2n+1)(1/4)^n/(2n+1)!!·0F1(n+3/2;1/64)。
正規化、係数2、odd poleの負符号を独立監査した。

128個の幅1/4のpanel、各32点Gauss–Legendre求積を使用。
nodesとweightsは `arb.legendre_p_root(..., weight=True)` が返す認証ball。
すべての演算は192bit Arb。浮動行列の正の固有値を証明の代用にしない。

## 求積誤差を明示的に覆う

各panelのBernstein ellipseのparameterをρ=6とする。
複素tの範囲は |Im t|<.4, −.3<Re t<T+.3。
ψの実部は半和[ψ(1/4+it/2)+ψ(1/4−it/2)]/2へ解析的に延長する。
最寄りのpoleはIm t=±.5なのでellipse上にない。

Re z≥.05, |z|≤T/2+.6の場合、
ψ(z)=−γ−1/z+Σ_(k≥1) z/[k(k+z)] から
|ψ(z)|≤1+20+2|z|≤T+22.2。
logπ<2、|cos(t log2)|<2により

\[
|\Psi(t)-\beta|\le M_0:=T+25+2A+|\beta|.
\]

Poisson–Legendre表示から |j_n(at)|≤exp(a|Im t|)。したがってhead全成分の
1/π込みの被積分関数は

\[
M=\frac{M_0(2d-1)e^{.4}}\pi,\qquad d=64
\]

で抑えられる。独立に導いた保守的なGauss剰余は、次数2q−1までのChebyshev近似を用いて

\[
\varepsilon_{\mathrm{entry}}
\le\frac{4TM\rho^{1-2q}}{\rho-1},\qquad q=32.
\]

証明: ellipse上の上界MからChebyshev係数は2Mρ^(−k)以下。
次数2q−1までの切断剰余は2Mρ^(1−2q)/(ρ−1)以下。
q点Gaussはその多項式にexact、積分と正のweightsの和が各2なので、
[-1,1]上の剰余作用素ノルムは4以下。各panelの変数変換と全幅Tを戻すと上式。
数値的な収束差を誤差保証に使っていない。

得たε_entry<8.713×10^(−45)を各成分ballに明示的に加えた。
poleとβは特殊関数ballで直接囲み、追加の非認証求積はない。

両headについて**厳密な10^(−7)Iを引いた後**にinterval LDLを実行し、
各32個、計64個のpivotがすべて厳密に正になった。
よって両head A_parity≽10^(−7)I。
JSONは全head ball・全pivot・L因子を含む。pivotを固有値とは呼ばない。

## 無限tailと交差項

d=64、X=aT=16、y=a/2=1/4とする。

\[
b_n=\frac{\sqrt{2n+1}X^n}{(2n+1)!!},\quad
\frac{b_{n+1}}{b_n}=\frac{X}{\sqrt{(2n+1)(2n+3)}}
\le r=\frac{16}{129}<1.
\]

全次数n≥64を含む保守的評価
v_tail≤b_64/√(1−r²)<6.237×10^(−32)を得る。
奇・偶を合わせた上界なので、両parity個別にも使える。
pole側もPoisson表示で exp(y)y^n/(2n+1)!! を使い、
η_tail<2.017×10^(−147)。

完全Legendre族のevaluation vectorにはParsevalでΣ_n|F_φn(t)|²=2a=1。
head vectorのノルムも1以下。poleの全vectorはe^y以下。
したがってsigned Cとpoleを合わせ、

\[
\|B\|\le\varepsilon_B=\frac{M_0T}\pi v_{tail}+2e^y\eta_{tail}
<3.785\cdot10^{-29},
\]
\[
D\succeq(\beta-\varepsilon_D)I,\quad
\varepsilon_D=\frac{M_0T}\pi v_{tail}^2+2\eta_{tail}^2
<2.361\cdot10^{-60}.
\]

**T/πを保持している。** 本文の不備のあるentry boundを使っていない。
β>.616、従ってδ=β−ε_D>10^(−7)。二つのblockの標準不等式から

\[
R_T\succeq[\min(10^{-7},\delta)-\varepsilon_B]I
\succeq9\cdot10^{-8}I.
\]

これはheadの有限PSDだけから全体を結論したものではない。
無限tailの総和と交差項を解析的に覆っている。
より強いHilbert–Schmidt boundを用いる別導出はbuilderの固定窓監査に保存。

## 再実行・異常系・適用境界

```sh
.venv-cert/bin/python experiments/scripts/window_half_certificate.py
.venv-cert/bin/python experiments/scripts/window_half_crosscheck.py
```

依存版は `experiments/requirements-cert.txt`。実行約6秒は当環境の観測値にすぎない。
`experiments/results/window-half-T32-cut64.json` が本証明書。
`window-half-crosscheck.json` は別方式のadaptive積分とJSON再読込の照合。

初回の未確定結果は、installed python-flintで0を跨ぐarb ballに一般の `**2` を使うと
nanになる挙動によるものだった。LDLの平方を `x*x` に修正し再実行した。
元の未認証行列は `window-half-T32-cut64-unverified.json` に、成功結果と分離して保存。
これは負固有値の検出でも、precision不足を無視した成功でもない。
前cycleのGroskin小例も同じhelper変更後に再認証・比較し、元の結論を維持した。

本結果は、標準の特殊関数恒等式、Weil幾何側の規約、Arb/FLINT実装と実行環境を信頼基盤とする。
Leanで全解析・全求積を形式検証した結果ではない。
添付された構造着想の論文は証明の前提でも引用根拠でもない。
一つの窓で成立した9×10^(−8)を大きい窓に再利用することはできない。
全窓の正値性、RH、新しい一様算術評価は依然未証明。

独立監査: BUILDERは別の高周波・Hilbert–Schmidt/Schur評価と実装の規約を検証。
DESTROYERはellipseと全tailを別導出し、224bitで再実行、さらに別実装のinterval Choleskyで
保存された両headを再検証した。記録は [window-half-independent.md](window-half-independent.md)。
rootの別adaptive積分による5成分照合もすべて元のGauss誤差ballに包含された。
完全RH候補の監査A/B/Cを通過したという意味ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/requirements-cert.txt`](../../../reports/experiments/requirements-cert.txt)
- [`experiments/results/window-half-T32-cut64.json`](../../../../artifacts/experiments/results/window-half-T32-cut64.json)
- [`experiments/scripts/window_half_certificate.py`](../../../../artifacts/experiments/scripts/window_half_certificate.py)
- [`experiments/scripts/window_half_crosscheck.py`](../../../../artifacts/experiments/scripts/window_half_crosscheck.py)
- [`literature/notes/zhu-certificate-audit.md`](../../../literature/literature/notes/zhu-certificate-audit.md)
- [`proofs/audits/fixed-window-reduction.md`](fixed-window-reduction.md)
- [`proofs/audits/window-half-independent.md`](window-half-independent.md)
- [`proofs/audits/zhu-reduction-audit.md`](zhu-reduction-audit.md)
