**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/selfdual_theta_boundary.md` · Original SHA-256: `91c10b91b78fa1a7352217f58f1296b7ce95b0e35f344450e3a6d3a4c242746e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# exact modular構成とGaussian固有の条件

2026-09-29。前巡の「有限素数和を切ってから偶延長する」案は終了済み。
今回はPoissonの自己双対性を最初から保つtest functionを構成した。
以下の結論は**標準のξやRHの反例ではない**。標準のGaussianに固有のMellin因子を
使わず、自己双対性・正値性・臨界帯への限定だけで零点を拘束する案への反例である。

## 1. 保持できる構造と、消せない共通因子

Fourier規約は \(\widehat f(y)=\int_\mathbb R f(x)e^{-2\pi ixy}dx\)。
実Schwartz関数 \(\widehat f=f\) は偶で、Poisson和から

\[
\Psi_f(t)=e^{t/2}\sum_{n\in\mathbb Z}f(ne^t)=\Psi_f(-t),
\qquad \Phi_f=\tfrac12(D_t^2-1/4)\Psi_f
\]

は偶になる。\(\Psi_f\) の両端の非減衰項は \(f(0)e^{|t|/2}\) で、
完成操作がこの項を消す。残りは任意の指数関数より速く減衰する。
従って \(B_f(s)=\int\Phi_f(t)e^{(s-1/2)t}dt\) は整関数。

\(M_f(s)=\int_0^\infty f(x)x^{s-1}dx\) をまず \(\Re s>0\) で定義する。
\(\Re s>1\) で和と積分の絶対収束と部分積分を使うと

\[
B_f(s)=s(s-1)\zeta(s)M_f(s)=\xi(s)A_f(s),\qquad
A_f(s)=\frac{2\pi^{s/2}M_f(s)}{\Gamma(s/2)}. \tag{1}
\]

偶関数の原点Taylor多項式を順に引けば、\(M_f\) の極は \(s=-2m\) の
単純極のみ。\(1/\Gamma(s/2)\) がすべてを消すため \(A_f\) も整関数である。
(1)は全平面へ延長できる。\(A_f(1-s)=A_f(s)\) も従う。
特にξの零点はtest functionの変更では打ち消せず、局所一様極限でも残る。
この枠での新しい正値性証明には、元の算術因子に対する制御がなお必要。

例えば \(f=(I+\varepsilon A^2)g\)、\(\varepsilon=1/100\) なら、後述の下界で
seedもcompleted kernelも正となり、追加因子 \(1+\varepsilon(s-1/2)^2\) の零点は
中心線上だけにある。しかし、この完成関数の全零点が中心線上にあるという命題は
**そのままRHと同値**。独立な弱い補題として採用しない。

## 2. 初めから自己双対な有限微分変形

\(g(x)=e^{-\pi x^2}\)、\(A=x\partial_x+1/2\) と置く。
積分による直接計算で \(\mathcal F A=-A\mathcal F\) なので、
\(A^{2j}g\) は自己Fourier。\(q=\pi x^2\) に対し

\[
\frac{A^2g}{g}=R_2(q)=\tfrac14-6q+4q^2,
\quad
\frac{A^4g}{g}=R_4(q)=\tfrac1{16}-39q+166q^2-112q^3+16q^4. \tag{2}
\]

