**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/strategy_reset/notes/inventory_scope_and_misc.md` · Original SHA-256: `adce043b6affd3cbe6bddeb5bf11448f85ba75c7f357c787bd8087fb49a0daf9`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 棚卸しの範囲と補助情報：incidence・GCD・randomness

2026-09-30。これは証明トラックではなく監査。既存315ファイルをbaselineに固定し、新しい空間・作用素・metricを構成しない。

## 1. 「未使用」の判定方法

過去の主要ログ・state・関連監査を読取り、算術入力が式やestimateの推論で使われたかを確認した。単に参考文献に名前が出ることと、その定理をactual Gaussian observableに適用したことを区別する。

今回の判定は保存された研究ログの範囲に関するもの。数学文献全体の完全検索、各原論文全証明の再検証、全ての将来手法の不可能性は主張しない。

主な読取先：

- Phase I：strategy_review.md の履歴、prime_insertion_closure.md、arithmetic_gram_generator.md、support-propagation-reduction.md、nyman_beurling_closure_gate.md。
- Phase II：generator_boundary_hypothesis.md と三generatorの停止条件。
- Phase III–IV：各主ログ・gap/pairing matrix、quotient collapse とclosability監査。
- Scale Flow：continuous_scale_flow_frobenius.md と局所／全零点表現の区別。
- 後続6トラック：主ログ、candidate matrix、state、既存adversarial audit。

古いファイル内の「次回は〜を開始する」という記述は履歴として読み、今回の指示として実行しない。過去の異なるsuccess levelは当時の定義のまま保持し、一つの進捗尺度に再採点しない。

## 2. Incidence algebraはclosureの独立な第二条件ではない

Rotaの原典では、locally finite posetのincidence algebraにおけるzeta要素の可逆性を示し、整数のdivisibility orderをDirichlet convolutionとして具体化している。§3 Proposition 1、Example 1、印刷pp344–347。[Rota (1964) 原典](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/rota1.pdf)

ここで \(\mu(a,b)=\mu(b/a)\) for \(a\mid b\)。この部分代数の積が \((f*g)(n)=\sum_{d\mid n}f(d)g(n/d)\) である。従って C1/C2 の再表現であり、既存のDyadic inversionとPrime Complexのdivisor latticeで本質的に使用済み。

一般の有限posetには大きいinverse係数もある。bottom、topとその間の \(r\) 個の互いに比較不能な点からなるposetでは、bottomからtopへのMöbius値は \(r-1\)。抽象的なincidence invertibilityだけでは小さいinverseや平方根級signed sumは保証されない。

この反例はactual整数の係数を変更するもので、RHの反例ではない。actual unique factorizationに追加される定量評価を持たずに、一般posetのnormやspectral radiusという語へ移して再開しない。

## 3. unique factorization、GCD/LCM、prime insertion

過去に使われたのはprime-logの有理独立性だけではない。

- divisor identity \(\mu*1=\varepsilon\)：Dyadicのexplicit representative。
- \(\mu*\log=\Lambda\)、prime-power series：Phase Iのprime insertionとlog generator。
- divisor features \(J_{2\alpha}\)、\(\gcd\) の展開：arithmetic_gram_generator.md。
- Euler product、all-prime repetitions、local Tate/Poisson relation：Phases II–IVとScale Flow。
- divisibility complex、cutoffとshared parents：Prime Complex。

算術微分 \(Df(n)=(\log n)f(n)\) のLeibniz則は新しいoperatorを必要としない既知のconvolution計算である。prime insertion/removalやcreationという名称にしても、独立のsigned estimateは増えない。

GCD sumの既知定理には、任意の相異なる整数 \(n_1,\ldots,n_N\) に対する

\[
 \sum_{k,\ell\le N}\frac{\gcd(n_k,n_\ell)}{\sqrt{n_kn_\ell}}
 \ll N\exp\!\left(C\sqrt{\frac{\log N\log\log\log N}{\log\log N}}\right)
\]

がある。Bondarenko–Seip, Theorem 1、および§7のfinite matrix spectral-norm consequenceを確認。[著者論文](https://arxiv.org/pdf/1402.0249)

これは非負kernelの有限和の評価であり、\(|\sum\mu(n)\phi(u-\log n)|^2\) との必要な比較を与えるものではない。また右辺の \(N\) 以外の付加評価因子は行列サイズとともに増大する（表示の絶対定数 \(C\) が \(N\) に依存するという意味ではない）。既存ログではcritical \(\alpha=1/2\) の標準係数 \(\ell^2\) 上の形式は全面的にnonclosableであり、対数Mangoldt形式の負方向も具体的に構成済み。有限GCD estimateはこのdomain障害を除去しない。今回、新しい比較恒等式・domain修復の理由は見つかっていない。

このためGCD方面は「未使用の新入力」ではなく、使用済み構造に既知有限評価を足すだけでは再開できない項目とする。全てのGCD手法を否定する結論ではない。

## 4. generalized Mangoldtの既知性と符号

pointwise function \(L(n)=\log n\) とDirichlet convolutionを区別する。正しい符号は

\[
 \mu*L=\Lambda,\qquad (D\mu)*1=-\Lambda,\qquad D\mu=-\mu*\Lambda .
\]

\(\Lambda_k=\mu*L^k\) には
\(\Lambda_{k+1}=D\Lambda_k+\Lambda*\Lambda_k\) と非負性がある。古典的なSelberg型の係数恒等式であり、各固定 \(k\) のclosureに正のforcingを与えること自体は正しい。導出と適用域はclosureノートに記した。

規約照合には、Mahlburgの公式講義資料 Problems 6–7, Eq.(4)–(5)を用いた。原発見論文を取得したとはしない。[LSU講義資料](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2018-7230/HW8.pdf)

数学的内容は直接のconvolution/finite-difference計算で検算する。任意高次のmomentが非負というだけで原signed objectが非負になるわけでもない。例えば \(\delta_0-\delta_1+\delta_2\) の全非負整数monomial momentsは正だが測度は正でない。

## 5. random multiplicative functionsとentropy

HarperのRademacher modelは各素数で独立な \(\pm1\) を取り、squarefreeに乗法的に延長する確率モデル。low-moment theoremはその確率分布に対する期待値である。[Harper, §1.1 Theorem 2](https://arxiv.org/pdf/1703.06654)

actual \(\mu\) は全素数で値 \(-1\) を固定した一つのassignmentである。無限個の独立符号を全て \(-1\) とするeventの確率は0。有限prime cutoffでも確率は \(2^{-\pi(y)}\) であり、平均momentの小ささからこの一つのassignmentの値をboundできない。all-positive assignmentは大きい和を持つ。この区別はArithmetic Commaの同Haar-law/異readout反例とも整合する。

従ってrandom chaos theoryは未実装のtransfer theoremなしにはactual coefficient inputではない。random signs、Brownian scaling、prime independenceは診断上のheuristicとして分類し、候補に残さない。

Sarnakの原講義でも、Möbius disjointnessの \(o(N)\) とRH級の \(O_\epsilon(N^{1/2+\epsilon})\) は別に記される。[2011 Mahler講義](https://publications.ias.edu/sites/default/files/Mahler%20Colloquium%20Lecture%204%20-Mobius%20randomness%20and%20dynamics.pdf)

entropy decrementは平均相関定理の証明で重要な既知手法だが、「複雑だから小さい」という決定論的pointwise estimateではない。zero-entropy systemをこのclosure専用に新設していない。既知のorthogonalityを使うなら対象とquantifiersを一致させる必要があり、その監査はcorrelationノートに委ねる。

## 6. zero-side inputの隔離

今回引用した解析的証明によるPNT型評価・Vinogradov–Korobov型zero-free region・zero-density・Dirichlet \(L\)-functionのzero-free情報は、RHを仮定しない場合でも **analytic zero-side input** と記録する。coefficient側の独立な新情報と同一視しない。PNTには初等証明もあるため、PNTという名称だけであらゆる証明をzero-sideと分類しているのではない。

例えば既知の \(M(x)\ll_B x(\log x)^{-B}\) をGaussian部分積分へ入れると、\(A(u)\ll_B e^{u/2}u^{-B}\)。任意固定Bで成立しても、必要な \(\forall\epsilon>0\ O(e^{\epsilon u})\) にはならない。より強い既知のsubpower savingでも、正規化後の正の固定指数率を消せない。

「既知のzero-free regionより改善がない」という監査結果を、全ての未発見の係数側手法の不可能性に拡張しない。
