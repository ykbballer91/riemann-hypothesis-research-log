**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/one_prime/notes/abstract_return.md` · Original SHA-256: `faa2567d34b9afabb8f06ddc0ccf0df89d7160f12c7c20398d958539ddc649a3`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# One-prime subexponential return：抽象補題と最小量化

2026-09-29。RHを仮定しない一般補題。作用素の算術的成長評価はここでは証明していない。Hilbert正性・trace・determinant・compact resolventはいずれも使わない。既知の基本的成長比較を独立に証明し、新規性を主張しない。

## AR1. 最小のスカラー比較

a,b>0、C≥0に対し a^m≤C b^m が全ての整数m≥0で成立するなら a≤b。
証明：a>bなら(a/b)^mは非有界でCを超える。□

従って全ε>0についてa^m≤C_ε exp(εm)ならa≤1。
a⁻ᵐにも同じ評価があればa≥1、よってa=1。
各C_εはεに依存してよい。最初からε=0での一様有界性は必要ない。

より弱く、ある非零値ℓ(f)と正数列b_m^±について

    |λ|^(±m)|ℓ(f)| ≤ C b_m^±,   limsup log(b_m^±)/m ≤ 0

だけでも|λ|=1。全vectorに一つのoperator norm estimateを要求するより弱い。
ただし算術的証明では、零点位置を使って都合のよいwitnessやtopologyを定義してはならない。

## AR2. Banach/Hilbert：両方向rateの正確な不等式

X≠0を複素normed space、Tをbounded invertible operator（逆もbounded）、
ℓ≠0をbounded linear functional、ℓT=λℓとする。λ≠0：λ=0ならTがontoなのでℓ=0。
全m≥0について

\[
\ell T^m=\lambda^m\ell,\quad
\ell T^{-m}=\lambda^{-m}\ell,\quad
|\lambda|^{\pm m}\le\|T^{\pm m}\|.                     \tag{AR2}
\]

最後の式はdual normで||ℓT^m||≤||ℓ||||T^m||と||ℓ||>0を使うだけ。
固定fの定量式なら、|ℓ(f)|>0に対し

\[
|\lambda|^{\pm m}|\ell(f)|
 \le C_\ell N(T^{\pm m}f)
 \le C_\ell a_m^\pm N(f).                              \tag{AR2'}
\]

\[
g_\pm=\limsup_{m\to\infty}\frac1m\log\|T^{\pm m}\|
\]

と置くと

\[
-g_-\le\log|\lambda|\le g_+,\qquad
|\log|\lambda||\le\max\{g_+,g_-\}.                    \tag{AR3}
\]

g_++g_-≥0は||T^m||||T^-m||≥1から従う。Banachではsubmultiplicativityにより両rateの極限が存在するが、この補題はlimsupだけで足りる。

λ=2^(ρ−1/2)、L=log2なら

\[
-g_-/L\le\Re\rho-\tfrac12\le g_+/L,\qquad
|\Re\rho-\tfrac12|\le\max\{g_+,g_-\}/\log2.             \tag{AR4}
\]

両gが0ならRHの実部条件が従う。operator growthを全零点と無関係に証明する義務は残る。
片方向だけのestimateは半平面制約しか与えない。ただし全零点のreflectionを別途用いれば、片方向だけでも全零点へ一様に適用できる場合は逆の半平面が得られる。今回はその追加条件に頼らず両方向を扱う。

## AR3. Locally convex：operator normという語を置き換える

XをHausdorff locally convex complex space、Tをcontinuous linear automorphismとする。
ℓ∈X'は非零、ℓT=λℓ。以下を明確に区別する。

EQUI: {T^n:n∈Z}はequicontinuous。すなわち全continuous seminorm qに対し、
continuous seminorm rとC>0がありq(T^n f)≤C r(f)（全n,f）。

SUBEQ: 全ε>0に対し{e^(−ε|n|)T^n:n∈Z}がequicontinuous。
すなわちq(T^n f)≤C_(q,ε)e^(ε|n|)r_(q,ε)(f)。入力seminormはεとqに依存してよいがnには依存させない。

POINTSUB: 全q、全f、全ε>0について、あるC_(q,f,ε)>0があり
q(T^n f)≤C_(q,f,ε)e^(ε|n|)（全n）。

EQUI⇒SUBEQ⇒POINTSUB。POINTSUBだけで|λ|=1を導ける。
実際q(f)=|ℓ(f)|はcontinuous seminormである。ℓ(f)≠0のfを一つ選び、AR1を正負方向に適用する。
全seminormを使わず、|ℓ|を支配するseminormについてそのwitnessのgrowthが劣指数なら足りる。

Fréchet空間ではPOINTSUB⇒SUBEQも成立する。固定ε,qについてA_n=e^(−ε|n|)T^nとし、
E_m={f:sup_n q(A_n f)≤m}を取る。各E_mは閉・絶対凸、POINTSUBにより和集合がX。
Baireの定理によりあるE_mは内点を持ち、E_m−E_m⊂E_(2m)は0の近傍を含む。
従ってsup_n q(A_n f)は0で連続、equicontinuityを得る。一般barrelled空間でも同じ原理。
任意locally convex/bornological空間へBaireの結論を無条件に移さない。

一般TVSでも「各orbitがbounded」なら連続ℓの像はboundedであるためunit modulusを得る。
ただしbornological representationのbounded action、integrated operatorのnuclearity、
bounded subsetを各T^nが個別に送る性質は、全nのequicontinuityとは違う。

先行研究との照合：[Wegner, 1408.5037v1](https://arxiv.org/pdf/1408.5037v1), §2 Definition 1 / Lemma 2は指数重み付きequicontinuityとseminorm systemのrecalibrationを区別する。固定したseminormを左右で同一にする条件は、異なる入力seminormを許す位相的条件と同じではない。本ノートのSUBEQは後者を採用する。Fréchet spectrumの一般理論をBanachのspectral-radius公式で置換しない。

## AR4. 多項式成長を許す意味

||T^n||≤C(1+|n|)^AはSUBEQを与えるがpower boundedとは限らない。
T=I+N, N²=0, N≠0ならT^n=I+nN（負整数も同じ）。
全finite Jordan blockについて多項式成長なので、subexponential版はunitary化と違いJordan jetsを排除しない。

ただし各modeの多項式boundを、一つの無限次元operatorの一様subexponential boundへ足してはいけない。
反例：Hilbert direct sum ⊕_(m≥1) C^m上でT=⊕(I+aN_m), 0<a<1、N_mはnilpotent shift。
TとT⁻¹はbounded、全finite blockの固有値は1だが、

    ||T^n||=(1+a)^n,  ||T^(-n)||=(1−a)^(-n)  (n≥0)。

上界はbinomial/Neumann展開。正冪の下界はN_mの+1に対する長いほぼ定数vector、逆冪の下界は−1に対する長いほぼ交代符号vectorをm→∞で取れば得る。
有限blockのJordan eigenvectorsは全体に稠密だが、uniform block-size controlがない。
この例は零点の多重度についての主張ではなく、位相を無視した推論の反証である。

## AR5. 一素数と連続flowの関係

Banach上に既にC0群W_uがある場合、一つのL>0でT=W_Lの両方向subexponential growthは
連続群全体の両方向subexponential growthと同値。
証明：u=nL+r, 0≤r<Lと書き、M=sup_(0≤r≤L)||W_r||<∞を使う。
||W_u||≤M C_ε exp(ε|n|)≤M C_ε exp(ε)exp(ε|u|/L)。逆は部分列。

この観察はp=3や全素数の条件を追加しない。one-primeの算術証明を得れば十分だが、
既存C0群上では時間を離散化するだけで未解決のgrowthが自動的に弱くなるわけではない。
群を最初から仮定しないAR1–AR4にはこの連続時間の条件は不要。

## AR6. 結論に必要でないものと、未証明のもの

RHの実部の結論には各非自明零点の非零continuous characterを一つずつ保持すればよい。
no-extra-spectrum、trace class、determinant、compact resolvent、完全Hilbert基底、simple zerosは不要。
T_2だけではρとρ+2πik/log2のmultiplierがaliasするため、flowの重複度をT_2の一固有値の重複度と同一視しない。

この補題は「線外zeroが存在すれば、それを保持するspaceでは対応するorbitに指数成長が必要」を示す。
線外zeroの存在も不存在もここからは示さない。「actual quotientではどんなtopologyも指数growth」と無条件に断定することもできない。
抽象的なunit-circle character空間ではzero-retention相当の評価とsubexponential controlは両立する。
従って一般的な両立不能定理でRHを反証したと誤記しない。
