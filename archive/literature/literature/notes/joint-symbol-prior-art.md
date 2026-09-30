**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/joint-symbol-prior-art.md` · Original SHA-256: `9b0c4c8e8f3b8c48627801f6bff9fff79f8b1dfe0552a32b7ec33b15502c22f2`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Joint symbol 認証の先行例と cancellation の量化

調査日: 2026-09-29。限定調査であり網羅的な新規性調査ではない。対象は

```text
h(t)=Re ψ(1/4+it/2)−log π,
P_a(t)=Σ_(log n<2a) 2Λ(n)n^(−1/2)cos(t log n),
Ψ_a(t)=h(t)−P_a(t),  A_a=Σ_(log n<2a) 2Λ(n)/√n.
```

**結論:** 固定 `a` について、有限区間の `Ψ_a` を直接区間認証し、その先を解析的 envelope へ接続して cutoff を下げる方法は **Zhu v2 §7 と §16 に既述**。今回の実装・数値結果について方法の新規性を主張しない。調べた無条件 cancellation の定理は、`∀a≥a₀, ∀|t|≥exp(Ca): Ψ_a(t)≥0` を導く強さ・量化を持たない。この未導出は、その目標の不可能性を証明したものではない。

## 1. Zhu の exact locator

一次資料: Xuefeng Zhu, [arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2), 2026-09-02 提出版。固定 source の `main.tex` SHA-256 は `14ec17c2b2e1d3d8069c1d424dae4f5aa6c92b75c73b89d10915ed868495f2c5`。取得・公開 package の未確認状況は [証明書監査](zhu-certificate-audit.md) に記録済み。査読掲載は未確認。本文の記述確認と全定理の独立検証は別であり、後者は未完。

| Locator | 原文の内容と採用範囲 |
|---|---|
| [§7](https://arxiv.org/html/2608.24827v2#S7), “The corrected cost of support 2.38”, `main.tex` 1327–1353 | L=1.19 の旧 cutoff1100 が不十分と述べ、有限区間の **Ψ 自体**の adaptive interval evaluation と、その先の crude-envelope takeover を明示。約8500まで下げる案と envelope単独約12000の比較。ただし元の約7400の `T₁` より下をこの例で達成したとは書いていない。 |
| 同 §7, `main.tex` 1343–1347 | 短い原文: “certified interval-arithmetic lower bound for $\Psi_L$ itself”。有限式なので区間最小値を認証できる、という提案そのものが今回案の先行例。 |
| 同 §7, `main.tex` 1353 | “We have not carried it out.” 数値見積り・計画と実行済み certificate を区別する。 |
| [§14.1](https://arxiv.org/html/2608.24827v2#S14.SS1), `main.tex` 2295–2302 | `β*=log(T♯/(2π))−1/T♯−A_a>0` と定める元の envelope に対して `T♯>T₁=2πe^(A_a)` が必要。`A_a∼4e^a` によりその手法の scale は二重指数。 |
| [§14.2](https://arxiv.org/html/2608.24827v2#S14.SS2) | Landau–Widom fit を一般の certificate の計算量下界に転用しない旨を区別。有限個の上界データから全窓の下界や全手法の不可能性を導かない。 |
| [§16](https://arxiv.org/html/2608.24827v2#S16), Open problems (v), `main.tex` 2429–2435 | envelope が悲観的な有限範囲で `min Ψ_L` を直接認証し、cutoff を resolution scale へ近づける interval route を再掲。 |

引用英語は同一 source 合計25語以内。それ以外は日本語要約。今回の Arb による具体実装・別窓の結果は、原提案の検査・実装例として記録する。Zhu が既に同じ Arb code または root の特定の定数を計算したとは主張しない。

## 2. 先行案と整合する厳密な接続条件

以下は先行案の論理を当方が整理した十分条件であり、新規定理として主張しない。固定 `a`、目標 floor `β≥0`、`15/4≤T₀≤T_end` を選ぶ。

1. 全区間を覆う outward-rounded interval 計算で `inf_[T₀,T_end] Ψ_a≥β` を認証する。
2. `log(T_end/(2π))−1/T_end−A_a≥β` を厳密に確認する。
3. Zhu Lemma 3.1 と右辺の単調増加より、`t≥T_end` でも `Ψ_a(t)≥β`。
4. `Ψ_a` は偶関数なので、`|t|≥T₀` 全体で同じ floor が得られる。

`T_end≈2π exp(A_a+β)` は見積りであり、`−1/T_end` を無視した等号値では厳密な takeover にならない。区間端点・prime-power support の厳密な比較・複素 digamma の包含も certificate の前件に残す。点列の float scan は全区間の下界ではない。

この接続は `T₀<T₁` を論理的には禁じないが、実際に達成したかは窓と β に依存する。`P_a≤A_a` という **t に依存しない一様定数 bound** の最適性から、`h(t)−P_a(t)` の joint な区間 bound の最適性は出ない。Zhu §14 の言い方を「任意の pointwise joint-symbol 法も T₁ 未満へ行けない」と広げるのは不適切。

また `Ψ_a≥0` を高周波で示すことと、全 Weil form の正値性は別である。残る低周波・pole・有限 head と無限 basis tail/coupling の認証は必要。strict floor を使う還元であれば `β>0` が別に必要で、零の floor から strict tail gap を作ることはできない。

## 3. 直接該当する既存の無条件 cancellation bound

一次資料: Kaisa Matomäki, Maksym Radziwiłł, Terence Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. Lond. Math. Soc. 118 (2019), 284–350, DOI [10.1112/plms.12181](https://doi.org/10.1112/plms.12181)。本文確認は [arXiv:1707.01315v3 §2.4](https://arxiv.org/html/1707.01315v3) と [大学 repository の final draft](https://www.utupub.fi/bitstream/10024/158999/1/correlations-repaired.pdf) pp.18–20。書誌・final draft の位置付けは [大学 repository](https://www.utupub.fi/items/3c8225f9-589a-4b31-8917-7c7cd03de559) で確認。査読誌掲載あり。全証明の独立再構成は未実施。

**Exact locator:** §2.4 の definition (29)、Lemmas 2.6–2.7 とその直後の Λ への適用。`q=1` とし、記号の衝突を避けて saving exponent を `K` と書くと、任意の固定 `K>0` に対して、十分大きな固定 `B′` について

```text
|Σ_(n≤x) Λ(n)n^(−1/2−it)| ≪_(K,B′) √x (log x)^(−K),
              (log x)^(B′)≤|t|≤x^(B′).
