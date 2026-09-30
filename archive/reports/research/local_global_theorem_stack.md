**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_global_theorem_stack.md` · Original SHA-256: `20ecc6491f31f4ce26bab5f4d988dca557aa00891558ecddac8d93f767bf5d21`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# LOCAL → SEMILOCAL → GLOBAL: theorem stack

2026-09-30。**RH OPEN。達成は限定監査 Level 1。**
KNOWN は原典の前件を含む既知定理、PROVED はこの監査中の初等的な推論、
OPEN は未証明、NUMERICAL は有限計算のみ、FALSE は指定された推論への反例あり。
新しい数学的結果の優先権を主張しない。

## 1. 対象を同じものと扱わない

|段階|対象|zero / spectrum|正性・内積|変換・gluing|極限と状態|
|---|---|---|---|---|---|
|real local|各 Hermite 関数の local Mellin transform|Gammaを除いた多項式の零点|Mellin-Plancherelからの正直交測度|特定の oscillator eigenfunction → Mellin|各有限次数の定理 KNOWN|
|nonarchimedean local|Weil representation の特定 vector、または非退化 quadratic character|有限 Laurent/polynomial correction の零点|局所 Fourier/Weil 構造。全てを real oscillator と同一視しない|局所functional equation、unit-circle argument|原典ごとの residue characteristic 条件付き KNOWN|
|Sauvalle adelic|global weak Mellin transform|completed global L factor と有限local corrections|local theoremのpositive measureをそのままglobalへ運んでいない|Tate型積分から \(L(s,\chi)\prod C_v\)|global confinement は Q の例で RH 同値|
|CCM Sonin|有限 \(S\) の \(\mathbf S_\lambda(X_S)\)|同じcompleted Mellin functionを別のnormで実現|bounded isomorphism、一般に等長でない| \(\upsilon_S\theta_S=\upsilon_\infty\)|空間・指定関数の同一性 KNOWN、全零点拘束とは別|
|finite Fourier cutoff|Weil 行列 \(Q_{\lambda,N}\) のground vector \(v_{\lambda,N}\)| \(\widehat v_{\lambda,N}\) の全零点、有限商＋Dirac tail| \(Q_{\lambda,N}-\epsilon I\) の商内積|rank-one perturbed \(D_{\lambda,N}\)|ESを満たす段階で実零点 KNOWN|
|prolate proxy| \(k_\lambda=1_{I_\lambda}\mathcal E h_\lambda\)|Fourier transform の零点一般|prolate固有関数は別operator|prolate→Hermite estimate、Poisson sum|規格化変換→actual \(\mathscr X\) KNOWN、proxy実零点 OPEN|
|target| \(\mathscr X(z)=\xi(1/2+iz)\)|全非自明ζ零点を重複度付きで保持|必要なglobal正性は未証明|上記ground transformとの同定|OPEN|

local Hermite の証明と finite Weil の証明は別々の入力である。
**Theorem L のlocal因子を掛ければ Theorem F のground transformになる、
というexact mapは構成されていない。** 三段階を一本道と描かない。

## 2. L / F / C / I の状態

|ID|数学命題|状態|前件・限定|
|---|---|---|---|
|L-real|Hermite Mellin のpolynomial zerosは \(\Re s=1/2\)|KNOWN|各指定固有関数。任意線形結合は不可|
|L-padic|局所Weil/quadratic-characterのlocal RH|KNOWN|Kurlberg II と Sauvalle で範囲を分離|
|S-Sonin|finite-place additionが Sonin spaceをbounded同型にする|KNOWN|norm・ground state・Weil positivityは同じではない|
|F-conditional|ESな \(Q_{\lambda,N}\) から \(\widehat v\) は全実零点|KNOWN|CCM Theorem 5.10。ES=単純かつ偶な最小固有vector|
|F-universal|全cutoff、または必要なcofinal列でESが成立|OPEN|数値とprolate側の類似だけでは不足|
|C-fixed-window|固定operatorの孤立単純groundをcoreから近似しFourier変換をcompact一様近似|KNOWN, CONDITIONAL|CvS Theorem 6.1 の全domain前件を要する|
|C-proxy|prolate \(k_\lambda\) の変換がstripで一様収束|KNOWN|CCM Lemmas 7.2–7.3。定数規格化とGaussian tailを明示|
|C-actual|ESを満たす適切なcofinal経路上で、規格化 \(\widehat v_{\lambda,N}\) のnormal family評価が得られる|OPEN|少なくとも \(N/\log\lambda\to\infty\) が必要。全パラメータ族のnormalityは \(N=0\) 反例によりFALSE|
|I-proxy|規格化proxyの極限は \(\mathscr X\)|KNOWN|Poisson/Gamma/Euler算術を実際に使用|
|I-actual|規格化ground変換の極限もproxyと一致|OPEN|下記 G* の正確な比較評価が不足|
|H|Fとactual C+IからRH|PROVED, CONDITIONAL|Hurwitz/Rouché。新しいRH入力ではない|

「Fは無条件に全て済み、C+Iだけ」との判定は原典の前件を落としている。
「normal family bound found」も、proxyとactual groundで異なる値にする必要がある。

## 3. Hurwitz の最小対象

\[
 \Omega=\{|\Im z|<1/2\},\qquad z_*=i/4,\qquad
 F_{\lambda,N}(z)=
 \mathscr X(z_*)e^{i(z-z_*)\log\lambda}
 \frac{\det_{\rm reg}(D_{\lambda,N}-z)}
      {\det_{\rm reg}(D_{\lambda,N}-z_*)}.
\tag{1}
\]
ES が成立する各段階で denominator は非零、F は整、全零点実数。
規格化点はRHによらず \(\mathscr X(z_*)=\xi(1/4)>0\)。

**十分条件 H.** ESを満たす列について
\[
 \lambda_j\to\infty,\quad
 \sup_{z\in K}|F_{\lambda_j,N_j}(z)-\mathscr X(z)|\to0
       \quad\text{for every compact }K\Subset\Omega.
\tag{2}
\]
ならRH。

**証明。** 非実零点 \(z_0\in\Omega\) があると仮定する。
小円板の閉包を \(\Omega\setminus\mathbb R\) 内に取り、
境界上に \(\mathscr X\) の零点がなく内部に \(z_0\) があるようにする。
孤立零点なのでこの選択にRHは不要。境界上の
\(\min|\mathscr X|>0\) と (2) から Rouché が適用できる。
Fも内部に同じ正の零点数を持つことになるが、Fの零点は実数のみ。矛盾。
\(\mathscr X\not\equiv0\) は規格化でも保証される。
非自明ζ零点は \(0<\Re s<1\) にあるから、全て \(\Omega\) 内で扱える。□

多重零点もRouchéの重複度付き個数に含まれる。
これは \(\mathscr X\) の全零点が実数という結論であり、
global自己共役作用素の構成を追加で要求しない。
全複素平面の収束、単一のgrowing-height rateは十分だが必要以上に強い。

## 4. 実際の missing proposition G*

規格化proxy
\[
 G_\lambda(z)=\mathscr X(z_*)\widehat k_\lambda(z)/
                                      \widehat k_\lambda(z_*)
\]
について \(G_\lambda\to\mathscr X\) は既知。
従って残りを次の一つの**複合命題**へ書ける：
\[
 \boxed{
 \begin{gathered}
 \exists(\lambda_j,N_j)\ \text{with ES},\quad \lambda_j\to\infty,\\
 \forall K\Subset\Omega:\quad
 \sup_K\left|
 \frac{\widehat v_{\lambda_j,N_j}}{\widehat v_{\lambda_j,N_j}(z_*)}
 -
 \frac{\widehat k_{\lambda_j}}{\widehat k_{\lambda_j}(z_*)}
 \right|\to0.
 \end{gathered}}
\tag{G*}
\]
「一個」と記述しても ES の証明と比較estimateの二義務を消さない。
原著 §8 と対応する。これを仮定してproof graphに入れてはいない。
RHからこの特定のprolate/Weil比較への逆含意は未証明。

## 5. さらに弱い十分条件

|形式|必要な正確な条件|不足するもの|
|---|---|---|
|Rouché only|任意の非実候補零点を囲む上記円板の境界で、ある十分大きいadmissible段階に \(|F-\mathscr X|<|\mathscr X|\)|実軸での値一致、数個の低零点一致|
|argument principle|同じ各円板の境界で \(\int F'/F\to\int\mathscr X'/\mathscr X\)|零点を無視した弱いtrace分布の一致|
|log derivative|対象円板境界の近傍でlog-derivative収束、各分母非零|ただの導関数のformal式|
|Vitali|actual Fの局所有界性と、\(\Omega\) 内に集積点を持つ集合上のactual \(\mathscr X\) への値収束|対称性、order、F(z*)の一値だけ|
|canonical products|有限compact内の零点・重複度同定に加え一様な高域product tail制御|固有値ごとの収束だけ|

単連結zero-free領域でlog-derivative収束と一点の値規格化を持てば、
積分して関数収束へ戻せる。多重連結領域ではperiod・枝も管理する。
「zero-free領域」は各関数が実際に非零な場所で指定し、
targetの非実零点不存在を先に仮定しない。

## 6. normal family、trace、high spectrum

固定窓supportからは
\[
 |\widehat v(z)|\le\sqrt{2\log\lambda}\,\lambda^r\|v\|_2
 \quad (|\Im z|\le r)
\]
しか直ちに出ない。規格化分母の下界も未供給で、
これはactual Fの窓一様なcompact boundではない。

Fredholm determinantの一般的な連続性は、同じ空間上のtrace-norm収束
\(\|K_j(z)-K(z)\|_1\to0\) がcompact一様なら使える。
regularized determinantでは対応するSchatten normと正則化規約を要する。
このactual familyにその仮定を供給するestimateは確認できない。
本文 (D) の Fourier transform公式を利用する方が、必要条件を直接書ける。

norm-resolvent収束でさえhigh-spectrumの累積を制御しない場合、
determinantに余分な非消失因子が残る。
反例・tail条件は [独立destroyerノート](local_to_global/notes/convergence_destroyer.md)。

また未変更tail \(\pi j/\log\lambda,\ |j|>N\) から
\[
 N_j/\log\lambda_j\to\infty
\]
は (2) の必要条件。全固定compactの同定とtail制御が別義務になる。
有限段階のRiemann–von Mangoldt型leading countの類似も、
個々の零点位置・欠落零点・余分零点・多重度を決定しない。

## 7. gluing と stability-preserver 比較の判定

finite product of real-zero polynomials はreal-zeroだが、
local Mellin correctionsの積が \(F_{\lambda,N}\) になるわけではない。
finite places追加はWeil形式に新しいprime-power項を加え、ground vectorを再計算する操作。
対応する entire functions 上の既知の線形stable-polynomial preserverとの
exact dictionary は得られない。
従って Asano / Lee–Yang / Borcea–Brändén を追加proof inputにはしない。

finite-field側では同じ有限次元Jacobianの算術作用と正polarizationが結ばれる。
ここでは \(k_\lambda\) の算術的極限同定と \(v_{\lambda,N}\) の実零点性が
**別のvector family** に載る。この違いを(G*)で測る。
「missing cohomology」と再命名して済ませない。

## 8. 判定

Level 1：厳密な条件付きstack、二つの族、正規化、strip位相、未変更tailの必要条件を固定。
Level 2 の新しいactual ground-state比較・一様gap・normal-family boundは0。
既知のprolate estimateが今回の新規外部入力であり、
監査者自身がそのestimateを新しく証明したという主張ではない。
三方向の限定監査を完了し、自動的な第四候補へは進まない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/local_to_global/notes/convergence_destroyer.md`](local_to_global/notes/convergence_destroyer.md)
