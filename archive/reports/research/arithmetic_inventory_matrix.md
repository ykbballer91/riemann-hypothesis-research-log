**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_inventory_matrix.md` · Original SHA-256: `6c883f7be7a591722a4ea13bfefdbc92c08f4d40aa2f04d9c9d7a46000e4e247`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic inventory：過去トラックと未使用入力の対応表

2026-09-30。RH OPEN。監査のみ。既存ファイル・state・proof graphは変更しない。

## 1. 全トラックのdependency / failure matrix

「残る情報」欄は未証明の目標を使用可能な算術入力へ昇格するものではない。関連する未適用分野と、必要だったが未取得の比較を分けて記す。

| Track / 保存された証拠 | 制御対象 | 本質的に使用したactual arithmetic | 戻った義務 | 具体的no-go / counterexample | 残る情報と再開禁止の理由 |
|---|---|---|---|---|---|
| [Phase I](strategy_review.md)、[support audit](../../audits/proofs/audits/support-propagation-reduction.md) | 全supportのWeil form、finite→infinite positivity | explicit formula、全prime powers、Gamma/pole、theta、Poisson、divisor/Mangoldt | 全窓正性、算術Schur complementの符号。exact Weil版はRH同値 | 小pivotから負Schur complement、有限PSDから全域への飛躍、actual GCD critical form非closable、Mangoldt form負方向 | bilinear/correlation評価は本質的には未適用。しかし具体的符号比較なしでfinite窓、GCD、正metricを増やさない |
| [Phase II](generator_boundary_hypothesis.md) | generatorのrangeをcritical spectrumへ拘束 | modular scatteringのactual Euler/Gamma、theta/Newman、prime m-germ | Herglotz性、全scattering resonanceの位置、Newman threshold | 自己共役modular Laplacianのzeta modesはL² eigenvaluesでなくresonances。cutoffは全零点を失う | positive generatorとactual全零点のfaithful比較は未取得。一般self-adjointnessの再実装禁止 |
| [Phase III](phase3_missing_frobenius.md) | finite-field Frobenius+purityの数体差分 | CCM算術商、trace、idèle scaling、Gamma determinant、finite-field proof spine | actual quotient上の独立polarization。Weil形式正性ならRH同値 | 特定ambient L²商は0。q=9のpositive closed-point-count/duality模型はnonpure | 幾何program全体は未否定だが、未知positive geometryを一個の新公理と数えない |
| [Phase IV](phase4_arithmetic_polarization.md) | actual零点空間の正pairingとadjoint | adelic Haar、product formula、Arakelov、height、Fourier、actual test range | positivityとzero retentionを同じspaceで実現 | dense radicalを消すclosable positive formは0。actual pole-free Fourier twistに負方向 | 他spaceの正性は未使用の零点情報ではない。metric/star変更だけで再開不可 |
| [Continuous Scale Flow](continuous_scale_flow_frobenius.md) | normalized scalingの全零点growth | actual prime mapping torus、Haar、CCM quotient、prime-power trace | faithful common-space return control | local Haarに有限周波数帯の無限多重度、指定した算術normal model上のp-adic valued exponent +1、hyperbolic conserving cocycle | 局所Frobenius→全零点のbounded intertwiner未取得。局所unitarity再説明禁止 |
| [One-Prime Return](one_prime_return_theorem.md) | p=2のsubexponential return | actual quotient、全zero functionals、標準q1、Gaussian witness | zero retentionとsubexponential controlの両立。operator版の逆含意は未証明 | 弱completionは評価を失い、強重みは指数growth、interpolationは欠落を補わない | 係数側の具体的相殺estimateが必要。topology新設・similarity定理名だけでは不可 |
| [Dyadic Reduction](dyadic_arithmetic_reduction.md) | actual relationsによる小代表元 | 全整数Möbius inversion、Poisson、pole-free correction | fixed algorithmの準指数endpointはRH同値 | compact foldは不可。無条件代表元は \(2^{n/2}(1+n)\) まで | μの深い定量評価は未使用部分が残る。closureそのものは既に使用済み |
| [Prime Complex](prime_complex_parity_pairing.md) | even/odd pairingのsigned defect | unique factorization、divisor simplex、toggle2、birth/death | 残る線形数のcritical cellsの符号相殺＝Mertens | total Betti/critical count \(\sim2X/\pi^2\)、shared parents、incidence matching障害 | additive μ correlationsは未適用。状態数削減・同じMorse/index再記述は禁止 |
| [Arithmetic Comma](arithmetic_comma_prime_log_flow.md) | phaseとactual cutoff readoutの相関 | Bohr lift、prime logs、integer gaps、Euler、Halász | distinguished point/readoutのsigned estimate | \(F_X(z)=C_X(-z)\) は同Haar lawでもidentity値が異なる。全time supremum線形 | uniform additive boundsは別入力として今回監査。marginal/time平均・generic dephasingへ戻らない |
| [Weighted Half-Space](weighted_prime_halfspace.md) | weighted Boolean full parity coefficient | actual log p、prime recursion、SD、finite tilt、PNT | endpoint remainder、tilted covariance、signed boundary estimate | generic threshold boundはcounting scaleで弱い。全SD係数消失でもMは残る | Type I/II、相関定理は名前以上の適用なし。unsigned boundary/CLTからsigned boundへの飛躍禁止 |
| [Global Remainder](global_remainder_beyond_all_orders.md) | faithful Gaussian scalarのgrowth | actual μ、逆ζ、Gamma、multiplicity、固定contour | \(A(u)=O_\epsilon(e^{\epsilon u})\iff RH\) | central/right inverseの違い、finite-jet対称反例、無限左移動発散、actual Aは非L² | 未適用の深い係数定理を今回監査。subexp/temperedを新仮定にして再開不可 |

## 2. 同じ義務へ戻る五分類

| 大分類 | 既に得たもの | 最後に要求したもの | 同値性の注意 |
|---|---|---|---|
| Geometry / positivity | exact arithmetic form、別対象上の真正な正性 | 同じactual全零点対象の全称符号／faithful正性 | Weil/Herglotzの指定形式はRH同値。未知幾何program全体まで同値と断定しない |
| Scale / dynamics | \(\ell_\rho(T_2^n x)=2^{n(\rho-1/2)}\ell_\rho(x)\) | retained modesの指数growthを消す算術estimate | scalar Gaussian/fixed dyadic endpointは同値。全operator topology条件はより強い可能性 |
| Combinatorial cancellation | exact index、recursion、threshold identity | actual cutoffのsigned discrepancy | 全 \(\varepsilon>0\) で \(M(X)=O_\varepsilon(X^{1/2+\varepsilon})\) はRH同値。\(O(\sqrt X)\) やmatching全体の存在との同値は主張しない |
| Phase / harmonic | exact integral reconstruction、distribution facts | 指定readoutでの符号付き相関 | marginal phase lawは不足。平均とpointwiseを同一視しない |
| Complex analytic | 局所bulk消失、faithful poles、正当なcontours | actual remainderの大域growth | 全ε subexpはRH同値。bounded/tempered/L²は同じ条件ではない |

同じ壁は「算術的に正確な表現は作れるが、全スケールの符号付き相殺を独立に制御できない」こと。単にすべてを一つの未証明metricと呼ぶのも不正確で、後半ではmetric不要のscalar boundまで弱めている。

## 3. 算術入力の棚卸し

I=独立性（RH不使用とzero-side不使用は別）、A=actual coefficientsへの関係、N=過去ログに対する未使用性、Q=定量強度、B=Gaussian/closureへの接続。数値スコアは証明可能性を表さないため使用しない。

| ID / 算術情報 | I・A | N：過去の使用状況 | Q：現時点の強度 | B：接続と判定 |
|---|---|---|---|---|
| D1 \(\mu*1=\varepsilon\)、Dirichlet inverse | exact、actual | Dyadicで本質的に使用済み | identity・左historyからの一意性 | C1/C2そのもの。新しい安定性入力ではない |
| D2 higher convolution powers、\(d_k\) | exact、actual | 基本代数は使用済み、全階層の記帳は今回明示 | ζの積／逆積を増やす | 同じ畳み込みを反復するだけで独立条件は増えない |
| D3 \(\mu*\log=\Lambda\)、\(D\mu=-\mu*\Lambda\) | exact、actual | Phase Iのprime/log generatorで使用済み | 正forcingのidentity、未制御signed inverse | ユーザー案の \(-\Lambda\) は \(\mu*\log\) について符号誤り |
| D4 \(\Lambda_k=\mu*(\log)^k\)、高階moment | exact、actual、非負性も無条件 | 全階層の適用は未記帳。材料は使用済み | positive RHS、ただしgrowth upper boundなし | ζ導関数/ζ。新しい \(\zeta^{(k)}(\rho)=0\) 条件を課さない |
| D5 u微分・shift微分 | exact、actual | Gaussian/scale側で使用済み | forcingの微分、同じpoles | closureの帰結。独立データではない |
| A1 bilinear/hyperbola | actual、RH不要な既知分解 | 保存ログで主要estimateとして未適用 | 分解だけでは無相関を保証しない | \(\sum_{mn}\mu(m)a_n w(mn/x)\) の非振動部分が残る |
| A2 Vaughan/Heath-Brown、Type I/II | minor arcsは係数側の深い情報。全域版major arcはPNT/zero-sideを含む | 定理の定量適用は未使用 | 振動を持つ範囲は強い。全周波数ではlog-power級 | Candidate A：α=0・低周波が元の問題、Gaussianは都合のよいphaseを与えない |
| A3 short intervals pointwise | actual、無条件定理にも解析的入力あり | 未適用 | 指定された長さ範囲でlog-power、RH級ではない | \(h\asymp x\) の元Gaussianへ入れても新しいfixed-power savingなし |
| A4 short intervals almost all | actual、無条件の新しい情報 | 未適用 | 例外集合を許すo(h)／log saving | 全uのpointwiseへ移す率・例外制御なし |
| A5 narrower kernel | identityはactual、estimateは任意bounded係数にも成立 | 未使用の変形だが新入力ではない | \(\sigma=x^{-1/2}\) なら絶対値だけで正規化和bounded | u依存kernelへ変更。全正係数でも成功するためRH検出とは別 |
| C1 fixed additive Chowla | actualなら有用だが一般の必要強度は未解決 | 未使用、採用不可 | 予想を新前提にしない | μ(n)μ(n+h)の全h・weighted sumを無条件に供給しない |
| C2 log-averaged Chowla | actual、RHなしの定理 | 本質的な適用は未使用 | log averageのo(log X)、pointwise xの率とは違う | 剰余energyへのsharpな移行なし |
| C3 shift-averaged / higher correlations | actual、RHなしの定理 | 未使用 | 全h平均でo(HX)等。必要なX規模二重和の平方根precision不足 | Candidate C：offdiagonalをo(X²)へしても目標O(X^{1+2ε})ではない |
| C4 compact-window autocorrelation of A | exact actual double sum | 今回の新しい監査表示 | μ相関のsmooth two-variable weight | 無限energyは不可。uniform sliding-window energyを得ていない |
| A6 large / dual / spectral sieve | 無条件だが一般係数の二乗量も扱う | explicit applicationは未使用 | 周波数・character familyの平均 | distinguished targetの例外を除く追加estimateなし |
| A7 dispersion、progressions平均 | actual、定理ごとのmodulus範囲・exceptionが必要 | 未適用 | 平均moduliで強い。principal modeを含むglobal sumは別 | q=1またはprincipal characterを平均で解消しない |
| A8 fixed q / characters | actual、Dirichlet L zero-free/Siegel issuesを分離 | phase character一般論は使用済み、AP定理は未適用 | Siegel–Walfisz型log-power／twisted range | untwisted partが残る。principalを非principalへ置換不可 |
| P1 Halász / pretentious | actualに適用可、RH不要 | Arithmetic Commaで使用済み | black box比較関数はlog-scale | closure追加で新しい距離拘束なし、再開しない |
| P2 Kátai / Daboussi–Delange / BSZ | 条件付きorthogonality criteria、actualμに適用可 | 定量適用は未使用 | BSZは小さいprime-dilation correlationsから定量o(X) | raw Gaussianのp=2,3 dilation correlationは自然scaleで正定数。必要な一様仮定を満たさない |
| P3 Sarnak/disjointness | 証明済み対象は限定、一般命題は予想 | 未適用 | o(X)、一般に必要rateなし | closure用systemを新造しない。constant observableはPNT尺度 |
| Z1 zero-free/density | RHなしでもzero-side input | PNT/explicit-formulaで使用済み | 既知subpower error、global固定stripではない | 独立coefficient武器として再分類しない |
| H1 Davenport additive uniform estimate | actual、RH不要、major arcsに解析情報 | uniform versionの適用は未使用 | 任意固定log-power | \(\alpha=0\) を含む。Gaussian partial summationもPNT級 |
| H2 Mellin twist \(\sum\mu(n)n^{it}\) | actual、finite truncationではexact | phase平均は使用済み、uniform finite boundsは今回監査 | bounded/polylog tでPNT級。全t一様square-rootは既反証 | 無限非減衰級数をGaussian Fourier積分へ交換しない |
| H3 Dirichlet polynomial means/large values | unconditional、一般係数で成立する部分も多い | 平均原理は一部使用、深いestimateは未適用 | 平均t、exceptional large values | Gaussianの固定readout・低tへ移す新機構なし |
| H4 mollifiers | actualμを使用、ゼロ側の平均手法 | 未適用 | critical-line zeroの割合等、全零点ではない | truncated inverseの成功とfull faithful inverseのsubexpは別 |
| R1 random multiplicative/chaos | 確率モデルでは無条件、actualμへのtransferなし | heuristicとしてのみ比較 | expectation / probability | 固定all-minus prime assignmentを平均momentで制御不可 |
| R2 entropy/complexity | entropy decrement等は既知相関証明に使用 | 本質的適用は未使用 | quantitative theoremの範囲次第 | 「複雑だから相殺」禁止。今回Cの範囲以上のbridgeなし |
| I1 prime-factor operators/incidence algebra | exact actual subalgebra | divisor/Morse/Euler操作として使用済み | inversion、有限差分 | 新しい作用素名は新情報ではない |
| I2 gcd/lcm/unique factorization | actual | Phase I、Dyadic、Prime Complexで本質的に使用済み | exact divisor features、positivity、local relations | all-log independence以上の内容も既に使用した |
| I3 GCD sum inequalities | 無条件actual kernelのfinite bound | 構造使用済み、finite norm改善は再開理由なし | size依存の正kernel評価 | nonclosabilityとsigned-readout比較の欠落を回避しない |
| B1 causal infinite-delay / WH | C2自体はexact actual | 同じMöbius inversionは使用済み、因果解釈を今回明示 | 左historyで一意、安定性は別 | Candidate B：formal zerosはraw seriesのdomain外、stable inverseを仮定しない |
| B2 renewal tilt | actual正kernel、総mass∞ | finite Gibbsとは異なるが収束障害は共通 | tilt後 \(\sigma>1/2\) で有限mass | probabilityへの規格化はplus符号inverseをrenewalへ変えない。critical shiftで発散 |
| B3 canonical/minimal inverse | actualμからcanonical inverseはexplicit | DyadicとGlobal Remainderで使用済み | unique inverse、nonzero residue coefficient | minimal growthは証明されない。forcingがunstable polesを消す説明は非消失Gaussianと矛盾 |

根拠と定理の量化は [bilinear監査](strategy_reset/notes/bilinear_and_uniform_estimates.md)、[closure監査](strategy_reset/notes/closure_causality.md)、[correlation監査](strategy_reset/notes/correlations_and_short_intervals.md)、[補助情報監査](strategy_reset/notes/inventory_scope_and_misc.md) に固定する。

## 4. 未使用入力と生存候補を分ける

実際に未適用だった情報は残っていた。特に深いType I/II・平均相関・short-interval・progression平均の定理は、これまでの座標変換・generic positivity・phase distributionと同じ内容ではない。

しかし「未適用の定理がある」と「今回の成功条件を満たす次トラックがある」は異なる。今回確認した適用では、全uのpointwise bound、平方根precision、例外除去、非振動部分のいずれかが欠ける。

| 候補 | 既知の独立情報 | 成功条件への不足 | 最終判定 |
|---|---|---|---|
| A Bilinear / Type I–II | あり、過去に本質的未適用 | 全周波数の非振動成分でPNT型を超えるpointwise評価なし | NOT_JUSTIFIED_FOR_NEXT_TRACK |
| B Causal closure / Wiener–Hopf | closureと一意性は厳密だが独立の安定性情報ではない | 因果性からforward subexpは出ない。raw homogeneous modeの解釈にもdomain訂正 | NOT_JUSTIFIED_FOR_NEXT_TRACK |
| C Averaged correlations | あり、過去に本質的未適用 | averagingの量化・率・weighted readout・pointwise移行が不足 | NOT_JUSTIFIED_FOR_NEXT_TRACK |

生存候補数は **0**。この監査の範囲での結論は **NO JUSTIFIED NEXT TRACK**。未調査の全数学を否定する意味ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/support-propagation-reduction.md`](../../audits/proofs/audits/support-propagation-reduction.md)
- [`research/arithmetic_comma_prime_log_flow.md`](arithmetic_comma_prime_log_flow.md)
- [`research/continuous_scale_flow_frobenius.md`](continuous_scale_flow_frobenius.md)
- [`research/dyadic_arithmetic_reduction.md`](dyadic_arithmetic_reduction.md)
- [`research/generator_boundary_hypothesis.md`](generator_boundary_hypothesis.md)
- [`research/global_remainder_beyond_all_orders.md`](global_remainder_beyond_all_orders.md)
- [`research/one_prime_return_theorem.md`](one_prime_return_theorem.md)
- [`research/phase3_missing_frobenius.md`](phase3_missing_frobenius.md)
- [`research/phase4_arithmetic_polarization.md`](phase4_arithmetic_polarization.md)
- [`research/prime_complex_parity_pairing.md`](prime_complex_parity_pairing.md)
- [`research/strategy_reset/notes/bilinear_and_uniform_estimates.md`](strategy_reset/notes/bilinear_and_uniform_estimates.md)
- [`research/strategy_reset/notes/closure_causality.md`](strategy_reset/notes/closure_causality.md)
- [`research/strategy_reset/notes/correlations_and_short_intervals.md`](strategy_reset/notes/correlations_and_short_intervals.md)
- [`research/strategy_reset/notes/inventory_scope_and_misc.md`](strategy_reset/notes/inventory_scope_and_misc.md)
- [`research/strategy_review.md`](strategy_review.md)
- [`research/weighted_prime_halfspace.md`](weighted_prime_halfspace.md)
