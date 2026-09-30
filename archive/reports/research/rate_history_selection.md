**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/rate_history_selection.md` · Original SHA-256: `e0759654a1878e8369845f7ebc097c7f1687592e9f82da75ba3dc811e064cfe3`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Degeneracy lifting / rate-and-history selection

2026-09-30。**RH OPEN。独立した限定監査。既存375ファイル・state・proof graphを保存。**

## 判定

指定されたsupport＋有限Fourier射影の全系について：
**NO FINITE-SCALE SELECTION PRINCIPLE IDENTIFIED.**

ただし、今回は単なる「速度」という言い換えで終わっていない。
実際の有限Weil行列上でradicalの分裂を計算し、
支持切断についてはその点数差の漸近式まで解析的に得た。
得られた先頭の採点原理は **境界値へのrank-one penalty** である。
さらに **支持切断だけ・二候補 \(k,k''\) に限れば、
restricted最小方向が一意にkへ近づく** ことまで証明できた。
この限定的なrate selectionと、指定されたfull canonical系の選択は区別する。
Fourier射影も含む指定の二parameter系で、pathに依存しない最小branch、
または異なるpath limitは証明できなかった。

有限endpointでgroundが単純なら、ground lineは現在のQだけで決まる。
従って同じ有限endpointへ来た履歴が新しいgroundを選ぶ、という意味のhistoryはない。
経路ごとに違う無限極限が存在するかは、これとは別の未解決命題である。
確率的selectorは追加せず、Track Cは入口で終了した。

## 1. 同点候補を同じ有限問題へ入れた

\[
 f_j=k^{(2j)},\quad0\le j\le m,\quad
 \widehat f_j(z)=(-1)^jz^{2j}\mathscr X(z)/4,\quad m=1,2,3.
\]
ここでkはactual theta/arithmetic kernel。
global radical membershipは前trackの既知結果を再利用する。
有限像は要求通り、sharp restriction、既存Fourier射影、標準L²単位化だけ：
\[
 b_j=\frac{P_N(1_{[-a,a]}f_j)}{\|P_N(1_{[-a,a]}f_j)\|_2},\quad a=\log\lambda.
\]
これらから実際のWeil形式と同じ内積で
\[
 M_{j\ell}=Q_W(b_j,b_\ell),\quad G_{j\ell}=\langle b_j,b_\ell\rangle,
 \qquad Mc=\mu Gc
\]
を作った。列ごとの単位化を線形mapと扱わず、
元のderivative basisへの係数も復元した。

三つのrateを分離した。

|rate|量|それだけでは分からないもの|
|---|---|---|
|A radical recognition|\(Q_W(b,b)\)、または別にその絶対値|full groundとの差・方向|
|B ground excess|\(Q_W(b,b)-e_0\)、方向にはfull gapとの比|複素Fourier変換の一様収束|
|C target|\(\widehat b/\widehat b(z_*)\) と \(\mathscr X/\mathscr X(z_*)\)|A/Bからの自動推論は不可|

## 2. 数値による有限分裂：Step31実行済み

\(\lambda^2=9,25,49,81,121,169\)、
\[
 N_2(a)=\max(4,\lceil a^2\rceil),\qquad
 N_3(a)=\max(4,\lceil a^3\rceil)
\]
を比較した。ともに \(N/a\to\infty\)。
重複を除く11有限endpoint、各 \(m=1,2,3\) の33restricted problems。
Qは448-bit Arb assemblyのmidpoint、固有解析は100桁。
theta積分とprolate比較は解像度を増やして検査した。
**区間認証でも、漸近収束の証明でもない。**

例えば \(\lambda=13,N=17\)：

|trial space|最低score|
|---|---:|
|k単独|\(9.53631\times10^{-12}\)|
|\(\operatorname{span}\{k,k''\}\) の有限像|\(4.99940\times10^{-15}\)|
|\(\operatorname{span}\{k,k'',k^{(4)}\}\) の有限像|\(1.99334\times10^{-18}\)|
|\(\operatorname{span}\{k,k'',k^{(4)},k^{(6)}\}\) の有限像|\(1.41541\times10^{-21}\)|
|全有限Fourier空間のactual ground|\(9.65967\times10^{-59}\)|

有限段階では明確な分裂があり、混合状態はk単独より低いscoreになる。
しかしRitz spanを増やせば最小値が下がることは一般原理でもある。
この表を「一番早い状態はこれ」とする漸近証明にしない。

最後のrestricted最小方向は、先頭係数を1に揃えるとおよそ
\[
 k+0.00612159\,k''+1.25445\,10^{-5}k^{(4)}
       +8.60879\,10^{-9}k^{(6)}.
\]
global kとのoverlap²は0.993463、
actual finite groundとは0.961262、
raw prolate proxyとは0.993194。
ここでfull gapは約 \(1.44\times10^{-55}\) で、
restricted excess/full gapは約 \(9.80\times10^{33}\)。
小scoreからtrue ground proximityを認証するには全く足りない。
この大きな比を距離の下界とも扱わない。

[行列・実装・全数値・conditioning](radical_degeneracy_lifting.md)に保存した。
小さいmの結論を無限radicalへ拡張していない。

## 3. 「消える速度」を解析的に得た範囲

まずFourier射影を外し、支持だけを切る。
\(R_a=1_{[-a,a]}\)、\(Y=\pi e^{2a}=\pi\lambda^2\) とする。
固定 \(j=0,1,2,3\) に対してactual Weil形式で
\[
 \boxed{
 Q_W(R_af_j)\sim
 \frac{a\,16^j}{\sqrt\pi}\,
 Y^{4j+7/2}e^{-2Y}.}
\tag{S}
\]
単位normなら固定定数 \(\|f_j\|_2^{-2}\) を掛ける。
全員が同じsuper-exponential因子 \(e^{-2\pi\lambda^2}\) で消えるが、
微分次数によってpolynomial prefactorが異なる。

これは単なる裾の個数やL²誤差ではない。
sharp tailをweighted BV test-spaceへ入れて明示公式を延長し、
global radicalから \(Q(R_af)=Q((I-R_a)f)\) を使った。
archimedean項が主項を与え、全prime/pole項が下位であることを評価した。
RH・global positivity・global L² closabilityは使用していない。
[証明](rate_history/notes/boundary_rate_analysis.md)、[独立監査](../../audits/proofs/audits/rate_history_selection_adversarial.md)。

ただし(S)の対象は **support-only**。
有限P_Nも含む全systemのleading asymptoticに読み替えない。

## 4. 境界が採点する：二候補に限る選択定理

\(A_j=f_j(a)\) とすると、support-only先頭形式は
\[
 Q_W\!\left(R_a\sum c_jf_j\right)
 \ \text{の先頭行列}\ \simeq
 \frac aY [A_iA_j]_{i,j}.
\]
対応するrescaled matrix limitはrank one。
先頭の「採点項」は \(|\sum c_jf_j(a)|^2\) であり、
\(m\ge1\) では非零の消去方向が残り、\(m\ge2\) では複数の射影方向が残る。

具体的には
\[
 g_a=k-\frac{k(a)}{k''(a)}k'',\qquad g_a(a)=0,
 \quad \frac{k(a)}{k''(a)}\sim\frac1{4Y^2}
\]
について
\[
 g_a\to k\quad\text{in }L^2,\qquad
 \frac{Q_W(R_ag_a)}{Q_W(R_ak)}\sim\frac2{Y^2}.
\tag{C}
\]
したがって「有限段階でk単独が常に最速」は支持切断だけでも成り立たない。
しかしこの勝つ組合せ自体はkへ近づくので、kが極限でないという反証にもならない。
ここから、二候補だけなら次のpositive結果を得る。
raw basis \((k,k'')\) のsupport matrixとGramを \(M_a,G_a\) とし、
\[
 s_a=\frac aY A_1^2>0,\quad
 \frac{M_a}{s_a}\longrightarrow
 \begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad G_a\longrightarrow G_\infty>0.
\tag{S1}
\]
\(A_0/A_1\sim1/(4Y^2)\) なので、先のentrywise漸近から直接従う。
whitened limitはrank one、固有値は0と
\(\nu=(G_\infty^{-1})_{11}>0\)（添字0,1）。
従って十分大きいaでこの **restricted support-only groundは単純**、
\[
 \frac{\Delta_{\rm support,\mathcal R_1}}{s_a}\to\nu,\qquad
 \operatorname{span}v_{\rm support,\mathcal R_1}(a)
 \longrightarrow \operatorname{span}k.
\tag{S2}
\]
物理空間では位相を合わせたunit vectorが \(k/\|k\|_2\) へL²収束する。
最小energyの最初の非零係数や符号を仮定せず、縮退分裂とGramから方向を選べる。

これはユーザー仮説の限定的な数学例である。
ただしP_N込みのjoint limit、\(m\ge2\)、全有限Weil ground、
実零点性、G*へは拡張しない。
最速absolute scoreと最小signed energyも別であり、(S2)は後者の方向選択。
この範囲を越えて次次数を無限に追加しない。

## 5. 支持とFourier切断を混ぜない

\(e=R_af-f,\ d=(P_N-I)R_af\) とおくと
\[
 Q_W(P_NR_af)=Q_W(e,e)+2\Re Q_W(e,d)+Q_W(d,d).
\tag{D}
\]
これがexact defect decompositionである。
signed形式なので混合項を捨てたり、三つのpositive costsだと仮定したりしない。

support内の相関は \(2a\) より遠くで0になる。
従って \(p^k\le\lambda^2\) はこの有限supportに対するexact arithmetic rangeで、
「missing primes」という独立の正誤差をさらに足してはいけない。

固定aでのFourier係数にはboundary derivativeの \(n^{-2}\) 項が現れる。
しかし \(a\to\infty,\ N/a\to\infty\) のjoint limitには、
実軸上の \(\mathscr X(\pi n/a)\) とsupport tailの両方が入る。
固定aの展開をそのまま二parameterの最速選択定理にしていない。

## 6. Fourier射影込みの全認識行列にも上界を得た

固定m、\(a\ge1,\ \Omega=\pi(N+1)/a\ge1\) について、
正規化前の列 \(p_j=P_NR_af_j\) に対し無条件に
\[
 \boxed{
 |Q_W(p_i,p_j)|\le C_m\left[
 a(1+\Omega)^{4m+8}e^{\,a-\pi\Omega/2}
 +\lambda^{8m+24}e^{-2\pi\lambda^2}\right].}
\tag{U}
\]
ここで定数は固定mに依存する。最適率や漸近等号ではない。

証明は実軸上のGamma由来Fourier減衰、theta tail、
periodic projectionのH¹誤差、零延長のjumpを含むweighted BV評価を組み合わせる。
明示公式の全零点和へ移すときに使うのは
\(0<\Re\rho<1\) と既知の \(N(T)=O(T\log T)\) だけで、RHは使用しない。
構成する有限vectorに零点データを入力してもいない。
[証明と独立監査済みのdomain処理](rate_history/notes/full_projection_upper_bound.md)。

二経路では、それぞれsuper-exponentialなtailを除き
\[
 N_2:\quad O_m\!\left(a^{4m+9}
             e^{-(\pi^2/2-1)a}\right),\qquad
 N_3:\quad O_m\!\left(a^{8m+17}
             e^{a-\pi^2a^2/2}\right)
\tag{U2}
\]
という**上界**を得る。
固定mのGramが正定値極限を持つため、unit-normalized matrixと
全restricted Ritz値の絶対値にも、定数を変えて同じ上界が成り立つ。
従って固定候補群が両経路でradicalとして認識されることは無条件に証明できた。

ただし「cubic経路の実際の減衰が必ずこの速さ」「この状態が最速」とは言わない。
両式は経路ごとの粗い上界であり、比の非零極限を与えるものではない。
任意の \(N/a\to\infty\) へも無条件に広げない。
全員の認識が進むことは、誰か一人を選ぶ次次数行列を決めない。

## 7. 履歴を検査した結果

actual \(Q_{\lambda,N}\) は、固定Nでprime-power eventを越えて連続。
\(n=p^k,\ L=2\log\lambda\) では
\[
 [\partial_L Q]_{\log n+}-[\partial_L Q]_{\log n-}
 =-\frac{2\Lambda(n)}{\sqrt n\log n}{\bf1}{\bf1}^*.
\tag{E}
\]
新しいprime項はoverlap長0で入り、行列値のjumpでなく傾きのcornerを作る。
gamma/pole項も含めて確認した。
これはKatoのgap条件下でprojectorを区分的に追える具体的情報であり、
hysteresisではない。

同じ有限endpointでgroundが単純ならRiesz projectorは現在のQだけで決まる。
前のvectorとのoverlap最大というtracking conventionを、groundの定義に代用しない。
gap collapse/crossingでは個々のvectorを選ぶ追加ruleが必要になる。

二経路の有限prefixは、同じλでもNが違うので違う状態を与える。
例えばλ=13のN=7と17のfull-ground overlap²は0.948024、
restricted \(m=3\) のglobal方向同士は0.935637。
これは **異なる有限endpoint** の比較であり、
同じendpointの履歴依存や、異なる無限limitの存在証明ではない。

固定mのGramは、canonical projectionとeven endpoint条件から
\[
 \|P_NR_af_j-f_j\|_2
 \le\|1_{|t|>a}f_j\|_2+\frac{a}{\pi(N+1)}\|f'_j\|_2
\]
により、全 \(N/a\to\infty\) で同じ正定値global Gramへ収束する。
この事実だけでWeil energyのnext-order matrixやground limitは決まらない。
[trajectory・Γ-development・probability監査](ground_state_trajectory.md)。

## 8. 確率の入口gate

Qのprojection-valued spectral measure自体はある。
しかしscalar spectral probabilityには入力vectorが必要で、
normalized counting measureは一つのstateを選ばない。
heat stateにはtemperature/time scaleが必要で、
gapが消えるとそのscheduleが選択を左右する。
それらを算術が指定する追加法則は見つからなかった。
任意のGibbs分布・entropy・新しいmetricは作らず、この候補は終了した。

## 9. RHへ必要な接続は残る

restricted radical spanの最小状態はactual全空間のgroundではない。
従って全groundのES条件付き実零点定理も自動では継承しない。
また任意のglobal radical組合せは
\[
 \widehat f(z)=P(z)\mathscr X(z)/4
\]
であり、同じzero conditionを満たすことと、同じXi関数へ値規格化収束することは違う。

必要なのは、actual next-order formの一意な選択、
full groundとその状態の定量比較、さらにG*へ十分なFourier評価率。
今回これらを新仮定として採用しなかった。

## 10. 最終六問

1. **同点候補は有限では違う点数か。** はい。actual M/Gを構成し、有限診断で分裂を確認。支持切断では解析的にも異なる主係数を得た。
2. **差はどの速さで消えるか。** 支持切断だけなら(S)という漸近等号。全P_N系では(U)–(U2)の無条件上界を得た。leading splitting rateの同定とは区別する。
3. **一番速い状態は一意か。** full系の最速認識方向は未証明。支持切断のみ・二候補に限れば、最低energyのbranchは十分先で単純となることを証明した。
4. **それはk/prolateか。** その限定branchの極限はk。有限では混合状態が低くなる。P_N込みの全finite groundの同定ではない。
5. **cutoff経路を変えても同じか。** 二経路を実測したが、共通limitも異なるlimitも証明していない。
6. **違うなら履歴が選択の一部か。** 異なる無限limitを得た場合にはregularization pathがデータとなる。しかし今回はその前提を証明しておらず、history dependenceとは判定しない。

指定されたfull canonical系の判定：
**NO FINITE-SCALE SELECTION PRINCIPLE IDENTIFIED.**

## 成果の範囲と停止

full canonical finite regularizationの辞書・M/G・33有限分裂問題を固定した点はLevel 1。
支持切断というsubcomponentに限れば、actual Weil defectの異なる主漸近と
rank-one effective boundary formを証明したLevel 2相当の部分成果があり、
さらに二候補 \(\mathcal R_1\) のsupport-only方向選択(S2)も証明した。
さらに全canonical projectionの認識行列に(U)の無条件上界を得た。
限定した二候補での選択をfull-systemのLevel 3やRH進展へ昇格しない。新規性も主張しない。
三系統の限定監査を終え、第4候補や無限次次数探索には進まない。

[候補表](rate_history_candidate_matrix.md)、
[machine state](../../../data/source-records/research/rate_history_state.json)、
保存baseline（原資料参照・公開版未収録: `research/rate_history/preservation_baseline.json`）。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/rate_history_selection_adversarial.md`](../../audits/proofs/audits/rate_history_selection_adversarial.md)
- [`research/ground_state_trajectory.md`](ground_state_trajectory.md)
- [`research/radical_degeneracy_lifting.md`](radical_degeneracy_lifting.md)
- [`research/rate_history/notes/boundary_rate_analysis.md`](rate_history/notes/boundary_rate_analysis.md)
- [`research/rate_history/notes/full_projection_upper_bound.md`](rate_history/notes/full_projection_upper_bound.md)
- [`research/rate_history_candidate_matrix.md`](rate_history_candidate_matrix.md)
- [`research/rate_history_state.json`](../../../data/source-records/research/rate_history_state.json)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `research/rate_history/preservation_baseline.json` — SOURCE REFERENCE NOT INCLUDED
