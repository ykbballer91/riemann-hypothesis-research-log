**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase4_arithmetic_polarization.md` · Original SHA-256: `bfe256245f976b10c3f5b860be776895205f4e35a8d966fe96711fc32a7e57cc`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# RH Phase IV — Arithmetic Polarization / Positive Pairing

2026-09-29。**RH OPEN。独立トラックの第1巡を完了し、3つのmajor pairing候補後のstrategy reviewで終了。**
Phase IIIの探索・state・active track・既存ファイルは変更していない。
canonical `proof_state.json`、`STATUS.md`、既存主グラフにも書き込んでいない。
Phase IVの内部資料は `research/phase4/`、正準stateは `phase4_state.json`。
追加指示のcontinuous-scale-flow探索も別トラックであり、この記録への自動mergeはしない。

## 1. 何を構成でき、何が残ったか

actual adèle上の自然な正内積とΘ*=1−Θは、自己双対Haar測度とscalingから構成できる。
Arakelov/heightの真正の算術的正性とpolarized endomorphismのadjointも既知定理として存在する。
しかし、それらを全ζ零点を担う同じspaceへ忠実に移すpositive comparisonは得られない。
別々のspace上の成功を合わせて目標を達成したとは扱わない。

今回追加して確かめた限定的障害は、**稠密な算術的radicalを消す非零positive formは、
指定されたambient L²に関して可閉にもできない**というもの。
Phase IIIのbounded Hilbert-completion障害を「非有界なclosed form」で避ける修復も、
同じdomainとarithmetic relationsを保持する限り使えない。
これはRHへのpositive bridgeではなく、候補を絞るnegative knowledgeである。

## 2. 有限体の機能だけを最小化する

|矢印|本当に必要な入力|
|---|---|
|ARITHMETIC ACTION → POSITIVE PAIRING|作用だけからは出ない。同じJacobianのample polarizationという別の幾何入力が必要|
|POSITIVE PAIRING → ADJOINT|忠実な有限次元実表現の正内積、または正のRosati trace代数。無限次元ではdomainが別義務|
|ADJOINT → NORM IDENTITY|同じFrobeniusについてπ†π=q。Frobenius–Verschiebungとbase-field compatibilityを使う|
|NORM → EIGENVALUE MODULUS|非零固有vectorのnormが正なので、abs(α)²||v||²=q||v||²を割れる|
|MODULUS → RH LINE|その忠実表現とzeta determinantの全固有値が一致し、T=q^(−s)と置く|

最後の計算だけなら正definite scaled isometryで十分だが、そのmetricを根から選んではならない。
真の有限体証明は、metricも作用も先に幾何から得ている。
数体で模倣するべきものは名称でなく、この同じ対象上の比較である。
出典：[Milne AV I§14/II§1](https://www.jmilne.org/math/CourseNotes/AV.pdf)。

## 3. 初期portfolioと集中先

最大4候補を初期比較した。AのNéron–Tate、CのDeninger/Hilbert-moduleは同じ候補の比較対象として扱い、
6つの独立な長期ルートを増やしてはいない。

- PV-A：Arakelov/intersectionとheight。finite/infinite placesと符号を固定。
- PV-B：actual explicit formulaのintersection解釈。RH同値の符号条件で初期終了。
- PV-C：actual adelic quotientへのpositive formのdescent。最もactual fidelityが強いため、ここへ集中。
- PV-D：product formula / Fourier / star。独立な積公式ルートとして実際の内積を構成。

比較表と各candidateの必須role cardは `phase4_pairing_matrix.md`。
PV-Bのknown RH criterionを新しいpairing構成として深追いしなかった。

## 4. Major attempt 1 — Arakelovの正性をどのspaceへ移すか

finite divisor D=Σn_p[p]+a∞のdegreeとprincipal divisorを実際に計算すると、
CHhat¹(Spec Z)≅R、degree-zero quotient=0。
Spec Zは絶対次元1なので、算術曲面で使うdivisor×divisorの数値intersectionをそのまま使えない。
この直接候補はspaceとdegreeの時点で終了した。

数体上の曲線のJacobianを別に指定すると、finite intersectionとArchimedean Greenの全局所和が
Néron–Tate heightと結び付く。これは独立なARITHMETIC/GEOMETRIC positivity。
ただしlocal forms個々がPSDではなく、積公式がprincipal divisorsの全和を消すことが重要。
fixed Mordell–Weil spaceは有限次元で、actual ζの全zero spectrumとは未同定。
heightが正という一般論をRH入力として採用しない。

詳細：`phase4/notes/arakelov_height.md`。Gillet–Soulé/Moriwaki/BHMの本文を照合。
Faltings/Hriljacの元版全文は取得できなかったため、未読の定理番号は引用しない。
これは原定理の不成立という判定ではない。

## 5. Major attempt 2 — 積公式から正metricとstarを作る

P(f,g)=∫_A f overline(g)dx、R_af(x)=f(a⁻¹x)を置くと

    P(R_af,R_ag)=|a|P(f,g),  R_a*=|a|R_(a⁻¹).

Q×について|r|=1になるのが積公式の正確な役割。
実scalingのgenerator Θ=−x∞∂x∞、D=Θ−1/2はlog座標で−∂tとなり、
適切なH¹ domainでDはskew-adjoint。従ってΘ*=1−Θはambientで真である。
しかしその連続スペクトルを、ζ零点の離散スペクトルと同一視できない。

Fourierを使うtwist P_F(f,g)=P(f,Fg)を試すと、even subspaceでHermitianだが不定。
h∞=(8u³−30u²+15u)e^(−u)、u=πx²、有限素点は1_(Z_p)として、

    Fh=−h,  h(0)=∫h=0,
    P_F(h,h)=−585/(32√2).

pole-free actual adelic testで負になり、このstar候補は終了。
同じtestのTate integralはZ(h,s)=(2s−1)ξ(s)。Euler/Γを変更したtargetの議論ではない。
正部分への射影で修復する場合、捨てたmodeの完全性を説明できなければ採用しない。
詳細：`phase4/notes/product_formula_star.md`。

## 6. Major attempt 3 — 非有界・可閉な形式ならquotientを保てるか

CCMのtest quotientは全零点を含むが、そのrestriction image V₀は指定weighted H₀に稠密。
非負形式qがV₀を消し、H₀に関してclosableなら、
任意のxをv_j∈V₀で近似したy_j=x−v_jに可閉性を適用してq[x]=0を得る。
従って、このambient normのままでのnonzero positive closed-form修復は不可能。
Hilbert/module上の調和代表への可閉写像も同じ理由で零になる。

ここではpositivityを証明したのではなく、positiveであるとすれば使えないcompletionを特定した。
不定形式、別domain、stronger topologyまで不可能と言っていない。

stronger norm H_k=L²(e^(2k|t|)dt)では、strip内のMellin evaluationと有限jetを連続にできる。
だがnormalized scalingのnormは一般に増減し、unitaryではない。
実際、正半直線内にsupportを持つgをr>0だけ右へ移せばnorm²は正確にe^(2kr)倍になる。
modeの保存と望む随伴の両方を得る算術的理由は未取得。
このnormをRHが真になるよう選んだり、全kでの完全性を仮定したりしない。

positive starを持つDeninger–Singhofの実在する葉層幾何も調べたが、
それをactual arithmetic generatorと同一視する比較定理は別に必要。
詳細：`phase4/notes/adelic_descent.md`。

## 7. 追加の即時gate

1. actual explicit formulaのpole/degreeを消しても、その全面的符号はRH同値。
   q=9 syntheticではdegree/co-degreeを消した対応Rのstar traceまで−486になる。
2. JΘJ⁻¹=1−Θ*はΘ*=1−Θと同値ではない。標準正内積の2×2線外反例を保存。
3. literal Θ⁻¹=1−Θは二固有値だけを許し、actual ζの全零点を回収できない。
4. PSDのradical quotientがmultiplicityを保持するとは限らない。
   jet algebra C[ε]/ε^mではtrace formがPSDでもradical quotientは1次元となる。
   実際の算術moduleが必ずこのmodelだとは仮定していない。

## 8. Strategy review / success level

指定の3 major pairing候補が失敗し、actual zero-bearing spaceへの独立なpositive descentは得られなかった。
この時点でレビューを行い、同じmissing positivityの4度目の呼称変更を開始しない。
Weil positivityの再定義、未知のHodge starの仮定、局所PSDから全域への飛躍は採用していない。

**Phase IVの到達レベルは0。** ambient正metricとadjointの実在は有効だが、
要求されたactual zero-bearing spaceへのnew bridgeではない。
Level1–5を別対象上の既知定理の寄せ集めで達成したことにしない。
RH OPEN、独立なpositive bridgeなし、主グラフへのmergeなし、未証明追加前提なし。
未知の別polarizationや算術幾何program全般を否定したわけではない。

再開に必要な具体内容は、算術cycle/Green/Hodge dataから定義され、
旧test quotientと全local terms・全multiplicityを保つ、独立なpositive comparison。
当該L²へ可閉に移す案は再採用しない。新metricを単に「自然」と命名するだけでも不十分。

## 9. 検証と独立性

BUILDER / LITERATURE / DESTROYERの別担当による原典照合と計算監査を実施。
正準監査：`../proofs/audits/phase4_pairing_adversarial.md`。
exact Fractionの検算と非認証mpmath診断は `phase4/experiments/pairing_checks.json`。
新しいproof-critical positive bridgeがないため、一般理論の大量Lean形式化は行っていない。

Phase III保全baselineと照合結果は `phase4/phase3_preservation_baseline.json` および
`phase4/preservation_check.json` に保存。Phase IVのstateは独立の `phase4_state.json`。
新しいcontinuous-scale-flowトラックの結果は別ログへ保存し、ここからPhase IIIを操作しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/phase4_pairing_adversarial.md`](../../audits/proofs/audits/phase4_pairing_adversarial.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/pairing_checks.json` — SOURCE REFERENCE NOT INCLUDED
- `research/phase4` — SOURCE REFERENCE NOT INCLUDED
