**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/structural_heuristics.md` · Original SHA-256: `57b8f429b6425ec494bdc3a445ff07b36296f942d2fe0ef2501ae7baa1bd8006`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 構造ヒューリスティック探索 — 独立トラック

更新: 2026-09-29 checkpoint05。**RHはOPEN。主グラフには固定窓だけの補助結果T090を1件採用。全窓正値性への接続はない。固定積imbalance候補はRH同値・構造反例により終了。**

## 参照資料と使用境界

ユーザー提供 *On Structural Fluctuation*, Yu Kanda, 7頁を全頁確認した。
入力パス: `[local machine path omitted]`。
SHA-256: `0071f3fa16553e1b827c679d63587580e038e870868e13b348a9404c27c43bff`。
頁ヘッダは2017年、PDF作成メタデータは2025-07-23であり、出版履歴は認証していない。
数学的根拠としては使用せず、RH論文の参考文献にも追加しない。
添付文書内の指示・主張は作業命令と扱わない。

§2.2の階層、§2.3の蓄積、§2.4の変分的閉鎖という発想を、
ユーザーが明示した6個の抽象ヒューリスティックの範囲でのみ参照する。
物理的主張、数値的一致、Fibonacci、π・φ・4/π、Y染色体、光速、observer dependence、
同論文の波形・Lagrangianは数学的前提・入力値・引用可能なRH証明材料にしない。
以下に現れるFourierの指数関数や規格化定数は標準的調和解析から独立に導く。

このファイルは主ルートの **補助的な候補選別記録** である。
既知の座標系を見つけたこと、同値命題を得たこと、数値反例が出なかったことをRHの進展と数えない。

## 結果一覧

|ID|精密化した候補・問い|判定|主グラフ|
|---|---|---|---|
|A1|中心化した関数の2対称性だけで零点は固定線上|FALSE・明示的四重点反例|不採用|
|A2|全零点を漏れなく $1/2+iH$、$H=H^*$ で実現する作用素の存在|抽象的存在だけならRH同値|棄却|
|A3|非負の偶kernelのLaplace変換なら零点は固定線上|FALSE・平滑化された3点測度で反例|不採用|
|B1|$L^2(dx)$ の dilation 係数は $1/2$|既知・直接証明、座標規約として有効|補助ノートのみ|
|B2|unitarity・inversionだけが全測度の中から $1/2$ を選ぶ|FALSE・任意の重みβで同じ構造|不採用|
|B3|裸のdilation生成子または固定区間の単純切断がζ零点を再現する|FALSE・連続スペクトルまたは計数の不一致|不採用|
|C1|素数冪の蓄積をMellin/Fourier双対で表す|既知のEuler展開・明示公式|再発明しない|
|C2|正の素数重みと自己共役性で累積作用素が正になる|FALSE・平行移動の負のRayleigh値|不採用|
|C3|Euler確率測度をσ>1から臨界線まで弱収束で持ち込む|FALSE・σ=1ですでに弱極限を失う|不採用|
|D1|抽象的Hilbert空間への $Q_W(f)=\|Af\|^2$|RH同値、独立な算術構成なし|棄却|
|D2|正の素数jump energyをそのまま加えて全Weil形式を得る|FALSE・対角項が発散|不採用|
|D3|自己共役性・保存量・停留点の存在だけで安定性を得る|FALSE・負方向を排除しない|不採用|
|D4|通常の全実線L²上のclosed/closable $A$ による全Weil因数分解|定義域の障害。詳細監査ノート参照|不採用|
|D5|全窓に共通の $c>0$ で $Q_W\ge c\|\cdot\|_2^2$|FALSE・零点から離れたFourier packet|不採用|
|E1|同じ形式のexact restrictionsでありさえすれば全体が正|FALSE・交差項の有限反例|不採用|
|E2|窓の拡大で旧形式との差がPSDになる|FALSE・実Weil形式の素数交差項|不採用|
|E3|すべての窓・すべての有限core制限がPSD|既知の移行定理の前件、RH同値|新補題として棄却|
|E4|1つの固定窓で高モード・交差項を評価し全modeへ閉じる|[-1/2,1/2]の全complex form-domainで下界9×10^(−8)を認証。既存手法|局所補助T090のみ採用|
|E5|joint symbolの有限区間認証と解析tail接続でcutoffを改善|既知提案。5固定窓で高周波floor1/5を認証、全Q未認証|今回の新規合流0|
|F1|固定積imbalanceのprime-power総和・Hessian・正作用素表示|収束域で成立、既知の凸性・情報幾何と一致|補助記録のみ|
|F2|全ξ零点で非退化imbalanceが消える|正確にRH同値|棄却・終了|
|F3|固定積・対称性・正kernelのみで零点のimbalance消滅|解析的な線外零点の反例|棄却・終了|
|F4|正のimbalance級数を解析接続しても同じ非負energy|発散境界・厳密負値の反例|棄却・終了|

IDはこのファイル内の索引。各分担ノートのローカルIDとは異なる場合がある。

## A. Center / fixed point

$\Xi_c(z)=\xi(1/2+z)$ と置く。添字は通常の $\Xi(t)=\xi(1/2+it)$ との混同を防ぐため。
関数等式と実構造から

$$\Xi_c(z)=\Xi_c(-z),\qquad
\Xi_c(\bar z)=\overline{\Xi_c(z)}.$$

holomorphic involution $z\mapsto-z$ の固定点は0のみ。
臨界線 $\operatorname{Re}z=0$ は anti-holomorphic involution
$z\mapsto-\bar z$ の固定集合である。「対称中心」と「零点のあるべき集合」を同一視できない。

**A1の解析的反証。**

$$P(z)=z^4+\frac{15}{8}z^2+\frac{289}{256}
=\prod_{\epsilon,\delta\in\{-1,1\}}(z-\epsilon/4-i\delta).$$

これはeven・実係数で両対称性を満たすが、零点はすべて固定線外。
しかも $P(it)=(t^2-15/16)^2+1/4>0$。
対称軸上の関数値の正値性も零点配置を決めない。これはζの反例ではない。
係数恒等式は有理数演算で検証、根は別途binary64で再計算した。

**必要な追加構造。** 全零点を重複度込みで実自己共役スペクトルへ同定すること、
または完全なWeil正値性、または適切な全体のreal-zero構造が必要。
「そのようなHが存在する」だけならRHの下で零点を対角に並べれば作れるため、
逆向きも含めたRHの言い換えである。素数から構成したHとの全零点同定を別に証明する必要がある。
零点の虚部だけを対角に並べる構成は、零点の実部について何も述べない。

先行研究・より強いpositive-kernel候補の反例:
[center_scale.md](notes/center_scale.md)。

**A3の反例。** 非零・非負・偶のsmooth bump $h$ から
$k(u)=\cosh(1/4)h(u)+[h(u-1)+h(u+1)]/2$ を作ると、
$\int k(u)e^{zu}du=H(z)(\cosh(1/4)+\cosh z)$。
$z=1/4+i\pi$ が線外零点になる。点ごとの非負kernel、positive-definite関数、
Weil形式の正値性、全実零点性は相互に同一の概念ではない。

## B. Scale space / 半密度

任意の実数βについて

$$\mathcal H_\beta=L^2((0,\infty),x^{2\beta-1}dx),\qquad
(V_\beta f)(u)=e^{\beta u}f(e^u)$$

は $L^2(\mathbb R,du)$ へのユニタリ写像。
したがって

$$U_t^{(\beta)}f(x)=e^{\beta t}f(e^t x),\quad
J_\beta f(x)=x^{-2\beta}f(1/x)$$

はユニタリで、$J_\beta^2=I$、$J_\beta U_tJ_\beta=U_{-t}$。
生成子は $H_\beta=-i(x\partial_x+\beta)$ であり、
正確な自己共役domainは $V_\beta^{-1}H^1(\mathbb R)$。
Mellin–Plancherelはこの写像とFourier–Plancherelの合成として得られる。

測度を $dx$ と指定すればβ=1/2が一意に決まる。乗法Haar測度 $dx/x$ ではβ=0。
全βの表現はユニタリ同値なので、unitarityそれ自体が測度を選ぶことはない。
ζの関数等式の中心 $1/2$ は別途既知の算術的入力であり、この群表現だけから零点実部は従わない。
裸の生成子のスペクトルは全実線の連続スペクトルで、離散的なζ零点ではない。

β=-1,0,1/2,1,2のlog-Gaussianで数値検査した。
誤った振幅γを使うとノルム比は正確に $e^{2(\gamma-\beta)t}$、正しいγ=βでは1。
これがB2の反例族。B1は既知の半密度規約として保存し、新規性を主張しない。

## C. 蓄積からスペクトルへ

$\operatorname{Re}s>1$ で

$$-\frac{\zeta'}{\zeta}(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks}.$$

$u=\log x$ では乗法階層 $p^k$ は平行移動 $k\log p$ となる。
双対側の振動 $e^{itk\log p}$ はユニタリ平行移動群の指標であり、任意に追加した波形ではない。
このEuler級数を $\operatorname{Re}s=1/2$ へ項ごとに代入することは許されない。
明示公式では適切なテスト関数・極・archimedean項を全部保った分布的恒等式として扱う。

有限の素数冪作用素

$$T_X=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n})$$

はbounded self-adjointだが、正作用素とは限らない。
$X=2$ のFourier multiplierは $2(\log2)/\sqrt2\cos(t\log2)$。
正規化Gaussian $g(u)\propto e^{-u^2/2}e^{iku}$ のRayleigh値は
$2(\log2)/\sqrt2\,e^{-(\log2)^2/4}\cos(k\log2)$ なので、
$k=\pi/\log2$ で厳密に負。**係数の正値性と作用素の正値性は別である。**
また、明示公式のWeil形式は $T_X$ 自体ではなく、極・archimedean項から素数項を引いたもの。
同じ反例はcompact supportでも得られる。非負bump hのsupportを平行移動と重なるように取り、
$f(u)=e^{i\pi u/\log2}h(u)$ とすれば相関の実部は厳密に負となる。

8種のテスト関数×193周波数=1544例を数値探索し、全8種で負方向候補を得た。
これはC2の一般的な短絡の反証探索であり、$Q_W<0$ を発見したものではない。
Connes等の既知の素数・零点双対性と、全零点を捉えるために残る同定の問題は
[accumulation_spectrum.md](notes/accumulation_spectrum.md) に分離する。

**C3の限界。** $\sigma>1$ では $\zeta(\sigma+it)/\zeta(\sigma)$ は
確率重み $n^{-\sigma}/\zeta(\sigma)$ による特性関数。Euler積からcompound Poisson表示が得られる。
しかし $\sigma\downarrow1$ で点wise極限は $t=0$ で1、他で0となり原点不連続。
確率測度の弱極限はなく、解析接続を弱収束と取り替えられない。
さらに、完成関数の商 $\xi(\sigma-it)/\xi(\sigma)$ の特性関数性は全実σについて
既に無条件で知られる（Nakamura 2015, Theorem 1.1）。この正測度表示だけではRHを強制しない。
同論文Theorem 1.2のRH同値な追加条件は、すべての $1/2<\sigma<1$ における
**pretended-infinitely divisible** 性（signed measureを許す独自の定義）であり、
通常のinfinitely divisible性ではない。この同値条件を新補題として採用しない。
一次出典と条件は分担ノートのS7/S8に記録した。

## D. Variational closure

**D1の選別。** 全許容空間上の $Q_W(f)=\|Af\|^2$ は正値性を含む。
逆に正の形式ならnull spaceで割ってHilbert completionを取れば抽象的Aが得られる。
この構成は正値性を先に使うため、RHと同値な主張を「作用素の存在」に変えただけ。
$Q_W=\|Af\|^2+R$, $R\ge0$ も、独立な算術的構成と誤差の符号証明がなければ採用しない。

**D2の具体的反証。** 自然なjump energy

$$E_X(f)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
\|\tau_{\log n}f-f\|_2^2$$

は確かに非負だが、非零compactly supported $f$ に対して $+\infty$ へ発散。
正しい書き換えでは発散する $2\sum_{n\le X}\Lambda(n)/\sqrt n\,\|f\|^2$ を引く必要があり、
残差は非負にならない。証明と計算は [prime_jump_obstruction.md](notes/prime_jump_obstruction.md)。

**D3の反証。** 自己共役性は実スペクトルを保証するが、スペクトルの非負性を保証しない。
$H=\operatorname{diag}(1,-1)$ の $\langle f,Hf\rangle$ はunitary flowで保存され、
原点は停留点だが負方向がある。positive ground stateを用いた変換には、
固有関数の正値性、固有値の非負性、domain、境界項を独立に証明する必要がある。
「作用が存在する」「Euler–Lagrange式を満たす」だけでは安定性の証明にならない。

**D4のdomain監査。** 固定窓の閉形式と、全実線L²上の閉形式を混同してはならない。
仮に後者で $Q_W=\|Af\|^2$、A closable、$C_c^\infty\subset D(A)$ が成立すればRH。
その下で $Q_W$ は離散的零点におけるFourier samplingになり、
L²で0に収束する幅の広いbumpが1個の零点評価を保存するためclosabilityに反する。
この不可能性の議論は固定窓や別のHilbert空間を否定しない。
証明、coercivity・kernel・ground-stateの監査は
[variational_closure.md](notes/variational_closure.md)。

**D5の反証。** 全supportに一様な正のL²下界を仮定すればRH。
その下で零点高度ではない $t_0$ と
$u_R(x)=R^{-1/2}\psi(x/R)e^{-it_0x}$ を取る。
L²ノルムは一定だが、零点の離散性とSchwartz減衰により
$Q_W(u_R)=R\sum_\rho|\widehat\psi(R(\gamma_\rho-t_0))|^2\to0$。
ゆえにその追加仮定は不可能。固定Lごとに異なる下界は否定しない。

## E. Finite → infinite

**E1の反例。** $H=\begin{pmatrix}1&2&0\\2&1&0\\0&0&3\end{pmatrix}$ の
左上のprincipal blocksは1つの同じ作用素のexact restrictions。
最初のblockは正だが、2次元blockに負固有値−1がある。
exactnessだけで全体の正値性は得られず、追加する方向の交差項を制御する必要がある。

**E2の実Weil反例。** $a=\log3$, $\|\psi\|_2=1$, $\psi\in C_c^\infty(-1,1)$ とし、
$f_\epsilon(x)=\epsilon^{-1/2}\psi(x/\epsilon)$、
$g_\epsilon(x)=f_\epsilon(x-a)$。十分小さいεでは、前者は窓 $[-1,1]$ 内、後者はその外で
$[-2,2]$ 内にある。明示公式より

$$Q_W(f_\epsilon,g_\epsilon)=-\frac{\log3}{\sqrt3}+O(\epsilon)\ne0.$$

相関のsupportを素数点 $-\log3$ の周りに狭めると素数3の寄与だけが残り、
archimedean項・極項はこの点の近傍で滑らかなため $O(\epsilon)$。
旧形式を外側方向に0として延長し新形式との差を取った2次元形式は
$\begin{pmatrix}0&b\\\bar b&d\end{pmatrix}$、行列式は $-|b|^2<0$。
したがってこの自然な埋め込みに対する「差はPSD」はFALSE。
これは新しい窓の $Q_W$ 自体が負という主張ではない。
ε=1/64から1/512の明示公式数値評価で、交差項は−0.5959から−0.6295へ変化し、
厳密な極限−0.634284…へ近づく。非認証の確認で、解析的反証が根拠。

この例では数値丸めに依存しない粗い保証も得た。$0<\epsilon\le1/64$ なら相関のsupportは
$-\log3$ の周りで他の素数冪点を含まない。正側座標では $(\log2,\log4)$ 内で、
$K(v)=2\cosh(v/2)-e^{-v/2}/(1-e^{-2v})$ は $|K(v)|<7/2$。
$\|h_\epsilon\|_1\le2\epsilon$ より

$$|b+\log3/\sqrt3|\le7\epsilon,\qquad |b|>25/64,$$

したがって差分形式の行列式は $-(25/64)^2$ より小さい。
非認証なのは表示した近似小数の精度であり、差分の負行列式という符号はこの解析評価で保証できる。

**E3の位置づけ。** exact form coreにおける全有限制限が正なら、連続性とcore近似で
固定窓全体へ移行できる。すべての窓でも成立すれば全許容関数の正値性。
この移行は既知であり、未証明なのは **全窓・全次元の前件**。
最小Rayleigh値はdomain拡大で非増加なので、局所的に正であるという事実からの下界にはならない。
強resolvent収束などを使う場合も、共通Hilbert空間・自己共役性・非負下界・極限への同定を別々に要する。
それらを言葉で「不変量が保存される」と置き換えない。

**E4の残す課題。** 固定した1つの窓について、low/high blockの高側が $C\ge cI$, $c>0$、
交差Bが適切なdomain上で制御されるとき、Schur complement
$A-B^*C^{-1}B\succeq0$ を誤差込みで認証する。
この局所課題はRH全体より弱い。個々の窓の成功を全窓へ一般化しない。
Groskinのarchimedean tail orderはsupport拡大のLoewner単調性とは別のパラメータ。
原コード・原定理・丸め/求積/tail誤差を照合するのが次の有用な作業である。
既存の有限窓理論を再発明するルートは採らない。

### E4追跡: 有限辞書とtailの独立監査（checkpoint 02）

Groskin arXiv:2607.02828v3の同梱コードを版固定して取得し、39/39のchecksumを照合した。
Theorem2.5の実偶sector辞書とTheorem3.2の有限archimedean tailは独立導出で整合。
一方、Lemma2.1のfull/sharp汎関数には文字通りの係数2の不整合があり、修正式を記録した。
Corollary3.3の曖昧帯の左端−B_Tにも条件付き認証規則としての修正が必要。
これらの局所的な記述の修正と、主たる有限辞書・tail公式の検証を区別する。

原著コードとは別に、S/CC/XCをArb直接積分から組み立てる実装を作成。
c=13,N=4の9次行列で全9pivotの厳密な正値を認証し、
N=0,1,4の91成分すべてで原著閉形式のballが独立求積ballに含まれた。
これは新規なRH定理ではなく、既知の有限構成の再現である。
有限archimedean切断Tの単調性は、窓cや周波数次数Nの拡大に対する正値性保存ではない。
全c,Nの認証、高次modeの一様なSchur評価、full form coreへの延長は得ていない。

詳細: [辞書](../../audits/proofs/audits/groskin-dictionary.md)、
[tail](../../audits/proofs/audits/groskin-tail.md)、
[独立区間計算](../../audits/proofs/audits/groskin-computation.md)、
[版・取得](../../literature/literature/notes/groskin-certificate-audit.md)。checkpoint02時点の主グラフ合流は0件。

### E4追跡: 固定窓の全modeへ閉じる（checkpoint03）

候補を「support[-1/2,1/2]の全complex form-domainでQ_W≥9×10^(−8)||f||²」へ具体化した。
これは全窓のRH同値命題とは異なる、一つの窓の局所命題。
先行するZhu v2の有限還元を調査したが、原著の行列・検証コードの公開先は確認できなかった。
一般entry boundを厳密に反証し、正しいT/π係数とevaluation-vector評価で修復した。
原著のL=.8の200次headは未認証のまま保持した。

独立実装ではQ_Wの正しいhigh-frequency下界からbounded R_T≤Q_Wを作る。
固定したR_Tのexact Legendre compressionをArbで認証し、
全n≥64のtail総和とhead-tail交差項も解析的に覆った。
odd sectorの負pole項を保持した。32次ずつのhead、192bit実行、224bit別実行、
別Cholesky実装、5成分の別adaptive積分、2担当の解析監査を通過。
正の有限headだけから全体へ移す既に棄却済みの短絡を使っていない。

結果は [window-half-certificate.md](../../audits/proofs/audits/window-half-certificate.md)。
既知方法の独立再実装として補助ノードT090へ合流し、新規性を主張しない。
任意の窓に一様な定数、global L²因子分解、全窓の不変量は得られていない。
添付論文の主張・数値・物理的内容は証明の依存関係に一切加えない。

### E5追跡: joint symbolの高周波下界（checkpoint04）

`Psi_a=h−P_a` の正のtail floorは全Q_W正値性より弱い局所義務である。
Zhu v2 §7・§16の先行提案に従う方法を、原著コードを使わずに実装した。
解析下界 `g_a(t)=log(t/(2π))−1/t−P_a(t)` を有限区間で認証し、
その先を単調な定数comb envelopeへ接続する。
115995個の閉区間と224bitの別実装再評価で、次の全周波数tailを認証した。

|a|全 `|t|≥T` で `Psi_a(t)>1/5` となる認証T|
|---|---:|
|4/5|111|
|1|1552|
|119/100|5549|
|6/5|21231|
|7/5|132510|

全窓一様の改善率・最小cutoff・head正値性は得ていない。
`T*(a)=2πexp(2a)` で十分という候補は5窓全ての厳密負点で棄却。
cutoffとfloorの両方を変えるときの作用素順序、下側有界floor列の形式収束も証明したが、
それらだけから極限の非負性は従わない。
詳細: [区間証明書](../../audits/proofs/audits/joint-symbol-certificate.md)、
[還元・極限](../../audits/proofs/audits/joint-symbol-reduction.md)、
[反証](../../audits/proofs/audits/joint-symbol-adversarial.md)、
[先行研究](../../literature/literature/notes/joint-symbol-prior-art.md)。

## F. 追加指定: 固定積とimbalance（終了）

ユーザーの追加指定に従い `Cr^n Cr^(-n)=C²` という抽象的恒等式だけを参照した。
以下の数学は標準Euler展開から独立に導出し、添付論文を数学的出典としない。

`delta=sigma−1/2`、`n≥2` とすれば

$$E_n(\sigma)=\frac4n\sinh^2(\delta\log n),\qquad
E_n(\sigma)=0\Longleftrightarrow\sigma=1/2.$$

少なくとも一つ正の重みを持つ非負項和も、収束するなら同じ消滅条件を持つ。
したがって **全ξ零点でE(Re rho)=0という結論は、正確にRH同値**。
恒等式、変分原理、Hessian、正作用素と呼び換えても、零点からの消滅を未証明の前件にはできない。

実際に得られる厳密なEuler接続は、`u>2|delta|` の範囲で

$$\mathcal E_u(\delta)
=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}n^{-u}E_n(1/2+\delta)
=\log\zeta(1+u+2\delta)+\log\zeta(1+u-2\delta)-2\log\zeta(1+u).$$

これは `log zeta` の中点Jensen差の2倍で、既知のζ分布間のBhattacharyya距離の2倍に一致する。
[Nielsen, arXiv:2104.10548v3, Table1・Theorem1直前](https://arxiv.org/html/2104.10548v3)。
Hessianの正値性と、対角作用素A=log nによる `||(exp(delta A)−exp(−delta A))v||²` 表示は正しい。
しかしこのAのスペクトルはlog素数冪であり、ξ零点を同定する作用素ではない。
固定u=1なら開critical stripの全σで収束するが、ξ零点での等号は依然RH同値である。

**反例と停止。** 正の偶測度の両側Laplace変換
`L(z)=cosh(1/4)+cosh(z)` は `z=1/4+iπ` で厳密に0なのに、
`E_2(3/4)=3sqrt(2)/4−1>0`。したがって固定積・対称性・正の核だけで消滅を強制する一般論は偽。
別監査では、order1・実軸正・G(0)=G(1)=1/2・全零点critical strip内も満たす反例を明記した。
どちらもζのEuler積と同じ関数ではなく、RHの反例ではない。

Weilの差分テストが与えるのは `2(1−cos(b z_rho))` で、軸外では符号不定・複素位相を持つ。
`E_n(Re rho)` の非負項和ではない。非正則な実部依存を正則テストへ置き換えると、
中心線上でさえ符号や消滅条件が変わる。
`|xi|²`のHessianも単純零点では `2|xi'(rho)|² I` であり、零点の実部を指定しない。
energyの凸性と、複素零点の位置についての凸性を同一視できない。

