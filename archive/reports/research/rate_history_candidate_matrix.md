**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/rate_history_candidate_matrix.md` · Original SHA-256: `ceaf4c52c9b61c23aef69c74b42a5143f81915e541b74c0b2216cbe576120e9a`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Rate/history candidate matrix

2026-09-30。RH OPEN。限定三方向、旧成果へのmergeなし。

|項目|Track A: rate / splitting|Track B: history / projector|Track C: canonical probability gate|
|---|---|---|---|
|actual object|Q、canonical projected k derivatives、M/G|同じQの全ground spectral projector|Qに既に付随するspectral measure候補|
|実行|11endpoint×m1,2,3、二経路、全M/G・overlap|prime-power event解析、次元増加、元log空間でpath比較|PVM・counting measure・heat stateの前件監査|
|解析的に得たもの|support主漸近、rank-one境界形式、境界消去例、full projected recognition上界|prime eventの連続性とrank-one derivative corner、fixed-m Gram収束|scalar measureにはvector、heat stateにはscaleが要ること|
|認識rate|支持だけでは異なるpolynomial prefactors。全射影では両経路でM→0を証明|Gram収束とenergy選択は別|未導入|
|一意な選択|support-onlyのR1内最低方向→kは証明。full P_N系は未取得|同じ単純有限endpointは履歴を持たない。無限path limitは未同定|算術から追加のcanonical selectorなし|
|反証gate|G無視、absolute Qとground混同、fixed-a rateのjoint流用、restricted gapの誤用|有限endpoint差をhysteresis扱い、追跡規約を定理扱い、座標集中を消滅扱い|任意Gibbs/entropy/metricによる後付け|
|残る具体的義務|actual full whitened next-order matrixのscale・remainder・simple minimum、補空間coupling|二つのlimitの存在と同一性/相違、full-gap control|追加データなしのstate-selecting arithmetic measure|
|判断|rateに関する部分解析成果あり、full selectorなし|有限path診断あり、history-dependent selectionなし|入口で終了。確率モデルを作らない|

## 正確な到達度

- Level 1：actual finite splittingを固定。
- 支持切断だけにはLevel 2型の異なる主漸近を証明。
- 二候補R1のsupport-only最低方向→kと、そのrestricted gapの主漸近も証明。
- 全P_N系でも認識の無条件上界を証明したが、異なる状態の最適leading rateは未同定。
- full canonical系でのLevel 3–5（unique selector、actual full ground convergence、G*/RH）は未達。支持切断だけの二候補についての限定選択定理とは区別する。
- known inputと本監査の導出を分け、新規性は主張しない。

次次数を無限に追加せず三方向で停止。
再開にはfull next-order formの具体的な同定・一意性・remainderを与える独立入力が必要。
これを新仮定として採用しない。

full canonical support-plus-Fourier系について：
**NO FINITE-SCALE SELECTION PRINCIPLE IDENTIFIED.**
