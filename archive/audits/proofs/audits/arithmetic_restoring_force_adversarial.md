**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/arithmetic_restoring_force_adversarial.md` · Original SHA-256: `13e371f24883ad52a036e8157b4a888ab9d26285e91c681ef750fcef6958f0e0`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Restoring Force — adversarial audit

2026-09-30。RH OPEN。既存ファイルを保持した独立監査。三候補を超えて研究を継続しない。

## 1. 採用基準

必要なのは、actual primes / standard Gamma / actual thetaから、全零点のcritical-line confinementを独立に導く算術的入力である。既知の局所符号、他の関数のreal zeros、RH同値条件の新名称は成功と数えない。

## 2. 符号・potentialへの破壊検査

| ID | 主張候補 | 反証・検算 | 判定 |
|---|---|---|---|
| A01 | even symmetryが復元方向を与える | evennessは中心一階微分0のみ | 不足 |
| A02 | \(a\Re(\xi'/\xi)>0\) は弱い独立仮説 | 全 \(a\ne0,t\)、ξ非零点での命題はRH同値。off-line zeroの中心側で \(m/(s-\rho)\) が逆符号 | 既知同値条件として停止 |
| A03 | scalar signは数値で反証された | 128点gridで反例なし。一方これは証明でもない | どちらの過大主張もしない |
| A04 | \(V=-\log|\xi|\) は復元potential | t=0ではactual正thetaのlog-mgfがstrict convexで、反転potentialは中心最大 | actual反例 |
| A05 | 正のΛ係数ならprime force一定符号 | σ=4および8でt=0とπ/log2が反対符号。主項・尾の解析的比較 | actual反例、完成ξへ転用不可 |
| A06 | Gamma・pole-removal部分を単独の中心力と呼べる | 項の符号はσ,tに依存し、0,1等で相殺が必要 | 不採用 |
| A07 | ξ零点はξ'/ξ=0の平衡 | ξ'/ξは零点で正整数residueのpole | 誤り |
| A08 | log|ξ|は全水平線で凸 | actual on-line zero近傍で曲率 \(-m/a^2+O(1)<0\) | 無条件に偽、単純性不使用 |
| A09 | 中心の全regular点の正曲率は全零点を拘束 | \(\cos(10w)((w-1)^2+1/16)((w+1)^2+1/16)\) はκ≥36だがoff-real quartetあり | 一般条件への厳密反例 |
| A10 | 水平minimumは二次元の束縛minimum | zero-free logmodulusはharmonic。Hessian trace0、中心実点はsaddle | 別の概念 |
| A11 | A08は|ξ|²全凸性も反証 | modulus squaredは別物。全水平凸性はRH同値 | 誤転用を禁止 |

Sondow–Dumitrescuの定理はhalf-plane内のzero-free仮定を使う。ある一点の近くに零点が見当たらないことを、この仮定に代用しない。Hadamard productによる符号説明は零点を入力しており、新しいprime-side force lawではない。

## 3. theta二条件への破壊検査

| ID | 主張候補 | 反証・検算 | 判定 |
|---|---|---|---|
| B01 | 新しいoff-axis integral identityが得られた | 規約 \(F(t-ia)=\xi(1/2+a+it)\) と旧D4を照合、完全一致 | 新規identityではない |
| B02 | Φ>0、cosh>0、sinh/a>0なので両条件は両立しない | cos(tx),sin(tx)の符号は振動 | 不足 |
| B03 | actual核のshapeをgeneric positivityと同じく捨てる | strict concavity of logΦ(√u)は無条件の既知定理 | 真の情報として保持 |
| B04 | その凹性ならFourier zerosは実 | 既存quartic-Gaussian核は同じ凹性を持ち非実零点あり | 一般shapeからの含意は偽 |
| B05 | Poisson対称性も足せば十分 | 旧正seed/正completed核例はoff-axis zerosを追加 | 標準Gammaを変えた限定反例、actualζ反例ではない |
| B06 | actual Φは標準Toeplitz PF∞ | Schoenberg reciprocal-Laplace必要条件とentire transformからGaussianに限られる。actual tailと矛盾 | このPF∞候補は偽 |
| B07 | B06からactualFはLPでない | PF∞の逆Laplace条件とFourier-LPは別 | 誤り。actualFのLPはRH同値で未証明 |
| B08 | universal factorは前件なしにreal zerosを作る | 原定理は元のtransformのreal-zero性を前提に保存する | 保存と生成を区別 |
| B09 | 正測度のcharacteristic-function boundで零点を排除 | \(|\xi(1/2+a+it)|\le\xi(1/2+a)\) は上界 | 必要な非消滅下界ではない |
| B10 | 数値求積で全a≠0の同時消滅禁止を検証 | 5点で恒等式を照合しただけ | 数値からの全域結論なし |

PF∞の限定no-goはactual核の減衰まで使うが、RHを狭める新しい零点不等式ではない。特定の十分条件候補を排除した監査結果としてだけ保存する。

## 4. deformation・electrostaticsへの破壊検査

| ID | 主張候補 | 反証・検算 | 判定 |
|---|---|---|---|
| C01 | \(e^{\tau x^2}\) はunitary evolution | actual変形は \(\partial_\tau H=-H_{ww}\)、正時間で全L²上のbounded multiplicationでもない | 不採用 |
| C02 | zero velocityは全ての零点でH''/H' | simple branchのみ。multiple collisionで分母0 | domainを限定 |
| C03 | forward帯収縮が時刻0を解く | 幅Δは \(\sqrt{\max(\Delta^2-2h,0)}\)。Δ=1/2から安全時間1/8 | 逆伝播は出ない |
| C04 | RT非負性Λ≥0は必要な上界 | 欲しいのはΛ≤0 | 逆の方向、閾値0はRH同値 |
| C05 | 全ての内側zeroが軸へ動く | even real heat polynomialの枝2+iで \(\Im w'(0)=14/1275>0\) | 一般法則への厳密反例 |
| C06 | 実零点の反発はoff-axis confinement | 実軸のordinals方向と虚方向の変位を区別 | 含意なし |
| C07 | Stieltjesの平衡をactualξへ使える | 正の直交測度、ODE、外場の条件が別途必要 | actual bridgeなし |
| C08 | random matrix Coulomb gasはRHの証拠 | Hermitian/実配置が前提。ensembleと指定ζは別 | heuristicのみ |
| C09 | τ≠0でもactual Euler/Gammaを保持 | heat-deformed Fourier objectであって同じζとは限らない | fidelityを明記 |

有限多項式とmodified核は、actual Riemann zerosを変更した事実として扱わない。反証するのは指定した一般推論だけである。

## 5. Gaussian・energy gate

既存 \(A(u)\) とそのnonvanishing Gaussian transformを保持した。(6)の全域符号やtheta二条件の排除からRH、そこからAのsubexponentialityという後半の含意は正しい。しかし最初の独立算術評価は未取得。

actual \(A\notin L^2\) という以前の結果を尊重し、unweighted有限energyは再仮定しない。arbitrary weight、零点に合わせたkernel、zero-bearing情報を失うcompletionは導入していない。scalarの静的な符号から人工的な零点運動を定義し、その安定性をRHの証拠にすることもしていない。

## 6. 独立点検・資料の取得範囲

- ROOTはactual completed derivative、center/非center curvature、prime符号、theta二積分を数値診断し、prime尾のrational marginを解析的に確認。
- scalar担当は別にσ=4のprime反例、RH同値性の両方向、中心曲率countermodelを検算。
- theta担当は標準核、旧D4との一致、Csordas–Varga原定理の規約、Schoenberg原版のreciprocal-Laplace必要条件を確認。
- deformation担当はde Bruijn原著、Newman原著、Rodgers–Taoの規約・Theorem 4.1の適用域を確認し、outward polynomial枝をexact rational arithmeticで確認。
- 別担当がSchoenbergの引用定理を前提にPF∞ no-goの導出を独立点検し、theta担当が主文の積分係数・虚部符号、熱変形の係数2・安全時刻1/8・outward速度を再計算した。主文のsinhの正性をa>0に限定し、LPの肯定命題と否定命題の指示語を明確化した。
- primary全文取得の限界：Pólya1926は原論文英訳で確認。Pólya1927とStieltjes1885の原著全文は取得できず、使用した特殊例・一般化はde Bruijn/Ismailの著者一次論文で確認。Dyson1962は出版社abstractのみ。未読の定理をRH用入力に採用していない。

全参照論文の全証明の独立再形式化を行ったという記録ではない。数値は50/80桁の診断でinterval proofではない。厳密な反証は本文の解析計算による。

## 7. 終了と保存

**NO ARITHMETIC RESTORING FORCE IDENTIFIED。**

RH OPEN。三候補のいずれにも新しい独立な全零点拘束はない。第4候補、Hilbert–Pólya再開、positive metric新設、proof graphへのmergeは行わない。

旧329ファイルの保存は [preservation_check.json](../../../../data/source-records/research/arithmetic_restoring_force/preservation_check.json)、新規成果の機械的整合確認は [validation.json](../../../../data/source-records/research/arithmetic_restoring_force/validation.json) に記録する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/arithmetic_restoring_force/preservation_check.json`](../../../../data/source-records/research/arithmetic_restoring_force/preservation_check.json)
- [`research/arithmetic_restoring_force/validation.json`](../../../../data/source-records/research/arithmetic_restoring_force/validation.json)
