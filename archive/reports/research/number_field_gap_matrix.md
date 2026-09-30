**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/number_field_gap_matrix.md` · Original SHA-256: `65d55c25db164c8c0bbf10a13c2b42d7cacbf1384f82f89890d8eaa2f516163c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 有限体 → Q：対応の強さと未解決差分

2026-09-29。EXACT=指定範囲で定理、PARTIAL=役割の一部、CONJECTURAL=対応構想はあるが未証明、
ABSENT=今回必要な構成は供給されていない、であり存在不可能の意味ではない。
「有限次元の同一コピーがない」と「算術的実現が全くない」を区別する。

|有限体側|ζ_Q側|状態と残る差分|
|---|---|---|
|curve/variety|Spec Zは実在する算術scheme、Krull次元1|EXACTな算術対象。ただし有限体上のproper curveではなく同じH¹偏極を持つとの結論なし|
|closed points|Spec Zの点p、residue field F_p、norm p|EXACT|
|degree-n closed points|一つのqに対する整数degreeはない|ABSENT。同じ閉点の反復がprime powers p^kに対応するのであって、degree-n点=prime powerではない|
|Frobenius|各pのlocal Frob、idèle norm/scaling action|local FrobはEXACT、単一global q-Frobの代役はPARTIAL|
|Frobenius iterates|各prime orbitのk反復、period log p|prime-power dataはEXACT。一つの整数clockの反復にはできない|
|cohomology Hⁱ|CCM cyclic quotient、Deningerの実在する層構成、未知のpolarized global H¹|前二者は指定範囲でEXACT、有限体の全役割を同時に満たす対象はCONJECTURAL|
|Lefschetz trace|Weil explicit formula、CCM Thm4.16/6.1|test関数で積分したtraceはEXACT。裸のTr(Fⁿ)やHilbert trace classへは昇格しない|
|determinant|既知Hadamard積、local regularized Γ、site countingから完成ζ|各解析式はEXACT。prime-built positive graded spaceのcanonical determinantとの同時同定は未取得|
|Poincaré duality|ξのFE、Mellin反転、算術trace pairing|反転・FEはEXACT、geometric duality/polarization全体はPARTIAL|
|weight|local trivial motiveはweight0。global H¹に欲しいweight1は未証明|局所の既知pure objectとglobal zerosの度数を混同しない|
|polarization/positivity|Weil traceの非負性、Deningerのstar/cup正性|前者はRH同値・OPEN。後者は未構成の幾何を含むCONJECTURALで逆含意は不明|
|Frobenius eigenvalues|finite fieldはα、Qのflowではρまたはexp(tρ)|PARTIAL。parameter mapと多重度を指定して初めて比較可能|
|dimension|Spec ZのKrull次元1、期待されるH⁰,H¹,H²|Krull次元はEXACT、そこから所要のcohomological gradingとweightを導くのは未達|
|archimedean place|Γ_RとHodge/Rees tower|local determinantはEXACT。finite fieldには同型のinfinite placeはない。global H¹との接着は未達|

## Frobenius候補を七つの証明上の役割で監査

|候補|算術起源|反復|trace|spectral recovery|determinant|duality|purity|
|---|---|---|---|---|---|---|---|
|一素点local Frob=1|EXACT|EXACT|localのみ|local weight0のみ|Euler local factor EXACT|local|weight0 EXACT、global RHに届かない|
|CCM idèle/scaling cyclic quotient|EXACT|EXACT|指定核型空間でEXACT|全非自明零点・trace多重度 EXACT|zero divisorは回収。自然なpositive graded detへの昇格は未供給|形式的相似則 EXACT|trace positivityはRH同値|
|Arithmetic Siteの点/対応|EXACT|点作用 EXACT、correspondence合成には例外的接線変形|counting分布 EXACT|その解析式の零点情報|完成ζのlog微分再構成 EXACT|対応候補 PARTIAL|Weil cohomologyと幾何的符号未供給|
|Scaling Hamiltonian半局所系|EXACT|scaling EXACT|cutoff有限部分 EXACT|全zero-positive-spectrum同定ではない|global graded detではない|Fourier/反転 EXACT|全支持正性は未証明、一般不等式には既知失敗|
|Deninger rational Witt suspension|EXACT、定義条件あり|EXACT|prime orbit packetsまで|H⁰は既知、global H¹は未同定|globalはCONJECTURAL|所要構造未供給|所要positive star未供給|
|log translation/renormalization/transferの一般名|座標・解析道具として存在|作用則のみ|算術とのexact traceなしでは不足|未同定|未同定|対称性のみ可|なし。独立candidateとして継続しない|

