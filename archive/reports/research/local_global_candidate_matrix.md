**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_global_candidate_matrix.md` · Original SHA-256: `b8cfc07a522237455a99e4b943cc9871b3494002fab95fcc78ec46afde908248`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Local-to-global candidate matrix

2026-09-30。RH OPEN。3方向のみ。旧track・state・proof graphは読取専用。

|Track|actual input|厳密に成立するところ|接着の不足を表す式|反証・誤用gate|決定|
|---|---|---|---|---|---|
|A Local RH→adèle|Hermite、Weil representation、quadratic character、Tate積分|特別なlocal Mellin correctionの臨界線零点| \(\Xi_f=e^{-\pi is/4}C_2(s)\,2\xi(s)/(s(s-1))\)|off-lineで \(\operatorname{ord}\Xi_f=\operatorname{ord}\xi\)。局所結果が新たにglobal零点を消すことはない|local定理 KEEP、local積からRHというroute REJECT|
|B finite-prime→Ξ|actual \(Q_{\lambda,N}\)、prime powers \(p^k\le\lambda^2\)、Gamma、極項|ES条件下の実零点とexact determinant。別途prolate proxyのstrip一様収束| \(\widehat v/\widehat v(z_*)-\widehat k_\lambda/\widehat k_\lambda(z_*)\to0\) compact in \(|\Im z|<1/2\)|ES未証明、別族混同、ground gap≠prolate leakage、finite-tail必要条件|最小gapとして記録。比較estimateは未達、限定監査を完了|
|C zero-preserving limit|Bの既存entire関数、Hurwitz/Rouché|非零compact一様極限ならreal-zero性が保存| \(\sup_K|F_{\lambda,N}-\mathscr X|\to0\)|pointwise、normalization、operator topology、high tail|条件付きlemma KEEP。追加算術estimateではなく、独立proof routeに昇格しない|

## 1. 文献の新しい入力と、その射程

|入力|今回以前との違い|actual gapに届くか|
|---|---|---|
|CCM Theorem 5.10|旧 accumulation_spectrum.md §4 で使用済み。今回はphase・非実点規格化・無限tailまで再固定|実零点族を指定できる。ただしESを要する。定理自体を今回の未使用入力とは数えない|
|CCM Lemma 7.2|固定prolate次数0,4の \(O(\lambda^{-2})\) sup estimate|算術sumに渡す前の関数が近いことを示す|
|CCM Lemma 7.3|proxyの変換→Ξ をcritical strip内で一様に制御|target identificationを一方の族で解く。true groundとの比較は解かない|
|CvS Theorem 6.1|定理の前件は旧記録で使用済み。今回は固定窓の近似誤差式と変動窓での損失を分離|変動窓で必要なgap/誤差/規格化の一様性は供給しない|
|CCM Sonin Theorem 4.6|place additionのbounded isomorphismをexactに記述|groundを運ぶ等長mapではない。completed Mellinでは同じ関数を保存するだけ|
|2026追加数値論文|cutoff、精度、有限次数の診断が増える|新しい無条件global upper boundにはならない|

**new_external_input_found=true** は上の具体的な既知estimateをこの監査へ取り込めた意味。
具体的には旧記録に式としてなかった Lemmas 7.2–7.3 のproxy estimateを指す。
Theorem 5.10、CvS Theorem 6.1、§8の二つのmissing steps自体は
[旧 accumulation_spectrum.md §4](notes/accumulation_spectrum.md)に既出である。
**new_global_arithmetic_bridge_proved=false**。両者を同一視しない。

## 2. 同じに見えるが異なる量

|混同しやすい二つ|差|
|---|---|
|local Euler factor / global ζ|前者はしばしば零点なし。Euler積の絶対収束域は \(\Re s>1\)、臨界帯へ積として渡せない|
|local positive measure / global Weil metric|前者は特別な局所多項式族を直交させる。後者の同定は別義務|
|Sonin function stability / ground-state stability|同じentire functionを別normで表しても最小化問題は変わる|
|\(S\)を増やす / \(N\)を増やす / \(\lambda\)を増やす|places、Galerkin次数、support窓。相互交換可能ではない|
|finite \(Q-\epsilon I\ge0\) / \(Q\ge0\)|最小固有値を引いた正性は自動、元のWeil正性は別|
|prolate concentration \(1-\chi_n\) / Weil ground gap \(e_1-e_0\)|異なる作用素の異なる固有値差|
|prolate \(k_\lambda\) / Weil \(v_{\lambda,N}\)|前者はΞへの収束既知、後者はES下で実零点既知。両性質を同一対象に集める橋が未証明|
|real spectrum / 全ζ零点との完全対応|実数という性質だけでは、線外零点の取り落としを排除しない|
|norm resolvent / determinant limit|高域累積のtrace/Schatten制御が追加で必要|
|有限点での零点一致 / compact一様関数収束|normal familyとlimit identificationが別に必要|

## 3. 過去failed routesとの比較

|旧route|今回再使用するnegative knowledge|今回の具体的差分|
|---|---|---|
|Phase I finite windows|窓を増やすだけではWeil positivityを伝播できない|窓positive certificateを拡大せず、指定ground transform同士の比較に限定|
|Phase II generator|自己共役性と全零点同定は別|determinant formulaが有限段階でexact。なおglobal同定は未証明|
|Phase III/IV arithmetic quotient|ambient \(L^2\) 正性はactual zero-bearing商へ忠実に降りない|今回の有限商 \(E_N/\mathbb Cv\) は別物。旧collapseを回避したと主張しない|
|selfdual theta / restoring force|Hermite線形結合、positive kernel、自己双対性だけではRHにならない|local RHは特定固有関数の定理。prolate proxyの全実零点性を勝手に付加しない|
|One-Prime / scale flow|unitary local return とglobal charactersを同一視しない|有限実零点族と算術proxyを別列として維持|
|Global remainder|全解析germの同定と対称性だけは違う|明示的な値規格化とcomplex compact収束で同定条件を固定|

## 4. strategy review

1. A はlocal/global対象の混同を解消したが、Sauvalleのglobal confinementは既存RH同値条件。
2. B では旧探索で未使用だった **proxy convergence の具体的estimate** を得た。
   ただし、真のWeil ground stateについてそれを利用する比較定理を構築できていない。
3. C はBの残りを安全に記述する論理であり、第四の算術候補を提供しない。

結果：指定された切断点監査は完了。成功Level 1、RH OPEN。
今回の結果だけでG*を証明可能と判定しない。
追加の同型候補、未証明positivity、数値の拡大だけによる延長を行わない。
再開に値する新入力は actual Weil ground に対するES・残差/gap・
正規化したweighted比較のいずれかを独立に制御する定理に限る。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/notes/accumulation_spectrum.md`](notes/accumulation_spectrum.md)
