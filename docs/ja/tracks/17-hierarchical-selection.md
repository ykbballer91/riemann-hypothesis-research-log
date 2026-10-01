# 17. 固定微分族での階層的選択

**STATUS: RIEMANN HYPOTHESIS OPEN**

記録日：2026-09-30。報告書に記録された日付。個別の開始・終了時刻は復元しない。

## 着想

先頭境界エネルギーが縮退した後、後続項が F_m = span{k,k″,…,k⁽²ᵐ⁾} 内でkを選ぶかを調べた。操作順は実際の P_N R_a。

## 調べたこと

固定mの支持漸近、Gram行列、Fourier解像と境界尺度を比較し、素数の階数1摂動とSoninフィルターも別に監査した。

## 残った結果

各固定有限mについて、支持制限後の最低固有値は十分先で単純となり、規格化した最小化方向は k/‖k‖ へ収束する。記録された先頭項は a(m!)²Y^(7/2−2m)e^(−2Y)/(√π‖k‖²)、Y = πe^(2a)。同じ制限族の選択は liminf N/(aY) > 4/π² のもとで P_N R_a 後も成立する。これは十分条件であり、必要性・最適性は未証明。素数イベントの微分は階数1で記述できるが、有限更新は正とは限らない。Sonin/Gamma対応はその空間では正確だが、現在のエネルギーを別の選択問題へ移すものではない。

## 成立しなかったこと・未証明のこと

定数と誤差はmの増大に一様でなく、有限行列全体の補空間は制御できない。全体の最低状態の偶性・単純性とG*は未取得。制限族の選択は全体の最低状態の捕捉ではない。

## 次の問いへ進んだ理由

別の日付付き更新で、微分族の合併が偶L²で稠密かだけを調べた。その更新では後続の全体捕捉に進んでいない。

## この記録の範囲

記載領域で固定有限mの階層を確立。全体の最低状態、増大するm、RHは未解決。

「証明済み」は、リンク先に範囲と前提を記した補助主張を指す。内部AI監査は外部査読ではない。数値・形式化の限界は[再現手順](../reproducibility.md)を参照。新規性・優先権は主張しない。

## 原文と証拠

- [研究原文](../../../archive/reports/research/hierarchical_selection.md)
- [完了報告](../../../archive/reports/research/hierarchical_selection/final_report_ja.txt)
- [範囲を限定した内部監査](../../../archive/audits/proofs/audits/hierarchical_selection_adversarial.md)
- [当時の状態記録](../../../data/source-records/research/hierarchical_selection_state.json)
- [保存された検証](../../../data/source-records/research/hierarchical_selection/validation.json)

研究原文は翻訳せず保持している。これらは公開用の原文コピーであり、第三者論文のダウンロードではない。[出典](../source-map.md)で状態記録の範囲を、[参考文献](../references.md)で文献と検証の区別を確認できる。

[履歴](../timeline.md)
