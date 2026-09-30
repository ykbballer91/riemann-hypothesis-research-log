**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/weighted_prime_halfspace_candidates.md` · Original SHA-256: `2fed85b9d527c62aa66501bcce3293aeca77e9d4e2aefe5dfc855004f770dfed`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Weighted prime halfspace — candidate matrix

2026-09-30。RH OPEN。今回の Level 1 は「新しい算術固有 identity」を要求する。既知の exact reconstruction を確認しただけでは達成としない。

| ID | 精密化した命題／候補 | 独立入力・実際に証明した範囲 | 反証・不足・counting scale | 判定 |
|---|---|---|---|---|
| A1 | \(M(X)=\prod(I-\tau_{\log p})J(\log X)\) | Boolean 展開、actual cutoff、順序可換 | 恒等式は既知、収縮を含まない | 保存・Level 0 |
| A2 | 高階差分は正の spline なので小さい | \(F_m=D^{m-1}B\)、\(B\ge0\) | 微分後の符号・振幅は別。全変動 \(2^m\)、smooth bound は \(h^{-m}\) と高階微分 | positivity shortcut 棄却 |
| A3 | 一般 threshold の Fourier bound から RH | sharp absolute bound \({m-1\choose\lfloor(m-1)/2\rfloor}\) | normalized \(O(m^{-1/2})\) を戻すと \(2^m/\sqrt m\) | 棄却 |
| A4 | 小さい irrational perturbation が強相殺を作る | 閾値 margin 内なら Boolean function は不変 | 独立重みでも equal-weight extremizer を保持 | 一般則を反証 |
| A5 | influence / LO / noise / hypercontractivity | shell count、標準確率規約、\(\rho^m\) multiplier | unsigned shell、\(2^m\) と \(\rho^{-m}\) の復元費用 | 追加算術入力なしで終了 |
| A6 | permutation / martingale で amplitude が縮む | 全順序の最終値一致、最後の martingale difference に最高次数係数 | order average が同符号の threshold 反例 | 自動 cancellation を反証 |
| A7 | 大素数 block の parent を一回ずつ数える | 正しい分解は \(\sum_r\mu(r)(\pi(X/r)-\pi(\sqrt X))\) | multiplicity を消すと別の和。PNT alone は signed correlation を与えない | 正しい既知 identity 保存 |
| B1 | \(\mathcal F(s,z)=\zeta(s)^zG(s,z)\) | actual squarefree Euler factors、\(G\) の正則性 | 全整数版 \(\omega\)・Liouville と混同しない | 保存 |
| B2 | \(z=-1\) で generic main term が消える | \(G(s,-1)=1\)、全 \(h_j(-1)/\Gamma(-1-j)=0\) | 主項係数の消失であり有限和0ではない | 既知・確認 |
| B3 | 全 main terms 消失 ⇒ square-root remainder | 局所 \(s=1\) の正則性のみ | synthetic \(D_\beta\) は局所零点でも係数和 \(\asymp X^\beta\) | 推論を反証 |
| B4 | fixed-log 全次数展開から fixed power | 固定 \(K\) ごとの \(O_K(X/\log^KX)\) | \(K\) 依存、既存 \(\tau_{-1}=\mu\) の入力、非自明零点の極 | route 終了 |
| B5 | CLT / local counts から parity へ代入 | 標準化の \(\pi\) は増大周波数 | 強い mod-Poisson は扱える場合もあるが対象・絶対誤差を要確認 | Gaussian-only 推論棄却 |
| C1 | tilted probability で cutoff を典型化 | finite Gibbs と actual readout identity | 正規化と \(e^{\sigma W}\) の復元を全て保持する必要 | exact identity 保存 |
| C2 | parity expectation × cutoff expectation | 独立 prime coordinates | \(X=3,\sigma=1\) では積近似 \(+1/2\)、actual \(-1\) | 反証 |
| C3 | saddle なら通常 Gaussian LCLT | saddle の存在条件と一意性、\(W/\log X\) の非Gaussian極限 | variance が境界の二乗規模、Lindeberg 失敗 | 当該 Gaussian shortcut 棄却 |
| C4 | \(\sigma\le1\) で無限 parity product を確率化 | finite system は well-defined | infinite selected set と \(W=\infty\)、通常 parity 未定義 | critical-product shortcut 棄却 |
| C5 | sieve local densities で parity を決める | \(\mu^2+\mu,\mu^2-\mu\) は固定 divisor ごとに同じ主密度 | signed remainder を除く情報では識別不可。全 exact divisor data は別 | 限定 barrier、全方法への no-go ではない |

## Arithmetic specificity と equivalence

- 新しい prime-specific bound はなし。実際の prime factors は定義・recursion・Euler product・PNT 入力で保持したが、それらから新しい parity estimate を導けていない。
- 全ての固定 \(\varepsilon>0\) に対する \(X^{1/2+\varepsilon}\) bound を covariance、remainder、signed shell の名前で置き直しても新補題とは数えない。
- 固定 \(\theta\in(1/2,1)\) の power bound はそのまま RH 同値とは呼ばない。ただし既知でない zero-free strip input を伴うため、今回無条件に得たと主張しない。
- Synthetic weights・\(D_\beta\) は論理飛躍への反例専用。actual ζ の代わりの proof model には採用しない。

## 終了時水準

Level 0: 達成。既知構造の固定と failure mechanism の明確化。
Level 1–5: 未達成。

三系統を閉じる。独立監査済みの新しい算術評価がないため主 proof graph への merge は0。