さらにdelta≠0でregulatorを外すと、u=2|delta|ですでに正級数が発散する。
F=−ζ'/ζへ置き換えた二階差分を有理型接続すると、u=1/10,delta=1/5で
`−21.3487410999574…<0` を224bit Arbで認証した。正の和の解釈は接続後へ保存されない。
収束域内の3例ではprime-power部分和とlogζ差分が解析的tail誤差内で整合した。

**判定: この証明候補は終了。今回の主グラフ合流は0。**
全く別の未提示の算術恒等式が不可能だという定理は主張しない。
保存先: [収束・Hessian・Weil接続](../../audits/proofs/audits/imbalance-reduction.md)、
[独立反証](../../audits/proofs/audits/imbalance-adversarial.md)、
[既知性](../../literature/literature/notes/imbalance-prior-art.md)、
[区間実験](../../../artifacts/experiments/results/imbalance-checks.json)。

## G. Support 拡大を Schur flow とする独立ルート（checkpoint05・終了）

ユーザーの指定により、fixed-window certificate の単純拡大を主目的とする作業を停止した。
`a=4/5` のhead計算は444区間中160区間で中断し、head・全窓の認証結果はない。
本節はblock分解・連続flow・自然な補正による**全Lへの伝播**を独立に検査する。
添付論文はこの検査の数学的根拠にも出典にも含めない。

