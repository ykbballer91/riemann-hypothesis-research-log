**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/common_parent_candidate_matrix.md` · Original SHA-256: `416cf929f1be858b5e1d0502eeca3dee6349a148fe866d793c4e721f4b6723fb`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Common-parent candidate matrix

2026-09-30。RH OPEN。最大三試行で限定監査を終了。

|要件 / 機構|A Common Rayleigh|B Common parent / Γ-limit|C Common Euler equation|
|---|---|---|---|
|actual入力|Weil prime/Gamma/pole matrix、raw prolate proxy|算術和S、Weil形式、concentration C|prolate PW、有限Q、S|
|exact object|projected normalized b、R、excess、full gap|pullback Q(Sh)/‖Sh‖²|S*QS h=μS*S h と二つのprolate mode|
|無条件に得たもの|有限代入、標準gap/residual補題|Sのkernel、単純leakage identityの反証|0/4 mixtureはC/PWの単一固有vectorでない|
|独立算術入力か|行列とproxyはyes。極限評価は未取得|写像はyes。新しいparentはno|既知式はyes。共通limitは未取得|
|既知の共通接続|global算術和像はWeil radical|同じ。ただし無限次元で一意性なし|kernel limitのFourier transformはXiの定数倍|
|最重要不足|excess/gapのrate、projection tail、ES|equi-coercivity、unique選択、共通objective|intertwining、定量誤差、共通極限方程式|
|反証gate|低energy・小residual・可換性だけでは不足|kernel上でaffine leakage表示破綻、Moscoだけでground逃走|Cがker Sを保たず自然なdescent不可|
|数値の役割|診断のみ。小gapは高精度で再計算|数値なし|seed特性の実装照合のみ|
|停止理由|必要rateを証明できず、有限overlapでは不足|Aを再表現しただけのparentは不採用|似たeigen equation以上の同一性なし|

## Type別判定

- Type I：指定Bは通常concentrationのmean-zero最適解でもない。両者を選ぶ共通目的量は未取得。
- Type II：canonical Sは非等長でkernelあり。AのpullbackだけではBを選べない。
- Type III：Fourier/Mellin/traceのdualityは既知。objectiveのprimal/dual同一性は未証明。
- Type IV：common Γ/Mosco limitを構成していない。自然な大域Weil候補はunique minimizerを持たない。

## 到達度と停止

Level 1：actual A/B辞書、有限Step31、比較のexact十分評価、明示的no-goを固定。
Level 2以上の算術的almost-minimizer theoremはない。
「全ての未知parentが存在しない」とは主張しない。
既知radical関係を新規発見と呼ばない。

**NO COMMON PARENT IDENTIFIED.**
