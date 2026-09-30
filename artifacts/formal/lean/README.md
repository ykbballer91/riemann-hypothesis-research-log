**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `formal/lean/README.md` · Original SHA-256: `28a7161795d541c5a472a71d4131c5a3b854b9f243d31cfe5ea9658be1c223bc`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 形式検証の範囲

Lean 4.19.0 と Mathlib v4.19.0 をこのディレクトリに構築し、`RhAudit.lean` を実行検証した。
Mathlib commit: `c44e0c8ee63ca166450922a373c7409c5d26b00b`。
依存の厳密な版は `lake-manifest.json` に保存。

検証対象は8宣言。

1. `nonneg_of_pointwise_limit`: 非負な実数値形式が各ベクトルで収束すると、その極限も非負。
2. `nonneg_of_vanishing_lower_error`: 各点で消える下側誤差がある場合の同じ結論。
3. `nonneg_on_dense`: 指定した位相に対して連続な実数値写像が稠密集合上で非負なら全体で非負。
4. `coordinate_restrictions_nonneg`: 2変数形式の座標軸への制限は非負。
5. `larger_block_negative`: 同じ形式が (1,-1) で −2。
6. `quartet_coefficient`: 軸外四重点反例の有理数係数 −15/8。
7. `two_block_lower_bound`: μ,δ≥ell+ε、ε≥0なら二blockの結合を含む実二次式がell(x²+y²)以上。
8. `scalar_schur_equivalence`: a>0なら、全実数x,yに対するax²+2bxy+cy²の非負性とc−b²/a≥0は同値。

`verification/build.txt` と `verification/axioms.txt` を保存。
8宣言の axiom 出力は `[propext, Classical.choice, Quot.sound]` であり、
`sorryAx`、独自の RH 公理、未証明の補題を使っていない。

**これは RH の形式検証ではない。** ξ、零点計数、Weil criterion、strip decay の解析証明、
bump族の稠密性、積分で与えられる四重点反例、kernel最適化はまだ形式化していない。
連続性・稠密性・点ごとの収束を明示した抽象補題を検証したのであり、
Weil形式がそれらの仮定を満たすという解析的証明まではLeanへ移していない。
現時点で未形式化なのは作業範囲の問題で、ライブラリ不足と断定したものではない。
固定窓のArb証明書・特殊関数・求積・無限tailもLeanには移していない。
7番目はblock結合の下界、8番目は実数のSchur必要十分条件という有限次元の代数だけを形式化したもの。
8番目は無限次元逆作用素の定義域、supportの拡張、Weil形式の正値性を主張していない。

## 再現

通常の elan がある環境で、このディレクトリから実行:

```sh
lake update
lake exe cache get
lake build
lake env lean RhAudit.lean
```

このワークスペースだけに導入した環境なら:

```sh
export ELAN_HOME="$PWD/.elan"
export PATH="$ELAN_HOME/bin:$PATH"
lake build
lake env lean RhAudit.lean
```

`.elan/` と `.lake/` は再取得可能な依存物として Git / 公開用checkpointに含めない。
