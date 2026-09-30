**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/continuous_scale_flow_frobenius.md` · Original SHA-256: `4b78d6047b2624496d14d79d5ef3a355b5a6f969c6aa96869de4a5b35220767e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Continuous Scale Flow / Frobenius Section — 独立研究ログ

2026-09-29。RH OPEN。Phase III / IVとは独立。既存state・主グラフへの書込み、未証明metricの借用、自動mergeは行わない。本巡は具体的な3候補を検査して終了する。既知のmonodromy定理を新発見としない。

## 結論と到達範囲

素数周期軌道のFrobenius mapping torusは正確に存在する。全零点を保持する別の算術的表現では、正規化した双対指標の成長率が厳密に Re(rho)−1/2 となる。しかし、局所FrobeniusのHaar正計量と、この全零点表現を結ぶ忠実な正計量は得られなかった。

Level 1は既知結果の整理として完了。Level 2–3は **spectral-character growth** の意味で厳密化した。滑らかな横断接束のLyapunov指数を構成・同定したとの意味では未達。新規のno-growth機構を要するLevel 4、およびRHを閉じるLevel 5は未達。新しいRH証明、RH反例、新規性の主張はいずれもない。

さらにactual adelic transverse actionのp-adic normal modelには指数+1がある。したがって「算術flowのあらゆる横断成長がゼロ」というliteralな候補は反証される。これは零点指標の指数に関する反例ではない。以下§7.1で両者を分ける。

主要ノート：`scale_flow/notes/frobenius_mapping_torus.md`、`spectral_growth.md`、`program_comparison.md`。版・定理・取得範囲は各ノートに固定した。

## 1. 既知のFrobeniusを、向きと空間まで確定する

Y=Q×\A_Q、X=Y/Zhat×、π:Y→X と置く。素数pについて

\[
C_p=\mathbb R_+^\times/p^{\mathbb Z},\quad L_p=\log p,\quad
H_p=\prod_{q\ne p}\mathbb Z_q^\times,
\]
\[
M_p=\pi^{-1}(C_p)\simeq
(H_p\times\mathbb R)/((h,u)\sim(ph,u+L_p)).                 \tag{1}
\]

