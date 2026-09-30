**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/failed/COUNTEREXAMPLE_LOG.md` · Original SHA-256: `99b7869a848351288caa76f4168bc5bba84e98f9bf1ba6eb2f24211254e7fd27`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 反例・棄却ログ

2026-09-29、初回cycle。

|ID|棄却した推論|厳密な根拠|範囲|
|---|---|---|---|
|F001|稠密な有限圧縮が全てPSDなら連続性なしで全域PSD|c00⊕Cuの不連続形式、q(u)=−1|一般論。Weil形式の反例ではない|
|F002|正の制限から次元拡大もPSD|[[1,2],[2,1]] と (1,−1)、q=−2|一般論。文献の特定作用素を反証していない|
|F003|虚部の自己共役スペクトル化だけで臨界線性|軸外の対称四重点にも同じ虚部スペクトル|完全な零点同定条件の必要性|
|F004|軸外ペアでもWeil型和は絶対値二乗|compact smooth witnessで −15A²/8<0|合成四重点。ζの零点についての反例ではない|
|F005|有限個のexact Gram PSDで全次元を保証|最終確認次元の次の座標に負の対角成分|任意に多い有限検証も不足|
|F006|同じsupport・二次モーメント式で核だけ改良して下界100%|既知最適定数 C_MT>1、独立再導出|得られる割合下界の上限。実際の零点割合上限ではない|

詳細は `finite_positivity_shortcuts.md` と `../lemmas/kernel_optimization_barrier.md`。
数値計算ログは `experiments/results/`。非認証近似を厳密証明の代替にしない。
Arbによる誤差包含を使う計算機援用証明は、解析的保証と信頼基盤を別に記載する。

## 2026-09-29: Zhu v2の一般entry boundを修復

対象: §4のC_nmに対する一般上界で、積分長T/πが欠けた表示。
L=.001,T=100,n=m=0の実際のarchimedean symbolで、
|C_00|>0.06350に対して掲示上界は0.01626未満となり、Arbで不等式の破綻を認証。
解析的反例族も `proofs/audits/zhu-reduction-audit.md` に記録した。
正しい積分長またはより精密なn依存積分を戻せば還元は修復できる。
原著L=.8のtail/couplingは別評価で修復したが、原著headは未取得なので成功とは記録しない。
独立a=.5実装はこの偽の上界を使わず、全modeの局所正値性をT090に保存した。
これはRH、Weil形式の正値性、または修復済み有限還元の反証ではない。

## 2026-09-29 checkpoint04: joint symbol と固定積imbalance

- `Psi_a(t)>=0 for all t>=2πexp(2a)` は a=.8,1,1.19,1.2,1.4 のすべてで厳密負点・負区間がある。
  `audits/joint-symbol-adversarial.md` を参照。補助symbolの反例で、Weil形式の負方向ではない。
- 正の非退化な加重和 `E(σ)=Σw_n(n^-σ−n^(-(1−σ)))²` の零点はσ=1/2のみ。
  したがって全ξ零点でE=0という候補はRH同値、独立補題として棄却。
- 正の対称測度のLaplace変換 `cosh(1/4)+cosh(z)` は `z=1/4+iπ` で0だが、
  `E_2(3/4)=3√2/4−1>0`。固定積・対称性・正kernelのみからの強制は偽。
- `F=-ζ'/ζ` の二階差分を収束域外へ有理型接続すると、u=1/10,δ=1/5で値は−21.3487…。
  元の正級数は発散しており、接続した関数の値と同じ非負和とは扱えない。

詳細: `audits/imbalance-reduction.md`、`audits/imbalance-adversarial.md`。
固定積候補はここで終了。これらはRH反例ではなく、他の未検討の算術構造の不可能性証明でもない。

## 2026-09-29: 内部構築した核候補の反証

- 正・強対数凹・増加scoreだけでは積分核のPSDは出ない。
  四次Gaussian模型の5点Gram値は厳密に `-109/160000`。
  超指数減衰を加え、Fourier変換を位数1にしても負方向が残る。
