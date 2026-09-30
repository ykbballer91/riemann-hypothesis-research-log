**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/prime_complex_adversarial.md` · Original SHA-256: `c52322a013b8a5ab3c7d42d59731465f78780742c66d9767010ccb13c8e287ef`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Prime complex parity pairing — adversarial audit

2026-09-30。RH OPEN。主担当、builder、destroyer、文献担当による限定監査。
既知結果を新規発見として扱わない。

**採用する事実:** exact toggle2 matching、linear residual、integral filtered chain
decomposition、barcode [n,2n)、doubling null homotopy、任意incidence matchingの孤立点障害。
**採用しない結論:** square-root residual、small harmonic kernel、RH、nonlocal pairing
全般の不可能性。

## 独立検証の範囲

[matching_persistence.md](../../../reports/research/prime_complex/notes/matching_persistence.md) に
builderの整数鎖分解、[independent_audit.md](../../research/prime_complex/notes/independent_audit.md)
にdestroyerのcone-collapseと量的障害、[literature.md](../../../reports/research/prime_complex/notes/literature.md)
に指定原文のlocatorを保存した。rootが記号・次数・範囲を照合した。

| Claim / gate | 結果 | 根拠または限定 |
|---|---|---|
| M=−reduced Euler | PASS | face dimension=omega−1、empty face込み |
| ordinary Euler=1−M | PASS | augmented contribution−1を除く |
| toggle2 involution and cutoff | PASS | odd m<=X/2 と2mが一意に対応 |
| acyclic matching | PASS | 2追加後の下向き2削除は不可能 |
| naive smallest admissible toggle | FAIL | X=5: 3->1->2 |
| all fixed primes give perfect matching | FAIL | p=3,X=10: critical3、reducedBetti1 |
| critical faces exactly U_X | PASS | odd sf X/2<n<=X |
| total Betti=cardinality U_X | PASS | star(2) collapse、整数chain basisの二つの証明 |
| total Betti asymptotic | PASS | 2X/pi²+O(sqrt X)、mu² identityで初等証明 |
| reduced barcode [n,2n) | PASS | filtrationを両方向に保つ整数unimodular基底変換 |
| finite bars imply small current homology | FAIL | 全log寿命log2なのにalive count Theta(X) |
| positive Hodge pairing implies small kernel | FAIL | kernel次元は全Betti数でmetric不変 |
| unimodular basis change gives unitary spectrum | FAIL | chain equivalenceはorthogonal equivalenceではない |
| p>sqrt X uniqueness gives injective parent map | FAIL | p=3,5 atX=5が双方parent1へ |
| any incidence matching has polynomial saving | FAIL | 孤立prime singleton lower bound ≫X/logX |
| recursive prime link is always full Delta_{X/p} | FAIL | 一般pではpを除いたD_p(X/p)が正しい |
| local divisor cancellation is destroyed for n<=X | FAIL | nの全divisorsも<=X、identityは保持される |
| local identities sum directly to M | FAIL | floor(X/d)のoverlap multiplicityが付く |
| arbitrary homology parity re-pairing gives new bound | FAIL | 順位でpairすればresidual=abs(M)、未解決量の再定義 |

## 三種類の「小さい」を混同しない

1. signed residual sum は M(X)。これが小さいという主張は目的そのもの。
2. toggle2 critical数、全 reduced Betti数、Hodge kernel総次元はTheta(X)。小さくない。
3. filtrationの各barのlog長はlog2。短いが、その時点のbar個数を制御しない。

従って普通のMorse/Hodge枠組みでは、線形個の偶奇homologyの差を別の算術mapで制御する
必要がある。そのような独立なmapと評価は今回得ていない。

## Exact finite experiments

実行script: [check_complex.py](../../../../artifacts/research/prime_complex/experiments/check_complex.py)
結果: [results.json](../../../../artifacts/research/prime_complex/experiments/results.json)

- 12個のcutoff標本、最大X=10000。全squarefree faceとtoggle2 pairsを整数列挙し、
  acyclicity、未対応集合、符号和、birth/deathを検査。
- 10個の小cutoffでactual boundary matricesを有理数上でrank計算。d²=0を検査し、
  Betti公式と一致。小例の自然Laplacian kernelもexact rational rankで一致。
- cutoff1000の標準F_2 persistence matrix reduction。204本のcompleted intervalsが
  すべて[n,2n)と一致。未完了intervalはU_1000の200本と一致。
- X<=210の標本で最大bipartite incidence matchingも計算。
  X=15では未対応1が可能だが有向cycleを持ち、Morseの最小critical3と矛盾しない。
- X=100のcritical recordsはn、prime factors、parity、largest prime、birth、deathを保存。
- finite prime sets、modified weights、固定seedのprime-weight perturbationsを検査。
  同じmin-vertex構造が成立するので、その構造だけではactual primesに固有でない。
- equal-weight8vertices・cutoff4ではsigned residual=−7。これはactual zetaの反例ではなく、
  generic topological structureだけの十分性を壊す模型。
- all-integerへの無断置換、X=15のflag completion、smallest-toggleの非involutionを反証。

数値fit、random-sign仮説、大規模Mertens探索は使用しない。有限計算から全Xの漸近を
推測していない。全Xの結論は別記した証明から得ている。

## 既知性と精度の監査

Björner 1101.5704v1 のEuler/Betti/wedge/linear総数は既知として登録。
Knill 1608.06877v1 はdivisibility order complexの別表現として照合。
Forman のweak Morse inequalitiesはcritical数の下界に使う標準結果であり、今回の
新しいRH補題ではない。barcodeのdirectproofも新規性を主張しない。

原文中の普通/reduced規約や孤立した符号表記を盲目的に転記せず、素数一個とempty face
で検算した。こちらの全式はM=−reduced Euler、cardinality supertrace=Mに統一した。

## Dyadicへの接続・kill decision

独立に得た絶対値上界はO(X)、theta=1。以前のtheta<1という仮定を満たさないため、
条件付き2^((theta−1/2)n)評価へ端点代入しない。以前の無条件
2^(n/2)(1+n) p_4(g)を改善していない。旧dyadic研究ログは変更しない。

3主要構成の後、linear critical-count / kernel-count と共有parentのkill条件で終了。
新規proof-critical bridgeなし、graph merge 0、RH OPEN。
形式化はLeanでは実施せず、整数鎖の解析証明とexact finite algebraを区別して記録した。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/prime_complex/experiments/check_complex.py`](../../../../artifacts/research/prime_complex/experiments/check_complex.py)
- [`research/prime_complex/experiments/results.json`](../../../../artifacts/research/prime_complex/experiments/results.json)
- [`research/prime_complex/notes/independent_audit.md`](../../research/prime_complex/notes/independent_audit.md)
- [`research/prime_complex/notes/literature.md`](../../../reports/research/prime_complex/notes/literature.md)
- [`research/prime_complex/notes/matching_persistence.md`](../../../reports/research/prime_complex/notes/matching_persistence.md)
