**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/support-propagation-flow-renormalization.md` · Original SHA-256: `a13bdf7c29259411a0cd7b8199ea8b74a0c237d24da0e513e45919b4f5572801`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Support flow と自然なtail補正 — 正確な恒等式と伝播の不足

2026-09-29。root。**全Lへの正値性伝播は未証明。以下の既知型の恒等式を新しいRH入力と扱わない。**
固定窓の数値拡大はユーザー指定により停止した。本稿はその代替となる構造を検査する。

## 1. 比較空間を指定した実際のWeil形状微分

`H_L=L²[-L,L]` を単に微分することはできない。固定 `g∈C_c∞(-1,1)` に対し

\[
 f_L(x)=L^{-1/2}g(x/L),\quad G(u)=\int g(x)e^{iux}dx,
 \quad C_g(v)=\int g(x+v)\overline{g(x)}dx
\]

というunitaryな座標移送を指定する。零延長を用い、内積は第一変数に線形。
`h(t)=Re psi(1/4+it/2)−log pi` とする。明示公式の各項を変数変換すると

\[
 q_L[g]:=Q_W(f_L)
 =\frac1{2\pi}\int_{\mathbb R}h(u/L)|G(u)|^2du
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                  \Re C_g(\log n/L)+V_L[g],                  \tag{1}
\]
\[
 V_L[g]=2L\int_{-1}^1\int_{-1}^1
       \cosh\bigl(L(x-y)/2\bigr)g(x)\overline{g(y)}dxdy.
                                                               \tag{2}
\]

素数冪和は各compactなL区間で有限和である。C_gはsmoothでsupport端で全導関数が0なので、
`log n=2L`で新項を加える境界項は生じない。この主張は固定smooth gについてのものであり、
端点で跳ぶbasisや最小化固有関数に無条件で同じ微分式を適用しない。

`h'(t)`は実軸でsmooth、`t h'(t)`は有界である。原点では部分分数展開、遠方ではdigamma漸近
または既存のh'上界から従う。GのSchwartz減衰により微分を積分内へ入れられ、

\[
\begin{aligned}
 \frac d{dL}q_L[g]
 ={}&-\frac1{2\pi L^2}\int u h'(u/L)|G(u)|^2du\\
 &+\frac2{L^2}\sum_{n\ge2}\frac{\Lambda(n)\log n}{\sqrt n}
                         \Re C_g'(\log n/L)+V_L'[g],           \tag{3}
\end{aligned}
\]
\[
 V_L'[g]=2\iint
 \left[\cosh(Lv/2)+(Lv/2)\sinh(Lv/2)\right]
 g(x)\overline{g(y)}dxdy,\quad v=x-y.                         \tag{4}
\]

`h'(t)>0` for t>0なので(3)のarchimedean部分は負である。相関微分もpole部分も一般に符号が定まらない。
従ってこれは厳密なscalar flowであるが、正増分・保存量・contractiveな移送ではない。
式(3)を全作用素のoperator-norm derivative、最小固有値の微分、またはRiccati closureとは呼ばない。
prime translationはLに依存して移動するので、作用素ノルム微分への昇格には追加のdomain評価が要る。

## 2. Schur flow の微分だけでは閉じない

固定した有限Galerkin空間で `M(t)=[[A(t),B(t)],[B(t)*,C(t)]]` がC¹で、Aが可逆とする。

\[
 S=C-B^*A^{-1}B,
\quad
 S'=C'-B'^*A^{-1}B-B^*A^{-1}B'
                 +B^*A^{-1}A'A^{-1}B.                       \tag{5}
\]

これは積の微分と `(A^{-1})'=-A^{-1}A'A^{-1}` による恒等式。
右辺はSだけの関数ではなく、別々のA,B,Cとその変化を要する。Riccati equationと呼ぶだけではclosed flowを得ていない。
空間を増やす離散Schur消去ではさらに新shellの係数が入力となる。
可逆性を失う点、traceを持たない境界値、変化するform domainには式(5)をそのまま移植しない。

## 3. 許される自然な補正を特定する

### 3.1 省いた素数冪

