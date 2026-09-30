**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/joint-symbol-certificate.md` · Original SHA-256: `3444b98e1d189d17bc59b0b69db9aa78774bdfb95074e35df5acff291025dba0`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Joint symbol の高周波下界 — 5固定窓の区間証明書

2026-09-29、checkpoint04。**高周波 symbol の下界だけを認証。全 Weil 正値性・RH は証明していない。**
方法は [Zhu v2 §7・§16](https://arxiv.org/html/2608.24827v2) に先行提案があり、新規性を主張しない。
原著コードや零点表を使わない具体実装と、限定された数値定数の独立認証として保存する。

## 命題と解析的接続

規約は [joint-symbol-reduction.md](joint-symbol-reduction.md)。
`h(t)=Re psi(1/4+it/2)−log(pi)`、
`P_a(t)=Σ_(log n<2a) 2Λ(n)n^(-1/2) cos(t log n)`、`Psi_a=h−P_a` とする。
次の各行について、全 `|t|≥T` で **`Psi_a(t)>1/5`** が成立する。

|a|認証したT|有限認証の終端U|定数combの零floor目安 T₁=2πexp(A_a)|区間数|
|---|---:|---:|---:|---:|
|4/5|111|148|約119.09|39|
|1|1552|2674|約2187.13|1153|
|119/100|5549|9074|約7427.04|3580|
|6/5|21231|38520|約31535.46|17444|
|7/5|132510|225986|約185020.05|93779|

各 `a` は表の有理数そのもの。小数を近似的な窓境界として扱わない。
表の T₁ は比較用の近似値で、正の `1/5` floor を定数combだけで保証する cutoff はさらに大きい。
この表が各窓の最小可能な T であるとは主張しない。

既存の [固定窓還元](fixed-window-reduction.md) で独立導出した
`h(t)≥log(t/(2π))−1/t` を用い、実装はむしろ強い補助命題

```text
g_a(t):=log(t/(2π))−1/t−P_a(t)>1/5  (T≤t≤U)
```

を証明する。`A_a=Σ2Λ(n)/√n` とし、各Uでは
`b_a(U):=log(U/(2π))−1/U−A_a>1/5` もArbで確認する。
`b_a'(t)=1/t+1/t²>0` と `P_a≤A_a` より `t≥U` 全体も覆われる。
偶性で負の周波数へ移す。無限tailを有限gridの成功で置き換えていない。

## 実装・証明書・再現

- 生成器: `experiments/scripts/joint_symbol_certificate.py`。
- 保存証明書: `experiments/results/joint-symbol-tail-certificates.json`。
- python-flint0.9.0、Arb160bitで生成。224bitで全115,995区間を再検査。
- BUILDERは生成器をimportせず、整数因数分解でprime powersを再列挙し、224bitで全区間を別に再評価。
- DESTROYERは静的監査、別の小窓改善例、resolution-height仮説の反証を担当。

```sh
.venv-cert/bin/python experiments/scripts/joint_symbol_certificate.py
.venv-cert/bin/python experiments/scripts/joint_symbol_certificate.py \
  --verify experiments/results/joint-symbol-tail-certificates.json --bits 224
```

`python -O` を使わない。認証義務は `assert` で強制される。
保存coverの `[d,c]` は、直前の端点から幅 `2^(-d)` の閉区間がc個連続する意味。
始点Tからの有理数加算で終点Uと一致することを確認するため、隙間・格子丸めはない。
各区間全体をArb ballに含め、log・cos・四則演算をoutward roundingで評価する。
有限区間の最小の認証余裕はどの行も正で、最も小さい行でも `2.76e-4` より大きい。
境界が厳密に判定できないprime powerは採用・除外を推測せず停止する。
floatは候補Uと列挙上限の選択にだけ使い、最後にArb不等式で安全性を再確認する。

信頼基盤はPython実行、python-flint/FLINT/Arbの包含演算、保存した解析的digamma下界。
この証明書はLean未形式化。同じライブラリを使う別実装・別精度の一致を、別の数学ライブラリによる完全独立認証とは呼ばない。

## 残る条件と棄却した近道

このfloorから `R_(T,1/5)≤Q_a` は従うが、Rのheadが正という前提は得られていない。
低周波のsigned symbol・負のodd pole・head-tail結合を別に認証する必要がある。
主グラフにはこの数値表を全窓正値性への矢印として追加しない。

`T*(a)=2πexp(2a)` 以後はPsiが非負という候補は、上の5窓すべてで厳密負点と負近傍があり棄却。
詳しくは [joint-symbol-adversarial.md](joint-symbol-adversarial.md)。
これはPsiという補助symbolの反例であって、Q_aの負方向やRH反例ではない。

大きいaでの一様cutoff bound、prime cancellationの明示一様定数、全窓でのhead正値性は未取得。
今回の結果を「定数comb法の障壁が全て解消した」または「全窓で効率的」と解釈しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/joint-symbol-tail-certificates.json`](../../../../artifacts/experiments/results/joint-symbol-tail-certificates.json)
- [`experiments/scripts/joint_symbol_certificate.py`](../../../../artifacts/experiments/scripts/joint_symbol_certificate.py)
- [`proofs/audits/fixed-window-reduction.md`](fixed-window-reduction.md)
- [`proofs/audits/joint-symbol-adversarial.md`](joint-symbol-adversarial.md)
- [`proofs/audits/joint-symbol-reduction.md`](joint-symbol-reduction.md)
