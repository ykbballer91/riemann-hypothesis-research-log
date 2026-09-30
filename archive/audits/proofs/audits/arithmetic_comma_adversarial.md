**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/arithmetic_comma_adversarial.md` · Original SHA-256: `577f24d715316f0314738cf3f83922f3ad08723f73db2ff46ee1237fb800d451`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Comma — adversarial audit

2026-09-30。RH OPEN。有限次元恒等式、位相法則の反例、既知定理の適用域を監査した。文献の全証明を再証明したとは主張しない。一般の phase/cutoff correlation 法全体への不可能性定理も主張しない。

## 1. 検証範囲と担当

BUILDER：Bohr lift、Haar coefficient extraction、Fourier–Mellin、no-tail、Perron endpoint、smoothing。
DESTROYER：非共鳴の量化、Matveev 適用、mixing 反例、same-cutoff phase-law 反例、builder の正規化。
LITERATURE：一般乗法的 Halász 定理、pretentious distance、prime-power と twist の範囲。
ROOT：同分布の直接証明、all-comma signed gap distribution、高次 resonance、exact experiments と統合。

LITERATURE が最後に root の直接証明と実験コードを独立に再検査した。別実装の整数 sieve と90桁 Decimal を用い、元コードの再実行に頼らず、整数計数4件・Haar moments6件・有限時間値8件・near-return records7件を照合した。重大な誤りなし。数値比較の最大差 \(4.90\times10^{-24}\) は保存25桁の丸め内。ただし区間演算による厳密誤差保証ではない。

## 2. 九つの必須 failure gates

| Gate | Test / evidence | Verdict |
|---|---|---|
| 1 vertical average と係数 cutoff | \(\int B\,dm=1\) だが \(M(X)=\int B\overline C_X\,dm\) | cutoff 相関を省く推論を棄却 |
| 2 非共鳴を mixing と誤認 | character autocorrelation は絶対値1 | mixing は偽、等分布だけを保存 |
| 3 増大する次元の定数 | elementary height bound と Matveev の \(k,H,p\) 依存を明記 | fixed-\(k\) からの無条件 limit 交換なし |
| 4 nonrectangular cutoff を除去 | \(C_{P,X}\) を全式で保持、finite toy の省略 prime の差を確認 | 合格 |
| 5 稀な near-resonance の扱い | 0 側は積を抑え、π 側は増幅；actual finite sum の supremum は線形 | 「稀だから無害」を棄却。RH 自体の反例ではない |
| 6 contour shift | \(\sigma>1\) でのみ full Euler integral を採用；\(1/\zeta\) の poles を明記 | hidden RH の移動なし |
| 7 Halász の精度 | 距離二乗 \(\le2\log\log X+O(1)\) | その black box 単独の固定 power saving を棄却 |
| 8 randomness の証明化 | torus marginal law と deterministic identity を分離、grid は diagnostic | 合格 |
| 9 bound の改名 | 必要な kernel 相関へ平方根評価を置くだけでは未解決 | 新 lemma として採用しない |

## 3. Exact identities の細部

1. Haar は normalized。係数抽出に \(2^k\) を付けない。確率化 \(2^{-k}\nu_P\) は別対象。
2. \(\widehat\phi(t)=\int\phi(v)e^{-itv}dv\) の規約で inverse に \(e^{itL}\) と \(1/(2\pi)\)。積は \(1-p^{-it}\)。
3. Full arithmetic では \(\sigma>1\)、\(g_\sigma(v)=e^{-\sigma v}\phi(v)\)、外因子 \(e^{\sigma L}\)。\(\sigma>1/2\) の \(\ell^2\) existence で置き換えない。
4. Sharp no-tail は \(P\) が全 \(p\le X\) を含むこと。単に最大素数が大きいだけでは不足。compact smoothing では \(p\le Xe^h\) を含める。
5. Nonnegative compact mollifier では差が cutoff 付近の整数だけにあり、\(2X\sinh h+1\)。Gaussian へ no-tail を転用しない。
6. Perron at integer は half jump。\(M^*(X)\) と右連続の \(M(X)\) を区別。
7. 全 \(n\le X\) が squarefree ではない。Bohr comparison は squarefree support だけで行い、\(\mu^2\) の positive comparison とした。
8. \(\mu\) は completely multiplicative でない。prime powers を \((-1)^k\) に変えない。
9. \(\zeta\) の \(s=1\) の pole は \(1/\zeta\) の zero。一方非自明 zeros は \(1/\zeta\) の poles。

## 4. 最も強い反証と限定

\(F_X(z)=C_X(-z)\) から、same logs・same weighted cutoff の signed と all-positive polynomial は全 Haar law を共有する。しかし identity の値は \(M(X)\) と \(N_X\asymp X\)。これは time statistics から特定位相の値を推定する一般法則を否定する。

さらに \(\sup_{t\ge t_0}|F_X(z(t))|=N_X\)。任意に遅い時間にも大きな値があり、全 \(t\) 一様 square-root cancellation は actual coefficients 自体で偽。

ここから次を結論してはいけない：

- actual \(M(X)\) が線形である。
- RH が偽である。
- 全ての kernel-correlated phase 法が不可能である。
- 最初の大きい excursion が小さい \(t\) で起こる。
- 同分布だから有限時間の二つの平均も完全一致する。

最後の点は実験でも区別した。有限時間平均は違い得るが、fixed \(X\) の無限時間極限は一致する。

## 5. Near-resonance と高次相関の罠

Elementary \(|\log(a/b)|\ge1/\max(a,b)\) は無条件。actual \(a,b\le X\) の場面では \(1/X\) を使い、generic Fourier modes の巨大な primorial-height bound を持ち込んで必要時間を誇張しない。

Continuous time の非共鳴と、sampling interval \(\tau\) に対する \(\tau m\cdot\log p\notin2\pi\mathbb Z\) は別。実験の固定 grid から continuous-time box density の証明を主張しない。

高次の product equalities は残る。\(2\cdot15=3\cdot10\) は prime logs の整数独立性への反例ではなく、同じ合成指数ベクトルへの到達である。全ての偶数絶対モーメントを利用しても同分布障害は解消しない。

## 6. 数値検査と既存ファイル保全

- 有限 subset sums は整数で exact enumeration。
- Haar moments は積の multiplicity を整数で数え、signed/positive が厳密一致。
- Fourier product identity は60桁で誤差 \(10^{-50}\) 未満を検査。これは数値照合であり一般恒等式の証明は展開による。
- Near-return search は \(\log3\) の係数 \(1\le b\le400\) の範囲。全 coefficient box の最短 return を証明したものではない。
- 二・三素数で計40,000 sampled times。成長 fit や無限次元の推論なし。
- 同じ phase flow での all-positive model、cutoff-cluster subsystem、higher-moment resonance を falsifier として使用。いずれも actual ζ の改変を proof track へ採用していない。
- 保存確認は新 track 外の従来275ファイルの SHA-256 baseline と照合する。結果は research/arithmetic_comma/preservation_check.json。

## 7. 最終判定

Exact bridge と基本的 quantitative nonresonance は無条件。新しい Mertens bound、subexponential return、RH proof は得られていない。三つの主要構成は全て、actual cutoff と位相積との未評価な算術的相関へ戻った。

Level 1 に限定して終了。主証明グラフへ merge しない。今回の elementary obstruction に新規性は主張せず、既知の線形代数・Fourier 解析からの直接帰結として保存する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/arithmetic_comma/preservation_check.json`](../../../../data/source-records/research/arithmetic_comma/preservation_check.json)