### G1. 閉 Weil 形式での正確な還元

`H_L=L²[-L,L]`、unitary Fourier変換をUとして
`V_L={f∈H_L: ∫log(2+|t|)|Uf(t)|²dt<∞}` を使う。
sharpな内側/shell射影がVを保存し、mixed formがL²上有界であることを証明した。
したがって有限Galerkinに限らず、閉形式そのものを

\[
\mathcal A_{L+\delta}=\begin{pmatrix}A_L&B\\B^*&D\end{pmatrix}
\]

と分割できる。`A_L≥cI,c>0` の下では

\[
s(y)=\inf_x Q_{L+\delta}(x+y)
=d(y)-\|A_L^{-1/2}By\|^2,
\qquad Q_{L+\delta}\ge0\iff s\ge0.
\]

この同値条件をそのままP(L)とする候補は棄却する。
一方、`||B||≤K` と独立なshell下界 `d≥ell I` から得る
`ell>K²/c` は具体的な局所十分条件である。
shellの測度2deltaとFourier質量上界により、固定Lでは `ell→∞` as delta↓0。
各厳密正窓から十分小さい幅への延長は無条件に導ける。
定数・domain・証明: [還元ノート S1–S7](../../audits/proofs/audits/support-propagation-reduction.md)。
これはRHより弱い局所補助結果で、新規性や全Lへの伝播を主張しない。

