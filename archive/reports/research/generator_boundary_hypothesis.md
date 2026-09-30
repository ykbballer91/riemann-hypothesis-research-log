**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/generator_boundary_hypothesis.md` · Original SHA-256: `6d6642b0ba2111a84c9802608724e10736ec3aa7a2bb7f839f196a1e37e1f696`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# RH Phase II — Generator / Boundary hypothesis

2026-09-29。Phase Iの23サイクルとは独立したトラック。
**RHはOPEN。3 major attemptsの検証と、指定されたstrategy reviewを完了した。**
生成子・exact arithmetic boundary mapは構成できたが、線外状態を禁止する新しい
独立の算術機構は未取得。主グラフ合流0、追加仮定0、RHへの証明距離短縮の主張なし。
物理・宇宙論・生物学は数学的前提や引用根拠に一切使用していない。

実行制約は phase2_charter.md（原資料参照・公開版未収録: `research/phase2_charter.md`）。
A/B/C/Dを並列比較し、標準Euler/Gammaを保持する具体的作用素を持つCへ主作業を集中。
A/Bも全対象を使った具体構成を検査し、Dは初期screenとして扱った。
以下の各候補の詳細ノートに、証明・domain・先行文献・反例のscopeを保存した。

## 1. Candidate C — actual arithmetic scattering generator

**Candidate generator:** modular surface \(X=\mathrm{PSL}_2(\mathbb Z)\backslash\mathbb H\)
のDirichlet閉形式からの非負自己共役Laplacian \(G\)。

**Arithmetic input:** primitive整数対、totient Euler積、標準Gamma、全素数。全て保持。

**Boundary data:** Eisenstein seriesの零次Fourier係数は
\[
y^s+\phi(s)y^{1-s},\quad
\phi(s)=Z(2s-1)/Z(2s),\quad Z(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u).
\]
primitive classesを積分してtotient級数へ、Euler積でζ比へ変えるexact map。
さらに \(\Re u>1\) では
\[
\zeta(u)=\prod_{j\ge0}
\frac{\Gamma((u+j+1)/2)}{\sqrt\pi\Gamma((u+j)/2)}\phi((u+j+1)/2).
\]
有限積は \(\zeta(u)/\zeta(u+N)\)。局所一様収束と解析接続による境界→全関数の再構成である。

**Evolution law:** \(e^{-itG}\) はunitary。cusp半密度で \(-\partial_v^2+1/4\)。

**Why 1/2 appears:** 測度 \(dy/y^2\) のlog半密度と散乱channelの中心。
ζ変数は \(u=2s\) なので、ζの1/2は散乱極の1/4へ移り、channelの1/2とは別。

**What forbids off-line states:** 得られていない。全非自明零点
\(\rho=\beta+i\gamma\) は散乱極 \(s_\rho=\rho/2\) へ移り、
\(Z(\rho-1)=Z(2-\rho)\ne0\) により相殺なし・重複度一致・指定strip内の余剰なし。
しかし
\[
\Im[s_\rho(1-s_\rho)]=\gamma(1-\beta)/2\ne0
\]
なので、RH下でもGのL²固有値にはならない。自由度はresonanceの実部と増大率に残る。

**Known prior art:** Müller (2007)、Lagarias–Suzuki (2006)のactual Eisenstein/cut-off構成。
該当式・条件を構成後に照合。独立導出を新規発見とは扱わない。

**RH-equivalent hidden assumption?:** Gの構成はNO。開strip \(0<\Re s<1/2\) 内の
全散乱極（非自明ζ零点由来）の実部1/4を追加するならYES。\(s=1\) の極は含めない。

**Synthetic counterexample status:** generic模型に依存せずactual算術で固有値との不一致を証明。
全Euler/Gammaを保つ別関数やRH反例を作れたとは言っていない。

**Exact missing lemma:** 同じ開strip内の全散乱極の実部を1/4へ固定する独立な算術rigidity。
結論だけを新lemmaとすればRH同値。独立機構は未取得。

**Decision:** exact生成・自己共役性・scalar pole対応は成立するが、要求された
critical-line-only state spaceにはならず停止。自然なcut-off修復も
\[
D_a(s)=a^sZ(2s)+a^{1-s}Z(2s-1),\quad
D_a(\rho/2)=a^{1-\rho/2}Z(2-\rho)\ne0\quad(\forall a>0)
\]
で棄却した。別の閉部分空間上の自己共役cut-offでは全ζ零点が境界関数のzeroから外れる。
無限cut-offのdominant normalizationも両開half-stripでzero-freeな別極限になる。
片方の項を引き去る操作はspectral realityを保存しない。

詳細・証明・出典: [Track C](notes/phase2_scattering_generator.md)。

## 2. Candidate B — full prime germからのinverse canonical generator

**Candidate generator:** \(m_\xi(z)=-\Xi'(z)/\Xi(z)\) をWeyl関数として逆構成する候補。

**Arithmetic input:** \(s=1/2-iz,\ \Im z>1/2\) の収束域で
\[
m_\xi(z)=i\left[\frac1{s-1}+\frac12\psi(1+s/2)-\frac12\log\pi
-\sum_{p,k\ge1}(\log p)p^{-ks}\right].
\]
全Euler/Gamma/pole項を保持し、一意な解析接続を取る。

**Boundary data:** exact meromorphic \(m_\xi\)。全零点は単純poleの留数として重複度を保持。
余分な有限poleはない。

**Evolution law:** 正Hamiltonianが存在すれば \(JY'=zHY\) とRiccati式。
算術germからHamiltonianの正性を導出したわけではない。

**Why 1/2 appears:** 完成関数の既知の対称中心を実spectral parameterへ移す座標。

**What forbids off-line states:** 全上半平面のHerglotz性なら禁止するが、
actual \(m_\xi\) のその性質はRHと厳密に同値。

**Known prior art:** Csordas–Escassutの複素Laguerre基準、de Branges逆定理
（Eckhardt–Kostenko–Teschlの一次論文中の定理・条件を照合）。

**RH-equivalent hidden assumption?:** YES。素数germと非空開集合で一致する正canonical
systemの存在と書いても、一意性によって同じ条件になる。

**Synthetic counterexample status:** 一般条件のquartet模型
\(F=((z-1)^2+1/16)((z+1)^2+1/16)\) では
\(\Im(-F'/F)(1+i/5)=-428313920/24221529<0\) を有理数計算で検証。
全算術を共有する反例ではない。

**Exact missing lemma:** 必要bandを含むHerglotz性を全素数データから独立に証明する評価。
無条件の \(\Im z>1/2\) の正性は古典的stripの外側にとどまる。

**Decision:** RH同値の再表現として停止。逆定理は入力の正性を供給しない。
scalar measureの原子質量と固有空間次元は別であり、重複度付きdeterminant対応を
自動的に主張しない。有限Euler修復は予備排除のみとし、新attemptに数えない。

詳細: [Track B](notes/phase2_inverse_generator.md)。

## 3. Candidate A — actual Newman generatorと算術時計

**Candidate generator:** \(Mf(u)=u^2f(u)\)、Fourier側は \(-\partial_z^2\)。
\(H_\tau(z)=\int e^{\tau u^2}\Phi(u)e^{izu}du,\ H_0=\Xi\)。

**Arithmetic input:** 標準Gaussianの全整数theta和によるactual \(\Phi\)。
\(\tau\ne0\) で同じEuler積が成立するとは仮定しない。

**Boundary data:** actual \(\Phi\) が初期値を固定する。さらに
\[
\lim_{u\to\infty}
\frac{\log(e^{au^2}\Phi(u))+\pi e^{2u}-(9/2)u-\log(4\pi^2)}{u^2}=a
\]
により標準算術のtail条件がこのorbitの時間原点 \(a=0\) を一意に固定。
これは非RH補題だが、零点実軸性を含まない。

**Evolution law:** \(\partial_\tau H_\tau=-\partial_z^2H_\tau\)。
正自己共役生成子だが正時間の指数は全L²上の有界flowではない。actual初期値は必要domainに入る。

**Why 1/2 appears:** ξの空間的中心。熱時間の0とは別の規格化。

**What forbids off-line states:** 正核は純虚零点を排除するが一般の非実quartetは排除しない。
既知の実零点保存は時間増加方向であり、既知時刻から0へ戻す評価は未達。

**Known prior art:** de Bruijn–Newman変形とRodgers–Taoの非負性定理。
原論文との換算は \(H_t^{RT}(z)=H_{t/4}(z/2)/8\)。

**RH-equivalent hidden assumption?:** 算術時計の0はNO。Newman閾値0を置くならYES。

**Synthetic counterexample status:** 同じheat equationと正偶測度からの
\(c+e^\tau\cos z\) は閾値 \(\log c\)。標準算術を共有する模型ではない。
actual kernelには、各複素compact上で
\[
\frac{\sqrt T H_{-T}(\sqrt Tz)}{\sqrt\pi\Phi(0)}
=e^{-z^2/4}\left[1+\frac{\Phi''(0)}{2\Phi(0)T}
\left(\frac12-\frac{z^2}4\right)\right]+O_R(T^{-2})
\]
を全実線Taylor剰余で証明した。一方、既知のNewman定数非負性によれば各負時間に
非実零点がある。**actual核で、零点のないGaussian境界と全負時間の非実零点が両立する。**
零点はcompactificationの可視範囲から無限遠へ逃げる。

**Exact missing lemma:** 標準算術初期値を用いた全高さ一様の逆向き評価。
局所Rouchéの時間幅は導けるが、全高さの幅を供給しない。

**Decision:** clockとcompactificationはKEEP。そこから閾値0を強制する推論は停止。
零点配置と初期値の係数を結ぶ新しい算術不等式が必要。

詳細: [Track A](notes/phase2_newman_generator.md)。

## 4. Candidate D — fixed Gaussianからactual lattice lift

**Candidate generator:** \(B=\partial_x+2\pi x,\ G=B^*B\ge0\)。
Gaussian \(g=e^{-\pi x^2}\) は規格化後に一意のground state。

**Arithmetic input:** \(Tg(x)=\sum_{n\ge1}g(nx)\)、全整数和と標準Mellin/Gamma。

**Boundary data:** \(\Theta(x)=x^{-1}\Theta(1/x)\) はexact Poisson fixed-point式。
ただし \(\Theta,Tg\) は選んだL²のベクトルではない。

**Evolution law:** \(e^{-\tau G}g=g\) だがTはflowをintertwineしない。
\[
Gg_n=2\pi(n^2-1)[1-2\pi(n^2+1)x^2]g_n.
\]
\(x\ge1,N\ge2\) では \(GT_Ng<0=T_NGg\)。actual dataでの厳密反例。

**Why 1/2 appears:** log半密度と反転規約。

**What forbids off-line states:** なし。positive固定点生成子はGaussianを固定するが、
算術的lift後の生成子の正性へそのまま移せない。

**Known prior art:** Riemannのtheta/Mellin構成とPoisson反転。非可換式は直接微分で検証。

**RH-equivalent hidden assumption?:** Gaussian構成はNO。全zeroの自己共役mode同定は未証明。

**Synthetic counterexample status:** Gamma変更模型を使わずactual \(g,g_n\) で候補を反証。

**Exact missing lemma:** 今回の \(GT=TG\) は未証明ではなくFALSE。
別生成子なら残差と端点を保つexact mapが新たに必要。

**Decision:** 初期screenで停止。旧直和発散やmodified Gamma反例を新しく数えない。
4番目のmajor attemptとして継続しない。

詳細: [Track D](notes/phase2_modular_generator.md)。

## 5. t=0の10通りの解釈

|解釈|actual Newman familyでの判定|新しい禁止機構|
|---|---|---|
|ordinary initial condition|全時間でentireな軌道の、算術が指定する正則な初期値|なし|
|terminal condition|時間を反転すればそう呼べるが終端条件は増えない|なし|
|fixed point|\(\partial_\tau H_\tau(0)=\int u^2e^{\tau u^2}\Phi>0\)、固定でない|なし|
|phase transition|実零点性の転移はNewman閾値。それが0ならRH同値|未証明|
|boundary|actual軌道は0を跨いでentire。実零点coneの境界なら同値義務|なし|
|separatrix|同じ閾値を指すなら新しい力学的不変集合は未構成|なし|
|compactified infinity|τ=1/tは座標特異性のみ。Gaussian境界では零点が逃げる|逆伝播不可|
|renormalization fixed point|negative-time rescalingの極限はGaussianでactual H0ではない|なし|
|self-dual point|算術は0を指定するが反転のfixed pointと実零点性は別|なし|
|coordinate singularity|Hは時間・空間でentire。逆数座標の特異性は元の解にない|なし|

正規化密度でも \(m_2'(\tau)=\operatorname{Var}(u^2)>0\) なので固定状態ではない。
conformal/projective/Cayley/log等の正則な一対一座標変換は情報を同型に移すだけ。
別の正Hilbert構造やboundary conditionが現れれば対象になるが今回は供給されていない。
全ての可能なrenormalizationを不可能と証明した表ではない。

## 6. 情報圧縮とprojectionの監査

関数を変形できる自由度と、一意な関数の零点位置が未証明であることを分ける。

|入力|制約するもの|それだけで残る問題|
|---|---|---|
|functional equation / real structure|反射・共役pair、quartet|pairを線上へ潰さない|
|全actual Euler積|収束半平面の関数germを一意に固定|strip内の非消滅評価は別|
|analytic continuation|germの連結領域への延長は一意|一意性はzero-location theoremではない|
|growth / order 1|Hadamard積の型・指数因子|Eulerを外せばquartet追加模型は残る|
|所定Gamma/pole terms|trivial cancellation・archimedean completion|nontrivial零点の位置は未確定|
|normalization|非零定数等を固定|定数固定は零点を動かさない|

全条件をactualな値のまま課せば関数のmoduliは一点であり、自由な線外変形はない。
その一点が線外零点を持たないという結論は依然RHである。
一意性を「線外stateが存在しない証明」と読まない。
一本の境界関数にも無限個の精密な値がある。有限情報への圧縮や、
prime側とzero側の自由度の有限次元計測をしたわけではない。

Cのcusp射影 \(Pf(y)=\int_0^1f(x+iy)dx\) はcuspidal modeを消すが、
全算術的散乱極はPの像に非零係数で残る。仮想的off-line modeだけが
\(\ker P\)に入る機構ではない。cut-off別空間への移行は全ζ零点の回収を失う。

## 7. 検証scope

- A: ROOTは微分・domain・算術tail・Taylor剰余・時間換算を再読検算。
  DESTROYERはGaussian展開係数と任意閾値模型を独立検算。
- B: BUILDERがB1–B7、正常収束、Herglotz同値、resolvent、multiplicityを独立監査。
- C: LITERATUREとDESTROYERがC1–C7を独立監査。閉部分空間と最高Laurent係数の修正を反映。
- D: ROOTがGaussian微分、符号、domain、Mellin規約を再導出。
- 数値: phase2-scattering-checks.json（70桁）、phase2-boundary-falsification.json（55桁）。
  特殊関数・積分は非認証diagnostic。Bの負値は有理数演算でexact。全称定理は解析証明による。
- 新しいLean宣言は追加していない。既存8宣言を今回の解析・散乱理論全体の
  形式検証とは呼ばない。外部専門家による査読を受けたという主張もない。

## 8. 3 major attempts後のstrategy review

判定順はC → B → A。Dは初期screen。Cのcut-off修復を別attemptへ水増ししない。
3候補とも、自己共役性／境界正性／時間原点とactual全零点の制約の間で止まった。

1. Cは全Euler/Gammaを含むexact generatorを持つがzero dataはresonance。
   実スペクトルへ移す修復はactual dataで完全対応を失う。
2. Bは全零点を保持するが、正生成子へ変える入力条件がRH同値。
3. Aは生成子・標準初期値を独立に固定できるが、算術時計と実零点閾値の一致は未証明。
   compactified境界からの逆伝播はactual familyでも失敗する。

**終了判断:** Generator / Boundaryという名前だけを理由に探索を延長しない。
今回の具体的framingからの自動的な零点排除候補は終了し、strategy reviewを完了した。
補助恒等式は保存するが、主証明グラフへの合流0、追加採用仮定0。
あらゆる生成子法の不可能性を証明したわけではない。
再採用には、今回のmissing linkを独立に変える算術的等式・評価・domain定理が必要。
別の呼称・compactification・正Gramだけでは採用しない。
今回の3候補にその追加内容はなく、機械的な4番目や有限窓拡大は開始しない。
長期のRH目標は未達。routeの終了をRHの完成と取り違えない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/notes/phase2_inverse_generator.md`](notes/phase2_inverse_generator.md)
- [`research/notes/phase2_modular_generator.md`](notes/phase2_modular_generator.md)
- [`research/notes/phase2_newman_generator.md`](notes/phase2_newman_generator.md)
- [`research/notes/phase2_scattering_generator.md`](notes/phase2_scattering_generator.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `research/phase2_charter.md` — SOURCE REFERENCE NOT INCLUDED