これは[Connes–Consani 2024, Thm 1.1](https://arxiv.org/pdf/2401.08401v1)、[2025, Prop 3.4](https://arxiv.org/html/2501.06560v1#S3.SS1)の既知の構成である。pによる乗法は、pで不分岐な最大abelian拡大上の arithmetic Galois Frobenius に対応する。

正のlog-scale flow φ_v[h,u]=[h,u+v] を取ると

\[
\varphi_{L_p}[h,0]=[p^{-1}h,0].                              \tag{2}
\]

原著のdeck monodromyはp、選んだ正時間のreturnはp⁻¹。逆時間ならreturnもpとなる。この規約差は誤りでも新現象でもない。

H_p×{0}はtopological transversalであり、滑らかな実Poincaré断面・normal derivativeではない。full liftの軌道はpの無限位数のため閉じない。有限abelian quotientではFrobeniusの位数f_pに応じて長さf_p log pの閉軌道になる。baseのC_p、full lift、有限coverを区別する。

このGalois作用を、有限体曲線のpolarized H¹に作用するweight-one Frobeniusと同じものにしてはならない。有限体では同じ幾何学的表現にπ†π=qが成立することが必要である。局所compact群のtranslationだけにはそのweight-one入力がない。

## 2. 実際に局所正metricを作り、スペクトルを計算する

Haar確率測度 dh と du/L_p は(1)へ降りる。L²(M_p)上の Koopman K_vF=F∘φ_v は強連続unitary群となる。このmetricは算術的compact fiberからRHを仮定せず構成できる。

ここから先は(1)の直接計算であり、既知論文が全ζ零点を同定したという主張ではない。連続character χ:H_p→T と

\[
F_{\chi,n}(h,u)=\chi(h)e^{i\omega_{\chi,n}u},\qquad
\omega_{\chi,n}=\frac{2\pi n-\arg\chi(p)}{L_p}
\]

を取ると、降下条件は

\[
\chi(p)e^{i\omega L_p}=1.                                   \tag{3}
\]

χは有限像のunitary characterなのでωは実数。χ-sectorごとのquasiperiodic Fourier展開により、これらは局所Haar空間の完全な直交基底を与える。

**即時のfidelity反証。** H_pの双対は無限である。arg χ(p)∈(−π,π]、n=0を取るだけで、|ω|≤π/L_pの有限帯に無限個の直交modeが入る。したがってこの全L²(M_p)のgeneratorはcompact resolventを持たず、有限高さに有限個しかないζ零点の離散divisorと重複度までそのまま一致しない。trivial characterには定数modeもある。

これは局所Haar空間の無修正同定を否定する。未知のcohomological quotientや別の算術的比較を全て否定するものではない。modeを恣意的に射影して取り除く修復は採用しない。すでにunitaryなK_vにe^(−v/2)を掛けると、ノルムはe^(−v/2)倍となる。weight 0の局所表現へweight 1の規格化を挿入しても純性は得られない。

## 3. prime powersとcompressed historyのexactな範囲

Re s>1で絶対・局所一様収束するEuler積から

\[
\log\zeta(s)=\sum_p\sum_{k\ge1}\frac{e^{-skL_p}}k,\qquad
-\frac{\zeta'}{\zeta}(s)=\sum_{p,k\ge1}L_p e^{-skL_p}.        \tag{4}
\]

対数は右方で0へ近づく枝。k回の巡回の長さはk log p、微分後の重みはlog pである。prime-power event distributionはΣ_(p,k)log p δ_(k log p)。critical stripでこの素数級数が絶対収束するとはしない。

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

について必要な全項は

\[
-\frac{\xi'}{\xi}(s)=\sum_{p,k}(\log p)p^{-ks}
+\tfrac12\log\pi-\tfrac12\psi(s/2)-\frac1s-\frac1{s-1}.       \tag{5}
\]

Γ・infinity・0,1のpole処理をprime circlesのlogだけから得たとはしない。長さlog pの円を列べるだけでも(4)は書けるため、compressed historyという呼び方自体はgeneratorのtrace/determinant定理も純性も追加しない。

## 4. 全零点表現ではgrowthを厳密に同定できる

別の既知対象として、CCMの急減test空間と算術的restriction rangeの商を用いる。これはnuclear/locally convexな対象であり、(1)の局所Haar Hilbert空間ではない。記号・domain・閉包は`notes/spectral_growth.md` SG1に記録した。全零点とmultiplicity付きtraceは[CCM07, Thm 4.16](https://arxiv.org/pdf/math/0703392v1)等の算術的定理を使う。

\[
\widehat f(s)=\int_0^\infty f(x)x^s\frac{dx}{x},\quad
W_uf(x)=e^{-u/2}f(e^{-u}x),\quad
\ell_\rho(f)=\widehat f(\rho).
\]

各零点の非零連続双対指標について

\[
\ell_\rho\circ W_u=e^{(\rho-1/2)u}\ell_\rho,\qquad
\lim_{u\to+\infty}\frac1u\log
\frac{\|W'_u\ell_\rho\|}{\|\ell_\rho\|}=\Re\rho-\tfrac12.     \tag{6}
\]

normはこの1次元指標空間の任意のnorm。幾何学的接束のLyapunov指数、Hilbert固有vector、解析接続のresonanceと混同しない。Mellin jetsには多項式uの因子が付くが指数は同じ。jetの商への降下・独立性は別途算術rangeの消失次数を必要とする。

## 5. Phase IVのmetricが本当に満たすべき条件

算術test quotient Eの上で、零点を入力にせずqを構成し、次を同じ空間上で示す必要がある。

1. qは半正定値でq(W_uv,W_uw)=q(v,w)。
2. q(W_uv−v)→0 as u→0。radical quotientのHilbert完備化で強連続群を得る。
3. **全て**の零点について非零ℓ_ρが残り、|ℓ_ρ(v)|≤C_ρ sqrt(q(v))。

条件3はradicalで零点を消さず、そのHilbert空間の有界双対に保持する条件である。unitarityによって

\[
\|\ell_\rho\|=\|\ell_\rho\circ W_u\|
=e^{(\Re\rho-1/2)u}\|\ell_\rho\|
\]

となり、(6)のgrowthは0。この条件付き補題は初等的に証明・監査できたが、その算術的前提は構成できなかった。

強連続群のgenerator GはStoneの定理によりskew-adjoint。Θ=G+1/2なら同じdomainでΘ*=1−Θ。形式的integration by partsだけでは群、core、closureを代替できない。RHの実部結論だけには各零点の非零bounded characterの保持で足りる。完全なspectral determinantを要求するなら、no extra modes、multiplicity、全traceまでさらに確認する。非自明Jordan chainの忠実なunitary化は不可能であり、これをRHだけから保証してはならない。

**completionの障害。** 補助空間H_k=L²(R,e^(2k|t|)dt)では、α=Reρ−1/2に対して

\[
\|W_u\|=e^{k|u|},\qquad
\|\ell_\rho\|^2=\frac{k}{k^2-\alpha^2}\quad(k>|\alpha|).
\]

k≤|α|では評価が非有界。k=0ではα=0の単一点Fourier評価すら裸のL²に有界でない。mode保持とunitarityを別のnormで証明して足し合わせることはできない。CCMの指定ambient L²では算術rangeが稠密で商が消える。この既知障害およびPhase IVの可閉形式障害を参照するが、Phase IVのファイルは変更しない。

## 6. 一周期の制御を全時間へ移す正確な補題

同じHilbert空間上のC0群W_uで、あるL>0についてW_Lがunitaryなら、u=nL+rによって全時間で一様有界となる。逆時間も有界なので全非零vectorの指数成長は0。また

\[
q_L(v,w)=\frac1L\int_0^L\langle W_tv,W_tw\rangle\,dt          \tag{7}
\]

は元のnormと等価で、全時間に不変な正内積である。証明はintegrandのL-periodicityと局所有界性のみ。元のnorm自体で全時間unitaryとは限らない。

これはstroboscopic controlの十分条件を具体化するが、素数ごとに異なるH_p上のunitary returnを代入できない。必要なのは全零点を保持する共通H上のreturnである。同じ元のnormでW_log2とW_log3がunitaryなら、時間の稠密部分群から全時間unitaryになるが、この算術的前提も未取得。

周期cocycleのmonodromy Mに正G0でM*G0M=G0があれば、transportにより周期正metricを作れる。しかし任意の時間依存metricは非一様に退化し得る。無限次元ではbounded invertibilityとuniform coercivityを省略できない。新しい算術的return制御を得ていないため、(7)をRHへの新規bridgeとは数えない。

## 7. 反証、duality、保存則

X(u)=diag(e^(au),e^(−au)), a>0 と置けば、det=1、symplectic、非退化な不定pairingの保存、R X(u) R=X(−u)（Rはswap）を同時に満たす。それでもgrowthは±a。各素数circle上にこのcocycleを載せれば、周期log pと反復p^kも保てる。base Euler logはactual ζと一致しても、cocycleのtrace weight p^(ka)+p^(−ka)はactual ζと一致しない。この違いを隠してRH反例とはしない。

actual Weil形式も正規化scalingに対する保存則を持つ。しかしoff-line pairの指数は不定pairingでも相殺できる。その全面的正性は既知RH同値条件であり、保存則からの帰結ではない。

inversion u↔−u は両端を交換するexact involutionとして検査した。0と∞を同じ点とはせず、symmetryで±aが対になることとa=0を区別した。product formulaもscalarの積を1にできるだけでは上の反例を除外しない。

さらにcompact hyperbolic surfaceのgeodesic flowでは、Liouville測度のKoopman群はunitaryである一方、Jacobi方程式J''−J=0により接束の指数は±1。**関数空間の正不変内積は接束の横断伸長を禁止しない。** 算術表現・接束・resonanceの比較が必要となる。

### 7.1. actual p-adic transverse actionは非零成長を持つ

[CC25 Introduction, PDF p.3](https://arxiv.org/pdf/2501.06560v1)は、素点vのtransverse space K_vとisotropy K_v×の作用からlocal trace kernelを説明している。従って「profinite fiberに実接束がない」から「算術的横断作用そのものがない」と結論してはならない。

actual adelic representativeのp成分をz∈Q_p、他の有限成分をh∈H_p、実成分をe^uと置く。算術normal modelは

\[
E_p=(\mathbb Q_p\times H_p\times\mathbb R)/
 ((z,h,u)\sim(pz,ph,u+\log p)).                              \tag{8}
\]

これはM_pをzero sectionとするp-adic line modelで、actual adèle class spaceへ連続単射を持つ。ただしその写像は **topological embeddingではない**。全他素点のunit条件がopenでないだけではこの結論は出ない。ノート§3のCRT構成により、HausdorffなE_p内の列がambient商Yではzero-sectionの点と非零normal点の両方へ収束することを確認した。従って(9)をambient商の連続距離として扱わない。singular quotientの位相を省略せず、算術normal model上の命題として使う。

正時間log pで実座標を元に戻すrational gauge p⁻¹を使うと、横断return cocycleは(z,h)↦(p⁻¹z,p⁻¹h)。従ってp-adic normで|p^(−k)z|_p=p^k|z|_p。さらに

\[
N([z,h,u])=e^u|z|_p                                         \tag{9}
\]

はdeck不変な連続fiber normで、φ_vによりN↦e^v Nとなる。時間をlog-scaleとするnormal valued exponentは **+1**。逆時間なら−1。compactなzero section上の連続同値fiber normでも指数は変わらない。この計算はarithmetic action groupoidのnormal modelについてexactであり、実smooth tangentの構成とは別である。

非零横断成長は算術的local termと両立する。Q_p上のunitary half-density dilation

\[
U_\lambda f(z)=|\lambda|_p^{-1/2} f(\lambda^{-1}z)
\]

のformal fixed-point kernel integralは、λ≠1について

\[
\frac{|\lambda|_p^{1/2}}{|1-\lambda|_p}=p^{-k/2},
\quad\lambda=p^{\pm k},\ k\ge1.                            \tag{10}
\]

primitive length log pと合わせるとcentered explicit formulaのprime-power係数になる。ただし(10)はlocal distributional fixed-point traceであり、Hilbert trace-classの証明でも正Weil形式でもない。Γ・pole項・全零点へのglobal比較はまだ別入力。局所Jacobianの補償とglobal purityを混同しない。

このSF1の追加反証により、探索すべき禁止機構は「幾何学的横断伸長を全て無くすこと」には置けない。実際の零点指標のαを制御することへ限定する必要がある。詳細と独立監査は`scale_flow/notes/padic_transverse_audit.md`。

## 8. 全candidateの指定カード

### SF1 — actual mapping torusのHaar metricをそのまま移植

```text
Continuous flow: phi_v[h,u]=[h,u+v] on M_p, the actual orbit lift
Prime periodic orbit: base C_p; full lift trajectories are not periodic
Orbit length: log p; finite abelian lift has f_p log p
Prime-power iterates: k log p; return p^{-k}, deck p^k
Frobenius relationship: arithmetic Galois Frobenius is deck monodromy; inverse for positive-time return
Normalized flow: local Haar Koopman is already unitary; no arithmetic weight-one normalization supplied
Candidate transverse exponent: local Haar character frequencies are real; actual p-adic normal model has valued exponent +1; smooth real tangent not claimed
Relation to Re(rho)-1/2: not identified
Invariant metric: Haar L2(M_p), independently positive
Arithmetic source of metric: compact profinite arithmetic fiber and Haar measure
Known prior art: CC2016 Lem5.1; CC2024 Thm1.1; CC2025 Prop3.4/Thm3.12
New content: direct local-mode audit; bounded-frequency infinite multiplicity blocks the unmodified full-space identification; no novelty claimed
RH-equivalent assumption?: local construction NO; faithful unitary transfer to all zero characters would imply RH but is absent
Counterexample status: full local L2 has infinitely many modes in a bounded frequency band; actual normal p-adic growth is +1, so literal geometric no-growth is false
Decision: KEEP established monodromy; KILL unmodified Haar-to-zero-space transfer
```

### SF2 — full arithmetic zero quotientと不変形式

```text
Continuous flow: W_u f(x)=exp(-u/2) f(exp(-u)x), on the arithmetic test quotient
Prime periodic orbit: actual scaling-site C_p is known, but not a Hilbert eigenmode identification
Orbit length: log p
Prime-power iterates: exact Euler/Mangoldt terms, with Gamma and poles separately retained
Frobenius relationship: local monodromy and this global zero representation are not identified by a positive comparison
Normalized flow: Mellin half-density normalization fixed in the representation
Candidate transverse exponent: continuous-dual spectral-character exponent
Relation to Re(rho)-1/2: exact on every nonzero zero character; not geometric Lyapunov equality
Invariant metric: an invariant Hermitian Weil form is known; independent positivity is absent
Arithmetic source of metric: actual explicit formula supplies the form, not its sign
Known prior art: CCM07 Def4.10/Thm4.16/Prop6.2-6.4; Meyer03 summable representation
New content: bounded-functional retention, radical, domain and multiplicity obligations made explicit; no new arithmetic metric
RH-equivalent assumption?: full positivity of the actual Weil form YES; not adopted
Counterexample status: ambient L2 loses the quotient; H_k retains evaluations but allows exponential growth
Decision: KEEP exact growth identity; KILL as a new no-growth route without another arithmetic metric
```

### SF3 — return control、duality、global conservationからのmetric

```text
Continuous flow: one common C0 group on a faithful zero-bearing Hilbert space is required
Prime periodic orbit: local C_p alone does not supply a return on that common space
Orbit length: one L>0 suffices for the conditional theorem; log p is the desired arithmetic choice
Prime-power iterates: W_{kL}=(W_L)^k on the SAME representation
Frobenius relationship: no arithmetic intertwiner from local Frobenius Haar modules has been constructed
Normalized flow: W_u; exponential factor must match the full-zero representation
Candidate transverse exponent: representation norm/character growth, with two-sided control
Relation to Re(rho)-1/2: follows from retained characters, not from periods alone
Invariant metric: average (7) if the same W_L is unitary; premise not proved arithmetically
Arithmetic source of metric: none beyond the insufficient local Haar/product-formula inputs
Known prior art: elementary C0-group averaging and periodic linear-cocycle metric transport; no novelty claim
New content: precise sufficient conditions and failure tests, no new arithmetic verification
RH-equivalent assumption?: sufficient package implies RH; converse for full topology/Jordan retention not established
Counterexample status: hyperbolic 2x2 preserves duality, symplectic form, determinant and prime periods with nonzero drift
Decision: KILL unless an independent common-space return/metric theorem is supplied
```

## 9. 必須8プログラムとの差分

Berry–Keating、Connes spectral realization、CC scaling Hamiltonian、scaling site/adèle class space、Deninger、dynamical zeta、Selberg、Gutzwillerを`scale_flow/notes/program_comparison.md`で個別比較した。self-adjoint ambient dilation、weighted almost-unitary quotient、nuclear full-zero trace、semilocal cutoff、local Haar suspension、geometric Hodge theory、anisotropic resonances、semiclassical traceを互換なものに扱わない。

Selberg/Gutzwillerには追加の反復stability重みがあり、prime側のlog pとそのまま一致しない。Selberg1956/Gutzwiller1971原著の今回未取得の本文を読了したとは記録しない。著者講義・関連一次式で照合できた範囲を明示した。

Li(x)による角度表示はPNT座標として初期終了。2π(π(x)−Li(x))と位相誤差を呼んでも、新たな誤差評価は出ない。

## 10. Strategy reviewと再開条件

3候補とも、同じ全零点空間への独立なpositive metricを与えなかった。既知のperiodic orbitを再説明するだけの第4候補は開始しない。有限窓拡大やarbitrary countertermへ戻らない。

本巡で残った最小の義務は、**算術入力から定義された共通表現の正metricと、全零点characterがその有界双対に非零で残る比較定理**である。stroboscopic版なら、その同じ表現の一周期unitarityが十分になる。ここではその前提を証明していない。単にこの未解決義務を新しい名前で呼ぶことを成果には数えない。

位相とmultiplicityを含むfull geometric bridgeがRHから逆に従うとは未証明。したがってプログラム全体を根拠なくRH同値と断定しない。直接のWeil positivityや全零点のα=0だけを再要求する候補はRH同値として棄却する。

原典照合、独立監査、exact行列反証、数値診断を分離して保存した。数値は認証ではなくRHの証拠にも使わない。旧Phase III・IVおよびcanonical state/graphは保存し、このトラックを主証明グラフへ合流しない。
