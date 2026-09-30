**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_comma_candidate_matrix.md` · Original SHA-256: `a84e27f62c23d375fa76ffbfcd0c4026d080d460086127e3a1882b3dc2ab5a49`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Comma candidate matrix

2026-09-30。RH OPEN。新規性の主張なし。三つの主要試行を終了し、未監査の主証明グラフへの統合なし。

| ID / precise proposal | Actual arithmetic fidelity | Exact bridge / independent input | Falsification / missing lemma | Decision |
|---|---|---|---|---|
| A1 \(A_P=\int B_P\overline C_{P,X}dm\) | \(P\supset\{p\le X\}\) なら actual Mertens | monomial orthogonality、係数抽出 | estimate ではない；CS は一般に自明界以下 | Level 1 として保存、既知構造 |
| A2 smoothed \(M_h\) の Fourier–Mellin integral | \(\sigma>1\) で full ζ、有限積では全 support primes を含める | 絶対収束、Fourier inversion、no-tail | shrink \(h\) の uniform kernel correlation 不明 | identity 保存、cancellation route 終了 |
| A3 contour を \(1/2+\varepsilon\) へ移して residues 無し | 形式上は actual ζ | 独立入力なし | \(1/\zeta\) の poles を無視；全重みで零点不存在を仮定すれば循環 | 棄却 |
| A4 \(\mu(n)n^{-\sigma}\in\ell^2\), \(\sigma>1/2\), から指定点を評価 | 係数は actual | HLS の \(H^2\) 空間、正の norm | identity boundary evaluation が非連続；cutoff dual norm の増大 | 棄却 |
| B1 nonresonance ⇒ time equidistribution | actual finite prime logs | unique factorization、character の直接積分 | growing \(P,X,T\) の uniformity は別 | 既知事実として保存 |
| B2 nonresonance ⇒ mixing | actual finite prime logs | なし | character autocorrelation の絶対値1 | 反証、終了 |
| B3 time law / all moments ⇒ fixed-point square-root bound | actual logs と weighted cutoff を両模型で保持 | Haar rotation | \(F_X(z)=C_X(-z)\)、同分布、identity 値は (M(X)) と \(N_X\asymp X\) | 一般則を反証 |
| B4 actual Möbius polynomial が全 \(t\) で \(O_\varepsilon(X^{1/2+\varepsilon})\) | actual μ | なし | sup over \(t\ge t_0\) は \(N_X\asymp X\) | 反証。\(t=0\) の RH は反証していない |
| B5 elementary/Matveev gaps ⇒ growing-dimension cancellation | prime arithmetic | \(1/\max(a,b)\)、固定 \(P\) の coefficient-height bound | gap は signed kernel correlation の bound ではない；定数と量化 | 非共鳴下界を保存、RH route 終了 |
| B6 rare simultaneous returns ⇒ small product integral | finite actual primes | fixed-box Haar density | 0 位相では抑制、π で増幅；稀な大振幅・cutoff kernel が残る | 根拠不足、終了 |
| B7 weighted all-comma measure ⇒ small discrepancy | full actual cutoff and parity | signed pair-gap measure と sinc identity | その signed integral を評価する算術内容が未取得 | 定義・identity 保存のみ |
| C1 Halász distance ⇒ fixed-power saving | 一般 multiplicative μ、prime powers を変更しない | GS03 p1192 の theorem | 距離二乗 \(le2\log\log X+O(1)\)；比較式だけでは log-power scale | fixed-power route 終了 |
| C2 character twists / high correlations で不足を埋める | twist の対象は明示可能 | 一部の既知分離定理 | conductor/height の一様評価や新しい予想を丸ごと仮定できない | 主候補へ追加しない |

## 合格した exact toy、棄却した解釈

- 二素数 squarefree model は4状態で \(X\ge6\) に総和0。大きな \(m\log2-n\log3\) が Boolean states を追加するわけではない。
- 三素数も8状態の exact step function。fixed finite-prime limit の完全相殺を growing-prime Mertens bound と混同しない。
- primary Matveev bound の次元依存を保持。粗い十分 averaging time を必要時間の下界とはしない。
- phase law の反例は全ての kernel-correlated phase methods への no-go ではない。反証したのは phase law だけを使用する推論。

## 成功水準

Level 1: **達成（既知の exact bridge の固定・検算）**。
Level 2: 新しい PNT 以上の機構 **なし**。
Level 3: 本トラックによる固定 power saving **なし**。
Level 4: 平方根級 bound **なし**。
Level 5: RH **OPEN**。

詳細は [main log](arithmetic_comma_prime_log_flow.md)、[adversarial audit](../../audits/proofs/audits/arithmetic_comma_adversarial.md)。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/arithmetic_comma_adversarial.md`](../../audits/proofs/audits/arithmetic_comma_adversarial.md)
- [`research/arithmetic_comma_prime_log_flow.md`](arithmetic_comma_prime_log_flow.md)