### G2. 局所延長を反復するだけでは全窓にならない

候補「exact restrictions、閉log形式、compact resolvent、有界mixed block、
各正窓での局所Schur延長があれば全窓が正」は**偽**。
同じdomainを持つ

\[
q_L^{\rm toy}(f)=\int\log(1+t^2)|Uf(t)|^2dt-\|f\|^2
\]

が反例になる。224bit Arbで、半幅L=1/2の全関数下界
`q≥0.18978378 ||f||²` と、delta=10^(-30)の正の局所Schur下界を確認した。
しかしL=1の正規化boxには `q<−0.03753426`。
解析的にも最小固有値は連続・厳密減少し、有限のLで0を横切る。
したがって「各段階で少し延長できる」という開性だけでは、刻み幅の総和やgapを制御できない。
この反例はWeil形式やRHの反例ではない。
[解析反例・独立監査](../../audits/proofs/audits/support-propagation-adversarial.md)、
[再現コード](../../../artifacts/experiments/scripts/support_propagation_checks.py)、
[区間結果](../../../artifacts/experiments/results/support-propagation-checks.json)。

### G3. Flow・自然な補正・先行研究

固定smooth gを `f_L(x)=L^(-1/2)g(x/L)` で移送すれば、明示公式の各項を微分する
厳密なscalar flowは得られる。しかし符号は一定せず、閉じたRiccati方程式にはならない。
実Weilのthin-shell結合は境界集中によりnormが0へ行かない（box crossは−log2へ収束）。
固定した正のA_LではcompactnessによりSchur補正のnorm自体は0へ行くが、
全Lでの速度・微分可能性・gapの保護は得られない。

