**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/hierarchical_selection_candidate_matrix.md` · Original SHA-256: `11743ad1eafed38a04d4318c3d177224a1be39252db5bed222350977bac93c38`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Hierarchical selection — three-candidate decision matrix

2026-09-30。RH OPEN。Proof graphへのmergeなし。新規性主張なし。

|方向|actual input|検査した命題|結果|残る限界|
|---|---|---|---|---|
|A1 support hierarchy|全theta級数、Weil prime/Gamma/pole、元のL² Gram|fixed mの全方向を一様に扱い、Schur消去でkを選ぶか|PROVED：全fixed finite m、単純最低方向→k、最小値の主定数、Γ階層|m→∞・全groundには一様でない|
|A2 critical/resolved Fourier|既存periodic P_Nとexact periodization、同じjet basis|境界のeffective formとrestricted selectorが保存されるか|PROVED：liminf N/(aY)>4/π²でuniform jet coercivityと方向→k。有限critical h>2/πでJ_h、resolvedで元のH|4/π²は十分条件。小critical比・under-resolvedの全選択は未確定|
|B prime rank-one flow|actual new-prime correlation、event derivative jump|rank-one則を有限幅追加・反復へexactに延長できるか|LIMITED NO-GO：有限幅項はconstant/odd-sineで符号不定。frozen secular式はexact|背景drift・高rank・N依存誤差が閉じない|
|C Sonine/RKHS chain|Burnol cosine-gapとco-Poisson、Suzuki unimodular framework|現在の二cutoffをenergy/selectionを保って一parameterへ置換できるか|NOT IDENTIFIED：Gamma/Sonine exact辞書とPW support辞書はあるが、current finite vectorsの代替ではない|compact supportとSonine gapの不一致、norm gap collapse、未知transfer|

## Γ-theoryを引用するだけでは得られなかったもの

Anzellotti–Baldoはminimizer hierarchyを表現する枠組みを与える。
今回の尺度s_mとY^(-6)、jet matrixの一様正定値性、prime remainderの相対評価は
actual formulasから別に導いた。枠組みの名前をproof inputの代わりにはしない。

## 解像度の三regime

|regime|今回の結論|
|---|---|
|N/(aY)→0|境界周波数ではunder-resolved。以前のa²/a³経路が該当。選択の全挙動は未確定|
|N/(aY)→c、0<c≤4/π²|full Fourier tailを今回のboundでは捨てられない。未解決であり失敗定理ではない|
|N/(aY)→c>4/π²|actual jet form→J_(πc/2)。fixed-m restricted最低方向→k|
|N/(aY)→∞|actual jet formはsupport-onlyのHへ戻る。fixed-m restricted最低方向→k|

有限critical比でJ_hがHと異なっていても、同じ物理方向kを選ぶ。
したがって「無限大解像度比こそ必要」とは結論しない。

## 止めるべき飛躍

* restricted lowest stateを全有限Weil matrixのgroundに置換しない。
* P_N R_mの最小状態に全groundのES・real-zero theoremを自動適用しない。
* 固定mのcoercivity定数を無限radicalに拡張しない。
* 数値で係数の符号が変わる点をsharp transitionの証明にしない。
* prime derivativeのrank-oneとfinite updateを同一視しない。
* Sonine chainの存在を未知のenergy-preserving identificationと同一視しない。

## 成功レベル

固定有限候補空間に限ってLevel 2・3・4を得た。
Level 5（actual full ground comparison + G*）とRHは未達。
三系統の依頼範囲を終了する。第4候補・新しいmetric・確率分布・entropyは導入しない。

**HIERARCHICAL SELECTION IDENTIFIED: support階層と高解像度full restricted系がkを選ぶ。**
