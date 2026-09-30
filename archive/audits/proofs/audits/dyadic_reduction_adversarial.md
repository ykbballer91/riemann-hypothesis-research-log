**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/dyadic_reduction_adversarial.md` · Original SHA-256: `d4dba37bd39d14cbe4475774ff797aeaa108f0a04683265e616ebf2ce77dd83b`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Dyadic reduction — adversarial audit and release gate

2026-09-30。RH OPEN。主担当の直接証明、builder の算術恒等式、literature 担当の
一次資料照合、destroyer の独立計算を分離して統合した。旧 proof graph への merge は 0。

**PASS:** explicit w_n∈actual W、forward-only sufficiency、p_4→p_1 exponent 1/2、
compact folding no-go。**未証明:** exponent 0。
**棄却:** 同じアルゴリズムの準指数 endpoint を RH より弱い新入力とする主張。

完全な独立計算は [independent_audit.md](../../research/dyadic/notes/independent_audit.md)。
構成の全式は [explicit_mobius_reduction.md](../../../reports/research/dyadic/notes/explicit_mobius_reduction.md)。

## 証明の依存関係

1. actual arithmetic range の pole-free even Schwartz 部分を使用する。
2. 全整数の絶対収束 Möbius inversion は x>0 ごとに正当。
3. cutoff と mean correction で f_a(0)=integral f_a=0 を厳密に満たす。
4. w_n=-JSf_a は closure への近似ではなく、既に実際の range の元。
5. x>=1 の相殺は divisor identity による。RH・zero-free 仮定なし。
6. Poisson に必要な二つの境界項は test 条件で本当に消える。
7. ||f''||_1 と ||xf'''||_1 の bound、p_1 の左重みを個別に確認。
8. 全 g∈E に p_1(R_n)<=C2^{n/2}(1+n)p_4(g)。C は n,g に非依存。
9. 各代表元に適用して infimum を取るので q_4 入力の quotient estimate も正しい。
10. RH による条件付き Mertens bound の使用箇所は endpoint の逆含意だけ。

## Mandatory destroyer tests

| Test | 実行した検査 | 結果・範囲 |
|---|---|---|
| arbitrary function | 複素値の任意 g∈E について級数、微分、moment、Poisson を証明 | PASS。偶性は g でなく構成された real-axis f_a の偶延長に課す |
| compact support extreme | W∩Cc∞={0}、遠方の compact support を固定区間へ移す案 | compact exact folding を反証 |
| one-sided tail | D3 は右裾を消し、左裾を O(x^{3/2})（p_1 用）で制御 | tail を捨てず保存。全 E への所属には全 Schwartz derivatives を使用 |
| oscillatory input | g_omega=e^{i omega t}g の微分を展開 | p_4(g_omega)<=C(1+|omega|)^4p_4(g)。定理の定数は変えず入力 seminorm が周波数費用を払う |
| Gaussian | g=e^{-t²} の entire Laplace transform は sqrt(pi)e^{z²/4} | 全零点を非零で検出。元の range 内の Gaussian polynomial test と混同しない |
| translated bump | g_b(t)=g(t-b) は E、p_4(g_b)<=e^{4|b|}(1+|b|)^4p_4(g) | 初期位置の費用を隠さない。compact fold の反例にも使用 |
| synthetic off-line character | 対称 pair alpha=±delta（必要なら共役も）と return 2^{n alpha} | c=1/2 bound は 0<delta<1/2 を許す。準指数 bound は許さない。actual zeta の反例ではない |
| quotient collapse | w_n は元の V に属す。topology/completion 不変 | q_1 を弱めることで off-line evaluation を消す偽解決なし |
| unbounded evaluation | 既存の評価 abs(ell_rho)<=4q_1 を最初から最後まで使用 | 定性的 continuous だけに後退せず定量 bound を保持 |
| hidden functional equation | reflection の使用を forward conclusion の最後に限定 | reduction construction と rate 1/2 に RH/reflection は不要 |
| hidden RH-equivalent density | full epsilon Mertens hypothesis の採用を検査 | endpoint は明確に RH 同値と判定、不採用 |
| artificial weight / operator | E、W、T_2、q_1 を維持、cutoff は代表元選択だけ | 新しい metric/topology/spectral encoding なし |
| local/global error | real-only idele と diagonal rational 2^n を別計算 | product formula を T_2=I の証明へ転用する案を排除 |
| infinite regularization | x>0 の和は locally absolute、divisor regrouping も absolute | 未定義 regularized sum なし。数値有限和を global identity の根拠にしない |
| multiplicity | W の全 zero jets の消滅を保持 | compact no-go の R log R は multiplicity 込み。単純性を仮定しない |

## 追加の exact counterexamples / no-go

非零 Laurent polynomial P に対し P(T_2)E⊂W は不可能。幅<log2 の非零 compact bump を
使えば P(T_2)g は disjoint translates の非零 compact 和。W∩Cc∞={0} と矛盾する。
これは有限 dyadic filter を universal arithmetic relation にする案を排除するが、
非compact input ごとの特別な coboundary を排除しない。

Ordinary periodicization を使うと T_2=I になり、一般の zero multiplier を失う。
actual W にはその同値関係がない。L² で収束する odd sum を全指数重み E の収束と
取り違える案には、p_N remainder が 2^{(N-1/2)J}poly(J) で増大する exact test がある。

Báez-Duarte の generators を 2^j のみにしたモデルでは、有限和の tail A/x と
3つの区間の値から target の極限が 1,1,2 となる矛盾を得る。よって target はその
閉包にない。これは既存 W を dyadic-only range に改変してよい根拠にならない。

## n=1,2,3,4 の実行検証

[check_reduction.py](../../../../artifacts/research/dyadic/check_reduction.py) を 40 桁 mpmath で実行。
[結果](../../../../artifacts/research/dyadic/reduction_checks.json)：

- divisor convolution identity を 1<=r<=512 で整数として検査、全件一致。
- compact smooth H(x)=exp(-1/((x-1)(2-x))) on (1,2) を使用。
  正の x ごとに Möbius inverse/summation は有限和なので、隠れた truncation tail はない。
- n=1,2,3,4 の右半軸相殺と archimedean shell recurrence を評価。
  標本中の最大絶対残差は約 1.57e-43（閾値 1e-30）。
- mean correction の係数は数値積分。左裾の weighted samples も記録したが、
  p_1 の global supremum、無限 n の bound、interval certification ではない。
- dyadic Beurling の区間矛盾は有理数演算で 1,1,2 を確認。
- synthetic delta=±0.2 の n=40 の振幅は 1/256 と 256。ゼロ位置の fit はしない。

上記は誤符号・半密度係数・有限実装の反証試験。定理の根拠は別に書いた解析証明と
独立監査である。数値標本の小さな値から準指数成長を推測していない。

## 最終 claim gate

| Claim | Gate |
|---|---|
| explicit reduction exists on actual arithmetic quotient | PASS |
| literal task Level 3, fixed c=1/2<1 | PASS |
| one compact fundamental-region representative | FAIL for nontrivial compact folding |
| q_1 Banach operator norm has rate 1/2 | NOT PROVED; source seminorm is q_4 |
| exponent 1/2 is necessary or optimal | NOT PROVED |
| all possible subexponential reductions are impossible | NOT PROVED |
| subexponential endpoint of this fixed algorithm is RH-equivalent | PASS, both implications checked |
| new RH-independent arithmetic bridge | NONE |
| RH closed | FALSE |

3主要機構の後に strategy review を行い終了。無条件の成果と失敗の範囲を保存し、
主証明 graph や旧 phase state は更新しない。Lean 形式化は今回実施していない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/dyadic/check_reduction.py`](../../../../artifacts/research/dyadic/check_reduction.py)
- [`research/dyadic/notes/explicit_mobius_reduction.md`](../../../reports/research/dyadic/notes/explicit_mobius_reduction.md)
- [`research/dyadic/notes/independent_audit.md`](../../research/dyadic/notes/independent_audit.md)
- [`research/dyadic/reduction_checks.json`](../../../../artifacts/research/dyadic/reduction_checks.json)
