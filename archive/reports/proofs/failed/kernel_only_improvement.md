**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/failed/kernel_only_improvement.md` · Original SHA-256: `679e3a37f605f86965749cc83d9dc34c7cc5fa692e529e020c70559c5834a36a`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 核交換だけによる完全証明候補の棄却

Hypothesis: Lamzouri型の固定support・同じ二次モーメント評価・同じ下界式を保ち、核ηを最適化すれば得られる割合下界を1にできる。

Why plausible: 自由な滑らかな試験関数を最適化でき、有限行列探索にも適している。

Test performed: 対応するL²制約付き汎関数を解析的に最小化し、文献の既知最適値と照合。

Counterexample / failure: 最小値C_MT=1/2+cot(1/√2)/√2>1であり、同じ下界式の右辺は2−C_MT<1に制限される。
厳密なgapは C(f)−C(f0)≥(2/3)||f−f0||²。数値最適化に依存しない。

Can it be repaired?: 同じクラスの核交換では不可。support範囲、モーメント情報、または推論自体を変更する必要がある。それが可能だという証明はない。

Final status: FALSE（上記の限定候補）。他手法、実際の零点割合、RHの否定を意味しない。

Newness: 既知の最適定数の再導出。新規成果とは扱わない。
