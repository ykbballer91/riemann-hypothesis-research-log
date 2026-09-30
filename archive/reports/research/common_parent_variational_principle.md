**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/common_parent_variational_principle.md` · Original SHA-256: `ddab318de9b3001d623b713c8459a6bf1e4c0bedcb0a1240e8db6b2a63f730e8`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Common parent variational principle / dual projections

2026-09-30。**RH OPEN。限定監査完了。既存研究・state・proof graphには統合しない。**

## 結論

**NO COMMON PARENT IDENTIFIED.**

指定されたBを、実際の有限Weil行列Aの目的関数に代入した。
小さい例ではほぼ最低点になる。一方、別の有限例ではRayleigh値が小さくても
ground gapがさらに小さく、energy excess / gapは大きい。
この結果は「BがAから遠い」ことの証明ではなく、
小energyだけからgroundへの接近を認証できないことを示す診断である。
適切な同時極限での \(\varepsilon/\Delta\to0\) は証明していない。

原典と式から、二つの重要な区別も固定した。

1. Bのseedは最も集中した単一prolate modeではない。
   0次・4次modeの積分零の組合せであり、通常のeven mean-zero concentration問題の
   stationary pointですらない。
2. 極限proxyには、Weil形式のradicalに入るという本当の算術的関係がある。
   しかしこれは既知であり、無限次元のradicalはunique groundを選ばない。

到達度は本ユーザー指定の **Level 1（辞書・明示的な比較式・反証まで）**。
共通parentの存在、無条件almost-minimizer評価、gap比の極限、G*、RHは未取得。
三系統を評価し、同型の第4候補へ移行しない。

## 1. 対象を固定する

\(\lambda>1,\ a=\log\lambda\) とし、Aの空間は
\[
 Y_\lambda=L^2([-a,a],dt),\qquad
 E_N=\operatorname{span}\{(2a)^{-1/2}e^{i\pi j(t+a)/a}:|j|\le N\}.
\]
区間外には0延長する。actual Weil形式をこの空間へ制限したHermitian行列
\(Q_{\lambda,N}\) に対して
\[
 e_0=\min_{\|v\|_2=1}Q_{\lambda,N}(v,v),\qquad Q_{\lambda,N}v_0=e_0v_0 .
\]
Gamma・pole-removal・全 \(p^k\le\lambda^2\) のprime項を含める。
有限Fourier次数Nはprime cutoffと別のparameter。
ESは全空間の最小固有値が単純かつgroundがevenという条件であり、
reflection可換性だけからは得られない。

Bのseedはadditive空間 \(L^2([-\lambda,\lambda],dx)\) にある。
\[
 C_\lambda=P_\lambda\mathcal F^{-1}P_\lambda\mathcal F P_\lambda,\quad
 J_{\rm leak}(h)=\|h\|_2^2-\langle h,C_\lambda h\rangle.
\]
単位normでleakageを最小化するのはprolate \(\psi_0\)。
指定proxyはそれとは異なり
\[
 h_\lambda\propto\psi_4-\frac{\int\psi_4}{\int\psi_0}\psi_0,\qquad
 k_\lambda(u)=\sqrt u\sum_{1\le m\le\lambda/u}h_\lambda(mu),
 \quad \lambda^{-1}\le u\le\lambda .
\]
有限区間外のseedは0。比較に使うのはlog座標 \(k_\lambda(e^t)\) の
既存Fourier射影
\[
 p=P_N k_\lambda,\qquad b=p/\|p\|_2
\]
である。新しい内積、任意のunitary identification、零点依存の補正は導入しない。
raw proxyのlog-evennessも仮定しない。

全objective、境界、規格化、原典対応は
[variational dictionary](common_variational_dictionary.md)、
[BのEuler式](common_parent/notes/B_variational_and_equations.md)に固定した。
[CCM §7](https://arxiv.org/html/2511.22755v1)のBを別のconcentration minimizerへ置換していない。

## 2. 最初の実験：BをAの採点へ代入

測定量は
\[
 R_B=b^*Qb,\quad \varepsilon=R_B-e_0,\quad
 \Delta=e_1-e_0,\quad \eta=\varepsilon/\Delta .
\]
Qはprime/pole/archimedean成分から組み立てた。
trialはprolateのLegendre Ritz近似から算術和・Fourier射影で作った。
seed次数、求積次数を増やして診断の変動を確認し、微小gapの例は
288-bit Arbによる行列組立てと75桁固有分解で再計算した。
trial係数自体は倍精度近似の丸め値であり、全prolate誤差のinterval certificateではない。
Arb行列もmidpointを渡すため、gapとscore自体についても区間認証とは主張しない。

| \(\lambda^2\) | \(N\) | \(R_B\) | \(\Delta\) | \(\eta\) | \(|\langle b,v_0\rangle|^2\) |
|---:|---:|---:|---:|---:|---:|
|2|4|\(1.95493\,10^{-3}\)|\(1.03506\,10^{-1}\)|0.00211972|0.99978990|
|3|4|\(3.07328\,10^{-7}\)|\(5.32075\,10^{-5}\)|0.0000328082|0.99999995|
|5|4|\(6.00467\,10^{-7}\)|\(1.58783\,10^{-8}\)|37.8112|0.99548421|
|5|8|\(5.60528\,10^{-13}\)|\(2.20320\,10^{-12}\)|0.252341|0.99988509|
|9|8|\(2.76804\,10^{-11}\)|\(8.69688\,10^{-18}\)|\(3.18280\,10^6\)|0.99470913|
|13|8|\(8.19928\,10^{-10}\)|\(3.90717\,10^{-20}\)|\(2.09852\,10^{10}\)|0.98487843|

大きい比は距離の下界ではない。例えば最後の行のoverlapは依然高い。
標準gap上界が弱いことと、実際に近くないことは違う。
また固定Nでの有限例から、\(\lambda,N\) の適切な同時極限を反証しない。
数値の詳細・再現方法・precision gateは
[Step31記録](common_parent/notes/rayleigh_calculation.md)、
[高精度診断JSON](../../../artifacts/research/common_parent/experiments/high_precision_results.json)に保存した。
ground gapがroundoff以下となった倍精度結果は結論に使わない。

## 3. Rayleigh法の正しい結論と追加のrate

単純groundと \(\Delta>0\) のもとで、固有vector展開により厳密に
\[
 \varepsilon
 =\sum_{j\ge1}(e_j-e_0)|\langle v_j,b\rangle|^2
 \ge\Delta\,\operatorname{dist}(b,\mathbb Cv_0)^2 .
\]
従って
\[
 \operatorname{dist}(b,\mathbb Cv_0)^2\le\eta,\qquad
 \min_{|\omega|=1}\|b-\omega v_0\|^2\le2\eta .
\]
一様正gapは不要。\(\varepsilon=o(\Delta)\) で十分である。
残差 \(r=(Q-R_B)b\) なら、別途 \(R_B<e_1\) が分かる場合に限り
\[
 \|(I-P_{v_0})b\|\le\|r\|/(e_1-R_B).
\]
残差0のexcited stateは反例なので、groundの識別を省略しない。
これらは標準的な補題であり、以前のLocal-to-Global監査にも現れた。
新しい算術的energy estimateとしては数えない。

さらに、ユーザーのLevel 3とLevel 4の間には窓依存の評価損失がある。
\(p=P_Nk_\lambda\)、\(cv_0=P_{v_0}p\) とおくと
\[
 d_{\lambda,N}:=\|p\|_2\sqrt{\eta}+\|(I-P_N)k_\lambda\|_2,\qquad
 \|cv_0-k_\lambda\|_2\le d_{\lambda,N}.
\]
全 \(0<r<1/2\) について
\[
 \sup_{|\Im z|\le r}|c\widehat v_0(z)-\widehat k_\lambda(z)|
 \le \sqrt{\frac{\lambda^{2r}-1}{r}}\ d_{\lambda,N}.
\tag{V*}
\]
従って、この右辺が0へ行くことがG*への明示的な十分評価。
既知 \(\widehat k_\lambda\to\mathscr X/4\) と、
\(z_*=i/4\) での非零極限を合わせれば値規格化も処理できる。
これは必要最小条件とは主張しない。
単なる \(\eta\to0\) は、増大support上の複素Fourier評価を自動では制御しない。

raw proxyは小さな内部・端点jumpを持ち得るため、
根拠のないperiodic \(H^1\) boundを使わなかった。
全変動 \(V_\lambda\) に対する安全なtail boundは
\[
 \|(I-P_N)k_\lambda\|_2\le\frac{\sqrt{\log\lambda}}{\pi\sqrt N}V_\lambda .
\]
(V*)に必要な全パラメータrateは未取得である。

## 4. 本当に共通しているもの：既知のWeil radical

Hermite極限seed
\[
 h(x)=\frac\pi2x^2(2\pi x^2-3)e^{-\pi x^2}
\]
の算術和 \(k(t)=e^{t/2}\sum_{n\ge1}h(ne^t)\) は両側でsuper-exponentialに減衰し、
\(\widehat k(z)=\mathscr X(z)/4\)。
全指数重み付き導関数が可積分なtest-space上でWeil明示公式を連続拡張すると
\[
 Q_W(k,g)=0\qquad\text{for every admissible }g .
\tag{Z}
\]
証明は明示公式の各零点評価が \(\widehat k\) を消すことによる。
ここでは零点の実部を仮定していない。
実際、Connes–Consaniは算術和の像がWeil形式のradicalに入ることを
既に明記している：
[Spectral triples and ζ-cycles, §3, pp.118–120](https://ems.press/content/serial-article-files/44477)。

(Z)は単なる見た目の類似より強い、本当の算術的接続である。
しかし「最低点へのほぼ到達」とは違う。
負の方向が存在すればzero-energy vectorはgroundではない。
非負ならzero-energy vectorは最小解だが、
\(k,k'',k^{(4)},\ldots\) もradicalに入り線形独立なので一意でない。
このtest-spaceの形式を、閉じた大域 \(L^2\) 正形式と無断に同一視しない。

滑らかなcompact cutoffによる \(k_a\to k\) から
\(Q(k_a,k_a)/\|k_a\|^2\to0\) は得られる。
これはactual prolate proxyのWeil energy/gap比を評価したものではない。
さらにcontinuum compact-core最小値
\[
 e_0(a)=\inf_{\|f\|=1,\ \operatorname{supp}f\subset[-a,a]}Q_W(f,f)
\]
は非増加なので、Weil criterionと合わせると
\[
 e_0(a)\to0\quad\Longleftrightarrow\quad\mathrm{RH}.
\]
「ground値も0へ行くはず」を独立な新入力にすることはできない。
この同値性は指定continuum coreについてであり、任意の有限joint pathへ
未証明のGalerkin収束を挟んだ主張ではない。

## 5. 共通parentへの持ち上げはどこで止まるか

算術和 \(S_\lambda\) 自体はcanonicalで、正半直線のseed空間からYへboundedかつonto。
しかし \((0,\lambda^{-1})\) 支持の全関数がkernelに入り、等長写像ではない。
自然なpullbackは
\[
 J_A(h)=\frac{Q_W(S_\lambda h,S_\lambda h)}
                  {\langle h,S_\lambda^*S_\lambda h\rangle},\qquad
 S_\lambda^*Q_WS_\lambda h=\mu S_\lambda^*S_\lambda h .
\tag{P}
\]
これはAの再表現。Bを選ぶ新しいparent principleではない。

さらに全natural source上の
\[
 Q_W(S_\lambda h,S_\lambda h)
   =\alpha_\lambda J_{\rm leak}(h)+\beta_\lambda\|S_\lambda h\|^2,
 \qquad \alpha_\lambda\ne0
\]
はkernel上で矛盾する。左辺と最後の項は0、leakageは正になるからである。
concentration作用素もkernelを保たず、単純な
\(\widetilde C_\lambda S_\lambda=S_\lambda C_\lambda\) は定義できない。
非零kernel関数にCを作用させると解析的な非零関数となり、
算術和の一項しかない上端領域で消えないためである。

従ってType II/IIIを保証する可換図式や、objective同一性はない。
追加制約を持つ全ての未知parentを排除したわけではない。
ただし誤差項を「差そのもの」と定義して小ささを仮定することは進展に数えない。

## 6. Γ-limit と common Euler equation

Γ/Mosco routeにはcanonical空間同定、equi-coercivity、liminf、
recovery sequence、正規化された解の一意性が必要である。
本対象ではこれらを満たす共通limit functionalを得ていない。
自然なglobal Weil候補には上記radicalの非一意性もある。
Mosco収束・各段階compact resolvent・一様gapだけでgroundが逃走する
対角形式の厳密反例を独立監査に記録した。

prolate側は
\[
 PW_\lambda\psi_j=\theta_j\psi_j,\qquad
 (PW_\lambda-\theta_0)(PW_\lambda-\theta_4)h_\lambda=0
\]
であり、Weil側はprime shiftsを持つ非局所の(P)。
二つとも固有値問題というだけでは同じEuler式ではない。
known prolate→Hermite limitがWeil側のlimiting equationを供給するわけでもない。
共通境界flux・Lagrange multiplier identity・small-commutator estimateは未取得。
可換でもgroundが反対になる有限反例があるので可換性だけにも依存しない。

## 7. 三試行のstrategy review

|試行|実行・取得|止まった箇所|判定|
|---|---|---|---|
|A Common Rayleigh|actual finite scoring、gap/residual式、既知radicalの確認|全parameterの \(\varepsilon/\Delta\) と(V*)のrateなし|限定監査終了。数値増量だけで続行しない|
|B Common parent / Γ-limit|canonical pullback、kernel反証、radical非一意性|同じcoercive unique-minimizer limitを取得できない|指定単純parentを棄却。一般不存在の主張なし|
|C Common Euler|prolate 0/4 annihilatorとWeilの式を比較|自然なintertwining・共通limit equationなし|類比のみでは採用しない|

three-direction stopを実行する。新しい主証明ルート、positivity、metricを作らない。
再開を正当化するにはactual formでのenergy/residualとfull-gapの**定量評価**、
または追加の独立な状態選択恒等式が必要である。
これは新仮定として採用する要求ではなく、現在何が未証明かの記録である。

## 8. 最終六問

1. **Aは何を最適化するか。** 指定log支持・有限Fourier空間・標準 \(L^2\) 単位球面でactual Weil形式を最小化する。
2. **Bは何を最適化するか。** seedの各prolate modeにはconcentration min–maxがあるが、指定Bは0/4のmean-zero mixtureの算術像。B自体の同じ最小化原理はない。
3. **同じquantityか。** 確認できない。通常concentration目的量との単純同一化はkernel検査で偽。
4. **共通parentへ持ち上げられるか。** Aのcanonical pullbackは書けるが、Bも選ぶparentは得られない。
5. **Bの点数はどれほど最低に近いか。** 上表の有限診断では非常に近い例がある一方、excess/gapが巨大な例もある。全parameterのalmost-minimizer theoremはない。
6. **1位と2位の差を使いA≈Bを証明できたか。** 一般gap lemmaは証明したが、必要な算術的比の極限は未証明。G*にはさらに(V*)とprojection tailのrateが要る。

**NO COMMON PARENT IDENTIFIED.**

## 保存・監査

- [candidate matrix](common_parent_candidate_matrix.md)
- [independent adversarial audit](../../audits/proofs/audits/common_parent_variational_adversarial.md)
- [prior art / perturbation / limits](common_parent/notes/variational_limits_and_prior_art.md)
- [machine state](../../../data/source-records/research/common_parent_state.json)
- preservation baseline（原資料参照・公開版未収録: `research/common_parent/preservation_baseline.json`）

有限数値、既知のradical identity、標準摂動補題はRH進展として誇張しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/common_parent_variational_adversarial.md`](../../audits/proofs/audits/common_parent_variational_adversarial.md)
- [`research/common_parent/experiments/high_precision_results.json`](../../../artifacts/research/common_parent/experiments/high_precision_results.json)
- [`research/common_parent/notes/B_variational_and_equations.md`](common_parent/notes/B_variational_and_equations.md)
- [`research/common_parent/notes/rayleigh_calculation.md`](common_parent/notes/rayleigh_calculation.md)
- [`research/common_parent/notes/variational_limits_and_prior_art.md`](common_parent/notes/variational_limits_and_prior_art.md)
- [`research/common_parent_candidate_matrix.md`](common_parent_candidate_matrix.md)
- [`research/common_parent_state.json`](../../../data/source-records/research/common_parent_state.json)
- [`research/common_variational_dictionary.md`](common_variational_dictionary.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/high_precision_results.json` — SOURCE REFERENCE NOT INCLUDED
- `research/common_parent/preservation_baseline.json` — SOURCE REFERENCE NOT INCLUDED
