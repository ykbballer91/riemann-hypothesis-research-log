**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/spiral-scale-topology.md` · Original SHA-256: `668a911ab35ada3687ce8fb18f6d39c2a68a840ac2de2e24e36072e1bac2915d`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Scale flow の位相・自己相似・保存量 — 独立な反証と到達限界

2026-09-29。root。数学的構造だけを扱う。物理的螺旋、DNA、黄金比等を前提としない。
以下の反例はζの反例ではなく、候補となる一般含意の反例である。RHはOPEN。

## 1. 反射の fixed locus を取り違えない

`z=s−1/2=alpha+it` と置く。関数等式は `z↦−z`。
この複素線形写像の点ごとのfixed locusは **z=0だけ**であり、虚軸全体ではない。
実構造 `z↦bar z` と組み合わせた反線形反射 `z↦−bar z` のfixed locusが `Re z=0`。
虚軸上では `z↦−z` は回転方向・高度の符号を反転する。
この区別をした上でも、二つの対称性は四重点 `±alpha±it` を許す。

正規化したcharacter `chi_z(u)=exp(−zu)` は

\[
|\chi_z(u)|^2=e^{-2\alpha u},\qquad
\frac d{du}|\chi_z(u)|^2=-2\alpha|\chi_z(u)|^2.
\]

通常の複素絶対値が全uで一定、または全実uで有界、という条件はalpha=0と同値。
これは正しい初等定理である。しかし全ζ零点がこの条件を満たすとの仮定はRHの再表現である。
回転という語からその仮定は得られない。

## 2. 可逆性・contractivity・保存する計量

一般のgroupは可逆でもnormを保存しない。`T_u=diag(e^(−alpha u),e^(alpha u))`
は全uで可逆、`T_(-u)=T_u^(-1)`、det T_u=1、反射で二成分が交換される。
それでもalpha≠0なら増幅と減衰がある。

`J=[[0,1],[1,0]]` とすれば `T_u* J T_u=J`。
標準symplectic行列に対しても同様である。自然なflux・Wronskian・determinant・
不定二次形式の保存は、相殺する増幅/減衰を排除しない。

一方、正定値行列Kについて `T_u* K T_u=K`、またはgroupの両方向で
`||T_u||≤1` が成立するなら、normは保存される。後者は
`||v||=||T_(-u)T_uv||≤||T_uv||≤||v||` による。
generator G のeigenvector vには

\[
G^*K+KG=0\quad\Longrightarrow\quad
2\Re\lambda\,\langle Kv,v\rangle=0.
\]

従って固有値の実部は0。これは独立な一般作用素論の機構だが、実際のζ零点を
非零のHilbert固有ベクトル、または対応する実スペクトルのgeneralized modeとして
漏れなく実現する構成が必要である。その同定を未証明のまま置けばHilbert–Pólya候補を改名しただけになる。
分布的resonance、非有界の相似変換、outgoing boundary conditionにはこの固有ベクトル計算を流用しない。

## 3. 実軸上unitaryな散乱と複素resonanceは両立する

`a>0` とし、自然なscalar Blaschke因子

\[
S_a(w)=\frac{w-ia}{w+ia}
\]

を取る。実wで `|S_a(w)|=1`、`S_a(-w)=S_a(w)^(-1)`。
上半平面ではcontractiveであるが、下半平面w=−iaにpoleを持つ。
実境界のunitarity・反転対称性はmeromorphic continuationのpoleを実軸へ拘束しない。
これは散乱系一般に関する最小の解析反例であり、ζの散乱モデルを構成したものではない。

背景: [Dyatlov–Zworski, Mathematical Theory of Scattering Resonances](https://math.mit.edu/~dyatlov/res/res_final.pdf)
は自己共役な散乱問題の実スペクトルと継続resolventのresonanceを区別する。
[Connes, 1998/1999原著](https://arxiv.org/abs/math/9811068) もcritical zerosとeventual off-line resonancesを区別する。
unitary scatteringという性質を、この欠落の解消として引用してはならない。

## 4. 線上の位相だけでは線外零点を検出しない

実構造と関数等式から `xi(1/2+it)` は実数である。
零点のない線上区間でその偏角は0またはpiであり、常に滑らかに回転する量ではない。
ζからGamma位相を除くRiemann–Siegel Z(t)についても同じ実数性がある
（[DLMF 25.10.1–2](https://dlmf.nist.gov/25.10)）。

`0<a<1/2,b>0` とし

\[
P(z)=((z-a)^2+b^2)((z+a)^2+b^2)
\]

を取る。Pは実係数の偶多項式で、零点は `±a±ib`。
一方

\[
P(it)=(a^2+b^2-t^2)^2+4a^2t^2>0\quad(t\in\mathbb R).
\]

従って完成関数の対称性と線上の偏角を保ちながら、線外の四重点を挿入できる。
例えばPを既存の実偶entire関数に掛けても、その線上の符号は変わらない。
Euler積や正確な明示公式を保つ変形ではないため、ζについての反例とは呼ばない。

四重点を含む閉輪郭のargument principleは当然4個を数え、位相幾何に矛盾は起きない。
零点が輪郭を横切らない限り、winding numberは零点の位置を連続変形しても不変である。
したがってwinding/indexだけでalpha≠0を禁ずる候補は棄却する。
全zero countと線上zero countが等しいと追加すれば、求める未証明の内容を戻しただけである。
Maslov/spectral flowを使うには具体的なFredholm/self-adjoint familyとζの全零点との同定が必要で、
整数値という性質だけでは不足する。

## 5. Exact self-similarityでも中心1/2を強制しない

正整数m≥2、0<r<1/mに対し、長さr^jをm^j本ずつ持つgeometric stringを考える。
総長は `sum (mr)^j<∞`、幾何ζは収束域で

\[
\zeta_{\mathcal L}(s)=\sum_{j\ge0}m^j r^{js}
=\frac1{1-mr^s},\qquad
\Re s>D=\frac{\log m}{\log(1/r)}.
\]

有理型接続のpole列は `D+2pi i k/log(1/r)`。
これはexact recursive scaling/log-periodicityであって比喩ではない。
Dは(0,1)内の任意の値を取り得るので、self-similarity自体はD=1/2を選ばない。
境界の幾何次元やMinkowski measurabilityを使う逆スペクトル定理の詳細条件は
[一次文献監査](../../../literature/literature/notes/spiral-scale-prior-art.md) で別に扱う。

さらにm=2,r=1/8を取り、そのgeometric factorから自然な双対積

\[
F(s)=(1-2\,8^{-s})(1-2\,8^{-(1-s)})
=\frac32-\sqrt2\cosh((s-1/2)\log8)
\]

を作る。これはentire、`F(s)=F(1-s)`、実構造と厳密な虚方向周期を持つ。
零点は `Re s=1/3,2/3` の二本の列だが

\[
F(1/2+it)=\frac32-\sqrt2\cos(t\log8)
\ge\frac32-\sqrt2>0.
\]

したがってexact scale recursion・双対性・critical-lineの一定位相を全て要求しても、
線外零点は排除されない。数値の零包含は等号の証明に使わず、上のfactorizationを証明とする。
当然、FはRiemann xiではなく同じEuler積も持たない。

## 6. Prime phase ensembleの収束を飛び越えない

`p^(-ks)=p^(-k/2) exp(−k alpha log p) exp(−ikt log p)` は恒等式であり、
対数座標のFourier/Mellin表現と整合する。しかし
`−zeta'/zeta(s)=sum Lambda(n)n^(-s)` の絶対収束はRe(s)>1。
alpha=0では係数の絶対和は発散し、正の有限energyとしてそのまま集約できない。
位相のある解析接続、明示公式のdistribution、compactな相関を持つ試験関数を区別する。
正則性やunitarityを収束域外へ維持するには追加の定理が要る。

既知のWeil明示公式は、全零点の複素スペクトルパラメータを許したまま成立する。
primeの実周波数log(p^k)が現れることは、双対側の零点パラメータの実数性を保証しない。
この不足は、prime Fourier modesを並べることや有限traceの数値的一致では解消しない。

## 7. 自然な保存量が既にある場合の結論

global test-space Weil formは平行移動で不変であり、zero-evaluation空間ではJを用いた
不定energyとして記述できる。構成とdomainは [BUILDERノート](spiral-scale-reduction.md) を参照。
この事実を `Q_W=conserved energy` という名前だけで正性へ昇格しない。
正定値の保存normと全零点のmode同定、または実際のevaluation range上のJ非負性が欠けている。
後者を仮定として置けばWeil positivity/RHの同値条件に戻る。

本稿の位相・自己相似・可逆性だけによる各候補は反例または同値性により終了する。
算術固有の新しいmechanismが不可能だという一般不可能定理は主張しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/spiral-scale-prior-art.md`](../../../literature/literature/notes/spiral-scale-prior-art.md)
- [`proofs/audits/spiral-scale-reduction.md`](spiral-scale-reduction.md)