- 実Riemann核は `A exp(-c t²) prod(1+lambda_j t²)`, `lambda_j>=0` の
  点wise閉包から外れる。実核の `log Phi(sqrt(u))` の三次差分が負だからである。
  `c` の発散を許しても成立。任意の正係数多項式の閉包への主張ではない。
- thetaから導いた正・増加・凹な `P` をBernstein型へ強める案は
  `P'''(0)<-1/6` で反証。正の整数移動係数だけによる核PSDの移植も単一shiftで偽。

詳細・範囲・独立検算: `research/internal_first_principles.md`。
これらは内部候補の終了理由であり、RHやactual Weil正値性の反例ではない。

## 2026-09-29: 素数追加・finite Euler completion

- 一素数 `p=2` の全幾何級数をGaussianに適用しても核のPSDは保存しない。
  二点の厳密な負方向を、無限尾の解析評価で証明した。単一shiftへの置換ではない。
- actual thetaの有限素数和はcompactでは全核へ収束するが、全実線の積分は負に発散。
  反射欠損とその正エネルギーも大域的に制御されない。
- 正半直線を原点で偶延長するとweighted L1・Fourier局所一様収束は回復する。
  しかし全ての有限素数集合で原点の右微分が正となり、Fourier変換には非実零点が無限個ある。

詳細: `research/prime_insertion_closure.md`。有限近似族の棄却で、RHや全ξの反例ではない。

## 2026-09-29: exact selfdual theta と所定のMellin因子の区別

- 正の自己Fourier seed、正のcompleted kernel、滑らかなmodular反射、位数1、
  零点の臨界帯内限定、端点規格化を保っても、Mellin因子を変更すれば
  `s=1/4±32i,3/4±32i` に非臨界線零点を追加できる。全域正値性は有理下界で証明。
  標準Gamma因子を維持した反例ではなく、標準ξはこの四点で非零と区間認証した。
- Gaussian畳み込みには正rank-one増分があるが、全有限時間で既存の非実零点が残る。
  正のGaussian極限から逆向きに正値性を移す候補は棄却。
- 各整数channelのGaussian ground stateは正エネルギーを持つが、等係数の無限ベクトルは
  直和Hilbert空間外。点ごとの完成theta和はL²でも、自然な部分和はL²収束しない。

詳細: `research/selfdual_theta_boundary.md`。いずれもRHの反例ではない。

## 2026-09-29: canonical continuum subtraction

- 正・単調増加するprimitive U_Nに対して、自然なresolvent energyは
  E_2−E_1=11/(4√2)−112/(25√5)<0。最初の段階だけで正増分案を反証。
- 全H^kでactual Φに収束する補正R_Nでも、偶対称化のGram形式は
  D_N(i/2,i/2)≤−(γ+log(4π))/64<0、全Nで負方向を持つ。
- 当該変換はF_N(i/2)=1/4だが、actual F_Φ(i/2)=1/2。
  全Sobolev収束から指数重み付き評価を連続に移す推論を棄却。
- 正測度ρ(r)={√(r/π)}のLaplace Gram核には正増分がある。
  その核とWeil／K_Φとの未証明の同一視によって、上の負方向は消えない。

詳細: `research/continuum_subtraction.md`。自然な補正近似自体は収束する。
その族による正値性伝播を棄却したもので、RHや他の補正全般の反例ではない。

## 2026-09-29: 全整数のGramとMangoldt共役

- G_α(m,n)=(gcd(m,n)²/(mn))^α は全有限Gramが正定値。
  しかし標準係数ℓ²では0<α≤1/2でnonclosable。全divisor feature方向が
  入力norm0の列の像として現れ、D(A*)={0}。正Gram完備化そのものは存在する。
- α=1/2で B=A(log n)A^(-1) の自然なHermitian formは
  h(e_1−e_2/2)=−log2/4。有限prime-star圧縮のSchur式により下半有界性も否定。
  B*のdomainにe_1が入らないため、formと通常の対称作用素を同一視しない。
- 正Poisson密度の対数微分は単一素数でも符号不定。素数冪の係数が一致するだけでは
  archimedean・pole項を含むWeil全形式との同定にならない。