再帰式は \(R\mapsto2qR'+(1/2-2q)R\)。
\(D_t\Psi_f=\Psi_{Af}\) だから、自己双対性と完成操作を保ったまま

\[
f=(I+aA^2+bA^4)g,\qquad
\widetilde\Phi=(I+aD_t^2+bD_t^4)\Phi \tag{3}
\]

を得る。全整数和を維持しており、原点で貼り合わせる操作はない。

\[
N=16385^2=268468225,\quad a=524256/N,\quad b=256/N,
\quad c=1+a/4+b/16=268599305/N.
\]

以下では最後に \(f\) と \(\widetilde\Phi\) を正の \(c\) で割る。
これにより \(f(0)=\int f=1\) と通常の端点規格化も回復する。

## 3. 全実線での厳密な正値性

\(R_2\ge-2\)。また
\(R_4=(4q^2-14q)^2-30q^2-39q+1/16\) より \(0\le q\le7\) で
\(R_4\ge-27887/16\)。\(q\ge7\) では
\(R_4=16q^3(q-7)+q(166q-39)+1/16>0\)。従って

\[
\boxed{f/g\ge1-2a-(27887/16)b=266973521/N>0.} \tag{4}
\]

完成theta核についても、点の数値確認でなく全項に共通の下界を証明できる。
各項を \(e^{t/2}V_0(x)e^{-x}\)、\(x=\pi n^2e^{2t}\)、\(t\ge0\) と書くと

\[
V_0=4x^2-6x,
\quad V_2=16x^4-112x^3+165x^2-(75/2)x,
\]
\[
V_4=64x^6-1056x^5+5176x^4-8512x^3+(15465/4)x^2-(1875/8)x
\]

が元の項、二階微分、四階微分の多項式である。\(x\ge\pi>3\) で

\[
\frac{V_2}{V_0}=4x^2-22x+\frac{33}4+\frac6{2x-3}\ge-\frac{87}4,
\]
\[
\frac{V_4}{V_0}=16x^4-240x^3+934x^2-727x-\frac{1983}{16}-\frac{489}{2x-3}
\ge-\frac{13139071}{16}. \tag{5}
\]

最後の評価は、\(3\le x\le15\) で負項だけをそれぞれ上端／下端で評価する。
\(x\ge15\) では \(16x^3(x-15)\ge0\)、残りの
\(934x^2-727x-1983/16-489/(2x-3)\) も正。
従って全項を足し、偶性で負側へ延長すると

\[
\boxed{\widetilde\Phi/\Phi
\ge1-(87/4)a-(13139071/16)b
=46840521/N>1/6.} \tag{6}
\]

(4)、(6)は規格化前の比。\(c\) で割った後も厳密な正値性を保つ。
すべて有理数と \(\pi>3\) による全域評価である。

## 4. 臨界帯内に追加される明示的な四つ組

Mellinの部分積分で \(M_{Af}(s)=(1/2-s)M_f(s)\) だから

\[
\boxed{\widetilde\xi(s)=\frac{P(s-1/2)}c\xi(s),\qquad
P(w)=1+aw^2+bw^4
=\frac{256}{N}[(w-1/4)^2+32^2][(w+1/4)^2+32^2].} \tag{7}
\]

追加零点は厳密に

\[
\boxed{s=1/4\pm32i,\qquad s=3/4\pm32i.} \tag{8}
\]

これらは臨界帯の中にあり、標準のξの既知の帯内限定と合わせ、変形後も全零点は帯内にある。
\(P(\pm1/2)=c\) なので \(\widetilde\xi(0)=\xi(0)\)、
\(\widetilde\xi(1)=\xi(1)\)。完成関数は実対称・関数等式・位数1を保つ。
臨界線座標 \(s=1/2+iz\) では乗数は
\(1-az^2+bz^4=b[(z-32)^2+1/16][(z+32)^2+1/16]\)、実 \(z\) で厳密に正。
したがって、臨界線上の元の零点と符号もすべて保持される。

標準の \(\xi(1/4+32i)\ne0\) は別途Arb192bitで認証した。他の三点は関数等式と共役から従う。
この点の零点は変形で追加されたものであり、元のξの零点を報告したのではない。
正の完成kernelからPSDへの推論も直接検査できる。\(F(z)=\widetilde\xi(1/2+iz)\) とし

\[
D_F(w,z)=\frac{F(z)F'(\bar w)-F'(z)F(\bar w)}{4(z-\bar w)}
\]

を使う。\(z_0=32+i/4\) は単純零点なので \(D_F(z_0,z_0)=0\)、一方
\(D_F(0,z_0)=-F'(z_0)F(0)/(4z_0)\ne0\)。
二点Gram行列の行列式は \(-|D_F(0,z_0)|^2<0\)。
その符号も独立に区間評価した。標準のWeil形式への負方向ではない。

**変更されたのは所定のMellin／Gamma因子である。**
算術級数のEuler coreはζのままだが、完成因子は
\(P(s-1/2)\pi^{-s/2}\Gamma(s/2)/c\) になり、零点を持つ。
自己Fourier性・正のseed・正のcompleted kernel・滑らかなmodular反射・帯内限定・
端点規格化だけでは、この変更を排除できない。標準の零点を持たないGamma因子まで
保った反例とは主張しない。

<a id="5-正の増分があっても零点を除去しない例"></a>

## 5. 正の増分があっても零点を除去しない例

全指数モーメントを持つ実偶kernelのGaussian畳み込みでは
\(F_\tau(z)=e^{-\tau z^2}F(z)\)。直接微分により

\[
D_{F_\tau}(w,z)=e^{-\tau z^2-\tau\bar w^2}
\{D_F(w,z)+(\tau/2)F(z)F(\bar w)\}. \tag{9}
\]

ここには真の正なrank-one増分がある。しかし (8) の単純零点では同じ二点Gramの
負行列式が全ての有限 \(\tau\) で残る。
\(F_\tau(z/\sqrt\tau)=e^{-z^2}F(z/\sqrt\tau)\to F(0)e^{-z^2}\)
というGaussian極限では、非実零点は \(\sqrt\tau z_0\) へ逃げる。
極限の正値性から逆向きに正値性を伝える候補も採用しない。
Schwartz性だけでは複素Fourier積分の整性は保証されないので、モーメント仮定を省略しない。

## 6. Gaussianのground stateを直和へ移す場合のdomain

標準のGaussianに固有の消滅方程式も、実際の算術項で検査した。

\[
v_n(t)=e^{t/2}e^{-\pi n^2e^{2t}},\qquad
B_n=\partial_t-1/2+2\pi n^2e^{2t},\qquad B_nv_n=0.
\]

各 \(B_n^*B_n\) は非負。滑らかなcutoffによるgraph近似で、\(v_n\) は
閉 \(B_n\) および \(B_n^*B_n\) のdomainに属する。しかし

\[
\|v_n\|_2^2=\frac1{2\sqrt2\,n},\qquad
\|\phi_n\|_2^2=\frac{33}{32\sqrt2\,n},\quad
\phi_n=(D_t^2-1/4)v_n=n^{-1/2}k(t+\log n). \tag{10}
\]

どちらの等係数ベクトルも直和Hilbert空間に入らない。
定数は \(x=ne^t\) または \(x=\pi e^{2t}\) の置換で確認でき、例えば
\(\|k\|_2^2=(2\sqrt\pi)^{-1}\int_0^\infty
x^{-1/2}(4x^2-6x)^2e^{-2x}dx=33/(32\sqrt2)\)。
点ごとの和 \(\sum_n\phi_n=\Phi\) はmodular関係により \(L^2\) 関数になるが、
自然な部分和 \(S_N=\sum_{n\le N}\phi_n\) は \(L^2\) 収束しない。実際

\[
N^{-1/2}S_N(u-\log N)
\longrightarrow -2\pi e^{5u/2}e^{-\pi e^{2u}} \tag{11}
\]

がcompactな \(u\) で一様に成立する。これはRiemann和の極限
\(e^{u/2}\int_0^1(4c^2y^4-6cy^2)e^{-cy^2}dy\)、\(c=\pi e^{2u}\) を
\((-2cy^3e^{-cy^2})'\) で積分したもの。
極限が非零なので \(\|S_N\|_2^2\gtrsim N\)。
有限の各ground-state energyが0という事実を、閉作用素の極限定理だけで
全算術和の正値性へ移すことはできない。これは単純な直交直和の案への障害であり、
ground-state法全般や、別のdomainを持つ厳密構成の不可能性証明ではない。

## 7. 既知性の限定確認と判定

構成・反証の後に、一次資料を限定確認した。
[Bump–Choi–Kurlberg–Vaaler, *A Local Riemann Hypothesis, I*](https://kurlberg.github.io/eprints/lrh1.pdf)
の著者公開preliminary版、§1 pp.2–3、Theorem 1は、個々のHermite関数のMellin多項式の
零点が中心線上にあることを証明する。そこではoscillator Hamiltonianの個別固有関数を使う。
Fourier固有値+1の空間全体に同じ結論を与える定理ではなく、今回の線形結合と矛盾しない。
一般の因子分解 (1) と明示例 (2)〜(8) はここでの初等導出として記録し、
論文の定理そのものや新規な発見としては表示しない。文字どおりの先行例の網羅調査はしていない。

- ROOTが臨界帯内の四点を指定し、正値性の有理下界を構成。
- BUILDER/DESTROYERが係数、Fourier規約、全域下界、規格化を独立検算。
- LITERATURE担当は一般SchwartzのMellin極相殺を独立導出し、構成後に既知定理の範囲を照合。
- (10)〜(11)は ROOT/DESTROYER が定数・domain・収束様式を独立確認。
- [再現スクリプト](../../../artifacts/experiments/scripts/selfdual_kernel_checks.py)と
  [結果](../../../artifacts/experiments/results/selfdual-kernel-checks.json)に有理恒等式とArb評価を保存。

**一般の正な自己双対test functionからの零点強制、およびGaussian極限からの逆伝播は終了。**
次に必要なのは、標準Gaussianの固有の方程式／Mellin因子を整数和へ通した際の、
独立した全域正値性入力である。Gaussianの消滅作用素を使う案も直接検査したが、
単純な直和ではdomainと極限が破綻する。実際の算術的相殺を保持して正エネルギーを
Gram表現へ移す橋は未取得。今回の仮説を条件の改名や数値拡大で継続しない。
主証明グラフ合流0、RHは未証明。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/selfdual-kernel-checks.json`](../../../artifacts/experiments/results/selfdual-kernel-checks.json)
- [`experiments/scripts/selfdual_kernel_checks.py`](../../../artifacts/experiments/scripts/selfdual_kernel_checks.py)
