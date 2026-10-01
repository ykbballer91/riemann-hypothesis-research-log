# 14. 局所から大域への零点拘束

**STATUS: RIEMANN HYPOTHESIS OPEN**

記録日：2026-09-30。報告書に記録された日付。個別の開始・終了時刻は復元しない。

## 着想

局所的・制約付きの変換で実零点性が成立する例から、Xiへその性質を移すために正確に何を収束させる必要があるかを調べた。

## 調べたこと

Hermite–Mellin定理、局所体、有限補正因子付き完備変換、半局所Sonin安定性、有限Weil最低状態の構成を比較した。

## 残った結果

実零点定理には指定されたベクトル、正値性、支持、直交性の前提がある。ζを因子に持つ完備変換から、正則な補正で軸外ゼータ零点を取り除くことはできない。実際の有限Weil最低状態の実零点性には偶性・単純性ESが必要であり、変換がXiの定数倍へ局所収束するプロレート近似とは別の族として保持した。

## 成立しなかったこと・未証明のこと

値で規格化した真の最低状態と近似を同定する定理はない。不足するG*は、必要な最低状態の前提とともに、帯域 |Im z| < 1/2 のコンパクト集合上で変換を比較する条件。合わせた判定は十分条件であり、RHからG*への逆は示していない。

## 次の問いへ進んだ理由

実際のエネルギー恒等式、残差、固有値差が比較を与えるかを共通変分原理の調査で検査した。

## この記録の範囲

局所定理と近似の収束は保持。大域への橋は未解決。

「証明済み」は、リンク先に範囲と前提を記した補助主張を指す。内部AI監査は外部査読ではない。数値・形式化の限界は[再現手順](../reproducibility.md)を参照。新規性・優先権は主張しない。

## 原文と証拠

- [研究原文](../../../archive/reports/research/local_to_global_zero_confinement.md)
- [完了報告](../../../archive/reports/research/local_to_global/completion_report.txt)
- [範囲を限定した内部監査](../../../archive/audits/proofs/audits/local_global_zero_confinement_adversarial.md)
- [当時の状態記録](../../../data/source-records/research/local_global_state.json)
- [保存された検証](../../../data/source-records/research/local_to_global/validation.json)

研究原文は翻訳せず保持している。これらは公開用の原文コピーであり、第三者論文のダウンロードではない。[出典](../source-map.md)で状態記録の範囲を、[参考文献](../references.md)で文献と検証の区別を確認できる。

[履歴](../timeline.md)