Arithmetic SiteとCCM cyclic quotientは別の構成である。
前者に適切なWeil cohomologyが未構成という記述を、後者の既存cohomological realizationの否定にしない。
詳細な定理番号とtopologyは `notes/phase3_connes_consani_audit.md`。
Deningerの2024 v4は実在する空間とH⁰を構成している。closed pointsは一軌道ではなくpacket。
2010の全cohomology conjectureが完成したとは扱わない。`notes/phase3_deninger_audit.md`。

## consistency triangle と候補の絞り込み

|構成|Prime → H,F|H,F → 全zeros|独立な正性・weight|判定|
|---|---|---|---|---|
|有限体Jacobian|成立|成立|同じ対象でRosati成立|基準モデル|
|CCM arithmetic quotient|成立|指定traceの意味で成立|Weil同値条件で停止|最も小さく明示できる既知gap。ただし新進展ではない|
|Arithmetic Site単独|成立|counting分布経由で成立|同じ対象のpositive cohomology未供給|複数義務をまとめて「一個の空間」と呼ばない|
|Deninger global program|実在部分あり|H¹ trace/detには未証明部分|偏極・star・flow整合性に未証明部分|全部の存在を採用するなら巨大な未証明仮定|
|M3 prime circles + Γ tower|localは成立|自然Hilbert直和では失敗|local正性のみ|限定接着候補を終了|

初期比較後は **Track B — Missing purity** に絞った。
具体的対象はCCMの既知算術商であり、対象のない新作用素を作らない。
局所的positive構造をこの商へ移せるかをM1–M3で検査したが、独立なpositive comparisonは得られない。

Track Aは既存の複数spaceを無視する危険、Track Cは今回の最も進んだ既知商では既に
trace同定がある、Track Dはlocal Γが構成済みで障害全部がinfinityに集中するとの根拠がない、
という理由で長時間の独立継続を選ばなかった。この選択は他のprogramの数学的否定ではない。

**最小差分の正確な表現:**
「算術から既に構成された、全零点を担う商のtrace pairingに、
幾何的理由による正のpolarizationを与えること」。
その符号命題だけならRH同値である。幾何的polarizationの具体的構成まで含めると、
存在・比較・domain・重複度保持という未証明義務が増え、RHからの逆含意も不明となる。
従ってこの記述を新しい一個の独立lemmaへ圧縮できたというLevel1成功には数えない。

## determinantの採否条件

Hadamard productは既知の解析恒等式。これを使って零点をbasis labelにする新作用素は作らない。
CCMの算術構成はこの禁止例には該当せず、構成が零点入力より先にある。
ただし本監査で確認したものは、全零点・重複度のtrace同定と完成ζの分布的再構成まで。
traceを積分したspectral productを規格化して解析関数を回収することと、
独立なpositive graded geometryのregularized determinantとして同じ関数を得ることを区別する。
後者の定理を未証明のまま完成generatorとして採用しない。

## 出典

[CCM 2007](https://arxiv.org/pdf/math/0703392v1) §§4,6、
[Arithmetic Site](https://arxiv.org/pdf/1405.4527v1) Thms2.6–2.7、
[Geometry of the Arithmetic Site](https://arxiv.org/pdf/1502.05580v1) Thm4.2, §4.3、
[Scaling Hamiltonian](https://arxiv.org/pdf/1910.14368v1) Thm2.5, Fact3.6, Conj4.1、
[Deninger 2010](https://arxiv.org/abs/1001.1621) Conj2、
[Deninger 2024 v4](https://arxiv.org/pdf/1807.06400v4) §§7,10。
局所Γの出典と独立計算は `notes/phase3_structural_tests.md` に記録。
