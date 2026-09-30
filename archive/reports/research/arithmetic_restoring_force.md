**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_restoring_force.md` · Original SHA-256: `08d2a661c8bdfc24b5f14f7597ebcda8c87a3b327796868e25d1d57c27a3f241`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Restoring Force / Critical-Line Confinement

2026-09-30。独立した限定監査。**RH OPEN。新しい独立の復元法則は未取得。**

物理的な力・束縛状態は着想としてのみ用い、証明の前提にしない。Hilbert–Pólya、正metric、weighted completion、Weil positivityを再開しない。既存ファイル・state・proof graphは読取り専用。

## 1. 判定の要点

**NO ARITHMETIC RESTORING FORCE IDENTIFIED。**

この文言は、actual arithmeticにそのような法則が存在しないと証明したという意味ではない。今回検査した三方向で、RHを仮定せず全零点を臨界線へ拘束する新しい算術入力を特定できなかった、という終了判定である。

- **A：scalar force。** \(\log|\xi|\) の全域の復元符号は既知のRH同値条件。符号を反転したpotentialは既知の実軸で逆向きになる。全水平log凸性は実際の零点近傍で偽。中心上の正曲率だけでも不足する。
- **B：theta二条件。** actual核から正確に導けるが、過去のmodular-generator式(D4)と同じ。正核・既知の凹性から両条件の同時消滅を排除できない。標準的Toeplitz PF∞はactual核に対して偽、Fourier変換のLaguerre–Pólya性はRHへ戻る。
- **C：変形と零点運動。** de Bruijnの既知の帯収縮は正しい。ただしforward heat-parameter方向の結果で、元の時刻0が実零点域にあることを証明しない。各非実枝が常に中心へ動くという一般則も偽。

以下は反証・同値性・未取得を区別して記録する。有限の符号標本からRHを推論しない。

## 2. 記号とdomain

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
 s=\frac12+a+it.
\]

二つの座標を混同しない：

\[
 \mathcal X(z)=\xi(1/2+z),\qquad
 F(w)=\xi(1/2+iw),\qquad
 \xi(1/2+a+it)=F(t-ia).
 \tag{1}
\]

両関数はevenでreal symmetryを持つが、RHのaxisは \(\mathcal X\) では虚軸、\(F\) では実軸。

\[
 V_+(\sigma,t)=\log|\xi(\sigma+it)|,\qquad
 Q(\sigma,t)=\partial_\sigma V_+=\Re\frac{\xi'}{\xi}(\sigma+it).
 \tag{2}
\]

(2)は \(\xi(s)\ne0\) 上で用いる。復元方向は \(aQ>0\)、すなわち \(\mathcal F_+=-Q\) に対し \(a\mathcal F_+<0\)。\(a=0\) でstrict inequalityを要求しない。\(V_-=-V_+\) なら符号は反転する。

零点は \(\xi'/\xi=0\) という平衡点ではない。multiplicity \(m\) の零点 \(\rho\) では

\[
 \frac{\xi'}{\xi}(s)=\frac{m}{s-\rho}+O(1).
 \tag{3}
\]

したがってlog potentialは特異、forceも一般に発散する。

## 3. Track A：prime・Gamma・poleを分離した符号

\[
 Q(\sigma,t)=
 \Re\left(\frac1s+\frac1{s-1}\right)
 -\frac12\log\pi+\frac12\Re\psi(s/2)
 +\Re\frac{\zeta'}{\zeta}(s).
 \tag{4}
\]

これは各因子が定義される点での分解。個々の項の極が相殺する \(s=0,1\) やtrivial-zero付近では、completed関数全体の極限を使う。

\(\sigma>1\) に限ってprime部分は絶対収束し、

\[
 \Re\frac{\zeta'}{\zeta}(\sigma+it)
 =-\sum_{n\ge2}\Lambda(n)n^{-\sigma}\cos(t\log n).
 \tag{5}
\]

この符号は不定。例えば \(\sigma=8\) で \(t=0\) では負、\(t=\pi/\log2\) では正である。後者は \(n=2\) 項の下界から全残りの絶対上界を引いて、正の有理数 \(248273/164602368\) を下界として証明できる。数値実験だけによる判定ではない。[直接計算](arithmetic_restoring_force/notes/diagnostics_and_scope.md)

pole-removal項も \(t\) によって符号が変わり得る。例えば \(1/2<\sigma<1\) で \(t=0\) では負、十分大きい \(|t|\) では正。Gamma・\(\pi\) の項も独立の一様な中心復元項ではない。各因子の一部を落として全体の符号と同一視しない。

一方、**completed \(Q\) の全域復元符号は反証されたわけではない**。

\[
 \boxed{\mathrm{RH}\iff
  aQ(1/2+a,t)>0
  \quad\text{for all }a\ne0,t\in\mathbb R
       \text{ with }\xi(1/2+a+it)\ne0.}
 \tag{6}
\]

RH下ではHadamard productから、multiplicity込みで
\(Q=\sum_\gamma a/(a^2+(t-\gamma)^2)\)。逆にoff-line零点があれば、そのすぐ中心側で(3)が逆符号を生む。(6)は新しい仮説ではなく、既知の水平monotonicity criterionと整合する。[Sondow–Dumitrescu, Theorem 1 / Corollary 1](https://arxiv.org/pdf/1005.1104)

無条件では \(\sigma>1\) と \(\sigma<0\) の既知zero-free半平面で対応する符号が成立し、実軸 \(t=0\) でもactual正theta核により成立する。しかしそこからcritical stripの全 \(t\) へ延ばす独立算術評価はない。

### 曲率と「中心が好ましい」の限界

\(\xi(1/2+it)\ne0\) なら対称性により \(Q(1/2,t)=0\)。水平曲率は

\[
 \kappa(t)=\partial_\sigma^2 V_+(1/2,t)
 =\frac{F'(t)^2-F(t)F''(t)}{F(t)^2}.
 \tag{7}
\]

これは一次Laguerre inequalityの量。RH下では正だが、今回全 \(t\) で無条件に証明したわけではない。

全水平log凸性は無条件に偽。既知のcritical-line零点 \(1/2+i\gamma\) の水平近傍では
\(\partial_\sigma^2\log|\xi(1/2+a+i\gamma)|=-m/a^2+O(1)<0\)。
この反証に単純零点仮定は不要。一方、\(t=0\) では正のtheta測度のlog-mgfとして曲率は分散になり正。従って \(V_-\) はここで中心最大となり、所望の向きと逆。

さらに、中心の全regular点で \(\kappa>0\) という条件だけでもoff-axis zerosを排除しない。明示模型

\[
 F_{\rm syn}(w)=\cos(10w)
   \left((w-1)^2+\frac1{16}\right)
   \left((w+1)^2+\frac1{16}\right)
 \tag{8}
\]

はeven、real、order 1で、\(w=\pm1\pm i/4\) に零点を持つ。それでもreal \(t\) のnonzero点では
\(-(\log|F_{\rm syn}|)''\ge100-64=36\)。
つまり各通常点での局所的な水平minimumと、全横方向の単調性は違う。actual Euler/Gamma係数を保った模型ではなく、この弱い一般条件への反例だけである。

また \(\log|\xi|\) はzero-free領域でharmonicなので、水平凸性を二次元のconfining minimumと呼ばない。特に \(s=1/2\) は二次元ではsaddle。 \(|\xi|^2\) の水平凸性は別の条件で、こちらの全域版はRH同値になる。log曲率の反例を別potentialへ誤用しない。

**A判定：部分領域の既知符号はあるが、独立なglobal restoring lawは未取得。**
詳細は [scalar監査](../../audits/research/arithmetic_restoring_force/notes/scalar_sign_audit.md)。

## 4. Track B：actual theta核の二条件

このrepoの規約を固定する：

\[
 \Phi(x)=\sum_{n\ge1}
 \left(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2}\right)
             e^{-\pi n^2e^{2x}}\quad(x\ge0),
 \qquad \Phi(-x)=\Phi(x).
 \tag{9}
\]

Poisson反転から滑らかなeven kernelとなり、全導関数がdouble-exponentialに減衰する。\(x\ge0\) で各項は正。零点位置を入力しないactual arithmetic kernelである。

\[
 F(w)=\int_{\mathbb R}\Phi(x)e^{iwx}\,dx
     =2\int_0^\infty\Phi(x)\cos(wx)\,dx.
 \tag{10}
\]

全複素 \(w\) に絶対収束し、複素compact集合で微分交換可能。Riemannのtheta表示を上の変数へ換えたもの。[Riemann 1859、Wilkins訳 p.3](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf)

従って

\[
\begin{aligned}
 \xi(1/2+a+it)&=U(a,t)+iJ(a,t),\\
 U(a,t)&=2\int_0^\infty\Phi(x)\cosh(ax)\cos(tx)\,dx,\\
 J(a,t)&=2\int_0^\infty\Phi(x)\sinh(ax)\sin(tx)\,dx.
\end{aligned}
\tag{11}
\]

符号は \(w=t-ia\) と \(\cos(t x-iax)=\cos(tx)\cosh(ax)+i\sin(tx)\sinh(ax)\) に一致する。off-line zeroの条件は正確に \(U=J=0,\ a\ne0\)。

**今回の式は新しくない。** 既存 [phase2_modular_generator.md (D4)](notes/phase2_modular_generator.md) と同一で、単なる位相／距離の言い換えによる新しい制約は増えていない。

\(t=0\) では \(U>0\) なので零点を除外できる。しかし \(t\ne0\) ではcosとsinが振動する。\(a>0\) に限定しても、正の \(\Phi\)、\(\cosh\)、\(\sinh\) だけから二つの積分の同時消滅を否定できない。分けて非負と扱うこともできない。

### actual shapeとsynthetic反証の照合

actual核の強い既知shapeとして \(v\mapsto\log\Phi(\sqrt v)\) の厳密凹性がある。これはCsordas–Vargaの原定理で確認した。しかし既存の
\(e^{-x^2}(1+3x^2/20+x^4/100)\)
も対応する凹性を持ち、そのFourier transformには非実零点がある。

過去には、正seed、正completed kernel、Poisson対称性、帯内限定などを保つより強いsynthetic例も構成済み。ただし標準Gamma因子を変更した例であり、actual zetaの反例ではない。

このため今回、genericな核の正性・低階形状条件へ戻らない。actual thetaの標準算術から \(a\ne0\) の同時消滅を禁止する新しい不等式は得ていない。

### PF∞とLaguerre–Pólyaを混同しない

標準的な「Toeplitz核 \(\Phi(x-y)\) が全次数でtotally positive」というPF∞は、actual \(\Phi\) に対して偽である。

Schoenbergの必要条件では、そのbilateral Laplace transformは、0を含むstripであるentire Laguerre–Pólya関数の逆数になる。actual \(\Phi\) のLaplace transform自体はentireなので、その逆数との積1が全平面へ延びる。積因子に零点を許せず、even性も使うと非退化のintegrable densityはGaussianに限られる。actual double-exponential tailとは矛盾する。

これは「Fourier transform \(F\) がLaguerre–Pólyaでない」という結論ではない。一方、\(F\) がLaguerre–Pólyaに属するという条件は、actual \(F\) ではRH同値で未証明である。二種類のtotal positivity／real-zero criterionを取り違えない。

**B判定：二条件は正確だが既存式と重複。独立なactual-kernel obstructionは未取得。**
一次資料、核の定数換算、PF∞証明、過去反例の保持条件は [theta監査](arithmetic_restoring_force/notes/theta_off_axis.md)。

## 5. Track C：復元と見える変形の方向

\[
 H_\tau(w)=\int_{\mathbb R}e^{\tau x^2}\Phi(x)e^{iwx}\,dx,
 \qquad \partial_\tau H_\tau=-\partial_w^2H_\tau.
 \tag{12}
\]

これは \(\tau\) 増加方向ではbackward heat。全実 \(\tau\) で合法だが、\(\tau\ne0\) にactual ζと同じEuler/Gamma構造があるとはいわない。物理時間でもunitary evolutionでもない。

単純零点の局所枝は

\[
 w'(\tau)=H_\tau''(w)/H_\tau'(w).
 \tag{13}
\]

衝突・multiple zerosの位置ではこの商で枝の微分を定義しない。実零点列に対する既知のrepulsion equationも、初めから全枝が実である範囲を勝手に \(\tau=0\) まで広げない。

de Bruijnの既知のstrip contractionはactual familyに適用できる。この規約では、初期幅 \(|\Im w|\le1/2\) から \(\tau\ge1/8\) の全実零点性を得る。これは保守的な古典上界の換算で、最新の最良定数ではない。

Newman閾値を \(\lambda_{\rm repo}\) とすれば
\(H_\tau\) が全実零点を持つことと \(\tau\ge\lambda_{\rm repo}\) は同値で、Rodgers–Taoの非負性も既知。だが必要なのは \(\lambda_{\rm repo}\le0\)、すなわちRHそのもの。forwardな帯収縮から、正の安全時刻を元の0へ逆向きに戻すことはできない。

各内側の非実枝が常に軸へ戻るという一般則は、even real polynomialの同じheat equationでも偽になる。上端の帯が収縮することと、内部の各枝が単調に戻ることは別である。

Stieltjesのorthogonal-polynomial zerosやrandom-matrix log gasは別の対象。前者には所定の微分方程式・実区間・weightがあり、後者はensembleの確率分布である。actual ζへその平衡原理を移す定理は得ていない。

**C判定：既知のforward収縮はあるが、時刻0の実零点性を与える新しい算術lawは未取得。**
規約、原典、明示的outward branchは [deformation / electrostatics監査](arithmetic_restoring_force/notes/deformation_and_electrostatics.md)。

## 6. Gaussian observable・energyとの接続

全域(6)または(11)の全off-axis排除が独立に証明されれば、全零点実部が \(1/2\) となり、既存のfaithful Gaussian criterionを通じて
\[
 A(u)=O_\varepsilon(e^{\varepsilon u})\quad\forall\varepsilon>0
\]
が従う。しかしその前半を今回証明していない。後半だけで新しいbridgeと数えない。

unweighted有限energy案は再開しない。actual \(A\notin L^2(\mathbb R)\) は以前に確認済み。任意weightや新しいmetricを後から設計しない。\((\sigma,t)\) のscalar potentialを \(u\)-energyへ移す自然な算術恒等式も得ていない。

## 7. 数値検査とstrategy review

50桁の128点grid、一部80桁との照合、中心曲率16点、既知零点近傍、theta二積分5点を診断した。first-derivative signに反する点は見つからなかったが、それはRHやglobal signの証明ではない。log曲率の負値とprime側の反対符号は、それぞれ解析的反証も伴う。[実験結果](../../../artifacts/research/arithmetic_restoring_force/experiments/results.json)

三方向とも、偽の一般則、過去の同一theta式、または既知RH同値条件へ戻った。actual thetaの一意な全算術構造を使う新しい排除不等式は未取得。

**NO ARITHMETIC RESTORING FORCE IDENTIFIED。**

比喩は説明上のheuristicとしてのみ保存する。第4の候補へ移らず、この限定監査を終了する。RHの証明・反証、新しいMertens bound、主proof graphへのmergeはない。

## 8. 保存先

- [候補比較](arithmetic_restoring_force_candidates.md)
- [独立反証監査](../../audits/proofs/audits/arithmetic_restoring_force_adversarial.md)
- [state](../../../data/source-records/research/arithmetic_restoring_force_state.json)
- [持ち帰り用plain-text報告](arithmetic_restoring_force/completion_report.txt)
- [旧ファイル保存確認](../../../data/source-records/research/arithmetic_restoring_force/preservation_check.json)
- [validation](../../../data/source-records/research/arithmetic_restoring_force/validation.json)


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/arithmetic_restoring_force_adversarial.md`](../../audits/proofs/audits/arithmetic_restoring_force_adversarial.md)
- [`research/arithmetic_restoring_force/completion_report.txt`](arithmetic_restoring_force/completion_report.txt)
- [`research/arithmetic_restoring_force/experiments/results.json`](../../../artifacts/research/arithmetic_restoring_force/experiments/results.json)
- [`research/arithmetic_restoring_force/notes/deformation_and_electrostatics.md`](arithmetic_restoring_force/notes/deformation_and_electrostatics.md)
- [`research/arithmetic_restoring_force/notes/diagnostics_and_scope.md`](arithmetic_restoring_force/notes/diagnostics_and_scope.md)
- [`research/arithmetic_restoring_force/notes/scalar_sign_audit.md`](../../audits/research/arithmetic_restoring_force/notes/scalar_sign_audit.md)
- [`research/arithmetic_restoring_force/notes/theta_off_axis.md`](arithmetic_restoring_force/notes/theta_off_axis.md)
- [`research/arithmetic_restoring_force/preservation_check.json`](../../../data/source-records/research/arithmetic_restoring_force/preservation_check.json)
- [`research/arithmetic_restoring_force/validation.json`](../../../data/source-records/research/arithmetic_restoring_force/validation.json)
- [`research/arithmetic_restoring_force_candidates.md`](arithmetic_restoring_force_candidates.md)
- [`research/arithmetic_restoring_force_state.json`](../../../data/source-records/research/arithmetic_restoring_force_state.json)
- [`research/notes/phase2_modular_generator.md`](notes/phase2_modular_generator.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/results.json` — SOURCE REFERENCE NOT INCLUDED
