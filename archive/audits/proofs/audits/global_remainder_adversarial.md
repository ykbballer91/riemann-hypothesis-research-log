**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/global_remainder_adversarial.md` · Original SHA-256: `af10e82e4b8e7084094d1ce01a8cb37a48e52eec21c1406b27ba1b53b2e2c232`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Adversarial audit — Global Remainder / Beyond-All-Orders

2026-09-30。範囲：本トラックの三候補。RH OPEN。過去ファイルの再監査完了を主張せず、過去ファイルを変更しない。

## 1. 証明上の destroyer tests

| Test | 検査・反例 | 結果 |
|---|---|---|
| identity theorem | 同じ全Taylor germを持つ異なる一価解析接続 | 不可。ユーザーの局所情報に関する広すぎる文言を限定 |
| arbitrary finite jet | \(Q_N=1+(z^2-1/4)^{N+1}(A+Bz^2)\) | 軸外quartetを追加可能。任意有限Nと同時全Nを区別 |
| symmetry and finite order | \(\widetilde\Xi=\Xi Q_N\) | 偶性・実対称性・order1を保持しても軸外零点を許す |
| actual-zeta fidelity | synthetic polynomial modification | Euler product不保持。実zetaへの反例とは扱わない |
| local annihilation | \(\lambda_j(-1)=h_j(-1)/\Gamma(-1-j)\) | h_j自体は消えない。Taylor全消失という誤記なし |
| absolute convergence | \(\sum|\mu(n)|\int\phi(u-\log n)e^{-\sigma u}du\) | 最初は \(\sigma>1\) で正当 |
| contour normalization | Gaussian kernelには \(1/s\) がない | simple residueに \(1/\rho\) を付けない |
| multiplicity | Laurent主部と \(e^{\rho u}P_\rho(u)\) | degree \(m-1\)、最高係数非零。simple zero仮定なし |
| pole/trivial bookkeeping | \(s=1,0,-2k\) | 前二者留数なし、後者は有限左移動に応じて保持 |
| infinite zero summation | good heights、genus1 product、Gaussian decay | 高さ別groupingを証明。個別絶対収束と並替えは主張しない |
| infinite left shift | trivial residue \(\exp(k^2-2k\log k+O(k))\) | 発散。左線remainderを捨てる候補をkill |
| quartet cosh claim | 実際のGamma/derivative coefficients | common amplitudeは出ない。cosh/sinh＋振動を維持 |
| cancellation among zeros | transformの非消失numeratorとholomorphy | 点ごとの下界や最大零点仮定を使わず処理 |
| scalar growth | 全ε subexponentiality | actual AについてRH同値。新しい入力にしない |
| boundedness | Laplace \(O(1/\epsilon)\) | 全零点単純性も要求。RHから導いていない |
| polynomial bound | Laplace \(O(\epsilon^{-d-1})\) | 多重度制約が追加される |
| temperedness | cutoff distributional Laplace | RHの十分条件、一様多重度上限。逆含意なし |
| unweighted L² | Cauchy–Schwarz \(O(\epsilon^{-1/2})\) vs pole | 実A・実Hで無条件に不可能 |
| contour reflection | \(H_{-c}(u)=H_c(-u)\) | H自体をevenとしない。横断留数を残す |
| fake stable inverse | \(e^{z^2}/(z^2-a^2)\) | centralはSchwartz、rightは増大。収束stripの違いを明示 |
| artificial projection | right objectをcentral Fourier/PVへ交換 | 不採用。算術的同定領域を変える |
| Gaussian dominance | 垂直減衰と水平増大 | 全方向rapid decayとは記さない |
| Borel/resurgence | zero formal series と nonzero remainder | 自動resurgence/Stokes論を採用しない |
| parameter derivatives | \(\lambda'_j(-1)=(-1)^{j+1}(j+1)!h_j(-1)\) | endpoint readoutと全parameter familyの情報量を区別 |
| double scaling | δ=c/loglogX、additive uniform error | 端点も一様なscaled limit。相対誤差へ不正変更なし |
| limit noncommutation | fixed-X polynomial vs large-X asymptotic | 規約なしの非可換極限を主張しない |
| novelty | Mellin inversion、SD、既知germ原理との比較 | 新規性未認定、success0 |
| fourth candidate | 三主要方向後のreview | 終了。同型第4候補なし |

## 2. 独立監査の範囲

- BUILDER：Gaussianノートを導出。有限矩形、multiple zeros、good-height estimate、fixed left line、growth conditionsを証明。
- DESTROYER：Gaussian good-height estimateのfinite factors/tail、L²反証を読み取り再導出しPASS。
- DESTROYER：completed two-sidedノートを導出。右／左／中央の逆変換、Gamma係数、tempered gateを証明。
- BUILDER：completed noteのStirlingの冪、反射と水平辺符号、quartetのsinh係数、actual Euler/Gamma expansion、cutoff Laplace、rational模型を独立読取監査しPASS。
- LITERATURE：局所germ、finite-jet synthetic model、一様SDとdouble scaling、Mellin/Darboux/Borelの適用範囲を一次資料と比較。
- ROOT：各ノートと総合稿を照合し、exact rationalモデルと数値contourを別に検算。全資料の定理を形式化したとの主張はしない。
- LITERATURE：Gaussianノートのgood-height finite part/tail、block summability、無限trivial residuesの通常級数発散、quartet係数・部分積分符号を追加の読取監査でPASS。
- DESTROYER：総合稿と実験コードを読取監査。J_Tの1/(2πi)を明示する軽微修正を指摘し、ROOTが修正。tail定数・多重度・growth hierarchy・double scaling・新規性の限定はPASS。

最終総合稿・実験コードへの追加読取監査結果は validation.json に記録する。各PASSは記した範囲だけを意味し、RHの証明監査PASSではない。

## 3. 実験と証拠の区分

再現コマンド（repo root）：

    .venv-cert/bin/python research/global_remainder/experiments/check_global_remainder.py

1. N=50000のMöbius係数をexact integer sieveで作成。u=-2,0,2のGaussian和を50桁計算。省略tailは単調関数の積分上界を用いる。
2. c=1.5, T=16の逆積分との相違は、級数tail＋Gaussian縦線tailの上界内。数値積分誤差を厳密区間で認証したという意味ではない。
3. a=-3,c=1.5,T=16,u=1の有限矩形で水平辺も含めた恒等式を計算。50桁表示で差0。これは実数としてのexact zeroの証明ではない。
4. 数値留数は最初の臨界線零点にmpmathのζ′を用いた診断。一般の零点展開の定理は位数任意であり、診断から零点単純性を推定しない。
5. rational Gaussian inverseのjumpとreflectionを6点で計算。恒等式の証明はconvolution/contourにある。
6. jet次数0,1,2,5,8のQ_NをFractionで構成。target z*=1/5+2iでの根はexact rational arithmeticで確認。jet一致はfactorの次数で証明。
7. Gamma slope7例、S_zのexact coefficient polynomial3例を確認。large-X growth fitは実施しない。
8. 非実軸外quartet ±0.2±i の有理模型を4点で検算。部分分数とGaussian畳込みを用い、right inverse−central inverseが右半平面留数和に一致する。common cosh amplitudeや点ごとの指数下界は仮定しない。

非区間の浮動小数検算、exact rational checks、解析的証明を混同しない。既知実零点だけをnumerical inputにした結果を、新しい零点位置定理として使用しない。

## 4. 保持・終了・再開条件

開始時に既存302ファイルのSHA-256をbaselineへ保存。終了時に同じ302ファイルの欠損・hash差分を検査する。既存state・proof graph・Phase III/IVのactive trackは変更しない。成果は本トラックのみのファイルに隔離する。

三候補とも同じ未取得算術的成長評価へ戻ったため終了。再開には、RH同値なsubexponentialityを仮定せずactual coefficientsから得た具体的な新しい評価入力が必要。temperedness、positivity、unitaryという新しい名前だけでは再開条件を満たさない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/global_remainder/experiments/check_global_remainder.py`](../../../../artifacts/research/global_remainder/experiments/check_global_remainder.py)
