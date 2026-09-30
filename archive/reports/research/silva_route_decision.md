**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/silva_route_decision.md` · Original SHA-256: `7436b569a9f5ee0f975c0b1a4f1fabc79e9b5050ff4fc8c3ca0466dfea7587ee`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Silva 有限近似ルートの判断

更新: 2026-09-29。一次文献の限定照合。RH は OPEN、主 graph へ新しい RH 証明入力を追加しない。

## Statement と確定範囲

対象命題 S は「Silva の actual theta profile から作るすべての偶数次数 E の Z_E が、Re(s)=1/2 上の零点だけを持つ」。[Silva, arXiv:2609.25564v1](https://arxiv.org/html/2609.25564v1), Theorem 3.1 は対称性と critical strip 内の局所一様収束 Z_E→ξ を示す。§5 は零点配置を未解決としており、単位円零点定理を主張していない。

- **S ⇒ RH は確定**。左右の半 strip で各 Z_E が零点を持たず、局所一様極限 ξ は恒等的に零でないため、Hurwitz の定理が適用できる。実際には E→∞ となる部分列についての直線零点性で十分。
- **RH ⇒ S は未確認**。この特定の近似列への逆向きを証明していないため、S を既知の RH 同値条件と分類しない。
- root の Arb 計算と DESTROYER の監査によれば actual U_4 は単位円零点を持たず、actual Z_4 の4零点は臨界線上。これは E=4 の単位円十分条件ルートを閉じるが、S や RH の反証ではない。本メモ担当は当該計算を再実行していない。

## Closest known と差分

1. **Rodríguez-Villegas の十分条件**。[On the zeros of certain polynomials (2002)](https://frvillegas.github.io/pdf/frv-hilbert-functions.pdf), p.2251 Theorem は U の単位円零点性から Hilbert polynomial の直線零点性を導く。p.2252 Remark 5 は逆命題を否定する。例は U(t)=t³+23t²+23t+1、U(t)/(1−t)^4=ΣH(n)t^n、H(x)=(2x+1)³。Silva の規約 Z(s)=H(−s) では Z(s)=(1−2s)³。この既知例は奇数次数であり、actual U_4/Z_4 の個別認証とは区別する。

2. **Jensen–Pólya 型の RH 同値条件**。[O’Sullivan, Zeros of Jensen polynomials and asymptotics for the Riemann xi function](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/xi-revised.pdf), Theorem 3.1、Corollary 3.2、Theorem 3.5。通常の Jensen 多項式は、固定された ξ の Taylor 係数列 γ(j) を用いる Σ binom(d,j)γ(n+j)X^j。Silva の式 (20) を beta 積分で項別評価すると

   Z_E(s)=Σ_{j=0}^E P_ξ(j/E) (s)_j (1−s)_{E−j}/[j!(E−j)!]

   となる（(a)_j は rising factorial）。標本列が E に依存し、基底も異なる。したがって引用した Jensen 同値定理をそのまま移植できない。両者を結ぶ零点保存同定は未取得。

## Preservation と作業判断

今回の限定検索では、Silva の Bernstein–beta 合成変換に適用できる一般的零点保存定理は**未発見**。網羅的な不存在主張ではない。DESTROYER の有理反例 G(p)=99/100+1/[100(1+1000p)] は「正値・対称・Stieltjes だけで Z_4 の直線零点性が従う」という一般論を否定する。一方、入力の Fourier 変換が Laguerre–Pólya 型である場合の合成変換の保存性は別問題であり、この反例だけでは決まらない。

**RH の未解決部分を埋める new content は未達。全 E の数値計算へ拡大しない。** 少数次数の計算は候補を棄却する bounded falsification に限って有用。次の必要入力は actual theta profile 固有の次数間 recurrence / interlacing、または適用条件を独立に満たす zero-preserver。有限次数の成功、近似の収束、対称性の再確認だけでは全次数命題への距離を縮めない。新規性は主張しない。

## 直近30日 frontier の限定照合

9月の arXiv math.NT / math.CA / math.SP / math.GM 一覧、および Nyman–Beurling・de Branges・Li・trace の語検索と選択的本文読取では、追加の有望 DIRECT 入力を確認できなかった。8月末を含む全更新・全媒体を網羅したとは主張しない。

- [Mishra–Sarkar 2609.26787v1](https://arxiv.org/html/2609.26787v1): Theorem 4 は強化 Robin 不等式と RH の同値性。固定 ω ごとの有限還元は全 ω を処理しない。
- [Kazin–Kadyrov 2609.29898v1](https://arxiv.org/html/2609.29898v1): Theorem 1 は sinh に置換した tempered ξ の barrier。端点項による議論は原 ξ の cosine 変換に移らない。
- [Grobner 2609.02713v1](https://arxiv.org/html/2609.02713v1): Main Theorem は通常の高さ順の ΣR(x^ρ) の発散。平滑な Weil 明示公式や actual support-propagation への否定ではない。外部入力を含む全面的な独立検証は未実施。

## Bounded Jacobi test の結果

`proofs/audits/silva-jacobi-test.md` と独立係数補間監査で、E=0,2,4,6のmonic列に
21578447.73<gamma<21578447.74という非零Favard残差を認証。
同じu=(s−1/2)²・index E/2による固定scalar Jacobiのprincipal characteristic polynomials
という具体候補を棄却した。別のblock operatorや全零点命題の否定ではない。
次数を増やす計算へ進まない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/silva-jacobi-test.md`](../../audits/proofs/audits/silva-jacobi-test.md)
