**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/desogus-computation-and-repair.md` · Original SHA-256: `d524c32eafda83b02ab9cb1d83ed842f9536cd63b8111bc791582e17c3345f17`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Desogus v2: critical な計算の限定再現と修復試行

2026-09-29。root。対象TeX SHA-256:
`af2f080510ec9dbeef6b2a1616e71f4727165573bccb480e7381e6a17bcbce79`。
外部claimは未検証。著者コードは実行・importしていない。

## 1. 数値の再現と証明上の射程

実装: `experiments/scripts/desogus_targeted_checks.py`。
結果: `experiments/results/desogus-targeted-checks.json`。

Appendix A.3の最終7×7区間行列について、印刷された有限小数を全て厳密有理数へ変換し、
指定された正対角congruence後のGershgorin下界をFractionだけで再計算した。
7行全て正、最小下界は厳密に `>0.5198729787`。本文の値と整合する。
**VALIDATEDは印刷された区間行列の正定値性だけ**。
この行列が実Weil作用素から正確に組み立てられたこと、無限complementの支配、
Y=7の全mode認証はこの計算では独立再現していない。

次にprime-power集合を独自に列挙し、各parent binの定義からVを直接集計した。
著者のlong-double/atanh方式に対し、256bit Arbの直接logを使う。
`k=2,3,7,8,32,33,34,4999,5000` の9点でAWGCとMASTERのscalar量を検査した。
k=2は空集合による厳密等号。その他で必要な正符号を確認した。
k=33では保守的aligned marginは `1.87814156017034755…` で、本文の下界を上回る。
**全整数のsweep、analytic tail、operator liftは未検証**。
scalar数値が正でも、同じ予算が本来の作用素のSchur損失を上回るとはまだ言えない。

GateI covariance theoremは、本文の明示引用を追った範囲で最終inductionの必須nodeではない。
従って146880以上のboxを再実行する前に、GateIIの最小cutを優先した。
atomic polynomialの導関数係数sumは別のFraction計算でC0..C3以下と確認したが、
GateIのglobal theoremを検証済みとはしない。

## 2. Piの符号を消去恒等式から得ることはできない

Lemma6.28の一般モデルで、両区間の長さと乗算係数を1、beta=3/4とする。
旧blockは1/4>0、old-harmonic vectorはx=(3,1)、新Schur pivotは−2。
形式的にQ=D=−2なのでQ−D=0だが、元のcutは負である。
Lemma6.28自体はPi>0を仮定しているため、この例でその補題を反証したとは言わない。
問題はCor6.29のrow equationだけでは、その符号仮定が供給されないことである。

rootによるTeX全文検索では `a_{k,±}` と `beta_k` の算術的な具体式は一般モデルの定義以外に見つからない。
実際のtransportされたWeil blockとの同定とPiの符号を確保する追加証拠が必要。
これは未指定の係数が必ず上の例と等しいという主張ではない。

## 3. 二つのarmの消去と一つのdebitの不一致

Lemma8.4の印刷された二arm形式を独立に平方完成すると

\[
q(x,t_+,t_-)=Q[x]+\langle Pt_+,t_+\rangle+\langle Pt_-,t_-\rangle
+2\Re\langle bx,t_+\rangle+2\Re\langle bx,t_-\rangle
\]

のinfimumは `Q[x]−2||P^(-1/2)bx||²`。
本文も途中でこの2倍を記している。一方最終組立てに渡す残差はQ−D。
同じQを使うなら、前段に一arm消去または+Dが含まれることを明示しない限り同一にならない。

符号の問題とは独立に、**Piが正でも**この差は残る。
I=J=1,beta=1/4ならold pivot=3/4、gamma=1/3、Pi=2/3。
x=(1/3,1)はold-harmonicで、Q=D=2/3、Q−D=0。
literalな二armについてP=b=2/3を取ればt+=t−=−1でinfimumは−2/3。
全値をFractionで再現した。これは印刷された一般代数の不足を示すmodelで、実Weil負方向ではない。

## 4. 最小修復を試した結果

**A. 正のPiだけを追加:** §3の正pivot反例が残る。これだけの修復はFAILED。

**B. unitaryなsymmetric/antisymmetric変換:**
`t_s=(t_++t_-)/sqrt2` にするとcouplingはsqrt2 b、diagonalはP。
Schur debitは依然2 b*P^(-1)b。非unitaryなt+=t−=tでもdiagonal2P、coupling2bで同じ。
従って座標normalizationだけでは修復できない。FAILED。

**C. 各couplingをb/sqrt2へ変更:** 同じP,Qのままなら別の作用素になる。
元のWeil形式からこの係数を導くexact identityが必要。未証明のまま採用不可。

**D. 残るarmは一本だと再定義／pre-Q=post-Q+Dと区別:**
代数的には可能だが、原文の二arm表示とcommon-cut/form transport全体を組み直す必要がある。
同じpositive reserveを重複計上せず成立するかが未解決。

**E. Q−2Dを非負に支配する新しい評価:**
本文の記号なら `Q−2D=E[1−(2−c)u]`。
0<c<1,u=1という正pivotの純ground例で負となるので、一般的なCauchy–Schwarzだけでは得られない。
実Weilのharmonic vectorを追加制限するか、別の未使用reserveが必要である。

この時点で、印刷されたfinal assemblyは独立に検証できていない。
修復は単純な定数訂正・精度改善では済まず、算術的なexact block identityが必要。
他担当のGateII/GateIII監査と照合して最終gap分類を確定する。

## 5. finite safe-cut の技術的修復

`desogus_safe_cut_repair.py` は著者のlong-double branch loopを実行せず、
Arb192のlog、von Mangoldt二乗のprefix sum、floor quotient blockで全7≤k≤4999を独立計算した。
各kでprime-power divisorを除く指定を保持し、全4,993件についてgap>1.5202196525を認証。
Destroyerはアルゴリズムを読み、別の256bit trial-division direct sumで
k=7,8,33,4998,4999を再検査して包含が重なることを確認した。
詳細は `desogus-gate3.md` のfinite repair監査、結果は
`experiments/results/desogus-safe-cut-repair.json`。

分類は **TECHNICAL — FINITE COMPONENT REPAIRED**。
minimum_atは最小lower endpointの位置であり、真のargminの認証と混同しない。
k≥5000の解析tail、有限行列の作用素への同定、RL-kはこの修復の射程外。
この結果をRH証明に合流させない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/desogus-safe-cut-repair.json`](../../../../artifacts/experiments/results/desogus-safe-cut-repair.json)
- [`experiments/results/desogus-targeted-checks.json`](../../../../artifacts/experiments/results/desogus-targeted-checks.json)
- [`experiments/scripts/desogus_targeted_checks.py`](../../../../artifacts/experiments/scripts/desogus_targeted_checks.py)