support[-L,L]のfの相関は[-2L,2L]にある。従って `log n>=2L` の素数冪tailは、
この固定窓の**正確なWeil形式では既に零**である。未知の正の補償項として足せない。
窓を広げると新しい相関が現れるが、符号は正ではない。

具体的にL=1/2,delta=1/10とし、新shell内の中心 `±log(3)/2` に同じ十分狭いL²正規化bumpを置く。
旧窓から新窓までに追加されるprime powerは3だけ。その寄与の2次元行列は

\[
 -\frac{\log3}{\sqrt3}
 \begin{pmatrix}0&1\\1&0\end{pmatrix},                         \tag{6}
\]

で固有値は正負両方。supportとshiftを一致させれば係数は厳密に得られる。
これは新しいprime項だけの反例で、archimedean・poleを合わせたQ_Wの負性を主張しない。
省略prime tailを正補正と呼ぶことはできない。

### 3.2 省いたarchimedean積分

固定support・固定basisについて、T≥7の先のarchimedean tailは自然に

\[
 D_{T_1,T_2}(f)=\frac1{2\pi}\int_{T_1<|t|\le T_2}
                       h(t)|F_f(t)|^2dt\ge0                 \tag{7}
\]

と定まる。tailを足すのは打切り量から元の量を復元する操作であり、元のQ_Wに任意の正項を足す操作ではない。
有限basisでは積分は有限、T₂=∞へのtailも収束する。
全L²に同じ有界tail作用素があるとは限らず、log form domainを保持する。

