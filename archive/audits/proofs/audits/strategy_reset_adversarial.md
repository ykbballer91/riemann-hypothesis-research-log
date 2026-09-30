**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/strategy_reset_adversarial.md` · Original SHA-256: `02e3a54c922e2be74baa7b1966f34706bb8526b0e0f28c68cdd77344d8992b4c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Strategy Reset：独立算術入力とclosure解釈の反証監査

2026-09-30。RH OPEN。新しいproof trackを作らない。過去ファイルは変更しない。

## 1. 判定

**監査対象から正当化された次トラックは0件。NO JUSTIFIED NEXT TRACK。**

これは候補A/B/Cの確認した定理・適用に対する停止判断。bilinear・相関・算術的因果性に将来の成果が存在し得ないという不可能性定理ではない。

## 2. Proof-critical checks

| ID | 攻撃する推論 | 検査・証拠 | 判定 |
|---|---|---|---|
| AD01 | C1/C2で和を交換できる | \(\sum_{m,n}|\mu(n)|\phi(u-\log mn)\le e^{cu+c^2/4}\zeta(c)^2\), c>1 | PASS、compact uでも一様 |
| AD02 | \(\zeta(\rho)=0\) だから指数関数は通常のhomogeneous solution | \(\sum_{m\le N}m^{-\rho}=N^{1-\rho}/(1-\rho)+O_\rho(N^{-\Re\rho})\) | REJECT、その和は発散。継続symbolのformal modeと区別 |
| AD03 | 左で0へ行くというだけで一意 | 左Gaussian boundは単なる \(o(1)\) より強い | REJECT、境界条件を弱く読み替えない |
| AD04 | 左Gaussian classでMöbius inverseは一意か | polynomial-growth coefficientsのdelay convolutionが絶対交換、\(D_\mu D_1=I\) | PASS、右growth条件なし |
| AD05 | causal＋一意＋左Gaussianならstable | \(f+af(\cdot-L)=\phi\), a>1。唯一の左Gaussian解に右半平面poles | REJECT。toyはactualζ反例ではない |
| AD06 | real-frequency boundary symbol非零なら指定inverseはstable | 同toyにboundedな未来inverseと不安定な過去inverseが別に存在 | REJECT、inverseの向き・domainを保持 |
| AD07 | forcingがactual off-line zero residueを消せる | Gaussian multiplier \(\sqrt\pi e^{s^2/4}\ne0\)、multiple zeroでも最高pole係数は非零 | REJECT、仮にoff-line zeroがあればcanonical solutionのtransformに残る |
| AD08 | \(\mu*\log=-\Lambda\) | prime pで直接検算、Leibniz則 | CORRECTED：\(\mu*\log=+\Lambda\)、\((\mu\log)*1=-\Lambda\) |
| AD09 | higher closureが \(\zeta^{(k)}(\rho)=0\) を強制 | 正しいRHSは \(S_{\Lambda_k}g\)、symbolは \((-1)^k\zeta^{(k)}/\zeta\) | REJECT、非零forcingを落とさない |
| AD10 | log-momentの係数正値性は存在しない | finite-difference integralで \(\Lambda_k\ge0\) を直接証明 | REJECT、この既知算術情報は本当にある |
| AD11 | 全positive momentsならsigned objectがpositive | \(\delta_0-\delta_1+\delta_2\) は全非負整数momentsが正 | REJECT。actualμについての反例とはしない |
| AD12 | 無限massのC2をprobability renewal theoremへ代入 | \(\sum m^{-1/2}=\infty\)、rearrange後feedbackは負 | REJECT。tilt後有限mass域の指数損失を保持 |
| AD13 | Type I/II分解そのものがGaussian和を小さくする | 中央blockの裸内和は正で長さ規模、Mellin長方形位相は1 | REJECT、別の算術的相殺推定が必要 |
| AD14 | Davenport uniformityならsqrt bound | α=0を含み、実際の移行は \(A(u)\ll_B e^{u/2}u^{-B}\) | REJECT、対数節約と指数率0は異なる |
| AD15 | large sieveのRMSは指定readoutのsqrt bound | 全＋係数でも平均不等式は成立し、指定点の和はN | REJECT、actualμの反例ではなく平均推論の反例 |
| AD16 | AP平均でglobal componentも改善 | principal-average差で定義するΔはq=1で恒等的0 | REJECT、消した成分を復元する評価が必要 |
| AD17 | fixed log Gaussianはadditive short interval | \([xe^{-B},xe^B]\) の長さ \(2x\sinh B\) | REJECT、固定Bでは線形幅 |
| AD18 | Gaussian尾は固定Bでsqrt精度に無視可能 | normalized absolute tailは \(\sqrt x e^{-(B-1/2)^2}/B\) 程度 | REJECT、目的に応じてBと一様性を追跡 |
| AD19 | 可変幅でboundedなら元のcriterionも成立 | \(\sigma=x^{-1/2}\) では全＋係数でもnormalized sum bounded | REJECT、fixed-kernel witnessを変更している |
| AD20 | 既知MRの例外評価は対数節約だけ | MR IIに例外数のpower savingが存在 | CORRECTED、ただし誤差閾値を小さくするとsavingが崩れる |
| AD21 | log Chowla・almost all scalesは全xのweighted correlation | 固定shift・log weight・例外scaleとGaussian二変量kernelの差 | REJECT、量化とweightを維持 |
| AD22 | weighted offdiagonal o(X²)でsqrt cancellation | squared targetは \(O_\varepsilon(X^{1+2\varepsilon})\) | REJECT、rate不足 |
| AD23 | 平均からpointwiseへは原理的に不可能 | local H¹ Sobolev boundは有効 | REJECT、その一般的no-goは主張しない |
| AD24 | 既知平均定理が必要なSobolev RHSを既に供給 | 全sliding windows、derivative energy、全εのboundは未証明 | NO BRIDGE、欠ける評価を新仮定にしない |
| AD25 | compact-W相関式でW→1を無条件交換 | compact-W Fubiniのみ。過去解析はactual A非L²を確認 | REJECT、無限energyを定義で有限化しない |
| AD26 | BSZ/Kátaiの条件はraw Gaussianに成立 | \(X^{-1}\sum_{m\le X}F_X(2m)F_X(3m)\to c_{2,3}>0\) | REJECT、尺度に一様な小相関がない |
| AD27 | incidence invertibilityならinverseは小さい | bottom/topとr incomparable中間点でMöbius値r−1 | REJECT、generic inverseの大きさは制御されない |
| AD28 | 有限GCD inequalityで旧domain問題は解消 | サイズ因子とnonclosabilityが残りsigned比較も未取得 | NO REOPENING REASON |
| AD29 | random multiplicative平均をactualμへ移せる | 全素数−1 assignmentは確率0、有限版も指定rare assignment | REJECT、transfer theoremなし |
| AD30 | 全旧programがRHと同値と証明済み | scalar/指定Weil版と、より強い未知geometric/operator packageを区別 | CORRECTED、逆含意未証明は維持 |
| AD31 | 未適用算術があるから次routeを推奨 | 成功条件を満たす具体的bridgeが各候補に必要 | REJECT、候補数0を許す |

