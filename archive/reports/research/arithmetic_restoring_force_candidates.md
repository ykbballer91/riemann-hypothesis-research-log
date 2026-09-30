**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_restoring_force_candidates.md` · Original SHA-256: `d7a8e4763e65ce6ee66bdb3ee69c061fe26caf036dffd0d28fb460a1584f2b50`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Restoring Force — 三候補の比較

2026-09-30。RH OPEN。全候補の「成功」は、局所的な真の符号が一つあることではなく、actual arithmeticから全零点を拘束する独立入力が得られることを指す。

| 候補 | actual arithmetic input | 正確に得たもの | 反証／既知性／不足 | RH同値か | 判定 |
|---|---|---|---|---|---|
| A1 \(V=\log|\xi|\) の \(a\partial_\sigma V>0\) | completed Euler/Gamma/pole、actual theta | 領域外・実軸で既知符号、全域lawから零点排除する局所lemma | 全域lawはSondow–Dumitrescu型水平monotonicity。独立証明なし | 全域版YES | STOP_EQUIVALENT |
| A2 \(V=-\log|\xi|\) | 同じactual completed ξ | 実軸 \(t=0\) の正theta表示 | \(a>0\) で \(\partial_a\log\xi>0\)、符号反転potentialは外向き | 単純lawは偽 | REJECT_COUNTEREXAMPLE |
| A3 prime-only force | absolute Euler product、σ>1 | \(-\sum\Lambda(n)n^{-\sigma}\cos(t\log n)\) | 同じσで正負の厳密例。critical stripで級数の流用不可 | なし | REJECT_SIGN_INDEFINITE |
| A4 global log-convexity | actual ξ | ゼロ近傍Laurent展開 | actual critical-line零点の近くで曲率 \(-m/a^2+O(1)<0\) | 偽 | REJECT_COUNTEREXAMPLE |
| A5 center curvature / local minimum | actual \(F(t)=\xi(1/2+it)\) | \(\kappa=(F'^2-FF'')/F^2\)、t=0で正 | 全center regular点でκ>0でもoff-axis quartetを持つorder1模型 | 一次不等式だけの同値は主張しない | REJECT_INSUFFICIENT |
| A6 \(|\xi|^2\) の全水平凸性 | completed ξ | log凸性と異なるJensen/Pólya型条件 | 未証明の全域符号を名前変更しただけ | YES | STOP_EQUIVALENT |
| B1 cosh/cos・sinh/sin二条件 | actual全整数theta kernel | \(\xi(1/2+a+it)=U+iJ\)、\(U=J=0\) | 旧modular-generator D4と同じ。oscillatory signsを制御できない | 全a≠0同時消滅禁止はYES | STOP_PRIOR_OVERLAP |
| B2 正性・shape / universal factors | actual Φ>0、既知厳密凹性 | 無条件のshapeは実在 | 同じ一般条件を満たすoff-real-zero核あり。universal-factor定理は元のreal zerosを仮定 | 強化してLPを置けばYES | REJECT_GENERIC_INFERENCE |
| B3 standard Toeplitz PF∞ | actual integrable even double-exponential Φ | Schoenberg必要条件とentire Laplace | このclassではGaussianに限られ、actual tailと矛盾 | actual Φでは偽 | REJECT_NOT_MEMBER |
| B4 Fourier transformのLaguerre–Pólya性 | actual order1 even F | 正確なreal-zero criterion | kernelのPF∞とは別。actualFのLPを独立に得ていない | YES | STOP_EQUIVALENT |
| C1 de Bruijn strip contraction | actual \(e^{\tau x^2}\Phi(x)\) | forward時間で上端帯を縮める既知定理 | repo規約τ≥1/8は安全。τ=0への逆伝播なし | 閾値≤0がYES | STOP_NO_NEW_INPUT |
| C2 各zero branchのrestoring velocity | actual local simplezero公式 | \(w'=H''/H'\) | even real heat polynomialでも内側branchが外向きに動く | 一般則は偽 | REJECT_GENERIC_LAW |
| C3 electrostatic / log gas | 他対象の既知平衡・確率モデル | zerosによるlog potentialの表示 | actual primes→独立potential→全zero拘束の橋なし | zeros入力なら循環 | NOT_ADOPTED |

## 既存theta検査との差分

| 過去資料 | 既に検査した内容 | 今回の位置付け |
|---|---|---|
| [phase2_modular_generator.md](notes/phase2_modular_generator.md) (D4) | 同じoff-axis二積分 | exact identityの再確認、new identityではない |
| [internal_first_principles.md](internal_first_principles.md) | 正・強log-concave・増加scoreでも非実零点、actual低階flux | shapeから同時消滅禁止への飛躍を再開しない |
| [selfdual_theta_boundary.md](selfdual_theta_boundary.md) | 正seed・正completed kernel・Poissonを保つoff-axis模型、直和energyのdomain障害 | modified Gammaを明記し、actualζの反例としない |
| [phase2_newman_generator.md](notes/phase2_newman_generator.md) | PDE、算術時計、閾値、Gaussian極限、explicit synthetic threshold | 既知収縮方向は維持、時刻0のthreshold仮定を追加しない |
| [freedman-weyl bridge gate](../../audits/proofs/audits/freedman-weyl-bridge-gate.md) | 複素Laguerre / PSDとreal-zero条件 | Hermite–Biehler/de Branges/Weilへ自動移行しない |

## 停止判定

主候補数はA/B/Cの3系統であり、表の細分を独立の第4候補とは数えない。新規の算術拘束、全域零点排除、Gaussian growth改善はいずれも未取得。

**NO ARITHMETIC RESTORING FORCE IDENTIFIED。**

無条件の既知の局所符号やforward帯収縮まで「存在しない」と否定したわけではない。得られなかったのは、それをactual ζの全零点・時刻0へ接続する独立法則である。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/freedman-weyl-bridge-gate.md`](../../audits/proofs/audits/freedman-weyl-bridge-gate.md)
- [`research/internal_first_principles.md`](internal_first_principles.md)
- [`research/notes/phase2_modular_generator.md`](notes/phase2_modular_generator.md)
- [`research/notes/phase2_newman_generator.md`](notes/phase2_newman_generator.md)
- [`research/selfdual_theta_boundary.md`](selfdual_theta_boundary.md)
