**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/one_prime_return_theorem.md` · Original SHA-256: `612c31f7e219a065708a6b64140d74ca7067e4d52540ee59cb7be56e8fe69f3d`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# RH Focus Track — One-Prime Return Theorem

2026-09-29開始、2026-09-30完了（JST）。RH OPEN。素数は **p=2** のみに固定。Phase I〜IV、continuous-scale-flow、既存主グラフ・state・Lean成果は変更しない。内部資料は `research/one_prime/`、独立stateは `one_prime_return_state.json`。

## 0. 結果

**Level 1および限定的なLevel 2を確認した。Level 3〜5は未達。**

両方向subexponential-return lemmaを証明し、そのスカラー部分をLeanで検証した。実際の算術商の標準seminormから、全零点の評価を有界・非零に保つBanach完備化X₁を構成した。この構成は既知の算術空間からの直接の帰結であり、新規性は主張しない。

しかしT₂の得られた上界はまだ指数的である。補間・quotient-first・局所Haarからのtransfer・similarity/dilationを具体的に検査しても、この算術商上の両方向subexponential boundは得られなかった。3つの主要構成を終え、同じ未解決estimateの言い換えを続けない。主証明グラフへのmergeはない。

## 1. Attack 1 — 成長の十分条件をsubexponentialまで弱める

Xを複素normed space、Tをbounded invertible operator、ℓ≠0をbounded functional、ℓT=λℓとする。Tがontoなのでλ≠0。dual normから全m≥0について

\[
|\lambda|^{m}\le\|T^m\|,\qquad
|\lambda|^{-m}\le\|T^{-m}\|.
\]

\[
g_\pm=\limsup_{m\to\infty}\frac{\log\|T^{\pm m}\|}{m}
\quad\Longrightarrow\quad
-g_-\le\log|\lambda|\le g_+ .                              \tag{1}
\]

λ=2^(ρ−1/2)を代入すれば

\[
\left|\Re\rho-\tfrac12\right|
\le\frac{\max(g_+,g_-)}{\log2}.                            \tag{2}
\]

両rateが0ならRHの実部条件を得る。polynomial power growthで十分であり、unitary similarityは不要。

locally convex空間ではoperator normを仮定せず、各continuous seminorm qに対して

\[
q(T^nx)\le C_{q,\epsilon}e^{\epsilon|n|}r_{q,\epsilon}(x)
\quad(\epsilon>0,n\in\mathbb Z)                             \tag{3}
\]

とする。入力seminorm rはq,εに依存してよいがnには依存させない。さらに弱く、各固定x,qのorbitが両方向subexponentialでも足りる。q=|ℓ|、ℓ(x)≠0のxを取れば指数を直接比較できる。FréchetではBaireの定理によりpointwise版から指数重み付きequicontinuity版が従う。

単に各Tⁿが連続であること、nuclearity、各bounded setを個別にbounded setへ送ることでは(3)にならない。固定seminormを左右で同じにする条件とも区別した。[Wegner, §2](https://arxiv.org/pdf/1408.5037v1)との照合はこの量化の確認に使った。

詳しい証明は `one_prime/notes/abstract_return.md`。Leanは `one_prime/formal/ReturnLemma.lean`、成功出力は `verification.txt`。4宣言にsorry・追加公理はない。**算術的なgrowth estimateやRHそのものの形式化ではない。**

## 2. Attack 2 — actual arithmetic spaceを固定する

[CCM math/0703392v1](https://arxiv.org/pdf/math/0703392v1)のEq.(4.20)、Def.4.10/4.14、Thm.4.16、および[Meyer math/0311468v1](https://arxiv.org/pdf/math/0311468v1)の§5を指定版で確認した。一般cyclic/bornological対象と、Qのcompact-unit invariant scalar sectorを区別する。

半密度座標g(t)=e^(t/2)h(e^t)におけるtest spaceを

\[
E=\{g\in C^\infty(\mathbb R):p_N(g)<\infty\text{ for all }N\ge1\},
\quad
p_N(g)=\max_{0\le j\le N}\sup_t
 e^{N|t|}(1+|t|)^N|g^{(j)}(t)|                              \tag{4}
\]

とする。これは既存の全指数重み付きSchwartz topologyを表すseminorm系で、零点を使って設計したweightではない。

算術relations Vはadèle上のSchwartz関数ηでη(0)=∫η=0を満たすもののsummation Σ_(a∈Q×)η(ax)をcompact-unit平均し、半密度座標へ移したrange。W=closure_E Vとし

\[
\mathcal Q=E/W,\qquad q_N([g])=\inf_{w\in W}p_N(g+w).       \tag{5}
\]

この順序でtest space→arithmetic relations→quotient→topology→completionを固定した。QはHausdorff nuclear Fréchet。Meyerとの限定的なclosed-range同定はノートに記したが、以下の構成はWというclosureを明示したままでよい。

finite places、実place、Poissonのpole-free条件を含むactual arithmetic rangeを用いる。別のEuler factorsやΓ因子、有限素数モデルに置換しない。既知の全零点traceは核型空間上のintegrated operatorについての定理であり、T₂そのもののHilbert traceとはしない。

## 3. Attack 3a — 全零点を保持する具体的Banach完備化

ρを任意の非自明零点、δρ=Reρ−1/2とする。既知のstrip inclusionから|δρ|<1/2。

\[
\ell_\rho([g])=\int_{\mathbb R}g(t)e^{(\rho-1/2)t}\,dt.
\]

Tate/Mellinの算術因子によりℓρはVを消し、連続性によりWも消す。直接積分で

\[
|\ell_\rho([g])|
\le\frac{2}{1-|\delta_\rho|}q_1([g])
\le4q_1([g]).                                               \tag{6}
\]

従って

\[
X_1=\overline{\mathcal Q/\ker q_1}^{\,q_1}                  \tag{7}
\]

は全零点の非零有界functionalを保持するBanach空間である。各ℓρはcompactly-supported tests上で非零で、(6)によりkernelで消されず、完備化へ延長後も非零。

位数mρの零点についてj<mρのMellin jetsも

\[
|\ell_{\rho,j}([g])|\le2^{j+2}j!\,q_1([g])                \tag{8}
\]

で保持される。有限jet familyの独立性も維持される。これが限定Level 2の内容である。標準seminormを一つ選ぶことは非一意だが、零点配置はその定義に入らない。

ただしQ→X₁の全面的単射性、元の全商位相との同値性、余分なspectrumがないことは未証明であり、成功条件に必要ない段階で仮定しない。

T₂g(t)=g(t−log2)、L=log2とすると、Wの両方向不変性から

\[
q_N(T_2^nx)\le2^{N|n|}(1+|n|L)^N q_N(x),                  \tag{9}
\]
\[
\|T_2^n\|_{X_1}\le2^{|n|}(1+|n|\log2).                   \tag{10}
\]

T₂、T₂⁻¹はboundedに延長され、両者は互いに逆。(10)は上界であり、actual商の最良normが指数的だと証明したわけではない。

零点評価からの主計算式は

\[
2^{n\delta_\rho}|\ell_\rho(x)|
=|\ell_\rho(T_2^nx)|\le4q_1(T_2^nx).                       \tag{11}
\]

全ℓρを既にq₁が支配するため、必要なmissing estimateは全seminormの同時制御より弱くてよい：

\[
\boxed{\forall\epsilon>0\ \exists M\ge1,C_\epsilon<\infty:
q_1(T_2^nx)\le C_\epsilon2^{\epsilon|n|}q_M(x)
\quad(\forall n\in\mathbb Z,\ x\in\mathcal Q).}             \tag{12}
\]

各ρについてℓρ(x)≠0のxを固定し、正負nとε→0を使えばδρ=0となる。C、Mはnに依存してはならない。Banach X₁のoperator-norm boundは(12)より強いので、不要にそこへ限定しない。

Meyer Prop.5.9の既知のnuclear integrated-operator estimateも照合した。中心化後のstrip幅は約1/2で、smoothingを外したT₂ⁿのtype 0 estimateではない。conductor、support移動、Schwartz seminormの通常評価は指数係数を残す。新しい算術的相殺により(12)を示す定理は得られなかった。

## 4. Attack 3b — quotient-first、補間、弱い位相の破壊試験

同じseminorm Nで商を先に取った場合のHausdorff完備化は

\[
\overline{(S/R)/\ker q_N}\simeq X_N/\overline{R}^{X_N}       \tag{13}
\]

に等長である。またℓ(R)=0なら、|ℓ|≤CNと|ℓ|≤Cq_Nは同値で最良定数も同じ。従って順序変更だけではdense collapseを修復できず、Nで失われた評価を復活できない。算術rangeで最適化した後にreturn normが小さくなる可能性は残るが、それには新しいestimateが必要である。

診断用H_a=L²(e^(2a|t|)dt)では

\[
[H_0,H_k]_\theta=H_{\theta k},\quad
\|T_2^n\|_{H_a}=2^{a|n|},\quad
\ell_\rho\in H_a'\iff a>|\delta_\rho|\ (a>0).              \tag{14}
\]

real (θ,2) interpolationも同じ重みを等価normで与える。endpoint a=0では、単点Fourier評価すら有界でない。有限個のscaling derivativesは指数率と閾値を変えない。polynomial/GRS weightsはsubexponential returnを与えるが、線外のFourier–Laplace評価を連続双対から外す。

Hardy半平面では逆shiftがなく、両側stripでは指数重みが戻る。固定Paley–Wiener型ではsupportがreturnで動く。別々のnに別の位相を選ぶ方法は同じ作用素のgrowth estimateではない。これらをactual全零点保持の証明としない。

追加の設計上の罠：q_ε(x)=sup_n e^(−ε|n|)q₁(T₂ⁿx)と定義しても、その値が有限で元の算術位相に連続であることがまさに未証明。orbitの絶対凸包から不変seminormを作る場合も、|λ|≠1の指標はそこで有界になれない。設計による指標の排除を算術的な不在証明としない。

詳細は `one_prime/notes/topology_constructions.md`。一般の全自然位相が不可能という定理は主張しない。

## 5. Attack 4 — local Frobeniusからのtransferを最小化する

J:H_local→X、JU=T₂J、Uがunitaryで、全ρについてℓρJが非零boundedなら

    ||ℓρJ||=||ℓρJU||=|2^(ρ−1/2)| ||ℓρJ||

からRHの実部条件を得る。Jの全射性は不要。連続Jのdense rangeは各ℓρJ≠0の十分条件だが、最小条件は各指標がrangeを消さないことである。この部分は新metricより弱い。

しかしactual local profinite Haar return U₂の固有値はroots of unityである。boundedな非零ℓρJをこのsourceから引き戻すと、modulus 1だけでなく

\[
\frac{\Im\rho\log2}{2\pi}\in\mathbb Q                     \tag{15}
\]

も要求される。これはRHだけから出るとは確認されていない。実際の零点のこのrationalityを肯定も否定もしていない。unitary operatorのspectrumの閉包と、bounded dual eigenfunctionalが要求するpoint spectrumを区別した。

dense bounded intertwinerだけからglobal normの一様有界性が出るという主張は、pure-point torsion sourceを持つ2×2 block直和で反証できる。その例のglobal power growthは線形であり、指標別の正しいtransfer補題とは矛盾しない。逆方向のinjective mapだけでは指数成長さえ防げず、weighted bilateral shiftが反例となる。

必要なactual arithmetic Jまたは指標別bounded pullbackを構成できなかった。局所の正性やFrobeniusという名称でこの不足を埋めない。

## 6. Attack 5 — similarity、dilation、product formula

Hilbert上で二側uniform power boundがあればunitaryにsimilarになることは[Sz.-Nagy 1947, Thm I](https://acta.bibl.u-szeged.hu/38563/1/math_011_fasc_003.pdf)の既知定理。invariant meanによる証明も再構成した。この定理は既にあるuniform boundを使い、算術的boundを新しく与えない。Banachでは等価な不変normを得るが、それをHilbert内積としない。

subexponential growthはこのsimilarityより弱い。Jordan block I+NはTⁿ=I+nNで十分条件を満たすがunitaryとsimilarではない。全jetを残してuniform boundを要求するとmultiple zerosも排除する余分な義務になる。

unitary dilationは正powersとadjoint powersを実現するもので、inverse powersを制御しない。scalar contraction rI, 0<r<1に対するPoisson dilationが明示反例。polynomially bounded operatorという用語もpolynomial power growthと区別した。

product formulaの伸長・収縮の積1から二側norm boundは出ない。diag(c,c⁻¹)はdeterminantと不定pairingを保存しながらc^|n|の成長を持つ。各local termの非負性やrigidityをactual quotientへ追加する独立定理は得られなかった。

一次資料の読取範囲と反例の全式は `one_prime/notes/transference_similarity.md`。Dayの原典は書誌確認に限定し、本文まで読んだとは記録していない。

## 7. Strategy review

主要構成は3つに束ねて評価した。

1. 既存算術商・標準q₁完備化：全零点保持は成功。二側subexponential estimateは未達。
2. quotient-firstと自然な解析位相の補間：保持と成長のtradeoffを改善できず、一般的修復案を反証。
3. 一素数local transferとsimilarity/dilation：最弱条件は得たが算術map/boundが未構成。

本巡の主経路では、(12)に必要な算術的representativeの相殺評価が未証明のまま残った。別の十分経路である全指標を保持するarithmetic Jも未構成である。Jの存在と(12)の同値性は主張しない。3 major constructionsでいずれも独立な算術的成長制御に到達しなかったため終了し、未証明のgrowthを別名にする第4構成は行わない。p=3は追加しなかった。既存C0群では一素数のsubexponential制御から全実時間の同種制御が従うため、二素数化だけで新しい算術入力が得られる見込みは今回の結果から出ない。

「任意のzero-retaining topologyは無条件に指数成長する」とは証明していない。証明できたのは、**もし線外characterが存在するなら、それを連続に保持するspaceの該当orbitには指数成長が必要**という条件付き下界である。これはRHの反証ではない。

直接のWeil positivityや全零点のmodulus 1を仮定する案はRH同値として棄却した。一方、(12)やX₁のoperator-norm版がRHから逆に従うことは未証明なので、全構成を無根拠にRH同値とも断定しない。nonnormality、無限jet block、位相の一様性が逆向きの別義務になる。

## 8. 保存・検証

必須の8種のDestroyer testの対応と候補比較は `one_prime_topology_matrix.md`。
指定補題の数学的独立監査は `../proofs/audits/one_prime_return_adversarial.md`、stateは `one_prime_return_state.json`。全関連分野・全数値実験を独立に再実行したという意味ではなく、監査ファイルに範囲を明示した。
Lean scalar kernel 4宣言が通過。数値はsynthetic modelの反証補助で、`one_prime/return_checks.json`に保存した。actual ζの有限窓数値拡張は実施していない。

再開に必要なのは、(12)を既知の算術inputから導く独立な見積もり、または全零点指標を非零boundedに引き戻す算術的J₂である。位相の名称・補間parameter・similarity theoremを追加することは、この不足の代替にならない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/one_prime_return_adversarial.md`](../../audits/proofs/audits/one_prime_return_adversarial.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `formal/ReturnLemma.lean` — SOURCE REFERENCE NOT INCLUDED
- `research/one_prime` — SOURCE REFERENCE NOT INCLUDED