## 3. 相互監査の記録

closure担当と別担当が以下をread-onlyで照合した。

- 左Gaussian classでの絶対convolution・Möbius inverse・一意性。
- classical homogeneous指数関数のdomain外判定。
- 有限遅延反例のpole位置、residue、antiperiodic Fourier coefficients、未来inverseとの区別。
- 相関担当とは別担当がGaussian tail、可変幅反証、compact-window相関の \(e^{1/8}/\sqrt{mn}\)、導関数factor \(4t^2-d^2\)、Sobolevの全移動窓条件を点検。
- prior matrix担当とは別担当が、Mertens endpointの全ε量化、GCD定数とN依存因子、PNTの証明依存分類、p-adic normal modelの適用域を点検。4点の表現を修正した。

有限exact検算は [check_finite_identities.py](../../../../artifacts/research/strategy_reset/notes/check_finite_identities.py) に保存。1000個のμ反転、1000個のlog符号、4000個のgeneralized Mangoldt多項式を整数係数で確認。これらは一般証明の代替でもRHの数値的根拠でもない。

監査は定理文の一次資料照合とここに記した計算の独立点検。全参照論文の全証明の再形式化は行っていない。

## 4. 保存条件

旧315ファイルをSHA-256 baselineで固定した。今回新規のstrategy-resetファイル群だけを作成・修正し、既存stateとproof graphへmergeしない。Git commitを作らず、過去の未追跡研究ファイルも旧資料として保存する。

実測結果は [preservation_check.json](../../../../data/source-records/research/strategy_reset/preservation_check.json)、機械的整合確認は [validation.json](../../../../data/source-records/research/strategy_reset/validation.json)。

## 5. 終了判定

Candidate A、B、Cはいずれも今回指定された成功条件を満たさない。新しいproof-critical bridgeも、既知結果を越えるMertens/零点boundも得ていない。

**NO JUSTIFIED NEXT TRACK。RH OPEN。**

より弱い既知定理を無価値とは呼ばない。未確認の全数学を否定もしない。しかしこの監査終了時点で、別名の第4候補や安定性の新仮定を置いて研究を続けることは正当化しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/strategy_reset/notes/check_finite_identities.py`](../../../../artifacts/research/strategy_reset/notes/check_finite_identities.py)
- [`research/strategy_reset/preservation_check.json`](../../../../data/source-records/research/strategy_reset/preservation_check.json)
- [`research/strategy_reset/validation.json`](../../../../data/source-records/research/strategy_reset/validation.json)
