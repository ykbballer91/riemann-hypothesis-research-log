**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/strategy_review.md` · Original SHA-256: `5a54bb9d8d066700e9a978292d4da8d3a625e316153ce8059cd11a6a4c75a7bb`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Strategy review — 2026-09-29

## Phase II — 3 major attempts後の見直し（現在）

ユーザーの明示的再開指示によりGenerator / Boundaryを別トラックとして検査した。
初期A/B/C/D比較からactual算術のCへ集中し、C→B→Aの3つの具体構成が終了条件に達した。
Dは初期screen、Cのcut-off修復はC内の検査とし、attempt数を水増ししない。

Cは独立に正自己共役だが全ζ零点をresonanceとして生成する。actual poleのLaplace
parameterはRH下でも非実。正のcut-off系へ移すと全ζ零点の回収を失う。
Bはexact prime m-functionを持つが逆canonical定理への入力がRH同値。
Aは算術時計の0を固定するがNewman thresholdの0を与えず、Gaussian境界への極限は
actual familyの非実零点を無限遠へ逃がす。Dは実Gaussianのlattice liftで交換式が偽。

したがって、今回のframingだけから自動的にzero exclusionが出る候補を終了する。
全generator理論の不可能性を証明したのではない。再採用には上のmissing linkを
独立に変える具体的算術identity/estimate/domain theoremが必要で、今回は得ていない。
主graph合流0、追加仮定0、RH義務削減0。補助成果をRHへの距離短縮に数えない。
詳細・監査・既知性は `generator_boundary_hypothesis.md` と同ノートのリンク先。
新しい独立入力のない同型4候補目やfixed-window enlargementは開始しない。

## 以下はPhase Iの履歴

第23サイクル後の詳細報告は `release/research_handoff_2026-09-29.txt` に保存した。
その後の一時停止はユーザーのPhase II指示で解除された。以下の古い次候補は現在の実行指示ではない。

## 現在の方針 — ユーザーの最新指示が優先

外部の新しいproof claimを順に選ぶ運用を停止し、内部構築・第一原理を優先する。
文献は、具体的な候補の既知性と必要な条件を確認する段階で用いる。
以下の古いfrontier優先・次回の外部候補指定は履歴であり、実行指示として再開しない。

最初の内部巡では、境界平方＋残差の恒等式から実核の正値性を狙った。
強対数凹性・増加scoreは、位数1のFourier変換を持つ超指数減衰模型でも不十分。
平方和になるGaussian実因子積も、実核の三次対数差分により点wise閉包から除外された。
次にactual thetaの正な低階fluxと整数移動の和を直接導出したが、
Bernstein型への強化は原点の厳密な符号で失敗し、移動和には未制御の差引項が残る。
全証明と検算は `internal_first_principles.md`。終了した候補を局所条件の追加や
同じ式の改名で継続しない。新体系にも正値性を仮定として埋め込まない。

RH同値クラス1、主グラフ合流0、追加採用仮定0。今回も証明距離の短縮は主張しない。
今後の候補は内部導出した、実際の算術対象への独立な制御から組み立てる。

次巡では正移動の一般論に戻らず、Mangoldtの畳み込みと一素数の全幾何級数を使用。
正負Gram項の更新式を得たが、一素数でもPSD保存は偽だった。
さらにactual thetaの有限素数近似を検査し、積分・反射欠損・正エネルギーの
大域極限が失敗することを解析的に証明した。正半直線の偶延長へ直しても、
全ての有限段階に無限個の非実零点があるため、全実零点保存族にはならない。
この近似法を素数数・零点表の拡大で続けない。詳細は `prime_insertion_closure.md`。
前巡は次の行動を変える証拠を得たPROGRESSに分類するが、RH証明距離の短縮ではない。
今回も主グラフ合流0。次の有限構成を検討するなら、事後的な偶化ではなく
全核のmodular境界条件を保つ仕組みが必要。別の全域算術機構も排除せず探索する。

その条件を満たす自己Fourier seedの構成も次巡で検査した。
一般Schwartz testの完成関数はξ×整Mellin因子であり、元の全零点を除去できない。
さらに自己双対性・seedとcompleted kernelの正値性・帯内限定・端点規格化を保ちながら、
1/4,3/4±32iの四点を追加する具体的な微分変形を構成した。
標準のGamma因子は変わるため、固定Gammaを含むRH構造への反例とは扱わない。
構成後の限定文献確認では、個々のHermite固有関数の既知定理と、自己Fourierな
線形結合全体に対する偽の拡張を区別した。最新proof claimの追跡には戻っていない。
Gaussianの消滅方程式の素朴な直和も、必要ベクトルが空間外で部分和がL²発散するため終了。
`selfdual_theta_boundary.md` に証明・区間評価・終了範囲を保存。主グラフ合流0。
次は標準Gamma/Gaussian固有の条件を算術的な相殺に接続する独立恒等式が必要。
既に棄却した一般自己双対性や直和のpositivityに戻らない。

続く巡では、そのGaussianを固定し、整数和から連続密度を差し引く自然な補正を構成。
全H^kで収束を修復でき、共通正測度の制限として正のLaplace Gram増分も存在した。
しかし微分後の自然なscalar energyは最初の段階で減少し、実際の有限補正核には
全Nで負Gram方向がある。収束する位相と指数重み付き評価の位相の違いも具体的に確認。
`continuum_subtraction.md` に独立解析監査と有理数・区間検算を保存した。
今回もRH義務は減っていない。終了した有限近似をNや補正次数の増加で続けない。
有限theta近似の正値性からの伝播という設計を一旦外し、全算術対象の交差項を
直接制御する別の恒等式を内部から探す。全称正値性を新しい公理や局所条件へ改名しない。

有限theta近似を外した次巡では、全整数の相関からGCD Gramを構成した。
Möbius反転で正のdivisor featureへ移し、整数倍shiftの全域等長表現も得た。
しかし標準係数ℓ²ではα=1/2の形式が全面的にsingularであり、
log nを共役したMangoldt生成子の自然なHermitian formも下半有界ではない。
正測度の対数微分には必然的に符号と発散する定数が現れる。
`arithmetic_gram_generator.md` に構成・domain・反証・構成後の既知性照合を保存。
この巡もRH証明距離は不変。次は正Gram模型を先に増やす設計を外し、
所定のGamma・pole項を含むactual Weil全形式から、算術交差項の恒等式を導く。
独立な符号評価を持たないまま形式の名前・完備化・共役だけを変えて続けない。

## 以下は方針変更前の履歴

発動理由: imbalance、generic Schur propagation、spiral-scaleの3候補が終了。
OPEN nodeが3 cycle変わらず、新しいdirect proof claimをユーザーが指定した。

最大のボトルネックは、全試験関数についてのWeil正値性を与える独立な算術機構。
自己共役性、座標変更、保存量、有限認証、局所延長では閉じていない。
T000/T100/T110の同値クラスは変わらず、新しい未証明仮定を採用していない。
したがって直近の成果は研究上の整理と反証で、RHまでの証明距離の短縮ではない。

## Discovery reset とportfolio選択

|候補枠組み|現在不足しているもの|今回の優先度|
|---|---|---|
|Weil positivity|全supportの算術正値性|Desogusがまさにこの補題を主張。DIRECT監査を最優先|
|Hilbert–Pólya / dilation|全零点を漏れなく実スペクトルへ同定する構成|新入力なし、保留|
|de Branges / Krein|全区間可逆性・正Hamiltonianと算術同定|既知同値条件だけでは進まない、保留|
|Nyman–Beurling|必要な全域近似／距離消滅の無条件評価|現状の新規入力なし、次回frontierで再比較|
|Li criterion|全係数の正性を独立に強制する評価|同値変形だけは採用しない|
|explicit / trace formula|算術項と全zero spectrumの正性を保つ同定|外部候補のrouting監査に直接必要|
|dynamical / spectral zeta|指定したζを実現し線外resonanceを排除|一般unitarity・自己相似では不足|
|function-field analogy|数体に対する実在する正性構造|比喩を証明に採用しない|
|statistics / random matrices|全零点の厳密禁止機構|統計・有限一致のみではDIRECTにしない|

Weilを優先する理由は過去の投資ではなく、現在のcritical unknownを埋めたと主張する
版固定可能な外部候補があるため。主張が壊れた場合は最小gapの修復可能性から再評価する。

DIRECT: Desogus2609.20367v2の依存グラフ・最小cut・算術induction。
ENABLING: そこで発見したproof-critical gapの修復に限って優先する。
HEURISTIC: 現行一般候補は終了。固定窓の数値記録更新で埋め合わせない。

## 実行規則

ユーザーへルート選択・継続承認を質問しない。各pivotで一次文献frontierを確認する。
補助定理数、README、checkpoint数、精度向上を進展の指標にしない。
非criticalなLean追加は停止。新規proof-critical、domain/sign事故、有限無限の橋だけを優先する。
論文のPROVED-IN-PAPERとINDEPENDENTLY-VERIFIEDは別欄にする。
内部監査を全て通過しても外部claimの監査通過であり、外部承認なしにRH SOLVEDとは記録しない。
資源制限時以外は、状態更新・ボトルネック再評価・次の最高優先処理まで自律継続する。

## Compaction / direct-claim review

Desogusの最小cutは6.29→8.4→8.5のactual Weil block同定に絞られた。
一armのdebitを二armへ渡す追加identity、半密度の対角補正、positive physical pivotが未確保。
RL-kの直接修復を試したが未修復。有限safe-cut4,993件の認証は技術的修復に限られ、
RH OPEN同値クラスと最短証明経路は変わらない。
Cáceres2609.28529v1の新しいDIRECT claimはTheorem4.1が反証された。
定義したratioは零点条件なしで全stripの固定sについて1へ収束する。端点符号修正でも直らない。
この候補は即時終了し、より大きな有限表や図の再現に進まない。
次は直近30日frontierをNyman–Beurling/de Branges/Li/traceも含め再比較し、
具体的な新入力があるDIRECT候補を選ぶ。Desogusは未証明RL-kを明示して保留し、
追加計算の量によってgapを隠さない。

## Finite-to-infinite continuation の bounded gate

Silvaの有限近似は正しいpartial statementだが、actual U4がunit-circle条件を満たさないため
Rodríguez–Villegasの直接十分条件は停止。actual Z4の成功や特殊LP模型の有限成功を
全Eの証拠にはしない。全Z_E lineはHurwitzによりRH十分だが逆方向は未確認であり、
既知Jensen criterionと同一と断定しない。新しいDIRECT claimは限定frontier検索で未発見。
最後にE=0,2,4,6のmonic Favard整合性だけを調べ、固定Jacobi作用素への最も直接の
同定が可能かを判定する。次数を広げる計算はしない。
Desogusの全shellをmultiplication−rankoneへunitary同定する強い読解はspectral typeで不可能だが、
原文はground contributionに限定され得る。このscope攻撃を論文への確定反証へ昇格しない。
OPEN classは依然1、主graphへ新規merge0、実質的な証明距離短縮なし。

Jacobi整合性検査はE≤6で反証され終了した。次にNyman–Beurlingの正射影decrementを
一次文献と照合したが、自然なGram正値性とexact restrictionsだけではlimit defectを消せない。
Bettin–Conrey–Farmerの最適近似はRH自体を仮定しており、無条件入力には採用しない。
`nyman_beurling_closure_gate.md` に現在不足する独立評価を明記。
この比較も既知criterionの整理であり、RHへの距離短縮として数えない。

## 追加debit修復後の強制レビュー

compactionと最短経路不変のため再評価。literal 2Dを残し余裕で払う条件を具体化したが、
actual folded response / pivot upper boundの算術辞書を得られなかった。
固定forcingの厳密反例はgenericな小pivot相殺による追加支払いを否定し、
全窓polar-free core正値性は既知criterionの直接拡張によりRH同値と判定した。
修復は未完、主graph merge0、RH OPEN class1、追加採用仮定0。
今回も証明距離の短縮でなく、修復候補の選別と不足条件の精密化である。

この地点でDesogusの同じ辞書探索を周回しない。過去30日の検索をarXiv外の一次preprintへ広げ、
Zhangのentire-divisibility claim（Preprints.org v61、2026-09-09）とMukhaのχ-lift claim
（Cambridge Open Engage v4、2026-09-11）を新たなDIRECT候補として最小cut監査に着手した。
両者とも未検証から開始し、対称因子の固定と交換、対数branchと実ζのspectral同定をまず検査する。
割合定理や同値条件を新しい完全証明として扱わない。

Zhang v61のLemma6は、全明示的な積・strip条件を満たすorder1反例で終了。
Mukha v4は紹介ページの指数写像でなく本文のMöbius写像を監査し、因子2の座標修正を分離した。
修正後もTheorem10.2.Cの境界前提を全零点について外せず、同値の連鎖からのRH証明は未成立。
この2件とDesogus追加debit修復後にも最短経路は不変なので、再度discovery reset。
新しい独立算術入力がない同じrouteを、補助定理・表・精度・文書量で継続しない。

## 9月27日の新しい算術階層に対する bounded gate

[Musin, 2609.33794v1](https://arxiv.org/html/2609.33794v1)はRH proof claimではない。
§3のarithmetical familyは無条件にfirst contactが無限遠へ逃げるが、§4 Theorem4.1の
global maximumを保つfamilyでは、その逃走自体がRH同値。両者を混同しない。
後者へ「任意の固定整数Mは、十分高いlevelの全memberを割る」という§3型の性質を移す案を検査した。
CA部分集合C_kについては、この性質も `min C_k→∞` と同値である。
順方向は任意の閾値BにM>Bを選べば全member>Bとなる。逆方向はLemma2.1の
各固定素数の指数→∞を、Mを割る有限個の素数に適用するだけである（空集合min=∞を含む）。
従って§4のfamilyでは移植候補もRH同値。§3の無条件証明は当該familyの逃走を既に使用し、
そのまま新familyの逃走を証明する入力にはならない。ROOT/BUILDERが独立確認し即時停止。
論文全体の独立検証や反証ではなく、こちらの移植案を棄却したもの。CA表は生成しない。

現時点: RH OPEN nodes T000/T100/T110（同値クラス1）、新規採用仮定0、主経路上の新規proved node0。
次の採用条件は、名前や座標を変えた全称正値性ではなく、実際の算術量に対する独立に証明できる評価。
今回の作業は研究上の選別・修復範囲の確定であり、RHへの証明距離短縮とは記録しない。

## Adam の直接主張と有限負指数の gate

新しいDIRECT claimとcompactionのため再評価。Adam v4（2026-09-09）は
Lemma 1の作用素近似が実際の核について反証された。固定した半区間指示関数で
誤差normが一様に正であり、より細かいmeshの計算は不要。
正しい圧縮へ修正すれば収束するが、共通のcoercivityは不可能。
定理の一般的な条件付き単射性と、実作用素で偽になる前提を区別して終了した。
`proofs/audits/adam-projection-audit.md` に最小cutと修復限界を保存。

別の弱い構造として有限負指数を検査したが、有限個の不定pairを排除する算術入力は得られない。
平行移動はそのblockをJ-unitaryに保ち、負方向を無限個へ増やす推論も偽。
Bombieri (2000)の原本を確認し、有限行列の指数定理を全compact coreへ転記していない。
このbounded gateは `research/finite_negative_index_gate.md` に保存して終了。

Arneth SSRN7483040（2026-09-21公開）はlandingの書誌・abstractまで。
本文はweb/curlの取得失敗で未監査であり、数学的な棄却とは分類しない。
Dhiman–Kadiri–Quesada-Herrera2609.00537v1 Cor0.3とFiori2609.22624v1 Thm2/Cor1は
本文の定理文・条件まで比較した。前者の全高ζ近似誤差、後者の短区間におけるstrip内割合は、
全零点の中心線所属やWeil算術項の必要な符号評価を与えない。全面検証や主グラフ採用はしていない。

このcycleもOPEN同値クラス1、追加採用仮定0、主グラフ新規proved node0である。
今の最大障害は、作用素の一般論でなく実際の算術対象に適用できる全域評価。
次は、新しく見つけたFreedman2606.29555v1のclosed-trace quotientをENABLING候補として
限定確認する。RH proof claimではない。別モデルのcertificateなら、それをWeilの全域正値性へ
移す実恒等式がない限り計算再現へ進まない。Suzuki v3は既照合で、新版未出のため再監査しない。

Freedmanの限定gateも終了。本文と付録でstatusが異なり、Appendix C後半は全域収縮性を主張する。
これを単に『著者が未完と認めている』として処理せず、critical inferenceを監査した。
元の核からde Branges型核へは、二変数Fourier変換とparameter積分による厳密恒等式を得た。
ROOT/BUILDERの独立導出、DESTROYERの共役・多重零点検査を通過。
しかし中心parameterのPSDはCsordas–Escassutの既知複素Laguerre基準へ戻り、RH同値。
さらに \(|\kappa|\le1\) とGreen minimizerの定常性から圧縮後の収縮性を導く一般推論は、
\(\|C\|=1,\|K\|=1/2\) でも \(\|CKE\|=3/2\) となる厳密有限模型で偽。
不足しているのはactual liftのエネルギー制御であり、完備化・小さい数値残差では補えない。
これを新しいWeil全域正値性入力として採用する案を終了し、数値certificate再現を開始しなかった。

今回の接続恒等式は外部プログラムの一段を明示化したが、新規性を主張せず、
主RHグラフの未解決義務を減らしていない。再評価後も最短経路は不変。
次回は新しい全域算術評価がある入力に限定し、Freedmanの同じ収縮性を
normの付け替えや有限matrix拡大で再試行しない。主グラフに採用した仮定は増えていない。


## Phase III — 三つのbounded attempts後のstrategy review（第25サイクル）

有限体曲線は同じJacobian上のRosati正性とFrobenius adjointが核心。Deligne一般次元は
tensor/monodromy/極支配という別機構である。数体では既存CCM算術商に全零点traceが
既にあるためMissing purityへ集中したが、その正性は既知RH同値条件。

M1: q=9のrational trace模型で、全次数の正整数閉点数、duality、FEがあっても非pure。
M2: LF商の一般反例に加え、CCMの特定weighted L2商がactual arithmeticで0となる既知障害。
M3: prime circlesとGamma towerはlocalでexactだが、直和はglobal positive zero realizationに届かない。

三試行後も独立positive comparisonは未取得。gap記述の改善をLevel1成功には数えない。
主graph19nodes、RH同値class1、追加前提0、追加Lean0、RH OPEN。
最終ログ research/phase3_missing_frobenius.md、機械状態 research/phase3_gap_state.json。
全算術幾何programを不可能とは判定せず、試した三つの機構だけを終了する。
再採用には既存算術商と同じtraceを保つ、具体的な算術的intersectionまたはtensor/pole入力が必要。
その内容を持たない4番目の名称変更や有限窓拡大は開始しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/adam-projection-audit.md`](../../audits/proofs/audits/adam-projection-audit.md)
- [`release/research_handoff_2026-09-29.txt`](../release/research_handoff_2026-09-29.txt)
- [`research/finite_negative_index_gate.md`](finite_negative_index_gate.md)
- [`research/phase3_gap_state.json`](../../../data/source-records/research/phase3_gap_state.json)
- [`research/phase3_missing_frobenius.md`](phase3_missing_frobenius.md)
