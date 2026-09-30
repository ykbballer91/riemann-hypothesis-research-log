**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/finite_field_dependency_spine.md` · Original SHA-256: `8c1e04bf24bc6b8f4a43c30dca65e8d867f0e6aee60027e3a7f945558335859b`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 有限体RH — 最小に近い証明依存骨格

2026-09-29 / Phase III。既知証明の依存比較であり、唯一の最小公理系や論理的独立性の証明ではない。
以下の「独立」はRHを結論として前借りしない証明入力という意味。
詳しい導出・版・ページ・確認範囲は `notes/phase3_finite_field_audit.md`。
曲線を基準とし、一般次元の追加装置を曲線へ遡及して要求しない。

## 十二の役割を分離する

|役割|曲線 C/F_q|どの段階で使うか|
|---|---|---|
|1 点数対象|Z(T)=exp(Σ NₙTⁿ/n)=Π_x(1−T^deg x)⁻¹|入力の算術的定義|
|2 rationality|Z=P₁/((1−T)(1−qT))|trace＋有限次元性から出る結果。追加の正性ではない|
|3 cohomology|Hⁱ_et(C̄,Q_ℓ)、i=0,1,2|算術点とスペクトルを載せる共通対象|
|4 trace|Nₙ=Σ(−1)ⁱTr(Fⁿ\|Hⁱ)|全nの点数を同じ作用の反復へ接続|
|5 Frobenius|C、Jac(C)のq乗Frobenius射|任意に固有値を設定した行列ではない|
|6 determinant|Z=Πᵢ det(1−TF\|Hⁱ)^{(−1)^{i+1}}|traceのlog積分とZ(0)=1から導出|
|7 Poincaré duality|H¹の交代pairing、倍率q|αとq/αを組にする|
|8 functional equation|T↔1/(qT)|双対性の結果。線外pairを排除しない|
|9 weight/purity|H¹の全複素根についてabs(α)=q^(1/2)|証明すべき中間結論|
|10 polarization/positivity|同じJacobian上のRosati正性|曲線の決定的な幾何入力|
|11 絶対値制御|正形式＋π†π=q ⇒ abs(α)²=q|有限次元の固有vector計算|
|12 零点位置|T=q^(−s)、αT=1 ⇒ Re(s)=1/2|determinantとの完全対応を最後に使う|

表の指数 `(-1)^(i+1)` は行列式の交代積の指数を表す。smooth projectiveの一般次元では
各Hⁱのweightはiであり、全零点が一律Re(s)=1/2なのではない。
singular/nonproperの全H_cⁱがpure weight i、という主張もしない。

## 曲線の入力セット

曲線で十分なspineは、算術的実現・trace/determinant同定・Jacobian上の忠実性に、
同じ算術作用に対する正のRosati形式とscaled-adjoint identityを加えるもの。
Poincaré dualityやfunctional equationは比較に重要だが、最後のnorm計算に別途加える必要はない。

### FF1

- **Statement:** smooth projective geometrically connected C/F_qの有限次元H⁰,H¹,H²と自然なFが存在し、H⁰上1、H²上q。
- **Role in proof:** 度数と作用を算術から固定し、極と非自明分子を区別。
- **Can it be weakened?:** 必要なH¹と既知の二つの極を忠実に実現できればよい。
- **Is it logically independent of later RH conclusion?:** 有限次元性・functorialityの既知定理を入力。RHからこれらを定義したのではない。形式的独立性は主張しない。
- **Finite-field source:** Grothendieck exp.279 Thm5.1、Deligne I §§1.3–1.5。
- **Number-field analogue:** CCMのcyclic quotientとscaling。有限次元étale H¹と同じ対象ではない。
- **Analogue status:** PARTIAL。

### FF2

- **Statement:** 全nでNₙ=Σ(−1)ⁱTr(Fⁿ|Hⁱ)。従ってZの全divisorは交代determinantで回収される。
- **Role in proof:** 算術と零点の同一対象上での完全同定。
- **Can it be weakened?:** 十分なtest classの忠実なtraceと正当なdeterminant再構成でも代替できる。
- **Is it logically independent of later RH conclusion?:** 正性や絶対値制御を使わない。合成模型でも成立する。
- **Finite-field source:** Grothendieck Thm5.1、Deligne I (1.5.1)–(1.5.4)。
- **Number-field analogue:** explicit formula、CCM Thm4.16/6.1の全零点・重複度付きtrace。通常のTr(Fⁿ)ではない。
- **Analogue status:** PARTIAL（指定された核型test空間でのtrace対応はEXACT）。

### FF3

- **Statement:** H¹(C)≅H¹(Jac(C))で、Fと可換。End⁰(J)のTate module作用は忠実。
- **Role in proof:** 正性を使うJacobianの作用と、zeta分子を担う作用を同一視。
- **Can it be weakened?:** Fとそのadjointを含む代数の忠実な共通実現で足りる。
- **Is it logically independent of later RH conclusion?:** 幾何的比較定理であり、根の位置から選んだ空間ではない。
- **Finite-field source:** Milne AV、Oort §3、Kedlaya Chapter6。
- **Number-field analogue:** 算術商と独立に正の幾何的実現との、全modeを失わない比較。
- **Analogue status:** ABSENT（本監査でそのような比較定理は得られない）。

### FF4

- **Statement:** F_q上のample polarizationが定めるRosati†について、実End代数上τ(xx†)>0（x≠0）。
- **Role in proof:** 幾何と作用に結び付いた正のnorm。ℓ-adic cupを複素正内積と読み替えない。
- **Can it be weakened?:** 零点を担う作用に忠実な正定値部分で十分。nullspaceにmodeが隠れる半正性だけでは足りない。
- **Is it logically independent of later RH conclusion?:** ample divisorの幾何的正性として証明される。有限体RHを仮定しない。
- **Finite-field source:** Milne AV I §14 Thm14.3、Oort Prop3.3。
- **Number-field analogue:** 全零点を担う算術的trace pairingの正性。これは既知Weil criterionではRH同値。
- **Analogue status:** CONJECTURAL。対応する正の幾何的証明はABSENT。

### FF5

- **Statement:** 同じpolarizationについてπ†π=qI。
- **Role in proof:** normをq倍にする算術的機構。FF4と合わせて全|α|=√q。
- **Can it be weakened?:** 忠実な正表現上のscaled isometryで足りる。
- **Is it logically independent of later RH conclusion?:** Frobenius–Verschiebungとbase-field compatibilityで証明。正性とは別入力。
- **Finite-field source:** Milne AV II §1 Lemmas1.2–1.3、Oort Prop3.4。
- **Number-field analogue:** H(T_af,T_ag)=aH(f,g)は算術Weil trace形式で無条件に成立する。ただしHは正とは未証明。
- **Analogue status:** PARTIAL（形式的相似則はEXACT、positive adjointとしての使用はCONJECTURAL）。

### FF6（比較用・最終norm証明では冗長）

- **Statement:** cup dualityとTate twistによりα↔q/α、FEが成立する。
- **Role in proof:** weight候補と対称性を説明。正性の代替にはならない。
- **Can it be weakened?:** reciprocal spectrum closureで同じ対称結論を得る。
- **Is it logically independent of later RH conclusion?:** M1の線外模型で成立するので、これだけではRH結論を含まない。
- **Finite-field source:** Deligne I §2.3。
- **Number-field analogue:** ξ(s)=ξ(1−s)とMellin反転。これはEXACT。geometric Poincaré pairing全体は未同定。
- **Analogue status:** PARTIAL。

## 一般次元：曲線の正内積をそのまま仮定していない

Deligne Iの原定理はsmooth projective。smooth properへの後年の拡張、非properでの混合weightは別問題。
1974年のspineはLefschetz pencil、vanishing cycles、monodromy、tensor操作と極の制御である。
hard Lefschetzやstandard conjecturesの正性を入力として扱わない。

### D1

- **Statement:** pencilと弱Lefschetz/Lerayで、必要なvanishing-cycle lisse sheafへ還元できる。
- **Role in proof:** 高次元の問題を曲線上のlocal systemsの評価へ移す。
- **Can it be weakened?:** 同等の幾何的還元と相補部分の制御でよい。
- **Is it logically independent of later RH conclusion?:** 幾何的還元が先。purityを先取りしない。
- **Finite-field source:** Deligne I §§4–5,7.1。
- **Number-field analogue:** 対応する算術family/vanishing cyclesは未供給。
- **Analogue status:** ABSENT。

### D2

- **Statement:** symplectic monodromyと局所特性多項式の有理性がある。
- **Role in proof:** 偶数tensorの局所traceを実数の偶数冪にし、coinvariantsをTate型へ制約。
- **Can it be weakened?:** 必要な全tensorのcoinvariant・実数性を直接支配すればよい。
- **Is it logically independent of later RH conclusion?:** monodromyと有理性を別に証明する。有理性を最終purityから引用しない。
- **Finite-field source:** Deligne I Thms3.2,5.10,6.2。
- **Number-field analogue:** ζのlocal Euler因子は有理だが、global zerosを担うfamilyとtensor構造はない。
- **Analogue status:** PARTIAL（local rationalityのみ）。

### D3

- **Statement:** 各2k tensor Euler積の非負係数と、H_c²からの極の位置q^(−kβ−1)の制御が両立する。
- **Role in proof:** 局所収束半径の比較から|α|≤q_x^(β/2+1/(2k))。k→∞と双対性でpurity。
- **Can it be weakened?:** exponentの損失がkに依存しないO(1)で足りる。各有限kだけでは足りない。
- **Is it logically independent of later RH conclusion?:** D2・traceから導く評価。結論の純性を仮定しない。
- **Finite-field source:** Deligne I Lemmas3.3–3.6, §3.7。
- **Number-field analogue:** 全tensorで同じ算術対象の極を支配する定理は未供給。ζのEuler係数の非負性だけでは代替不可。
- **Analogue status:** ABSENT。

### D4

- **Statement:** Xの積とKünnethによりα^kを次数kiに載せ、積対象にも誤差O(1)の評価が成立する。
- **Role in proof:** 最終のexponent誤差を1/kへ縮める。
- **Can it be weakened?:** 同じ増幅を保つfunctorと全次数の一様な誤差制御でよい。
- **Is it logically independent of later RH conclusion?:** 正当な幾何的積と既に得た評価を使う。名前だけのtensorでは不可。
- **Finite-field source:** Deligne I §7.3。
- **Number-field analogue:** global ζ零点に対する同じ閉じた算術体系は未供給。
- **Analogue status:** ABSENT。

## 結論と出典

曲線での最小の最後の計算は `FF3 + FF4 + FF5 ⇒ purity`、零点結論へはFF1–FF2が必要。
FF4を「正性がある」と仮定して数体へ輸送するとRH義務を別名で置いただけになる。
一般次元の別経路では、正のEuler係数と全tensorの極の制御が同じ算術familyから出ることが核心。
この二経路を「dualityがあるから正」という一文に縮めない。

[Deligne I 原論文](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)、
[Grothendieck 原報告](https://www.numdam.org/item/SB_1964-1966__9__41_0.pdf)、
[Milne AV](https://www.jmilne.org/math/CourseNotes/AV.pdf)、
[Oort](https://math.nyu.edu/~tschinke/books/finite-fields/final/05_oort.pdf)、
[Kedlaya](https://kskedlaya.org/weil-cohom/chapter-6.html)。
Weil IIの一般混合sheafの全理論を追加入力にする必要は本比較にはなかった。
「Weil II全文を監査した」とは記録しない。
