**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase4_pairing_matrix.md` · Original SHA-256: `2b35f0fc623195a34f021aae2c8218888a80140860baf3290fe0e6a850501986`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase IV — pairingの機能比較

2026-09-29。Phase IIIのstate/active track/graphは変更しない。
以下のLevelは、別対象上の既知positive metricを数えるのでなく、要求されたactual zero-bearing spaceへのbridgeについて判定する。

|ID / 候補|算術から構成できるもの|正性の出所|actual ζへの接続|判定|
|---|---|---|---|---|
|PV-A Arakelov / height（A,E）|全placeの交点、高さ、polarized endomorphismのadjoint|GEOMETRIC / ARITHMETIC、既知Hodge index / canonical height|Spec Zのdegree0 quotientは0。別Jacobianの正性とζ spectrumの比較なし|major1終了|
|PV-B explicit-formula intersection（B）|Euler・Γ・極で定義する形式、canonical sharp、既知全零点trace|正性はRH-EQUIVALENT|actual fidelityはあるが独立なHodge comparisonなし|初期screenで終了|
|PV-C adelic quotient / Hodge / module（C,D,F）|全零点の算術商、formal star、別の葉層幾何では正star|算術商の正性はRH-EQUIVALENT。葉層の正性はGEOMETRICだが別対象|指定L²で商消失。非有界な可閉positive formでも修復できない|最も接続が強い候補として集中、major3終了|
|PV-D product formula / star（積公式独立候補）|S(A)の正内積、全placeのHaar、closed Θ*=1−Θ|ANALYTIC / REPRESENTATION-THEORETIC、算術測度|ambient spectrumは連続。Fourier twistはactual pole-free testで負|major2終了|

初期四候補を並列比較した後、PV-Cの「非有界な形式にすればdescentできるか」へ集中した。
別トラックで進行するPhase IIIへ候補や判定をmergeしていない。

## finite-fieldの最小機能を何で置き換えたか

|機能|A|B|C|D|
|---|---|---|---|---|
|正norm|固定Jacobianのheightで存在|未証明|別Hodge空間では存在、actual商では未証明|ambient Haar normで存在|
|算術adjoint|projection formula / polarized endomorphism|sharpによるformal pairing|formal scaling identity、Hilbert adjointは未供給|Θ*=1−Θを閉作用素として構成|
|全局所情報|交点multiplicityとGreen関数|prime powers、Γ、極を全て保持|既知nuclear traceで保持|Tate積分でEuler/Γ/極を保持|
|同じ対象の全zero spectrum|未同定|traceで同定済み|旧test topologyで同定済み|未同定|
|非退化quotient|degree0 Spec Zは0、heightはtorsion/base radicalを分離|全jet保持は未証明|自然L²では0、stronger normはunitaryでない|原L²は非退化だがζ商へのdescent未証明|
|最小missing property|cycle/Greenとactual formの比較|幾何的Hodge indexの適用対象|非可閉障害を避ける独立な算術metricと忠実な作用比較|zero-bearing spaceへの同定と正性の保持|

## 各candidateの固定条件

### PV-A

Finite-field object: polarized Jacobianの正trace form。
Number-field candidate: arithmetic divisors / fixed JacobianのNéron–Tate pairing。
Exact matching property: finite/infinite局所和、積公式によるprincipal classes消去、f* f=dI。
Missing property: 同じ空間でのactual ζ traceと全零点。
Proof: Spec Zのdegree同型は直接計算、height/intersectionは既知原典を引用採用。
Counterexample attempts: degree-zero quotient=0、divisor平方の次数不適合。
RH-equivalent assumption used?: 既知heightにはNO。ζのWeil形式との比較を仮定すれば未証明bridge。

Space/topology/completion: arithmetic divisor群→主因子商R、degree0は0。fixed MW real spaceは有限次元。
Kernel: Spec Zではprincipal divisors、heightはtorsion、full arithmetic liftにはbase pullbackも残る。
Finite/infinity/poles/normalization: finite length×log p、Green gまたはg/2の規約、ζのpolesとの同定なし。
詳細：`phase4/notes/arakelov_height.md`。

### PV-B

Finite-field object: correspondence intersectionとRiemann–Rochによる符号。
Number-field candidate: B(f,g)=pole−finite−archimedean のactual explicit form。
Exact matching property: primitive degree/co-degree、sharp、全零点trace。
Missing property: 対応する真正のcycles/Green currentsとeffectivity / Hodge indexの比較。
Proof: 正規化付き明示公式、CCM §7。
Counterexample attempts: q=9 syntheticでdegree/co-degree除去後もstar trace=−486。
RH-equivalent assumption used?: 全testの正性はYES。独立入力として棄却。

Space/topology/completion: C_c∞のLF coreとCCMの全指数Schwartz商は区別。
Kernel: arithmetic imageはradicalに含まれるが、compact coreの部分空間とは限らない。
Finite/infinity/poles/normalization: log p·p^(−k/2)、Γ_Rの固定principal-value項、0,1の両極。
詳細：`phase4/notes/explicit_intersection.md`。

### PV-C

Finite-field object: 正偏極上の忠実な算術作用。
Number-field candidate: 既知算術商をclosable positive formまたはHodge代表で完成。
Exact matching property: もとのnuclear test-space traceは全零点・位数を保持。
Missing property: その商を失わず正metric・star・generatorを同じspace上に置くこと。
Proof: dense-null-subspace lemmaにより、指定ambient L²に可閉な非零positive formは不可能。
Counterexample attempts: stronger weightではMellin modesを保てるがnormalized scalingはunitaryでない。
RH-equivalent assumption used?: 既存Weil形式の正性を供給するにはYES。lemma自体はRH不要。

Space/topology/completion: Eのstrong Fréchet quotientとH₀=L²(u d×u)を区別。
Kernel: restriction V₀はH₀に稠密。同じrelationsを保つclosable Gram liftは零。
Finite/infinity/poles/normalization: actual traceの全成分を保持することが条件。新regularizationは導入しない。
詳細：`phase4/notes/adelic_descent.md`。

### PV-D

Finite-field object: 正normとscaled isometry。
Number-field candidate: 全adèleのHaar内積とproduct formula、Fourier/star。
Exact matching property: R_a*=|a|R_(a⁻¹)、Θ*=1−Θ、Tate Euler/Γ integral。
Missing property: 同じpositive spaceへのzero-bearing quotientの忠実な比較。
Proof: measure change、log-coordinate、Gaussianの直接計算。
Counterexample attempts: Fourier-twistはpole-free hで−585/(32√2)。Jを含む弱いadjoint式にも線外2×2反例。
RH-equivalent assumption used?: ambient計算はNO。全ζ零点とのunitary同定は未証明。

Space/topology/completion: S(A)→L²(A)、domainはlog座標でvector-valued H¹。
Kernel: ambient Pは0、Fourierの正部分への射影は新しいkernelを作るので完全性なしに採用しない。
Finite/infinity/poles/normalization: vol(Z_p)=1、Gaussian、自己双対加法測度、vol×(Z_p×)=1、原点/積分条件。
詳細：`phase4/notes/product_formula_star.md`。

## 最終判定

各候補の未証明部分を合成して一つの完成metricとすることは禁止。
正性が既知なのは全零点同定のない側、全零点を保つ側では独立positive comparisonが欠ける。
「正性はある」「作用もある」「零点もある」を別々のspaceから集めてもbridgeにはならない。
Phase IVの到達レベルは0。限定no-goは保存するが、Level1以上のpositive bridgeとして数えない。
