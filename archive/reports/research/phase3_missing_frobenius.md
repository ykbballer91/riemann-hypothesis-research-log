**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase3_missing_frobenius.md` · Original SHA-256: `fdfab13252c49921482ee6a9619e6fdffbd56af1a4c23d9d6ffca3346ea3bc6f`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# RH PHASE III — Missing Frobenius / Arithmetic Geometry

2026-09-29。**RH OPEN。第25研究サイクル。指定された初期比較、三つの限定試行、strategy reviewを完了。**
Phase Iの23サイクル、Phase IIの第24サイクル、全反例・failed routesを保存した。
新規の主RHグラフ合流0、採用した未証明仮定0、完成証明候補0。
この研究巡の終了は、全ての算術幾何ルートの不可能性やRHの反証を意味しない。

## 結論を先に

有限体の曲線で算術的正確さと正性が結び付く場所は、**同じJacobian上の**
Frobeniusとample polarizationである。幾何的Rosati正性とπ†π=qが独立に分かるため、
その作用を忠実に受けるH¹の全固有値は|α|=√qになる。
古典的ζでは算術的な作用や全零点のtrace実現が全くないわけではない。
Connes–Consani–Marcolliの算術的cyclic quotientには、全非自明零点が重複度付きで現れる。
そこで不足する正値性は、既知のWeil/RH同値条件である。

したがって最も小さく**記述**できた既知gapは、
「この算術的商のtrace形式に、算術から独立に証明できる正のpolarizationを与えること」。
しかし、この記述そのものは新しい独立lemmaではない。
positive geometryと算術商を結ぶ具体的な比較定理を構築できておらず、
Level1の新しい差分圧縮を達成したとは判定しない。

さらに、この商へ周囲のL²正性を移す最も自然な案は、実際の算術データで失敗する。
CCM Proposition6.4の帰結として、特定の重み付きL² normで像を閉じると商が0になる。
unitarityは残るが全零点情報を失う。これは有限窓を拡張しても直らない位相の障害である。

## 0. 実行方針と出典境界

ユーザー指定に従い、最初は新しいproofを考えず既知のfinite-field spineを抽出した。
その後、gapを埋める限定命題を内部構成し、解析反例、既知性、独立監査を行った。
新しい外部RH証明主張を追う作業は行っていない。
物理・宇宙論・DNA・元の着想論文は証明材料に使用しない。
未知のHを「ζ零点をスペクトルに持つ空間」と定義することもしていない。

本記録は原論文全証明の再形式化ではない。既知の幾何定理・trace theoremを引用入力として
使った箇所、内部で再計算した箇所、数値診断を区別する。
一次資料の版・定理番号は各専門監査と `phase3_sources.json` に保存した。

## 1. 成功したfinite-field証明の差分抽出

必須12役割と10個の入力カードは `finite_field_dependency_spine.md`。
曲線の最終計算は次の通り。

    End⁰(J)_R 上の (x,y)=τ(xy†)>0
    + 同じ π に対する π†π=q
    ⇒ L_π* L_π=qI
    ⇒ |α|=√q
    ⇒ det(1−q^(−s)F|H¹)の零点はRe(s)=1/2.

忠実なTate realizationとH¹(C)≅H¹(J)が、最後のαを実際のzetaのαへ接続する。
ここで1/2はweight 1の平方normから出る。関数等式の中心を再説明しただけではない。

一般次元のDeligne Iでは別の経路が必要。
偶数tensorの局所traceは実数traceの偶数冪だから非負となり、monodromyはtensor
coinvariantsを制限してEuler積の極を制御する。
この二つが同じlocal systemで成り立つため、|α|≤q_x^(β/2+1/(2k))を得てk→∞とする。
さらに積variety/Künnethで残る誤差を除く。
単なる「Deligne purity」という名前に置換せず、何を幾何が供給するかまで分離した。
hard Lefschetzは1974年のこの証明の前提にしない。

## 2. Q側に既にあるもの

全対応表は `number_field_gap_matrix.md`。

1. Spec Zのclosed pointsはrational primesで、normはp。この算術対応は厳密。
2. prime powersは同じ点の反復に対応する。degree-n closed pointそのものとは違う。
3. 全log pを一つのlog qの整数倍へ変換できない。連続scalingはその代案だが、それだけでweightはない。
4. explicit formulaはprime powers、Gamma、極と全非自明零点を厳密に結ぶ。
5. CCMには算術restrictionの像のclosureによるcyclic quotientがあり、積分した作用のtraceが
   Σρmρ ĥ(ρ)と一致する。zero inputからの人工的対角作用素ではない。
6. Arithmetic Siteの点・Frobenius correspondencesと分布的countingは実在するが、
   適切なWeil cohomologyの未構成問題は別に残る。CCMの既存cyclic cohomologyを否定しない。
7. Deningerには実在するWitt-vector dynamical spaces、層cohomologyの定義、H⁰の定理がある。
   しかし必要なH¹の全零点・Gamma込みtrace/determinant・positive starは未供給。
8. local Γ factorは既に正則化determinantとして構成できる。infinityが全障害だとする根拠はない。

## 3. 最初に選んだ一つのtrack

**選択：Track B — Missing purity。対象：既知のCCM arithmetic quotient。**

全ての候補理論を同時に育てるのでなく、既に算術起源と全零点traceがある構成を基準にした。
Arithmetic SiteそのもののWeil cohomologyやDeningerの全programを一つの巨大仮定として
採用すれば、positivity以外にも比較・domain・determinant等の義務が残る。
それらを「一個のmissing object」と数えてgapを減らしたことにはしない。

CCMのtest coreでsharp反転を固定すると、

    H(f,g)=Tr θ(f*g♯),       H(T_af,T_ag)=aH(f,g)

は無条件に成立する。Hが正ならa^(−1/2)T_aはHを保存するunitary作用へ進められる。
だがHの正性は、ζの自明文字sectorではRHと同値。
この一行をpurity theoremの発見とは扱わない。
Hilbert completionにより元のgeneralized eigenspacesと全多重度が保存されるかも別義務。

**Missing axiom candidateの双方向監査:**

- A*を「全testでH(f,f)≥0」とするならA*⇔RH。即時に新ルートとしては棄却。
- A*を「具体的なfunctorial幾何、正の偏極、全trace/det比較が存在」とするならA*⇒RHは条件付き。
  RH⇒その幾何全体は未証明。強い未知条件を公理として採用しない。
- semisimple有限行列でpositive scaled metricを要求するだけならpure spectrumと同値。
  これを無限次元の幾何の存在と同値だとは言わない。

## 4. 三つのmajor bounded attempts

完全な新cohomologyを三個作ったという意味ではない。いずれも選択したgapを埋める
具体的な移植命題を一つ構成し、破壊試験で終了したもの。
式と全nの証明は `notes/phase3_structural_tests.md`。

|ID|試みた橋|厳密な結果|Decision|
|---|---|---|---|
|M1|点数・determinant・duality・算術的反復からpositive weightを導く|q=9、分子1−7T+9T²。全閉点数は正整数、traceとFEは成立するが根はweight1でない|一般公理からの強制を反証。positive polarizationを省けない|
|M2|ambient unitary normを全零点の算術商へ下ろす|LF模型で商modeが消える。さらにCCMの特定natural L² quotientも0となる既知算術障害を確認|bounded comparison / 単純Hilbert closureによる接続を終了|
|M3|各primeのpure local actionとexact Γ towerを直接接着|prime-circle traceは局所的にexact、Γ determinantもexact。しかし直和は非compact/non-trace-class、global zero H¹を得ない|local weight0からglobal weight1への直和接着を終了|

M1の追加公理テストで、正定値scaled-invariant metricを入れれば反例は不可能になる。
その場所がpositive inputの必要箇所である。ただしsynthetic testingは公理系の論理的最小性を
完全に証明したものではなく、実際の有限体幾何を持つ反例を作ったものでもない。

M2のactual障害は重要なnegative knowledge：CCMのtrace同定は急減少空間での商であり、
unitarityを持つ単一weightのL²商とは異なる。正値性が足りないからnormを取り替える、
という一般的修復で全零点を保持できるわけではない。

## 5. Archimedean placeを独立に監査した結果

Γ_R(s)=π^(−s/2)Γ(s/2)を単なる規格化として捨てていない。
local Hodge/Rees側のtower Θ∞eₙ=−2neₙについて、

    det_ζ((s−Θ∞)/(2π)) = √2/Γ_R(s)

を再計算した。√2はregularizationから固定される。
自明零点、Γの極、完成ζの極0,1を合わせることと、global nontrivial H¹を構成することは別。
infinityを座標の境界へ移しただけでmissing purityが出る機構は得られなかった。
このtowerは局所因子の既知構成であり、新たなLevel2成果とは数えない。

## 6. 反証・循環性・完全性の最終gate

- **Synthetic:** M1はrationality・全点数・反復・reciprocityを保った反例。positive polarizationまでは保たない。
- **Arithmetic-specificity:** M2 actual部分とM3 local部分は実際の算術を保持。そこからglobal positivityが出るとは未証明。
- **Circularity:** Weil positivity / normalized adjointをRHなしの正内積として使っていない。
- **Completeness:** CCMの全零点traceを承認するが、Hilbertizationがmodeやmultiplicityを保存するとは追加仮定しない。
- **Determinant:** 新しいpositive graded determinant実現はなし。Hadamardから作用素を人工的に製造していない。
- **Domains:** 核型空間のtraceとHilbert Schatten trace、formal adjointとclosed operator adjointを区別。
- **Scope:** Deningerの全programの逆含意は不明。特定の接着・商normの失敗を全幾何programの否定にしない。

## 7. 独立監査と数値の役割

BUILDERがfinite-field原典とcurve/generalの分離、LITERATUREがCCM/AS/SHと
actual quotientのsector平均、DESTROYERがDeningerとM1–M3の数学的反証を担当。
`proofs/audits/phase3-independent-audit.md` が限定監査の正準記録。
外部査読やRH完全証明の独立三重監査ではない。

`experiments/scripts/phase3_structural_checks.py` は整数・有理数でmatrix identitiesと
b₁,…,b₂₀₀を検算した。全bₙの正性は解析証明が担い、200までの計算から帰納しない。
零点位置とGamma恒等式のmpmath値は非認証診断。
初回のmp.diffはHurwitz引数1/4でtiny-step誤差を生じ、固定step四次差分へ修正した。
その数値失敗を恒等式の反例とも認証とも扱っていない。
結果：`experiments/results/phase3-structural-checks.json`。
新しいLean定理は追加していない。

## 8. Strategy review — 三回後のgap再計算

開始時：arithmetic exactnessとpositivityを同じ対象で結ぶ証明がない。
終了時：既知算術商での全零点traceは明確になったが、独立positive comparisonは得られない。
最短RH proof pathの未解決義務は不変。T000/T100/T110、同値クラス1のまま。

今回の進歩は誤った欠落分類の訂正と限定されたnegative knowledgeである。
「Frobeniusが一切ない」「cohomologyが一切ない」「Γが未構成」「作用素をもう一つ作ればよい」
のいずれも採らない。一方で、新たな非同値算術lemmaを得たとも主張しない。

**Level判定:** Level1–5は今回いずれも未達。
最小の既知gapの記述はできたが、RH同値の符号命題から独立な一個の数学的構造へ
圧縮することができなかったため、Level1を自己認定しない。

**終了範囲:** M1–M3のルートを終了し、同じgapを持つ4番目の一般作用素・norm・局所直和を
自動開始しない。fixed-window numerical enlargementにも戻らない。
再開条件は、具体的な算術的cycle/intersectionまたはtensor/pole identityで、
既存算術商の全零点traceを失わず正性を独立に供給する新しい内容があること。
現時点でその内容を持つ未処理候補はない。RHは未解決のまま保存する。

## 9. 再開用ファイル

- `phase3_gap_state.json`: machine-readableなgap、三試行、成功レベルと停止条件。
- `finite_field_dependency_spine.md`: 公理カードと12役割。
- `number_field_gap_matrix.md`: 1対1比較、七役割、consistency triangle。
- `notes/phase3_finite_field_audit.md`: Deligne・Grothendieck・Rosatiの詳細。
- `notes/phase3_connes_consani_audit.md`: 三種類の構成とtopologyの区別。
- `notes/phase3_deninger_audit.md`: 実在部分、巨大未証明条件、local Γ、限定no-go。
- `notes/phase3_structural_tests.md`: 内部構成と破壊試験の全計算。

一次資料：
[Deligne I](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)、
[Grothendieck](https://www.numdam.org/item/SB_1964-1966__9__41_0.pdf)、
[CCM](https://arxiv.org/pdf/math/0703392v1)、
[Arithmetic Site](https://arxiv.org/pdf/1405.4527v1)、
[Scaling Hamiltonian](https://arxiv.org/pdf/1910.14368v1)、
[Deningerのcohomological program](https://arxiv.org/abs/1001.1621)。
これは文献リスト自体を成果とした報告ではなく、その定理の役割と残る数学的差分の記録である。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/phase3-structural-checks.json`](../../../artifacts/experiments/results/phase3-structural-checks.json)
- [`experiments/scripts/phase3_structural_checks.py`](../../../artifacts/experiments/scripts/phase3_structural_checks.py)
- [`proofs/audits/phase3-independent-audit.md`](../../audits/proofs/audits/phase3-independent-audit.md)
