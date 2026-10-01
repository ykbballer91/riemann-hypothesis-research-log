# 11. 局所漸近展開の全次数を越える大域残差

**STATUS: RIEMANN HYPOTHESIS OPEN**

記録日：2026-09-30。報告書に記録された日付。個別の開始・終了時刻は復元しない。

## 着想

局所漸近展開の全係数が消えてもMöbius和はどこに残るのか。固定Gaussian観測で、局所展開と大域特異点を分けた。

## 調べたこと

R(u) = Σ μ(n)e^{−(u−log n)²} の変換は、Re s > 1で絶対収束により √π e^{s²/4}/ζ(s)。高さごとの群分けと重複度を明記して積分路移動を確認した。

## 残った結果

有限回の左移動では、制御された群別留数表示を得る。零点ごとの任意の並べ替えや絶対収束は主張しない。この固定観測で A(u) = e^{−u/2}R(u) の前向き劣指数成長はRH同値。有限ジェット模型は、有限局所データが大域的な極を見落とし得ることを示す。

## 成立しなかったこと・未証明のこと

無限の左移動と無制限の自明零点級数は収束条件を満たさない。完全な解析的な芽は連結な有理型解析接続を決めるため、全Taylor係数を保ったまま変更できない。Selberg–Delange係数の消失と1/ζのTaylor係数の消失は異なる。

## 次の問いへ進んだ理由

新しい構成を止め、実際の算術評価と各点評価の不足を棚卸しした。

## この記録の範囲

正確な変換と有限移動は保持。目標の成長評価はRH同値のまま。

「証明済み」は、リンク先に範囲と前提を記した補助主張を指す。内部AI監査は外部査読ではない。数値・形式化の限界は[再現手順](../reproducibility.md)を参照。新規性・優先権は主張しない。

## 原文と証拠

- [研究原文](../../../archive/reports/research/global_remainder_beyond_all_orders.md)
- [完了報告](../../../archive/reports/research/global_remainder/completion_report.txt)
- [範囲を限定した内部監査](../../../archive/audits/proofs/audits/global_remainder_adversarial.md)
- [当時の状態記録](../../../data/source-records/research/global_remainder_state.json)
- [保存された検証](../../../data/source-records/research/global_remainder/validation.json)

研究原文は翻訳せず保持している。これらは公開用の原文コピーであり、第三者論文のダウンロードではない。[出典](../source-map.md)で状態記録の範囲を、[参考文献](../references.md)で文献と検証の区別を確認できる。

[履歴](../timeline.md)