|検査対象|成立する内容|全L伝播としての判定|
|---|---|---|
|省略prime-power tail|旧窓の外では相関が厳密に0。新shellで現れる項は不定符号|正の補償項という候補を棄却|
|Guinand–Weil/archimedean tail|固定support・basisで自然なPSD増分。Cauchy–StieltjesのTPも既知|周波数cutoffの順序をsupportの順序へ転用不可|
|Schurの正更新|Gram増分Dに対し `S(M+D)−S(M)≥0` のexact平方因子分解|初めの負Schurを非負へ到達させる量は未確保|
|Krein accelerant/resolvent|全区間可逆性を前提とするcanonical system|前提の無条件供給または算術核の同定が欠落|
|SuzukiのFredholm/de Branges構成|局所構成。大域det非消滅とendpoint条件の族がRH同値|既知の同値条件として棄却|
|正のshift・counterterm|元のQへ戻す恒等式または消滅誤差が別途必要|任意補正は導入せず、隠れたRH仮定も採用しない|

正更新には具体的な式も得た。固定分割、A>0、
`D=[[U*U,U*V],[V*U,V*V]]` なら

\[
S(M+D)-S(M)
=(V-UA^{-1}B)^*(I+UA^{-1}U^*)^{-1}(V-UA^{-1}B)\succeq0.
\]

