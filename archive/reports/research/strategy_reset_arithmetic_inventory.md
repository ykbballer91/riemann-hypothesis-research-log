**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/strategy_reset_arithmetic_inventory.md` · Original SHA-256: `1ed1c620d2e07aedc0739d8849ccbc43fde9a0130cc5bb68a860e836f2e91a96`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# RH Strategy Reset — Arithmetic Inventory / Möbius Closure Audit

2026-09-30。**監査完了。RH OPEN。NO JUSTIFIED NEXT TRACK。**

これは新しい証明トラックではない。過去の研究を止める一般的命令でもなく、今回指定された研究空間の棚卸しである。旧研究ファイル・state・proof graphを読取り専用とし、今回の報告を自動統合しない。

## 1. 結論と監査範囲

確認した範囲では、次に一本の証明トラックを開始するに足る入力は **0件** だった。

未適用だった算術情報そのものは残っていた。Type I/II、短区間、平均相関、算術級数の平均、Dirichlet polynomialの平均値などは、既存の座標変換と同じ内容ではない。しかし、その定理の実際の量化・率を固定Gaussian observableへ戻すと、既知PNT型を超える必要な各点評価には到達しない。未適用の定理があることだけを次トラックの根拠にはしない。

新しいclosureの表示には、収束・解の選択を点検する意義がある。一方、準指数成長を強制する独立な安定性評価は含まれない。さらに、零点での指数関数を通常の収束和によるhomogeneous solutionとする解釈には、重要なdomain訂正が必要だった。

監査は保存ログ、下記の一次資料・著者講義資料、式の直接検算に基づく。各原論文の全証明を再証明した、文献全体を尽くした、将来の全手法を不可能とした、という意味ではない。「未使用」は、保存ログ中の推論でその定理の定量評価を実際に使ったかで判定した。単なる文献名の出現は使用と数えない。

## 2. 固定したactual observableと既存の到達点

\[
 \phi(u)=e^{-u^2},\qquad
 R(u)=\sum_{n\ge1}\mu(n)\phi(u-\log n),\qquad
 A(u)=e^{-u/2}R(u),\qquad g(u)=e^{-u^2-u/2}.
\]

前トラックの [Gaussian解析 G6](global_remainder/notes/gaussian_global_decomposition.md) は、固定kernelについて

\[
 \mathrm{RH}\ \Longleftrightarrow\
 \forall\varepsilon>0,\quad
 A(u)=O_\varepsilon(e^{\varepsilon u})\quad(u\to+\infty)
 \tag{SR1}
\]

を確認している。この同値性は今回の新入力ではない。

必要なのは、同じactual \(\mu\)、同じ固定kernel、同じ全 \(u\) の条件を保ったまま右辺を算術から評価すること。平均、ほとんど全区間、可変kernel、零点を失うcompletionの結果とは交換できない。

## 3. C1/C2は絶対収束で成立する

任意の実 \(u\)、任意の \(c>1\) について

\[
\begin{aligned}
 \sum_{m,n\ge1}|\mu(n)|e^{-(u-\log(mn))^2}
 &\le\sum_{k\ge1}d(k)e^{-(u-\log k)^2}\\
 &\le e^{cu+c^2/4}\zeta(c)^2<\infty.
\end{aligned}
\tag{SR2}
\]

最後は \(-v^2+cv\le c^2/4\) と \(\sum d(k)k^{-c}=\zeta(c)^2\) による。compact \(u\)-setsでも一様で、有限階の微分や固定次数のlog weightsも同様に扱える。

従って和を交換して

\[
 \sum_{m\ge1}R(u-\log m)
 =\sum_{k\ge1}\left(\sum_{n\mid k}\mu(n)\right)\phi(u-\log k)
 =\phi(u).
 \tag{C1}
\]

また \(m^{-1/2}A(u-\log m)=e^{-u/2}R(u-\log m)\) なので

\[
 \boxed{\sum_{m\ge1}m^{-1/2}A(u-\log m)=g(u).}
 \tag{C2}
\]

このouter sumも絶対収束する。Möbius反転をGaussianで表現した正しい恒等式であり、新規性は主張しない。

bilateral Laplace規約を \(\mathcal L f(z)=\int_{\mathbb R}f(u)e^{-zu}\,du\) とすると、Fubiniで直接正当化できる域は \(\Re z>1/2\) であり、

\[
 \zeta(1/2+z)\mathcal L A(z)
 =\sqrt\pi\,e^{(z+1/2)^2/4}.
 \tag{SR3}
\]

この域ではclosureと \(1/\zeta\) 表示は同じ反転を記述する。

## 4. 重要訂正：零点は通常のclosureのhomogeneous解ではない

指数関数 \(H(u)=e^{zu}\) に対して

\[
 \sum_{m\ge1}m^{-1/2}H(u-\log m)
 =e^{zu}\sum_{m\ge1}m^{-1/2-z}
 \tag{SR4}
\]

を絶対収束和として使えるのは \(\Re z>1/2\)。この領域にζ零点はない。非自明零点 \(\rho\) で \(z=\rho-1/2\) とすると、必要な普通の和は発散する。具体的には

\[
 \sum_{m\le N}m^{-\rho}
 =\frac{N^{1-\rho}}{1-\rho}+\zeta(\rho)
       +O_\rho(N^{-\Re\rho}),\qquad 0<\Re\rho<1.
 \tag{SR5}
\]

従って「零点はclosureの自由mode」は **解析接続したsymbolの形式的mode、または逆変換のresidue mode** としてのみ読む。C2の同じ絶対収束domainにあるclassical homogeneous solutionとはいえない。zero-residue expansionへC2の無限和を項別に作用させることも正当化されていない。

これは過去の算術quotient上の非零dual evaluationsを否定しない。それとは異なるdomainの問題である。今回、regularized actionや新しいtopologyでこの差を埋めていない。

## 5. 左側境界は解を一意に選ぶが、右側の成長は決めない

新しいnormやcompletionを導入せず、左側で

\[
 |f(u)|\le C e^{-\eta u^2+b|u|}\quad(u\le0),\quad\eta>0
 \tag{SR6}
\]

を満たす連続関数を考える。右側にはgrowth conditionを課さない。

polynomial growthの係数 \(a(n)\) による既存のdelay sum
\(D_af(u)=\sum a(n)f(u-\log n)\) はこのclass上で絶対収束し、
\(D_aD_b=D_{a*b}\)。従って \(D_\mu D_1=I\)。正規化したsumでも同じである。

このためC1/C2はこのclassで一意に解け、解はもとの \(R,A\) そのもの。実際、

\[
 \frac{R(u)}{\phi(u)}=\frac{A(u)}{g(u)}
       =1+O(2^{2u})\quad(u\to-\infty).
 \tag{SR7}
\]

しかし一意性は安定性ではない。反例は \(a>1,L>0\) の有限遅延方程式

\[
 f(u)+af(u-L)=e^{-u^2},\qquad
 f_+(u)=\sum_{j\ge0}(-a)^j e^{-(u-jL)^2}.
 \tag{SR8}
\]

\(f_+\) は同じ左Gaussian条件を満たす唯一の解だが、そのLaplace transformは

\[
 \frac{\sqrt\pi e^{s^2/4}}{1+ae^{-Ls}},\qquad
 \Re s>(\log a)/L.
 \tag{SR9}
\]

右半平面に非零residueを持つpolesがあり、右方向に指数増大するsubsequenceがある。同じ方程式には未来側のGaussian和で作るbounded solutionもあるが、左Gaussian条件を満たさない。境界上symbolの非消失だけでは、正しい向きのinverseを選べない。

この模型はactual zetaの反例ではない。「causality＋forcing＋左急減衰＋一意性だから安定」という一般推論だけを反証する。actual arithmetic kernelへ独立の安定性評価があるかは、別の未達事項である。

C2のkernelの総質量 \(\sum m^{-1/2}\) は無限。通常のprobability renewal theoremはそのまま適用できない。\(A_\sigma=e^{-\sigma u}A\) とtiltすれば質量は \(\zeta(1/2+\sigma)\) となるが、有限なのは \(\sigma>1/2\) で、戻す際に \(e^{\sigma u}\) を払う。Wiener–Hopfのinverseを右半平面全域でpole-freeと仮定すれば、必要なζの零点なし条件を先に入れることになる。

証明と原典照合は [closure監査 CC2–CC6](strategy_reset/notes/closure_causality.md)。

## 6. 高次closureは独立の追加拘束か

正しいlogの規約は \(L(n)=\log n\)、pointwise productを \(\mu L\) として

\[
 \mu*L=+\Lambda,\qquad (\mu L)*1=-\Lambda,\qquad
 \mu L=-\mu*\Lambda.
 \tag{SR10}
\]

ユーザー指示中の \(\mu*\log=-\Lambda\) は通常のDirichlet convolutionでは符号が逆。負号が付くのは第二式である。

高次に \(\Lambda_k=\mu*L^k\) と置くと \(\Lambda_k(n)\ge0\)。これはgenuineな算術的正値性であり、消去しない。例えば \(n>1\)、異なる素因数が \(p_1,\ldots,p_r\)、\(v=\log n,a_i=\log p_i\) なら

\[
 \Lambda_k(n)=
 \begin{cases}
 0 &(k<r),\\
 \displaystyle\frac{k!}{(k-r)!}
 \int_0^{a_1}\!\cdots\!\int_0^{a_r}
 (v-t_1-\cdots-t_r)^{k-r}\,dt_1\cdots dt_r &(k\ge r).
 \end{cases}
 \tag{SR11}
\]

正規化delay sumを \(S_af=\sum a(n)n^{-1/2}f(u-\log n)\) と略記すれば、

\[
 S_{L^k}A=S_{\Lambda_k}g\ge0,\qquad
 S_1 A^{(j)}=g^{(j)},\qquad
 S_1^rA=S_{1^{*(r-1)}}g.
 \tag{SR12}
\]

全部absolute identitiesだが、右辺は一般に0ではない。transformの比
\((-1)^k\zeta^{(k)}/\zeta\) は零点でpolesを持ち得るので、\(\zeta^{(k)}(\rho)=0\) という新しい制約は出ない。高次の正momentから元のsigned measureの正値性を推論する一般原理も成立しない。

これらはμ反転、係数微分、有限差分の既知代数から導かれる。独立のsubexponential estimateを追加したわけではない。全算術から論理的に独立かではなく、既存の恒等式を書き換える以上の定量入力を得たか、という意味で評価した。

有限整数 \(n\le1000\) でも、μ反転1000件、log符号1000件、\(k=1,\ldots,4\) のformal log-prime多項式4000件をexact arithmeticで検算した。一般証明は [CC4](strategy_reset/notes/closure_causality.md)、検算は [結果JSON](../../../artifacts/research/strategy_reset/notes/finite_identity_checks.json)。有限検算を漸近評価の根拠にしていない。

## 7. 過去11トラックが戻った壁

全trackの六項目比較は [dependency / failure matrix](arithmetic_inventory_matrix.md) に保存した。

| 大分類 | 保持できたもの | 欠けたもの |
|---|---|---|
| Geometry / positivity | actual explicit formula、算術作用、いくつかのambient positive forms | 全零点を失わない同一対象の正値性・nondegenerate descent |
| Scale / dynamics | 各零点の正確な倍率、actual Möbius reduction | returnの指数率を0にする独立な算術評価 |
| Combinatorial cancellation | actual squarefree parity、Morse・recursion・weighted threshold | 線形規模のeven/odd populationsの差の定量制御 |
| Phase / harmonic | Bohr/Kroneckerの厳密表示、全Haar統計 | actual cutoff/readoutとの相関。分布一致でもreadoutは異なる |
| Complex analytic | 全零点を検出するGaussian、全local係数消失、residue分解 | global remainderの成長率の独立上界 |

共通する壁は、**actual arithmeticを完全に保持したsigned observableへの大域的な相殺評価** が得られていないこと。正値性、安定性、境界相関、global remainderという語だけを変えて同じ義務を再要求した箇所がある。

ただし全ての大きい理論パッケージがRHと双方向に同値だったとはいわない。exact Weil positivity、今回の固定scalar criterionなどは同値。任意の完全なpositive geometry、全operatorの一様制御、domain条件まで含む構成は、より強いか逆向きが未証明の場合がある。

## 8. Candidate A：bilinear / Type I–II

既存ログで主要評価として未適用だった独立の算術手法はある。Green–Taoのactual μのVaughan型有限分解、Heath–Brown型因子分解、large sieve、dispersionを定理の範囲まで確認した。

しかしGaussianの中心block \(x<n\le2x\) では

\[
 e^{-(\log2)^2}\le e^{-\log^2(n/x)}\le1.
\]

裸のType I内和に振動はなく、加法minor arcの小ささを与える前提を満たさない。Mellin phase \(f(n)=n^{it}\) のType II長方形積も

\[
 f(dw)\overline{f(dw')}\overline{f(d'w)}f(d'w')=1
\]

と正確に消える。これらはbilinear法全般を否定せず、今回提案された既知推定の直接適用を排除する。

Davenportの全加法周波数一様評価は、任意固定 \(B\) について \(N(\log N)^{-B}\)。\(\alpha=0\) はMertens和そのもの。部分積分で実際に得られるのは

\[
 |A(u)|\ll_B e^{u/2}u^{-B},
 \tag{SR13}
\]

であり、任意小さい指数率ではない。全域版major arcの解析的入力を「零点領域にも完全非依存」と誤分類しない。

large sieveやDirichlet polynomial平均のsqrt規模を特定の低周波へ移せない。算術級数の誤差をprincipal averageからの差で定義した定理では、\(q=1\) の誤差が恒等的に0になることすらあり、global Mertensを評価したことにならない。mollifierの零点割合も全零点の排除ではない。

**判定：未適用の定理はあるが、今回の成功条件を満たす入力は0。**
定理番号・範囲・primary linksは [Candidate A監査](strategy_reset/notes/bilinear_and_uniform_estimates.md)。特に [Green–Tao 2008](https://www.numdam.org/item/10.5802/aif.2401.pdf) Lemma 4.1、Proposition 4.2、§5。

## 9. Candidate C：平均相関・短区間

固定log Gaussianの中心は
\(xe^{-B}\le n\le xe^B\)、幅 \(2x\sinh B\)。固定 \(B>0\) では \(x\) に比例し、短い加法区間ではない。さらにGaussianの尾は消せず、

\[
 x^{-1/2}\sum_{|\log(n/x)|>B}e^{-\log^2(n/x)}
 \ll \frac{x^{1/2}e^{-(B-1/2)^2}}{B-1/2}
       +x^{-1/2}e^{-B^2}\quad(B\ge1).
 \tag{SR14}
\]

目標 \(0<\varepsilon<1/2\) に対し絶対値だけで尾を \(O(x^\varepsilon)\) へ戻すなら、\(B\) を \(\sqrt{\log x}\) 程度へ増やす必要がある。

MRのalmost-all短区間結果、MR IIの例外集合に対するpower saving、MRTのshift平均、Taoのlog Chowla、Tao–Teräväinenのalmost-all scales、2026改訂版を含むhigher-uniformity/correlationの定理文を区別して確認した。すべてを「定性的o(1)しかない」と片付けてはいない。しかし誤差閾値と例外量、shift範囲、scaleの例外、logとnatural averageを保ったままでは、必要な全 \(u\) の評価は出ない。

例として全区間の [Matomäki–Teräväinen定理1.1](https://ems.press/content/serial-article-files/32826) は、固定 \(\theta>0.55,\eta>0\)、\(H\ge x^\theta\) で
\(\sum_{x<n\le x+H}\mu(n)=O_{\theta,\eta}(H(\log x)^{-1/3+\eta})\)。
これはactual μの強い全区間結果だが、今回の平方根精度とは異なる。最新の最良指数だとは主張しない。

今回のobservableへ相関を入れるexact bridge自体はある。compact supportのbounded \(W\) に対し

\[
\begin{aligned}
 \int W(u)A(u)^2\,du
 &=e^{1/8}\sum_{m,n\ge1}\frac{\mu(m)\mu(n)}{\sqrt{mn}}
      e^{-\frac12(\log(n/m))^2}\\
 &\quad\cdot\int W(u)
     e^{-2(u-\frac12\log(mn)+1/4)^2}\,du.
\end{aligned}
\tag{SR15}
\]

絶対交換可能で、導関数energyにも明示式がある。これは新しい相殺評価ではない。\(n=m+h\) とすると固定log ratioに対応する \(h\) は一般に \(m\) と同程度で、固定shiftの定理と一致しない。有限 \(n\asymp x\) blockでweighted offdiagonalを仮に \(o(x^2)\) にできても、和は \(o(x)\) まで。必要な平方は \(O_\varepsilon(x^{1+2\varepsilon})\)。

平均からpointwiseへ進む道を一般的に否定しない。実際Sobolevの局所不等式

\[
 |A(u_0)|^2\le C\int_{u_0-1}^{u_0+1}(|A|^2+|A'|^2)\,du
 \tag{SR16}
\]

は成立する。しかし右辺を **全移動窓** で \(O_\varepsilon(e^{2\varepsilon u_0})\) とする算術評価が未取得であり、それ自体を新前提にはしない。

また可変幅 \(\sigma(x)=x^{-1/2}\) のGaussianへ変更すると、全係数を \(+1\) にしてもnormalized absolute sumがboundedになる。これは標本数の縮小であり、もとのfixed-kernel RH criterionへのtransferではない。

**判定：未適用の実算術情報はあるが、確認した定理から正当化できる次トラックは0。**
全量化とprimary sourcesは [Candidate C監査](strategy_reset/notes/correlations_and_short_intervals.md)。

## 10. その他のinventoryと採点方法

divisor、Mangoldt、higher moments、Type I/II、短区間、相関、large sieve、AP、characters、pretentious、Kátai/Daboussi–Delange、Sarnak、zero-density、Davenport、Mellin、Dirichlet polynomials、mollifiers、random models、entropy、incidence、GCD、renewal、Wiener–Hopfを [inventory表](arithmetic_inventory_matrix.md) にまとめた。候補ごとに独立性・actual arithmetic・過去使用・定量的強さ・bridgeを記録した。

数値スコアの合計は証明可能性を示さないため、採否は定理の具体的適用可否で決めた。「RH不使用」と「既知zero-free/Mertens評価にも非依存」は分離した。

unique factorizationは有理独立性だけでなく、divisor lattice、convolution、Euler factorization、GCD特徴、actual summation rangeとして既に使用済み。incidence algebraは \(\mu*1=\varepsilon\) の同じ代数。GCD finite-norm改善は既存のnonclosabilityとsigned-readout比較の欠落を解消しない。

random multiplicative functionsの平均定理から、全素数で値 \(-1\) のactual μという指定assignmentを評価できない。entropy/complexityという語だけにも率はない。pretentious theoryの既存black boxをclosureと組み合わせても、今回独立の距離拘束は得られなかった。zero-free/densityは既知のanalytic zero-side inputとして別分類した。

Kátai型の具体的入力としては、[Bourgain–Sarnak–Ziegler Theorem 2](https://arxiv.org/pdf/1110.0992v1) を原文照合した。小さいprime-dilation correlationsが仮定となるが、raw Gaussian readoutの \(p=2,3\) 相関は自然な尺度で正定数に収束し、必要な一様仮定を満たさない。固定したkernel中心の後で長さだけを無限にする適用では、評価が欲しい尺度を過ぎてしまう。詳細は相関ノートC7。

根拠の補足は [scope / miscellaneous監査](strategy_reset/notes/inventory_scope_and_misc.md)。

## 11. Strategy reviewと最終六回答

1. **同じ壁は何か。** 全零点を保持するactual arithmetic objectに対する、RH級の大域的signed cancellationの独立評価。exactnessは得られても、正値性・return stability・parity discrepancy・global remainderの必要な上界は未取得だった。
2. **未使用情報は残っていたか。** はい。特に定量的bilinear、短区間・平均相関、AP/dispersion、Dirichlet polynomial技法。ただし今回確認した適用範囲・率では固定Gaussianの全点準指数成長を導けない。
3. **C2は新入口か。** 検算・solution selectionの説明として有用だが、growth controlの独立入力としては \(1/\zeta\) の同じMöbius反転。因果性は安定性を追加しない。
4. **A/B/Cの生存は。** 0件。Aは非振動部分のpointwise相殺、Bは独立の安定性、Cは必要な率と全移動窓への移行が未取得。
5. **次に一本なら。** 今回の監査から推奨できるものはない。新しい証明トラックを開始しない。
6. **判定。** **NO JUSTIFIED NEXT TRACK。**

これは3候補の現在の証拠に対する停止判定であり、全ての未来の算術的アプローチへの不可能性定理ではない。成功していない同型候補を第4の名前で継続しない。

## 12. 保存・独立監査

- [比較表](arithmetic_inventory_matrix.md)
- [adversarial audit](../../audits/proofs/audits/strategy_reset_adversarial.md)
- [machine-readable state](../../../data/source-records/research/strategy_reset_state.json)
- [持ち帰り用plain-text報告](strategy_reset/completion_report.txt)
- [旧315ファイルの保存確認](../../../data/source-records/research/strategy_reset/preservation_check.json)
- [validation](../../../data/source-records/research/strategy_reset/validation.json)

数学的監査はclosure、bilinear、一部相関を別担当で確認し、closureのdomain・符号・有限遅延反例、相関のGaussian平方完成とSobolev移行を相互点検した。形式化・大規模数値fit・新証明ルートは実施していない。RHはOPENのまま。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/strategy_reset_adversarial.md`](../../audits/proofs/audits/strategy_reset_adversarial.md)
- [`research/arithmetic_inventory_matrix.md`](arithmetic_inventory_matrix.md)
- [`research/global_remainder/notes/gaussian_global_decomposition.md`](global_remainder/notes/gaussian_global_decomposition.md)
- [`research/strategy_reset/completion_report.txt`](strategy_reset/completion_report.txt)
- [`research/strategy_reset/notes/bilinear_and_uniform_estimates.md`](strategy_reset/notes/bilinear_and_uniform_estimates.md)
- [`research/strategy_reset/notes/closure_causality.md`](strategy_reset/notes/closure_causality.md)
- [`research/strategy_reset/notes/correlations_and_short_intervals.md`](strategy_reset/notes/correlations_and_short_intervals.md)
- [`research/strategy_reset/notes/finite_identity_checks.json`](../../../artifacts/research/strategy_reset/notes/finite_identity_checks.json)
- [`research/strategy_reset/notes/inventory_scope_and_misc.md`](strategy_reset/notes/inventory_scope_and_misc.md)
- [`research/strategy_reset/preservation_check.json`](../../../data/source-records/research/strategy_reset/preservation_check.json)
- [`research/strategy_reset/validation.json`](../../../data/source-records/research/strategy_reset/validation.json)
- [`research/strategy_reset_state.json`](../../../data/source-records/research/strategy_reset_state.json)
