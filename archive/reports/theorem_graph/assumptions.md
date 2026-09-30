**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `theorem_graph/assumptions.md` · Original SHA-256: `e4c67ff58f6a5003ec115f7d601c0fcc54709f709dcbeaed6cf42264b746bb36`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 仮定と禁止された推論

この研究で RH、単純零点仮説、全零点の実部既知、全窓正値性を仮定した無条件定理はない。

## 既知の解析的入力

- ξ の整関数延長、実型性、関数等式。非自明零点は重複度込みで扱う。
- 非自明零点は 0<Re(ρ)<1。対称写像 ρ↦1−bar(ρ) は重複度を保つ。
- Riemann–von Mangoldt の零点計数から N_*(T)=O(T log(T+2))。
- Weil の全 C_c∞ テスト関数に対する非負性と RH の同値性。

これらは出典付き KNOWN とし、今回ゼロから証明したとはしない。
引用の版・定理条件の検証状況は literature/ledger.md と各ノートに記録。
同値定理を既知とすることは、同値な正値性命題を証明済みにすることではない。

## 今回の補題で使う解析

固定 support 上の部分積分、Cauchy–Schwarz、絶対収束の優級数判定、
非負実数列の極限の非負性、mollification と Riemann 和。
形式化がこれらの全実装を含むとは限らない。形式化の範囲は formal/lean/README.md に限定。

## 禁止する飛躍

- L² 稠密性を、非有界形式の form topology の稠密性と混同する。
- 有限個の正固有値を全次元の証明にする。
- 自己共役性・下に有界であることを非負性と同一視する。
- 虚部のみのスペクトルを全複素零点の同定と呼ぶ。
- 点ごとの Euler 積の一致を臨界帯の局所一様収束と呼ぶ。
- 2026年プレプリントの定理を、原稿が存在するというだけで独立検証済みと呼ぶ。

RHまでの「未解決ノード1個」という表現は、RH同値な命題へまとめただけなら
技術的距離を縮めたことを意味しない。すべての状態表示でこの点を維持する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`formal/lean/README.md`](../../../artifacts/formal/lean/README.md)
- [`literature/ledger.md`](../../literature/literature/ledger.md)