記録: `research/arithmetic_gram_generator.md`。標準ξ・Weil形式の反例ではなく、
指定したGram模型からの正値性移植候補を棄却した結果。別の完備化全般を否定しない。

## 2026-09-29: Phase II Generator / Boundary

- actual modular scatteringの全ζ零点ρ=β+iγはpole ρ/2に対応するが、Laplace parameterの
  虚部はγ(1−β)/2≠0。自己共役固有値との同一視はRH下でも失敗する。
- completed cut-off境界関数D_aについて全a>0でD_a(ρ/2)=a^(1−ρ/2)Z(2−ρ)≠0。
  自然な自己共役boundary restrictionへ移す修復は全零点の回収を失う。
- actual prime germからのm=−Ξ′/ΞはHerglotz iff RH。逆定理を適用する入口を未証明のままにしない。
  一般quartet模型はIm m(1+i/5)=−428313920/24221529というexactな負値を持つ。
- actual Newman familyは全負時間で非実零点を持つ（既知入力）が、負時間無限遠の
  rescaled境界は零点のないGaussianとなる（Taylor剰余による証明）。境界からの逆伝播を棄却。
  算術tailが時間原点0を固定することと、実零点閾値が0であることを区別する。
- actual Gaussian oscillatorのGと整数lattice lift TはGT≠TG。x≥1でGT_Ng<0=T_NGg。
  Gamma変更模型を使わず、当該intertwining候補を初期screenで棄却した。

詳細: research/generator_boundary_hypothesis.md と research/notes/phase2_*_generator.md。
C/B/Aの3 major attempts後にstrategy review完了。Dは初期screenで別majorに数えない。
これらはRHの反例でも、全generator構成の不可能性定理でもない。主graph合流0。


## Phase III — finite-field形式公理・商norm・局所接着（2026-09-29）

第25サイクル、主graphへの追加なし。
- q=9、F=[[0,-9],[1,7]]、Z=(1-7T+9T²)/((1-T)(1-9T))。
  全closed-point countsは正整数、trace/duality/FE成立、しかし固有値の絶対値は3でない。
  actual curveではない。positive polarizationを除いた公理の十分性を反証。
- LF test-space quotientはambient unitary L2 completionでmodeを失う。
  CCM Prop6.4の指定weighted L2商でも0となる（原定理を引用採用、sector帰結を独立検算）。
  他の偏極や算術商自体の無効性を意味しない。
- prime orbit circlesの直和は無限zero-mode multiplicity、除去後も低周波accumulation。
  元の正時間distribution traceは存在するがordinary Hilbert traceではない。
  local Gamma determinantは成立。global H1接着の成功とはしない。

全式・解析証明: research/notes/phase3_structural_tests.md。
独立監査: proofs/audits/phase3-independent-audit.md。
数値: experiments/results/phase3-structural-checks.json（有限整数部分のみexact、Gamma値非認証）。
RHそのものの反例ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/phase3-structural-checks.json`](../../../../artifacts/experiments/results/phase3-structural-checks.json)
- [`proofs/audits/phase3-independent-audit.md`](../../../audits/proofs/audits/phase3-independent-audit.md)
- [`proofs/audits/zhu-reduction-audit.md`](../../../audits/proofs/audits/zhu-reduction-audit.md)
- [`research/arithmetic_gram_generator.md`](../../research/arithmetic_gram_generator.md)
- [`research/continuum_subtraction.md`](../../research/continuum_subtraction.md)
- [`research/generator_boundary_hypothesis.md`](../../research/generator_boundary_hypothesis.md)
- [`research/internal_first_principles.md`](../../research/internal_first_principles.md)
- [`research/notes/phase3_structural_tests.md`](../../research/notes/phase3_structural_tests.md)
- [`research/prime_insertion_closure.md`](../../research/prime_insertion_closure.md)
- [`research/selfdual_theta_boundary.md`](../../research/selfdual_theta_boundary.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/results` — SOURCE REFERENCE NOT INCLUDED
