**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/one_prime_topology_matrix.md` · Original SHA-256: `685247c8ae6a78ab3939d4206b6aabd0a6497c6582eba1a6fbd65cfbb5f91a75`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# One-prime topology / return matrix

2026-09-29。p=2。列「全零点保持」は既知の算術test quotientとの比較を含む。単にcritical-lineの任意周波数を保持するだけならNOとする。新規性・RH証明は主張しない。

| ID / topology・構成 | source / quotientの順序 | zero functional continuity | T₂反復の確認範囲 | 未証明または反例 | 判定 |
|---|---|---|---|---|---|
| OP1 全指数重みnuclear Fréchet商Q | actual test E→arithmetic range→closure→quotient | 全ρおよびj<mρのjetsを保持 | q_N(Tⁿx)≤2^(N|n|)(1+|n|log2)^N q_N(x) | nuclearity/個別連続性は全nのsubequicontinuityでない | 既知spaceを採用、growth未達 |
| OP1b q₁によるX₁ | Q→ker q₁を割る→Banach完備化 | 全ρで|ℓρ|≤4q₁。finite jetsも保持 | T±1 bounded invertible、||Tⁿ||≤2^|n|(1+|n|log2) | full Qの単射性、no-extra-spectrum、type0未証明 | 限定Level2、主要集中先 |
| OP2 bare L² | quotient-firstでも同じL² normならcompletion quotientと等長 | 評価は非有界、actual rangeが稠密 | ambient translationはunitary | zero quotientが消える | KILL |
| OP2b exponential H_a | arithmetic quotient seminormを先に定義可 | a>|Reρ−1/2|で保持 | ambient exact norm2^(a|n|)、商には上界としてのみ移る | a→0で評価を喪失 | 改善機構なし |
| OP2c complex interpolation | [H0,Hk]_θ=Hθk | 同じ閾値θk>|δρ| | exact ambient exponentθk log2 | θを反復数ごとに変更すると同じspaceでなくなる | KILL |
| OP2d real (θ,2) interpolation | quadratic K-functional→weighted L² | complexの場合と同じ | 等価normなので指数率は同じ | zero retention endpointの破綻 | KILL |
| OP2e scaling Sobolev | 有限個の∂tを標準normに追加 | exponential threshold不変 | 2^(a|n|)のまま | derivativesはtime momentsと別 | 単独修復KILL |
| OP2f polynomial/Schwartz | 標準moment seminormの弱いtopology | imaginary-axis evaluationは保持、線外は非連続 | polynomial power growth | 全actual zero retentionを主張するとRHを含意 | 未確認retentionを採用しない |
| OP2g Beurling/GRS | submultiplicative weightの診断 | 線外Laplace評価は非有界 | GRSでsubexponential | 成長率を設計して評価を落とす偽解決 | 全零点案KILL |
| OP2h Hardy strip | 両境界Plancherel | strip内部の複素評価 | exponentはstrip幅に依存 | stripを潰すと評価喪失 | KILL |
| OP2i half-plane Hardy | 片側Laplace space | 負実部のbounded dual評価あり | 右shiftはisometric semigroup | ontoでなく逆群がない | bilateral案KILL |
| OP2j fixed Paley–Wiener | finite support/type | finite typeでは全複素評価有界 | returnでsupportが動く | 同じspaceを保存しない | KILL |
| OP2k weighted nuclear/Gelfand–Shilov/modulation | 族の全理論を構築せず一般補題でscreen | 線外評価を残すならそのorbitに指数下界 | spaceごとの証明が必要 | 名前の変更だけではretentionとrateを同時改善できない | 算術指定なしの新候補へ拡張しない |
| OP3 local Haar forward J | JU=T₂J、各ℓρJ bounded非零 | このpullbackが成立すれば十分 | global norm boundなしでも指標を制御 | actual J未構成、literal sourceはtorsionも強制 | 条件付きlemmaのみ |
| OP3b reverse injective J | JT₂=UJ | injectivityだけではbounded dualを移せない | weighted bilateral shiftは指数成長 | norm下界なし | KILL |
| OP3c unitary similarity | 同じHilbert spaceで二側uniform boundが前提 | 元のbounded dualを保持 | similarityならuniform | 算術的similarity未構成、subexpからは出ない | 算術橋なし |
| OP3d unitary dilation | compression、forward powers | exact intertwinerとは違う | 負powersはadjoint、inverseでない | scalar contractionが反例 | KILL |
| OP3e product formula | finite/infinite norm積を固定 | actual quotientのnormとの比較なし | hyperbolic expansion/contraction許容 | determinant1でもnorm指数成長 | KILL |

## 必須Destroyer test対応

| test | witness / 結論 |
|---|---|
| off-line synthetic character | translationのℓα+iγ：retentionと両方向subexpが両立するならα=0。仮定外の評価を捨てた解を検出 |
| bilateral weighted shift | exp重み空間→裸のℓ²に連続単射でintertwineしても元のnormはexp成長 |
| hyperbolic cocycle | diag(5/4,4/5)：product/involution保存と指数成長が両立 |
| dense quotient collapse | completion-order同定。synthetic Gaussian補正でもoff-axis評価kernelがL²で稠密になることを確認 |
| unbounded evaluation | H_a threshold、a=0のFourier評価、polynomial/GRSの線外評価 |
| non-equivalent topology | n依存interpolation weight、異なるclosure、weak/strong quotientの取り違えを棄却 |
| artificial weight | zero-side定義、orbit supremumの有限性を未証明で仮定、不変seminormで指標を排除する設計を不採用 |
| hidden RH equivalence | 線外character不在やWeil positivityを入力にしない。RH⇒fixed-topology growthは自動とはしない |

## 最小の残差

q₁が全ℓρを支配するため、全体の正metricも全seminormの一様制御も必須ではない。

    ∀ ε>0 ∃ M,Cε  ∀ n∈Z,x∈Q:
        q₁(T₂ⁿx) ≤ Cε 2^(ε|n|) q_M(x)

この一つの出力seminormに対する両方向評価で十分。今回これを保証する、RHと独立な算術的representative/cancellation estimateを得ていない。
