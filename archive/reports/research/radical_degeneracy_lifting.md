**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/radical_degeneracy_lifting.md` · Original SHA-256: `31791fff51d87e2e80fe6e9dc04a4b76d4ed7dc407642a1dd6ea3a0c42b81c25`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Actual radical の有限分裂

2026-09-30。RH OPEN。旧375ファイルは読取専用。
有限数値は漸近・正値性・RHの証明ではない。

## 1. 三種類のrateと線形化

\(\mathscr X(z)=\xi(1/2+iz)\)、\(\widehat f(z)=\int f(t)e^{-izt}dt\)。
固定familyは
\[
 f_j=k^{(2j)},\quad 0\le j\le m,\qquad
 \widehat f_j(z)=(-1)^jz^{2j}\mathscr X(z)/4.
\]
actual global Weil形式の適切なtest-space拡張上で
\(Q_W(f_j,g)=0\)。RHを仮定せず、旧監査のradical事実を用いる。
今回の有限実現は
\[
 a=\log\lambda,\quad R_a=1_{[-a,a]},\quad
 L_{a,N}=P_NR_a,\quad b_j=L_{a,N}f_j/\|L_{a,N}f_j\|_2 .
\]
正規化前の \(L_{a,N}\) は線形だが、unit normalizationは線形でない。
正規化した列を \(S=(b_0,\ldots,b_m)\) と書き
\[
 G=S^*S,\quad M=S^*Q_{\lambda,N}S,\quad
 \mathcal R(c)=\frac{c^*Mc}{c^*Gc}.
\tag{1}
\]
個々の列のunit normalizationを行ってもspanは同じ。
generalized eigenproblemは \(Mc=\mu Gc\)。
元のraw derivative basisでの係数は \(c_j/\|L_{a,N}f_j\|\) であり、
正規化後の係数をそのままglobal組合せの係数にしない。

Rate Aは \(D(f)=Q_W(Lf,Lf)/\|Lf\|^2\) のradical recognition。
Rate Bは \(D(f)-e_0\) と、ground proximityならさらにfull gapで割った量。
Rate Cは規格化Fourier transformの \(\mathscr X\) への接近。
signed energy、absolute energy、ground excessを同一視しない。
indefinite形式ではRayleigh値0の組合せが連続的に存在し得るので、
「絶対値が最も小さい固有値」を最速absolute-score状態と定義しても一般には誤る。

## 2. actual kernelからの直接計算

\(t\ge0,\ y_n=\pi n^2e^{2t}\) として
\[
 k(t)=e^{t/2}\sum_{n\ge1}(y_n^2-\tfrac32y_n)e^{-y_n},\qquad k(-t)=k(t).
\tag{2}
\]
多項式を
\[
 P_0(y)=y^2-\tfrac32y,\quad
 P_{r+1}(y)=(\tfrac12-2y)P_r(y)+2yP_r'(y)
\]
とすれば \(f_j(t)=e^{t/2}\sum P_{2j}(y_n)e^{-y_n}\)。
zero ordinatesや零点位置は計算入力に使わない。

有限基底
\[
 V_n(t)=(-1)^n e^{i\pi nt/a}/\sqrt{2a}
\]
に対する列係数を偶性から
\[
 B_{nj}=\frac{2(-1)^n}{\sqrt{2a}}\int_0^a f_j(t)\cos(\pi nt/a)\,dt
\tag{3}
\]
として計算した。Qは既存の独立Arb prime/Gamma/pole組立てをread-onlyで利用する。
GramをCholesky \(G=LL^*\) でwhitenし、
\(L^{-1}ML^{-*}\) を対角化、係数を \(L^{-*}\) で戻す。
Gを無視した通常のM固有vectorは使わない。

## 3. Step31を実行した範囲

- \(m=1,2,3\)。
- \(\lambda^2=9,25,49,81,121,169\)。
- 二経路 \(N_2(a)=\max(4,\lceil a^2\rceil)\)、
  \(N_3(a)=\max(4,\lceil a^3\rceil)\)。双方 \(N/a\to\infty\)。
- 重複を除き11組、restricted problemsは33組。
- Q：448-bit Arb assemblyのmidpoint。固有解析：mpmath100桁。
- theta積分：Gauss 144点と192点を比較。
- global方向の診断用Gram：区間 \([-4,4]\)、192点と256点を比較。
- prolate比較：前trackのraw proxy構成をread-only再利用。
  Legendre192→256、区分求積32→48で比較。

これはinterval certificateではない。高精度固有残差は、Q組立て・quadrature・proxy全誤差の保証ではない。
theta列の求積変動は最大約 \(6.2\,10^{-51}\)、global Gram変動は約 \(4.0\,10^{-37}\)。
prolate比較の最大解像度変動はprojective distance約 \(1.05\,10^{-5}\)。
Gram conditionは最大約1936であり、100桁という表示だけを根拠に安全性を主張しない。

再現scriptと全M/Gは
[splitting_probe.py](../../../artifacts/research/rate_history/experiments/splitting_probe.py)、
[splitting_results.json](../../../artifacts/research/rate_history/experiments/splitting_results.json)。
既存実験結果は上書きしていない。

## 4. 同点は有限では分裂する

以下は \(m=3\) の最低generalized eigenvalue \(\mu_0^{(3)}\)。
overlapは二乗で、global derivative係数から元のlog-spaceで比較した。

| \(\lambda\) | \(N\) | k単独のR | \(\mu_0^{(3)}\) | 選択組合せとglobal k | 選択組合せとfinite ground |
|---:|---:|---:|---:|---:|---:|
|3|4|\(2.44125\,10^{-7}\)|\(2.33155\,10^{-13}\)|0.977842|0.999992|
|7|8|\(5.18907\,10^{-7}\)|\(1.78213\,10^{-17}\)|0.971739|0.980023|
|13|7|\(8.07733\,10^{-5}\)|\(2.32968\,10^{-17}\)|0.892770|0.967642|
|13|17|\(9.53631\,10^{-12}\)|\(1.41541\,10^{-21}\)|0.993463|0.961262|

最後の行のglobal単位norm係数はおよそ
\[
 7.49151\,k+0.04585997\,k''+
 9.39774\,10^{-5}k^{(4)}+6.44929\,10^{-8}k^{(6)}.
\]
先頭係数を1に揃えると \(k+0.00612159\,k''+\cdots\)。
有限の最小方向はkそのものではない。
この小さいderivative係数だけから、その極限がkだと証明しない。

同じ最後の例で
\[
 \mu_0^{(1)}\simeq4.99940\,10^{-15},\quad
 \mu_0^{(2)}\simeq1.99334\,10^{-18},\quad
 \mu_0^{(3)}\simeq1.41541\,10^{-21}.
\]
固定有限問題でspanを広げればRitz最小値は下がる。
このm方向の改善を \((\lambda,N)\) のrateや \(m\to\infty\) の定理と混同しない。

## 5. groundとの隔たり

\(\lambda=13,N=17\) のfull ground値は約 \(9.66\,10^{-59}\)、full gapは
\(1.44\,10^{-55}\)。
restricted最小値とfull groundのexcess/gapは約 \(9.80\,10^{33}\)。
したがって小さいrestricted scoreでも、前trackのgap補題によるground認証には届かない。
大きい比は距離の下界ではなく、実測overlap約0.961とも矛盾しない。

同例でfull groundの \(\mathcal R_3\) 有限像への射影量は約0.999905。
subspaceには非常に近くても、その中のRitz最低方向がgroundに同程度近いとは限らない。
極小gapに対する補空間couplingの制御が別に必要である。

prolateとの比較も記録した。最後のrestricted最小方向とのoverlap²は約0.993194。
これはraw proxyの有限診断であり、proxy→Xiやground→proxyのrateを証明したものではない。

## 6. defectの分解と二重計上の防止

\(e=R_af-f\)、\(d=(P_N-I)R_af\) とする。
global radical identityを使うと正確に
\[
 Q_W(P_NR_af)=Q_W(e+d,e+d)
 =Q_W(e,e)+2\Re Q_W(e,d)+Q_W(d,d).
\tag{4}
\]
項間の符号相殺を捨てない。nonnegative error budgetsだと仮定しない。
unit normalizationはこの右辺全体を \(\|P_NR_af\|^2\) で割る。

support内の関数の相関は距離 \(2a\) より外で0なので、
Qのprime cutoff \(p^k\le e^{2a}\) はそのsupportに対してexact。
「missing primes beyond \(\lambda^2\)」という独立の形式誤差をさらに加えるのは二重計上。
global tailを使う(4)の側では、全prime項とGamma/pole項を保持する。

## 7. Rate C は独立

固定 \(f=\sum c_jf_j\) について
\[
 \widehat f(z)=P_c(z)\mathscr X(z)/4,\qquad
 P_c(z)=\sum c_j(-1)^jz^{2j}.
\]
例えば旧監査と同じ \(z_*=i/4\) を使い \(P_c(z_*)\ne0\) なら
\[
 \frac{\widehat f(z)}{\widehat f(z_*)}
 =\frac{P_c(z)}{P_c(z_*)}
  \frac{\mathscr X(z)}{\mathscr X(z_*)}.
\]
全radical状態は零点を消すが、同じXi関数を再現するわけではない。
固定mで \(\mathscr X\) と同じ規格化極限を得るにはpoly factorが定数へ行く必要がある。
さらに有限像からglobal transformへは、拡大窓の評価損失を含む比較が要る。
L² normやenergyだけをG*へ読み替えない。

## 8. 支持切断に対する解析的rate

\(Y=\pi e^{2a}=\pi\lambda^2\)、\(A_j=f_j(a)\) と置く。
actual theta展開とWeil形式の全成分から、固定jについて
\[
 A_j\sim4^j\pi^{-1/4}Y^{2j+9/4}e^{-Y},\qquad
 Q_W(R_af_j)=\frac{A_j^2}{2Y}[2a+o(1)].
\]
従って
\[
 Q_W(R_af_j)\sim\frac{a16^j}{\sqrt\pi}
                 Y^{4j+7/2}e^{-2Y}.
\tag{5}
\]
単位normのscoreではさらに \(\|f_j\|_2^{-2}\) を掛ける。
共通のsuper-exponential因子は同じだが、polynomial prefactorは異なる。
これは単なるtail normでなく、actual Weil scoreの漸近である。
Archimedean項が主項、全prime/pole項はこの精度で下位と評価した。
[完全な導出とdomain](rate_history/notes/boundary_rate_analysis.md)。

しかし組合せを許すと先頭行列はrank one：
\[
 \frac{Y}{a}\operatorname{diag}(A_j)^{-1}
 [Q_W(R_af_i,R_af_j)]
 \operatorname{diag}(A_j)^{-1}
 \longrightarrow{\bf1}{\bf1}^*.
\tag{6}
\]
先頭の採点対象は境界値であり、零空間が残る。
例えば
\[
 g_a=k-\frac{k(a)}{k''(a)}k'',\quad
 \frac{k(a)}{k''(a)}\sim\frac1{4Y^2},\quad g_a\to k\text{ in }L^2
\]
は境界値をexactに消し、
\[
 \frac{Q_W(R_ag_a)}{Q_W(R_ak)}\sim\frac2{Y^2}.
\tag{7}
\]
有限aでk単独より速く0へ近づくが、その例自体のglobal方向はkへ近づく。
「混合状態が勝つ」ことと「kが極限ではない」ことを同一視しない。
また(6)から一意な全次次数selectorを導いてはいない。

ただしm=1の二候補については、raw固定basisで
\[
 s_a=(a/Y)A_1^2,\quad M_a/s_a\to\operatorname{diag}(0,1),\quad G_a\to G_\infty>0
\]
なので、whitened limitの最低固有値0は単純である。
従ってrestricted support-only groundの方向はkへ収束し、
gapは \(s_a(G_\infty^{-1})_{11}\) と漸近的に等しい（添字0,1）。
この限定選択結果は、上記P_N付き数値problemの極限を証明したものではない。

## 9. 解析的なrateの範囲

有限Fourier射影まで含むraw matrix全成分には
\[
 |M_{ij}|\le C_m\left[
 a(1+\Omega)^{4m+8}e^{a-\pi\Omega/2}
 +\lambda^{8m+24}e^{-2\pi\lambda^2}\right],
 \qquad \Omega=\pi(N+1)/a
\]
という無条件上界を得た。
[導出](rate_history/notes/full_projection_upper_bound.md)は実軸Fourier decay、
weighted BV、actual明示公式から成り、単なるL²形式連続性の仮定ではない。
指定二経路で固定mの全Ritz値が0へ行くことも従う。
support漸近・boundary cancellationと、このfull-system上界を分離して記録する。
支持だけの \(N\to\infty\) 先行極限と、上記二つのcofinal pathsは同一でない。
異なる正規化・m・pathを混ぜたgrowth fitは行わない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/rate_history/experiments/splitting_probe.py`](../../../artifacts/research/rate_history/experiments/splitting_probe.py)
- [`research/rate_history/experiments/splitting_results.json`](../../../artifacts/research/rate_history/experiments/splitting_results.json)
- [`research/rate_history/notes/boundary_rate_analysis.md`](rate_history/notes/boundary_rate_analysis.md)
- [`research/rate_history/notes/full_projection_upper_bound.md`](rate_history/notes/full_projection_upper_bound.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/splitting_probe.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/splitting_results.json` — SOURCE REFERENCE NOT INCLUDED