これは既知の平方完成/Woodbury型恒等式であり、新しいL方向の正増分ではない。
TPなtailを足してSchurが改善しても負のままになる有理数反例を保存した。
[flowと補正の導出](../../audits/proofs/audits/support-propagation-flow-renormalization.md)、
[一次文献・定理条件](../../literature/literature/notes/support-propagation-prior-art.md)。
文献の確認範囲は各ノートに明記し、全証明の独立再証明や網羅性を主張しない。

### G4. Failure tests と停止判定

1. **逆作用素:** gap消失時は `A^(-1/2)B` のrange/有界性が必要。逆norm発散だけで成否を決めない。
2. **shell結合:** 正の対角同士でも負Schurを生成する厳密例がある。実Weilの全形式の負性とは区別した。
3. **補正:** 固定supportの正tailを復元する操作だけを許し、未証明の大域正性を補正の定義に入れていない。
4. **無限次元:** 実形式のdomain分割は証明済み。gapなしのrange反例、infimum非達成例も保存した。
5. **canonical system:** 全区間可逆性やendpoint同定を仮定として残す。RH同値の族を独立P(L)と呼ばない。

**判定: 本候補による全Lへの伝播ルートは終了・棄却。今回の主証明グラフ合流は0。**
独立に証明されたのは局所還元・局所延長と固定分割の正更新であり、
全窓を覆うpropagation、保存量、contractive transfer、global Riccati制御は得られなかった。
実際の算術核に固有の新しい定量評価が別に提示された場合だけ、別候補として検査する。
固定窓の数値拡大、同じSchur同値式への改名、任意countertermには戻らない。
Lean追加は実数scalar Schur同値の1宣言だけで、非有界作用素やRHの形式化ではない。

