**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_restoring_force/notes/diagnostics_and_scope.md` · Original SHA-256: `14582cd8e7a52c5415faa4ff83e5ce6151e0bda320c097409a1d74e7f77c3055`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Scalar / theta診断の規約と適用限界

2026-09-30。有限数値は式と反例の点検だけに使う。RHや全域の符号の証明には使わない。

## 1. 数値結果

[再現スクリプト](../../../../../artifacts/research/arithmetic_restoring_force/experiments/check_scalar_theta.py) と [全結果](../../../../../artifacts/research/arithmetic_restoring_force/experiments/results.json) を保存した。mpmath 50桁、一部を80桁で照合。interval certificationではない。

- 零点から離れた点も含む \(a=\sigma-1/2\ne0\)、\(0\le t\le100\) の128点では、\(a\Re(\xi'/\xi)>0\) に反する点は見つからなかった。この有限事実から全域への主張はしない。
- 中心 \(a=0\) の16個のregularな標本では曲率は正だった。全 \(t\) の符号の証明ではない。
- 第一の既知critical-line零点のordinate近傍では、水平log曲率に負値が現れた。例えば \(a=0.1,t\approx14.1347251417\) で約 \(-99.9323338541\)。これは一般の零点局所展開による解析的反証と整合する。零点の単純性は一般証明の前提にしていない。
- theta二積分とcompleted \(\xi\) を5点で比較し、最大差は約 \(8.61\times10^{-52}\)。有限n和・有限積分域による診断であり、一般の積分恒等式の証明はthetaノートを参照する。
- \(\sigma=8\) で、prime-side対数微分は \(t=0\) で約 \(-0.00289016830805\)、\(t=\pi/\log2\) で約 \(+0.00265101738134\)。

数値でfirst-derivative lawを反証できなかったことと、独立な復元法則が証明されたことは別である。全域lawがRH同値であることが主要な終了理由。

## 2. Prime-sideの反対符号は解析的にも証明できる

\(\sigma>1\) では絶対収束で

\[
 \partial_\sigma\log|\zeta(\sigma+it)|
 =-\sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}\cos(t\log n).
\]

\(\sigma=8,t=0\) なら全非零項が負である。\(\sigma=8,t=\pi/\log2\) なら \(n=2\) 項は \(\log2/2^8>1/512\)。他の全項の絶対値は

\[
 \sum_{n\ge3}\frac{\log n}{n^8}
 \le \frac{\log3}{3^8}
       +3^{-7}\left(\frac{\log3}{7}+\frac1{49}\right)
 <\frac2{3^8}+3^{-7}\left(\frac27+\frac1{49}\right).
\]

ここでは減少関数のsum–integral比較、\(\Lambda(n)\le\log n\)、\(\log2>1/2,\log3<2\) だけを用いた。主項下界から尾の上界を引くとexact rational number

\[
 \frac{248273}{164602368}>0
\]

となる。従ってprime-side符号の不定性は有限数値に依存しない。completed \(\xi\) について同じ反例が成立するとはいわない。Gamma・pole-removal項を落としてはならない。

独立scalar監査には別に \(\sigma=4\) のより強い例も記録される。二つの例は同じ不足を示すもので、別候補へ数えない。

## 3. Horizontal curvatureと二次元potentialは別

零点のない近傍で \(\log|\xi(\sigma+it)|\) はharmonic:

\[
 \partial_\sigma^2 V+\partial_t^2 V=0.
\]

従って水平曲率が正でも、二次元でpositive-definiteなHessianを得たことにならない。特に \(s=1/2\) は対称性でgradientが0、actual theta kernelから水平曲率が正なので、二次元Hessianは正負一つずつのsaddleである。一般の \(1/2+it\) では水平微分0でも垂直微分は0とは限らず、二次元のcritical pointだと呼べない。

単純な水平復元力を定義してgradient flowを新たに置くことも、actual zerosがそのflowに従うこととは異なる。今回そのような人工的なdynamicsは導入しない。

## 4. Energy / Gaussian observableの再開条件

前トラックで固定した

\[
 A(u)=e^{-u/2}\sum_n\mu(n)e^{-(u-\log n)^2}
\]

をそのまま保持する。全域scalar符号から全零点実部 \(1/2\) が出れば、既存Gaussian criterionを介して準指数成長が出る。しかしその全域符号自体がRH同値で、新しい独立算術入力ではない。

既存 [Gaussianノート G7](../../global_remainder/notes/gaussian_global_decomposition.md) はactual \(A\notin L^2(\mathbb R)\) を無条件に確認している。従ってunweighted有限energyを再仮定しない。任意のweightを付ければ発散を隠せても、全zero modesの検出と必要なgrowth評価を保存したことにはならない。

\(\log|\xi(\sigma+it)|\) は \((\sigma,t)\) の関数であり、それをそのまま \(u\)-energyのpotentialへ挿入する算術恒等式は得ていない。新しいpositive metric、self-adjoint generator、weighted completion、Weil形式への置換は実施しない。

「電子の束縛」「重力」「復元力」は着想上の説明であり、数式の根拠・仮定・引用証拠として使用しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/arithmetic_restoring_force/experiments/check_scalar_theta.py`](../../../../../artifacts/research/arithmetic_restoring_force/experiments/check_scalar_theta.py)
- [`research/arithmetic_restoring_force/experiments/results.json`](../../../../../artifacts/research/arithmetic_restoring_force/experiments/results.json)
- [`research/global_remainder/notes/gaussian_global_decomposition.md`](../../global_remainder/notes/gaussian_global_decomposition.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_scalar_theta.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/results.json` — SOURCE REFERENCE NOT INCLUDED
