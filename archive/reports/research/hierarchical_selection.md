**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/hierarchical_selection.md` · Original SHA-256: `d707a1fb03b61273e71161c148186cf1c7a992846d9919b987e97a30e5182beb`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Hierarchical selection / resolution scale / prime-rank-one flow

2026-09-30。**RH OPEN。既存研究・state・proof graphは不変更。自動mergeなし。**

## 今回の結論

**HIERARCHICAL SELECTION IDENTIFIED:** 固定した任意の有限微分候補空間で、
支持境界の階層的分裂は最小方向をkへ選ぶ。さらに、十分高いFourier解像度では、
既存のsupport＋periodic Fourier射影を含むactual Weil形式でも同じrestricted方向選択が残る。

対象は
\[
 \mathcal R_m=\operatorname{span}\{k,k'',\ldots,k^{(2m)}\},\quad m<\infty\text{ fixed}.
\]
**全有限Fourier空間のgroundをkと同定した結果ではない。**
ここにG*への未解決の接続が残り、RHの証明にはならない。
新規性の学術的主張はしない。

三つの主要方向を検査した。

* Track A/A2：階層と高解像度のrestricted selectionを解析的に導いた。
* Track B：prime eventの一次rank-one則は正確だが、有限幅の素数追加項は符号不定。
  actual repeated rank-one flowへの同一視は反証された。
* Track C：SonineとSuzukiの既存chainの正確な関係はあるが、現在の二cutoffを
  energyと選択を保って置換する写像・評価は得られなかった。

## 1. 二候補から固定有限m全体へ

\(a=\log\lambda,\ Y=\pi e^{2a},\ \beta=2Y\) とする。
global radicalという入力をそのまま使い、全prime・Gamma・pole項を保持した。

高階方向を逆順にSchur消去する際、個々の元の行列要素の誤差評価では不足する。
そこで第1theta項の多項式を、境界Yにおけるexact Taylor jetへ変換した。
これは同じ有限候補空間の座標変換であり、新しいmetricや空間ではない。
その座標zで
\[
 Q_W(R_af)=2a\kappa_Y z^*H_Yz,
 \quad H_Y\to H>0,
 \quad H_{rs}=\frac{(r+s)!}{2^{r+s+1}},
 \quad\kappa_Y=\pi^{-1/2}Y^{-1/2}e^{-2Y}.
\tag{1}
\]
prime/pole誤差もz全体に一様なので、高次相殺後に誤差が主項へ昇格する問題を避けられる。

Gramも同時に運んだ最小固有方向と最小値は
\[
 u_{a,m}\to k/\|k\|_2,
 \qquad
 \mu_{a,m}\sim
 \frac{a(m!)^2}{\sqrt\pi\|k\|_2^2}
 Y^{7/2-2m}e^{-2Y}.
\tag{2}
\]
大きいaで最小固有値は単純。
特にm=2の係数は \(4Y^{-1/2}\)、m=3は \(36Y^{-5/2}\)
（共通因子 \(ae^{-2Y}/(\sqrt\pi\|k\|_2^2)\) を除く）。

exact Schur pivotsは
\[
 d_j\sim a\kappa_Y16^j((m-j)!)^2Y^{6j+4-2m}.
\tag{3}
\]
従って隣接階層の尺度比はY^6。
最初に指数的共通尺度を除き、\(\varepsilon=Y^{-6}\)で順次再尺度化すると、
最高階から一つずつ縮退が解ける。liminf・recovery sequence・compactnessも明示した。
Anzellotti–Baldoの名称だけを当てはめたものではなく、有限次元で直接証明できる階層である。

[主定理・Γ辞書](higher_order_gamma_selection.md)、
[完全なjet・Schur証明](hierarchical_selection/notes/support_hierarchy.md)。

## 2. Fourier解像度の仮説：何が正しく、何が未確定か

境界座標 \(v=2Y(t-a)\) でtailは \(e^{-v}\)。
\(v=Y(t-a)\) なら \(e^{-2v}\) となる。
\[
 \Omega_N=\pi N/a,\qquad h_N=\Omega_N/(2Y),
 \qquad c_N=N/(aY),\quad h_N=\pi c_N/2.
\]
したがって幾何学的に境界を見る尺度は確かに **NがaYのオーダー**。
以前の \(N\asymp a^2,a^3\) は境界座標では低解像度に属する。

しかしP_Nはperiodic projectorであり、単純な全実線Fourier cutoffではない。
\(G_af=\sum_\ell f(t+2a\ell)\)、区間内で \(H_af=G_af-f\) とすると、
\[
 (P_NR_af-f)|_{[-a,a]}=(I-P_N)H_af-(I-P_N)G_af.
\tag{4}
\]
第1項は両端から折り返された境界tail、第2項は真のFourier/Gamma tail。
このexact分解が、新しい解像度解析の出発点である。

## 3. Full系のeffective boundary form

jet profile \(F(v)=e^{-v}\sum_{r=0}^mz_rv^r\) を偶延長してEFと書く。
H_hをscaled周波数のhigh-passとすると、実際の周期射影の極限から
\[
 J_h(F)=\|F\|_{L^2(0,\infty)}^2
       +\tfrac12\|H_hEF\|_{L^2(\mathbb R)}^2,
 \qquad \|F\|^2\le J_h(F)\le2\|F\|^2
\tag{5}
\]
を得る。第1項は窓外のtail、第2項はFourier切断によって内側へ残る誤差である。
両方を含めたactual Weil形式について、
\[
 \frac{Q_W(P_NR_a e_{z,Y})}{2a\kappa_Y}\to J_h(F)
\tag{6}
\]
がjet unit ball全体に一様に成立する。ここでh_N→h>2/π、またはh_N→∞。
prime/pole項は同じ座標で下位であることを個別評価した。
ambient positivityを仮定していない。

F=e^(-v)だけなら
\[
 J_h(F)=1-\frac{\arctan h+h/(1+h^2)}\pi.
\tag{7}
\]
支持だけの値は1/2なので、有限hでは残差の係数が変わる。
h→∞では元の支持境界形式が復元される。

## 4. 指定されたfull restricted系での選択

任意の固定有限mについて、
\[
 \boxed{\liminf\frac{N}{aY}>\frac4{\pi^2}}
\tag{8}
\]
を満たす全経路で、P_NR_a R_mに制限した最低固有方向は十分先で単純になり、
元のL²(R)でk/||k||へ収束する。
特に **N/(aY)→∞ならYES**。
正確な極限比が存在しなくても、一様jet coercivityで同じ選択を得る。

4/π²は今回の証明の**十分条件の定数**であり、真の必要十分な臨界定数ではない。
由来はfull Fourier tailのe^(-πΩ/4)とtheta境界のe^(-Y)を厳密な余裕をもって分離する条件。
0<c≤4/π²やc=0の全選択問題は未解決である。

従って、今回支持された説明は「十分な解像度なら階層選択をfull restricted系へ渡せる」。
「それ未満ではkが選ばれない」「無限大の解像度比が必要」とまでは言えない。
むしろ十分大きい有限比cでも同じ物理方向kが選ばれる。

[実際の射影・算術項・joint limitの証明](fourier_resolution_transition.md)。

## 5. 小さいactual systemでの診断

λ=3を固定し、既存のactual Weil matrixのmidpointを用いてrestricted problemsだけを解いた。
係数をk+bk''と書くと、N=4,8ではbは正、N=12,20,40では負になった。
N=40ではb≈−0.000378821。これにより、同じsupportでも解像度で有限選択方向が
実際に変わり得ることを診断できる。

これらは100桁計算とquadrature増加検査をした有限診断であり、interval certificateでも
漸近率のfitでもない。(1)–(8)の証明はこの数値に依存しない。
大きいNの全行列ground対角化を主戦略にはしていない。

## 6. Rank-one flow：共通の境界量はあるが、反復法則は閉じない

prime eventの微分をtrial空間へ引き戻すと、境界評価
\(\overline{f_i(a)}f_j(a)\)という同じcovectorが現れる。
ただしsupport recognitionの主項は正、prime eventの微分は負であり、
背景・尺度も異なる。

さらにevent直後の有限幅では、constant trialへのprime寄与は負、
同じfinite space内のodd sine trialへの寄与は正。
**actual有限追加項そのものはnegative rank-oneではない。**
Aronszajn–Kreinのexact式はfrozen rank-one模型に使えるが、
そのまま素数を順次追加する閉じた流れにはならない。
Nが増えると一次近似にもNδ/h→0という一様性条件が必要となる。

[原典・secular equation・反例](prime_rank_one_flow.md)。

## 7. Sonine chain：何がexactで、何が代替にならないか

Burnolのcosine support-gap空間と、SuzukiのGamma由来unimodular chainには、
標準half-density mapによるexactな辞書がある。
しかし現在の非零compact-support finite vectorはそのSonine空間には入らない。
cosine transformがentireであるため、開区間でzero/constantという条件が
非零compact-support vectorと両立しないからである。

support-only ambient intervalのPaley–Wiener chainという自明な対応もあるが、
N切断・Weil energy・kの選択を運ばない。
各有限chain parameterでのstrict norm<1も、極限ではnorm→1となり、
必要な一様評価を自動で供給しない。
よって一parameter chainの存在を、二cutoffの解決として採用しない。

[Burnol・Suzuki原典の仮定と辞書](sonine_filtration_audit.md)。

## 8. 最終七問

1. **m=2,3でもkへ行くか。** はい。さらに任意の固定有限mで証明した。
2. **higher-order Γ-developmentか。** はい。指数共通尺度を先に除き、Y^(-6)ごとの
   exact Schur階層について、liminf・recovery・compactnessを固定した。
3. **境界を解像するscaleは何か。** β=2Yに対するΩなのでNはaYのオーダー。
   ただし選択の必要十分な臨界定数は同定していない。
4. **N/(aY)→∞ならfull系でも残るか。** 指定の固定有限候補空間に制限したgroundならYES。
   より弱い(8)でも成立する。全Fourier空間のgroundとは区別する。
5. **prime rank-one反復法則はあるか。** frozen模型にはあるがactual有限追加にはない。
   一次event則を全flowへ拡張する仮説は反例で止めた。
6. **Sonine chainで二parameterを置換できるか。** 選択とenergyを保つ置換は未取得。
7. **G*に必要なactual ground→k比較は進んだか。** restricted側の候補方向と十分な解像度条件は
   厳密化したが、actual全groundとその候補の距離/gap比較は得ていない。G*は未証明。

## 9. 成果の範囲と停止

user ladderでは、固定mのsupport hierarchyがLevel 2、critical高解像度のeffective formが
Level 3、(8)下のfull **restricted** selectorがLevel 4の限定達成。
Level 5、ES、全groundのreal-zero approximationへの接続、G*、RHは未達。
固定mの定数をm→∞で一様とみなさず、未解決のactual full groundをrestricted最小状態で
置き換えない。

独立destroyerによるdomain・scaling・相殺方向・射影・prime/pole・Γ回復列の監査を行った。
数値結果とは別の解析的証明として保存する。三系統の限定監査で終了し、第四候補は作らない。

**HIERARCHICAL SELECTION IDENTIFIED: 固定有限radical候補群では境界のSchur階層がkを選び、
十分高いFourier解像度でもそのrestricted選択が保存される。**


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/fourier_resolution_transition.md`](fourier_resolution_transition.md)
- [`research/hierarchical_selection/notes/support_hierarchy.md`](hierarchical_selection/notes/support_hierarchy.md)
- [`research/higher_order_gamma_selection.md`](higher_order_gamma_selection.md)
- [`research/prime_rank_one_flow.md`](prime_rank_one_flow.md)
- [`research/sonine_filtration_audit.md`](sonine_filtration_audit.md)
