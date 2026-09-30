**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase4/notes/product_formula_star.md` · Original SHA-256: `a1b163bbe00dc27ac3ab6494d252d8ffe7bda406ba7be2f41abb50898578d45e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase IV — 積公式・アデール内積・canonical starの構成と検査

2026-09-29。Phase IIIはread-only。以下の否定は具体的なpairing候補に限る。
RHやTate理論の反証ではなく、新規性の主張もない。

## 1. finite placesとinfinityを同時に入れる

A=A_Q、標準加法文字ψ:A/Q→S¹と自己双対Haar測度dxを使う。
実素点はdx∞、有限素点はvol(Z_p)=1。test spaceはSchwartz–Bruhat S(A)。
既知の積公式 Π_v|r|_v=1 (r∈Q×) によりrの掛け算はdxを保つ。

    P(f,g)=∫_A f(x)overline(g(x))dx

は既知算術対象上の非退化な正内積で、Hilbert completionはL²(A,dx)。
positivityの源はANALYTIC / REPRESENTATION-THEORETIC、測度とQ×不変性の源はARITHMETIC。
有限素点を省略し後でΓを足す構成ではない。

idèle aに対しR_a f(x)=f(a⁻¹x)とすると変数変換から

    P(R_af,R_ag)=|a|_A P(f,g),
    R_a* = |a|_A R_(a⁻¹),
    U_a=|a|_A^(−1/2)R_a は unitary.

積公式はr∈Q×に対する|r|_A=1を供給する。
しかし、積公式から全零点を担うquotientの非退化性が出るわけではない。
元のL²(A)のnormを、idèle上の算術的商のnormと無断で同一視しない。

## 2. 求める随伴恒等式はambient spaceでは実際に成立する

a_t=(e^t,1,1,…)、R_t=R_(a_t)とする。
S(A)上の生成子Θ=−x∞∂_(x∞)について、積分 by partsは

    P(Θf,g)+P(f,Θg)=P(f,g)

を与える。無限端の項はSchwartz性で消え、原点のx∞因子も境界項を作らない。
D=Θ−1/2はa_tの正規化unitary群の生成子である。

domainを形式的に済ませないため、実軸の正負二つの半直線を
V_±f(t)=e^(t/2)f(±e^t)でL²(R,dt)へ移す。
V_± D V_±⁻¹=−∂_t。従って閉生成子のdomainは各半直線でH¹(R)に対応し、
有限adèle部分とのHilbert tensor productを取る。
正確にはlog座標でH¹(R;L²(A_fin)⊕L²(A_fin))というvector-valued domainを使う。
標準のtranslation unitary群は強連続であり、その生成子Dはskew-adjoint。
よって適切な閉包についてΘ*=1−Θが成立する。

これは目標式に似せた人工的adjointではない。既知の測度から計算した恒等式である。
ただしスペクトルは連続な1/2+iRで、非自明ζ零点を離散固有値として全回収したのではない。
このambient identityだけをPhase IV Level3達成とは呼ばない。

積公式単独でcenterが決まるわけでもない。
idèle class上のweight |u|^(2c)d×uは任意の実cについてQ×へ不変であり、
R_aのnorm倍率は|a|^(2c)、形式的生成子の対称部分はcとなる。
本構成の1/2は、固定した加法Haar測度の一次元Jacobian倍率から来る。
その正規化をactual zero-bearing quotientのweight theoremへ移す橋はない。

## 3. Fourier dualityをstarにすると正性が付いてくるか

Fourier変換Fは自己双対測度についてunitaryで、F²f(x)=f(−x)。
変数変換により

    F R_a = |a|_A R_(a⁻¹) F,
    F Θ = (1−Θ) F.

even subspaceではF²=I、F*=Fなので、自然なtwisted pairing

    P_F(f,g)=P(f,Fg)

はHermitian。だがpositiveではない。
bilinear form B₀(f,g)=∫fgに、標準共役starを使えばPとなる。
even subspaceでFourierと共役を合成した別のantilinear involutionを使えばP_Fとなる。
どちらのstarも定義できることと、どちらもpositiveであることを混同しない。

### actual adelic test core上の厳密な負方向

u=πx²、g(x)=e^(−πx²)として

    h∞(x)=(8u³−30u²+15u)g(x),
    h=h∞ ⊗ Π_p 1_(Z_p).

Gaussian微分から

    F∞(ug)=(1/2−u)g,
    F∞(u²g)=(u²−3u+3/4)g,
    F∞(u³g)=(−u³+(15/2)u²−(45/4)u+15/8)g.

従ってF∞h∞=−h∞、有限素点ではF_p1_(Z_p)=1_(Z_p)なのでFh=−h。
さらにh(0)=0、∫_A h=Fh(0)=0。poleを消す二つのtest条件も満たす。
Gaussian momentsを用いると

    ||h||² = 585/(32√2),
    P_F(h,h) = −585/(32√2) < 0.