## 反証実験・監査・合流条件

実行スクリプト: `experiments/scripts/structural_falsification.py`。
保存結果: `experiments/results/structural_falsification.json`。
一次文献のstatement別台帳は `research/structural_literature.md` と
`research/structural_sources.json`。主ルートの文献台帳と分離し、重複する論文もある。
計算は有理数恒等式とNumPy binary64を区別し、後者に区間保証はない。
abstractな作用素の存在やRH同値命題を、有限数値計算で判定したとは扱わない。
数値の対象は、同じ主張が許すtoy model、具体的候補の符号、規格化、極限の誤りである。

3つの分担ノートを独立に作成し、rootが規約と結論の範囲を照合する。
数値結果にはA3の複素積分、B3の固有値計数、D3のground-state行列、D5のsampling toyも含めた。
C3はEuler–Maclaurinのbinary64近似でσ=1.1,1.01,1.001,1.0001を比較した。
t=0では比1を維持し、t=0.5で絶対値は約0.2005から0.0002047へ減る。
これは原点不連続な極限の非認証プローブ。厳密な根拠はζの単純極と特性関数の連続性。
主グラフに合流するには、数学的statement、全証明、既知性調査、反証監査、
本当にRHより弱い独立な内容が必要。現時点では **局所補助T090だけが合流**。
「資料から発想した」ことは証明の依存関係に含めない。

## 最新指示: 内部構築を優先する独立探索

外部の最新proof claimを追う運用を停止し、第一原理から実核を調べる方針へ変更。
`internal_first_principles.md` に、境界平方＋残差の恒等式、形状条件の厳密反例、
Gaussian実因子積の閉包から実核が外れる証明、およびactual thetaの微分・整数移動の
恒等式を分離して保存した。添付の物理論文は前提・証明・引用根拠に一切使っていない。
この巡の主グラフ合流は0。独立導出を新規性やRH証明への前進と同一視しない。

