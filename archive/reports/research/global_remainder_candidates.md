**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/global_remainder_candidates.md` · Original SHA-256: `dcd255e20e42a7aec6400f8774889a339659813392d2e264ee798657a0a1a725`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Global remainder：三候補の比較と終了判定

2026-09-30。RH OPEN。独立トラック。最大三候補を保持し、第4候補へ移らない。

| 項目 | A：Gaussian global decomposition | B：completed two-sided closure | C：local annihilation / parameter transition |
|---|---|---|---|
| 固定対象 | 実係数 \(\mu(n)\) と固定 Gaussian の convolution | 実際の \(\Xi(z)\) と \(E(z)=e^{z^2}\)、右側積分路 | 実際の \(S_z(X)\)、SD係数 \(\lambda_j(z)\) |
| Exact arithmetic input | \(1/\zeta(s)=\sum\mu(n)n^{-s}\) in \(\Re s>1\) | Euler product、Gamma、pole factor の同じ対象での積 | \(\prod_p(1+zp^{-s})=\zeta(s)^zG(s,z)\) |
| 構成済み | bilateral transform、有限矩形、good-height grouped zero modes、固定左線 remainder | faithful right inverse、反射された左inverse、exact arithmetic kernel sum | 全 local coefficients消失、finite-jet反例、parameter derivative回復、double scaling |
| Kernel は零点依存か | いいえ、entire/nonvanishing | いいえ、entire/nonvanishing | 新kernelを作らない |
| 多重度 | degree \(m-1\) の多項式 mode を保持 | pole orderを保持、同じ residue rule | synthetic modelに追加多重度も許容 |
| 希望する新入力 | normalized remainder の全 \(\epsilon>0\) subexponential bound | 右側 inverse の tempered/subexponential bound | 消えたlocal seriesからglobal pole位置への拘束 |
| 実際に得た独立入力 | 固定左線 remainder の指数減衰。全modeの成長制御ではない | 負側急減衰。正側には従来の指数上界のみ | 有界 double-scaling parameter 上の既知一様漸近の帰結 |
| RH-equivalence gate | 正側 subexponentiality はRH同値 | temperedness⇒RH。逆向きは証明しない。多重度上限も必要 | endpoint remainder評価はMertens問題のまま |
| 主反例・障害 | 無限trivial residuesは項が0に行かない。L²も不可能 | 同一meromorphic式にtempered central inverseと増大right inverseが併存 | 任意有限jetを保つ軸外quartet模型。全analytic germ一致は逆に不可 |
| 旧トラックとの関係 | One-Prime Gaussianの非消失検出と重複する構造 | Phase II/IVのfaithfulness＋stability欠落と同型 | Weighted Prime Half-SpaceのSD端点を定量的に整理 |
| 決定 | CLOSED_EQUIVALENT_GROWTH_INPUT | CLOSED_NO_INDEPENDENT_RIGHT_SIDE_BOUND | CLOSED_NO_LOCAL_TO_GLOBAL_RESTRICTION |
| 成功レベル | 0：既知変換原理の適用 | 0：変換の定義域を含むno-go、既知原理 | 0：既知解析／一様SDの帰結 |

## A の具体的 falsifiable conjecture

候補 A1：「local SD coefficients が全消失し、Gaussian で平滑化すれば、normalized observable は subexponential」。

判定：局所消失と非消失 kernel だけでは根拠不足。actual zeta についての conclusion は RH 同値。synthetic finite-jet/even models は前提の一般論から global pole位置を制御できないことを示す。

候補 A2：「Gaussian が全方向の積分を減衰させるので、無限左移動後は全zero residuesだけでよい」。

判定：反証。自明零点の留数の対数は \(k^2-2k\log k+O_u(k)\) で正に発散。有限の左線を残す。

候補 A3：「faithful normalized remainder の finite energy が arithmetic stability の自然な弱条件」。

判定：反証。\(L^2\) は既知のcritical-line polesと矛盾する。boundednessやtemperednessと混同しない。

## B の具体的 falsifiable conjecture

候補 B1：「even transform の inverse はevenで、左右のgrowthが相殺する」。

判定：反証。右側積分路は反射で左側へ移り、差は留数である。実際の faithful right inverse は even なら負側の任意指数減衰が正側へ移り \(L^2\) となるため、無条件に非偶。

候補 B2：「imaginary-axis Fourier inverseがtemperedなら軸外poleはない」。

判定：反証。\(e^{z^2}/(z^2-a^2)\) の中央線 inverse は Schwartz。極 \(\pm a\) は存在し、right inverseにはその差が指数項として残る。

候補 B3：「同じ actual right inverse の temperednessを独立に算術表示から証明できる」。

判定：未達。exact Euler/Gamma formulaはできるが、その絶対値評価は指数的。temperednessを仮定することで問題を閉じない。RHからの逆含意も得ていない。

## C の具体的 falsifiable conjecture

候補 C1：「任意高次のjetを保ったまま軸外極を入れられない」。

判定：各有限次数について反証可能。偶・実 polynomial factor で指定 quartet を挿入できる。

候補 C2：「全Taylor coefficientsが同じでも異なるmeromorphic continuationを作れる」。

判定：一致定理により偽。有限jetと全germを混同しない。全消失するのはSDの係数写像。

候補 C3：「endpointのzero formal expansionをBorel変換すれば非zero remainderのStokes情報が自動的に出る」。

判定：根拠なし。zero seriesの通常Borel transformはzero。追加sectorやglobal singularity dataを入力する理論は別途必要で、今回構成していない。

候補 C4：「double scalingでendpoint remainderまで相対誤差付きに制御できる」。

判定：偽の推論。有界 \(c\) に対して scaled limit \(-ce^c\) は一様だが、\(c=0\) ではbulkが消え、additive errorの内側のMertens remainderは未評価のまま。

## Strategy review

三候補は別々の厳密なobjectを与えるが、actual arithmeticによる正側growth boundは一つも供給しなかった。新しいprime-specific cancellationを仮定せず導く矢印がない。既存の positivity、self-adjoint operator、Boolean pairing、phase distributionへ名前を変えて戻らない。

研究終了時点の最小欠落は、Gaussian convolution または completed right inverse の **符号付き算術和の大域評価**。それをRH同値条件として再掲しても進展とはしない。

本稿の exact no-go と構成例は再利用可能な negative knowledge として保存する。新しい公開定理の新規性認定、主証明グラフへの採用、RH実部境界の改善は行わない。
