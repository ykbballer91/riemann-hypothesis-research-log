# Phase 3 — 25件の固定seed traceability監査

**STATUS: RIEMANN HYPOTHESIS OPEN**

対象は出版物のclaim scopeと出典対応であり、原論文や保存された全証明の再証明ではない。過去の数値スクリプトは再実行していない。

## 抽出方法

固定seed 20260930、Python random.Random、category順 PROVED / FALSE-REJECTED / OPEN / KNOWN / NUMERICAL、各categoryのIDをソートして5件ずつ重複なしで抽出した。母集団は19 trackに対応する52件の代表的claimで、全keyword occurrencesとは異なる。母集団・抽出順・原文quote・hashは [claims inventory](phase3_claims_inventory.json) に保存した。このsampleを数学全体の正しさの統計的評価とは扱わない。

各行で公開trackの明示的canonicalリンクを辿り、export manifestのexport SHA-256およびread-only原資料のsource SHA-256と照合した。リンク先の存在だけでなく、肯定・否定・条件・数値のscopeが同じかを確認した。

| ID / category | 公開ページ → canonical原資料 | 保存根拠 | scope確認 |
|---|---|---|---|
| P13 / PROVED | [Track 13](../docs/tracks/13-restoring-force.md) → [原資料](../archive/reports/research/arithmetic_restoring_force.md) | 原資料 line 163:  U(a,t)&amp;=2\int_0^\infty\Phi(x)\cosh(ax)\cos(tx)\,dx,\\ | PASS — cosh/sinh恒等式の正確さ。線外零点の不可能性を結論しない。 |
| P12 / PROVED | [Track 12](../docs/tracks/12-mobius-closure-audit.md) → [原資料](../archive/reports/research/strategy_reset_arithmetic_inventory.md) | 原資料 line 128: このためC1/C2はこのclassで一意に解け、解はもとの \(R,A\) そのもの。実際、 | PASS — 指定past-Gaussian classでの一意性。右向き安定性を含まない。 |
| P09 / PROVED | [Track 09](../docs/tracks/09-arithmetic-comma.md) → [原資料](../archive/reports/research/arithmetic_comma_prime_log_flow.md) | 原資料 line 47: \boxed{A_P(\log X)=\int B_P(z)\overline{C_{P,X}(z)}\,dm(z).} \tag{A1} | PASS — finite cutoffと収束域を保持。critical stripでの評価を追加しない。 |
| P10 / PROVED | [Track 10](../docs/tracks/10-weighted-prime-half-space.md) → [原資料](../archive/reports/research/weighted_prime_halfspace.md) | 原資料 line 154: \le {m-1\choose\lfloor(m-1)/2\rfloor}.}                    \tag{10} | PASS — 一般downsetのcentral-binomial bound。算術signed cancellationの新上界ではない。 |
| P18 / PROVED | [Track 18](../docs/tracks/18-even-l2-cyclicity.md) → [原資料](../archive/reports/research/full_ground_capture/cyclicity.md) | 原資料 line 12: 2026-09-30。**RH は OPEN。K IS CYCLIC IN EVEN L2: PROVED.** | PASS — even L2での密度。form core・moving-ground rateは別。 |
| F02 / FALSE-REJECTED | [Track 02](../docs/tracks/02-generator-boundary.md) → [原資料](../archive/reports/research/generator_boundary_hypothesis.md) | 原資料 line 55: なので、RH下でもGのL²固有値にはならない。自由度はresonanceの実部と増大率に残る。 | PASS — L2 eigenvalueとscattering resonanceの混同を棄却。RHへの反例ではない。 |
| F15 / FALSE-REJECTED | [Track 15](../docs/tracks/15-common-parent.md) → [原資料](../archive/reports/research/common_parent_variational_principle.md) | 原資料 line 29:    stationary pointですらない。 | PASS — 指定h0/h4 mixtureのstationarityを棄却。未知の全parentを排除しない。 |
| F12 / FALSE-REJECTED | [Track 12](../docs/tracks/12-mobius-closure-audit.md) → [原資料](../archive/reports/research/strategy_reset_arithmetic_inventory.md) | 原資料 line 136: しかし一意性は安定性ではない。反例は \(a&gt;1,L&gt;0\) の有限遅延方程式 | PASS — finite-delay toyがcausality⇒stabilityを反証。actual zetaの不安定性を主張しない。 |
| F07 / FALSE-REJECTED | [Track 07](../docs/tracks/07-dyadic-arithmetic-reduction.md) → [原資料](../archive/reports/research/dyadic_arithmetic_reduction.md) | 原資料 line 183:                          W\cap C_c^\infty(\mathbb R)=\{0\}.\tag{9} | PASS — 指定Wに対するcompact-support foldingの障害。全代表元構成の不可能性ではない。 |
| F10 / FALSE-REJECTED | [Track 10](../docs/tracks/10-weighted-prime-half-space.md) → [原資料](../archive/reports/research/weighted_prime_halfspace.md) | 原資料 line 163: threshold の margin を保つ任意小の rationally independent perturbation でもこの値は変わらない。distinct subset sums や generic irrationality 自体は利得にならない。 | PASS — perturbed thresholdのsynthetic反例。actual prime logsについての包括的不可能性ではない。 |
| O18 / OPEN | [Track 18](../docs/tracks/18-even-l2-cyclicity.md) → [原資料](../archive/reports/research/full_ground_capture/cyclicity.md) | 原資料 line 268: この定理は、任意の **固定された** 偶 L² 関数を有限微分結合で任意精度まで近似できることを述べる。必要次数・係数・conditioning の一様評価は与えない。変化する ground state への定量近似、Weil form norm での core 性、複素 Fourier strip 上の収束は出ない。 | PASS — qualitative L2 densityからform normへの未証明移行。 |
| O15 / OPEN | [Track 15](../docs/tracks/15-common-parent.md) → [原資料](../archive/reports/research/common_parent_variational_principle.md) | 原資料 line 23: 適切な同時極限での \(\varepsilon/\Delta\to0\) は証明していない。 | PASS — 必要な同時極限におけるactual excess/gap estimateが未取得。 |
| O02 / OPEN | [Track 02](../docs/tracks/02-generator-boundary.md) → [原資料](../archive/reports/research/generator_boundary_hypothesis.md) | 原資料 line 164: **Exact missing lemma:** 標準算術初期値を用いた全高さ一様の逆向き評価。 | PASS — 標準算術初期値の特別なtime-zero confinementが未証明。 |
| O17 / OPEN | [Track 17](../docs/tracks/17-hierarchical-selection.md) → [原資料](../archive/reports/research/hierarchical_selection.md) | 原資料 line 213: 固定mの定数をm→∞で一様とみなさず、未解決のactual full groundをrestricted最小状態で | PASS — fixed-m constantsはgrowing mへ一様化されていない。 |
| O07 / OPEN | [Track 07](../docs/tracks/07-dyadic-arithmetic-reduction.md) → [原資料](../archive/reports/research/dyadic_arithmetic_reduction.md) | 原資料 line 173:  \forall\epsilon&gt;0\ \exists C_\epsilon:\quad | PASS — 独立subexponential arithmetic estimateは得られていない。 |
| K04 / KNOWN | [Track 04](../docs/tracks/04-arithmetic-polarization.md) → [原資料](../archive/reports/research/phase4_arithmetic_polarization.md) | 原資料 line 67: Néron–Tate heightと結び付く。これは独立なARITHMETIC/GEOMETRIC positivity。 | PASS — Faltings-Hriljac/heightのcurve setting。zero quotientとの同定はない。一次原版未取得という原記録の出典範囲も保持。 |
| K05 / KNOWN | [Track 05](../docs/tracks/05-continuous-scale-flow.md) → [原資料](../archive/reports/research/continuous_scale_flow_frobenius.md) | 原資料 line 37: これは&#91;Connes–Consani 2024, Thm 1.1&#93;(https://arxiv.org/pdf/2401.08401v1)、&#91;2025, Prop 3.4&#93;(https://arxiv.org/html/2501.06560v1#S3.SS1)の既知の構成である。pによる乗法は、pで不分岐な最大abelian拡大上の arithme | PASS — 固定版CC mapping-torus theorem。positive-r returnのp^-1向きとlocal weight-zero scopeを保持。 |
| K10 / KNOWN | [Track 10](../docs/tracks/10-weighted-prime-half-space.md) → [原資料](../archive/reports/research/weighted_prime_halfspace.md) | 原資料 line 68: これは既知である。de la Bretèche–Tenenbaum の原典 p.3、式(1.9)–(1.10)直後にも非正整数で全係数が消えることが明記されている。&#91;Remarks on the Selberg–Delange method&#93;(https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf) | PASS — 既知Selberg-Delange local coefficient。global remainder cancellationには昇格しない。 |
| K14 / KNOWN | [Track 14](../docs/tracks/14-local-to-global.md) → [原資料](../archive/reports/research/local_to_global_zero_confinement.md) | 原資料 line 55: &#91;BCKV I, Theorem 1 の二証明&#93;(https://kurlberg.github.io/eprints/lrh1.pdf)。 | PASS — BCKV I Theorem 1の指定Hermite local family。任意local factorsのglobal gluingを含まない。 |
| K15 / KNOWN | [Track 15](../docs/tracks/15-common-parent.md) → [原資料](../archive/reports/research/common_parent_variational_principle.md) | 原資料 line 112: 単純groundと \(\Delta&gt;0\) のもとで、固有vector展開により厳密に | PASS — simple groundかつpositive gapを前提にする標準Rayleigh角度評価。gapの確保は別。 |
| N10 / NUMERICAL | [Track 10](../docs/tracks/10-weighted-prime-half-space.md) → [原資料](../archive/reports/research/weighted_prime_halfspace.md) | 原資料 line 241: - 最初の6素数の全720順序：\(X=100\) の最終値は4で不変、途中の最大振幅は順序により4または5。これは6素数 subsystem で、actual \(M(100)=1\) とは区別。 | PASS — 有限整数・順序検査。6素数の切断値をactual Mertens全体と同一視しない。 |
| N13 / NUMERICAL | [Track 13](../docs/tracks/13-restoring-force.md) → [原資料](../archive/reports/research/arithmetic_restoring_force.md) | 原資料 line 239: 50桁の128点grid、一部80桁との照合、中心曲率16点、既知零点近傍、theta二積分5点を診断した。first-derivative signに反する点は見つからなかったが、それはRHやglobal signの証明ではない。log曲率の負値とprime側の反対符号は、それぞれ解析的反証も伴う。&#91;実験結果&#93;(../../../artifact | PASS — 50桁有限gridの非認証診断。全域符号の証明ではない。 |
| N16 / NUMERICAL | [Track 16](../docs/tracks/16-rate-history.md) → [原資料](../archive/reports/research/rate_history_selection.md) | 原資料 line 71: Qは448-bit Arb assemblyのmidpoint、固有解析は100桁。 | PASS — Arb assemblyのmidpointを固有値診断に使用。interval eigenvalue certificateではない。 |
| N11 / NUMERICAL | [Track 11](../docs/tracks/11-global-remainder.md) → [原資料](../archive/reports/research/global_remainder_beyond_all_orders.md) | 原資料 line 331: - actual Möbius Gaussian 和と右側逆変換：3 点、級数 tail と縦線 tail の明示上界を照合。 | PASS — 3点の数値逆変換。一般定理の多重零点許容と単純零点を使う診断を区別。 |
| N09 / NUMERICAL | [Track 09](../docs/tracks/09-arithmetic-comma.md) → [原資料](../archive/reports/research/arithmetic_comma_prime_log_flow.md) | 原資料 line 160: &#91;実験コード&#93;(../../../artifacts/research/arithmetic_comma/experiments/check_phase_bridge.py) と &#91;結果&#93;(../../../artifacts/research/arithmetic_comma/experiments/results.json) を保存した。sub | PASS — 有限phase sampling。全scale・identity characterの主張へ拡張しない。 |

## 結果と限定

25/25件でリンク・export hash・原資料hash・scope対応が一致した。FALSE-REJECTEDは指定推論または模型の棄却でありRHの反証ではない。KNOWNは外部入力への帰属であり新規性の認定ではない。NUMERICALは有限診断であり一般定理の代用ではない。

Priority 2は母集団に含めたが、このseedの25件には選ばれなかった。したがって [Track 19](../docs/tracks/19-finite-even-head-spanning.md) を別途全項目照合し、fixed-head exact span、fixed-N eventual minimal prefix、有限exception、2件のraw-coordinate interval certificateとphysical-Gram診断の区別を確認した。joint-limit・growing-order・full-ground capture・ES・G*・RHへの拡張は記載されていない。

初回に未収録だったPriority 2は追加済み。Track 18の「当該updateではPriority 2を行っていない」はdated scopeとして正しく、後続ページへリンクされている。

本確認は公開snapshotに対するもの。対象ファイルのhashはJSONに固定した。以後本文を変更する場合は影響する行を再確認する。
