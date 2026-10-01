# 10. 素数の重み付き半空間

**STATUS: RIEMANN HYPOTHESIS OPEN**

記録日：2026-09-30。報告書に記録された日付。個別の開始・終了時刻は復元しない。

## 着想

平方因子なし整数を対数重み制約付きの素数部分集合として表し、偶数個と奇数個の部分集合の間に相殺が強制されるかを調べた。

## 調べたこと

有限差分評価、大素数による正確な分解、Gibbs傾斜、Selberg–Delange族 S_z(X) = Σ_{n≤X} μ²(n)z^{ω(n)} を検査した。μはMöbius関数、ωは異なる素因子の数。

## 残った結果

有限組合せ恒等式は親の重複度と実際の符号を保持する。有理独立な重みでも、一般的な中央二項係数評価は鋭くなり得る。z = −1では S_z = M(X)。逆Gamma因子により局所Selberg–Delange漸近係数はすべて消えるが、これは漸近展開についての主張である。

## 成立しなかったこと・未証明のこと

局所係数の消失は有限Xでのペアリングではなく、残った大域項を評価しない。符号を外した影響度や反集中評価では必要な符号付き共分散を求められない。傾斜からの復元には規格化と共分散項を残す必要がある。

## 次の問いへ進んだ理由

大域的残差を分離し、平滑化した明示公式が何を決めるかを調べた。

## この記録の範囲

局所展開と正確な有限恒等式は保持。固定冪の相殺評価は未取得。

「証明済み」は、リンク先に範囲と前提を記した補助主張を指す。内部AI監査は外部査読ではない。数値・形式化の限界は[再現手順](../reproducibility.md)を参照。新規性・優先権は主張しない。

## 原文と証拠

- [研究原文](../../../archive/reports/research/weighted_prime_halfspace.md)
- [完了報告](../../../archive/reports/research/weighted_prime_halfspace/completion_report.txt)
- [範囲を限定した内部監査](../../../archive/audits/proofs/audits/weighted_prime_halfspace_adversarial.md)
- [当時の状態記録](../../../data/source-records/research/weighted_prime_halfspace_state.json)
- [保存された検証](../../../data/source-records/research/weighted_prime_halfspace/validation.json)

研究原文は翻訳せず保持している。これらは公開用の原文コピーであり、第三者論文のダウンロードではない。[出典](../source-map.md)で状態記録の範囲を、[参考文献](../references.md)で文献と検証の区別を確認できる。

[履歴](../timeline.md)
