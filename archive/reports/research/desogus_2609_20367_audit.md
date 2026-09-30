**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/desogus_2609_20367_audit.md` · Original SHA-256: `884485b02c39ae2672f1fb5de370a9081f4a12710e1112ad605732a7aa519885`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Desogus 2609.20367 — DIRECT adversarial audit

開始・統合更新: 2026-09-29。**STATUS = UNVERIFIED EXTERNAL PROOF CLAIM WITH PROOF-CRITICAL GAP**。
RHはOPEN。公開論文の結論を事実・前提として採用しない。

対象は Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*。
v1は2026-09-17、最新版v2は2026-09-20。v2を主対象としv1との差も確認する。
[原文・版履歴](https://arxiv.org/abs/2609.20367)、
[v2全文](https://arxiv.org/html/2609.20367v2)。
[Clayの現在の未解決分類](https://www.claymath.org/millennium/riemann-hypothesis/) を確認した。
原本hash・取得範囲は `desogus_source_provenance.json`。著者コードは実行・importせず静的に調査し、必要な有限計算は独立実装で検査した。

## 最小cutを優先する分担

- ROOT: GateI scalar bound、proof-critical arithmetic budgets、Y=7証明書の独立検査。
- BUILDER: GateII common-cut、inherited-response配置、同じprimal formにおける予算・infimum。
- DESTROYER: restricted odd Weil criterion、exact compression、domainとGateIII closure。
- LITERATURE: 全論文の依存グラフ、外部引用、補足package、版差分。

全ページの一様な要約を作らず、各新規ノードの仮定とcutを先に監査する。
以下は [Gate II監査](../../audits/proofs/audits/desogus-gate2.md)、
[Gate III監査](../../audits/proofs/audits/desogus-gate3.md)、
[計算・修復監査](../../audits/proofs/audits/desogus-computation-and-repair.md)、
[依存グラフの scoped audit findings](desogus_dependency.json) を統合した対応票である。
`VALIDATED` は指定範囲だけの判定であり、著者の全結論を承認する意味ではない。
依存グラフの原文 inventory に残る `INDEPENDENTLY_VERIFIED=NO` と、後から追加された個別監査結果を区別する。

## OUR BARRIER: 局所正値性は全窓へ伝播しない

WHY GENERIC METHOD FAILS:
Schur residual `D−B*A^(-1)B` は内側gapだけから非負にならない。
同じlog-domain、exact restrictions、compact resolvent、局所延長を持つ一般模型は有限半幅で0を横切り得る。
この模型は実Weil形式の負方向ではない。

DESOGUS CLAIMED REPAIR:
指定された算術routingと同時common-cutで、継承応答・mismatch・aligned forcingを同じ形式へ配置し、
全整数stepの正のscalar reserveへ結び付ける。

EXACT THEOREM / LEMMA:
v2 Theorem 6.53 (`thm:MASTER-common-cut`)、Lemma 8.2 (`lem:MASTER-P2-response`)、
Lemma 8.4 (`lem:MASTER-P3-final`)、Theorem 8.5 (`thm:final-master-harmonic`)、
Corollary 8.6 (`cor:final-gate2`)。実作用素への同定は Corollary 6.29 を経由する。

ASSUMPTIONS:
旧窓のstrict positivity、正しいrouting/domain、同じprimal formの下界、算術予算の正値性。
さらにモデルの正pivot `Pi_phys>0` と、実際のold/shell blockからのexact coefficient dictionaryが必要。

IS THE REPAIR ACTUALLY SUFFICIENT?: **NO AS PRINTED / CORE GAP REMAINS。**
one-cell common-cutの下界自体は成立するが、そのlower modelを実Weilのexact folded operatorへ昇格させる同定は未証明。
Lemma 6.28は正pivotを仮定し、Corollary 6.29のrow equationだけではその符号を供給しない。
加えてLemma 8.4の表示された二armのshortは `Q−2D` であり、Theorem 8.5が使う `Q−D` と一致しない。
正pivotを追加してもこの差は消えない。具体的な最小修復義務は末尾のRL-kを参照。

INDEPENDENTLY REPRODUCED?: **YES, MODEL ONLY; NO, ACTUAL ALL-STEP INDUCTION。**
Lemma 6.48 / Theorem 6.53のrank-one short・ground/transverse同時下界、
Lemma 8.1 / 8.2のstationarity・Young代数は独立に再導出した。
実際の応答・comparatorの配置と全整数stepの正値性は再現していない。

STATUS: **PROOF-CRITICAL GAP。** Corollary 6.29 → Lemma 8.4 → Theorem 8.5が残る最小cut。
一般模型の反例はこの推論の不足を示すもので、実Weilの反例でもRHの反証でもない。

## OUR BARRIER: gap消失・逆作用素と無限次元domain

WHY GENERIC METHOD FAILS:
`A^(-1/2)B` のrange/有界性を失う場合があり、形式的なSchur式だけでは足りない。
正injectiveだけで有界逆作用素は得られず、局所closednessからglobal L² closabilityも従わない。

DESOGUS CLAIMED REPAIR:
true metric、root lift、harmonic graph上の正性、endpoint induction、局所closed form。

EXACT THEOREM / LEMMA:
v2 `lem:root-lift-final`、`lem:green-nested-schur`、`lem:MASTER-P3-final`、`lem:closure-global`。

ASSUMPTIONS:
各旧blockの可逆性、minimizerの所属、各shortingのrange/domainの整合。
たとえば `A_k≥c_k I, c_k>0` と必要なmixed-form制御を用意すれば通常のSchur最小化は正当化できるが、
その前件と実算術blockとの同定を各stepで別に示す必要がある。

IS THE REPAIR ACTUALLY SUFFICIENT?: **CONDITIONAL FOR LOCAL FORMS; NOT ESTABLISHED FOR THE INDUCTION。**
必要なdomain・正pivotを仮定したscalar消去代数は正しい。しかしrow equationを満たすことだけでは、
正pivot、same-vector energy、実際のminimizerへの適用条件は得られない。
一方Lemma 7.1を通常のglobal `L²_odd(R)` closureと読むと、その追加主張は成立しない。
全局所正値性の仮定からRHを経由した場合でも、零点でのFourier sampling形式はこの空間でnonclosableになる。

INDEPENDENTLY REPRODUCED?: **YES, SCOPED。**
Lemma 6.28の正pivot付き代数、固定窓のform-domainでのexact restriction、
全endpoint正値性を仮定したradius independence / compact-core positivityを確認した。
global L² closureについては、L²で0へ収束しながらWeil-formで非零sampling vectorへ収束する列を構成した。
root-lift・全nested shortの実算術domainを包括的に検証済みとはしない。

STATUS: **CONDITIONAL VALIDATED（上記局所・compact-core部分）／GLOBAL L² CLOSURE: FAILED, NOT ACTUALLY NEEDED。**
closure句は削除し、compact odd coreからTheorem 1.2へ直接進めるので、この誤りは主cutではない。
削除によってGate IIの未証明なinductionが修復されるわけではない。

## OUR BARRIER: 正tail・部分予算を重複使用できない

WHY GENERIC METHOD FAILS:
固定supportのarchimedean tailの正増分はL方向のshell追加ではない。
素数項は不定で、別々に下界した同じreserveを足せば過大計上する。

DESOGUS CLAIMED REPAIR:
arithmetic routing、full-form transport、coherent multi-source shorting、ground/transverseのcommon-cut。

EXACT THEOREM / LEMMA:
v2 `prop:full-form-transport`、`thm:residual-CMC`、`thm:MASTER-common-cut`、`cert:MASTER-aligned-final`。

ASSUMPTIONS:
全項の正規化・符号・source重複を保存する恒等式。finite certificateとanalytic tailの重なり。
半密度の変数変換ではoff-diagonal kernelだけでなく、対角killing項・potential・pole・prime operatorを運ぶこと。
inherited shortの負のreference debitと二armの両方の費用を同じactual formへ残すこと。

IS THE REPAIR ACTUALLY SUFFICIENT?: **NO AS PRINTED / EXACT BUDGET PLACEMENT UNREPAIRED。**
stationarityの恒等式 `−pθ²|X|²=−p|X|²+(1−θ²)p|X|²` は正しいが、
右辺の正surplusだけを残して負referenceを捨てることはできない。
二armの `2D` はunitaryな対称・反対称座標変換でも不変であり、単なるnormalizationでは `D` にならない。
またProp. 5.3の抽象unitary transport自体は問題なくても、kernelの等式だけではfull-formの等式にならない。
Gate II監査DG10では、半密度変換で非零かつ負にもなる対角補正を厳密に導出した。
これはkernel-only等式への反例であり、full Weil形式や抽象unitary性への反例ではない。

INDEPENDENTLY REPRODUCED?: **YES, SEPARATED SCOPES。**
二armの平方完成、正pivotのまま `Q−D=0` かつ `Q−2D<0` となる一般模型、
full difference formのcanonical transport、one-cell formとそのlower modelが等しくないことを確認した。
DG10の半密度補正の閉形式、負になるsmooth-core例、kernel minor、未知量依存forcingの費用もDESTROYERが独立に検算した。
補足ZIPの静的検索でも、欠けたactual row / coefficient dictionaryの追加証明は見つからなかった。
有限safe-cutは独立Arb192実装で `7≤k≤4999` の全4,993整数を検査し、
全gapに `>1.5202196525` を認証した。別実装Arb256では5点を再検査した（全件の二重実行とはしない）。

STATUS: **CORE OPERATOR BRIDGE: GAP / RL-k NOT REPAIRED。FINITE SAFE-CUT: TECHNICAL — FINITE COMPONENT REPAIRED。**
後者の結果は [finite certificate](../../../artifacts/experiments/results/desogus-safe-cut-repair.json) に保存済み。
`k≥5000` の解析tail、actual operatorへのlift、第二armの費用はこの有限修復の射程外。

## OUR BARRIER: 有限endpointから全testへの全称量化

WHY GENERIC METHOD FAILS:
有限個の数値結果は全supportを覆わない。subsetの正性だけではWeil基準を使えない。

DESOGUS CLAIMED REPAIR:
Y=7から全整数Yへのinduction、正確なzero-extension、restricted real odd criterion、closure。

EXACT THEOREM / LEMMA:
v2 `cert:base-Y7`、`lem:zero-extension-proof`、`lem:cofinal`、`thm:weil-odd`、`thm:final-rh-closure`。

ASSUMPTIONS:
baseの全mode認証、全整数induction、奇実testによる線外zeroの検出、各固定窓の稠密性。
endpointは `a_N=(log N)/2` であり、全整数 `N≥7` の実localized Weil formの正値性が前件である。

IS THE REPAIR ACTUALLY SUFFICIENT?: **YES, CONDITIONAL ON ALL-ENDPOINT POSITIVITY。**
任意の有限support半幅aに対し `N>e^(2a)` を選べばexact zero-extensionにより
`q_a(f)=q_(a_N)(Ef)≥0`。endpoint間で一様なspectral gapや極限交換は不要。
その後restricted real odd Weil criterionを適用でき、global L² closureを経由する必要もない。
ただし全endpointの前件を有限certificateや局所延長から得る段階は未証明である。

INDEPENDENTLY REPRODUCED?: **YES FOR THE CRITERION / COMPRESSION / CONDITIONAL COFINAL BRIDGE; NO FOR ITS ALL-STEP PREMISE。**
Theorem 1.2の奇実testによる零点検出、Lemma 1.3のexterior cancellation・zero-extensionを
smooth core / form domain上で再導出した（任意L²関数のoperator bracketという意味ではない）。
Lemma 1.4 / Corollary 8.6のcofinal bridgeも上の前件付きで確認した。
Y=7について独立に確認したのは、Appendix A.3の印刷された7×7区間行列の正定値性である。
厳密有理Gershgorin下界は `>0.5198729787` だが、その行列のactual operator assembly・無限complement・全mode支配は未認証。

STATUS: **CRITERION / COMPRESSION: VALIDATED。COFINALITY: CONDITIONAL VALIDATED。BASE MATRIX: VALIDATED MATRIX ONLY。**
最後の論理橋は修復を要しない。前段の実作用素上のbaseと全整数inductionの不足を、この橋で埋めることはできない。

## 残る最小修復義務と停止判定

修復課題はscalar精度の追加でなく、Gate II監査DG9の **RL-k（未証明）** に限定する。
実Weilのold/shell blockから、lower modelへ置換する前にtransportと所定のcommon-complement/source shortを行い、
最後の二armを残した閉形式を `M_k^act` とする。消去済みinherited responseの負referenceもground blockに含める。
actual arm blockから `P_k>0`、coupling `b_k`、`d_k=b_k*P_k^(-1)b_k` を定義し、必要なdomain/rangeを指定する。
実kernelから独立に構成した `C_k^fold` に対し、少なくとも次のexact identityが必要である。

\[
M_k^{\rm act}=
\begin{pmatrix}
C_k^{\rm fold}+d_k&b_k^*&b_k^*\\
b_k&P_k&0\\
b_k&0&P_k
\end{pmatrix},
\qquad
\operatorname{Short}_{\rm arms}M_k^{\rm act}=C_k^{\rm fold}-d_k.
\]

これは「二armが一arm分しか消費しない」という命題ではない。前段の対角に実際に `+d_k` が存在することを証明すれば、
正しい二arm費用 `2d_k` の後に本文が必要とする残差が得られる、という候補修復である。
`C_fold:=R_act−d_k` と結果に合わせて定義することや、任意countertermの追加は禁止する。
`P_k` の正値性・domainと、独立に定義した `C_k^fold−d_k` の下界も別途必要である。

この辞書で追跡すべき未指定費用は、(i) DG10の半密度killing項と元のpotential、
(ii) retained-retained残差と負reference debit、(iii) final assemblyで支払先のない第二armの `d_k`。
one-cell lower modelの下界をexact operator同定へ読み替えてはならない。
現状は `a_(k,±), beta_k, C_fold` をactual operatorからこの精度で計算する定義・証明がなく、
**RL-kは未修復**である。actual対角が `C_fold` のままなら、この修復案は成立せず、本当に `2d_k` を支払う別の算術評価が必要になる。

原文v2と補足でこの不足を解消する証拠は得られなかった。一般模型による代数的反例は実Weil負方向とは区別する。
**主RH証明グラフへのmergeは0。RHはOPEN。** 条件付きの正しい橋と有限技術修復を、核心の証明完了として扱わない。

## 追加修復の有界探索: literal 2D を払えるか

[追加debit修復条件](../../audits/proofs/audits/desogus-extra-debit-repair.md)で、2Dを保持した十分条件を導出した。
先行する実form辞書を条件付きで認めても、残余予算M_kに対して `D_k[f]≤M_k[f]` という
ζ固有の応答評価が必要である。元のunitarityだけでは、その実folded写像がcontractionとは言えない。
actual a_+、β、射影・metricの辞書が欠ける地点で、この修復探索を停止した。

[固定forcingの厳密族](../../audits/proofs/audits/desogus-pivot-cancellation-stress.md)では旧scalar pivot≥1/2、
全source Hessian正、core正、停留条件、root identityを保ちながらD=1/εとなる。
正しい単一charge相殺Q−D=0を否定せず、有限reserveで第二Dを自動的に払うgeneric案だけを棄却する。
また全窓polar-free core正値性は、極で消える実奇testもWeil基準に十分なためRH同値。
この迂回も独立な弱い前提には採用しない。

2026-09-29の再照合でarXiv最新はv2、Zenodo最新supplementは2.0.0で変更なし。
限定検索で修復erratumは未発見。外部claimは依然未検証、最小cutは不変。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/desogus-safe-cut-repair.json`](../../../artifacts/experiments/results/desogus-safe-cut-repair.json)
- [`proofs/audits/desogus-computation-and-repair.md`](../../audits/proofs/audits/desogus-computation-and-repair.md)
- [`proofs/audits/desogus-extra-debit-repair.md`](../../audits/proofs/audits/desogus-extra-debit-repair.md)
- [`proofs/audits/desogus-gate2.md`](../../audits/proofs/audits/desogus-gate2.md)
- [`proofs/audits/desogus-gate3.md`](../../audits/proofs/audits/desogus-gate3.md)
- [`proofs/audits/desogus-pivot-cancellation-stress.md`](../../audits/proofs/audits/desogus-pivot-cancellation-stress.md)
- [`research/desogus_dependency.json`](desogus_dependency.json)