これはEuler因子やGamma factorを別のzetaに置換した反例ではない。
actual adelic Schwartz testを一つ取って、候補P_Fの符号を計算したものである。
このtestのTate zeta integralまで照合すると、Re(s)>1で

    Z(h,s) = [s(s−1)(2s−1)/2] Γ_R(s)ζ(s) = (2s−1)ξ(s),
    Γ_R(s)=π^(−s/2)Γ(s/2).

この式の乗法Haar規約はd×x∞=dx∞/|x∞|、
d×x_p=(1−p⁻¹)⁻¹dx_p/|x_p|、従ってvol×(Z_p×)=1。
加法の自己双対測度と乗法Haarを同じ記号で混同しない。

ここに現れる多項式はtestのMellin transformによる既知の乗数であり、
新しいtarget functionの零点をRHへ転用しない。追加因子2s−1も隠さない。
Γ_Rの定義、全finite Euler factors、pole除去を同じ計算に保持した。
P_F自体は正のpairing候補から即時に除外する。

またP_Fに関するformal adjointはFΘ*F=Θであり、
Fourierによるtwistがpositive adjoint relationを自動的に改善するわけではない。
|F|=Iへ置換すればPへ戻るだけで、zero quotientの問題は解けない。
(I+F)/2を使えば負固有部分をkernelへ捨てるため、完全性を別に証明しない限り採用しない。

## 4. local-to-global positivityが供給しないもの

restricted tensor productのPは、純粋tensorに対してlocal normsの積になり、
ほとんど全ての有限素点で基準vectorのnormが1なので定義は収束する。
これは正のambient pairingを構成する正しいlocal-to-global手順。
しかしprime-power traceやpole subtractionの符号をこのnormから導いたわけではない。

finite contribution: vol(Z_p)=1、local zeta integral=(1−p^(−s))⁻¹。
infinity contribution: Gaussianのlocal zeta integral=Γ_R(s)。
pole contribution: Poisson/Tateの原点評価f(0)と積分Ff(0)がs=0,1の項を生む。
normalization: ψ、自己双対測度、標準Gaussianを同時に固定。自由なcountertermなし。

Pを全零点の算術商へ渡すには、新たな比較写像・normの一致・radical処理が必要。
CCMの指定weighted L² modelを使った候補については `adelic_descent.md` のno-goがある。
他の全てのpositive formsが不可能だとは結論しない。

## 5. 提示されたadjoint候補の論理的強さ

Θ*=1−Θはpositive normと適切なdomain上では線制約を与える。
一方、unitary involution Jを含む JΘJ⁻¹=1−Θ* だけでは足りない。
例えばΘ=diag(3/4,1/4)、J=[[0,1],[1,0]]、標準正内積ではこの式が成立するが、
両固有値は臨界線上にない。Jを勝手に省いてはいけない。

さらに依頼中のliteral Θ⁻¹=1−Θを、そのまま作用素恒等式と解釈すると、
共通invariant domainでΘ²−Θ+I=0となる。
固有値は(1±i√3)/2の二値だけなので、無限に多く高さが非有界な実際のζ零点を回収できない。
これはinvolutionを介する共役関係の代わりにはならず、このliteral候補は終了。
Θ*Θ=Cも、C=cIというscalarの場合で原点からのmodulusを縛るだけであり、
追加構造なしに垂直線を強制しない。一般の未指定Cなら固定した円周すら定まらない。

## 6. finite-field role cardと判定

Finite-field object: polarized Jacobianの正normと算術Frobenius。
Number-field candidate: S(A)⊂L²(A)、加法Haar内積P、idèle dilation。
Exact matching property: finite/infinite placesを含む正性、scaled isometry、閉生成子のΘ*=1−Θ。
Missing property: same positive spaceから全zero-bearing quotientへの非退化・重複度保持比較。
Proof: 上記の測度変換、log座標、Poisson/Fourier、local Mellinの直接計算。
Counterexample attempts: Fourier-starはpole-free actual test hで負。Jを含む弱い式には2×2反例。
RH-equivalent assumption used?: 計算にRHなし。全零点を正しいnormへ同定する未証明条件を採用しない。
Decision: ambient Pの構成は既知の有効な事実として保存。RH bridgeとしての候補は終了。

## 7. 出典と確認範囲

[Stephen Kudla, Tate's Thesis](https://u.cs.biu.ac.il/~reznikov/courses/kudla-1.pdf),
§2 product formula、§3自己双対測度とProp3.5/Lemma3.6、§4 (4.1)–(4.8)。
これは著者によるTate理論の一次講義資料で、Tate1950原論文の全頁を再検証したとは扱わない。
Fourier多項式、norm、随伴、Mellin乗数は本ノートで独立計算した。
[CCM2007](https://arxiv.org/pdf/math/0703392v1) §§4,6は算術quotientの比較用。