[Groskin v3 Theorem3.2](https://arxiv.org/html/2607.02828v3) は指定の有限basisで、このtailを
`∫[(s-m)(s-n)]^(-1)dnu(s)` 型のCauchy–Stieltjes行列として表し、
post-band条件の下で自然順序のstrict total positivityを与える。
本repoの [独立監査](groskin-tail.md) ではPD・TP・密度の符号・基底依存を分離した。
変化するパラメータはarchimedean cutoffであり、support Lの拡大ではない。
元論文のsupport log(c)は本稿の半幅Lと同じ記号ではない。

## 4. Archimedean tail がSchur補形式へ与える正の増分

有限次元でA>0とし、正の増分を

\[
 D=\begin{pmatrix}U^*U&U^*V\\V^*U&V^*V\end{pmatrix}
\]

と因数分解する。M自体はPSDと仮定しない。Woodbury恒等式または平方完成から

\[
 \boxed{\ S(M+D)-S(M)
 =(V-UA^{-1}B)^*(I+UA^{-1}U^*)^{-1}(V-UA^{-1}B)\succeq0.\ }
                                                               \tag{8}
\]

最短の証明は `x=z-A^{-1}By` と置き、
`z*Az+||Uz+(V-UA^{-1}B)y||²` をzについて最小化すること。
固定分割でのarchimedean cutoff増分には(8)を適用できる。
正のtailのGram因子U,Vは積分Hilbert空間値としても、Aが有界可逆かつ関連作用素が有界なら同様に扱える。

**限界:** これはL方向のshell追加ではない。Sがもともと負なら、正増分があっても0に届くとは限らない。
またAの可逆性、tail因子のdomain、極限の一様制御を不要にする恒等式ではない。
total positivityもprime/poleに対する必要量の支配を与えない。

厳密なCauchy–Stieltjes型の例を取る。節点0,1、測度delta₂+delta₃なら

\[
 D=\begin{pmatrix}13/36&2/3\\2/3&5/4\end{pmatrix},
 \quad\det D=1/144>0.
\]

全minorが正だが、`M=[[1,2],[2,1]]` に足した行列は
`det(M+D)=−583/144<0`。従ってTP tailというクラスの情報だけから、
全行列またはSchur補形式の正値性は出ない。実際のWeil行列をこのMと同一視しない。

## 5. 補正後から元のQへ戻る条件

`tilde Q_L=Q_L+C_L` を導入するなら、これがどの正確な打切り量を補正するのか明示する。
例えば全Lのtilde Q_L≥0を示しても、固定compact-support fについてC_L(f)が0へ戻らなければ
元のQ_W(f)≥0は従わない。許される十分条件の一つは

\[
 \forall f\in C_c^\infty,\quad
 C_L(f)\longrightarrow0,\qquad
 \widetilde Q_L(f)\ge0\quad(L\text{ sufficiently large}),       \tag{9}
\]

で、このとき極限はQ_W(f)≥0となる。(9)の正値性を未証明に仮定すれば核心は残る。
`C_L(f)≤0` が独立に分かる場合も帰結には使えるが、正の補正で負方向を隠す場合は使えない。
大きなL²対角shiftや、既知の零点配置を使って作る補正をここでは導入しない。

## 6. 判定

実際のWeil形式の固定coordinate微分、Schur微分、自然なarchimedean tailの正増分(8)は成立する。
しかし全Lを覆うS≥0、保存量、contractiveなsupport移送、零固有値を避けるglobal flowは得られていない。
archimedean cutoffに関する既知の正増分をsupportの伝播へ読み替える候補は棄却する。
`P(L)=S_(L,delta)≥0` をそのまま局所条件とする候補も拡大窓の正値性の言い換えとして棄却。
固定窓の数値拡大へ戻って、この不足を進捗として埋め合わせることはしない。

## 7. 反証実験と符号の再現

`experiments/scripts/support_propagation_checks.py`、保存先
`experiments/results/support-propagation-checks.json`。
Fractionによる厳密有理演算と224bit Arbを区別して使った。

- 同じ対角1・隣接coupling−3/4を持つToeplitz制限では、LDL pivotが
  `1,7/16,−2/7`。最初の二つの正値制限から三つ目の正値性は従わない。
- 上記Cauchy–Stieltjes tailのdet、全minor、Sの改善と改善後の負性を有理数で再計算した。
- (8)のscalar版を異なる二組の有理係数で両辺照合した。一般証明は§4の平方完成であり、二例だけで一般恒等式を検証したとは扱わない。
- `A→0`でも`B=√A/2,C=1`ならS=3/4。一方、Bを√Aより少し大きくすればS<0。
  逆作用素の発散だけで必ず失敗とも、bounded Bだけで安全とも言えない。

さらに [独立監査の付録](support-propagation-adversarial.md) の対数型countermodel

\[
 q_L(f)=\int\log(1+t^2)|\mathcal Ff(t)|^2dt-\|f\|^2
\]

で、**同じ初期窓に対する全関数の正下界、局所Schur延長、より大きい窓の負方向**を区間認証した。
このqは実際のWeil形式ではない。

support測度mのbathtub下界をb(m)とすると、L=1/2では
`b(1)−1>0.18978378`。delta=10^(-30)ではshell下界と混合norm≤√2πから
`b(2delta)−1−2π²/(b(1)−1)>32.0493` となり、確かに局所延長可能である。
この極小のdeltaは保守的十分条件の一例で、最適な刻み幅ではない。

一方、L=1の正規化box `f=1_[−L,L]/√(2L)` では

\[
 q_L(f)=\frac{1-e^{-2L}}L+2E_1(2L)-1,
 \qquad E_1(x)=\int_x^\infty e^{-u}\,du/u,
\]

となり、L=1で `q_1(f)<−0.03753426` を認証した。
この式は `log(1+t²)=2∫e^(−r)(1−cos tr)dr/r` と
boxの相関 `(1−r/(2L))_+` を代入して直接得る。
boxは対数form-domainに属するので、滑らかな関数に限定した話との不整合はない。
必要ならform-norm近似で同じ負符号のC_c∞関数が存在する。

したがって全L伝播の不足は、数値精度不足や単に厳しい誤差定数の問題ではない。
同じlog domain・compact resolvent・exact restrictions・有界mixed block・局所延長を備えたクラスで
一般のbootstrap自体が偽である。実際のWeilに固有の追加情報が必要である。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/support-propagation-checks.json`](../../../../artifacts/experiments/results/support-propagation-checks.json)
- [`experiments/scripts/support_propagation_checks.py`](../../../../artifacts/experiments/scripts/support_propagation_checks.py)
- [`proofs/audits/groskin-tail.md`](groskin-tail.md)
- [`proofs/audits/support-propagation-adversarial.md`](support-propagation-adversarial.md)