```

一般形は residue class、`q≤log^B x` を含み、`B′` の必要な大きさと implicit constant は saving exponent 等に依存する。RH 仮定はない。著者らは van der Corput、Vinogradov–Korobov zero-free region と convolution を使う。

**今回目標へそのまま使えない理由（当方の適用判定）。** `x=e^(2a)` なら右辺は `e^a/(2a)^K`。一方 `t=exp(Ca)` の archimedean floor は `h(t)=Ca−log(2π)+o(1)` で `O(a)`。任意の **固定** K に対して前者は O(a) より大きく、この上界から `P_a≤h` は出ない。これは実際の和が必ず大きいという主張ではなく、掲示 bound が不足という判定。Kをa依存に選ぶと implicit constants・開始閾値・B′依存も変わるため、定理の固定パラメータ版を一様 bound に昇格できない。

さらに固定 `B′` は `|t|≤exp(2B′a)` までしか覆わない。analytic takeover は約 `exp(4e^a)` なので、その間に広い未処理区間が残る。任意に大きい B′ ごとの存在を、一つの明示定数で全 t を覆う bound と読み替えない。有限窓で実際に使う場合にも implicit constants を明示化する別作業が必要。

## 4. 強い large-values 定理でも「例外なし」にはならない

一次資料: Larry Guth, James Maynard, *New large value estimates for Dirichlet polynomials*, [arXiv:2405.20552v2](https://arxiv.org/html/2405.20552v2)（この v2 は2026-04-07）、**Theorem 1.1**。査読掲載は [Annals of Mathematics 203 (2026), 623–675](https://annals.math.princeton.edu/2026/203-2/p06)、DOI 10.4007/annals.2026.203.2.6 で確認。全証明の独立検証は未実施。

`|b_n|≤1`、`[0,T]` の1-separated点 `t_r` 上で `|Σ_(N≤n≤2N)b_n n^(it_r)|≥V` なら、その点数 R は

```text
R ≤ T^(o(1)) [N²V^(−2)+N^(18/5)V^(−4)+T N^(12/5)V^(−4)].
```

これは無条件の **大値の個数** の評価であり、すべての点で cancellation する定理ではない。Λ-weight は dyadic 区間ごとに `b_n=Λ(n)√N/(√n log(2N))` と正規化できるが、必要な対数尺度の threshold では RHS を1未満にする保証がない。例外集合の測度・密度が小さいこと、zero-density bound、平均二乗の小ささのいずれも、joint-symbol の負の小区間がゼロ個だという結論を与えない。`T^(o(1))` も有限パラメータの Arb 証明書へ即時代入できる数値定数ではない。

## 5. 固定 prime comb の高 t recurrence が禁止するもの

一次 locator は **Zhu v2 Lemma 3.2 とその証明**。有限個の素数について `{log p}` の Q-linear independence と連続時間 torus equidistribution を用い、任意に大きい t でも prime phases を同時に0へ近づける。したがって固定 a と任意の H に対し

```text
sup_(t≥H) P_a(t)=A_a.
```

当方の確認: 各 `dist(t log p,2πZ)<δ` なら、有限範囲内の `p^k` について `cos(kt log p)≥1−k²δ²/2` となり、`A_a−P_a(t)` を任意に小さくできる。従って固定 a で `P_a(t)≤(1−η)A_a`（固定 η>0）が **全 t≥H** に成立するという cancellation 仮説は偽。`ΣΛ(n)n^(−1/2−it)→0` という固定長 Dirichlet polynomial の減衰も成立しない。

ただし、この recurrence を joint symbol の反証に転用してはならない。`h(t)→∞` なので、十分高い t の再整列は Ψ を負にしない。`∀H ∃t≥H` という定性結論は、`t` が `exp(Ca)` と analytic takeover の **間**にあるとは保証しない。従ってこれだけで単指数 cutoff の可能性を否定できないし、T₁が実際の Ψ の最終負点の下界とも証明できない。必要なのは relevant finite height range における定量的な同時位相情報である。

## 6. 今回の採用判断

| 候補 | 正確さ・先行性 | 今回の用途と限界 |
|---|---|---|
| finite interval Ψ lower bound + analytic takeover | Zhu §7/§16 に明示的先行例 | 固定窓の実装・独立認証として有用。新規手法・全窓定理とはしない。 |
| MRT (29), Lemmas2.6–2.7 | Λ の無条件 cancellation、対象の重みと位相に直接適合 | 対数 saving、固定 polynomial height range。必要な O(a) bound と全高tの量化を満たさない。 |
| Guth–Maynard Thm1.1 | 無条件、強い large-values count | 平均・個数から全点 positivity へ進む別義務が残る。 |
| finite-comb recurrence | 固定aの arbitrarily-large-t alignment | 一様 comb 定数の改善を排除。joint Ψ cutoff 改善そのものは排除しない。 |

今回確認した一次資料から、`∀a≥a₀,∀|t|≥exp(Ca)` の joint positivity を与える無条件 cancellation theorem は抽出できなかった。全研究領域にその定理が存在しないという網羅的断定はしない。root の今回の計算は、その実際の証明済み窓・β・区間分割・誤差 budget に限定し、先行案の実装検証として記述する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/zhu-certificate-audit.md`](zhu-certificate-audit.md)
