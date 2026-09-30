**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/structural_audit.md` · Original SHA-256: `e8a5144e3e90f20c649f62f28f9f358e6a8077132b8de8416353a4e76f3b6930`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 構造ヒューリスティック第1巡の独立監査

日付: 2026-09-29。RHはOPEN。第1・2巡の合流は0件、第3巡で固定窓補助T090のみ採用。
エージェント間監査であり、外部査読・完全RH候補の監査A/B/Cとは異なる。

## 読取・出典境界

添付PDFはpypdfでテキスト抽出し、7頁すべてをPNGで視覚確認した。
抽出物は `research/source_inspection/` に置きGit・checkpoint archiveから除外。
公開史の認証はせず、ユーザーが許可した6個の抽象的着想だけを使用した。
主論文のBibTeXと主依存グラフに添付資料を追加していない。

## 分担とroot再構成

|対象|構築・調査|別担当の攻撃|判定|
|---|---|---|---|
|中心化・Mellin・dilation|BUILDER|DESTROYERとrootが符号・domain・反線形性を照合|補助計算PASS|
|prime–zero・既存core/trace理論|LITERATURE|rootが原文と既存規約を照合|条件付き結果の条件を維持|
|global L² closability障害|DESTROYER|rootがsampling列とDCTを独立再構成|限定候補の反証PASS|
|global coercivity障害|DESTROYER|rootが別の規格化と零点からの距離を確認|限定候補の反証PASS|
|実Weil窓差分|DESTROYER|rootが明示公式のsmooth kernelを再導出・実験。DESTROYERが実装再監査|係数・符号PASS|
|prime jump energy発散|root|BUILDERとDESTROYERが係数2・support・Euler発散を独立確認|限定候補の反証PASS|

rootによるclosability再構成では、全 $C_c^\infty$ を含む通常L² domainと線形性が不可欠。
候補からRHを導いた後にだけ、零点評価を非負sampling形式にする。
規格化 $R^{-1}\psi(x/R)e^{-i\gamma_0x}$ はL²で0へ収束する一方、
評価ベクトルは1つの多重度ブロックに収束する。
Schwartz評価 $(1+|\gamma-\gamma_0|)^{-2m}$ と零点数 $O(T\log T)$ はm≥1で可算和の支配を与える。
値域の完備性で非零極限が存在し、closabilityと矛盾する。固定窓にはこの列を入れられない。

coercivityでは規格化が $R^{-1/2}$ であり、$t_0$ は零点高度でない実数を選ぶ。
離散性から距離δ>0。Schwartz減衰で $R\sum|\Psi(R(\gamma-t_0))|^2=O(R^{1-2m})\to0$。
両候補はRHを否定せず、余分なglobal L²要求だけを否定する。

## 実Weil交差項の係数確認

$a=\log3$ の周りに相関を置いた場合、prime3の評価は1回だけなので
寄与は $-\log3/\sqrt3$。係数2を付けてはならない。
極項とarchimedean項から

$$K(v)=2\cosh(v/2)-\frac{e^{v/2}}{e^v-e^{-v}}
=2\cosh(v/2)-\frac{e^{-v/2}}{1-e^{-2v}}$$

となる。$K(\log3)=23/(8\sqrt3)>0$。
実験のFFT convolutionは今回のψが実偶なのでautocorrelationと一致し、ゼロpaddingも十分。
一般の複素/非偶ψへ変えるときは反転共役が必要。

$\epsilon\le1/64$ ならsupportは $(\log2,\log4)$ 内で、素数冪3だけが入る。

$$|K(v)|\le 2\cosh(\log4/2)+\frac4{3\sqrt2}<\frac72,
\qquad\|h_\epsilon\|_1\le2\epsilon.$$

したがって $|b+\log3/\sqrt3|\le7\epsilon$。
$\log3>1$, $\sqrt3<2$ を用いれば $|b|>25/64$。
窓差分の2次元行列式が負という結論は、この解析上界で認証できる。
数値小数の全桁を保証したという意味ではない。

## 監査で修正した表現

- jump energyのコードは各差分ノルムを独立積分せず、恒等式右辺を評価する。記述を修正。
- Gaussianの幅を明記。厳密なclosed-form値と8系統実験の別の幅を混同しない。
- Nakamura2015 Theorem 1.2は通常のinfinitely divisibleではなく
  **pretended-infinitely divisible**。∀σ∈(1/2,1)という量化も維持。
- positive ground functionと非負ground energyを別の前提に分離。
- MellinのFourier負指数と主ノートの正指数の対応を明示。
- 数値実験の負値をWeil負値またはRH反例と呼ばない。

## 未実施（第1巡終了時）

このトラックの追加解析はLean未形式化。既存Lean6宣言の検証範囲は増えていない。
既存プレプリントの全証明・計算証明書の独立再現は未済。
新規性の主張も、主グラフでの新しいRH入力への採用も行わない。

## 第2巡の追記: Groskin有限系

2026-09-29、checkpoint02で限定再現を追加した。
BUILDERは辞書と規約、DESTROYERはtailと区間計算、LITERATUREは公開packageの版・checksumを独立監査。
rootは原著閉形式を使わないArb直接積分からc13,N4の9次行列を認証し、原著再実行と照合。
全9pivotが正で、数値精度を理由とする不明判定を成功へ読み替えていない。
係数・符号・変数変換・Cor3.3左端の表記上の問題を採用公式から分離した。
詳細は `proofs/audits/groskin-computation.md` と関連3監査。
原著の401次計算の再現、全窓正値性、追加Lean形式化は未済。

## 第3巡: 固定窓の全mode認証

`proofs/audits/window-half-certificate.md` の解析・数値境界をBUILDERとDESTROYERが別々に監査。
root192bit、DESTROYER224bitの2実行と、保存行列への別Cholesky検査が通過。
全n≥64のtailと交差項を明示的に覆い、support[-1/2,1/2]の全complex form-domainで
Q_W≥9×10^(−8)||f||²を認証した。5成分は別adaptive積分でも包含一致。
Zhuの未取得head証明書や添付着想資料を前提にしていない。
この局所結果のみT090へ採用。RH全体の監査A/B/C、新規性、全窓正値性は未達。


## 第4巡: joint symbol と固定積imbalance

BUILDERは一般tail floorの還元・作用素順序・形式極限を直接証明し、root実装の全115995区間を
別のprime-power列挙で224bit再評価した。DESTROYERはcutoff仮説の5厳密負区間とscannerを監査。
rootはgの偶性に関する表現をg(|t|)へ修正し、補助g-floorの失敗とPsi-floorの失敗を区別した。
5固定窓の高周波下界だけを採用し、全Q_W正値性や主グラフへの新規合流とはしない。

固定積imbalanceはrootの224bit検査、BUILDERの収束・Hessian・Weil符号導出、DESTROYERの
解析的反例、LITERATUREの既知性調査を照合した。Euler差分公式は収束域に限定し、
positive-measure toyの零点はcosh恒等式で証明する。区間の零包含を等号の証明と呼ばない。
全ξ零点でのenergy消滅はRH同値なので、ユーザーの停止条件に従い候補を終了した。
構造反例はRH反例ではない。今回の追加Lean宣言は0、主グラフの新規合流も0。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/groskin-computation.md`](../../audits/proofs/audits/groskin-computation.md)
- [`proofs/audits/window-half-certificate.md`](../../audits/proofs/audits/window-half-certificate.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `research/source_inspection` — SOURCE REFERENCE NOT INCLUDED