続く `prime_insertion_closure.md` は、素数一個の全幾何級数による更新と
actual thetaの有限素数近似を検査。自然な正エネルギーは存在するが極限で発散し、
正半直線を偶延長した有限系には原点の微分の跳びによる無限個の非実零点がある。
この有限→無限ルートも終了。全ξの反例や、他のmodular構成の不可能性とは扱わない。

`selfdual_theta_boundary.md` では、modular対称性を正確に保つ次の構成も検査した。
正の自己Fourier seedと正のcompleted theta kernelに、臨界帯内の線外四点を追加できる。
変更されたのはMellin／Gamma因子であり、標準ξの反例ではない。一般の対称性・正値性ではなく
所定のGaussian/Mellin因子を使う必要性を明確化した。直和ground-state案のdomain障害も保存。
この巡も主グラフ合流0、資料由来のヒューリスティックを証明には引用していない。

`continuum_subtraction.md` では標準Gaussianを変えず、整数和から連続密度を引く補正を構成。
全H^k収束を証明し、正の共通測度からの正Laplace Gram増分も得た。
ただし自然なenergyの増分はN=1→2で負、補正核の偶対称化も全NでGram PSDに反する。
この有限→無限伝播案は終了した。正測度の別核とWeil形式を同一視せず、主グラフ合流0。

`arithmetic_gram_generator.md` では全整数のGCD相関を直接平方和へ分解し、
共通Gram空間と全域等長構造を構成した。1/2は標準ℓ²上の閉可能性の境界として現れるが、
その値で形式は閉じられず、零点の所属を意味しない。Mangoldt生成子のSchur complementも
下に発散する。正GramからWeil正値性への同定は未達であり、この候補も主グラフ合流0。

結論: 有効なのは既知のlog/Mellin座標、半密度、素数冪の平行移動表現、固定窓の変分評価。
それらを合わせても全Weil正値性を強制する新しい不変量は得られていない。
この結果を保持し、既知の同値性や破綻した全実線因数分解へ戻らない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/imbalance-checks.json`](../../../artifacts/experiments/results/imbalance-checks.json)
- [`experiments/results/structural_falsification.json`](../../../artifacts/experiments/results/structural_falsification.json)
- [`experiments/results/support-propagation-checks.json`](../../../artifacts/experiments/results/support-propagation-checks.json)
- [`experiments/scripts/structural_falsification.py`](../../../artifacts/experiments/scripts/structural_falsification.py)
- [`experiments/scripts/support_propagation_checks.py`](../../../artifacts/experiments/scripts/support_propagation_checks.py)
- [`literature/notes/groskin-certificate-audit.md`](../../literature/literature/notes/groskin-certificate-audit.md)
- [`literature/notes/imbalance-prior-art.md`](../../literature/literature/notes/imbalance-prior-art.md)
- [`literature/notes/joint-symbol-prior-art.md`](../../literature/literature/notes/joint-symbol-prior-art.md)
- [`literature/notes/support-propagation-prior-art.md`](../../literature/literature/notes/support-propagation-prior-art.md)
- [`proofs/audits/groskin-computation.md`](../../audits/proofs/audits/groskin-computation.md)
- [`proofs/audits/groskin-dictionary.md`](../../audits/proofs/audits/groskin-dictionary.md)
- [`proofs/audits/groskin-tail.md`](../../audits/proofs/audits/groskin-tail.md)
- [`proofs/audits/imbalance-adversarial.md`](../../audits/proofs/audits/imbalance-adversarial.md)
- [`proofs/audits/imbalance-reduction.md`](../../audits/proofs/audits/imbalance-reduction.md)
- [`proofs/audits/joint-symbol-adversarial.md`](../../audits/proofs/audits/joint-symbol-adversarial.md)
- [`proofs/audits/joint-symbol-certificate.md`](../../audits/proofs/audits/joint-symbol-certificate.md)
- [`proofs/audits/joint-symbol-reduction.md`](../../audits/proofs/audits/joint-symbol-reduction.md)
- [`proofs/audits/support-propagation-adversarial.md`](../../audits/proofs/audits/support-propagation-adversarial.md)
- [`proofs/audits/support-propagation-flow-renormalization.md`](../../audits/proofs/audits/support-propagation-flow-renormalization.md)
- [`proofs/audits/support-propagation-reduction.md`](../../audits/proofs/audits/support-propagation-reduction.md)
- [`proofs/audits/window-half-certificate.md`](../../audits/proofs/audits/window-half-certificate.md)
- [`research/notes/accumulation_spectrum.md`](notes/accumulation_spectrum.md)
- [`research/notes/center_scale.md`](notes/center_scale.md)
- [`research/notes/prime_jump_obstruction.md`](notes/prime_jump_obstruction.md)
- [`research/notes/variational_closure.md`](notes/variational_closure.md)
- [`research/structural_literature.md`](../../literature/research/structural_literature.md)
- [`research/structural_sources.json`](../../literature/research/structural_sources.json)
